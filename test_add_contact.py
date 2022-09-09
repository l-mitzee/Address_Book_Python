"""
    @Author: Lisa Das
    @Date: 2022-09-09
    @Last Modified time: 2022-09-09
    @Title : Testing add contact method
"""

import unittest
from contacts import Person, AddressBook

class TestAddContact(unittest.TestCase):
    def test_add_contact(self):
        # Test area when adding one more contact
        person_list = Person('Rio', 'Kio', 'Berhampur', 'Murshidabad', 'West Bengal', 741128, 983256470, 'rio.kio@gmail.com')
        address_book = AddressBook()
        self.assertEqual(len(address_book.contacts) + 1, len(address_book.add_contact(person_list.get)))
        self.assertNotEqual(len(address_book.contacts), len(address_book.add_contact(person_list.get)))

    def test_type(self):
        # Test area to raise type error for phone number and zip code if it is not integer
        address_book = AddressBook()
        person_list = Person('Rio', 'Kio', 'Berhampur', 'Murshidabad', 'West Bengal', '741128', '983256470', 'rio.kio@gmail.com')
        self.assertRaises(TypeError, address_book.add_contact, person_list.get)


if __name__ == '__main__':
    unittest.main()