"""this will handle goal progress calculations.

helper_funcs - module of assistant functions
goal_classes - module that all classes related to goals
"""
from helper_funcs import *
from goal_classes import *


def goal_progress(goal) :
    """Will be responsible for calculating goal progress."""
    print(f"\nGoal Progress : {goal.name.title()}")

    if goal.reps_goal != 0 :
        """This calculate reps progress."""
        current = digit_validator("current reps")
        progress = round((current - goal.reps) / (goal.reps_goal - goal.reps) * 100)
        print(f"Start : {goal.reps} \nGoal : {goal.reps_goal} \nProgress : {progress}%")
        progress_comment(progress)

    if goal.sets_goal != 0 :
        """This calculate sets progress."""
        current = digit_validator("current sets")
        progress = round((current - goal.sets) / (goal.sets_goal - goal.sets) * 100)
        print(f"Start : {goal.sets} \nGoal : {goal.sets_goal} \nProgress : {progress}%")
        progress_comment(progress)

    if goal.weight_goal != 0 :
        """This calculate weight progress."""
        current = digit_validator("current weight")
        progress = round((current - goal.weight) / (goal.weight_goal - goal.weight) * 100)
        print(f"Start : {goal.reps} \nGoal : {goal.weight_goal} \nProgress : {progress}%")
        progress_comment(progress)

    if goal.distance_goal != 0 :
        """This calculate distance progress."""
        current = digit_validator("current distance")
        progress = round((current - goal.distance) / (goal.distance_goal - goal.distance) * 100)
        print(f"Start : {goal.reps} \nGoal : {goal.distance_goal} \nProgress : {progress}%")
        progress_comment(progress)

    if goal.laps_goal != 0 :
        """This calculate laps progress."""
        current = digit_validator("current laps")
        progress = round((current - goal.laps) / (goal.laps_goal - goal.laps) * 100)
        print(f"Start : {goal.reps} \nGoal : {goal.laps_goal} \nProgress : {progress}%")
        progress_comment(progress)

def view_goal_progress() :
    """This will view goals the database.
    
    Goal_Repository -  class responsible for CRUD related to goals
    Goal - goal object
    goal_validation - assistant function that check if goals are created yet
    read_from_db - method that reads goals from database
    goals - lsit for temporarily storing goals
    input_validation - assistant function that ensures user input values
    init_goal - method that initialise goals from database data
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
        """Get name goal to be viewed."""
        add_more1 = True
        while add_more1 :
            if len(goals) > 0 :
                name = input_validation("goal name")
                if name in goals :
                    """When user entered name correct."""
                    data2 = gr.read_from_db(name)
                    g = Goal()
                    g.init_goal(data[0])
                    print("Goal progress!")
                    goal_progress(g)
                    """Ask if they would like to view more goals."""
                    add_more1 = add_more("view more goals")
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