"""This will handle add updating a routine.

helper_funcs - module that contains assistant functions
exercise_routine_classes - module that contains all classes related to routines
exercise_classes - module that contains all classes related to routines
"""
from helper_funcs import *
from routine_classes import *
from exercise_classes import *

def add_upd_routine(name) :
    """This will add exercises to already existing routine.
    
    Exercise_Repository - class repomsible for all exercise CRUD
    input_validation - ensures user input values
    exercise_validation - checks if exercise is in database, returns a boolean
    Exercise - exercise object 
    read_from_db - method that reads data from the database
    init_exercise - method of that allows to initialse values from database
    user_workout_routine - gets data from user for more details on exercise
    update_db - method allows for adding an exercise to a routine
    close_db - method that closes database connection
    """
    rr = Routine_Repository()
    new_ex = []
    add_more1 = True
    while add_more1 :
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
            new_ex.append(ex_r)
            add_more1 = add_more("add another exercise")
            if not add_more1 :
                for item in new_ex :
                    rr.update_db(name, item)
                print("\nRoutine updated!\n")
                r.close_db()
                add_more1 = False

        else :
            """When exercise is not in database ask if they would like to try another."""
            print("Exercise does not exist!")
            add_more1 = add_more("try another exercise")
            if not add_more1 :
                if len(new_ex) > 0 :
                    for item in new_ex :
                        rr.update_db(name, item)
                        print("Routine updated!")
                r.close_db()
                add_more1 = False

def add_upd_routine_frame() :
    """This will handle user choice to add exercise to routines.
    
    Routine_Repository - class that handles all CRUD for workout routines
    routine_validation - checks if there are routines created or not
    read_from_db - method to read data from the database
    workout_input_valid - ensures user adhere to naming rules of workout routines
    Routine_exercise - exercise object for routines
    init_routine_exercise - initialises a exercise object from database data
    add_more - get user response to continue or not, returns a boolean
    add_more1 - variable to control while loop
    """
    """Check if routines has been created."""
    valid = routine_validation()
    if valid :
        """When routines has been created, get routine names and display to user and add to list."""
        rr = Routine_Repository()
        data = rr.read_from_db(pref ="routiness")
        all = []
        print("\nRoutines :")
        for item in data :
            print(item[0])
            all.append(item[0])
        if len(all) > 1 :
            """When more than one routine,ask if user for routine they want to update."""
            add_more2 = True
            while add_more2 :
                """Get the name of routine and check if it's in routines."""
                name = workout_input_valid("no")
                if name in all :
                    """User selected routine is in routines."""
                    data2 = rr.read_from_db(name, "routine")
                    for item2 in data2 :
                        """Initialise a exercise routine object and display all exercises."""
                        re = Routine_exercise()
                        re.init_routine_exercise(item2)
                        print(re)
                    add_upd_routine(name)
                    rr.close_db()
                        
                else :
                    """When user input an incorrect name for routine."""
                    print("Routine name not valid")
                    add_more2 = add_more("try again")
                    if not add_more2 :
                        rr.close_db()

        else :
            """User only has one routine."""
            data2 = rr.read_from_db(all[0], "routine")
            for item2 in data2 :
                """Initialise a exercise routine object and display all exercises."""
                re = Routine_exercise()
                re.init_routine_exercise(item2)
                print(re)
            add_upd_routine(all[0])
            rr.close_db()
    else :
        """When no routines have been created yet."""
        print("\nNo routines created yet!\n")