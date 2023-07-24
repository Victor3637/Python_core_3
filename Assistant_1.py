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


def parse_command(string):
    parts = string.split()
    command = parts[0]
    args = parts[1:]
    return command, args


def handle_hello(args):
    return "How can I help you?"


def handle_add(args, address_book):
    if len(args) < 2:
        raise ValueError("Please provide a name and phone number.")
    name = args[0]
    phone_number = " ".join(args[1:])
    record = Record(name)
    record.add_field(Phone("phone", phone_number))
    address_book.add_record(record)
    return "Contact added successfully."


def handle_change(args, address_book):
    if len(args) < 2:
        raise ValueError("Please provide a name and new phone number.")
    name = args[0]
    matching_records = address_book.find_records(name=name)
    if not matching_records:
        raise KeyError(f"No contact found with the name '{name}'.")
    phone_number = " ".join(args[1:])
    for record in matching_records:
        record.edit_field("phone", phone_number)
    return "Phone number updated successfully."


def handle_phone(args, address_book):
    if len(args) < 1:
        raise ValueError("Please provide a name to retrieve the phone number.")
    name = args[0]
    matching_records = address_book.find_records(name=name)
    if not matching_records:
        raise KeyError(f"No contact found with the name '{name}'.")
    return f"The phone number for {name} is {matching_records[0].fields[0].value}."


def handle_show_all(a, address_book):
    if len(address_book) == 0:
        return "The phone book is empty."
    contacts = "\n".join([f"{record.name.value}: {record.fields[0].value}" for record in address_book.values()])
    return f"Phone book contacts:\n{contacts}"


def handle_close(a):
    return "Good bye!"


command_list = {
    "hello": handle_hello,
    "hi": handle_hello,
    "add": handle_add,
    "change": handle_change,
    "phone": handle_phone,
    "show_all": handle_show_all,
    "close": handle_close,
    "good bye": handle_close,
    "exit": handle_close
}


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            return f"No contact found: {str(e)}"
        except ValueError as e:
            return f"Invalid input: {str(e)}"
        except IndexError as e:
            return f"Invalid input: {str(e)}"
    return wrapper


@input_error
def handle_command(command, args, address_book):
    if command in command_list:
        return command_list[command](args, address_book)
    else:
        raise ValueError("Invalid command.")


def main():
    address_book = AddressBook()
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_command(user_input)
        if command.lower() in ["good bye", "close", "exit"]:
            print(handle_command("close", [], address_book))
            break
        else:
            print(handle_command(command.lower(), args, address_book))


#if __name__ == "__main__":
    main()
