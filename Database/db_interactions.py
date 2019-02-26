from Classes import employee, work_week
import json
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


def create_employee(name):
    with open('workers.json', 'r+') as workers_json:
        workers = json.load(workers_json)
        taken_ids = []
        for worker_id in workers.keys():
            taken_ids.append(worker_id)
        id_checker = '1'
        while id_checker in taken_ids:
            id_checker = str(int(id_checker) + 1)

        emp = employee.Employee(id_checker, name)
        save_employee(emp)
        return emp


def save_employee(emp):
    with open('workers.json', 'r+') as workers_json:
        workers = json.load(workers_json)
        workers[emp.id] = {'Name': emp.name, 'Database': {}}
        workers_json.seek(0)
        json.dump(workers, workers_json)
        workers_json.truncate()


def load_employee(name):
    with open('workers.json', 'r+') as workers_json:
        workers = json.load(workers_json)
        for id, worker in workers.items():
            if worker['Name'] == name:
                id = id
                rules = worker['Rules']
                return employee.Employee(id, name, rules=rules)
        return None


def remove_employee(emp):
    with open('workers.json', 'r+') as workers_json:
        workers = json.load(workers_json)
        del workers[emp.id]
        workers_json.seek(0)
        json.dump(workers, workers_json)
        workers_json.truncate()


def modify_employee_rule(emp, key, value):
    with open('workers.json', 'r+') as workers_json:
        workers = json.load(workers_json)
        workers[emp.id]['Database'][key] = value
        workers_json.seek(0)
        json.dump(workers, workers_json)
        workers_json.truncate()

    emp.rules[key] = value


def remove_employee_rule(emp, key):
    with open('workers.json', 'r+') as workers_json:
        workers = json.load(workers_json)
        del workers[emp.id]['Database'][key]
        workers_json.seek(0)
        json.dump(workers, workers_json)
        workers_json.truncate()

    del emp.rules[key]


def create_work_week():
    with open('work_weeks.json', 'r+') as work_weeks_json:
        work_weeks = json.load(work_weeks_json)
        ids = []
        for work_week_id in work_weeks.keys():
            ids.append(int(work_week_id))
        if not ids:
            return work_week.WorkWeek(1, get_last_sunday(), get_next_saturday())
        else:
            return work_week.WorkWeek(ids[len(ids) - 1] + 1, get_last_sunday(), get_next_saturday())


def save_work_week(week_to_save):
    with open('work_weeks.json', 'r+') as work_weeks_json:
        work_weeks = json.load(work_weeks_json)
        id = week_to_save.id
        start_date = week_to_save.start_date
        end_date = week_to_save.end_date
        schedule = week_to_save.schedule
        work_weeks[id] = {'Start date': start_date.toordinal(), 'End date': end_date.toordinal(), 'Schedule': schedule}
        work_weeks_json.seek(0)
        json.dump(work_weeks, work_weeks_json)
        work_weeks_json.truncate()


def load_work_week(start_date=None, end_date=None, id=None):
    with open('work_weeks.json', 'r') as work_weeks_json:
        work_weeks = json.load(work_weeks_json)
        if id:
            for current_week_id, current_week in work_weeks.items():
                if str(id) == current_week_id:
                    start_date = current_week['Start date']
                    end_date = current_week['End date']
                    schedule = current_week['Schedule']
                    return work_week.WorkWeek(id, date.fromordinal(start_date), date.fromordinal(end_date), schedule)
        elif start_date:
            for current_week_id, current_week in work_weeks.items():
                if start_date == date.fromordinal(current_week["Start date"]):
                    id = current_week_id
                    end_date = current_week['End date']
                    schedule = current_week['Schedule']
                    return work_week.WorkWeek(id, start_date, date.fromordinal(end_date), schedule)
        elif end_date:
            for current_week_id, current_week in work_weeks.items():
                if end_date == date.fromordinal(current_week["End date"]):
                    id = current_week_id
                    start_date = current_week['Start date']
                    schedule = current_week['Schedule']
                    return work_week.WorkWeek(id, date.fromordinal(start_date), end_date, schedule)


def load_last_week():
    required_start_date = get_last_sunday().toordinal() - 7
    with open('work_weeks.json', 'r') as work_weeks_json:
        work_weeks = json.load(work_weeks_json)
        for current_week_id, current_week in work_weeks.items():
            if required_start_date == current_week['Start date']:
                id = current_week_id
                start_date = date.fromordinal(required_start_date)
                end_date = date.fromordinal(required_start_date + 6)
                schedule = current_week['Schedule']
                return work_week.WorkWeek(id, start_date, end_date, schedule)


def modify_global_rule(key, value):
    pass


def remove_global_rule(key):
    pass
