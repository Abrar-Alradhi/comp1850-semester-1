# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, birth):
        """
        Creates a person, given values for name and birth.
        """
        if not isinstance(name, str):
            raise TypeError("name should be a string.")
        if name == "":
            raise ValueError("please write a name.")
        if not isinstance(birth, date):
            raise TypeError("Enter a valid date.")

        self.name = name
        self.birth = birth
    
    def initials(self):
        """
        Returns uppercase initial letters of the name.
        """
        letters = []
        for part in self.name.split():
            letters.append(part[0].upper())
        return "".join(letters) 

    def is_birthday(self):
        """
        Returns True if today is the persons birthday.
        """
        today = date.today()
        return today.month == self.birth.month and today.day == self.birth.day



    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
