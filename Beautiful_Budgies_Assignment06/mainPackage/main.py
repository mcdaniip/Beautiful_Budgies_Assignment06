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
    my_cage = cage("bird-full")  
   
    print(my_cage)  # Calls __str__ to print type and locked/unlocked state
    my_cage.unlock()  
    my_cage.type = "bird-less"  
    print(my_cage) 