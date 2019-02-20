import json
import os


class Worker:

    def __init__(self, name='', id=0):
        with open(os.path.join('..', 'Rules', 'workers.json'), 'r+') as workers_json:
            workers = json.load(workers_json)
            if not id == 0:
                id_checker = id
                name = workers[str(id)]['Name']
                rules = workers[str(id)]['Rules']
            else:
                rules = {}
                taken_ids = []
                for worker_id in workers.keys():
                    taken_ids.append(worker_id)
                id_checker = '1'
                while id_checker in taken_ids:
                    id_checker = str(int(id_checker) + 1)
                self.save_worker()

        self.id = id_checker
        self.name = name
        self.rules = rules

    def __repr__(self):
        return self.name

    def save_worker(self):
        with open(os.path.join('..', 'Rules', 'workers.json'), 'r+') as workers_json:
            workers = json.load(workers_json)
            workers[self.id] = {'Name': self.name, 'Rules': {}}
            workers_json.seek(0)
            json.dump(workers, workers_json)
            workers_json.truncate()

    def modify_rule(self, key, value):
        with open(os.path.join('..', 'Rules', 'workers.json'), 'r+') as workers_json:
            workers = json.load(workers_json)
            workers[self.id]['Rules'][key] = value
            workers_json.seek(0)
            json.dump(workers, workers_json)
            workers_json.truncate()

        self.rules[key] = value

    def remove_rule(self, key):
        with open(os.path.join('..', 'Rules', 'workers.json'), 'r+') as workers_json:
            workers = json.load(workers_json)
            del workers[self.id]['Rules'][key]
            workers_json.seek(0)
            json.dump(workers, workers_json)
            workers_json.truncate()

        del self.rules[key]


guy = Worker(id=6)
print(guy)
