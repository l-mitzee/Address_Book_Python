"""
    @Author: Lisa Das
    @Date: 2022-09-09
    @Last Modified time: 2022-09-09
    @Title : Testing search contact in the contact list as per city
"""

#importing unittest and contacts module
import unittest
from contacts import Person, AddressBook

class TestSearchContactCity(unittest.TestCase):
    # Testing area to check duplicate value
    def test_search_contact_city(self):
        address_book = AddressBook()
        city_name = "Bangalore"
        self.assertTrue(address_book.search_contact_by_city(city_name))
        self.assertFalse(address_book.search_contact_by_city("Delhi"))


if __name__ == '__main__':
    unittest.main()