from ._common import unittest
from assembla import binder, models


def _make_uri(*args):
    params = ['{0}/{{{0}_id}}'.format(param) for param in args]
    return '/{0}'.format('/'.join(params))


class MockRequest(object):
    def __init__(self, test_case, uri):
        self.test_case = test_case
        self.url = 'https://api.assembla.com{0}'.format(uri)

    def get(self, url, **kwargs):
        return MockResponse()


class MockResponse(object):
    def json(self):
        return {}


class BinderTest(unittest.TestCase):
    def setUp(self):
        self.binder = binder.Binder()

    def test_uri(self):
        uri = _make_uri('space')
        space_id = 'axk9jBJ64'

        handler = self.binder.bind(uri=uri, model=models.Model)
        binder.requests.get = MockRequest(self, uri.format(space_id=space_id)).get
        handler(space_id=space_id)

    def test_multi_uri(self):
        uri = []
        uri.append(_make_uri('space'))
        uri.append(_make_uri('space', 'milestone'))
        space_id = 'axk9jBJ64'
        milestone_id = 1

        handler = self.binder.bind(uri=uri, model=models.Model)
        binder.requests.get = MockRequest(self, uri[0].format(space_id=space_id)).get
        handler(space_id=space_id)

        handler = self.binder.bind(uri=uri, model=models.Model)
        binder.requests.get = MockRequest(self, uri[1].format(space_id=space_id, milestone_id=milestone_id)).get
        handler(space_id=space_id, milestone_id=milestone_id)


def suite():
    return unittest.TestLoader().loadTestsFromName(__name__)

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
