"""Student: inherits from Person and adds courses and grades."""

from exceptions import EnrollmentError, InvalidGradeError, ValidationError
from .person import Person


def grade_to_points(grade):
    """Convert a 0-100 grade to a 4.0 GPA scale value."""
    if grade >= 90:
        return 4.0
    if grade >= 80:
        return 3.0
    if grade >= 70:
        return 2.0
    if grade >= 60:
        return 1.0
    return 0.0


class Student(Person):
    """A student who can enroll in courses and receive grades."""

    def __init__(self, student_id, name, email, age, major="Undeclared"):
        super().__init__(student_id, name, email, age)  # parent constructor
        self.major = major
        self.__grades = {}  # private: {course_code: grade or None}

    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, value):
        value = str(value).strip()
        if not value:
            raise ValidationError("Major must not be empty.")
        self._major = value

    # ---- courses and grades ----
    @property
    def course_codes(self):
        return list(self.__grades)

    @property
    def grades(self):
        """Return a COPY so outside code cannot change the private dict."""
        return dict(self.__grades)

    def enroll(self, course_code):
        if course_code in self.__grades:
            raise EnrollmentError(
                f"{self.name} is already enrolled in {course_code}."
            )
        self.__grades[course_code] = None

    def drop(self, course_code):
        self.__grades.pop(course_code, None)

    def set_grade(self, course_code, grade):
        if course_code not in self.__grades:
            raise EnrollmentError(
                f"{self.name} is not enrolled in {course_code}."
            )
        try:
            grade = float(grade)
        except (TypeError, ValueError):
            raise InvalidGradeError("Grade must be a number.")
        if not 0 <= grade <= 100:
            raise InvalidGradeError("Grade must be between 0 and 100.")
        self.__grades[course_code] = grade

    def _graded_values(self):
        return [g for g in self.__grades.values() if g is not None]

    def average_grade(self):
        """Average of all graded courses (None if there are no grades)."""
        values = self._graded_values()
        return sum(values) / len(values) if values else None

    def gpa(self):
        """GPA on a 4.0 scale (None if there are no grades)."""
        values = self._graded_values()
        if not values:
            return None
        return sum(grade_to_points(g) for g in values) / len(values)

    # ---- polymorphism: overriding the abstract methods ----
    def get_role(self):
        return "Student"

    def get_summary(self):
        return (
            f"{self.person_id} | {self.name} | {self.email} | "
            f"Age {self.age} | Major: {self.major}"
        )
