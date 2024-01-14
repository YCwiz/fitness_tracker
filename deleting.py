"""This will handle user choice after choosing the delete option.

del_category - module that contains the main function for deleting an entire category
del_exercise - module that contains the main function for deleting a single exercise 
"""
from del_category import *
from del_exercise import *


def deleting() :
    """Function will handle user choice after choosing delete option.
    
    del_more1 - variable that aids in controlling the while loop
    user_pref2 - stores user input/choice
    menu - contains list of choices for user
    """
    del_more1 = True
    while del_more1 :
        menu2 = """\nWhat would you like to delete? :
1) A category 
2) An exercise
3) Cancel
: """
        user_pref2 = input(menu2)

        if user_pref2 == "1" :
            """When user choose delete whole category."""
            del_more1 = del_category()

        elif user_pref2 == "2" :
            """When user choose to delete a single exercise."""
            del_more1 = del_exercise()

        elif user_pref2 == "3" :
            """When user choose to cancel deleting."""
            del_more1 = False

        else :
            print("Enter valid response!")