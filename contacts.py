"""
    @Author: Lisa Das
    @Date: 2022-08-02
    @Last Modified date: 2022-09-06
    @Title : Create an Address Book and modifying with conditions
"""

class Person:
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone_no, email_id):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_no = phone_no
        self.email_id = email_id

    @property
    def get(self):
        return {'first_name': self.first_name,
                'last_name': self.last_name, 
                'address': self.address, 
                'city': self.city, 
                'state': self.state, 
                'zip_code': self.zip_code, 
                'phone_no': self.phone_no, 
                'email_id': self.email_id
                }
        
class AddressBook:
    def __init__(self):
        self.contacts = []

    @property
    def get(self):
        return self.contacts

    def add_contact(self, first_name, contact):
        """
        Description:
            Adding new contact to the list
        Parameter:
            All contact details from user
        Return:
            List of contact in the form of dictionery
        """
        
        self.contacts.append(contact)

    def check_duplicate(self, first_name):
        """
        Description:
            Checking for contact duplicacy
        Parameter:
            First name to check for duplicate contact
        Return:
            Return True if first name is already present in the list else false
        """
        for contact in self.contacts:
            if contact["first_name"] == first_name:
                return True
        return False
    
    def edit_contact(self, first_name, new_name):
        """
        Description:
            Editing existing contact to the list
        Parameter:
            First name and new contact details
        Return:
            List of contact in the form of dictionery
        """
        for contact in self.contacts:
            if contact["first_name"] == first_name:
                contact["first_name"] = new_name["first_name"]
                contact["last_name"] = new_name["last_name"]
                contact["address"] = new_name["address"]
                contact["city"] = new_name["city"]
                contact["state"] = new_name["state"]
                contact["zip_code"] = new_name["zip_code"]
                contact["phone_no"] = new_name["phone_no"]
                contact["email_id"] = new_name["email_id"]

    def delete_contact(self, first_name):
        """
        Description:
            Deleting existing contact to the list
        Parameter:
            First name to search for details
        """
        for i, contact in enumerate(self.contacts):
            if contact["first_name"] == first_name:
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

    def display_contact(self):
        """
        Description:
            Display existing contact to the list
        Return:
            List of contact which is present else empty list
        """
        for contact in self.contacts:
            for key in contact:
                print(key, ' : ', contact[key])