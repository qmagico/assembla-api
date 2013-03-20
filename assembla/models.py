

class Model(object):
    @classmethod
    def parse(cls, json):
        entity = cls()
        for key, value in json.items():
            setattr(entity, key, value)
        return entity

    @classmethod
    def parse_list(cls, json):
        entities = []
        for entity in json:
            entities.append(cls.parse(entity))
        return entities


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
