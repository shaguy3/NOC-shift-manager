class WorkWeek:

    def __init__(self, id, start_date, end_date, schedule=None):
        if schedule is None:
            schedule = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
        self.id = id
        self.start_date = start_date
        self.end_date = end_date
        self.schedule = schedule

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

    def __getitem__(self, item):
        return self.schedule[item]

    def __setitem__(self, key, value):
        self.schedule[key] = value
