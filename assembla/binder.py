import os
import requests


_key = os.environ.get('ASSEMBLA_KEY', '')
_secret = os.environ.get('ASSEMBLA_SECRET', '')


class ParamCountError(Exception):
    pass


def _check_params(uri, fields):
    for _, field_name, _, _ in uri._formatter_parser():
        if field_name and field_name not in fields:
            return False
        fields.remove(field_name)
    if len(fields) > 0:
        return False
    return True


def _fetch_object(uri, model, getter):
    headers = {'X-Api-Key': _key, 'X-Api-Secret': _secret}
    response = getter('https://api.assembla.com{0}'.format(uri), headers=headers)

    if isinstance(response.json(), list):
        return model.parse_list(response.json())
    return model.parse(response.json())


def bind(**config):
    def handler(**kwargs):
        if not _check_params(config['uri'], kwargs.keys()):
            raise ParamCountError()

        return _fetch_object(config['uri'].format(**kwargs), config['model'], config.get('getter', requests.get))

    def handler_multi(**kwargs):
        for uri in config['uri']:
            if _check_params(uri, kwargs.keys()):
                return _fetch_object(uri.format(**kwargs), config['model'], config.get('getter', requests.get))

        raise ParamCountError()

    if isinstance(config['uri'], list):
        return handler_multi
    return handler
