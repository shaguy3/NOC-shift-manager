class Employee:

    def __init__(self, id, name, rules=None):
        if rules is None:
            rules = {}
        self.id = id
        self.name = name
        self.rules = rules

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if self.id == other.id:
            return True
        else:
            return False
