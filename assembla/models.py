

class Model(object):
    @classmethod
    def parse(cls, json):
        entity = cls()
        for k, v in json.items():
            setattr(entity, k, v)
        return entity

    @classmethod
    def parse_list(cls, json):
        entities = []
        for i in json:
            entities.append(cls.parse(i))
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