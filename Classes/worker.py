class Worker:

    id = 1

    def __init__(self, name):
        self.id = Worker.id
        self.name = name

    def __repr__(self):
        return self.name
