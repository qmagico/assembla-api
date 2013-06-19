try:
    import mock
except ImportError:
    from unittest import mock

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from . import util
from assembla import api, models, exceptions


def _make_uri(*args):
    params = ['{0}/{{{0}_id}}'.format(param) for param in args]
    return '/{0}'.format('/'.join(params))


def _make_url(uri, **kwargs):
    return 'https://api.assembla.com' + uri.format(**kwargs)


@mock.patch.object(api.requests, 'get', spec=True)
class BindingTest(unittest.TestCase):
    def setUp(self):
        self.api = api.API()

    def test_check_uri(self, request):
        self.assertTrue(self.api._check_uri(_make_uri('space'), ['space_id']))
        self.assertTrue(
            self.api._check_uri(
                _make_uri('space', 'milestone'),
                ['space_id', 'milestone_id']
            )
        )
        self.assertFalse(self.api._check_uri(_make_uri('space'), ['space_id, milestone_id']))
        self.assertFalse(self.api._check_uri(_make_uri('space', 'milestone'), ['space_id']))

    def test_uri(self, request):
        uri = _make_uri('space')
        space_id = 'axk9jBJ64'

        handler = self.api.bind(uri=uri, model=models.Model)
        handler(space_id=space_id)
        self.assertEqual(util.request_call(request)[0], _make_url(uri, space_id=space_id))

    def test_multi_uri(self, request):
        uri = []
        uri.append(_make_uri('space'))
        uri.append(_make_uri('space', 'milestone'))
        space_id = 'axk9jBJ64'
        milestone_id = 1

        handler = self.api.bind(uri=uri, model=models.Model)

        handler(space_id=space_id)
        self.assertEqual(util.request_call(request)[0], _make_url(uri[0], space_id=space_id))

        handler(space_id=space_id, milestone_id=milestone_id)
        self.assertEqual(
            util.request_call(request)[0],
            _make_url(uri[1], space_id=space_id, milestone_id=milestone_id)
        )

    def test_headers(self, request):
        handler = self.api.bind(uri='/', model=models.Model)
        headers = {'X-Api-Key': None, 'X-Api-Secret': None}
        handler()
        self.assertEqual(util.request_call(request)[1], headers)

        handler = api.API(key='some-key', secret='some-secret').bind(uri='/', model=models.Model)
        headers = {'X-Api-Key': 'some-key', 'X-Api-Secret': 'some-secret'}
        handler()
        self.assertEqual(util.request_call(request)[1], headers)

    def test_auth(self, request):
        response = mock.Mock()
        response.status_code = 401
        request.return_value = response

        handler = self.api.bind(uri='/', model=models.Model)
        self.assertRaises(exceptions.AuthenticationError, handler)

    def test_param_count(self, request):
        handler = self.api.bind(uri='/', model=models.Model)
        self.assertRaises(exceptions.ParamCountError, handler, space_id=1)

        handler = self.api.bind(uri=_make_uri('space'), model=models.Model)
        self.assertRaises(exceptions.ParamCountError, handler)

    def test_duplicate_params(self, request):
        self.assertRaises(exceptions.URIError, self.api.bind, uri='/{space}/{user}/{space}', model=models.Model)

    def test_duplicate_uri_params(self, request):
        self.assertRaises(
            exceptions.URIError,
            self.api.bind,
            uri=['/{space}/user/{user}', '/{user}/space/{space}'],
            model=models.Model
        )


@mock.patch.object(api.requests, 'get')
class APITest(unittest.TestCase):
    def setUp(self):
        self.api = api.API()

    def test_api_error_response(self, request):
        request.return_value = util.make_response({'error': 'Message'})
        self.assertRaises(exceptions.APIError, self.api.ticket, space_id='1', id='1')

    def test_spaces(self, request):
        request.return_value = util.make_response([{}, {}])
        spaces = self.api.spaces()
        self.assertIsInstance(spaces, list)
        for space in spaces:
            self.assertIsInstance(space, models.Space)

    def test_space(self, request):
        request.return_value = util.make_response({})
        space = self.api.space(id=1)
        self.assertIsInstance(space, models.Space)

    def test_tickets(self, request):
        request.return_value = util.make_response([{}, {}])
        tickets = self.api.tickets(space_id=1)
        self.assertIsInstance(tickets, list)
        for ticket in tickets:
            self.assertIsInstance(ticket, models.Ticket)

    def test_ticket(self, request):
        request.return_value = util.make_response({})
        ticket = self.api.ticket(space_id=1, id=1)
        self.assertIsInstance(ticket, models.Ticket)

    def test_task(self, request):
        request.return_value = util.make_response([{}, {}])

        # _from because from is a reserved word
        tasks = self.api.tasks(_from='12-12-2012', to='24-12-2012')
        self.assertIsInstance(tasks, list)
        for task in tasks:
            self.assertIsInstance(task, models.Task)
