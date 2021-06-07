import os
import sys
import re
from prettytable import PrettyTable
from email_validator import validate_email, EmailNotValidError

# Class Contact
class Contact(object):
    def __init__(self,name,number,email):
        self.name=name
        self.number=number
        self.email=email

# Function to add a new contact
def add_contact():

    name_pattern = r'([a-zA-Z])\D*([a-zA-Z])$'
    name = input("Please enter name: ")
    if re.search(name_pattern, name):
        print("Name is valid ")
    else:
        print("Please enter a valid name,it must be a string")
        name = input("Please enter name: ")

    number_pattern = r'^(\d{10})(?:\s|$)'
    number = input("Please enter phone number: ")
    for i in range(0, len(contacts)):
        each_contact = contacts[i]
        if each_contact.number == number:
            print("Phone number already exist")
            show_contact()
            sys.exit()
    if re.search(number_pattern, number):
        print("Phone number is valid")
    else:
        print("The phone number is not valid. It must have ten digits.")
        number = input("Please enter phone number: ")

    email = input("Please enter email id:")
    for j in range(0, len(contacts)):
        each_contact = contacts[j]
        if each_contact.email== email:
            print("Email id already exist")
            show_contact()
            sys.exit()

    try:
        # Validate.
        valid = validate_email(email)
        # Update with the normalized form.
        email = valid.email
    except EmailNotValidError as e:
        # email is not valid, exception message
        print(str(e))
        email = input("Please enter email id: ")

    contacts.append(Contact(name,number,email))
# Function to show the contact
def show_contact():
    contact_table = PrettyTable(['Pos','Name','Number','Email'])
    contacts.sort(reverse=False, key=name)
    for contact in contacts:
        contact_table.add_row([contacts.index(contact) + 1, contact.name, contact.number,contact.email])
    print(contact_table)

# Function to remove a contact
def delete_contact():
    if not contacts:
        print("List is empty!")
    else:

        number1 = str(input("Enter the phone number that present in the contact list which is to be removed: "))
        confirm=input("Do you want to delete the selected contact list? Yes/No:")
        if confirm == 'yes':
            for k in range(0, len(contacts)):
                each_contact = contacts[k]
                if each_contact.number == number1:
                    del contacts[k]
                    print("Contact deleted")
        
# For sorting
def name(club):
    return club.name

# Function to take input
def take_input():
    print("\n\t1.Add contact\n\t2.Show contact\n\t3.Delete contact\n\t4.Quit\n")
    action = input("Please select desired action (1/2/3/4) :- ")
    contact_dict[action]()

# Clearing the console
def clear():
    os.system('cls')
# Closing the program
def quit_program():
    sys.exit()

# The main function
def main():

    global contact_dict, contacts
    clear()
    # Contact list
    contacts = []
    # Possible inputs
    contact_dict = {

        '1': add_contact,
        '2': show_contact,
        '3': delete_contact,
        '4': quit_program,
    }

    # Getting input for a desired action
    while True:
        take_input()

if __name__ == '__main__':
    main()