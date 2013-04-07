import re


def uri_params(uri):
    params = [param.strip('{}') for param in re.compile('{\w+}').findall(uri)]
    return params
