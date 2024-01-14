"""This will handle user choices after choosing to update a routine.

add_update - module that handles if user wants to add exercise to a routine
remove_update - module that handles user choice to remove exercises from routine
"""
from add_update import *
from remove_update import *

def upd_options() :
    """This will take user choice on how to update."""

    menu = """\nWould you like to :
1) Add an exercise
2) Remove an exercise
: """
    while True :
        user_pref = input(menu)

        if user_pref == "1" :
            add_upd_routine_frame()
            break
        
        elif user_pref == "2" :
            remove_upd_routine_frame()
            break

        else :
            print("Enter valid response!")