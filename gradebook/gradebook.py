"""Gradebook program, using OOP to obtain student grades."""


class Classroom:
    """Classroom instantiated with name of class and teacher."""
    def __init__(self, class_name, teacher):
        self.class_name = class_name
        self.teacher = teacher


def get_student_roster():
    """Method to get all students enrolled in class."""
    pass


def get_total_grades_average():
    """Method to claculate the average for the whole class."""
    pass


class Student:
    """Information about each student."""
    def __inti__(self, name):
        self.name = name

    assignments = {}
    # x is placeholder for the weight of each assignment
    assignment[x] = {}
    # id is the student unique id
    # grade is the grade earned on the assignment
    assignment[x][id] = grade

    def create_student_id():
        """Method to assign each student a unique student ID."""
        pass

    def get_student_attendance():
        """Method to store attendance record in student object."""
        pass
