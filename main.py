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
    person = contacts.Person("Lisa", "Das", "Sarjapur", "Bangalore", "Karnataka", 560001, 6295196004, "lisa.das9374@gmail.com")
    print(person)