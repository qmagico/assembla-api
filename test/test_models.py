from datetime import datetime

from test import unittest
from test.util import MockAPI
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
        user = models.User.instantiate_one(user_dict, api=MockAPI())

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

        users = models.User.instantiate_many(users_dict, api=MockAPI())

        self.assertEquals(2, len(users))
        self.assertIsInstance(users[0], models.User)

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

        space = models.Space.instantiate_one(space_dict, api=MockAPI())

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

        ticket = models.Ticket.instantiate_one(ticket_dict, api=MockAPI())

        self.assertEquals(8, ticket.number)
        self.assertEquals({'Text Field': '', 'list': ''}, ticket.custom_fields)
        self.assertEquals(0, ticket.total_estimate)
        self.assertEquals(1, ticket.priority)
        self.assertEquals(None, ticket.component)
        self.assertEquals(0, ticket.story_importance)
        self.assertIsInstance(ticket.space, models.Space)
        self.assertEquals('b89TL8MYWr4id7adbNA33N', ticket.space.id)
        self.assertIsInstance(ticket.reporter, models.User)
        self.assertEquals('bRxpnOMYWr4id7adbNA33N', ticket.reporter.id)
        self.assertEquals(None, ticket.milestone)
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
        self.assertEquals(None, ticket.assigned_to)
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

        time_entry = models.TimeEntry.instantiate_one(time_entry_dict, api=MockAPI())

        self.assertEquals(1, 1)
        self.assertEquals(datetime(2012, 12, 31, 16, 1, 17), time_entry.created_at)
        self.assertIsInstance(time_entry.space, models.Space)
        self.assertEquals('b3gNxoscyr4Q7K5bfBjDYC', time_entry.space.id)
        self.assertEquals('Description goes here', time_entry.description)
        self.assertIsInstance(time_entry.task, models.Task)
        self.assertEquals(25, time_entry.task.id)
        self.assertIsInstance(time_entry.user, models.User)
        self.assertEquals('b9DhI-spar4OJk5bfBjDYC', time_entry.user.id)
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

        milestone = models.Milestone.instantiate_one(milestone_dict, api=MockAPI())

        self.assertEquals(0, milestone.planner_type)
        self.assertEquals('sdfsd', milestone.description)
        self.assertEquals(None, milestone.release_notes)
        self.assertEquals('None', milestone.pretty_relese_level)
        self.assertEquals(None, milestone.release_level)
        self.assertIsInstance(milestone.created_by, models.User)
        self.assertEquals('bRxpnOMYWr4id7adbNA33N', milestone.created_by.id)
        self.assertEquals(None, milestone.completed_date)
        self.assertEquals(None, milestone.due_date)
        self.assertEquals(False, milestone.is_completed)
        self.assertEquals('dsa', milestone.title)
        self.assertEquals(datetime(2011, 7, 26, 8, 9, 25), milestone.created_at)
        self.assertEquals(datetime(2012, 5, 30, 9, 12, 14), milestone.updated_at)
        self.assertIsInstance(milestone.updated_by, models.User)
        self.assertEquals('bgnP_qA1Gr2QjIaaaHk9wZ', milestone.updated_by.id)
        self.assertEquals(3, milestone.id)
        self.assertEquals(None, milestone.user)
        self.assertIsInstance(milestone.space, models.Space)
        self.assertEquals('b89TL8MYWr4id7adbNA33N', milestone.space.id)

    def test_task_instantiation(self):
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

        task = models.Task.instantiate_one(task_dict, api=MockAPI())

        self.assertEquals(False, task.billed)
        self.assertEquals(datetime(2012, 12, 17, 8, 52, 20), task.created_at)
        self.assertEquals(None, task.ticket_number)
        self.assertIsInstance(task.space, models.Space)
        self.assertEquals('b3gNxoscyr4Q7K5bfBjDYC', task.space.id)
        self.assertEquals(datetime(2012, 12, 17, 8, 51, 0), task.begin_at)
        self.assertEquals(None, task.url)
        self.assertEquals('Description goes here', task.description)
        self.assertEquals(datetime(2012, 12, 17, 8, 52, 20), task.updated_at)
        self.assertEquals(None, task.job_agreement_id)
        self.assertIsInstance(task.user, models.User)
        self.assertEquals('apr9bascyr4Q7K5bfBjDYC', task.user.id)
        self.assertEquals(None, task.ticket)
        self.assertEquals(datetime(2012, 12, 17, 8, 51, 0), task.end_at)
        self.assertEquals(1.0, task.hours)
        self.assertEquals(7, task.id)

    def test_ticket_status_instantiation(self):
        ticket_status_dict = {
            'id': 1,
            'space_tool_id': 'dP3FZG_ber4B8UadbNA33N',
            'name': 'New',
            'state': 1,
            'list_order': 1,
            'created_at': '2012-09-11T13:09:26Z',
            'updated_at': '2012-09-11T13:09:26Z'
        }

        ticket_status = models.TicketStatus.instantiate_one(ticket_status_dict, api=MockAPI())

        self.assertEquals(1, ticket_status.id)
        self.assertIsInstance(ticket_status.space_tool, models.SpaceTool)
        self.assertEquals('dP3FZG_ber4B8UadbNA33N', ticket_status.space_tool.id)
        self.assertEquals('New', ticket_status.name)
        self.assertEquals(1, ticket_status.state)
        self.assertEquals(1, ticket_status.list_order)
        self.assertEquals(datetime(2012, 9, 11, 13, 9, 26), ticket_status.created_at)
        self.assertEquals(datetime(2012, 9, 11, 13, 9, 26), ticket_status.updated_at)

    def test_component_instantiation(self):
        component_dict = {
            'id': 16,
            'name': 'asd'
        }

        component = models.Component.instantiate_one(component_dict, api=MockAPI())

        self.assertEquals(16, component.id)
        self.assertEquals('asd', component.name)

    def test_space_tool_instantiation(self):
        space_tool_dict = {
            'type': 'SubversionTool',
            'tool_id': 12,
            'active': True,
            'created_at': '2011-09-09T09:43:07Z',
            'team_permissions': None,
            'url': None,
            'space_id': 'b89TL8MYWr4id7adbNA33N',
            'number': 1,
            'public_permissions': None,
            'parent_id': None,
            'name': 'subversion',
            'menu_name': 'Source/SVN',
            'watcher_permissions': None,
            'settings': {'state': 'failed', 'vcs_url': None},
            'id': 'aFsIka2SGr4j8fadbNA33N',
        }

        space_tool = models.SpaceTool.instantiate_one(space_tool_dict, api=MockAPI())

        self.assertEquals('SubversionTool', space_tool.type)
        self.assertEquals(12, space_tool.tool_id)
        self.assertEquals(True, space_tool.active)
        self.assertEquals(datetime(2011, 9, 9, 9, 43, 7), space_tool.created_at)
        self.assertEquals(None, space_tool.team_permissions)
        self.assertEquals(None, space_tool.url)
        self.assertIsInstance(space_tool.space, models.Space)
        self.assertEquals('b89TL8MYWr4id7adbNA33N', space_tool.space.id)
        self.assertEquals(1, space_tool.number)
        self.assertEquals(None, space_tool.public_permissions)
        self.assertEquals(None, space_tool.parent_id)
        self.assertEquals('subversion', space_tool.name)
        self.assertEquals('Source/SVN', space_tool.menu_name)
        self.assertEquals(None, space_tool.watcher_permissions)
        self.assertEquals({'state': 'failed', 'vcs_url': None}, space_tool.settings)
        self.assertEquals('aFsIka2SGr4j8fadbNA33N', space_tool.id)
