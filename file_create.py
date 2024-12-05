import csv


class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def save(self, contacts):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["Name", "Email", "Phone", "Address"])
            writer.writeheader()
            writer.writerows(contacts)

    def load(self):
        try:
            with open(self.filename, 'r') as file:
                reader = csv.DictReader(file)
                return [row for row in reader]
        except FileNotFoundError:
            return []




def validate_input(value, value_type):
    try:
        value_type(value)
        return True
    except ValueError:
        return False
