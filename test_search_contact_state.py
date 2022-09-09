"""
    @Author: Lisa Das
    @Date: 2022-09-09
    @Last Modified time: 2022-09-09
    @Title : Testing search contact in the contact list as per state
"""

#importing unittest and contacts module
import unittest
from contacts import Person, AddressBook

class TestSearchContactState(unittest.TestCase):
    # Testing area to check duplicate value
    def test_search_contact_state(self):
        address_book = AddressBook()
        self.assertTrue(address_book.search_contact_state("West Bengal"))
        self.assertFalse(address_book.search_contact_state("Delhi"))


if __name__ == '__main__':
    unittest.main()