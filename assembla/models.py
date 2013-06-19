from . import parsers


class Model(object):
    @classmethod
    def instantiate_one(cls, json):
        attrs = parsers.parse(json)
        instance = cls()
        for key, value in attrs.items():
            setattr(instance, key, value)
        return instance

    @classmethod
    def instantiate_many(cls, json):
        return [cls.instantiate_one(entity) for entity in json]


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
