"""This will assist user in choice to delete goal.

helper_funcs - module for assistant functions
goal_classes - module that contains all classes related to goals
"""
from helper_funcs import *
from goal_classes import *

def delete_goal() :
    """This will delete a goal from the database.
    
    Goal_Repository -  class responsible for CRUD related to goals
    goal_validation - assistant function that check if goals are created yet
    read_from_db - method that reads goals from database
    goals - lsit for temporarily storing goals
    input_validation - assistant function that ensures user input values
    delete_from_db - method that delete goals from the database
    add_more - assistant function ask user if want to perform more actions, returns a boolean
    """
    """Check if goals have been created."""
    valid = goal_validation()
    if valid :
        """When goals have been created, get all goals."""
        goals = []
        gr = Goal_Repository()
        data = gr.read_from_db(pref = "yes")
        """Display goals to user."""
        print("\nGoals :")
        for item in data :
            print(item[0].title())
            goals.append(item[0])
        """Get name goal to be deleted."""
        add_more1 = True
        while add_more1 :
            if len(goals) > 0 :
                name = input_validation("goal name")
                if name in goals :
                    """When user entered name correct."""
                    gr.delete_from_db(name)
                    print("Goal deleted!")
                    goals.remove(name)
                    """Ask if they would like to delete more goals."""
                    add_more1 = add_more("delete more goals")
                    if not add_more1 :
                        gr.close_db()

                else :
                    """When user entered incorrect name."""
                    print("Goal name invalid!")
                    add_more1 = add_more("try again")
                    if not add_more1 :
                        gr.close_db()
            else :
                print("\nNo goals available!\n")
                add_more1 = False
    else :
        """When no goals have been created."""
        print("\nNo goals created yet!\n")