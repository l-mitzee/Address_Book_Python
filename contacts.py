"""
    @Author: Lisa Das
    @Date: 2022-08-31
    @Last Modified date: 2022-09-02
    @Title : Create an Address Book
"""

class Person:
    def __init__(self, first, last, address, city, state, zip_code, phone_no, email):
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
        self.contacts = []

    def add_contact(self, contact):
        """
        Description:
            Adding new contact to the list
        Parameter:
            All contact details from user
        Return:
            List of contact in the form of dictionery
        """
        self.contacts.append(contact)

    def edit_contact(self, first, new_name):
        """
        Description:
            Editing existing contact to the list
        Parameter:
            First name and new contact details
        Return:
            List of contact in the form of dictionery
        """
        for contact in self.contacts:
            if contact["first"] == first:
                contact["first"] = new_name["first"]
                contact["last"] = new_name["Last"]
                contact["address"] = new_name["address"]
                contact["city"] = new_name["city"]
                contact["state"] = new_name["state"]
                contact["zip_code"] = new_name["zip_code"]
                contact["phone_no"] = new_name["phone_no"]
                contact["email"] = new_name["email"]

    def delete_contact(self, first):
        """
        Description:
            Deleting existing contact to the list
        Parameter:
            First name to search for details
        """
        for i, contact in enumerate(self.contacts):
            if contact["first"] == first:
                del self.contacts[i]

    def display_contact(self):
        """
        Description:
            Display existing contact to the list
        Return:
            List of contact which is present else empty list
        """
        print(self.contacts)