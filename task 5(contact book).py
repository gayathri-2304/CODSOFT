def is_valid_email(email):
  """Checks if the email format is valid."""
  return "@" in email and "." in email.split("@")[-1]

def is_valid_name(name):
  """Checks if the name contains at least one alphabet."""
  return any(char.isalpha() for char in name)

def is_valid_phone_number(phone_number):
  """Checks if the phone number is 10 digits long and numeric."""
  return phone_number.isdigit() and len(phone_number) == 10

def add_contact(contacts, name, phone_number, email, address):
  errors = []  # List to store encountered errors

  # Validate name
  if not is_valid_name(name):
    errors.append("Error: Name must contain at least one alphabet.")

  # Validate email immediately after input
  if not is_valid_email(email):
    errors.append("Error: Invalid email format. Email must contain '@' and '.'.")

  # Validate phone number
  if not is_valid_phone_number(phone_number):
    errors.append("Error: Invalid phone number. Phone number must be 10 digits long and numeric.")

  # Check if any errors occurred
  if errors:
    print("Encountered errors:")
    for error in errors:
      print(error)
    return  # Exit the function if errors exist

  # Add contact if no errors
  contacts.append({
      'name': name,
      'phone_number': phone_number,
      'email': email,
      'address': address
  })
  print("Contact added successfully!")

def display_contacts(contacts):
    if not contacts:
        print("Contact book is empty.")
    else:
        print("Contacts:")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. Name: {contact['name']}")
            print(f"   Phone Number: {contact['phone_number']}")
            print(f"   Email: {contact['email']}")
            print(f"   Address: {contact['address']}")
            print()

def search_contact(contacts, search_term):
    search_results = []
    for contact in contacts:
        if search_term.lower() in contact['name'].lower() or search_term in contact['phone_number']:
            search_results.append(contact)
    return search_results

def update_contact(contacts, name):
  updated_contacts = 0
  for contact in contacts:
    if contact['name'].lower() == name.lower():
      print(f"Found contact: {contact['name']}")
      while True:
        print("\nWhat information do you want to update?")
        print("1. Name")
        print("2. Phone Number")
        print("3. Email")
        print("4. Address")
        print("5. Exit Update")
        update_choice = input("Enter your choice: ")

        if update_choice in ('1', '2', '3', '4'):
          # Update specific field based on choice
          if update_choice == '1':
            contact['name'] = input("Enter new name: ")
          elif update_choice == '2':
            contact['phone_number'] = input("Enter new phone number: ")
          elif update_choice == '3':
            contact['email'] = input("Enter new email: ")
          elif update_choice == '4':
            contact['address'] = input("Enter new address: ")
          print("Information updated successfully!")
          updated_contacts += 1
        elif update_choice == '5':
          if updated_contacts > 0:
            print(f"{updated_contacts} details of contact(s) updated successfully!")
          else:
            print("No updates made.")
          return  # Exit the function after updates
        else:
          print("Invalid choice. Please enter a number between 1 and 6.")

  # Contact not found message
  print("Contact not found.")
  
def delete_contact(contacts, name):
    for idx, contact in enumerate(contacts):
        if contact['name'].lower() == name.lower():
            del contacts[idx]
            print("Contact deleted successfully!")
            return
    print("Contact not found.")
    
contacts = []
while True:
    print("1. Add a new contact")
    print("2. Display contacts")
    print("3. Search for a contact")
    print("4. Update contact details")
    print("5. Delete a contact")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        add_contact(contacts, name, phone_number, email, address)
    elif choice == '2':
        display_contacts(contacts)
    elif choice == '3':
        search_term = input("Enter name or phone number to search: ")
        search_results = search_contact(contacts, search_term)
        if search_results:
            print("Search results:")
            for idx, contact in enumerate(search_results, start=1):
                print(f"{idx}. Name: {contact['name']}")
                print(f"   Phone Number: {contact['phone_number']}")
                print(f"   Email: {contact['email']}")
                print(f"   Address: {contact['address']}")
                print()
        else:
            print("No matching contacts found.")
    elif choice == '4':
        name = input("Enter name of the contact to update: ")
        update_contact(contacts, name)
    elif choice == '5':
        name = input("Enter name of the contact to delete: ")
        delete_contact(contacts, name)
    elif choice == '6':
        print("Exiting...")
        break
    else:
            print("Invalid choice. Please enter a number between 1 and 6.")
