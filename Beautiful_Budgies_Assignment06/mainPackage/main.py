# File Name : main.py
# Student Name: Ian McDaniel, Sharvari Girish Patil, Nate Hoang, Michael Slivinski
# email:  mcdaniip@mail.uc.edu, patilsg@mail.uc.edu, hoangnd@mail.uc.edu, slivinmb@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date:   February 25 2025
# Course #/Section:   IS4010 - 001
# Semester/Year:   Spring Semester 2025
# Brief Description of the assignment:  collaboratively modeling a budgie with food, cage, bird, and nest classes

# Brief Description of what this module does.: This module is furthering our knowledge of python with classes as well as collaboration with github
# Citations: 

# Anything else that's relevant:

from birdPackage.bird import *
from foodPackage.food import *
from cagePackage.cage import *
from nestPackage.nest import *
#import statements for code to work properly 

if __name__ == "__main__":
    budgie = Bird("Budgie") #instantiate a bird 
    print(type(budgie)) #prints type 
    print(budgie) #prints the type of bird
    budgie.flaps() #prints the type of bird flying 

    print("")
    print("")

    feeder = BirdFeeder(500, "Backyard Shepherd Hook") #instantiates a feeder with 500g of food and on a shepherd hook in a backyard
    print(type(feeder)) #prints the type
    print(feeder) #prints state of feeder
    feeder.bird_eats(100) # a bird eats 100g of food
    print(f"Current food: {feeder.get_food_grams} grams") #gets current food weight from feeder
    print(f"Feeder location: {feeder.get_location}") #gets current location of feeder
    feeder.squirrel_eats(300) # a squirrel eats 300g of food
    print(feeder) #gets state of feeder
    feeder.refill_food(400) #refills feeder to 500g with an addition of 400g
    print(feeder) #prints state of feeder

    print("")
    print("")

    my_cage = cage("bird-full")  #instantiates a bird cage that is full
    print(type(my_cage)) #prints type
    print(my_cage)  #prints state of cage
    my_cage.unlock()  #unlocks the current cage
    my_cage.type = "bird-less"  #changes type to birdless representing an empty cage
    print(my_cage) #prints state of cage

    print("")
    print("")

    nest = BudgieNest("Eucalyptus Tree", 0) #instantiates a nest in a eucalyptus tree with no birds
    print(type(nest)) #prints type
    print(nest) # prints state of nest 
    nest.add_birds(1) #bird enters nest
    print(nest) #prints state of nest
    nest.bird_count = 1 
    nest.add_birds(1) #adds another bird
    print(nest) #prints state of nest
    nest.remove_birds(2) # both birds leave nest
    print(nest) #prints state of nest
    print("The nest fell out of the Eucalyptus Tree onto the ground") 
    nest.location = "Ground" #updates location of nest (no birds were harmed)
    print(nest) #prints state of nest

    