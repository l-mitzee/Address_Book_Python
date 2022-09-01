"""
    @Author: Lisa Das
    @Date: 2022-08-31
    @Last Modified time: 2022-09-01
    @Title : Create an Address Book
"""

# Importing contacts module
import contacts

# Driver code
if __name__ == '__main__':
    print("Welcome to the address book program")
    choice = 1
    person = contacts.Person("", "", "", "", "", 0, 0, "")
    while choice >= 1 and choice <= 2:
        print("\n1. Add New Person contact\n2. Get All Person Contact List\n")
        choice = int(input("Enter Your Choice: "))
        if(choice == 1):
            first = input("Enter your first name: ")
            last = input("Enter your last name: ")
            address = input("Enter your address: ")
            city = input("Enter your city: ")
            state = input("Enter your state: ")
            zip = int(input("Enter zip code: "))
            phone_no = int(input("Enter your contact number: "))
            email = input("Enter your email address: ")
            person = contacts.Person(first, last, address, city, state, zip, phone_no, email)
            person.addNewPerson

        elif(choice == 2):
            print("\n")
            for person in person.getPersonList():
                print(person)