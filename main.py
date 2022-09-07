"""
    @Author: Lisa Das
    @Date: 2022-09-05
    @Last Modified date: 2022-09-06
    @Title : Create an Address Book and modifying with conditions
"""

# Importing contacts module
from contacts import Person, AddressBook
from addressbook_collection import MulAddressBook

def main():
    print("Welcome to the address book program")
    choice = 1
    address_book = AddressBook()
    address_book_collection = MulAddressBook()
    while choice >= 1 and choice <= 9:
        print("""
        1. Add New Person contact
        2. Switch to the Address Book
        3. Edit existing contact details
        4. Delete existing contact details
        5. Searching contacts as per city
        6. View contact details as per city
        7. Searching contacts as per state
        8. View contact details as per state
        9. Display contact details
        10. Display Full address book contact details\n""")

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

        elif(choice == 3):
            first = input("Enter the first name which you want to change: ")
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
            address_book.edit_contact(first, edited_list_person.get) 

        elif(choice == 4):
            first_name_delete = input("Enter the first name which you want to delete: ")
            address_book.delete_contact(first_name_delete)
            print("Contact deleted successfully")     

        elif(choice == 5):
            city_name = input("Enter name of the city ")
            searched_contact = address_book.search_contact_by_city(city_name)
            print(searched_contact)
            
        elif(choice == 6):
            list_of_city = address_book.view_city()
            for city in list_of_city:
                print("Name of the city: ", city)
                contact_list_city = address_book.search_contact_by_city(city)
                print("Total number of contact present in the state: ", len(contact_list_city))
                for contact in contact_list_city:
                    for key in contact:
                        print(key, ' : ', contact[key])

        elif(choice == 7):
            state_name = input("Enter the name of the state ")
            searched_contact = address_book.search_contact_state(state_name)
            print(searched_contact)
                
        elif(choice == 8):
            list_of_state = address_book.view_state()
            for state in list_of_state:
                print("Name of the city: ", state)
                contact_list_state = address_book.search_contact_state(state)
                print("Total number of contact present in the state: ", len(contact_list_state))
                for contact in contact_list_state:
                    for key in contact:
                        print(key, ' : ', contact[key])


        elif(choice == 9):
            address_book.display_contact()

        elif(choice == 10):
            address_book_collection.show_contacts()
            print("All Address Book displayed")


# Driver code
if __name__ == '__main__':
    main()