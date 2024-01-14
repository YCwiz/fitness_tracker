"""This will hande creating new workout routines.

helper_funcs - module with assistant functions
"""
from helper_funcs import *
from exercise_classes import *
from routine_classes import *

def create_workout_routine() :
    """This function will create a new workout routine.
    
    workout_input_valid - checks to see if the user enters values and it has no spaces
    workout_validation - checks if the routine name is not taken
    Routine_Repository - class that will handle all CRUD
    Routine_table - class that will contain all exercises as one routine
    Exercise_Repository - class that handles all CRUD for exercises
    read_from_db - method that reads data from database
    input_validation - function that ensures user input values
    exercise_validation - function that check if exercise exist
    Exercise - exercise object class
    init_exercise - method initialises an exercise with data from the database
    user_workout_routine - takes in exercise object and gets further information of routine
                           initialise a exercise routine object and returns it
    add_to_routine - method that adds exercise object to routine
    add_more - function get user input if they would like to continue, return a boolean
    close_db - method of Exercise_repository and Routine_Repository that closes the database
    """
    add_more1 = True
    while add_more1 :
        """Get routine name, ensure it not already used and copen connection with database."""
        wr_name = workout_input_valid()
        valid = workout_validation(wr_name)
        rr = Routine_Repository()
        if valid :
            """When the name of routine is not already used, create routine."""
            rt = Routine_table(wr_name)
            add_more2 = True
            while add_more2 :
                """Get exercise name from the user and see if its in database."""
                r = Exercise_Repository()
                ex_name = input_validation("exercise name")
                valid1 = exercise_validation(ex_name)
                if not valid1 :
                    """When exercise is in database get more info on exercise add it to routine."""
                    x = Exercise()
                    data = r.read_from_db(ex_name, "exercise")
                    x.init_exercise(data)
                    """Display exercise to the user and ask if user want to add another."""
                    print(x)
                    ex_r = user_workout_routine(x)
                    rt.add_to_routine(ex_r)
                    add_more2 = add_more("add another exercise")
                    if not add_more2 :
                        rr.add_to_db(rt)
                        print("\nRoutine added!\n")
                        rr.close_db()
                        r.close_db()
                        add_more1 = False

                else :
                    """When exercise is not in database ask if they would like to try another."""
                    print("Exercise does not exist!")
                    add_more2 = add_more("try another exercise")
                    if not add_more2 :
                        if len(rt.all) > 0 :
                            rr.add_to_db(rt)
                            print("Routine added!")
                        rr.close_db()
                        r.close_db()
                        return
        else :
            """When routine name is already in use, ask if user would like to continue."""
            print("\nRoutine name already taken!")
            add_more1 = add_more("try another name")
            if not add_more1 :
                rr.close_db()