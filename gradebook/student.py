"""Gradebook program, using OOP to obtain student grades."""
from classroom import Classroom


class Student(object):
    """Information about each student."""

    def __init__(self, name, ID, classroom):
        """Initialize student with name and ID."""
        self.name = name
        self.ID = ID
        self.assignments = {}
        Classroom.roster += {self.name, self.id}

    def add_assignment(self, assignment_name, score):
        """Add assignment to assignments dictionary with name and score."""
        self.assignments[assignment_name] = score
        # line below is how to access the score
        # print(self.assignments[assignment_name])

    def update_assignment(self, assignment_name, new_score):
        """Update assignment from assignments dictionary with new score."""
        self.assignments[assignment_name] = new_score
        # print(self.assignments[assignment_name])

    def get_assignment_score(self, assignment_name):
        """Get score from assignments dictionary by assignment_name."""
        score = self.assignments.get(assignment_name)
        return score

    def remove_assignment(self, assignment_name):
        """Delete assignment from dictionary by assignment_name."""
        del(self.assignments[assignment_name])

    def get_gpa(self, assignments):
        """Iterate thru assignment dictionary, collect count of assignments."""
        """Add total of all the scores, divide score total by total count."""
        value_sum = 0
        count = 0
        for assignment in assignments.items():
            score = assignment[1]
            value_sum += score
            count += 1
        gpa = value_sum / count
        return gpa
