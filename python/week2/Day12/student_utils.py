"""
student_utils.py
A module containing helper functions to process student grades.
"""

def calculate_total(grades_list):
    """Calculates and returns the sum of a list of grades."""
    return sum(grades_list)

def calculate_average(grades_list):
    """Calculates and returns the average of a list of grades."""
    if not grades_list:
        return 0.0
    return sum(grades_list) / len(grades_list)

def calculate_grade(average):
    """Returns a letter grade based on the average score."""
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'