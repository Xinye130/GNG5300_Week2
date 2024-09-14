class Student:
    def __init__(self, name):
        self.name = name
        self.grade = None

    def add_grade(self, grade):
        self.grade = grade

    def print_grade(self):
        if self.grade is not None:
            print(f"The grade of {self.name} is {self.grade}.")
        else:
            print("Grade not found.")

# Example usage
students = []

john = Student("John")
jane = Student("Jane")

students.append(john)
students.append(jane)

john.add_grade(90)

while True:
    action = input("What would you like to do? (add student / add grade / print grade / exit): ")

    if action == "add student":
        name = input("Enter student name: ")
        student = Student(name)
        students.append(student)
    elif action == "add grade":
        name = input("Enter student name: ")
        grade = int(input("Enter student grade: "))
        for student in students:
            if student.name == name:
                student.add_grade(grade)
                break
        else:
            print("Student not found.")
    elif action == "print grade":
        name = input("Enter student name: ")
        for student in students:
            if student.name == name:
                student.print_grade()
                break
        else:
            print("Student not found.")
    elif action == "exit":
        break
    else:
        print("Invalid action. Please try again.")