import json
        
def load_contacts():
    try:
        with open("PROJECT/contact.json","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Contacts file is empty or corrupted. Starting with an empty contact list.")
        return []
        
             
def save_contacts(contacts):
    try:
        with open("PROJECT/contact.json","w") as file:
            json.dump(contacts,file,indent=4)
    except OSError:
        print("Could not save contacts")


def show_contacts(contacts):
    if not contacts:
        print("No contacts Found")
        return
    
    for contact in contacts:
        print(f"{contact["name"]} : {contact["number"]}")  
        
        
def add_contact(contacts,name,number):
    if search_contact(contacts, name):
        print("Contact already exists.")
        return

    contacts.append({"name": name, "number": number})
    save_contacts(contacts)
    print("Contact added successfully.")
 
       
def search_contact(contacts, name):
    for contact in contacts:
        if(contact["name"].lower()==name.lower()):
            return contact  
    return None

        
def update_contact(contacts, name, new_phone):
    contact=search_contact(contacts,name)   
    if contact:
        contact['number']=new_phone
        save_contacts(contacts)
        print("Contact updated successfully.")
    else:
        print("Contact not found.")


def delete_contact(contacts, name):
    contact= search_contact(contacts,name)
    if contact:
        contacts.remove(contact)
        save_contacts(contacts)
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")
        
def is_valid(number):
    return number.isdigit() and len(number)>=10

def main():
    contacts=load_contacts()
    while True:
        print("\n=====Contact Manager=====")
        print("1.Show contact")
        print("2.Add contact")
        print("3.Search contact")
        print("4.Update contact")
        print("5.Delete contact")
        print("6.Exit program")
        
        choice=input("Plz you select 1 to 6 :").strip()
        
        if choice == '1':
            print("\n--- Current Contacts ---")
            show_contacts(contacts)
            
        elif choice == '2':
            name=input("enter contact name :").strip()
            number=input("enter contact number :").strip()
            if not name:
                print("Name cannot be empty.")
            elif not is_valid(number):
                print("Invalid phone number.")
            else:
                add_contact(contacts,name,number)
            
        elif choice=='3':
            name=input("enter contact name :").strip()
            result = search_contact(contacts,name)
            
            if result:
                print(f"Found -> Name: {result['name']}, Phone: {result['number']}")
            else:
                print("Contact not found.")
                
        elif choice=='4':
            name=input("Enter the name of the contact to update: ").strip()
            new_number=input("Enter new phone number: ").strip()
            
            if name and new_number:            
                update_contact(contacts,name,new_number)
            else:
                print("Name and number cannot be empty")
            
            
        elif choice=='5':
            name = input("Enter the name of the contact to delete: ").strip()
            
            if name:
                delete_contact(contacts, name)
            else:
                print("Name cannot be empty.")
            
        elif choice == '6':
            print("Exiting application... Goodbye!")
            break
        
        else:
            print("Invalid option! Please select a number between 1 and 6.")
            
if __name__=="__main__":
    main()
