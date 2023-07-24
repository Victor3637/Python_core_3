from name import Name

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