from ._common import unittest, mock
from assembla import binder, models


def _make_uri(*args):
    params = ['{0}/{{{0}_id}}'.format(param) for param in args]
    return '/{0}'.format('/'.join(params))


def _make_url(uri, **kwargs):
    return 'https://api.assembla.com' + uri.format(**kwargs)


def _get_url(mock):
    args, _ = mock.call_args
    return args[0]


@mock.patch.object(binder.requests, 'get', spec=True)
class BinderTest(unittest.TestCase):
    def setUp(self):
        self.binder = binder.Binder()

    def test_uri(self, mock):
        uri = _make_uri('space')
        space_id = 'axk9jBJ64'

        handler = self.binder.bind(uri=uri, model=models.Model)
        handler(space_id=space_id)
        self.assertEqual(_get_url(mock), _make_url(uri, space_id=space_id))

    def test_multi_uri(self, mock):
        uri = []
        uri.append(_make_uri('space'))
        uri.append(_make_uri('space', 'milestone'))
        space_id = 'axk9jBJ64'
        milestone_id = 1

        handler = self.binder.bind(uri=uri, model=models.Model)

        handler(space_id=space_id)
        self.assertEqual(_get_url(mock), _make_url(uri[0], space_id=space_id))

        handler(space_id=space_id, milestone_id=milestone_id)
        self.assertEqual(_get_url(mock), _make_url(uri[1], space_id=space_id, milestone_id=milestone_id))


def suite():
    return unittest.TestLoader().loadTestsFromName(__name__)

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
