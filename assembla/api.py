import models
import binder


class API(object):
    def __init__(self):
        self.spaces = binder.bind(
            uri='/v1/spaces.json',
            model=models.Space)

        self.space = binder.bind(
            uri='/v1/spaces/{id}.json',
            model=models.Space)

        self.tickets = binder.bind(
            uri=['/v1/spaces/{space_id}/tickets.json', '/v1/spaces/{space_id}/tickets/milestone/{milestone_id}.json'],
            model=models.Ticket)
