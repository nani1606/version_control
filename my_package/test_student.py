import unittest
from student import Student

class TestStudent(unittest.TestCase):
    def test_study(self):
        student = Student("Bob", 20, "S12345")
        self.assertEqual(student.study(), "Bob is studying.")

if __name__ == "__main":
    unittest.main()