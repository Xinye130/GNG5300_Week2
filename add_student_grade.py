# Create an empty dictionary to store students and their grades
student_grades = {}

# Function to add a student and their grade
def add_student(name):
    student_grades[name] = grade

# Function to add a grade to an existing student
def add_grade(name, grade):
    if name in student_grades:
        student_grades[name] = grade
    else:
        print("Student not found.")

# Function to print the grade of a student
def print_grade(name):
    if name in student_grades:
        print(f"The grade of {name} is {student_grades[name]}.")
    else:
        print("Student not found.")

# Example usage
add_student("John")
add_student("Jane")
add_grade("John", 90)

while True:
    action = input("What would you like to do? (add student / add grade / print grade / exit): ")

    if action == "add student":
        name = input("Enter student name: ")
        grade = int(input("Enter student grade: "))
        add_student(name)
    elif action == "add grade":
        name = input("Enter student name: ")
        grade = int(input("Enter student grade: "))
        add_grade(name, grade)
    elif action == "print grade":
        name = input("Enter student name: ")
        print_grade(name)
    elif action == "exit":
        break
    else:
        print("Invalid action. Please try again.")
