from exercise_classes import *
from helper_funcs import *

def add_exercise_category():
    """This will be choice to add exercise.
                
    add_more1 - variable to control while loop
    """
    add_more1 = True
    while add_more1 :
        """Get name from user and ensure it has values."""
        name = input_validation("exercise name")

        """The function exercise_validation will check if name 
        is taken or not and return a boolean True if not taken False if taken.
        """
        valid = exercise_validation(name)
        if valid :
            """When the name is not taken add to database.
            And ask if user would like to add more.
            """
            x = user_exercise(name)
            print(x)
            r = Exercise_Repository()
            r.add_to_db(x)
            print("Exercise added succesfully!")

            add_more1 = add_more("add another category")
            if not add_more1 :
                r.close_db()

        else :
            """When the name is taken display a message and 
            ask if the user would like to try again.
            """
            print("Exercise already exists!")
            add_more1 = add_more("try again")
