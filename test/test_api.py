from ._common import unittest, mock
import os
from assembla import api, models


@mock.patch.object(api.requests, 'get', spec=True)
class BindingTest(unittest.TestCase):
    def _make_uri(self, *args):
        params = ['{0}/{{{0}_id}}'.format(param) for param in args]
        return '/{0}'.format('/'.join(params))

    def _make_url(self, uri, **kwargs):
        return 'https://api.assembla.com' + uri.format(**kwargs)

    def _get_url(self, mock):
        args, _ = mock.call_args
        return args[0]

    def _get_headers(self, mock):
        _, kwargs = mock.call_args
        return kwargs['headers']

    def setUp(self):
        self.api = api.API()

    def test_check_uri(self, request):
        self.assertTrue(self.api._check_uri(self._make_uri('space'), ['space_id']))
        self.assertTrue(self.api._check_uri(self._make_uri('space', 'milestone'), ['space_id', 'milestone_id']))
        self.assertFalse(self.api._check_uri(self._make_uri('space'), ['space_id, milestone_id']))
        self.assertFalse(self.api._check_uri(self._make_uri('space', 'milestone'), ['space_id']))

    def test_uri(self, request):
        uri = self._make_uri('space')
        space_id = 'axk9jBJ64'

        handler = self.api.bind(uri=uri, model=models.Model)
        handler(space_id=space_id)
        self.assertEqual(self._get_url(request), self._make_url(uri, space_id=space_id))

    def test_multi_uri(self, request):
        uri = []
        uri.append(self._make_uri('space'))
        uri.append(self._make_uri('space', 'milestone'))
        space_id = 'axk9jBJ64'
        milestone_id = 1

        handler = self.api.bind(uri=uri, model=models.Model)

        handler(space_id=space_id)
        self.assertEqual(self._get_url(request), self._make_url(uri[0], space_id=space_id))

        handler(space_id=space_id, milestone_id=milestone_id)
        self.assertEqual(self._get_url(request), self._make_url(uri[1], space_id=space_id, milestone_id=milestone_id))

    def test_headers(self, request):
        handler = self.api.bind(uri='/', model=models.Model)
        headers = {'X-Api-Key': os.environ.get('ASSEMBLA_KEY', ''), 'X-Api-Secret': os.environ.get('ASSEMBLA_KEY', '')}
        handler()
        self.assertEqual(self._get_headers(request), headers)

        handler = api.API(key='some-key', secret='some-secret').bind(uri='/', model=models.Model)
        headers = {'X-Api-Key': 'some-key', 'X-Api-Secret': 'some-secret'}
        handler()
        self.assertEqual(self._get_headers(request), headers)

    def test_auth(self, request):
        response = mock.Mock()
        response.status_code = 401
        request.return_value = response

        handler = self.api.bind(uri='/', model=models.Model)
        self.assertRaises(api.AuthenticationError, handler)

    def test_param_count(self, request):
        handler = self.api.bind(uri='/', model=models.Model)
        self.assertRaises(api.ParamCountError, handler, space_id=1)

        handler = self.api.bind(uri=self._make_uri('space'), model=models.Model)
        self.assertRaises(api.ParamCountError, handler)


def suite():
    return unittest.TestLoader().loadTestsFromName(__name__)

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
