import pytest
from grade_students import GradeTracker

# T. для додавання оцінок
def test_add_valid_score():
    tracker = GradeTracker("Yuliia")
    assert tracker.add_score(90) is True
    assert 90 in tracker.grades

def test_add_invalid_score():
    tracker = GradeTracker("Yuliia")
    # Перевіряємо, що занадто висока оцінка не додається
    assert tracker.add_score(150) == "Error: Score must be between 0 and 100"

# Т. для середнього балу
def test_average_calculation():
    tracker = GradeTracker("Yuliia")
    tracker.add_score(80)
    tracker.add_score(100)
    assert tracker.get_average() == 90

def test_average_empty():
    tracker = GradeTracker("Yuliia")
    assert tracker.get_average() == 0

# Т. для перевірки результату
def test_student_passed():
    tracker = GradeTracker("Yuliia")
    tracker.add_score(75)
    assert tracker.check_passing(60) == "Yuliia passed"

def test_student_failed():
    tracker = GradeTracker("Yuliia")
    tracker.add_score(30)
    assert tracker.check_passing(60) == "Yuliia failed"