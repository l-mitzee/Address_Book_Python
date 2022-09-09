"""
    @Author: Lisa Das
    @Date: 2022-09-09
    @Last Modified time: 2022-09-09
    @Title : Testing check current address book name
"""

import unittest
from addressbook_collection import MulAddressBook
from contacts import Person, AddressBook

class TestSwitchAddressBook(unittest.TestCase):

    def test_switch_address_book(self):
        # Test area to check current address book name
        mul_address_book = MulAddressBook()
        address_book = AddressBook()
        new_address_book_name = "Book1"
        self.assertEqual(mul_address_book.switch_address_book(new_address_book_name, address_book.contacts), mul_address_book.current_address_book)
        self.assertNotEqual(mul_address_book.switch_address_book(new_address_book_name, address_book.contacts), "Book2")


if __name__ == "__main__":
    unittest.main()