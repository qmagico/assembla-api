import os

from test import unittest, mock
from assembla import api, models


def _make_uri(*args):
    params = ['{0}/{{{0}_id}}'.format(param) for param in args]
    return '/{0}'.format('/'.join(params))


def _make_url(uri, **kwargs):
    return 'https://api.assembla.com' + uri.format(**kwargs)


def _get_url(mock):
    args, _ = mock.call_args
    return args[0]


def _get_headers(mock):
    _, kwargs = mock.call_args
    return kwargs['headers']


@mock.patch.object(api.requests, 'get', spec=True)
class BindingTest(unittest.TestCase):
    def setUp(self):
        self.api = api.API()

    def test_check_uri(self, request):
        self.assertTrue(self.api._check_uri(_make_uri('space'), ['space_id']))
        self.assertTrue(self.api._check_uri(_make_uri('space', 'milestone'), ['space_id', 'milestone_id']))
        self.assertFalse(self.api._check_uri(_make_uri('space'), ['space_id, milestone_id']))
        self.assertFalse(self.api._check_uri(_make_uri('space', 'milestone'), ['space_id']))

    def test_uri(self, request):
        uri = _make_uri('space')
        space_id = 'axk9jBJ64'

        handler = self.api.bind(uri=uri, model=models.Model)
        handler(space_id=space_id)
        self.assertEqual(_get_url(request), _make_url(uri, space_id=space_id))

    def test_multi_uri(self, request):
        uri = []
        uri.append(_make_uri('space'))
        uri.append(_make_uri('space', 'milestone'))
        space_id = 'axk9jBJ64'
        milestone_id = 1

        handler = self.api.bind(uri=uri, model=models.Model)

        handler(space_id=space_id)
        self.assertEqual(_get_url(request), _make_url(uri[0], space_id=space_id))

        handler(space_id=space_id, milestone_id=milestone_id)
        self.assertEqual(_get_url(request), _make_url(uri[1], space_id=space_id, milestone_id=milestone_id))

    def test_headers(self, request):
        handler = self.api.bind(uri='/', model=models.Model)
        headers = {'X-Api-Key': os.environ.get('ASSEMBLA_KEY', ''), 'X-Api-Secret': os.environ.get('ASSEMBLA_SECRET', '')}
        handler()
        self.assertEqual(_get_headers(request), headers)

        handler = api.API(key='some-key', secret='some-secret').bind(uri='/', model=models.Model)
        headers = {'X-Api-Key': 'some-key', 'X-Api-Secret': 'some-secret'}
        handler()
        self.assertEqual(_get_headers(request), headers)

    def test_auth(self, request):
        response = mock.Mock()
        response.status_code = 401
        request.return_value = response

        handler = self.api.bind(uri='/', model=models.Model)
        self.assertRaises(api.AuthenticationError, handler)

    def test_param_count(self, request):
        handler = self.api.bind(uri='/', model=models.Model)
        self.assertRaises(api.ParamCountError, handler, space_id=1)

        handler = self.api.bind(uri=_make_uri('space'), model=models.Model)
        self.assertRaises(api.ParamCountError, handler)


def _make_response(return_value):
    response = mock.Mock()
    response.status_code = 200
    response.json = mock.Mock()
    response.json.return_value = return_value
    return response


@mock.patch.object(api.requests, 'get')
class APITest(unittest.TestCase):
    def setUp(self):
        self.api = api.API()

    def test_spaces(self, request):
        request.return_value = _make_response([{}, {}])
        spaces = self.api.spaces()
        self.assertTrue(isinstance(spaces, list))
        for space in spaces:
            self.assertTrue(isinstance(space, models.Space))

    def test_space(self, request):
        request.return_value = _make_response({})
        space = self.api.space(space_id=1)
        self.assertTrue(isinstance(space, models.Space))

    def test_tickets(self, request):
        request.return_value = _make_response([{}, {}])
        tickets = self.api.tickets(space_id=1)
        self.assertTrue(isinstance(tickets, list))
        for ticket in tickets:
            self.assertTrue(isinstance(ticket, models.Ticket))
