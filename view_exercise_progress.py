"""This will handle user option view exercise progress.

exercise_routine_classes - module that contains all classes related to workout routine
"""
from routine_classes import *

def view_exercise_progress() :
    """This will give user exercises.
    
    Routine_Repository - class that handles all CRUD for workout routines
    read_from_db - method to read from database
    """
    rr = Routine_Repository()
    data = rr.read_from_db(name = "", pref = "routiness")
    if len(data) != 0 and type(data) != type("") :
        for item in data :
            progress = f"""\nRoutine name : {item[0]}
Date : {item[1]}\n"""
            print(progress)
    else :
        print("\nNo progress recorded!\n")