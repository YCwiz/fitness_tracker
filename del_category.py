"""This module contains main function that will assist in the deletion category of exercises.

exercise_classes -  module that contains classes related to exercises
helper_funcs - module that contains assistant functions
"""
from exercise_classes import *
from helper_funcs import *


def del_category() :
    """This is the main funtion for deleting an entire category.
    
    input_validation - assistant function that ensure user does enter values
    category_validation - this will return a boolean if a category exist or not
    Exercise_repository - class responsible for exercise/category CRUD
    Exercise - class object for retaining exercise values
    read_from_db - method to read data from database
    init_exercise - method to initialise an exercise from database data
    delete_from_db - method that removes a category from databse
    add_more - function to get user choice to continue or exit returns a boolean
    category - variable to store user category name input
    valid - contains boolean whether category exist, True if it does, False if not
    data - store database retrieved data
    r - instance of Exercise_Repository class
    ex - instance of exercise class
    del_more - stores users choice to continue or exit
    """
    """Get user category name input and check if it exists."""
    category = input_validation("category")
    valid = category_validation(category)
    r = Exercise_Repository()
    if valid :
        """When the category exist."""
        data = r.read_from_db(category)
        for item in data :
            """Display all exercises to the user under category."""
            ex = Exercise()
            ex.init_exercise(item)
            print(ex)
        """Delete the category and ask if user would like to delete more or exit."""
        r.delete_from_db(ex)
        del_more = add_more("delete more categories")
        if del_more :
            print("Category deleted!")
            return del_category()
                        
        else :
            print("Category deleted!")
            r.close_db()
            return False
            
    else :
        """When category does not exist display a message, ask they would like to try again."""
        print("Category does not exist!")
        del_more = add_more("try again")
        if del_more :
            return del_category()
        else :
            r.close_db()
            return False