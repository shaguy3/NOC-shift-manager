from datetime import datetime, date


def get_this_sunday():
    today = date.today()
    ordinal_today = today.toordinal()
    last_ordinal = ordinal_today - 6
    last_sunday_ordinal = last_ordinal - (last_ordinal % 7)
    return date.fromordinal(last_sunday_ordinal)


class WorkWeek:

    id = 1

    def __init__(self):
        self.id = WorkWeek.id
        self.start_date = datetime


last_sunday = get_this_sunday()
print(last_sunday)
