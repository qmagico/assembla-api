import requests
import os
import models


class MissingParamException(Exception):
    pass


def bind(**config):
    def handler(**kwargs):
        key = os.environ['ASSEMBLA_KEY']
        secret = os.environ['ASSEMBLA_SECRET']
        headers = {'X-Api-Key': key, 'X-Api-Secret': secret}

        try:
            uri = config['uri'].format(**kwargs)
        except KeyError as e:
            raise MissingParamException('Missing param \'{0}\' to get the assembla object'.format(e.message))
        r = requests.get('https://api.assembla.com/{0}'.format(uri), headers=headers)
        if config.get('is_list', False):
            return config['model'].parse_list(r.json())
        return config['model'].parse(r.json())

    return handler


class API(object):
    def __init__(self):
        self.spaces = bind(
            uri='/v1/spaces.json',
            model=models.Space,
            is_list=True
        )

        self.space = bind(
            uri='/v1/spaces/{id}.json',
            model=models.Space
        )

        self.tickets = bind(
            uri='/v1/spaces/{space_id}/tickets.json',
            model=models.Ticket,
            is_list=True
        )
