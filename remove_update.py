"""This will handle removal updating a routine.

helper_funcs - module that contains assistant functions
exercise_routine_classes - module that contains all classes related to routines
exercise_classes - module that contains all classes related to routines
"""
from helper_funcs import *
from routine_classes import *
from exercise_classes import *

def remove_upd_routine(name) :
    """This wil handle the removal of exercises from a routine.
    
    Routine_Exercise - object of an exercise in a routine
    Routine_Repository - class responsible for all CRUD related to routines
    init_routine_exercise - initialises values of an exercise from database data
    read_from_db - method responsible for reading data from database
    rouine_dict - dictionary for temporary storage of altered routine
    Routine_table - class that contains all exercises from routine
    add_to_db - method that adds data to database
    delete_from_db - deletes data from database
    close_db - method that closes connection to database
    """
    rr = Routine_Repository()
    routine_dict = {}
    data = rr.read_from_db(name, "routine")
    for count, item in enumerate(data, 1) :
        """Initialise a exercise routine object and display all exercises."""
        re = Routine_exercise()
        re.init_routine_exercise(item)
        routine_dict[str(count)] = re
        print(f"{count})")
        print(re)
    add_more1 = True
    while add_more1 :
        """Have user enter number dispalyed with exercise that they want to remove."""
        remove_ex = input("\nEnter number of exercise : ")
        remove_ex = remove_ex.lstrip()
        remove_ex = remove_ex.rstrip()

        if remove_ex in routine_dict.keys() :
            """When the exercise is in the dictionary remove it, ask they would like to remove more."""
            routine_dict.pop(remove_ex)
            add_more1 = add_more("remove another exercise")
            if not add_more1 :
                """When the user is finished delete old routine and add updated routine."""
                rt = Routine_table(name)
                rr.delete_from_db(name, "yes")
                for exercise in routine_dict.keys() :
                    rt.add_to_routine(routine_dict[exercise])
                rr.add_to_db(rt, "no")
                print("\nRoutine updated!\n")

        else :
            print("\nEnter valid response!") 

def remove_upd_routine_frame() :
    """This will handle user choice to remove exercise from routines.
    
    Routine_Repository - class that handles all CRUD for workout routines
    routine_validation - checks if there are routines created or not
    read_from_db - method to read data from the database
    workout_input_valid - ensures user adhere to naming rules of workout routines
    Routine_exercise - exercise object for routines
    init_routine_exercise - initialises a exercise object from database data
    add_more - get user response to continue or not
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
                    remove_upd_routine(name)
                    rr.close_db()
                        
                else :
                    """When user input an incorrect name for routine."""
                    print("Routine name not valid")
                    add_more2 = add_more("try again")
                    if not add_more2 :
                        rr.close_db()

        else :
            """User only has one routine."""
            remove_upd_routine(all[0])
            rr.close_db()
    else :
        """When no routines have been created yet."""
        print("\nNo routines created yet!\n")