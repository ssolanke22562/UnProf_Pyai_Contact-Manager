import json
import os

# Define the storage file
DATA_FILE = "contacts.json"

def load_contacts():
    """Loads contacts from the JSON file. Returns an empty list if not found."""
    if not os.path.exists(DATA_FILE):
        return []
    
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Warning: contacts.json is corrupted. Starting with an empty list.")
        return []

def save_contacts(contacts):
    """Saves the current list of contacts to the JSON file."""
    with open(DATA_FILE, 'w') as file:
        # indent=4 makes the JSON file human-readable
        json.dump(contacts, file, indent=4) 

def add_contact(contacts):
    """Prompts the user to add a new contact."""
    print("\n--- Add New Contact ---")
    name = input("Name: ").strip()
    
    if not name:
        print("Error: Name cannot be empty.")
        return

    phone = input("Phone Number: ").strip()
    email = input("Email Address: ").strip()
    notes = input("Other details/Notes: ").strip()

    new_contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "notes": notes
    }
    
    contacts.append(new_contact)
    save_contacts(contacts)
    print(f"\n✅ Success: '{name}' has been added to your contacts.")

def search_contacts(contacts):
    """Searches for a contact by checking all fields."""
    print("\n--- Search Contacts ---")
    if not contacts:
        print("Your contact list is currently empty.")
        return

    query = input("Enter name, phone, or detail to search: ").strip().lower()
    
    # Filter contacts where the query string exists in ANY of the dictionary values
    results = [
        contact for contact in contacts 
        if any(query in str(value).lower() for value in contact.values())
    ]

    if results:
        print(f"\n🔍 Found {len(results)} matching contact(s):")
        print("-" * 30)
        for idx, contact in enumerate(results, 1):
            print(f"{idx}. Name:  {contact['name']}")
            print(f"   Phone: {contact.get('phone', 'N/A')}")
            print(f"   Email: {contact.get('email', 'N/A')}")
            if contact.get('notes'):
                print(f"   Notes: {contact['notes']}")
            print("-" * 30)
    else:
        print(f"\n❌ No contacts found matching '{query}'.")

def main():
    """Main loop for the CLI menu."""
    contacts = load_contacts()
    
    while True:
        print("\n" + "="*25)
        print(" 📖 CONTACT MANAGER CLI ")
        print("="*25)
        print("1. Add a new contact")
        print("2. Search for a contact")
        print("3. View all contacts")
        print("4. Exit")
        print("="*25)
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            search_contacts(contacts)
        elif choice == '3':
            # Searching with an empty string returns all items
            print("\n--- All Contacts ---")
            if not contacts:
                print("Your contact list is empty.")
            else:
                for contact in contacts:
                    print(f"• {contact['name']} | {contact['phone']} | {contact['email']}")
        elif choice == '4':
            print("\nExiting Contact Manager. Goodbye!")
            break
        else:
            print("\n⚠️ Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()