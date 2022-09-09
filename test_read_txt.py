"""
    @Author: Lisa Das
    @Date: 2022-09-09
    @Last Modified time: 2022-09-09
    @Title : Test case for Reading from Text file
"""

import unittest
from addressbook_collection import MulAddressBook
from contacts import Person, AddressBook

class TestReadText(unittest.TestCase):

    def test_read_txt(self):
        # Test area to read text file
        mul_address_book = MulAddressBook()
        address_book = AddressBook()
        book_of_address = {'default': [{'first': 'Leo', 'last': 'De', 'address': 'Electronic City', 'city': 'Bangalore', 'state': 'Karnataka', 'zip_code': '560001', 'phone_no': '7890002345', 'email': 'leo.d@gmail.com'}, {'first': 'Riya', 'last': 'Bose', 'address': 'Jadavpur', 'city': 'Kolkata', 'state': 'West Bengal', 'zip_code': '700032', 'phone_no': '8976543219', 'email': 'riya.b@gmail.com'}, {'first': 'Lisa', 'last': 'Das', 'address': 'Jadavpur', 'city': 'Kolkata', 'state': 'West Bengal', 'zip_code': '700032', 'phone_no': '6295196004', 'email': 'lisa.das@gmail.com'}, {'first': 'Piu', 'last': 'De', 'address': 'Electronic City', 'city': 'Bangalore', 'state': 'Karnataka', 'zip_code': '560001', 'phone_no': '9876543221', 'email': 'piu.de@gmail.com'}], 'Book1': [{'first': 'Rohini', 'last': 'Sharma', 'address': 'Rajgar', 'city': 'Bihar', 'state': 'Bihar', 'zip_code': '456789', 'phone_no': '9876654321', 'email': 'rohini.s@gmail.com'}]}       
        self.assertEqual(mul_address_book.read_txt(), book_of_address)

if __name__ == "__main__":
    unittest.main()