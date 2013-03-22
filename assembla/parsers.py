from datetime import datetime


def parse(json, api=None):
    datetime_fields = [
        'applied_at',
        'begin_at',
        'commercial_from',
        'completed_date',
        'created_at',
        'created_on',
        'due_date',
        'end_at',
        'filled_for',
        'last_payer_changed_at',
        'restricted_date',
        'updated_at',
    ]

    float_fields = [
        'estimate',
        'hours',
        'importance',
        'total_estimate',
        'total_invested_hours',
        'total_working_hours',
    ]

    data = {}

    # imported here to avoid cyclic dependency
    from .api import API
    api = api or API()

    for key, value in json.items():
        if key in ['user_id', 'reporter_id', 'assigned_to_id']:
            key = key.replace('_id', '')
            if value:
                value = api.user(id=value)

        if key == 'space_id':
            key = 'space'
            if value:
                value = api.space(id=value)

        if key == 'ticket_id':
            key = 'ticket'
            if value:
                value = api.ticket(id=value)

        elif key in float_fields:
            if value:
                value = float(value)

        elif key in datetime_fields:
            if value:
                try:
                    value = datetime.strptime(value[:19], '%Y-%m-%dT%H:%M:%S')
                except ValueError:
                    value = datetime.strptime(value, '%Y-%m-%d').date()
        data[key] = value
    return data
