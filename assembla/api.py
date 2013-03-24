import os
import re
import requests
from . import models


class AuthenticationError(Exception):
    pass


class ParamCountError(Exception):
    pass


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

        self.user = self.bind(
            uri=['/v1/users/{user_id}.json', '/v1/users/{user_login}.json'],
            model=models.User)

        self.users = self.bind(
            uri='/v1/spaces/{space_id}/users.json',
            model=models.User)

    def _check_uri(self, uri, fields):
        params = [param.strip('{}') for param in re.compile('{\w+}').findall(uri)]

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
            raise AuthenticationError('Authentication Failed')

        if isinstance(response.json(), list):
            return model.parse_list(response.json())
        return model.parse(response.json())

    def bind(self, **config):
        def handler(**kwargs):
            uri_list = config['uri'] if isinstance(config['uri'], list) else [config['uri']]
            uri = [uri for uri in uri_list if self._check_uri(uri, kwargs.keys())]

            if len(uri) != 1:
                raise ParamCountError()
            return self._fetch(uri[0].format(**kwargs), config['model'])

        return handler
