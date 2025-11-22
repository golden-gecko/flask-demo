import requests

from urllib.parse import urlencode


def make_url(host: str, params: list = None, query: dict = None) -> str:
    if params:
        params = [str(x) for x in params]

    if query:
        return '{}/{}?{}'.format(host, '/'.join(params), urlencode(query))
    else:
        return '{}/{}'.format(host, '/'.join(params))


def make_api_url(host: str, version: str, params: list = None, query: dict = None) -> str:
    api_params = [version]
    api_params.extend(params)

    return make_url(host=host, params=api_params, query=query)


class Api:
    def __init__(self, host: str, version: str = 'v1'):
        self.host = host
        self.version = version

    def is_alive(self):
        return requests.get(make_api_url(self.host, self.version, ['healthcheck']))
