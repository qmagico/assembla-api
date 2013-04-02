import os
import requests

from assembla import models, exceptions
from test import util


class API(object):
    def __init__(self, key=None, secret=None):
        self.key = key or os.environ.get('ASSEMBLA_KEY', '')
        self.secret = secret or os.environ.get('ASSEMBLA_SECRET', '')

        self.spaces = self.bind(
            uri='/v1/spaces.json',
            model=models.Space)

        self.space = self.bind(
            uri='/v1/spaces/{id}.json',
            model=models.Space)

        self.tickets = self.bind(
            uri=['/v1/spaces/{space_id}/tickets.json', '/v1/spaces/{space_id}/tickets/milestone/{milestone_id}.json'],
            model=models.Ticket)

        self.ticket_status = self.bind(
            uri='/v1/spaces/{space_id}/tickets/statuses/{id}',
            model=models.TicketStatus)

        self.milestones = self.bind(
            uri=['/v1/spaces/{space_id}/milestones/all'],
            model=models.Milestone)

        self.user = self.bind(
            uri=['/v1/users/{id}.json', '/v1/users/{login}.json'],
            model=models.User)

        self.users = self.bind(
            uri='/v1/spaces/{space_id}/users.json',
            model=models.User)

    def _validate(self, uri_list):
        all_params = []
        for uri in uri_list:
            params = util.uri_params(uri)
            if len(set(params)) != len(params):
                raise exceptions.URIError('Duplicate params')

            if set(params) in all_params:
                raise exceptions.URIError('More than 1 URI with the same params')
            all_params.append(set(params))

    def _check_uri(self, uri, fields):
        params = util.uri_params(uri)

        if len(params) != len(fields):
            return False

        for param in params:
            if param not in fields:
                return False
        return True

    def _fetch(self, uri, model):
        headers = {'X-Api-Key': self.key, 'X-Api-Secret': self.secret}
        response = requests.get('https://api.assembla.com{0}'.format(uri), headers=headers)

        if response.status_code == 401:
            raise exceptions.AuthenticationError('Authentication Failed')

        if isinstance(response.json(), list):
            return model.instantiate_many(response.json(), self)
        return model.instantiate_one(response.json(), self)

    def bind(self, **config):
        uri_list = config['uri'] if isinstance(config['uri'], list) else [config['uri']]
        self._validate(uri_list)

        def handler(**kwargs):
            uri = [uri for uri in uri_list if self._check_uri(uri, kwargs.keys())]

            if len(uri) != 1:
                raise exceptions.ParamCountError()
            return self._fetch(uri[0].format(**kwargs), config['model'])

        return handler
