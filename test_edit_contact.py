"""
    @Author: Lisa Das
    @Date: 2022-09-09
    @Last Modified time: 2022-09-09
    @Title : Testing add contact method
"""

#importing unit test and contacts module
import unittest
from contacts import Person, AddressBook

class TestEditContact(unittest.TestCase):
    def test_edit_contact(self):
        # Test area to check contact is present in the existing contact list or not
        address_book = AddressBook()
        list_of_person = Person('Leo', 'De','Electronic City', 'Bangalore', 'Karnataka', '560001', '7890002345', 'leo.d@gmail.com')
        self.assertTrue(list_of_person.get in address_book.contacts) 
        self.assertFalse(list_of_person.get not in address_book.contacts) 

    def test_type(self):
        # Test area to raise type error for phone number and zip code if it is not integer
        address_book = AddressBook()
        person_list = Person('Rio', 'Kio', 'Berhampur', 'Murshidabad', 'West Bengal', '741128', '983256470', 'rio.kio@gmail.com')
        self.assertRaises(TypeError, address_book.edit_contact, person_list)


if __name__ == '__main__':
    unittest.main()