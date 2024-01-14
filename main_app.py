"""This is the main user interface.

del_or_upd - module for delete or updating exercises
add_exercise - module that aids adding of exercises to database
view_exercise_category - module for viewing of exercises
create_workout_routine - module for creating routines
view_workout_routine - module for viewing a workout routine
delete_workout_routine - module for deleting workout routines from database
exercise_routine_classes - module for viewing exercise progress
del_or_upd_routine - module for deleting or updating a routine
set_or_delete_goal - module to setting or deleting goaals
"""
from del_or_upd import *
from add_exercise import *
from view_exercise_category import *
from create_workout_routine import *
from view_workout_routine import *
from delete_workout_routine import *
from view_exercise_progress import *
from del_or_upd_routine import *
from set_or_delete_goal import *
from view_goal_progress import *
"""This will be all fuctions required to run app."""

def ui_display() :
    """Main function for user."""
    menu = """Enter your preference :
1) Add exercise category
2) View exercise by category
3) Delete/Update exercise by category
4) Create Workout Routine
5) View Workout Routine
6) Delete/Update Workout Routine
7) View Exercise Progress
8) Set/Delete Fitness Goals
9) View Progress towards Fitness Goals
10) Quit

: """
    while True :
        user_pref = input(menu)

        if user_pref == "1" :
            add_exercise_category()

        elif user_pref == "2" :
            view_category()

        elif user_pref == "3" :
            del_or_upd()
            
        elif user_pref == "4" :
            create_workout_routine()
            
        elif user_pref == "5" :
            view_workout_routine()            

        elif user_pref == "6" :
            del_or_upd2()

        elif user_pref == "7" :
            view_exercise_progress()

        elif user_pref == "8" :
            set_or_del()
            
        elif user_pref == "9" :
            view_goal_progress()

        elif user_pref == "10" :
            """This will allow user to exit."""
            print("Goodbye!")
            exit()
        else :
            print("\nEnter a valid response!\n")

ui_display()