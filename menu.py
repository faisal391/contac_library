from contact_book import ContactManager


def main():
    contact_book = ContactManager()
    contact_book.load_contacts()  # Load existing contacts from the file

    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Remove Contact")
        print("4. Search Contact")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':

            contact_book.add_contact()
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            contact_book.remove_contact()
        elif choice == '4':
            contact_book.search_contact()
        elif choice == '5':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")


if __name__ == "__main__":
    main()
