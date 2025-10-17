from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self,name,email,phone):
        self._name = name
        self._email = email
        self._phone = phone
    
    #to access the private properties, i need getters and setters

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        self._name = value

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self,value):
        self._email = value
    
    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self,value):
        self._phone = value
    
    @abstractmethod
    def display_info(self):
        pass
    

#encapsulation is implemented here: _name, _email, _phone are private. can only be accessed through getters and setters
#Abstraction is implemeneted in display_info- every subclass must implement it.
#Student & teacher will inherit this
