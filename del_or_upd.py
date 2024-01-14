"""This contains the function that will handle user choice delete or update exercises.

deleting - module that contains function that handle deleting
upd_exercise - module that contains function that handle update of exercises
"""
from deleting import *
from upd_exercise import *

def del_or_upd() :
    """Function willl help user navigate options of delete and update.
    
    deleting - function that handles deleting
    upd_exercise - function that handle update of exercise
    initiate - cariable that help control while loop
    menu - contains list of options for user
    user_pref - contains user choice
    """
    initiate = True
    while initiate :
        menu = """\nChoose from following :
1) Delete
2) Update
3) Cancel
: """
        user_pref = input(menu)

        if user_pref == "1" :
            """When user choose to delete option."""
            deleting()
            initiate = False

        elif user_pref == "2":
            """When user choose update option."""
            upd_exercise()
            initiate = False

        elif user_pref == "3" :
            """When user choose to cancel both delete and update."""
            initiate = False
        
        else :
            print("Enter a valid response! Try digits.")