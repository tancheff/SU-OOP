import unittest
from unittest import TestCase

from project.senior_student import SeniorStudent

class TestSeniorStudent(TestCase):
    def setUp(self):
        self.student = SeniorStudent("1234", "Name", 3.5)

    def test_initialisation(self):
        self.assertEqual(self.student.student_id, '1234')
        self.assertEqual(self.student.name, 'Name')
        self.assertEqual(self.student.student_gpa, 3.5)

    def test_student_id_setter(self):
        self.student.student_id = '4321'
        self.assertEqual('4321', self.student.student_id)

    def test_student_setter_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.student.student_id = '123'

        self.assertEqual("Student ID must be at least 4 digits long!", str(ex.exception))

    def test_student_name_setter(self):
        self.student.name = "NewName"
        self.assertEqual("NewName", self.student.name)

    def test_student_name_setter_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.student.name = ""

        self.assertEqual("Student name cannot be null or empty!", str(ex.exception))

    def test_student_gpa_setter(self):
        self.student.student_gpa = 1.5
        self.assertEqual(1.5, self.student.student_gpa)

    def test_student_gpa_setter_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.student.student_gpa = -1

        self.assertEqual("Student GPA must be more than 1.0!", str(ex.exception))

    def test_apply_to_college_success(self):
        res = self.student.apply_to_college(3, 'unss')
        self.assertEqual('Name successfully applied to unss.', res)

        self.assertEqual('UNSS' in self.student.colleges, True)

    def test_apply_to_college_exception(self):
        res = self.student.apply_to_college(3.5, 'aubg')
        self.assertEqual('Application failed!', res)

        # self.assertEqual('AUBG' in self.student.colleges, False)














if __name__ == '__main__':
    unittest.main()