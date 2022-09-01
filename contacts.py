"""
    @Author: Lisa Das
    @Date: 2022-08-31
    @Last Modified time: 2022-09-01
    @Title : Create an Address Book
"""

from tkinter import FALSE


class Person:
    contact_list = []
    def __init__(self, first, last, address, city, state, zip, phone_no, email):
        self.first = first
        self.last = last
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone_no = phone_no
        self.email = email

    def addNewPerson(self):
        """
        Description:
            Adding new contact to the contact list
        """
        Person.contact_list.append(self)
    def getPersonList(self):
        """
        Description:
            Printing new contact list
        Return:
            List of contact
        """
        return Person.contact_list
    def editContact(self, first, last, address, city, state, zip, phone_no, email):
        """
        Description:
            Editing existing contact details using first name
        Parameter:
            All value which needs to be edited
        Return:
            If first name in list return True else False
        """
        for list_contact in Person.contact_list:
            if(list_contact.getFirst() == first):
                list_contact.first, list_contact.last, list_contact.address, list_contact.city, list_contact.state, list_contact.zip, list_contact.phone_no, list_contact.email = first, last, address, city, state, zip, phone_no, email
                return True
            return False    
    
    def deleteContact(self, first):
        """
        Description:
            deleting existing contact details using first name
        Return:
            If first name in list return True else False
        """
        for list_contact in Person.contact_list:
            if(list_contact.getFirst() == first):
                Person.contact_list.remove(list_contact)
                return True
            return False

    def setFirst(self,first):
        self.first = first
    def getFirst(self):
        return self.first
    def setLast(self,last):
        self.last = last
    def getLast(self):
        return self.last
    def setAddress(self,address):
        self.address = address
    def getAddress(self):
        return self.address
    def setCity(self,city):
        self.city = city
    def getCity(self):
        return self.city
    def setState(self,state):
        self.city = state
    def getState(self):
        return self.state
    def setZip(self,zip):
        self.zip = zip
    def getZip(self):
        return self.zip
    def setPhone_no(self,phone_no):
        self.phone_no = phone_no
    def getPhone_no(self):
        return self.phone_no
    def setEmail(self,email):
        self.email = email
    def getEmail(self):
        return self.email

    def __str__(self):
        return "%s %s %s %s %s %d %d %s"%(self.first, self.last, self.address, self.city, self.state, self.zip, self.phone_no, self.email)