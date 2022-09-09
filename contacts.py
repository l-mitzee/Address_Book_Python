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
        return {'first': self.first,
                'last': self.last, 
                'address': self.address, 
                'city': self.city, 
                'state': self.state, 
                'zip_code': self.zip_code, 
                'phone_no': self.phone_no, 
                'email': self.email
                }
        
class AddressBook:
    def __init__(self):
        """
        Initializing an empty list for contact details
        """
        self.contacts = [{'first': 'Leo', 'last': 'De', 'address': 'Electronic City', 'city': 'Bangalore', 'state': 'Karnataka', 'zip_code': '560001', 'phone_no': '7890002345', 'email': 'leo.d@gmail.com'},
                        {'first': 'Riya', 'last': 'Bose', 'address': 'Jadavpur', 'city': 'Kolkata', 'state': 'West Bengal', 'zip_code': '700032', 'phone_no': '8976543219', 'email': 'riya.b@gmail.com'},
                        {'first': 'Lisa', 'last': 'Das', 'address': 'Jadavpur', 'city': 'Kolkata', 'state': 'West Bengal', 'zip_code': '700032', 'phone_no': '6295196004', 'email': 'lisa.das@gmail.com'},
                        {'first': 'Piu', 'last': 'De', 'address': 'Electronic City', 'city': 'Bangalore', 'state': 'Karnataka', 'zip_code': '560001', 'phone_no': '9876543221', 'email': 'piu.de@gmail.com'}]

    @property
    def get(self):
        return self.contacts

    def add_contact(self, first, contact):
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
            Editing existing contact with all details searching by first name contact to the list
        Parameter:
            First name and new contact details
        Return:
            List of contact in the form of dictionery
        """
        for contact in self.contacts:
            if contact["first"] == first:
                if type(contact["zip_code"]) != int:
                    raise TypeError("Zip code must be a number")
                if type(contact["phone_no"]) != int:
                    raise TypeError("Phone number must be a number")
                contact["first"] = new_name["first"]
                contact["last"] = new_name["last"]
                contact["address"] = new_name["address"]
                contact["city"] = new_name["city"]
                contact["state"] = new_name["state"]
                contact["zip_code"] = new_name["zip_code"]
                contact["phone_no"] = new_name["phone_no"]
                contact["email"] = new_name["email"]
        return new_name

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
        return self.contacts


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

    def view_city(self):
        """
        Description:
            Fetching all the city name
        Parameter:
            None
        Returns:
            Set of city name 
        """
        set_of_city = set()
        for contact in self.contacts:
            set_of_city.add(contact["city"])
        return set_of_city

    def view_state(self):
        """
        Description:
            Fetching all the state name
        Parameter:
            None
        Returns:
            Set of state name 
        """
        set_of_state = set()
        for contact in self.contacts:
            set_of_state.add(contact["state"])
        return set_of_state

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
