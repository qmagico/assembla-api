
try:
    import unittest2 as unittest
except ImportError:
    import unittest

from datetime import datetime

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
        user = models.User.instantiate_one(user_dict)

        self.assertEqual('112233', user.phone)
        self.assertEqual('test_1', user.login)
        self.assertEqual('Firstname Lastname', user.name)
        self.assertEqual('bLGGlS_Lyr4BonadbNA33N', user.id)
        self.assertEqual('Assembla', user.organization)
        self.assertEqual({'type': 'Skype', 'id': 'dsa'}, user.im)

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

        users = models.User.instantiate_many(users_dict)

        self.assertEqual(2, len(users))
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

        space = models.Space.instantiate_one(space_dict)

        self.assertEqual(1, space.status)
        self.assertIsNone(space.banner_height)
        self.assertIsNone(space.banner)
        self.assertEqual(datetime(2011, 6, 20, 13, 58, 6), space.updated_at)
        self.assertIsNone(space.last_payer_changed_at)
        self.assertEqual(0, space.team_tab_role)
        self.assertEqual(datetime(2011, 6, 20, 13, 58, 6), space.created_at)
        self.assertFalse(space.approved)
        self.assertIsNone(space.tabs_order)
        self.assertFalse(space.is_commercial)
        self.assertFalse(space.is_manager)
        self.assertEqual(2, space.team_permissions)
        self.assertIsNone(space.wiki_format)
        self.assertFalse(space.can_join)
        self.assertIsNone(space.banner_text)
        self.assertFalse(space.restricted)
        self.assertTrue(space.share_permissions)
        self.assertTrue(space.can_apply)
        self.assertFalse(space.is_volunteer)
        self.assertEqual(0, space.public_permissions)
        self.assertEqual('ADMIN', space.wiki_name)
        self.assertEqual('ADMIN', space.name)
        self.assertIsNone(space.style)
        self.assertIsNone(space.parent_id)
        self.assertEqual('Wiki', space.default_showpage)
        self.assertIsNone(space.description)
        self.assertEqual('dS5eHkVWar2RUfabdgZEU2', space.id)
        self.assertIsNone(space.banner_link)
        self.assertIsNone(space.commercial_from)
        self.assertIsNone(space.restricted_date)
        self.assertEqual(1, space.watcher_permissions)

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

        ticket = models.Ticket.instantiate_one(ticket_dict)

        self.assertEqual(8, ticket.number)
        self.assertEqual({'Text Field': '', 'list': ''}, ticket.custom_fields)
        self.assertEqual(0, ticket.total_estimate)
        self.assertEqual(1, ticket.priority)
        self.assertIsNone(ticket.component_id)
        self.assertEqual(0, ticket.story_importance)
        self.assertEqual('b89TL8MYWr4id7adbNA33N', ticket.space_id)
        self.assertEqual('bRxpnOMYWr4id7adbNA33N', ticket.reporter_id)
        self.assertIsNone(ticket.milestone_id)
        self.assertEqual(1, ticket.status)
        self.assertFalse(ticket.is_story)
        self.assertEqual('', ticket.notification_list)
        self.assertEqual(0, ticket.permission_type)
        self.assertEqual('', ticket.description)
        self.assertIsNone(ticket.completed_date)
        self.assertEqual(0, ticket.importance)
        self.assertEqual(datetime(2011, 9, 2, 10, 21, 48), ticket.created_on)
        self.assertEqual(0, ticket.total_invested_hours)
        self.assertEqual(datetime(2012, 4, 12, 10, 32, 58), ticket.updated_at)
        self.assertEqual('asd', ticket.summary)
        self.assertEqual(0, ticket.total_working_hours)
        self.assertEqual(0, ticket.estimate)
        self.assertEqual(10, ticket.id)
        self.assertIsNone(ticket.assigned_to_id)
        self.assertEqual('New', ticket.status_name)
        self.assertEqual(0, ticket.working_hours)

    def test_time_entry_instantiation(self):
        time_entry_dict = {
            'created_at': '2012-12-31T16:01:17Z',
            'space_id': 'b3gNxoscyr4Q7K5bfBjDYC',
            'description': 'Description goes here',
            'task_id': 25,
            'user_id': 'b9DhI-spar4OJk5bfBjDYC',
            'id': 2
        }

        time_entry = models.TimeEntry.instantiate_one(time_entry_dict)

        self.assertEqual(1, 1)
        self.assertEqual(datetime(2012, 12, 31, 16, 1, 17), time_entry.created_at)
        self.assertEqual('b3gNxoscyr4Q7K5bfBjDYC', time_entry.space_id)
        self.assertEqual('Description goes here', time_entry.description)
        self.assertEqual(25, time_entry.task_id)
        self.assertEqual('b9DhI-spar4OJk5bfBjDYC', time_entry.user_id)
        self.assertEqual(2, time_entry.id)

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

        milestone = models.Milestone.instantiate_one(milestone_dict)

        self.assertEqual(0, milestone.planner_type)
        self.assertEqual('sdfsd', milestone.description)
        self.assertIsNone(milestone.release_notes)
        self.assertEqual('None', milestone.pretty_relese_level)
        self.assertIsNone(milestone.release_level)
        self.assertEqual('bRxpnOMYWr4id7adbNA33N', milestone.created_by)
        self.assertIsNone(milestone.completed_date)
        self.assertIsNone(milestone.due_date)
        self.assertFalse(milestone.is_completed)
        self.assertEqual('dsa', milestone.title)
        self.assertEqual(datetime(2011, 7, 26, 8, 9, 25), milestone.created_at)
        self.assertEqual(datetime(2012, 5, 30, 9, 12, 14), milestone.updated_at)
        self.assertEqual('bgnP_qA1Gr2QjIaaaHk9wZ', milestone.updated_by)
        self.assertEqual(3, milestone.id)
        self.assertIsNone(milestone.user_id)
        self.assertEqual('b89TL8MYWr4id7adbNA33N', milestone.space_id)

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

        task = models.Task.instantiate_one(task_dict)

        self.assertFalse(task.billed)
        self.assertEqual(datetime(2012, 12, 17, 8, 52, 20), task.created_at)
        self.assertIsNone(task.ticket_number)
        self.assertEqual('b3gNxoscyr4Q7K5bfBjDYC', task.space_id)
        self.assertEqual(datetime(2012, 12, 17, 8, 51, 0), task.begin_at)
        self.assertIsNone(task.url)
        self.assertEqual('Description goes here', task.description)
        self.assertEqual(datetime(2012, 12, 17, 8, 52, 20), task.updated_at)
        self.assertIsNone(task.job_agreement_id)
        self.assertEqual('apr9bascyr4Q7K5bfBjDYC', task.user_id)
        self.assertIsNone(task.ticket_id)
        self.assertEqual(datetime(2012, 12, 17, 8, 51, 0), task.end_at)
        self.assertEqual(1.0, task.hours)
        self.assertEqual(7, task.id)

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

        ticket_status = models.TicketStatus.instantiate_one(ticket_status_dict)

        self.assertEqual(1, ticket_status.id)
        self.assertEqual('dP3FZG_ber4B8UadbNA33N', ticket_status.space_tool_id)
        self.assertEqual('New', ticket_status.name)
        self.assertEqual(1, ticket_status.state)
        self.assertEqual(1, ticket_status.list_order)
        self.assertEqual(datetime(2012, 9, 11, 13, 9, 26), ticket_status.created_at)
        self.assertEqual(datetime(2012, 9, 11, 13, 9, 26), ticket_status.updated_at)

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

        space_tool = models.SpaceTool.instantiate_one(space_tool_dict)

        self.assertEqual('SubversionTool', space_tool.type)
        self.assertEqual(12, space_tool.tool_id)
        self.assertTrue(space_tool.active)
        self.assertEqual(datetime(2011, 9, 9, 9, 43, 7), space_tool.created_at)
        self.assertIsNone(space_tool.team_permissions)
        self.assertIsNone(space_tool.url)
        self.assertEqual('b89TL8MYWr4id7adbNA33N', space_tool.space_id)
        self.assertEqual(1, space_tool.number)
        self.assertIsNone(space_tool.public_permissions)
        self.assertIsNone(space_tool.parent_id)
        self.assertEqual('subversion', space_tool.name)
        self.assertEqual('Source/SVN', space_tool.menu_name)
        self.assertIsNone(space_tool.watcher_permissions)
        self.assertEqual({'state': 'failed', 'vcs_url': None}, space_tool.settings)
        self.assertEqual('aFsIka2SGr4j8fadbNA33N', space_tool.id)

    def test_merge_request_instantiation(self):
        merge_request_dict = {
            'processed_by_user_id': None,
            'status': 0,
            'apply_status': None,
            'description': '',
            'title': 'title',
            'target_space_tool_id': 'bgfq4qA1Gr2QjIaaaHk9wZ',
            'target_space_id': 'bBEAVq-5Gr4yhAimNqr_pR',
            'applied_at': None,
            'target_symbol': 'master',
            'source_symbol_type': 0,
            'source_symbol': 'test_branch',
            'space_tool_id': 'a5BqzgFVSr4zLpab_q0pIh',
            'updated_at': '2012-07-26T07:59:40Z',
            'commit': None,
            'id': 2,
            'created_at': '2012-06-27T12:41:17Z',
            'user_id': 'aeF1CInHCr4ybVab_q0pIh'
        }

        merge_request = models.MergeRequest.instantiate_one(merge_request_dict)

        self.assertIsNone(merge_request.processed_by_user_id)
        self.assertEqual(0, merge_request.status)
        self.assertIsNone(merge_request.apply_status)
        self.assertEqual('', merge_request.description)
        self.assertEqual('title', merge_request.title)
        self.assertEqual('bgfq4qA1Gr2QjIaaaHk9wZ', merge_request.target_space_tool_id)
        self.assertEqual('bBEAVq-5Gr4yhAimNqr_pR', merge_request.target_space_id)
        self.assertIsNone(merge_request.applied_at)
        self.assertEqual('master', merge_request.target_symbol)
        self.assertEqual(0, merge_request.source_symbol_type)
        self.assertEqual('test_branch', merge_request.source_symbol)
        self.assertEqual('a5BqzgFVSr4zLpab_q0pIh', merge_request.space_tool_id)
        self.assertEqual(datetime(2012, 7, 26, 7, 59, 40), merge_request.updated_at)
        self.assertIsNone(merge_request.commit)
        self.assertEqual(2, merge_request.id)
        self.assertEqual(datetime(2012, 6, 27, 12, 41, 17), merge_request.created_at)
        self.assertEqual('aeF1CInHCr4ybVab_q0pIh', merge_request.user_id)
