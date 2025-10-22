# Test_last_Development
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from student_grader import add_student, students, calculate_average, grade_letter, display_report,get_all_students


#--- clear students before each test ---
@pytest.fixture(autouse=True)
def clear_students():
    students.clear()


# --- Test add_student function ---
def test_add_student():
    students.clear()
    add_student("Josephine", [85, 90, 78])
    assert "Josephine" in students
    assert students["Josephine"] == [85, 90, 78]


def test_add_many_students():
    add_student("Alice", [92, 88, 95])
    add_student("Bob", [70, 75, 80])
    assert "Alice" in students
    assert "Bob" in students
    assert students["Alice"] == [92, 88, 95]
    assert students["Bob"] == [70, 75, 80]


# --- Test get_all_students function ---
def test_get_all_students():
    add_student("Charlie", [60, 65, 70])
    assert get_all_students() == {"Charlie": [60, 65, 70]}  

    
# --- test average calculation ---
def test_calculate_average():
    add_student("David", [80, 90, 100])
    avg = calculate_average(students["David"])
    assert avg == 90.0      


def test_calculate_average_single_score():
    add_student("Eva", [75])
    avg = calculate_average(students["Eva"])
    assert avg == 75.0
     

def test_calculate_average_empty():
    avg = calculate_average([])
    assert avg == 0.0


def test_grade_letter():
    assert grade_letter(95) == 'A'
    assert grade_letter(85) == 'B'
    assert grade_letter(75) == 'C'
    assert grade_letter(65) == 'D'
    assert grade_letter(50) == 'F'


def test_display_report(capsys):
    add_student("Diana", [95, 85, 90])
    add_student("Ethan", [70, 75, 80])
    display_report()
    captured = capsys.readouterr()
    assert "Diana" in captured.out
    assert "Ethan" in captured.out
    assert "90.00" in captured.out  
    assert "A" in captured.out  
    assert "75.00" in captured.out  
    assert "C" in captured.out
    
