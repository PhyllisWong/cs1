from student import Student
"""Initialize classroom with a name, a teacher, and a roster of students."""


class Classroom:
    """Classroom instantiated with name of class and teacher."""

    def __init__(self, name, teacher):
        """Initialize the class with class name and teacher name."""
        self.name = name
        self.teacher = teacher
        self.roster = {}

    def add_student(self, student_name, id):
        """Add assignment to assignments dictionary with name and score."""
        self.roster[student_name] = id

    def get_student_roster(self, roster):
        """Print all students enrolled in class."""
        print(self.roster)

    def add_assignment_to_all():
        """Add assignments to every student."""
        pass

    def remove_assignment_from_all():
        """Remove an assignment from every student."""
        pass
