from Classes import employee
import json


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
                rules = worker['Database']
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
