from datetime import datetime

from _common import unittest
from assembla import models


class ModelsTest(unittest.TestCase):
    def test_user_instantiation(self):
        user_dict = {
            'phone': '112233',
            'login': 'test_1',
            'name': 'Firstname Lastname',
            'id': 'bLGGlS_Lyr4BonadbNA33N',
            'organization': 'Assembla',
            'im': {'type': 'Skype', 'id': 'dsa'}
        }
        user = models.User.parse(user_dict)

        self.assertEquals('112233', user.phone)
        self.assertEquals('test_1', user.login)
        self.assertEquals('Firstname Lastname', user.name)
        self.assertEquals('bLGGlS_Lyr4BonadbNA33N', user.id)
        self.assertEquals('Assembla', user.organization)
        self.assertEquals({'type': 'Skype', 'id': 'dsa'}, user.im)

    def test_users_instantiation(self):
        users_dict = [
            {
                'phone': '112234',
                'login': 'test_2',
                'name': 'Firstname2 Lastname',
                'id': 'bLGGlS_Lyr4BonadbNA33g',
                'organization': 'Assembla',
                'im': {'type': 'Skype', 'id': 'dsa2'}
            },
            {
                'phone': '112233',
                'login': 'test_1',
                'name': 'Firstname Lastname',
                'id': 'bLGGlS_Lyr4BonadbNA33N',
                'organization': 'Assembla',
                'im': {'type': 'Skype', 'id': 'dsa'}
            }
        ]

        users = models.User.parse_list(users_dict)

        self.assertEquals(2, len(users))
        self.assertTrue(isinstance(users[0], models.User))

    def test_space_instantiation(self):
        space_dict = {
            'status': 1,
            'banner_height': None,
            'banner': None,
            'updated_at': '2011-06-20T13:58:06Z',
            'last_payer_changed_at': None,
            'team_tab_role': 0,
            'created_at': '2011-06-20T13:58:06Z',
            'approved': False,
            'tabs_order': None,
            'is_commercial': False,
            'is_manager': False,
            'team_permissions': 2,
            'wiki_format': None,
            'can_join': False,
            'banner_text': None,
            'restricted': False,
            'share_permissions': True,
            'can_apply': True,
            'is_volunteer': False,
            'public_permissions': 0,
            'wiki_name': 'ADMIN',
            'name': 'ADMIN',
            'style': None,
            'parent_id': None,
            'default_showpage': 'Wiki',
            'description': None,
            'id': 'dS5eHkVWar2RUfabdgZEU2',
            'banner_link': None,
            'commercial_from': None,
            'restricted_date': None,
            'watcher_permissions': 1
        }

        space = models.Space.parse(space_dict)

        self.assertEquals(1, space.status)
        self.assertEquals(None, space.banner_height)
        self.assertEquals(None, space.banner)
        self.assertEquals(datetime(2011, 6, 20, 13, 58, 6), space.updated_at)
        self.assertEquals(None, space.last_payer_changed_at)
        self.assertEquals(0, space.team_tab_role)
        self.assertEquals(datetime(2011, 6, 20, 13, 58, 6), space.created_at)
        self.assertEquals(False, space.approved)
        self.assertEquals(None, space.tabs_order)
        self.assertEquals(False, space.is_commercial)
        self.assertEquals(False, space.is_manager)
        self.assertEquals(2, space.team_permissions)
        self.assertEquals(None, space.wiki_format)
        self.assertEquals(False, space.can_join)
        self.assertEquals(None, space.banner_text)
        self.assertEquals(False, space.restricted)
        self.assertEquals(True, space.share_permissions)
        self.assertEquals(True, space.can_apply)
        self.assertEquals(False, space.is_volunteer)
        self.assertEquals(0, space.public_permissions)
        self.assertEquals('ADMIN', space.wiki_name)
        self.assertEquals('ADMIN', space.name)
        self.assertEquals(None, space.style)
        self.assertEquals(None, space.parent_id)
        self.assertEquals('Wiki', space.default_showpage)
        self.assertEquals(None, space.description)
        self.assertEquals('dS5eHkVWar2RUfabdgZEU2', space.id)
        self.assertEquals(None, space.banner_link)
        self.assertEquals(None, space.commercial_from)
        self.assertEquals(None, space.restricted_date)
        self.assertEquals(1, space.watcher_permissions)

    def test_ticket_instantiation(self):
        ticket_dict = {
            'number': 8,
            'custom_fields': {'Text Field': '', 'list': ''},
            'total_estimate': 0.0,
            'priority': 1,
            'component_id': None,
            'story_importance': 0,
            'space_id': 'b89TL8MYWr4id7adbNA33N',
            'reporter_id': 'bRxpnOMYWr4id7adbNA33N',
            'milestone_id': None,
            'status': 1,
            'is_story': False,
            'notification_list': '',
            'permission_type': 0,
            'description': '',
            'completed_date': None,
            'importance': 0.0,
            'created_on': '2011-09-02T10:21:48Z',
            'total_invested_hours': 0.0,
            'updated_at': '2012-04-12T10:32:58Z',
            'summary': 'asd',
            'total_working_hours': 0.0,
            'estimate': 0.0,
            'id': 10,
            'assigned_to_id': None,
            'status_name': 'New',
            'working_hours': 0.0
        }

        ticket = models.Ticket.parse(ticket_dict)

        self.assertEquals(8, ticket.number)
        self.assertEquals({'Text Field': '', 'list': ''}, ticket.custom_fields)
        self.assertEquals(0, ticket.total_estimate)
        self.assertEquals(1, ticket.priority)
        self.assertEquals(None, ticket.component_id)
        self.assertEquals(0, ticket.story_importance)
        self.assertEquals('b89TL8MYWr4id7adbNA33N', ticket.space_id)
        self.assertEquals('bRxpnOMYWr4id7adbNA33N', ticket.reporter_id)
        self.assertEquals(None, ticket.milestone_id)
        self.assertEquals(1, ticket.status)
        self.assertEquals(False, ticket.is_story)
        self.assertEquals('', ticket.notification_list)
        self.assertEquals(0, ticket.permission_type)
        self.assertEquals('', ticket.description)
        self.assertEquals(None, ticket.completed_date)
        self.assertEquals(0, ticket.importance)
        self.assertEquals(datetime(2011, 9, 2, 10, 21, 48), ticket.created_on)
        self.assertEquals(0, ticket.total_invested_hours)
        self.assertEquals(datetime(2012, 4, 12, 10, 32, 58), ticket.updated_at)
        self.assertEquals('asd', ticket.summary)
        self.assertEquals(0, ticket.total_working_hours)
        self.assertEquals(0, ticket.estimate)
        self.assertEquals(10, ticket.id)
        self.assertEquals(None, ticket.assigned_to_id)
        self.assertEquals('New', ticket.status_name)
        self.assertEquals(0, ticket.working_hours)

    def test_time_entry_instantiation(self):
        time_entry_dict = {
            'created_at': '2012-12-31T16:01:17Z',
            'space_id': 'b3gNxoscyr4Q7K5bfBjDYC',
            'description': 'Description goes here',
            'task_id': 25,
            'user_id': 'b9DhI-spar4OJk5bfBjDYC',
            'id': 2
        }

        time_entry = models.TimeEntry.parse(time_entry_dict)

        self.assertEquals(1, 1)
        self.assertEquals(datetime(2012, 12, 31, 16, 01, 17), time_entry.created_at)
        self.assertEquals('b3gNxoscyr4Q7K5bfBjDYC', time_entry.space_id)
        self.assertEquals('Description goes here', time_entry.description)
        self.assertEquals(25, time_entry.task_id)
        self.assertEquals('b9DhI-spar4OJk5bfBjDYC', time_entry.user_id)
        self.assertEquals(2, time_entry.id)

    def test_milestone_instantiation(self):
        milestone_dict = {
            'planner_type': 0,
            'description': 'sdfsd',
            'release_notes': None,
            'pretty_relese_level': 'None',
            'release_level': None,
            'created_by': 'bRxpnOMYWr4id7adbNA33N',
            'completed_date': None,
            'due_date': None,
            'is_completed': False,
            'title': 'dsa',
            'created_at': '2011-07-26T08:09:25Z',
            'updated_at': '2012-05-30T09:12:14Z',
            'updated_by': 'bgnP_qA1Gr2QjIaaaHk9wZ',
            'id': 3,
            'user_id': None,
            'space_id': 'b89TL8MYWr4id7adbNA33N'
        }

        milestone = models.Milestone.parse(milestone_dict)

        self.assertEquals(0, milestone.planner_type)
        self.assertEquals('sdfsd', milestone.description)
        self.assertEquals(None, milestone.release_notes)
        self.assertEquals('None', milestone.pretty_relese_level)
        self.assertEquals(None, milestone.release_level)
        self.assertEquals('bRxpnOMYWr4id7adbNA33N', milestone.created_by)
        self.assertEquals(None, milestone.completed_date)
        self.assertEquals(None, milestone.due_date)
        self.assertEquals(False, milestone.is_completed)
        self.assertEquals('dsa', milestone.title)
        self.assertEquals(datetime(2011, 7, 26, 8, 9, 25), milestone.created_at)
        self.assertEquals(datetime(2012, 05, 30, 9, 12, 14), milestone.updated_at)
        self.assertEquals('bgnP_qA1Gr2QjIaaaHk9wZ', milestone.updated_by)
        self.assertEquals(3, milestone.id)
        self.assertEquals(None, milestone.user_id)
        self.assertEquals('b89TL8MYWr4id7adbNA33N', milestone.space_id)

    def test_task_milestone(self):
        task_dict = {
            'billed': False,
            'created_at': '2012-12-17T08:52:20Z',
            'ticket_number': None,
            'space_id': 'b3gNxoscyr4Q7K5bfBjDYC',
            'begin_at': '2012-12-17T08:51:00Z',
            'url': None,
            'description': 'Description goes here',
            'updated_at': '2012-12-17T08:52:20Z',
            'job_agreement_id': None,
            'user_id': 'apr9bascyr4Q7K5bfBjDYC',
            'ticket_id': None,
            'end_at': '2012-12-17T08:51:00Z',
            'hours': '1.0',
            'id': 7
        }

        task = models.Task.parse(task_dict)

        self.assertEquals(False, task.billed)
        self.assertEquals(datetime(2012, 12, 17, 8, 52, 20), task.created_at)
        self.assertEquals(None, task.ticket_number)
        self.assertEquals('b3gNxoscyr4Q7K5bfBjDYC', task.space_id)
        self.assertEquals(datetime(2012, 12, 17, 8, 51, 0), task.begin_at)
        self.assertEquals(None, task.url)
        self.assertEquals('Description goes here', task.description)
        self.assertEquals(datetime(2012, 12, 17, 8, 52, 20), task.updated_at)
        self.assertEquals(None, task.job_agreement_id)
        self.assertEquals('apr9bascyr4Q7K5bfBjDYC', task.user_id)
        self.assertEquals(None, task.ticket_id)
        self.assertEquals(datetime(2012, 12, 17, 8, 51, 0), task.end_at)
        self.assertEquals(1.0, task.hours)
        self.assertEquals(7, task.id)


def suite():
    return unittest.TestLoader().loadTestsFromName(__name__)

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
