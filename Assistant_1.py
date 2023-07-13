class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find_records(self, **criteria):
        matching_records = []
        for record in self.data.values():
            if all(field.matches(criteria.get(field.name)) for field in record.fields):
                matching_records.append(record)
        return matching_records


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.fields = []

    def add_field(self, field):
        self.fields.append(field)

    def delete_field(self, field_name):
        for field in self.fields:
            if field.name == field_name:
                self.fields.remove(field)
                break

    def edit_field(self, field_name, new_value):
        for field in self.fields:
            if field.name == field_name:
                field.value = new_value
                break


class Field:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value

    def matches(self, criteria):
        if criteria is None:
            return True
        return str(self.value) == str(criteria)


class Name:
    def __init__(self, value):
        self.value = value


class Phone(Field):
    pass
