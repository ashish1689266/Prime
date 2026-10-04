# Next topic is abstraction - this is the way through which do hide unnessesory details from
# the user and we are showing only the nessesory details
# this is done by importing ABC from abc, this is abstraction based class
# we inherit the parent class with ABC

from abc import ABC, abstractmethod
class Animal(ABC):
    # here the we create abstract method with no implementation or defination, the child class that inherit this class
    # will define the abstract method in the child class according to themselves
    # so as many as classes we can create and inherit this class to it and create their own definations
    # accordingly, and to do that you also have to import abstractmethod decorator
    @abstractmethod
    def create_sound(self, sound):
        pass # in abstract method we do not give any defination

class lion(Animal):
    def create_sound(self, sound): # here we are redefining the abstract method of the parent class
        self.sound = sound

    def call_sound(self):
        print(self.sound)

class bird(Animal):
    def create_sound(self, sound):
        self.sound = sound

    def call_sound(self):
        print(self.sound)

Adam = lion()
Adam.create_sound("Roar")
Adam.call_sound()

Neela = bird()
Neela.create_sound("Chirp")
Neela.call_sound()

# Abstraction is different from data hiding because we not only hide the data but also procedures that are not 
# usefull to user and show only user relevant details

# In abstraction the parent class is just the blueprint