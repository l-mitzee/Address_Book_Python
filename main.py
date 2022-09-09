"""
    @Author: Lisa Das
    @Date: 2022-09-09
    @Last Modified date: 2022-09-09
    @Title : Create an Address Book
"""

# Importing contacts module
from contacts import Person, AddressBook

# Driver code
if __name__ == '__main__':
    print("Welcome to the address book program")
    choice = 1
    while choice >= 1 and choice <= 2:
        print("\n1. Add New Person contact\n2. Edit existing contact details\n")
        choice = int(input("Enter Your Choice: "))

        # Adding new Contacts
        if(choice == 1):
            first = input("Enter your first name: ")
            last = input("Enter your last name: ")
            address = input("Enter your address: ")
            city = input("Enter your city: ")
            state = input("Enter your state: ")
            zip_code = int(input("Enter zip code: "))
            phone_no = int(input("Enter your contact number: "))
            email = input("Enter your email address: ")
            list_person = Person(first, last, address, city, state, zip_code, phone_no, email)
            address_book = AddressBook()
            print(list_person.get)
            address_book.add_contact(list_person.get)
            
        # Editing existing contact
        elif(choice == 2):
            first_name = input("Enter the first name which you want to change: ")
            first = input("Enter your first name: ")
            last = input("Enter your last name: ")
            address = input("Enter your address: ")
            city = input("Enter your city: ")
            state = input("Enter your state: ")
            zip_code = int(input("Enter zip code: "))
            phone_no = int(input("Enter your contact number: "))
            email = input("Enter your email address: ")
            edited_list_person = Person(first, last, address, city, state, zip_code, phone_no, email)
            address_book = AddressBook()
            print(edited_list_person.get)
            address_book.edit_contact(first_name, edited_list_person)
