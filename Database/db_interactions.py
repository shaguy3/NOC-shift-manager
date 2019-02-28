from Classes import employee, work_week
import json
from datetime import date
import os


def get_last_sunday():
    """documentation"""
    today = date.today()
    ordinal_today = today.toordinal()
    last_sunday_ordinal = ordinal_today - (ordinal_today % 7)
    return date.fromordinal(last_sunday_ordinal)


def get_next_saturday():
    """documentation"""
    today = date.today()
    ordinal_today = today.toordinal()
    next_saturday_ordinal = ordinal_today - (ordinal_today % 7) + 6
    return date.fromordinal(next_saturday_ordinal)


def create_employee(name, cwd=os.getcwd()):
    """documentation"""
    os.chdir(os.path.join('..', 'Database'))
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
        os.chdir(cwd)
        return emp


def save_employee(emp, cwd=os.getcwd()):
    """documentation"""
    os.chdir(os.path.join('..', 'Database'))
    with open('workers.json', 'r+') as workers_json:
        workers = json.load(workers_json)
        workers[emp.id] = {'Name': emp.name, 'Database': {}}
        workers_json.seek(0)
        json.dump(workers, workers_json)
        workers_json.truncate()
        os.chdir(cwd)


def load_employee(name, cwd=os.getcwd()):
    """documentation"""
    os.chdir(os.path.join('..', 'Database'))
    with open('workers.json', 'r+') as workers_json:
        workers = json.load(workers_json)
        for id, worker in workers.items():
            if worker['Name'] == name:
                id = id
                rules = worker['Rules']
                os.chdir(cwd)
                return employee.Employee(id, name, rules=rules)
        os.chdir(cwd)
        return None


def remove_employee(emp, cwd=os.getcwd()):
    """documentation"""
    os.chdir(os.path.join('..', 'Database'))
    with open('workers.json', 'r+') as workers_json:
        workers = json.load(workers_json)
        del workers[emp.id]
        workers_json.seek(0)
        json.dump(workers, workers_json)
        workers_json.truncate()
        os.chdir(cwd)


def modify_employee_rule(emp, key, value, cwd=os.getcwd()):
    """documentation"""
    os.chdir(os.path.join('..', 'Database'))
    with open('workers.json', 'r+') as workers_json:
        workers = json.load(workers_json)
        workers[emp.id]['Database'][key] = value
        workers_json.seek(0)
        json.dump(workers, workers_json)
        workers_json.truncate()

    emp.rules[key] = value
    os.chdir(cwd)


def remove_employee_rule(emp, key, cwd=os.getcwd()):
    """documentation"""
    os.chdir(os.path.join('..', 'Database'))
    with open('workers.json', 'r+') as workers_json:
        workers = json.load(workers_json)
        del workers[emp.id]['Database'][key]
        workers_json.seek(0)
        json.dump(workers, workers_json)
        workers_json.truncate()

    del emp.rules[key]
    os.chdir(cwd)


def create_work_week(cwd=os.getcwd()):
    """documentation"""
    os.chdir(os.path.join('..', 'Database'))
    with open('work_weeks.json', 'r+') as work_weeks_json:
        work_weeks = json.load(work_weeks_json)
        ids = []
        for work_week_id in work_weeks.keys():
            ids.append(int(work_week_id))
        if not ids:
            os.chdir(cwd)
            return work_week.WorkWeek(1, get_last_sunday(), get_next_saturday())
        else:
            os.chdir(cwd)
            return work_week.WorkWeek(ids[len(ids) - 1] + 1, get_last_sunday(), get_next_saturday())


def save_work_week(week_to_save, cwd=os.getcwd()):
    """documentation"""
    os.chdir(os.path.join('..', 'Database'))
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
    os.chdir(cwd)


def load_work_week(start_date=None, end_date=None, id=None, cwd=os.getcwd()):
    """documentation"""
    os.chdir(os.path.join('..', 'Database'))
    with open('work_weeks.json', 'r') as work_weeks_json:
        work_weeks = json.load(work_weeks_json)
        if id:
            for current_week_id, current_week in work_weeks.items():
                if str(id) == current_week_id:
                    start_date = current_week['Start date']
                    end_date = current_week['End date']
                    schedule = current_week['Schedule']
                    os.chdir(cwd)
                    return work_week.WorkWeek(id, date.fromordinal(start_date), date.fromordinal(end_date), schedule)
        elif start_date:
            for current_week_id, current_week in work_weeks.items():
                if start_date == date.fromordinal(current_week["Start date"]):
                    id = current_week_id
                    end_date = current_week['End date']
                    schedule = current_week['Schedule']
                    os.chdir(cwd)
                    return work_week.WorkWeek(id, start_date, date.fromordinal(end_date), schedule)
        elif end_date:
            for current_week_id, current_week in work_weeks.items():
                if end_date == date.fromordinal(current_week["End date"]):
                    id = current_week_id
                    start_date = current_week['Start date']
                    schedule = current_week['Schedule']
                    os.chdir(cwd)
                    return work_week.WorkWeek(id, date.fromordinal(start_date), end_date, schedule)
        os.chdir(cwd)
        return None


def load_last_week(cwd=os.getcwd()):
    """documentation"""
    os.chdir(os.path.join('..', 'Database'))
    required_start_date = get_last_sunday().toordinal() - 7
    with open('work_weeks.json', 'r') as work_weeks_json:
        work_weeks = json.load(work_weeks_json)
        for current_week_id, current_week in work_weeks.items():
            if required_start_date == current_week['Start date']:
                id = current_week_id
                start_date = date.fromordinal(required_start_date)
                end_date = date.fromordinal(required_start_date + 6)
                schedule = current_week['Schedule']
                os.chdir(cwd)
                return work_week.WorkWeek(id, start_date, end_date, schedule)


def load_global_rule(key, cwd=os.getcwd()):
    """documentation"""
    os.chdir(os.path.join('..', 'Database'))
    with open('global_rules.json', 'r') as global_rules_json:
        global_rules = json.load(global_rules_json)
        for category, rules in global_rules.items():
            for rule_key, rule_value in rules.items():
                if key == rule_key:
                    os.chdir(cwd)
                    return rule_value
    os.chdir(cwd)
    return None


def modify_global_rule(key, value):
    pass


def remove_global_rule(key):
    pass
