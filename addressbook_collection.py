"""
    @Author: Lisa Das
    @Date: 2022-09-05
    @Last Modified date: 2022-09-05
    @Title : Create Multiple Address Book
"""

class MulAddressBook:
    def __init__(self):
        self.mul_contacts = []
        self.current_address_book = ""
        self.address_book = {}


    def select_address_book(self, address_book_name, new_contacts):
        """
        Description:
            Adding multiple address book with user contact details
        Parameter:
            Address Book name and new contact details
        Return:
            List of contact with addressbook name
        """
        if not address_book_name:
            self.current_address_book = "default"
        else:
            self.current_address_book = address_book_name
        new_contacts.contacts = [] 
        self.address_book[self.current_address_book] = new_contacts.get
        return new_contacts

    def show_contacts(self):
        """
        Description:
            Showing full address book with individual contact details
        """
        print(self.address_book)