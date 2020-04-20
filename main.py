"""
Once you have defined all of your custom types, go to main.py, import the 
classes you need, and implement the following logic.

Create 4, or more, exercises.
Create 3, or more, cohorts.
Create 4, or more, students and assign them to one of the cohorts.
Create 3, or more, instructors and assign them to one of the cohorts.
Have each instructor assign 2 exercises to each of the students.
"""

from exercise import Exercise
from cohort import Cohort
from student import Student
from instructor import Instructor

lists = Exercise("Common Types - Lists", "Python")
dictionaries = Exercise("Common Types - Dictionaries", "Python")
tuples = Exercise("Common Types - Tuples", "Pyhton")
sets = Exercise("Common Types - Sets", "Python")

cohort_38 = Cohort("Cohort 38")
cohort_39 = Cohort("Cohort 39")
cohort_40 = Cohort("Cohort 40")

cody = Student("Cody", "Murdock", "RockMurdock")
dustin = Student("Dustin", "Murdock", "DMurdock")
bob = Student("Bob", "Builder", "BBuilder")
dora = Student("Dora", "Explorer", "DoraExplorer")

cohort_38.students.append(cody)
cody.cohort = cohort_38.name
cohort_38.students.append(dustin)
dustin.cohort = cohort_38.name
cohort_39.students.append(bob)
bob.cohort = cohort_39.name
cohort_40.students.append(dora)
dora.cohort = cohort_40.name

andy = Instructor("Andy", "Collins", "AndyCollins", "all-knowing")
bryan = Instructor("Bryan", "Neilson", "BryanNeilson", "high fives")
kristen = Instructor("Kristen", "Norris", "KristenNorris", "to the point answers")

cohort_38.instructors.append(kristen)
kristen.cohort = cohort_38.name
cohort_39.instructors.append(andy)
andy.cohort = cohort_39.name
cohort_40.instructors.append(bryan)
bryan.cohort = cohort_40.name

andy.assign_exercise(lists, bob)
andy.assign_exercise(tuples, bob)
bryan.assign_exercise(lists, dora)
bryan.assign_exercise(tuples, dora)
kristen.assign_exercise(dictionaries, cody)
kristen.assign_exercise(sets, dustin)

students = [cody, dustin, bob, dora]
exercises = [lists, dictionaries, tuples, sets]

for student in students:
    print(f"\n{student.first} {student.last} is working on:")
    for exercise in exercises:
        for studentEx in student.exercises:
            if exercise.name == studentEx.name:
                print(exercise.name)