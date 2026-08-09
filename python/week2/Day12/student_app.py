"""
student_app.py
Main application demonstrating the use of modules, lists, and dictionaries.
"""

# Import the functions from our custom module
from student_utils import calculate_total, calculate_average, calculate_grade

def main():
    # A dictionary storing student names as keys and a list of their grades as values
    student_data = {
        "Alice": [85, 92, 88, 94],
        "Bob": [70, 65, 78, 72],
        "Charlie": [95, 100, 91, 98],
        "David": [55, 60, 58, 62]
    }
    
    print("--- Student Grade Report ---")
    
    # Iterate through the dictionary items
    for name, grades in student_data.items():
        total = calculate_total(grades)
        average = calculate_average(grades)
        final_grade = calculate_grade(average)
        
        # Display the results formatted nicely
        print(f"\nStudent: {name}")
        print(f"  Grades: {grades}")
        print(f"  Total Score: {total}")
        print(f"  Average Score: {average:.2f}")
        print(f"  Final Grade: {final_grade}")

if __name__ == "__main__":
    main()
