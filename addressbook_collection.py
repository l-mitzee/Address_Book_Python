"""
    @Author: Lisa Das
    @Date: 2022-09-05
    @Last Modified date: 2022-09-05
    @Title : Create Multiple Address Book
"""

class MulAddressBook:
    def __init__(self):
        self.current_address_book = "default"
        self.address_book_name_with_contacts = {}

    @property
    def get(self):
        return self.address_book_name_with_contacts

    def switch_address_book(self, address_book_name, current_address_book_contact):
        """
        Description:
            Adding multiple address book with user contact details
        Parameter:
            Address Book name and new contact details
        Return:
            List of contact with addressbook name
        """
        self.address_book_name_with_contacts[self.current_address_book] = current_address_book_contact
        self.current_address_book = address_book_name
        current_address_book_contact = []
        return address_book_name

    def show_contacts(self):
        """
        Description:
            Showing full address book with individual contact details
        """
        return self.address_book_name_with_contacts

    def write_txt(self):
        """
        Description:
            Writing all contacts in text file
        Parameter:
            None 
        Returns:
            None
        """
        with open("address_books_contact.txt", "w") as text_file:
            text_file.write(str(self.address_book_name_with_contacts))

    def read_txt(self):
        """
        Description:
            Reading data from text file
        Parameter:
            None
        Returns:
            None
        """
        try:
            with open("address_books_contact.txt") as text_file:
                data = text_file.read()
                return data
        except FileNotFoundError:
            print("File not Found")