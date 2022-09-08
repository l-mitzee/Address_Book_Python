"""
    @Author: Lisa Das
    @Date: 2022-09-05
    @Last Modified date: 2022-09-08
    @Title : Create an Address Book
"""

# Importing contacts module
from contacts import Person, AddressBook
from addressbook_collection import MulAddressBook


# Driver code
if __name__ == '__main__':
    print("Welcome to the address book program")
    choice = 1
    address_book = AddressBook()
    address_book_collection = MulAddressBook()
    while choice >= 1 and choice <= 9:
        print("\n1. Add New Person contact\n2. Switch to the Address Book \n3. Edit existing contact details\n4. Delete existing contact details\n5. Searching contacts as per city \n6. Searching contacts as per state\n7. Display contact details \n8. Display Full address book contact details\n")
        choice = int(input("Enter Your Choice: "))

        if(choice == 1):
            while True:
                first = input("Enter your first name: ")
                if not address_book.check_duplicate(first):
                    break
                print("Enter new contact details")
            last = input("Enter your last name: ")
            address = input("Enter your address: ")
            city = input("Enter your city: ")
            state = input("Enter your state: ")
            zip_code = input("Enter zip code: ")
            phone_no = input("Enter your contact number: ")
            email = input("Enter your email address: ")
            list_person = Person(first, last, address, city, state, zip_code, phone_no, email)
            print(list_person.get)
            address_book.add_contact(first, list_person.get)

        elif(choice == 2):
            address_book_name = input("Enter the name of the address book: ")
            address_book = address_book_collection.select_address_book(address_book_name, address_book)
            print("Address Book Added")
            print("Present address Book")
            for ad_book in address_book_collection.show_contacts():
                print(ad_book)

        elif(choice == 3):
            first_name = input("Enter the first name which you want to change: ")
            first = input("Enter your first name: ")
            last = input("Enter your last name: ")
            address = input("Enter your address: ")
            city = input("Enter your city: ")
            state = input("Enter your state: ")
            zip_code = input("Enter zip code: ")
            phone_no = input("Enter your contact number: ")
            email = input("Enter your email address: ")
            edited_list_person = Person(first, last, address, city, state, zip_code, phone_no, email)
            print(edited_list_person.get)
            address_book.edit_contact(first_name, edited_list_person.get) 

        elif(choice == 4):
            first_name_delete = input("Enter the first name which you want to delete: ")
            address_book.delete_contact(first_name_delete)
            print("Contact deleted successfully")     

        elif(choice == 5):
            city_name = input("Enter name of the city ")
            searched_contact = address_book.search_contact_by_city(city_name)
            address_book.print_contact_list(searched_contact)


        elif(choice == 6):
            state_name = input("Enter the name of the state ")
            searched_contact = address_book.search_contact_state(state_name)
            address_book.print_contact_list(searched_contact)

        elif(choice == 7):
            address_book.print_contact_list(address_book.get)

        elif(choice == 8):
            address_book_collection.show_contacts()
            print("All Address Book displayed")
