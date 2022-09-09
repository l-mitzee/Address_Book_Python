"""
    @Author: Lisa Das
    @Date: 2022-09-05
    @Last Modified date: 2022-09-05
    @Title : Create Multiple Address Book
"""
import csv
from csv import DictWriter
import json

class MulAddressBook:
    def __init__(self):
        self.current_address_book = "default"
        self.address_book_name_with_contacts = {}

    @property
    def get(self):
        return self.address_book_name_with_contacts

    def select_address_book(self, address_book_name, current_address_book_contact):
        """
        Description:
            Adding multiple address book with user contact details
        Parameter:
            Address Book name and new contact details
        Return:
            List of contact with addressbook name
        """
        self.address_book_name_with_contacts[self.current_address_book] = current_address_book_contact.get
        self.current_address_book = address_book_name
        current_address_book_contact.contacts = []
        return current_address_book_contact

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
                print(data)
        except FileNotFoundError:
            print("File not Found")

    def write_csv(self):
        """
        Description:
            Writing all contact details into csv file
        Parameter:
            None
        Returns:
            None
        """
        contact = self.address_book_name_with_contacts
        file_name = "address_books_contact.csv"  
        with open(file_name, "a") as csv_file:
            fields = ['first' , 'last' , 'address', 'city' , 'state' , 'zip_code' , 'phone_no' , 'email']
            writer = DictWriter(csv_file, fieldnames = fields)
            writer.writeheader()
            value_list = list(contact.values())
            for value in value_list:
                for data in value:
                    writer.writerow(data)

    def read_csv(self):
        """
        Description:
            Reading data from csv file
        Parameter:
            None
        Returns:
            None
        """
        file_name = "address_books_contact.csv"
        count = 0
        with open(file_name, "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for line in csv_reader:
                self.address_book_name_with_contacts = line
                return line


    def write_json(self):
        """
        Description:
            Writing all contacts in json file
        Parameter:
            None 
        Returns:
            None
        """
        with open("address_books_contact.json", "w") as json_file:
            json.dump(self.address_book_name_with_contacts, json_file, indent = 2)

    def read_json(self):
        """
        Description:
            Reading contacts from json file
        Parameter:
            None 
        Returns:
            Json data
        """
        with open("address_books_contact.json", "r") as json_file:
            data = json.load(json_file)
            self.address_book_name_with_contacts = data
            # print(data)
            return data