# File Name : main.py
# Student Name: Ian McDaniel, Sharvari Girish Patil, Nate Hoang, Michael Slivinski
# email:  {required}
# Assignment Number: Assignment 06
# Due Date:   February 25 2025
# Course #/Section:   IS4010 - 001
# Semester/Year:   Spring Semester 2025

def main(): 
    print(cage)  


class cage:
    """
    Model a cage that can lock/unlock and holds a type.
    """

    def __init__(self, type: str):
        """
        Constructor to initialize the cage with its type.
        
        @param type String: The state of the cage
        """
        self.__type = type  # State of the cage
        self.__locked = True  # Cage starts locked by default

    @property
    def type(self):
        """Getter for the type of the cage."""
        return self.__type

    @type.setter
    def type(self, value: str):
        """Setter for the type of the cage."""
        self.__type = value

    def unlock(self):
        """Unlock the cage."""
        self.__locked = False
        print(f"The {self.__type} cage is now unlocked.")  # "Does something" - unlocking

    def __str__(self):
        """Human-readable string representation."""
        return f"Cage Type: {self.__type}, {'Locked' if self.__locked else 'Unlocked'}."



if __name__ == "__main__":
    main()  # Call main function to execute









