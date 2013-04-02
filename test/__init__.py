# Use unittest2 on Python < 2.7.
try:
    import unittest2 as unittest
except ImportError:
    import unittest

# Use the standard library mock on Python > 3.3
try:
    import mock
except ImportError:
    from unittest import mock
