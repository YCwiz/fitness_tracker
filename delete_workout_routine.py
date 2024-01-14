"""This contains the funtion that will handle user choice delete workout routines.

helper_funcs - module that contains assistant functions
exercise_routine_classes - module that contains all classes related to routines
"""
from helper_funcs import *
from routine_classes import *


def delete_routine() :
    """This will handle user choice to delete routines.
    
    Routine_Repository - class that handles all CRUD for workout routines
    routine_validation - checks if there are routines created or not
    read_from_db - method to read data from the database
    delete_from_db - method to delete from database
    workout_input_validation - ensures user adhere to naming rules of workout routines
    Routine_exercise - exercise object for routines
    init_routine_exercise - initialises a exercise object from database data
    add_more - get user response to continue or not
    add_mor1 - variable to control while loop
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
        """ask if user still want to delete routine."""
        add_more1 = add_more("proceed with deleting routine")
        if add_more1 :
            """When user choose to delete."""
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
                    rr.delete_from_db(name)
                    print(f"\n{name.capitalize()} is deleted!\m")
                    if len(all) > 1 :
                        """When there is more than one routine ask user if they would like to delete more."""
                        add_more2 = add_more("delete more routines")
                        if add_more2 :
                            return delete_routine()
                        else :
                            rr.close_db()

                    else :
                        """When there is only one routine exit."""
                        add_more2 = False

                else :
                    """When user input an incorrect name for routine."""
                    print("Routine name not valid")
                    add_more2 = add_more("try again")
                    if not add_more2 :
                        rr.close_db()
        else :
            """When user choose not to view a particular routine."""
            return
    else :
        """When no routines have been created yet."""
        print("\nNo routines created yet!\n")