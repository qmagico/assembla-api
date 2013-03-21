from datetime import datetime


class Model(object):
    @classmethod
    def parse(cls, json):
        datetime_fields = [
            'applied_at',
            'begin_at',
            'commercial_from',
            'completed_date'
            'created_at',
            'created_on',
            'end_at',
            'updated_at',
        ]

        date_fields = [
            'restricted_date',
            'last_payer_changed_at',
            'due_date',
            'filled_for',
        ]

        entity = cls()
        for key, value in json.items():

            if key in date_fields:
                # input example:
                # - 2013-01-12
                if value:
                    value = datetime.strptime(value, '%Y-%m-%d')

            if key in datetime_fields:
                # input example:
                # - 2013-01-12T13:10:24-05:00
                if value:
                    value = datetime.strptime(value[:19], '%Y-%m-%dT%H:%M:%S')

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
