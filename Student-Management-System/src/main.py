"""Console menu for the Student Management System.

Run from the project folder with:  python src/main.py
"""

from exceptions import StudentManagementError
from models import Person
from services import StudentManagementSystem

MENU = """
========== STUDENT MANAGEMENT SYSTEM ==========
 1. Add student              9. Display a student's courses
 2. Remove student          10. Add / update a grade
 3. Search for a student    11. Show GPA / average grade
 4. Display all students    12. Add instructor
 5. Update student          13. Assign instructor to course
 6. Add course              14. Demo: inheritance & polymorphism
 7. Display all courses     15. Load sample data
 8. Enroll student in course
 0. Exit
===============================================
"""


def ask(prompt):
    """Read one line of input and remove extra spaces."""
    return input(prompt).strip()


# ----------------------------- menu actions -----------------------------
def add_student(sms):
    student = sms.add_student(
        ask("Name: "), ask("Email: "), ask("Age: "),
        ask("Major (Enter = Undeclared): ") or "Undeclared",
    )
    print(f"Student added with ID {student.person_id}.")


def remove_student(sms):
    student = sms.remove_student(ask("Student ID to remove: "))
    print(f"Removed {student.name}.")


def search_student(sms):
    results = sms.search_students(ask("Enter student ID or part of the name: "))
    if not results:
        print("No matching students.")
    for student in results:
        print(student)


def display_students(sms):
    students = sms.get_all_students()
    if not students:
        print("No students yet.")
    for student in students:
        print(student)


def update_student(sms):
    student = sms.get_student(ask("Student ID to update: "))
    print(f"Current data: {student}")
    print("Press Enter to keep the current value.")
    sms.update_student(
        student.person_id,
        name=ask("New name: ") or None,
        email=ask("New email: ") or None,
        age=ask("New age: ") or None,
        major=ask("New major: ") or None,
    )
    print("Student updated.")


def add_course(sms):
    course = sms.add_course(
        ask("Course code (e.g. CS101): "), ask("Course title: "),
        ask("Credits (Enter = 3): ") or 3,
    )
    print(f"Course added: {course}")


def display_courses(sms):
    courses = sms.get_all_courses()
    if not courses:
        print("No courses yet.")
    for course in courses:
        print(course)


def enroll_student(sms):
    sms.enroll_student(ask("Student ID: "), ask("Course code: "))
    print("Enrollment successful.")


def display_student_courses(sms):
    student = sms.get_student(ask("Student ID: "))
    rows = sms.get_student_courses(student.person_id)
    print(f"Courses of {student.name}:")
    if not rows:
        print("  (not enrolled in any course)")
    for course, grade in rows:
        shown = "no grade yet" if grade is None else f"grade {grade:.1f}"
        print(f"  {course.code} - {course.title} ({shown})")


def set_grade(sms):
    sms.set_grade(ask("Student ID: "), ask("Course code: "), ask("Grade (0-100): "))
    print("Grade saved.")


def show_gpa(sms):
    student = sms.get_student(ask("Student ID: "))
    average, gpa = student.average_grade(), student.gpa()
    if average is None:
        print(f"{student.name} has no grades yet.")
    else:
        print(f"{student.name}: average = {average:.2f}, GPA = {gpa:.2f} / 4.0")


def add_instructor(sms):
    instructor = sms.add_instructor(
        ask("Name: "), ask("Email: "), ask("Age: "), ask("Department: ")
    )
    print(f"Instructor added with ID {instructor.person_id}.")


def assign_instructor(sms):
    sms.assign_instructor(ask("Instructor ID: "), ask("Course code: "))
    print("Instructor assigned.")


def demo_oop(sms):
    """Shows inheritance, abstraction and polymorphism with real objects."""
    print("\n--- Inheritance ---")
    print("Student method resolution order:",
          " -> ".join(c.__name__ for c in type(sms.get_all_students()[0]).__mro__)
          if sms.get_all_students() else "(add a student first)")

    print("\n--- Abstraction ---")
    try:
        Person("X1", "Nobody", "no@body.com", 30)
    except TypeError as error:
        print("Cannot create a Person directly:", error)

    print("\n--- Polymorphism (same call, different behaviour) ---")
    people = sms.get_all_people()
    if not people:
        print("No people yet. Add students/instructors or load sample data.")
    for person in people:
        print(person.introduce())  # Student and Instructor answer differently
    print(f"\nTotal Person objects created so far: {Person.total_people_created}")


def load_sample_data(sms):
    """Adds a few ready-made records so the program can be tried quickly."""
    ahmed = sms.add_student("Ahmed Ali", "ahmed@example.com", 20, "Computer Science")
    sara = sms.add_student("Sara Hassan", "sara@example.com", 19, "Software Engineering")
    sms.add_instructor("Dr. Omar Khaled", "omar@example.com", 45, "Computer Science")
    sms.add_course("CS101", "Intro to Programming", 3)
    sms.add_course("CS201", "Object-Oriented Programming", 4)
    sms.assign_instructor("I001", "CS201")
    sms.enroll_student(ahmed.person_id, "CS101")
    sms.enroll_student(ahmed.person_id, "CS201")
    sms.enroll_student(sara.person_id, "CS201")
    sms.set_grade(ahmed.person_id, "CS101", 92)
    sms.set_grade(ahmed.person_id, "CS201", 85)
    sms.set_grade(sara.person_id, "CS201", 78)
    print("Sample data loaded (students S001-S002, instructor I001, courses CS101, CS201).")


ACTIONS = {
    "1": add_student, "2": remove_student, "3": search_student,
    "4": display_students, "5": update_student, "6": add_course,
    "7": display_courses, "8": enroll_student, "9": display_student_courses,
    "10": set_grade, "11": show_gpa, "12": add_instructor,
    "13": assign_instructor, "14": demo_oop, "15": load_sample_data,
}


def main():
    sms = StudentManagementSystem()
    while True:
        print(MENU)
        try:
            choice = ask("Choose an option: ")
        except EOFError:  # input stream ended (e.g. piped input)
            break
        if choice == "0":
            break
        action = ACTIONS.get(choice)
        if action is None:
            print("Invalid option. Please choose a number from the menu.")
            continue
        try:
            action(sms)
        except StudentManagementError as error:  # our own custom errors
            print(f"Error: {error}")
        except EOFError:
            break
    print("Goodbye!")


if __name__ == "__main__":
    main()
