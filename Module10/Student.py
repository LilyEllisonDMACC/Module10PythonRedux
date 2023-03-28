"""
Program: Student.py
Author: Lily Ellison
Last date modified: 03/28/2023

The purpose of this program is to create a student class with student name (first and last), major, and gpa.
This information is printed to the screen.
To be tested by TestStudent.py

"""

class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'- ")
        if not(name_characters.issuperset(lname) and name_characters.issuperset(fname) and name_characters.issuperset(major)):
            raise ValueError
        if gpa and not isinstance(gpa, float) or gpa > 4.0 or gpa < 0:
            raise ValueError

        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with GPA: " + str(self.gpa)

    def display(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with GPA: " + str(self.gpa)


#Driver
student1 = Student('Smith', 'Joe', 'Stuff', 3.5)
print(student1.display())

student2 = Student('Ketchem', 'Ash', 'Animal Handling', 2.0)
print(student2.display())


'''
Testing Results:

Testing started at 10:42 AM ...
Launching unittests with arguments python -m unittest TestStudent.StudentTestCase in <omitted pathway>

Smith, Joe has major Stuff with GPA: 3.5
Ketchem, Ash has major Animal Handling with GPA: 2.0

Ran 9 tests in 0.005s

OK

Process finished with exit code 0
'''
