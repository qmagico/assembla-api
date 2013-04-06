from datetime import datetime


def parse(json, api):
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

    user_fields = [
        'user_id',
        'reporter_id',
        'assigned_to_id',
        'updated_by',
        'created_by'
    ]

    foreign_fields = [
        'component_id',
        'milestone_id',
        'space_id',
        'space_tool_id',
        'task_id',
        'ticket_id',
    ]

    data = {}

    for key, value in json.items():
        if key in user_fields:
            key = key.replace('_id', '')
            if value:
                value = api.user(id=value, lazy=True)

        elif key in foreign_fields:
            key = key.replace('_id', '')
            if value:
                value = getattr(api, key)(id=value, lazy=True)

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
