# Function to determine the grade based on marks
def assign_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    elif marks >= 50:
        return "E"
    else:
        return "F"


# Read marks from the user
try:
    marks = float(input("Enter the student's marks: "))
    if marks < 0 or marks > 100:
        print("Please enter a valid mark between 0 and 100.")
    else:
        grade = assign_grade(marks)
        print(f"The student's grade is: {grade}")
except ValueError:
    print("Invalid input. Please enter a numeric value.")
