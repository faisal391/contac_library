import csv
import os

class ContactManager:
    def __init__(self):
        self.contacts = []
        self.file_name = "contacts.csv"

    def load_contacts(self):
        """Load contacts from file."""
        if os.path.exists(self.file_name):
            with open(self.file_name, mode="r") as file:
                reader = csv.DictReader(file)
                self.contacts = [row for row in reader]
        else:
            print(f"No existing contact file found. Starting fresh.")

    def save_contacts(self):
        """Save contacts to file."""
        with open(self.file_name, mode="w", newline="") as file:
            fieldnames = ["Name", "Email", "Phone", "Address"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.contacts)

    def add_contact(self):
        """Add a new contact."""
        name = input("Enter Name: ").strip()
        email = input("Enter Email: ").strip()
        phone = input("Enter Phone Number: ").strip()
        address = input("Enter Address: ").strip()

        if not name.isalpha():
            print("Error: Name must be a string.")
            return
        if not phone.isdigit():
            print("Error: Phone number must be numeric.")
            return
        if any(contact['Phone'] == phone for contact in self.contacts):
            print("Error: Phone number already exists.")
            return

        self.contacts.append({"Name": name, "Email": email, "Phone": phone, "Address": address})
        self.save_contacts()
        print("Contact added successfully!")

    def view_contacts(self):
        """Display all contacts."""
        if not self.contacts:
            print("No contacts available.")
            return

        print("\nContacts:")
        print(f"{'Name':<20}{'Email':<30}{'Phone':<15}{'Address':<30}")
        print("-" * 95)
        for contact in self.contacts:
            print(f"{contact['Name']:<20}{contact['Email']:<30}{contact['Phone']:<15}{contact['Address']:<30}")

    def remove_contact(self):
        """Remove a contact."""
        phone = input("Enter the phone number of the contact to remove: ").strip()
        for contact in self.contacts:
            if contact['Phone'] == phone:
                self.contacts.remove(contact)
                self.save_contacts()
                print("Contact removed successfully!")
                return
        print("Error: Contact not found.")

    def search_contact(self):
        """Search for a contact."""
        search_term = input("Enter a name, email, or phone number to search: ").strip()
        results = [contact for contact in self.contacts if search_term in contact.values()]

        if not results:
            print("No matching contacts found.")
        else:
            print("\nSearch Results:")
            print(f"{'Name':<20}{'Email':<30}{'Phone':<15}{'Address':<30}")
            print("-" * 95)
            for contact in results:
                print(f"{contact['Name']:<20}{contact['Email']:<30}{contact['Phone']:<15}{contact['Address']:<30}")