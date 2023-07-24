from collections import UserDict

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find_records(self, **criteria):
        matching_records = []
        for record in self.data.values():
            if all(field.matches(criteria.get(field.name)) for field in record.fields):
                matching_records.append(record)
        return matching_records