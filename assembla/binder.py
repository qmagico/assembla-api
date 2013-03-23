import re
import requests


class ParamCountError(Exception):
    pass


class Binder(object):
    def __init__(self, key='', secret=''):
        self.key = key
        self.secret = secret

    def __fetch(self, uri, model):
        headers = {'X-Api-Key': self.key, 'X-Api-Secret': self.secret}
        response = requests.get('https://api.assembla.com{0}'.format(uri), headers=headers)

        if isinstance(response.json(), list):
            return model.parse_list(response.json())
        return model.parse(response.json())

    def __check_params(self, uri, fields):
        params = [param.strip('{}') for param in re.compile('{\w+}').findall(uri)]

        if len(params) != len(fields):
            return False

        for param in params:
            if param not in fields:
                return False
            fields.remove(param)

        return True

    def bind(self, **config):
        def handler(**kwargs):
            if not self.__check_params(config['uri'], list(kwargs)):
                raise ParamCountError()

            return self.__fetch(config['uri'].format(**kwargs), config['model'])

        def handler_multi(**kwargs):
            for uri in config['uri']:
                if self.__check_params(uri, list(kwargs)):
                    return self.__fetch(uri.format(**kwargs), config['model'])

            raise ParamCountError()

        if isinstance(config['uri'], list):
            return handler_multi
        return handler
