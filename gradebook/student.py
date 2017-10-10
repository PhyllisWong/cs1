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

    def get_gpa(self, assignments):
        """Iterate thru assignment dictionary, collect count of assignments."""
        """Add total of all the scores, divide score total by total count."""
        value_sum = None
        count = 0
        for key, value in assignments.items():
            value_sum += value
            count += 1
        gpa = value_sum / count
        return gpa
