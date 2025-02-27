# File Name : food.py
# Student Name: Nate Hoang (beautiful budgies)
# email:  hoangnd@mail.uc
# Assignment Number: Assignment 06
# Due Date:   2/25/2025
# Course #/Section:   4010-001
# Semester/Year:   Spring 25
# Brief Description of the assignment:  collaboratively modeling a budgie with food, cage, bird, and nest classes

# Brief Description of what this module does.: This module is furthering our knowledge of python with classes as well as collaboration with github
# Citations: 

# Anything else that's relevant:
class BirdFeeder:
    """
    A class representing a bird feeder with food, simulating birds and squirrels eating and refilling.
    """

    def __init__(self, initial_food_grams, location):
        """
        Initializes the BirdFeeder with a specified amount of food and location.

        
        @param    initial_food_grams (int): The initial amount of food in grams.
            location (str): The location of the bird feeder.
        """
        self._food_grams = initial_food_grams
        self._location = location

    def __str__(self):
        return f"Bird Feeder at {self._location} with {self._food_grams} grams of food."

    def __repr__(self):
        return f"BirdFeeder({self._food_grams}, '{self._location}')"

    @property
    def get_food_grams(self):
        """Gets the current amount of food in grams."""
        return self._food_grams

    
    def food_grams(self, new_food_grams):
        """Sets the current amount of food in grams."""
        self._food_grams = new_food_grams

    @property
    def get_location(self):
        """Gets the location of the bird feeder."""
        return self._location

    
    def location(self, new_location):
        """Sets the location of the bird feeder."""
        self._location = new_location

    def bird_eats(self, amount_eaten_grams):
        """Simulates a bird eating a specified amount of food."""
        if amount_eaten_grams <= self._food_grams:
            self._food_grams -= amount_eaten_grams
            print(f"A bird ate {amount_eaten_grams} grams of food from the feeder.")
        else:
            print("Not enough food in the feeder for the bird to eat that much.")

    def squirrel_eats(self, amount_eaten_grams):
        """Simulates a squirrel eating a specified amount of food."""
        if amount_eaten_grams <= self._food_grams:
            self._food_grams -= amount_eaten_grams
            print(f"A squirrel ate {amount_eaten_grams} grams of food from the feeder.")
        else:
            print("Not enough food in the feeder for the squirrel to eat that much.")

    def refill_food(self, refill_amount_grams):
        """Refills the bird feeder with a specified amount of food."""
        self._food_grams += refill_amount_grams
        print(f"Bird feeder refilled with {refill_amount_grams} grams of food.")

