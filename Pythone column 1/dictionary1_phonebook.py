#Initialize empty phonebook dictionary
phonebook={}

#Function to add a contact
def add_contact(name,number):
    phonebook[name]=number 
    #[name]This is the key that you are using to store the contact in the dictionary. In this case, it would be the name of the person you're adding to the phonebook.
    #number-This is the value associated with the key (the name). It's the phone number that corresponds to the contact you're adding.
    print (f"Contact '{name}' added with number '{number}'.")

# Function to remove a contact
def remove_contact(name):
    if name in phonebook:
        del phonebook[name]
        print(f"Contact '{name}' removed")
    else:
        print(f"Contact '{name}' not found")

#display all contacts
def display_contacts():
    print("Phonebook")
    for name, number in phonebook.items():#phonebook.items(): This method returns a view of the dictionary’s key-value pairs. It gives you a list of tuples where each tuple consists of:
        #The key (in this case, the name of the contact, like "Alice").
        #The value (in this case, the phone number associated with the contact, like "555-1111").
        print (f"{name}:{number}")

# Adding contacts
add_contact("Alice", "123-456-7890")
add_contact("Bob", "987-654-3210")
add_contact("Charlie", "555-555-5555")

# Displaying contacts
display_contacts()

# Removing a contact
remove_contact("Bob")

# Displaying contacts again
display_contacts()

# View the entire dictionary
print(phonebook)