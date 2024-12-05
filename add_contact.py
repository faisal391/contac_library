def add_contact(self):
    """Add a new contact with error handling."""
    try:
        name = input("Enter Name: ").strip()
        if not name.replace(" ", "").isalpha():
            raise ValueError("Error: Name must only contain letters and spaces.")

        email = input("Enter Email: ").strip()
        if "@" not in email or "." not in email:
            raise ValueError("Error: Invalid email format. Ensure it includes '@' and a domain (e.g., example@domain.com).")

        phone = input("Enter Phone Number: ").strip()
        if not phone.isdigit():
            raise ValueError("Error: Phone number must be numeric.")
        if any(contact['Phone'] == phone for contact in self.contacts):
            raise ValueError("Error: Phone number already exists in the contact book.")

        address = input("Enter Address: ").strip()
        if not address:
            raise ValueError("Error: Address cannot be empty.")

        # Add the validated contact
        self.contacts.append({"Name": name, "Email": email, "Phone": phone, "Address": address})
        self.save_contacts()
        print("Contact added successfully!")
    except ValueError as e:
        print(e)
