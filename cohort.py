#  You must define a type for representing a cohort in code.
"""
The cohort's name (Evening Cohort 6, Day Cohort 26, etc.)
The collection of students in the cohort.
The collection of instructors in the cohort.
"""

class Cohort():
    def __init__(self, name):
        self.name = name
        self.students = list()
        self.instructors = list()

    def add_student(self, student):
        self.students.append(student)

    def add_instructor(self, instructor):
        self.instructors.append(instructor)