"""This will handle user choice to delete or update a routine.

update_routine_ - module that handles updating a routine
delete_workout_routine - module that handles deletion of a routine
"""
from update_routine_ import *
from delete_workout_routine import *

def del_or_upd2() :
    """This will take user choice to delete or update.
    
    delete_routine - function that will delete an entire routine
    upd_options - function that handles option of updating
    """
    menu = """\nWould you like to :
1) Delete a routine
2) Update a routine
3) Cancel
: """
    while True :
        user_pref = input(menu)

        if user_pref == "1" :
            delete_routine()
            break
        
        elif user_pref == "2" :
            upd_options()
            break

        elif user_pref == "3" :
            return

        else :
            print("Enter valid response!")
