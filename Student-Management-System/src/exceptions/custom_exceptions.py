"""Custom exceptions for the Student Management System."""


class StudentManagementError(Exception):
    """Base class for every error raised by this project."""


class ValidationError(StudentManagementError):
    """Raised when user input (name, email, age, ...) is invalid."""


class InvalidGradeError(ValidationError):
    """Raised when a grade is not a number between 0 and 100."""


class StudentNotFoundError(StudentManagementError):
    """Raised when a student ID does not exist."""

    def __init__(self, student_id):
        super().__init__(f"Student with ID '{student_id}' was not found.")
        self.student_id = student_id


class CourseNotFoundError(StudentManagementError):
    """Raised when a course code does not exist."""

    def __init__(self, course_code):
        super().__init__(f"Course with code '{course_code}' was not found.")
        self.course_code = course_code


class InstructorNotFoundError(StudentManagementError):
    """Raised when an instructor ID does not exist."""

    def __init__(self, instructor_id):
        super().__init__(f"Instructor with ID '{instructor_id}' was not found.")
        self.instructor_id = instructor_id


class DuplicateEntryError(StudentManagementError):
    """Raised when adding something that already exists (e.g. same course code)."""


class EnrollmentError(StudentManagementError):
    """Raised for enrollment problems (already enrolled, not enrolled, ...)."""
