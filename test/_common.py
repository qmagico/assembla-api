import sys

from assembla import models

# Use unittest2 on Python < 2.7.
try:
    import unittest2 as unittest
except ImportError:
    import unittest

sys.path.insert(0, '..')


class TestCast(unittest.TestCase):
    pass

model_names = {
    'user': models.User,
    'space': models.Space,
    'ticket': models.Ticket
}


class APIMock(object):
    def __getattr__(self, attr):
        if not attr in model_names:
            raise NameError('No method called "{0}"'.format(attr))
        instance = model_names.get(attr)()

        def method(id):
            instance.id = id
            return instance
        return method
