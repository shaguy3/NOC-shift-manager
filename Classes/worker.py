import json
import os


class Worker:

    def __init__(self, name):
        with open(os.path.join('..', 'Rules', 'workers.json'), 'r+') as workers_json:
            workers = json.load(workers_json)
            taken_ids = []
            for worker_id in workers.keys():
                taken_ids.append(worker_id)
            open_id_checker = '1'
            while open_id_checker in taken_ids:
                open_id_checker = str(int(open_id_checker) + 1)
            workers[open_id_checker] = {'Name': name, 'Rules': {}}
            workers_json.seek(0)
            json.dump(workers, workers_json)
            workers_json.truncate()

    def __repr__(self):
        pass

    def add_rule(self, key, value):
        pass

    def modify_rule(self, key, value):
        pass

    def remove_rule(self, key):
        pass


test = Worker('test')
