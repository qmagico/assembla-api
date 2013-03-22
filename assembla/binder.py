import os
import requests
from string import Formatter


_key = os.environ.get('ASSEMBLA_KEY', '')
_secret = os.environ.get('ASSEMBLA_SECRET', '')


class ParamCountError(Exception):
    pass


def _check_params(uri, fields):
    parser = Formatter().parse(uri)
    for _, field_name, _, _ in parser:
        if field_name and field_name not in fields:
            return False
        fields.remove(field_name)
    if len(fields) > 0:
        return False
    return True


def _fetch_object(uri, model):
    headers = {'X-Api-Key': _key, 'X-Api-Secret': _secret}
    response = requests.get('https://api.assembla.com{0}'.format(uri), headers=headers)

    if isinstance(response.json(), list):
        return model.parse_list(response.json())
    return model.parse(response.json())


def bind(**config):
    def handler(**kwargs):
        if not _check_params(config['uri'], list(kwargs)):
            raise ParamCountError()

        return _fetch_object(config['uri'].format(**kwargs), config['model'])

    def handler_multi(**kwargs):
        for uri in config['uri']:
            if _check_params(uri, list(kwargs)):
                return _fetch_object(uri.format(**kwargs), config['model'])

        raise ParamCountError()

    if isinstance(config['uri'], list):
        return handler_multi
    return handler
