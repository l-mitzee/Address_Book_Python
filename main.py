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
        choice = int(input("Enter Your Choice or press 0 to exit: "))
        if(choice == 1):
            first = input("Enter your first name: ")
            last = input("Enter your last name: ")
            address = input("Enter your address: ")
            city = input("Enter your city: ")
            state = input("Enter your state: ")
            zip = int(input("Enter zip code: "))
            phone_no = int(input("Enter your contact number: "))
            email = input("Enter your email address: ")
            list_person = contacts.Person(first, last, address, city, state, zip, phone_no, email)
            list_person.addNewPerson()

        elif(choice == 2):
            print("\n")
            for list_person in person.getPersonList():
                print(list_person)