class Routine_exercise() :
    """Rhis will contain the values of a single exercise in a routine.
    
    __init__ - initialisation of object
    init_routine_exercise - will initialise a single exercise from database data
    __str__ - will give representation of exercise to user
    """
    def __init__(self, name = "", category = "", muscle_grp = "", reps = 0.0, sets = 0.0, weight = 0.0, distance = 0.0, laps = 0.0) :
        """Routine exercise will be a single recored in a routine table.
        
        name - will be the name of an already created exercise
        category - category of an already existing exercise
        muscle_grp - is the targeting muscle group of the exercise
        reps - is number of repitions per set
        sets - will record the number of sets of the exercise
        distance - distance is in the event of a running or jogging exercise
        laps - is the number of laps per distance
        """
        self.name = name
        self.category = category
        self.muscle_grp = muscle_grp
        self.reps = reps
        self.sets = sets
        self.weight = weight
        self.distance = distance
        self.laps = laps

    def init_routine_exercise(self, data) :
        """This will initialise a routine from data retrieved from database."""
        self.name = data[0]
        self.category = data[1]
        self.muscle_grp = data[2]
        self.reps = data[3]
        self.sets = data[4]
        self.weight = data[5]
        self.distance = data[6]
        self.laps = data[7]


    def __str__(self) :
        """Readable representation of exercise to user."""
        description = f"""\nName : {self.name}
Category : {self.category}
Muscle Group : {self.muscle_grp}
Reps/Set : {self.reps}
Sets : {self.sets}
Weight : {self.weight}
Distance : {self.distance}
Laps : {self.laps}\n"""
        return description


class Routine_table :
    """Will be responsible for recording all exercises in a routine."""

    def __init__(self, name = "") :
        """
        name - is the name of the workout routine
        self.all - will contain all exercise routines of workout"""
        self.name = name
        self.all = []

    def add_to_routine(self, routine_exercise) :
        """This method will add exercises to routine."""
        self.all.append(routine_exercise)


class Routine_Repository :
    """This class will be responsible for all CRUD of workout routines
    
    __init__ - initialisation of class object
    add_to_db - adds exercises to database
    read_from_db - read data from database
    update_db - updates records in database
    delete_from_db - removes routines from database
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

    def add_to_db(self, routine_table, pref = "") :
        """This will add the routines to database.

        datetime - module to help get current date
        """
        from datetime import datetime
        if pref == "" :
            self.cursor.execute(f'''CREATE TABLE {routine_table.name}
                            (name TEXT,  
                            category TEXT, muscle_grp TEXT,
                            reps INTEGER, sets INTEGER, weight INTEGER, distance INTEGER, laps INTEGER)''')
            self.db.commit()

            for item in routine_table.all :
                self.cursor.execute(f'''INSERT INTO {routine_table.name}
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', 
                                (item.name, item.category, item.muscle_grp, item.reps,
                                    item.sets, item.weight, item.distance, item.laps))
                self.db.commit()

            self.cursor.execute('''CREATE TABLE IF NOT EXISTS
                                routines (name VARCHAR PRIMARY KEY, date INTEGER)''')
            self.db.commit()

            today_date = datetime.now()
            self.cursor.execute('''INSERT INTO routines
                            VALUES (?, ?)''', (routine_table.name, today_date.strftime('%Y-%m-%d')))
            self.db.commit()
        
        else :
            self.cursor.execute(f'''CREATE TABLE {routine_table.name}
                            (name TEXT,  
                            category TEXT, muscle_grp TEXT,
                            reps INTEGER, sets INTEGER, weight INTEGER, distance INTEGER, laps INTEGER)''')
            self.db.commit()

            for item in routine_table.all :
                self.cursor.execute(f'''INSERT INTO {routine_table.name}
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', 
                                (item.name, item.category, item.muscle_grp, item.reps,
                                    item.sets, item.weight, item.distance, item.laps))
                self.db.commit()


    def read_from_db(self, name = "", pref = "") :
        """This will be rsponsible for reading data from the databse.
        
        sqlite3 -  module for database management, but here to validate errors
        """
        import sqlite3
        if pref == "routines" :
            try :
                self.cursor.execute('''SELECT *
                                    FROM routines
                                    WHERE name = ?''', (name,))
                data = self.cursor.fetchall()
                return data
            except sqlite3.OperationalError :
                return "No routines created yet!"
            
        elif pref == "routine" :
            try :
                self.cursor.execute(f'''SELECT *
                                        FROM {name}''')
                data = self.cursor.fetchall()
                return data
            except sqlite3.OperationalError :
                return "Routine does not exist!"
            
        elif pref == "routiness" :
            try :
                self.cursor.execute('''SELECT *
                                    FROM routines''')
                data = self.cursor.fetchall()
                return data
            except sqlite3.OperationalError :
                return "No routines created yet!"
            
            
    def delete_from_db(self, name, pref = "") :
        """This will remove data from database."""
        if pref == "" :
            self.cursor.execute(f'''DROP TABLE {name}''')
            self.db.commit()

            self.cursor.execute('''DELETE
                                FROM routines
                                WHERE name = ?''', (name,))
            self.db.commit()

        else :
            self.cursor.execute(f'''DROP TABLE {name}''')
            self.db.commit()

    def update_db(self, routine_table, exercise_routine) :
        """This will help update database."""
        self.cursor.execute(f'''INSERT INTO {routine_table}
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                              (exercise_routine.name, exercise_routine.category, 
                               exercise_routine.muscle_grp, exercise_routine.reps,
                                exercise_routine.sets, exercise_routine.weight, 
                                exercise_routine.distance, exercise_routine.laps))
        self.db.commit()
    
    def close_db(self) :
        self.db.close()
            










