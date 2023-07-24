class Field:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value

    def matches(self, criteria):
        if criteria is None:
            return True
        return str(self.value) == str(criteria)