from assembla import parsers


class Model(object):
    @classmethod
    def instantiate_one(cls, json, api):
        attrs = parsers.parse(json, api)
        instance = cls()
        for key, value in attrs.items():
            setattr(instance, key, value)
        return instance

    @classmethod
    def instantiate_many(cls, json, api):
        return [cls.instantiate_one(entity, api) for entity in json]

    def __init__(self, lazy_load=None):
        if lazy_load:
            self.lazy_load = lazy_load

    def __getattr__(self, name):
        if name != 'lazy_load' and self.lazy_load:
            api, json = self.lazy_load()
            attrs = parsers.parse(json, api)
            for key, value in attrs.items():
                setattr(self, key, value)
            delattr(self, 'lazy_load')
            return getattr(self, name)


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
