from student import Student
from classroom import Classroom
import pytest


def setup_for_test():
    """Test to make sure the new student test works."""
    student = Student('Bob Jones', 1)
    return student


def setup_for_test_classroom():
    """Test to make sure the new classroom test works."""
    classroom = Classroom('Biology 101', 'Teacher Name')
    return classroom


def test_new_classroom():
    """Test creating a new classroom with name and teacher name."""
    bio = setup_for_test_classroom()
    assert bio.name == 'Biology 101'
    assert bio.teacher == 'Teacher Name'


def test_add_student_to_roster():
    """Check if new instance of student is populated to roster."""
    classroom = setup_for_test_classroom()
    assert classroom.roster == {'Bob Jones': 1}
    pass


def test_get_student_roster():
    """Test printing a classroom roster with names and IDs."""
    classroom = setup_for_test_classroom()
    print(classroom)
