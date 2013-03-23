# from ._common import unittest

# import os
# from assembla.api import API


# class APITest(unittest.TestCase):
#     def setUp(self):
#         if 'ASSEMBLA_KEY' not in os.environ:
#             os.environ['ASSEMBLA_KEY'] = 'assembla_key'
#         if 'ASSEMBLA_SECRET' not in os.environ:
#             os.environ['ASSEMBLA_SECRET'] = 'assembla_secret'

#     def test_keys(self):
#         api = API(key='some_key', secret='some_secret')
#         self.assertEqual('some_key', api.binder.key)
#         self.assertEqual('some_secret', api.binder.secret)

#     def test_no_keys(self):
#         api = API()
#         self.assertEqual(os.environ['ASSEMBLA_KEY'], api.binder.key)
#         self.assertEqual(os.environ['ASSEMBLA_SECRET'], api.binder.secret)


# def suite():
#     return unittest.TestLoader().loadTestsFromName(__name__)

# if __name__ == '__main__':
#     unittest.main(defaultTest='suite')
