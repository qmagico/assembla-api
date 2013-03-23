import sys

from assembla import models

# Use unittest2 on Python < 2.7.
try:
    import unittest2 as unittest
except ImportError:
    import unittest

try:
    import mock
except ImportError:
    from unittest import mock

sys.path.insert(0, '..')


model_names = {
    'user': models.User,
    'space': models.Space,
    'space_tool': models.SpaceTool,
    'ticket': models.Ticket,
    'task': models.Task,
    'milestone': models.Milestone,
    'component': models.Component,
}


class MockAPI(object):
    def __getattr__(self, attr):
        if not attr in model_names:
            raise NameError('No method called "{0}"'.format(attr))
        instance = model_names.get(attr)()

        def method(id):
            instance.id = id
            return instance
        return method
