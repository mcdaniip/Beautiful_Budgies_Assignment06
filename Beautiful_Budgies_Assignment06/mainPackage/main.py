# File Name : main.py
# Student Name: Ian McDaniel, Sharvari Girish Patil, Nate Hoang, Michael Slivinski
# email:  {required}
# Assignment Number: Assignment 06
# Due Date:   February 25 2025
# Course #/Section:   IS4010 - 001
# Semester/Year:   Spring Semester 2025
# Brief Description of the assignment:  

# Brief Description of what this module does. 
# Citations: 

# Anything else that's relevant:

from birdPackage.bird import *
from foodPackage.food import *
from cagePackage.cage import *

if __name__ == "__main__":
    budgie = Bird("Budgie")
    print(type(budgie))
    print(budgie)
    budgie.flaps()

    print("")

    feeder = BirdFeeder(500, "Backyard Shepherd Hook")
    print(type(feeder))
    print(feeder)
    feeder.bird_eats(100)
    print(f"Current food: {feeder.get_food_grams} grams")
    print(f"Feeder location: {feeder.get_location}")
    feeder.squirrel_eats(300)
    print(feeder)
    feeder.refill_food(400)
    print(feeder)


    print("")