# File Name : bird.py
# Student Name: Michael Slivinski
# email:  slivinmb@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date:   2/27/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment: Collaborate with a group to develop a VS project modeling something in the real world
#                                      Each member must write one class except for one group member who writes the main.py code.
# Brief Description of what this module does. This module is the bird.py. It includes a property, getter, setter, and method for a class called bird.
#                                             It prints the type of bird that flaps its wings.  
# Citations: 
    # https://www.w3schools.com/python/python_string_formatting.asp
# Anything else that's relevant:


class Bird(object):
    """
    Model a bird that flaps its wings. 
    """
    def __init__(self, type): #Constructor
        """
        Constructor 
        @param type String: type of the bird.
        """
        self.set_type(type)

    def get_type(self):
        """
        @return String: The type of the current object.
        """
        return self.__type

    def set_type(self, type):
        """
        Assign a value to the bird type of the current object.
        """
        self.__type = type 


    def __str__(self):
        """
        @return String: Redable representation of the current object.
        """
        return "Type of Bird: " + self.__type

    def flaps(self):
        """
        Prints the type of bird that starts flapping its wings. 
        """
        print (f"The {self.__type} starts flapping its wings.")

