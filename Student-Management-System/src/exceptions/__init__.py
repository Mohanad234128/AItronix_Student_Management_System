"""Custom exceptions of the Student Management System."""

from .custom_exceptions import (
    CourseNotFoundError,
    DuplicateEntryError,
    EnrollmentError,
    InstructorNotFoundError,
    InvalidGradeError,
    StudentManagementError,
    StudentNotFoundError,
    ValidationError,
)

__all__ = [
    "StudentManagementError", "ValidationError", "InvalidGradeError",
    "StudentNotFoundError", "CourseNotFoundError", "InstructorNotFoundError",
    "DuplicateEntryError", "EnrollmentError",
]
