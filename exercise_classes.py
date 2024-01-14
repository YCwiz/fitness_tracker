class Exercise :
    """This class will be exercise object.
    
    __init__ - initialisation of class
    __str__ - representation of class to user
    init_exercise - will initialise values of a exercise from database data
    """
    def __init__(self, name = "", category = "", muscle_grp = "") :
        """Creates an instance of an exercise.

        name - is the exercise that should be unique
        category - category under which exerxise will fall
        muscle_grp - is the targeting muscle group of the exercise, do not need to be entered
        """
        self.name = name
        self.category = category
        self.muscle_grp = muscle_grp

    def __str__(self):
        """Creates a user representation of an exercise."""

        info = f"""\nExercise :
Name : {self.name.title()}
Category : {self.category.title()}
Muscle Group : {self.muscle_grp.title()} \n"""
        return info

    def init_exercise(self, data) :
        """intialise an instance of exercise.
        
        data - record retrieved from exercise table
        """
        self.name = data[0]
        self.category = data[1]
        self.muscle_grp = data[2]


class Exercise_Repository :
    """This class will be doing all CRUD operations.
    
    __init__ - initialisation of class object
    add_to_db - adds exercises to database
    read_from_db - read data from database
    update_db - updates records in database
    delete_from_db - removes exercises or categories from database
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

    def add_to_db(self, exercise_class) :
        """This method will input exercise data into database."""

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS exercises 
                            (name TEXT PRIMARY KEY, category TEXT, muscle_grp TEXT)''')
        
        self.db.commit()

        self.cursor.execute('''INSERT INTO exercises
                            VALUES (?, ?, ?)''', 
                            (exercise_class.name, exercise_class.category, exercise_class.muscle_grp))
        self.db.commit()

    def read_from_db(self, name, pref = "") :
        """This method will read from database.
        
        sqlite3 - module for database management
        """
        import sqlite3 # reason for importing again is to validate error
        if pref == "exercise" :
            """To read information from database based on name of exercise."""
            try :
                self.cursor.execute('''SELECT *
                                    FROM exercises
                                    WHERE name = ?''', (name,))
                data = self.cursor.fetchone()
                return data
            
            except sqlite3.OperationalError :
                return "No exercises created yet!"
        
        else :
            """To read information from database based on exercise category."""
            try :
                self.cursor.execute('''SELECT *
                                    FROM exercises
                                    WHERE category = ?''', (name,))
                data = self.cursor.fetchall()
                return data
            
            except sqlite3.OperationalError :
                return "No exercises created yet!"

    def update_db(self, old_category, new_category) :
        """This method will be responsible for updating exercises in database."""

        self.cursor.execute(f'''UPDATE exercises
                            SET category = {new_category}
                            WHERE category = {old_category}''')
        self.db.commit()

    def delete_from_db(self, exercise, pref = "") :
        """This method will remove exercises from the database.
        
        pref - user selection for deleting whole category or just an exercise"""
        if pref == "exercise" :
            self.cursor.execute('''DELETE
                                FROM exercises
                                WHERE name = ?''', (exercise.name,))
            self.db.commit()

        else :
            self.cursor.execute('''DELETE
                                FROM exercises
                                WHERE category = ?''', (exercise.category,))
            self.db.commit()

    def close_db(self) :
        """Method will close the database."""
        self.db.close()

