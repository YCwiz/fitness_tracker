"""This will help user set a goal.

goal_classes - module that contains all classes related to goals
helper_funcs - module that contains assistant functions
"""
from goal_classes import *
from helper_funcs import *


def set_goal() :
    """This will help user to set a goal.
    
    Goal_Repository - class responsible for all CRUD related to goals
    input_validation - assistant functions that ensures user input values
    exercise_validation - assistant function that check if a exercise is in database
    user_goal - assistant function that helps user create a goal
    add_more - assistant function that ask whether user would like perform mor actions
    add_to_db - method that adds data to database
    """
    gr = Goal_Repository()
    add_more1 = True
    while add_more1 :
        name = input_validation("exercise name")
        valid = exercise_validation(name)
        if not valid :
            valid1 = goal_validation2(name)
            if not valid1 :
                goal = user_goal(name)
                gr.add_to_db(goal)
                print("\nGoal created!")
                add_more1 = add_more("set another goal")
                if not add_more1 :
                    gr.close_db()
            
            else :
                print("Goal already set for exercise!")
                add_more1 = add_more("try another exercise")
                if not add_more1 :
                    gr.close_db()
        
        else :
            print("\nExercise name not valid. Add to exercise first.")
            add_more1 = add_more("try another exercise")