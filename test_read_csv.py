"""
    @Author: Lisa Das
    @Date: 2022-09-09
    @Last Modified time: 2022-09-09
    @Title : Test case for reading from csv file
"""

import unittest
from addressbook_collection import MulAddressBook
from contacts import Person, AddressBook

class TestReadText(unittest.TestCase):

    def test_read_csv(self):
        # Test area to read text file
        mul_address_book = MulAddressBook()
        read_csv_text = {'first': 'Leo', 'last': 'De', 'address': 'Electronic City', 'city': 'Bangalore', 'state': 'Karnataka', 'zip_code': '560001', 'phone_no': '7890002345', 'email': 'leo.d@gmail.com'}
        self.assertAlmostEqual(mul_address_book.read_csv(), read_csv_text)

if __name__ == "__main__":
    unittest.main()