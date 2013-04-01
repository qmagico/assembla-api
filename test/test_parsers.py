from datetime import datetime

from ._common import unittest, MockAPI
from assembla import parsers, models


class ParserTest(unittest.TestCase):
    def test_date_fields(self):
        self.assertEquals(
            {'restricted_date': datetime(2012, 1, 3, 0, 0).date()},
            parsers.parse({'restricted_date': '2012-01-03'})
        )

    def test_datetime_fields(self):
        self.assertEquals(
            {'created_on': datetime(2011, 9, 2, 10, 21, 48)},
            parsers.parse({'created_on': '2011-09-02T10:21:48Z'})
        )

    def test_user_fields(self):
        self.assertIsInstance(
            parsers.parse({'user_id': 'apr9bascyr4Q7K5bfBjDYC'}, api=MockAPI()).get('user'),
            models.User
        )

        self.assertIsInstance(
            parsers.parse({'reporter_id': 'apr9bascyr4Q7K5bfBjDYC'}, api=MockAPI()).get('reporter'),
            models.User
        )

        self.assertIsInstance(
            parsers.parse({'assigned_to_id': 'apr9bascyr4Q7K5bfBjDYC'}, api=MockAPI()).get('assigned_to'),
            models.User
        )

        self.assertIsInstance(
            parsers.parse({'updated_by': 'apr9bascyr4Q7K5bfBjDYC'}, api=MockAPI()).get('updated_by'),
            models.User
        )

    def test_ticket_fields(self):
        self.assertIsInstance(
            parsers.parse({'ticket_id': 'apr9bascyr4Q7K5bfBjDYC'}, api=MockAPI()).get('ticket'),
            models.Ticket
        )

    def test_task_fields(self):
        self.assertIsInstance(
            parsers.parse({'task_id': 25}, api=MockAPI()).get('task'),
            models.Task
        )

    def test_milestone_fields(self):
        self.assertIsInstance(
            parsers.parse({'milestone_id': 'bRxpnOMYWr4id7adbNA33N'}, api=MockAPI()).get('milestone'),
            models.Milestone
        )

    def test_component_fields(self):
        self.assertIsInstance(
            parsers.parse({'component_id': 'bRxpnOMYWr4id7adbNA33N'}, api=MockAPI()).get('component'),
            models.Component
        )

    def test_space_tool_fields(self):
        self.assertIsInstance(
            parsers.parse({'space_tool_id': 'aFsIka2SGr4j8fadbNA33N'}, api=MockAPI()).get('space_tool'),
            models.SpaceTool
        )


def suite():
    return unittest.TestLoader().loadTestsFromName(__name__)

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
