import sqlite3
from student import Student
from instructor import Instructor
from cohort import Cohort
from exercise import Exercise

class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/rockmurdock/workspace/python/python-student-exercises/studentexercises.db"

    def all_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student(row[1], row[2], row[3], row[5])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.Id,
                s.First_Name,
                s.Last_Name,
                s.Slack,
                s.CohortId,
                c.Name
            from Student s
            join Cohort c on s.CohortId = c.Id
            order by s.CohortId
            """)

            all_students = db_cursor.fetchall()

            print("----------Students with Cohort Name----------")
            [print(s) for s in all_students]
            print("---------------------------------------------")

    def all_cohorts(self):

        """Retrieve all cohorts"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Cohort(row[1])      
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT c.Id,
                c.Name
            FROM Cohort c
            ORDER BY Id
            """)

            all_cohorts = db_cursor.fetchall()

            print("--------------Cohort Name---------------")
            [print(s) for s in all_cohorts]
            print("----------------------------------------")

    def all_exercises(self):

        """Retrieve all exercises"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2]) 
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT e.Id,
                e.Name,
                e.Language
            FROM Exercise e
            ORDER BY Id
            """)

            all_exercises = db_cursor.fetchall()

            print("--------------Exercise Name-------------")
            [print(e) for e in all_exercises]
            print("----------------------------------------")

    def javascript_exercises(self):

        """Retrieve JavaScript exercises"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2]) 
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT e.Id,
                e.Name,
                e.Language
            FROM Exercise e
            WHERE e.Language LIKE "javascript"
            ORDER BY Id
            """)

            javascript_exercises = db_cursor.fetchall()

            print("----------Javascript Exercises----------")
            if len(javascript_exercises) == 0:
                print("There are no Javascript Exercises")
            else:
                [print(s) for s in javascript_exercises]
            print("----------------------------------------")

    def python_exercises(self):

        """Retrieve Python exercises"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2]) 
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT e.Id,
                e.Name,
                e.Language
            FROM Exercise e
            WHERE e.Language LIKE "python"
            ORDER BY Id
            """)

            python_exercises = db_cursor.fetchall()

            print("-----------Python Exercises-------------")
            [print(s) for s in python_exercises]
            print("----------------------------------------")

    def c_sharp_exercises(self):

        """Retrieve c# exercises"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2]) 
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT e.Id,
                e.Name,
                e.Language
            FROM Exercise e
            WHERE e.Language LIKE "cSharp"
            ORDER BY Id
            """)

            c_sharp_exercises = db_cursor.fetchall()

            print("-------------C# EXERCISES--------------")
            if len(c_sharp_exercises) == 0:
                    print("There are no C# Exercises")
            else:
                [print(s) for s in c_sharp_exercises]
            print("----------------------------------------")

    def all_instructors(self):

        """Retrieve all instructors with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Instructor(row[1], row[2], row[3], row[4], row[6])            
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT i.Id,
                i.First_Name,
                i.Last_Name,
                i.Slack,
                i.Specialty,
                i.CohortId,
                c.Name
            FROM Instructor i
            JOIN Cohort c ON i.CohortId = c.Id
            ORDER BY i.CohortId
            """)

            all_instructors = db_cursor.fetchall()

            print("------------Instructors-----------------")
            [print(s) for s in all_instructors]
            print("----------------------------------------")

    def student_workload(self):

        """Retrieve all students and the exercises they are working on"""

        students = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                SELECT
                    s.Id,
                    s.First_Name,
                    s.Last_Name,
                    e.Id,
                    e.NAME
                FROM Student s
                JOIN Student_Exercises se ON se.StudentId = s.Id
                JOIN Exercise e ON e.Id = se.ExerciseId
            """)                            

            dataset = db_cursor.fetchall()

            for row in dataset:
                student_id = row[0]
                student_name = f'{row[1]} {row[2]}'
                exercise_id = row[3]
                exercise_name = row[4]

                if student_name not in students:
                    students[student_name] = [exercise_name]
                else:
                    students[student_name].append(exercise_name)

            for student_name, exercises in students.items():
                print(f'\n\n{student_name} is working on:')
                for exercise in exercises:
                    print(f'\t* {exercise}')

    # def assigned_exercises(self):

    #     """Retrieve all exercises assigned by each instructor"""

    #     instructors = dict()

    #     with sqlite3.connect(self.db_path) as conn:
    #         db_cursor = conn.cursor()

    #         db_cursor.execute(""" 
    #             SELECT
    #                 i.Id,
    #                 i.First_Name,
    #                 i.Last_Name,
    #                 e.Id,
    #                 e.NAME
    #             FROM Instructor i
    #             JOIN Student_Exercises se ON se.InstructorId = i.Id
    #             JOIN Exercise e ON e.Id = se.ExerciseId    """)

    #         dataset = db_cursor.fetchall()

    #         for row in dataset:
    #             instructor_id = row[0]
    #             instructor_name = f'{row[1]} {row[2]}'
    #             exercise_id = row[3]
    #             exercise_name = row[4]

    #             if instructor_name not in instructors:
    #                 instructors[instructor_name] = [exercise_name]
    #             else:
    #                 instructors[instructor_name].append(exercise_name)

    #         for instructor_name, exercises in instructors.items():
    #             print(f'\n\n{instructor_name} has assigned:')
    #             for exercise in exercises:                                            
    #                 print(f"\t* {exercise}")

    def popular_exercises(self):

        """Retrieve all exercises and students assigned"""

        exercises = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                SELECT
                    e.Id,
                    e.NAME,
                    s.Id,
                    s.First_Name,
                    s.Last_Name
                FROM Exercise e
                JOIN Student_Exercises se ON se.StudentId = e.Id
                JOIN Student s ON s.Id = se.ExerciseId
            """)                            

            dataset = db_cursor.fetchall()

            for row in dataset:
                student_id = row[2]
                student_name = f'{row[3]} {row[4]}'
                exercise_id = row[0]
                exercise_name = row[1]

                if exercise_name not in exercises:
                    exercises[exercise_name] = [student_name]
                else:
                    exercises[exercise_name].append(student_name)

            for exercise_name, students in exercises.items():
                print(f'\n\n{exercise_name} is being worked on by:')
                for student in students:
                    print(f'\t* {student}')


reports = StudentExerciseReports()
reports.all_cohorts()
reports.all_exercises()
reports.javascript_exercises()
reports.python_exercises()
reports.c_sharp_exercises()
reports.all_students()
reports.all_instructors()
reports.student_workload()
# reports.assigned_exercises()
reports.popular_exercises()
