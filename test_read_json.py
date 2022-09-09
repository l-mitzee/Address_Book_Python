"""
    @Author: Lisa Das
    @Date: 2022-09-09
    @Last Modified time: 2022-09-09
    @Title : Test case for reading from json file
"""

import unittest
from addressbook_collection import MulAddressBook
from contacts import Person, AddressBook

class TestReadText(unittest.TestCase):

    def test_read_csv(self):
        # Test area to read json file
        mul_address_book = MulAddressBook()
        read_json_text = {'default': [{'first': 'Leo', 'last': 'De', 'address': 'Electronic City', 'city': 'Bangalore', 'state': 'Karnataka', 'zip_code': '560001', 'phone_no': '7890002345', 'email': 'leo.d@gmail.com'}, {'first': 'Riya', 'last': 'Bose', 'address': 'Jadavpur', 'city': 'Kolkata', 'state': 'West Bengal', 'zip_code': '700032', 'phone_no': '8976543219', 'email': 'riya.b@gmail.com'}, {'first': 'Lisa', 'last': 'Das', 'address': 'Jadavpur', 'city': 'Kolkata', 'state': 'West Bengal', 'zip_code': '700032', 'phone_no': '6295196004', 'email': 'lisa.das@gmail.com'}, {'first': 'Piu', 'last': 'De', 'address': 'Electronic City', 'city': 'Bangalore', 'state': 'Karnataka', 'zip_code': '560001', 'phone_no': '9876543221', 'email': 'piu.de@gmail.com'}], 'Book2': [{'first': 'Rio', 'last': 'kio', 'address': 'Jadavpur', 'city': 'Kolkata', 'state': 'West Bengal', 'zip_code': '700032', 'phone_no': '876543234567', 'email': 'rio.kio@gmail.com'}]}
        read_json_text1 = {'default': [{'first': 'Le', 'last': 'D', 'address': 'Electronic City', 'city': 'Bangalore', 'state': 'Karnataka', 'zip_code': '560001', 'phone_no': '7890002345', 'email': 'leo.d@gmail.com'}, {'first': 'Riya', 'last': 'Bose', 'address': 'Jadavpur', 'city': 'Kolkata', 'state': 'West Bengal', 'zip_code': '700032', 'phone_no': '8976543219', 'email': 'riya.b@gmail.com'}, {'first': 'Lisa', 'last': 'Das', 'address': 'Jadavpur', 'city': 'Kolkata', 'state': 'West Bengal', 'zip_code': '700032', 'phone_no': '6295196004', 'email': 'lisa.das@gmail.com'}, {'first': 'Piu', 'last': 'De', 'address': 'Electronic City', 'city': 'Bangalore', 'state': 'Karnataka', 'zip_code': '560001', 'phone_no': '9876543221', 'email': 'piu.de@gmail.com'}], 'Book2': [{'first': 'Rio', 'last': 'kio', 'address': 'Jadavpur', 'city': 'Kolkata', 'state': 'West Bengal', 'zip_code': '700032', 'phone_no': '876543234567', 'email': 'rio.kio@gmail.com'}]}
        self.assertEqual(mul_address_book.read_json(), read_json_text)
        self.assertNotEqual(mul_address_book.read_json(), read_json_text1)


if __name__ == "__main__":
    unittest.main()