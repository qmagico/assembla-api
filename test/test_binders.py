from ._common import unittest, MockBase
from assembla import binder, models


def _make_uri(*args):
    params = ['{0}/{{{0}_id}}'.format(param) for param in args]
    return '/{0}'.format('/'.join(params))


class MockRequest(MockBase):
    def get(self, url, **kwargs):
        self.uri = '/' + url.split('/', 3)[3]
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
        with MockRequest() as binder.requests:
            handler(space_id=space_id)
            self.assertEqual(binder.requests.uri, uri.format(space_id=space_id))

    def test_multi_uri(self):
        uri = []
        uri.append(_make_uri('space'))
        uri.append(_make_uri('space', 'milestone'))
        space_id = 'axk9jBJ64'
        milestone_id = 1

        handler = self.binder.bind(uri=uri, model=models.Model)
        with MockRequest() as binder.requests:
            handler(space_id=space_id)
            self.assertEqual(binder.requests.uri, uri[0].format(space_id=space_id))

            handler(space_id=space_id, milestone_id=milestone_id)
            self.assertEqual(binder.requests.uri, uri[1].format(space_id=space_id, milestone_id=milestone_id))


def suite():
    return unittest.TestLoader().loadTestsFromName(__name__)

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
