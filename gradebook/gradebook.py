"""Gradebook program, using OOP to obtain student grades."""


class Classroom:
    """Classroom instantiated with name of class and teacher."""

    def __init__(self, class_name, teacher):
        """Initialize the class with class name and teacher name."""
        self.class_name = class_name
        self.teacher = teacher


def get_student_roster():
    """Method to get all students enrolled in class."""
    pass


class Student:
    """Information about each student."""

    def __inti__(self, name):
        """Initializing student name."""
        self.name = name

    assignments = {}
    # x is placeholder for the weight of each assignment
    assignments[x] = {}
    # id is the student unique id
    # grade is the grade earned on the assignment
    assignments[x][id] = grade

    def get_total_grades_average():
        """Method to claculate the average for the whole class."""
        pass

    def create_student_id():
        """Method to assign each student a unique student ID."""
        pass

    def get_student_attendance():
        """Method to store attendance record in student object."""
        pass


class Assignment:
    """Information about each assignment"""

    homeworks = []
    quizzes = []
    exams = []

    def __init__(self, assignment_name, assignment_type):
        """Initialize assignment name and the type."""
        self.assignment_name = assignment_name
        self.assignment_type = assignment_type

    # Ask Mike if this would be better as an argument
    def get_assignment_weight(assignment_type):
        """Take in a string argument, returns a float."""
        a = assignment_type
        weight = None
        if a == "homework":
            weight = 0.5
        elif a == "quiz":
            weight = 0.3
        elif a == "homework":
            weight = 0.2
        return weight

    def get_average_of_type(type_arr):
        """Take in array, return an Int."""
        type_sum = None

        for each in type_arr:
            type_sum += each

        quotient = type_sum / len(type_sum)
        return quotient

    def store_assignment():
        """Append the specific array each time an assignment is created."""
        pass
