"""Course: stores course information."""

from exceptions import EnrollmentError, ValidationError


class Course:
    """Stores information about one course."""

    def __init__(self, code, title, credits=3):
        code = str(code).strip().upper()
        title = str(title).strip()
        if not code or " " in code:
            raise ValidationError("Course code must not be empty or contain spaces.")
        if not title:
            raise ValidationError("Course title must not be empty.")
        try:
            credits = int(credits)
        except (TypeError, ValueError):
            raise ValidationError("Credits must be a whole number.")
        if not 1 <= credits <= 6:
            raise ValidationError("Credits must be between 1 and 6.")

        self._code = code
        self._title = title
        self._credits = credits
        self.__student_ids = []      # private
        self._instructor_id = None

    @property
    def code(self):
        return self._code

    @property
    def title(self):
        return self._title

    @property
    def credits(self):
        return self._credits

    @property
    def student_ids(self):
        return list(self.__student_ids)

    @property
    def instructor_id(self):
        return self._instructor_id

    def add_student(self, student_id):
        if student_id in self.__student_ids:
            raise EnrollmentError(f"{student_id} is already in {self._code}.")
        self.__student_ids.append(student_id)

    def remove_student(self, student_id):
        if student_id in self.__student_ids:
            self.__student_ids.remove(student_id)

    def assign_instructor(self, instructor_id):
        self._instructor_id = instructor_id

    def __str__(self):
        teacher = self._instructor_id or "not assigned"
        return (
            f"{self._code} | {self._title} | {self._credits} credits | "
            f"Instructor: {teacher} | Students: {len(self.__student_ids)}"
        )
