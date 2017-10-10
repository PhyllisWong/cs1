from student import Student
import pytest


def setup_for_test():
    '''Test to make sure the new student test works.'''
    student = Student('Bob Jones', 1)
    # student.add_assignment('hw1', 100)
    # student.add_assignment('quiz1', 70)
    # student.update_assignment('quiz1', 100)
    return student


def setup_student_with_assignements():
    student = setup_for_test()
    student.assignments = {'hw1': 100, 'quiz1': 70, 'final_exam': 70}
    return student


def test_new_student():
    '''Test creating a new student with name and ID.'''
    student = setup_for_test()
    assert student.name == 'Bob Jones'
    assert student.ID == 1


def test_add_assignment():
    '''Test to see if the new assignment has a string name and an int score.'''
    student = setup_for_test()
    student.add_assignment('hw2', 80)
    assert student.assignments['hw2'] == 80


def test_update_assignment():
    '''Test to check that the update assignment function works.'''
    student = setup_student_with_assignements()
    student.update_assignment('quiz1', 100)
    assert student.assignments['quiz1'] == 100


def test_read_assignment_score():
    student = setup_student_with_assignements()
    student.get_assignment_score('quiz1')
    assert student.get_assignment_score('quiz1') == 70


def test_remove_assignment():
    """Test that an assignment was removed."""
    student = setup_student_with_assignements()
    student.remove_assignment('quiz1')
    assert student.assignments == {'hw1': 100, 'final_exam': 70}


def test_get_gpa():
    student = setup_student_with_assignements()
    student.get_gpa(student.assignments)
    print(student.assignments)
    assert student.get_gpa(student.assignments) == 80.0
