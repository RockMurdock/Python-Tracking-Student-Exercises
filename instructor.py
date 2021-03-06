# You must define a type for representing an instructor in code.
"""
First name
Last name
Slack handle
The instructor's cohort
The instructor's specialty (e.g. dad jokes, excitement, dancing, etc.)
A method to assign an exercise to a student
"""

# from person import Person

# class Instructor(Person):
#     def __init__(self, first, last, slack, specialty):
#         super().__init__(first, last, slack)
#         # self.first = first
#         # self.last = last
#         # self.slack = slack
#         self.cohort = ""
#         self.specialty = specialty

#     def assign_exercise(self, exercise, student):
#         student.exercises.append(exercise)

class Instructor():

    def __init__(self, first, last, slack, specialty, cohort):
        self.first_name = first
        self.last_name = last
        self.slack = slack
        self.specialty = specialty
        self.cohort = cohort

    def __repr__(self):
        return (f'{self.first_name} {self.last_name} teaches {self.cohort}') 
        