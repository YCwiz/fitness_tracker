"""This module contains all classes related to goals."""
class Goal :
    """This class will be exercise object.
    
    __init__ - initialisation of class
    __str__ - representation of class to user
    init_goal - will initialise values of a goal from database data
    """

    def __init__(self, name = "", reps = 0.0, reps_goal = 0.0, sets = 0.0, sets_goal = 0.0, 
                 weight = 0.0, weight_goal = 0.0, distance = 0.0, distance_goal = 0.0, 
                 laps = 0.0, laps_goal = 0.0) :
        """This will record goals that a user set from an existing exercise."""
        self.name = name
        self.reps = reps
        self.reps_goal = reps_goal

        self.sets = sets
        self.sets_goal = sets_goal
        
        self.weight = weight
        self.weight_goal = weight_goal
        
        self.distance = distance
        self.distance_goal = distance_goal
        
        self.laps = laps
        self.laps_goal = laps_goal

    def __str__(self) :
        """User representation of a goal."""
        return f"""\nGoal : 
Name : {self.name}
Reps at Start : {self.reps}
Reps Goal : {self.reps_goal}
Sets at Start : {self.sets}
Sets Goal : {self.sets_goal}
Distance at Start : {self.distance}
Distance Goal : {self.distance_goal}
Laps at Start : {self.laps}
Laps Goal : {self.laps_goal}"""
    
    def init_goal(self, data) :
        """This will initialise an instance of a goal from data retrieved from database."""
        self.name = data[0]
        self.reps = data[1]
        self.reps_goal = data[2]
        self.sets = data[3]
        self.sets_goal = data[4]
        self.weight = data[5]
        self.weight_goal = data[6]
        self.distance = data[7]
        self.distance_goal = data[8]
        self.laps = data[9]
        self.laps_goal = data[10]


class Goal_Repository :
    """this will handle all CRUD for goals.
    
    __init__ - initialisation of class
    add_to_db - adds goal to database
    delete_from_db - deletes a goal from database
    read_from_db - reads data from database
    close_db - closes connection to database
    """
    def __init__(self) :
        """This method will initialise a connection with the databse.
        
        sqlite3 - module for database management
        self.db - connection to database
        self.cursor - cursor obeject to write and read from database
        """
        import sqlite3
        self.db = sqlite3.connect('fitness')
        self.cursor = self.db.cursor()


    def add_to_db(self, goal) :
        """This will be responsible for adding goals to database."""

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS goals 
                            (name TEXT PRIMARY KEY, reps INTEGER, reps_goal INTEGER, sets INTEGER, sets_goal INTEGER, 
                 weight INTEGER, weight_INTEGER, distance INTEGER, distance_goal INTEGER, 
                 laps INTEGER, laps_goal INTEGER)''')
        
        self.db.commit()

        self.cursor.execute('''INSERT INTO goals
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                            (goal.name, goal.reps, goal.reps_goal, goal.sets, 
                             goal.sets_goal, goal.weight, goal.weight_goal, 
                             goal.distance, goal.distance_goal, goal.laps, goal.laps_goal))
        self.db.commit()


    def delete_from_db(self, name) :
        """This will remove a goal."""
        
        self.cursor.execute('''DELETE 
                    FROM goals
                    WHERE name = ?''', (name,))
        self.db.commit()

    def read_from_db(self, name = "", pref = "") :
        """This will read data from database.
        
        sqlite3 - module for databasse management, imported again to validate error
        """
        import sqlite3
        if pref == "" :
            try :
                self.cursor.execute('''SELECT *
                                    FROM goals
                                    WHERE name = ?''', (name,))
                data = self.cursor.fetchall()
                return data
            
            except sqlite3.OperationalError :
                return "No goals created yet!"
            
        else :
            try :
                self.cursor.execute('''SELECT *
                                    FROM goals''')
                data = self.cursor.fetchall()
                return data
            
            except sqlite3.OperationalError :
                return "No goals created yet!"

    def close_db(self) :
        self.db.close()

