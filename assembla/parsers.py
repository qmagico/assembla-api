from datetime import datetime


def parse(json):
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

    for key, value in json.items():
        if key in float_fields:
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
