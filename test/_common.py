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


class APIMock(object):
    def user(self, id):
        user = models.User()
        user.id = id
        return user

    def space(self, id):
        space = models.Space()
        space.id = id
        return space
