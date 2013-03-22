from . import parsers


class Model(object):
    @classmethod
    def parse(cls, json, api=None):
        attrs = parsers.parse(json, api=api)
        instance = cls()
        for key, value in attrs.items():
            setattr(instance, key, value)
        return instance

    @classmethod
    def parse_list(cls, json):
        return [cls.parse(entity) for entity in json]


class User(Model):
    pass


class Space(Model):
    pass


class SpaceTool(Model):
    pass


class Ticket(Model):
    pass


class TicketStatus(Model):
    pass


class TimeEntry(Model):
    pass


class Milestone(Model):
    pass


class Task(Model):
    pass


class Component(Model):
    pass
