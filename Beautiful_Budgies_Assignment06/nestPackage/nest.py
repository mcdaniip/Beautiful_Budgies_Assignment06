# File Name : nest.py
# Student Name: Ian McDaniel
# email:  mcdaniip@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date:   February 25 2025
# Course #/Section:   IS4010 - 001
# Semester/Year:   Spring Semester 2025
# Brief Description of the assignment:  collaboratively modeling a budgie with food, cage, bird, and nest classes

# Brief Description of what this module does.: This module is furthering our knowledge of python with classes as well as collaboration with github
# Citations: 

# Anything else that's relevant:

class BudgieNest:
    """
    Model the nest of a Budgie
    """
    def __init__(self, location, bird_count=0):
        """
        Constructor
        @param location: where the nest is
        @param bird_count: how many birds are in the nest 
        """
        self._location = location
        self._bird_count = bird_count
        
    def __str__(self):
        """
        String rep of the nest 
        @return string representing the state of the nest
        """
        return f"Nest at {self._location}, Birds: {self._bird_count}"

    @property
    def location(self):
        """
        Getter for nest location
        @param new_location: new location of the nest
        """
        return self._location

    @location.setter
    def location(self, new_location):
        """
        Setter for nest location
        @param new_loaction: The new location of the nest
        """
        self._location = new_location

    @property
    def bird_count(self):
        """
        Getter for the bird count
        @return The number of birds in nest
        """
        return self._bird_count

    @bird_count.setter
    def bird_count(self, count):
        """
        Setter for bird count
        @param count: The new number of birds in nest
        """
        if count >=0:
            self._bird_count = count
        else:
            print("Invalid bird count")

    def add_birds(self, count):
        """
        Adds birds to the nest 
        @param count: The number of birds that is added
        """
        if count > 0:
            self._bird_count += count
            print (f"{count} bird(s) entered the nest.")
        else:
            print("Invalid bird addition")

    def remove_birds(self, count):
        """
        Removes birds from the nest
        @param count: The number of birds to remove 
        """
        if 0 < count <= self._bird_count:
            self._bird_count -= count
            print(f"{count} birds() left the nest.")
        else:
            print("Invalid bird removal")

    if __name__ == "__main__":
        main()