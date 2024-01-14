"""This is the main function for controllling the 'view exercise' choice.

exercise_classes - module that contains classes related to exercises/ categories
helper_funcs -  module that contains assistant functions
"""
from exercise_classes import *
from helper_funcs import *

def view_category() :
    """This is to view exercises by category.

    add_more1 - variable to control while loop
    """
    view_more = True
    while view_more : 
        """
        category - variable to store category name input from user
        input_validation - ensure user does input a category name
        valid - variable to store boolean whether category exist True if it does, False if not
        category_validation - check to see if category exist and return a boolean
        """
        category = input_validation("category")
        valid = category_validation(category)
        r = Exercise_Repository()
        if valid :
            """When the category does exist.
                    
            Exercise_Repository - class responsible for exercise CRUD
            read_from_db - method to read category data from database

            """
            data = r.read_from_db(category)
            for item in data :
                """This will create an instance of an exercise and display it to the user.
                        
                Exercise -exercise class
                init_exercise - method that takes a tuple and sets the values in tuple 
                                to respective attributes of class
                """
                ex = Exercise()
                ex.init_exercise(item)
                print(ex)
            """Prompts the user if they would like to view more categories"""
            view_more = add_more("view more categories")
                    
        else :
            """When the entered category does not exist or entered wrong.
                    
            add_more - Prompts the user if they would like to view more categories
            """
            print("Category does not exist!")
            view_more = add_more("try again")

        r.close_db()