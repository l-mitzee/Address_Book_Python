"""
    @Author: Lisa Das
    @Date: 2022-09-09
    @Last Modified time: 2022-09-09
    @Title : Testing check duplicate value in the contact list
"""

#importing unittest and contacts module
import unittest
from contacts import Person, AddressBook

class TestCheckDuplicate(unittest.TestCase):
    # Testing area to check duplicate value
    def test_check_duplicate_contact(self):
        address_book = AddressBook()
        first = "Leo"
        first1 = "Rohini"
        for i, contact in enumerate(address_book.contacts):
            if contact["first"] == first:
                self.assertTrue(address_book.check_duplicate(first))
                self.assertFalse(address_book.check_duplicate(first1))


if __name__ == '__main__':
    unittest.main()