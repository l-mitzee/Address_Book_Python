"""
    @Author: Lisa Das
    @Date: 2022-09-09
    @Last Modified time: 2022-09-09
    @Title : Create an Address Book
"""

class Person:
    def __init__(self, first, last, address, city, state, zip_code, phone_no, email):
        """
        Initializing first, last, address, city, state, zip_code, phone_no, email details with the variable name
        """
        self.first = first
        self.last = last
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_no = phone_no
        self.email = email

    @property
    def get(self):
        return {'first': self.first, 'last': self.last, 'address': self.address, 'city': self.city, 'state': self.state, 'zip_code': self.zip_code, 'phone_no': self.phone_no, 'email': self.email}

class AddressBook:
    def __init__(self):
        """
        Initializing an empty list for contact details
        """
        self.contacts = []

    def add_contact(self, contact):
        """
        Description:
            Adds contact into the existing contact list
        Parameter:
            Person details as input
        Return:
            List of all contacts after adding contact of the person
        """
        if type(contact["phone_no"]) != int:
            raise TypeError("Phone number must be a number")
        if type(contact["zip_code"]) != int:
            raise TypeError("Zip code must be a number")
        self.contacts.append(contact)
        return self.contacts