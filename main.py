"""
    @Author: Lisa Das
    @Date: 2022-08-31
    @Last Modified date: 2022-09-02
    @Title : Create an Address Book
"""

# Importing contacts module
from contacts import Person, AddressBook

# Driver code
if __name__ == '__main__':
    print("Welcome to the address book program")
    choice = 1
    address_book = AddressBook()
    while choice >= 1 and choice <= 5:
        print("\n1. Add New Person contact\n2. Edit existing contact details\n3. Delete existing contact details\n4. Display existing contact details\n\n")
        choice = int(input("Enter Your Choice: "))
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
            print(list_person.get)
            address_book.add_contact(list_person.get)

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
            print(edited_list_person.get)
            address_book.edit_contact(first_name, edited_list_person.get) 

        elif(choice == 3):
            first_name_delete = input("Enter the first name which you want to delete: ")
            address_book.delete_contact(first_name_delete)
            print("Contact deleted successfully")     

        elif(choice == 4):
            address_book.print_contact_list(address_book.get)