"""
    @Author: Lisa Das
    @Date: 2022-08-02
    @Last Modified date: 2022-09-08
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
<<<<<<< HEAD
        return {'first': self.first,
                'last': self.last, 
                'address': self.address, 
                'city': self.city, 
                'state': self.state, 
                'zip_code': self.zip_code, 
                'phone_no': self.phone_no, 
                'email': self.email
                }
=======
        return {'first': self.first, 'last': self.last, 'address': self.address, 'city': self.city, 'state': self.state, 'zip_code': self.zip_code, 'phone_no': self.phone_no, 'email': self.email}
>>>>>>> UC9
        
class AddressBook:
    def __init__(self):
        self.contacts = []

    @property
    def get(self):
        return self.contacts

    def add_contact(self, first, contact):
        """
        Description:
            Adding new contact to the list
        Parameter:
            All contact details from user
        Return:
            List of contact in the form of dictionery
        """
        
        self.contacts.append(contact)

    def check_duplicate(self, first):
        """
        Description:
            Checking for contact duplicacy
        Parameter:
            First name to check for duplicate contact
        Return:
            Return True if first name is already present in the list else false
        """
        for contact in self.contacts:
            if contact["first"] == first:
                return True
        return False
    
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
                contact["last"] = new_name["last"]
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


    def search_contact_by_city(self, searching_city):
        """
        Description:
            Searching person in a City
        Parameter:
            City name
        Returns:
            Contact details of the person from the city
        """
        list_of_contact_in_the_city = []
        for contact in self.contacts:
            if contact["city"] == searching_city:
                list_of_contact_in_the_city.append(contact)
        return list_of_contact_in_the_city

    def search_contact_state(self, searching_state):
        """
        Description:
            Searching person in a state
        Parameter:
            State name
        Returns:
            Contact details of the person from the state
        """
        list_of_contact_in_the_city = []
        for contact in self.contacts:
            if contact["state"] == searching_state:
                list_of_contact_in_the_city.append(contact)
        return list_of_contact_in_the_city


    def print_contact_list(self, contact_list):
        """
        Description:
            Printing the list in string with proper format
        Parameter:
            Incoming list which needs to be printed
        Returns:
            The complete  list
        """
        count = 0
        for contact in contact_list:
            count += 1
            print(f'Contact {count}\nFirst_Name : {contact["first"]}, Last_Name : {contact["last"]}, Address : {contact["address"]}, City_Name : {contact["city"]}, State_Name : {contact["state"]}, Zip_Code : {contact["zip_code"]}, Phone_Number : {contact["phone_no"]}, Email_ID : {contact["email"]} \n')

