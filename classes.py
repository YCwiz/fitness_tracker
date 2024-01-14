class Repository :
    """Repositoty will be responsible for all CRUD."""

    def add_to_db (self, class_) :
        """Create an record of an exercise or category in db under different tables.
        
        sqlite3 - module to manage database
        datetime - allows for real time access
        class_ - is a class that will passed to be added to database
        """
        import sqlite3
        

        """Check to see if it's a exercise or category being added.
        
            db - open database 
            cursor - create a cursor to create table and create a record
            commit - enters the data to database and tables permanently
            close - closes connection to database
            """
        if class_.__class__.__name__ == "Exercise" :
            """Its an exercise so add it to exercise table. """
            db = sqlite3.connect('fitness')
            cursor = db.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS
                           exercises (name TEXT PRIMARY KEY,  
                           category TEXT, muscle_grp TEXT )''')
            db.commit()
            
            try :
                cursor.execute('''INSERT INTO exercises
                            VALUES (?, ?, ?)''',
                            (class_.name, class_.category, class_.muscle_grp) 
                                )
                db.commit()
                db.close()

            except sqlite3.IntegrityError as err :
                if err != ('UNIQUE constraint failed: exercise.name') :
                    print("Exercise already exist!")
                db.close()



        elif class_.__class__.__name__ == "Goal" :
            """This will add the goals to database."""
            db = sqlite3.connect('fitness')
            cursor = db.cursor()

            cursor.execute('''CREATE TABLE IF NOT EXISTS goals
                           (name TEXT PRIMARY KEY, reps INTEGER, reps_goal INTEGER,
                            sets INTEGER, sets_goal INTEGER,
                            weight INTEGER, weight_goal INTEGER, 
                           distance INTEGER, distance_goal INTEGER,
                           laps INTEGER, laps_goal INTEGER)''')
            db.commit()

            try :
                cursor.execute('''INSERT INTO goals
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                            (class_.name,class_.reps, class_.reps_goal, 
                                class_.sets, class_.sets_goal,
                                class_.weight, class_.weight_goal, 
                                class_.distance, class_.distance_goal,
                                class_.laps, class_.laps_goal))
                db.commit()
                db.close()
                print("Goal succesfully added!")

            except sqlite3.IntegrityError as err :
                if err != ('UNIQUE constraint failed: goal.name') :
                    print("Goal already exist!")
                db.close()
    
    def read_from_db(self, command) :
        """This willl be responsible for retrieving data from database.
        
        sqlite3 - module for database management"""
        import sqlite3
        if command == "all" :
            """This will be responsible for retrieving all exercises from database."""
            try :
                db = sqlite3.connect('fitness')
                cursor = db.cursor()

                cursor.execute('''SELECT DISTINCT category
                            FROM exercises''')
                
                categories = cursor.fetchall()
                print("\nChoose from the following :")
                for item in categories :
                    print(f"\n{item[0].title()} :")
                    cursor.execute('''SELECT *
                                FROM exercises
                                WHERE category = ?''',(item[0],))
                    for count, item2 in enumerate(cursor.fetchall(), 1) :
                        print(f"{count})")
                        disp_exercise = Exercise()
                        disp_exercise.init_exercise(item2)
                        print(disp_exercise)
                db.close()

            except sqlite3.OperationalError : 
                print("No categories created yet!")
                exit()

        elif command == "routine" :
            """This will retrieve all routines from database."""
            try :
                db = sqlite3.connect('fitness')
                cursor = db.cursor()

                cursor.execute('''SELECT *
                            FROM routines''')
                
                routines = cursor.fetchall()
                print("Choose from following : ")
                for item in routines :
                    print(f"\n{item[0].title()}")

                user_pref = input("Enter Routine name : ")
                    
                cursor.execute(f'''SELECT *
                                FROM {user_pref} ''')
                    
                data = cursor.fetchall()
                db.close()
                return data
            except sqlite3.OperationalError : 
                return "No routines created yet!"

        elif command == "goal" :
            """This will print out all goals to user from database."""

            try :
                db = sqlite3.connect('fitness')
                cursor = db.cursor()
                cursor.execute('''SELECT name
                            FROM goals''')
                data2 = cursor.fetchall()
                if len(data2) == 0 :
                    print("No goals is available!")
                    db.close()
                    exit()

                else :
                    print("\nChoose from the following :")
                    for item in data2 :
                        print(item[0])
                    db.close()

            except sqlite3.OperationalError :
                print("No goals has been set yet!")
                exit()

        elif command == "goal2" :
            """This will retrieve goals from database."""
            while True :
                name = input("Enter goal : ")

                if len(name) <= 0 :
                    print("Goal cannot be empty!")

                else :
                    break

            db = sqlite3.connect('fitness')
            cursor = db.cursor()
            cursor.execute('''SELECT *
                            FROM goals
                            WHERE name = ?''', (name,))
            goal = cursor.fetchone()
            if goal == None :
                print("Goal does not exist!")

            else :
                return goal
            
        elif command == "ex_progress" :
            """This will retrieve all routines from database."""
            db = sqlite3.connect('fitness')
            cursor =db.cursor()

            try :
                cursor.execute('''SELECT * 
                            FROM routines''')
                print("Exercise progress :")
                for item in cursor.fetchall() :
                    print(f"\nRoutine : {item[0].title()} \nDate : {item[1]}")
                db.close()
            
            except sqlite3.OperationalError :
                print("\nNo routines created yet!")
                exit()

        else :
            """This will retrieve a specific exercise from database."""
            db = sqlite3.connect('fitness')
            cursor = db.cursor()

            cursor.execute('''SELECT *
                           FROM exercises
                           WHERE name = ?''', (command,))
            return cursor.fetchone()

    def remove_from_db(self, command) :
        """This method will be reponsible for all removals from database.
        
        sqlite3 - module for database management.
        command - will give further information on what needs to be removed
        """
        import sqlite3
        if command == "category" :
            """This will remove a whole category or a single exercise."""
            self.read_from_db("all")
            db = sqlite3.connect('fitness')
            cursor = db.cursor()

            user_pref = input("""Would you like to delete :
    1) Category
    2) Exercise
    3) Cancel \n: """)
            
            if user_pref == "1" :
                
                del_category = input("Enter category : ").lower()

                cursor.execute('''SELECT COUNT() 
                                   FROM exercises 
                                   WHERE category = ?''', (del_category,))
                    
                check = cursor.fetchone()
                if check[0] > 0 :
                    cursor.execute('''DELETE 
                                FROM exercises
                                WHERE category = ?''', (del_category,))
                    db.commit()
                    db.close()
                    print(f"{del_category.title()} successfully deleted.")

                else :
                    print(f"{del_category.title()} category does not exist!")
                    db.close()

            elif user_pref == "2" :
                del_exercise = input("Enter exercise : ").lower()
                cursor.execute('''SELECT COUNT() 
                                   FROM exercises 
                                   WHERE name = ?''', (del_exercise,))
                    
                check = cursor.fetchone()
                if check[0] > 0 :
                    cursor.execute('''DELETE
                                FROM exercises
                                WHERE name = ?''', (del_exercise,))
                    db.commit()
                    db.close()
                    print(f"{del_exercise.title()} successfully deleted.")

                else :
                    print(f"{del_exercise.title()} exercise does not exist!")


            else :
                print("Goodbye!")
        
        elif command.__class__.__name__ == "Goal" :



