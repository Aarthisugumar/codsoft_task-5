def add_contact(contact):
    name=input("Enter Name: ")
    ph_no=int(input("Enter Phone Number: "))
    email=input("Enter Email: ")
    address=input("Enter Address: ")
    contact[name]={"phone_no":ph_no,"email":email,"address":address}
    print("Contact {} added successfully.".format(name))
    
def view_contact(contact):
    if not contact:
        print("No contacts to display.")
    else:
        for name, details in contact.items():
            print(f"Name: {name}, Phone: {details['phone_no']}")


def search_contact(contact,search_term):
    found = False
    for name, details in contact.items():
        if name == search_term or details['phone_no'] == search_term:
            print(f"Name: {name}, Phone: {details['phone_no']}, Email: {details['email']}, Address: {details['address']}")
            found = True
            break
    if not found:
        print("Contact not found.")

def update_contact(contact):
    name = input("Enter the name of the contact to update: ")
    if name in contact:
        ph_no = input("Enter new phone number: ")
        email = input("Enter new email address: ")
        address = input("Enter new address: ")
        contact[name] = {'phone_no': ph_no, 'email': email, 'address': address}
        print(f"Contact '{name}' updated successfully.")
    else:
        print("Contact not found.")

def delete_contact(contact):
    name = input("Enter the name of the contact to delete: ")
    if name in contact:
        del contact[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print("Contact not found.")

def main():
    contact = {}
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_contact(contact)
        elif choice == '2':
            view_contact(contact)
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            search_contact(contact, search_term)
        elif choice == '4':
            update_contact(contact)
        elif choice == '5':
            delete_contact(contact)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
