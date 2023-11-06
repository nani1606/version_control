import unittest
from teacher import Teacher

class TestTeacher(unittest.TestCase):
    def test_teach(self):
        teacher = Teacher("Charlie", 35, "Math")
        self.assertEqual(teacher.teach(), "Charlie is teaching Math.")

if __name__ == "__main":
    unittest.main()