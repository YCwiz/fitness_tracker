"""This will help user with choice to set or delete a goal.

set_goal - module to help user set new goals
delete_goal - module that will help user delete goals
"""
from set_goal import *
from delete_goal import *

def set_or_del() :
    """This will take user choice to create or delete a goal.
    
    set_goal - function that allows user to create a goal
    delete_goal - function that allows user to delete goals
    """
    menu = f"""\nWould you like to :
1) Set a goal
2) Delete a goal
: """
    while True :

        user_pref = input(menu)

        if user_pref == "1" :
            set_goal()
            break

        elif user_pref == "2" :
            delete_goal()
            break

        else :
            print("Enter valid response!")