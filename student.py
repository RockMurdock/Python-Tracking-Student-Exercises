# You must define a custom type for representing a student in code. A student can only be in one 
# cohort at a time. A student can be working on many exercises at a time.
"""
Properties:
First name
Last name
Slack handle
The student's cohort
The collection of exercises that the student is currently working on
"""

from person import Person

class Student(Person):
    def __init__(self, first, last, slack):
        super().__init__(first, last, slack)
        # self.first = first
        # self.last = last
        # self.slack = slack
        self.cohort = ""
        self.exercises = list()