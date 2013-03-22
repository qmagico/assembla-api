import os
import sys
from ._common import unittest
from assembla import binder, models

pkgpath = os.path.dirname(__file__) or '.'
sys.path.append(pkgpath)
os.chdir(pkgpath)


def _make_uri(*args):
    params = ['{0}/{{{0}_id}}'.format(param) for param in args]
    return '/{0}'.format('/'.join(params))


def _make_getter(test_case, uri):
    def getter(url, **req_kwargs):
        test_case.assertEqual('https://api.assembla.com{0}'.format(uri), url)
        return Response()
    return getter


class Response(object):
    def json(self):
        return {}


class BinderTest(unittest.TestCase):
    def test_uri(self):
        uri = _make_uri('space')
        space_id = 'axk9jBJ64'

        getter = _make_getter(self, uri.format(space_id=space_id))

        handler = binder.bind(uri=uri, model=models.Model, getter=getter)
        handler(space_id=space_id)

    def test_multi_uri(self):
        uri = []
        uri.append(_make_uri('space'))
        uri.append(_make_uri('space', 'milestone'))
        space_id = 'axk9jBJ64'
        milestone_id = 1

        getter = _make_getter(self, uri[0].format(space_id=space_id))

        handler = binder.bind(uri=uri, model=models.Model, getter=getter)
        handler(space_id=space_id)

        getter = _make_getter(self, uri[1].format(space_id=space_id, milestone_id=milestone_id))

        handler = binder.bind(uri=uri, model=models.Model, getter=getter)
        handler(space_id=space_id, milestone_id=milestone_id)


def suite():
    return unittest.TestLoader().loadTestsFromName(__name__)

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
