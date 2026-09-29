"""Model classes of the Student Management System."""

from .person import Person
from .student import Student, grade_to_points
from .instructor import Instructor
from .course import Course

__all__ = ["Person", "Student", "Instructor", "Course", "grade_to_points"]
