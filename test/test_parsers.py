
try:
    import unittest2 as unittest
except ImportError:
    import unittest

from datetime import datetime

from assembla import parsers


class ParserTest(unittest.TestCase):
    def test_date_fields(self):
        self.assertEqual(
            {'restricted_date': datetime(2012, 1, 3, 0, 0).date()},
            parsers.parse({'restricted_date': '2012-01-03'})
        )

    def test_datetime_fields(self):
        self.assertEqual(
            {'created_on': datetime(2011, 9, 2, 10, 21, 48)},
            parsers.parse({'created_on': '2011-09-02T10:21:48Z'})
        )

    def test_float_fields(self):
        self.assertEqual(
            {'estimate': 6.5},
            parsers.parse({'estimate': '6.5'})
        )
