from . import parsers


class Model(object):
    @classmethod
    def parse(cls, json):
        attrs = parsers.parse(json)
        instance = cls()
        for key, value in attrs.items():
            setattr(instance, key, value)
        return instance

    @classmethod
    def parse_list(cls, json):
        return cls.parse_list(json)


class User(Model):
    pass


class Space(Model):
    pass


class Ticket(Model):
    pass


class TimeEntry(Model):
    pass


class Milestone(Model):
    pass


class Task(Model):
    pass
