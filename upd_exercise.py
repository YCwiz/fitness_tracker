"""This contains the main function when user chooses to update a single exercise.

exercise_classes - module that contain classes related to exercises
helper_funcs - module that contains assistant functions
"""
from exercise_classes import *
from helper_funcs import *

def upd_exercise() :
    """This is the main funtion for updating a single exercise at a time.
    
    input_validation - assistant function that ensure user does enter values
    category_validation - this will return a boolean if a category exist or not
    user_exercise - functions that gets user input and initialise an instance of exercise
    Exercise_repository - class responsible for exercise/category CRUD
    Exercise - class object for retaining exercise values
    read_from_db - method to read data from database
    init_exercise - method to initialise an exercise from database data
    delete_from_db - method that removes a category from databse
    add_to_db - method that adds an exercise to database
    add_more - function to get user choice to continue or exit returns a boolean
    name - variable to store user exercise name input
    valid - contains boolean whether category exist, True if it does, False if not
    data - store database retrieved data
    r - instance of Exercise_Repository class
    old_x - instance of exercise class, exercise to be updated
    new_x - instance of exercise class, updated values
    del_more - stores users choice to continue or exit
    """
    """Get user category name input and check if it exists."""
    name = input_validation("exercise")
    valid = exercise_validation(name)
    r = Exercise_Repository()
    if not valid :
        """When the exercise exist."""
        old_x = Exercise()
        data = r.read_from_db(name, "exercise")
        old_x.init_exercise(data)
        """Display exercise to the user."""
        print(old_x)
        """Remove old exercise values from database."""
        r.delete_from_db(old_x, "exercise")

        while True :
            """Get new values from user."""
            print("\nEnter new values : ")
            new_name = input_validation("exercise")

            """Check to see if name of exercise is not already taken."""
            valid2 = exercise_validation(new_name)
            if valid2 :
                """When name is not taken get new values and add to database."""
                new_x = user_exercise(new_name)
                r.add_to_db(new_x)
                print("Exercise updated succesfully!")

                """Ask if user would like to update more or exit."""
                upd_more = add_more("update another exercise")
                if upd_more :
                    print("Exercise updated!")
                    return upd_exercise()
                            
                else :
                    print("Exercise updated!")
                    r.close_db()
                    break
            else :
                """When the name is taken, dispaly a message, ask to try another name"""
                print("Name already taken!")
                cont_upd = add_more("try another name")
                if not cont_upd :
                    """If user choose to not try another name add old exercise back into database."""
                    r.add_to_db(old_x, "exercise")
                    r.close_db()
                    break
    else :
        """When the exercise does not exist, ask user to try again or exit."""
        print("Exercise does not exists!")
        upd_more = add_more("try again")
        if upd_more :
            return upd_exercise()
        
        else :
            r.close_db()