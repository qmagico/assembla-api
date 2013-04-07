from test import mock
from assembla import models

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

        def method(id, lazy=None):
            instance.id = id
            return instance
        return method


def make_response(return_value):
    response = mock.Mock()
    response.status_code = 200
    response.json = mock.Mock()
    response.json.return_value = return_value
    return response


def request_call(mock):
    args, kwargs = mock.call_args
    return args[0], kwargs['headers']
