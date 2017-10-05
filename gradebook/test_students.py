from student import Student
import pytest


def setup_for_test():
    '''Test to make sure the new student test works.'''
    student = Student('Egon Lastname', 1)
    return student


def setup_for_assignment_test():
    '''Set up to make sure the test for score validation works.'''
    student = setup_for_test()
    score = student.assignments['hw1'] = 90
    return score


def test_new_student():
    '''Test creating a new student and creating an ID.'''
    student = setup_for_test()
    assert student.name == 'Egon Lastname'
    assert student.ID == 1


def test_add_assignment():
    '''Test to see if the new assignment has a string name and an int score.'''
    student = setup_for_test()
    student.add_assignment('hw1', 100)
    student.add_assignment('quiz1', 70)
    assert student.assignments['hw1'] == 100
    assert student.assignments['quiz1'] == 70


def test_update_assignment():
    '''Test to check that the update assignment function works.'''
    student = setup_for_test()
    student.assignments['quiz1'] = 100
    assert student.assignments['quiz1'] == 100


def test_read_assignment_score():
    student = setup_for_test()
    assert student.assignments != 0


def test_delete_student():

    pass


def test_get_gpa():

    pass
