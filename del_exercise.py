"""This contains the main function when user chooses to delete a single exercise.

exercise_classes - module that contain classes related to exercises
helper_funcs - module that contains assistant functions
"""
from exercise_classes import *
from helper_funcs import *


def del_exercise() :
    """This is the main funtion for deleting a single exercise at a time.
    
    input_validation - assistant function that ensure user does enter values
    category_validation - this will return a boolean if a category exist or not
    Exercise_repository - class responsible for exercise/category CRUD
    Exercise - class object for retaining exercise values
    read_from_db - method to read data from database
    init_exercise - method to initialise an exercise from database data
    delete_from_db - method that removes a category from databse
    add_more - function to get user choice to continue or exit returns a boolean
    name - variable to store user exercise name input
    valid - contains boolean whether category exist, True if it does, False if not
    data - store database retrieved data
    r - instance of Exercise_Repository class
    x - instance of exercise class
    del_more - stores users choice to continue or exit
    """
    """Get user category name input and check if it exists."""
    name = input_validation("exercise")
    valid = exercise_validation(name)
    r = Exercise_Repository()
    if not valid :
        """When the exercise exist."""
        x = Exercise()
        data = r.read_from_db(name, "exercise")
        x.init_exercise(data)
        """Display exercise to the user."""
        print(x)
        """Delete the exercise and ask if user would like to delete more or exit."""
        r.delete_from_db(x, "exercise")
        del_more = add_more("delete another exercise")
        if del_more :
            print("Exercise deleted!")
            return del_exercise()
                        
        else :
            print("Exercise deleted!")
            r.close_db()
            return False
    else :
        """When exercise does not exist display a message, ask they would like to try again"""
        print("Exercise does not exists!")
        del_more = add_more("try again")
        if del_more :
            return del_exercise()
        else :
            r.close_db()
            return False