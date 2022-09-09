"""
    @Author: Lisa Das
    @Date: 2022-09-09
    @Last Modified time: 2022-09-09
    @Title : Testing add contact method
"""

import unittest
from contacts import Person, AddressBook

class TestDeleteContact(unittest.TestCase):
    def test_delete_contact(self):
        # Test area to delete contact from existing contact list
        address_book = AddressBook()
        first = "Leo"
        for i, contact in enumerate(address_book.contacts):
            if contact["first"] == first:
                self.assertEqual(len(address_book.contacts) - 1, len(address_book.delete_contact(first)))
                self.assertNotEqual(len(address_book.contacts) + 1, len(address_book.delete_contact(first)))


if __name__ == '__main__':
    unittest.main()