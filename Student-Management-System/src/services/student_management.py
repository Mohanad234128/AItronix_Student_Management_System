"""StudentManagementSystem: the class that manages students, instructors and courses."""

from exceptions import (
    CourseNotFoundError,
    DuplicateEntryError,
    InstructorNotFoundError,
    StudentNotFoundError,
    ValidationError,
)
from models import Course, Instructor, Student


class StudentManagementSystem:
    """Keeps all data in memory and offers the main operations."""

    def __init__(self):
        self._students = {}
        self._instructors = {}
        self._courses = {}
        self._next_student_number = 1
        self._next_instructor_number = 1

    # ------------------------------ students ------------------------------
    def add_student(self, name, email, age, major="Undeclared"):
        self._ensure_email_unique(email)
        student_id = f"S{self._next_student_number:03d}"
        student = Student(student_id, name, email, age, major)  # validates input
        self._next_student_number += 1
        self._students[student_id] = student
        return student

    def get_student(self, student_id):
        student = self._students.get(str(student_id).strip().upper())
        if student is None:
            raise StudentNotFoundError(student_id)
        return student

    def remove_student(self, student_id):
        student = self.get_student(student_id)
        for code in student.course_codes:  # keep courses consistent
            self._courses[code].remove_student(student.person_id)
        del self._students[student.person_id]
        return student

    def search_students(self, keyword):
        """Find students by ID or part of the name (case-insensitive)."""
        keyword = str(keyword).strip().lower()
        if not keyword:
            raise ValidationError("Search text must not be empty.")
        return [
            s for s in self._students.values()
            if keyword == s.person_id.lower() or keyword in s.name.lower()
        ]

    def update_student(self, student_id, name=None, email=None, age=None, major=None):
        """Update only the fields that are not None."""
        student = self.get_student(student_id)
        if email is not None and email.strip().lower() != student.email.lower():
            self._ensure_email_unique(email)
        old = (student.name, student.email, student.age, student.major)
        try:  # apply the changes; undo everything if one value is invalid
            if name:
                student.name = name
            if email:
                student.email = email
            if age:
                student.age = age
            if major:
                student.major = major
        except ValidationError:
            student.name, student.email, student.age, student.major = old
            raise
        return student

    def get_all_students(self):
        return sorted(self._students.values(), key=lambda s: s.person_id)

    def _ensure_email_unique(self, email):
        email = str(email).strip().lower()
        for person in list(self._students.values()) + list(self._instructors.values()):
            if person.email.lower() == email:
                raise DuplicateEntryError(f"The email '{email}' is already used.")

    # ----------------------------- instructors -----------------------------
    def add_instructor(self, name, email, age, department):
        self._ensure_email_unique(email)
        instructor_id = f"I{self._next_instructor_number:03d}"
        instructor = Instructor(instructor_id, name, email, age, department)
        self._next_instructor_number += 1
        self._instructors[instructor_id] = instructor
        return instructor

    def get_instructor(self, instructor_id):
        instructor = self._instructors.get(str(instructor_id).strip().upper())
        if instructor is None:
            raise InstructorNotFoundError(instructor_id)
        return instructor

    def get_all_instructors(self):
        return sorted(self._instructors.values(), key=lambda i: i.person_id)

    # ------------------------------- courses -------------------------------
    def add_course(self, code, title, credits=3):
        course = Course(code, title, credits)
        if course.code in self._courses:
            raise DuplicateEntryError(f"Course '{course.code}' already exists.")
        self._courses[course.code] = course
        return course

    def get_course(self, code):
        course = self._courses.get(str(code).strip().upper())
        if course is None:
            raise CourseNotFoundError(code)
        return course

    def get_all_courses(self):
        return sorted(self._courses.values(), key=lambda c: c.code)

    def enroll_student(self, student_id, course_code):
        student = self.get_student(student_id)
        course = self.get_course(course_code)
        student.enroll(course.code)          # raises if already enrolled
        course.add_student(student.person_id)

    def assign_instructor(self, instructor_id, course_code):
        instructor = self.get_instructor(instructor_id)
        course = self.get_course(course_code)
        instructor.assign_course(course.code)
        course.assign_instructor(instructor.person_id)

    def get_student_courses(self, student_id):
        """Return a list of (Course, grade) for one student."""
        student = self.get_student(student_id)
        grades = student.grades
        return [(self._courses[code], grades[code]) for code in student.course_codes]

    def set_grade(self, student_id, course_code, grade):
        student = self.get_student(student_id)
        course = self.get_course(course_code)
        student.set_grade(course.code, grade)

    # ----------------------------- polymorphism ----------------------------
    def get_all_people(self):
        """Students and instructors together, as a list of Person objects."""
        return self.get_all_students() + self.get_all_instructors()
