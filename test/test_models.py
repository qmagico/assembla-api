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


def suite():
    return unittest.TestLoader().loadTestsFromName(__name__)

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
