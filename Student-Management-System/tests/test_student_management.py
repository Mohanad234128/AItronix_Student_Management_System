"""Simple automated tests. Run with:  python -m unittest discover -s tests -v"""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from exceptions import (
    CourseNotFoundError, DuplicateEntryError, EnrollmentError,
    InvalidGradeError, StudentNotFoundError, ValidationError,
)
from models import Instructor, Person, Student
from services import StudentManagementSystem


class TestStudentManagementSystem(unittest.TestCase):
    def setUp(self):
        self.sms = StudentManagementSystem()
        self.s1 = self.sms.add_student("Ahmed Ali", "ahmed@example.com", 20, "CS")
        self.sms.add_course("cs101", "Intro", 3)
        self.sms.add_course("CS201", "OOP", 4)

    def test_add_search_remove(self):
        self.assertEqual(self.s1.person_id, "S001")
        self.assertEqual(len(self.sms.search_students("ahm")), 1)
        self.sms.remove_student("S001")
        with self.assertRaises(StudentNotFoundError):
            self.sms.get_student("S001")

    def test_validation(self):
        with self.assertRaises(ValidationError):
            self.sms.add_student("", "a@b.com", 20)
        with self.assertRaises(ValidationError):
            self.sms.add_student("Bob", "bad-email", 20)
        with self.assertRaises(ValidationError):
            self.sms.add_student("Bob", "bob@b.com", "abc")
        with self.assertRaises(DuplicateEntryError):
            self.sms.add_student("Other", "ahmed@example.com", 22)

    def test_update_rolls_back_on_error(self):
        with self.assertRaises(ValidationError):
            self.sms.update_student("S001", name="New Name", age=5)
        self.assertEqual(self.s1.name, "Ahmed Ali")
        self.sms.update_student("S001", major="Math")
        self.assertEqual(self.s1.major, "Math")

    def test_enroll_and_grades(self):
        self.sms.enroll_student("S001", "CS101")
        self.sms.enroll_student("S001", "CS201")
        with self.assertRaises(EnrollmentError):
            self.sms.enroll_student("S001", "CS101")
        with self.assertRaises(CourseNotFoundError):
            self.sms.enroll_student("S001", "NOPE")
        self.sms.set_grade("S001", "CS101", 90)
        self.sms.set_grade("S001", "CS201", 80)
        self.assertAlmostEqual(self.s1.average_grade(), 85.0)
        self.assertAlmostEqual(self.s1.gpa(), 3.5)
        with self.assertRaises(InvalidGradeError):
            self.sms.set_grade("S001", "CS101", 101)

    def test_grade_needs_enrollment(self):
        with self.assertRaises(EnrollmentError):
            self.sms.set_grade("S001", "CS101", 80)

    def test_remove_student_cleans_course(self):
        self.sms.enroll_student("S001", "CS101")
        self.sms.remove_student("S001")
        self.assertEqual(self.sms.get_course("CS101").student_ids, [])

    def test_encapsulation_returns_copies(self):
        self.sms.enroll_student("S001", "CS101")
        self.s1.grades["CS101"] = 100  # changes only a copy
        self.assertIsNone(self.s1.grades["CS101"])
        with self.assertRaises(AttributeError):
            self.s1.person_id = "X"  # read-only property

    def test_abstraction_inheritance_polymorphism(self):
        with self.assertRaises(TypeError):
            Person("X", "N", "n@n.com", 30)
        teacher = self.sms.add_instructor("Omar Khaled", "o@x.com", 45, "CS")
        self.assertIsInstance(teacher, Person)
        self.assertTrue(issubclass(Student, Person))
        roles = [p.get_role() for p in self.sms.get_all_people()]
        self.assertEqual(roles, ["Student", "Instructor"])

    def test_assign_instructor(self):
        self.sms.add_instructor("Omar Khaled", "o@x.com", 45, "CS")
        self.sms.assign_instructor("I001", "CS201")
        self.assertEqual(self.sms.get_course("CS201").instructor_id, "I001")
        self.assertIsInstance(self.sms.get_instructor("I001"), Instructor)


if __name__ == "__main__":
    unittest.main()
