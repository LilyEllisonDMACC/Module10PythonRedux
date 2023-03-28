"""
Program: TestStudent.py
Author: Lily Ellison
Last date modified: 03/28/2023

The purpose of this program is to test a student class, Student.py.

"""

import unittest
from Module10 import Student as s


class StudentTestCase(unittest.TestCase):
    def setUp(self):
        self.student = s('Smith', 'Joe', 'Life')

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Smith')
        self.assertEqual(self.student.first_name, 'Joe')
        self.assertEqual(self.student.major, 'Life')

    def test_object_created_all_attributes(self):
        student = s('Smith', 'Joe', 'Life', 3.5)
        assert student.last_name == 'Smith'
        assert student.first_name == 'Joe'
        assert student.major == 'Life'
        assert student.gpa == 3.5

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            p = s('123', 'Daisy', 'Film')

    def test_object_not_created_error_fist_name(self):
        with self.assertRaises(ValueError):
            p = s('Duck', '123', 'Film')

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            p = s('Duck', 'Daisy', '123')

    def test_object_not_created_error_gpa_letter(self):
        with self.assertRaises(ValueError):
            p = s('Duck', 'Daisy', 'Film', 'A')

    def test_object_not_created_error_gpa_too_high(self):
        with self.assertRaises(ValueError):
            p = s('Duck', 'Daisy', 'Film', 4.1)

    def test_object_not_created_error_gpa_too_low(self):
        with self.assertRaises(ValueError):
            p = s('Duck', 'Daisy', 'Film', -1)
    def test_student_str(self):
        self.assertEqual(str(self.student), "Smith, Joe has major Life with GPA: 0.0")  # Uses person from setUp()

if __name__ == '__main__':
    unittest.main()
