# You must define a type for representing an exercise in code. An exercise can be assigned to many students.
"""
Name of exercise
Language of exercise (JavaScript, Python, CSharp, etc.)
"""

class Exercise():
    def __init__(self, name, language):
        self.name = name
        self.language = language
        