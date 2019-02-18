from datetime import date


def get_last_sunday():
    today = date.today()
    ordinal_today = today.toordinal()
    last_sunday_ordinal = ordinal_today - (ordinal_today % 7)
    return date.fromordinal(last_sunday_ordinal)


def get_next_saturday():
    today = date.today()
    ordinal_today = today.toordinal()
    next_saturday_ordinal = ordinal_today - (ordinal_today % 7) + 6
    return date.fromordinal(next_saturday_ordinal)


class WorkWeek:

    id = 1

    def __init__(self):
        self.id = WorkWeek.id
        self.start_date = get_last_sunday()
        self.end_date = get_next_saturday()
        self.schedule = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

        WorkWeek.id += 1

    def __repr__(self):
        string_to_return = 'Work week number {}. Start date: {}.  End date: {}.' \
            .format(self.id, self.start_date, self.end_date) + '\n'
        string_to_return += '         Sunday    Monday    Tuesday    Wednesday    Thursday    Friday    Saturday \n'
        string_to_return += 'Morning: '
        for i in range(7):
            string_to_return += str(self.schedule[i])
        string_to_return += '\nEvening: '
        for i in range(7, 14):
            string_to_return += str(self.schedule[i])
        string_to_return += '\nNight:   '
        for i in range(14, 21):
            string_to_return += str(self.schedule[i])
        return string_to_return

    def add_to_shift(self, shift_number, *workers):
        for worker in workers:
            self.schedule[shift_number].append(worker)
