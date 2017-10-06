"""Gradebook program, using OOP to obtain student grades."""


class Student(object):
    """Information about each student."""

    def __init__(self, name, ID):
        """Initialize student with name and ID."""
        self.name = name
        self.ID = ID
        self.assignments = {}

    def add_assignment(self, assignment_name, score):
        self.assignments[assignment_name] = score
        # line below is how to access the score
        # print(self.assignments[assignment_name])

    def update_assignment(self, assignment_name, new_score):
        self.assignments[assignment_name] = new_score
        # print(self.assignments[assignment_name])

    def get_assignment_score(self, assignment_name):
        score = self.assignments.get(assignment_name)
        return score

# needs a rework, not yet working
    def remove_assignment(self, assignment_name):
        del(self.assignments[assignment_name])

    def calculate_gpa():
        pass

    


bob = Student("Bob Jones", 1)
# should print and empty dictionary
print(bob.assignments)
bob.add_assignment("quiz1", 70)
bob.add_assignment('hw1', 100)
# should print a dictionary with 2 assignments
print(bob.assignments)
# should print score for named assignment
print(bob.get_assignment_score("quiz1"))
# should remove an assignment of this name
bob.update_assignment("quiz1", 90)
# bob.remove_assignment("quiz1")
# should print a dictionary with 1 assignment
print(bob.assignments)
bob.add_assignment('final', 87)
print(bob.assignments)
#
#
# class Assignment:
#     """Information about each assignment"""
#
#     homeworks = []
#     quizzes = []
#     exams = []
#
#     def __init__(self, assignment_name, assignment_type):
#         """Initialize assignment name and the type."""
#         self.assignment_name = assignment_name
#         self.assignment_type = assignment_type
#
#     # Ask Mike if this would be better as an argument
#     def get_assignment_weight(assignment_type):
#         """Take in a string argument, returns a float."""
#         a = assignment_type
#         weight = None
#         if a == "homework":
#             weight = 0.5
#         elif a == "quiz":
#             weight = 0.3
#         elif a == "homework":
#             weight = 0.2
#         return weight
#
#     def get_average_of_type(type_arr):
#         """Take in array, return an Int."""
#         type_sum = None
#
#         for each in type_arr:
#             type_sum += each
#
#         quotient = type_sum / len(type_sum)
#         return quotient
#
#     def store_assignment():
#         """Append the specific array each time an assignment is created."""
#         pass
