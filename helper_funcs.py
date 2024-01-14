"""All function found here does not neccessarily belong to any one class.

exercise_classes - module that contains classes related to exercises
exercise_routine_classes - module that contains classes retalted to routine
"""
from exercise_classes import *
from routine_classes import *
from goal_classes import *

def exercise_validation(name) :
    """Function will check to see if there is an record of an exercise.
    
    Exercise_Repository - instance of class that is responsible for exercise CRUD
    read_from_db - this method will read from database
    name - is the name of target exercise
    return a boolean
    """
    ex = Exercise_Repository()
    exr = ex.read_from_db(name, "exercise")
    if type(exr) == type(None) :
        return True
    elif type(exr) == type("") :
        return True
    else :
        return False
    

def input_validation(pref) :
    """This function will verify that user does enter values.
    
    value - variable that will contain user input
    """
    while True :

        value = input(f"Enter {pref} : ").lower()

        if len(value) <= 0 :
            print(f"{pref.capitalize()} cannot be empty!")

        else :
            break

    return value


def user_exercise(name) :
    """Retrieve data from the user for initialisation of exercise.
    
    name - name of exercise
    category - category of exercise 
    muscle_grp - targeting muscle group of exercise
    """
    category = input_validation("category")

    muscle_grp = input("Enter muscle group (Optional) : ").lower()

    exercise = Exercise(name, category, muscle_grp)

    return exercise


def add_more(pref) :
    """This will give the option to the user to add more or try again.
    
    pref - this will give user a preference on what they would like to do again
    """
    while True :
        pref = input(f"""\nWould you like to {pref}?
1) Yes
2) No
: """)
        if pref == "1" : 
            return True

        elif pref == "2" :
            return False
            
        else :
            print("Enter valid response! Try digits.")


def category_validation(name) :
    """Function will check to see if there is a record of an exercise.
    
    Exercise_Repository - instance of class that is responsible for exercise CRUD
    read_from_db - this method will read from database
    name - is the name of target exercise
    return a boolean
    """
    ex = Exercise_Repository()
    exr = ex.read_from_db(name)
    if len(exr) == 0 :
        return False
    elif type(exr) == type("") :
        return False
    else :
        return True

def workout_input_valid(pref = "" ) :
    """Function will ensure input values for workout name and it does not include spaces.
    
    pref - if the user would like to print out a message to user
    """
    if pref == "" :
        print("\nRoutine name must be unique and contain no spaces!")
    name = input_validation("routine name")
    if " " in name :
        return workout_input_valid()
    
    else :
        return name
    
def workout_validation(name) :
    """Function will check to see if there is routine.
    
    Exercise_Repository - instance of class that is responsible for exercise CRUD
    read_from_db - this method will read from database
    name - is the name of target exercise
    return a boolean
    """
    wr = Routine_Repository()
    exr = wr.read_from_db(name, "routines")
    if len(exr) == 0 :
        return True
    elif type(exr) == type("") :
        return True
    else :
        return False
    
def digit_validator(pref) :
    "This function ensures user input digits."
    while True :
        try :
            number = float(input(f"\nEnter {pref} : "))
            return number

        except ValueError :
            print("\nOnly make use of digits!")

def user_workout_routine(exercise) :
    """This function will get user input about workout.
    
    digit_validator - functions that helps ensure user enters a digit
    """
    print("Enter 0 if not applicable!!")
    name = exercise.name
    category = exercise.category
    muscle_grp = exercise.muscle_grp
    reps = digit_validator("number of reps/set")
    sets = digit_validator("number of sets")
    weight = digit_validator("weight in kg")
    distance = digit_validator("distance in km")
    laps = digit_validator("laps/distance")

    ex_routine = Routine_exercise(name, category, muscle_grp, reps, sets, weight, distance, laps)
    return ex_routine


def routine_validation() :
    """Function will check to see if there is routine.
    
    Exercise_Repository - instance of class that is responsible for exercise CRUD
    read_from_db - this method will read from database
    name - is the name of target exercise
    return a boolean
    """
    wr = Routine_Repository()
    exr = wr.read_from_db(pref = "routiness" )
    if len(exr) == 0 :
        return False
    
    elif type(exr) == type("") :
        return False
    
    else :
        return True
  

def user_goal(name) :
    """This will initialise a goal object for user with their input."""
    
    reps = digit_validator("current reps")
    reps_goal = digit_validator("reps goal")

    sets = digit_validator("current sets")
    sets_goal = digit_validator("sets goal")

    weight = digit_validator("current weight")
    weight_goal = digit_validator("weight goal")

    distance = digit_validator("current distance")
    distance_goal = digit_validator("distance goal")

    laps = digit_validator("current laps")
    laps_goal = digit_validator("laps goal")

    goal = Goal(name, reps, reps_goal, sets, sets_goal, weight, 
                weight_goal, distance, distance_goal, laps, laps_goal)
    return goal

def goal_validation(name = "") :
    """This will check to see if there is any goals created yet.
    
    Goal_Repository - class responsible for CRUD related to goals
    read_from_db - method to read data from database
    """
    gr = Goal_Repository()
    goals = gr.read_from_db(pref = "yes")
    if len(goals) == 0 :
        return False
    elif type(goals) == type("") :
        return False
    else :
        return True
    
def goal_validation2(name = "") :
    """This will check to see if there is any goals created yet.
    
    Goal_Repository - class responsible for CRUD related to goals
    read_from_db - method to read data from database
    """
    gr = Goal_Repository()
    goals = gr.read_from_db(name)
    if len(goals) == 0 :
        return False
    elif type(goals) == type("") :
        return False
    else :
        return True
    
def progress_comment(progress) :
    """This will give comment on progress."""
    if progress <= 15 :
        print("Consistency is key. Keep up the good work!\n")

    elif progress > 15 and progress <= 50 :
        print("Rome wasn't built in a day. Lets push!\n")

    elif progress > 50 and progress <= 70 :
        print("Almost there. Lets push more Champ!\n")

    else :
        print("Champions go till the end!\n")

