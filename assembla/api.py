import os
from . import models
from .binder import Binder


class API(object):
    def __init__(self, key=None, secret=None):
        key = key or os.environ.get('ASSEMBLA_KEY', '')
        secret = secret or os.environ.get('ASSEMBLA_SECRET', '')
        binder = Binder(key=key, secret=secret)

        self.spaces = binder.bind(
            uri='/v1/spaces.json',
            model=models.Space)

        self.space = binder.bind(
            uri='/v1/spaces/{id}.json',
            model=models.Space)

        self.tickets = binder.bind(
            uri=['/v1/spaces/{space_id}/tickets.json', '/v1/spaces/{space_id}/tickets/milestone/{milestone_id}.json'],
            model=models.Ticket)

        self.user = binder.bind(
            uri=['/v1/users/{user_id}.json', '/v1/users/{user_login}.json'],
            model=models.User)

        self.users = binder.bind(
            uri='/v1/spaces/{space_id}/users.json',
            model=models.User)
