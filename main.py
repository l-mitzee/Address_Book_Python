"""
    @Author: Lisa Das
    @Date: 2022-08-31
    @Last Modified time: 2022-09-02
    @Title : Create an Address Book
"""

# Importing contacts module
from contacts import Person, AddressBook

# Driver code
if __name__ == '__main__':
    print("Welcome to the address book program")
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    address = input("Enter your address: ")
    city = input("Enter your city: ")
    state = input("Enter your state: ")
    zip_code = int(input("Enter zip code: "))
    phone_no = int(input("Enter your contact number: "))
    email = input("Enter your email address: ")
    list_person = Person(first, last, address, city, state, zip_code, phone_no, email)
    print(type(list_person))
    address_book = AddressBook()
    print(list_person.get)
    address_book.add_contact(list_person.get)