import sys

# Use unittest2 on Python < 2.7.
try:
    import unittest2 as unittest
except ImportError:
    import unittest

sys.path.insert(0, '..')
import assembla


class TestCast(unittest.TestCase):
    pass
