"""
    @Author: Lisa Das
    @Date: 2022-08-02
    @Last Modified date: 2022-09-06
    @Title : Create an Address Book and modifying with conditions
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

    def sort_entries(self):
        """
        Description:
            Sorting contact details with the first name
        Parameter:
            None
        Returns:
            Sorted list of contact
        """
        sorted_entries = sorted(self.contacts, key = lambda a: a["first"])
        return sorted_entries

    def sort_entries_as_per_city(self):
        """
        Description:
            Sorting contact details with the city name
        Parameter:
            None
        Returns:
            Sorted list of contact as per city
        """
        sorted_entries = sorted(self.contacts, key = lambda a: a["city"])
        return sorted_entries

    def sort_entries_as_per_state(self):
        """
        Description:
            Sorting contact details with the state name
        Parameter:
            None
        Returns:
            Sorted list of contact as per state name
        """
        sorted_entries = sorted(self.contacts, key = lambda a: a["state"])
        return sorted_entries

    def sort_entries_as_per_zip_code(self):
        """
        Description:
            Sorting contact details with the zip code
        Parameter:
            None
        Returns:
            Sorted list of contact as per zip code
        """
        sorted_entries = sorted(self.contacts, key = lambda a: a["zip_code"])
        return sorted_entries

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
            for contact in self.contacts:
                text_file.write(f'First_Name : {contact["first"]}, Last_Name : {contact["last"]}, Address : {contact["address"]}, City_Name : {contact["city"]}, State_Name : {contact["state"]}, Zip_Code : {contact["zip_code"]}, Phone_Number : {contact["phone_no"]}, Email_ID : {contact["email"]} \n')
                text_file.close()

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

    def print_contact_list(self, contact_list):
        """
        Description:
            Printing the list in string with proper format
        Parameter:
            Incoming list which needs to be printed
        Returns:
            The complete  list
        """
        list_of_contact = ""
        count = 1
        for contact in contact_list:
            list_of_contact = f'Contact {count}\nFirst_Name : {contact["first"]}, Last_Name : {contact["last"]}, Address : {contact["address"]}, City_Name : {contact["city"]}, State_Name : {contact["state"]}, Zip_Code : {contact["zip_code"]}, Phone_Number : {contact["phone_no"]}, Email_ID : {contact["email"]} \n'
            count += 1
        return list_of_contact
