"""Instructor: inherits from Person and teaches courses."""

from exceptions import EnrollmentError, ValidationError
from .person import Person


class Instructor(Person):
    """An instructor who teaches courses."""

    def __init__(self, instructor_id, name, email, age, department):
        super().__init__(instructor_id, name, email, age)
        self.department = department
        self.__course_codes = []  # private

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        value = str(value).strip()
        if not value:
            raise ValidationError("Department must not be empty.")
        self._department = value

    @property
    def course_codes(self):
        return list(self.__course_codes)

    def assign_course(self, course_code):
        if course_code in self.__course_codes:
            raise EnrollmentError(
                f"{self.name} already teaches {course_code}."
            )
        self.__course_codes.append(course_code)

    # ---- polymorphism: same method names, different behaviour ----
    def get_role(self):
        return "Instructor"

    def get_summary(self):
        courses = ", ".join(self.__course_codes) or "no courses yet"
        return (
            f"{self.person_id} | {self.name} | {self.email} | "
            f"Dept: {self.department} | Teaches: {courses}"
        )
