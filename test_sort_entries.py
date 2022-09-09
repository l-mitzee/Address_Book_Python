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
        # Test area to check wheather the list is sorted or not
        sorted_list_of_contact = [{'first': 'Leo', 'last': 'De', 'address': 'Electronic City', 'city': 'Bangalore', 'state': 'Karnataka', 'zip_code': '560001', 'phone_no': '7890002345', 'email': 'leo.d@gmail.com'},
                {'first': 'Lisa', 'last': 'Das', 'address': 'Jadavpur', 'city': 'Kolkata', 'state': 'West Bengal', 'zip_code': '700032', 'phone_no': '6295196004', 'email': 'lisa.das@gmail.com'},
                {'first': 'Piu', 'last': 'De', 'address': 'Electronic City', 'city': 'Bangalore', 'state': 'Karnataka', 'zip_code': '560001', 'phone_no': '9876543221', 'email': 'piu.de@gmail.com'},
                {'first': 'Riya', 'last': 'Bose', 'address': 'Jadavpur', 'city': 'Kolkata', 'state': 'West Bengal', 'zip_code': '700032', 'phone_no': '8976543219', 'email': 'riya.b@gmail.com'}]
        
        unsorted_list_of_contacts = [{'first': 'Leo', 'last': 'De', 'address': 'Electronic City', 'city': 'Bangalore', 'state': 'Karnataka', 'zip_code': '560001', 'phone_no': '7890002345', 'email': 'leo.d@gmail.com'},
                        {'first': 'Riya', 'last': 'Bose', 'address': 'Jadavpur', 'city': 'Kolkata', 'state': 'West Bengal', 'zip_code': '700032', 'phone_no': '8976543219', 'email': 'riya.b@gmail.com'},
                        {'first': 'Lisa', 'last': 'Das', 'address': 'Jadavpur', 'city': 'Kolkata', 'state': 'West Bengal', 'zip_code': '700032', 'phone_no': '6295196004', 'email': 'lisa.das@gmail.com'},
                        {'first': 'Piu', 'last': 'De', 'address': 'Electronic City', 'city': 'Bangalore', 'state': 'Karnataka', 'zip_code': '560001', 'phone_no': '9876543221', 'email': 'piu.de@gmail.com'}]

        address_book = AddressBook()
        self.assertEqual(address_book.sort_entries(), sorted_list_of_contact)
        self.assertNotEqual(address_book.sort_entries(), unsorted_list_of_contacts)


if __name__ == '__main__':
    unittest.main()