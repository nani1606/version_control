import unittest
from person import Person

class TestPerson(unittest.TestCase):
    def test_greet(self):
        person = Person("Alice", 25)
        self.assertEqual(person.greet(), "Hello, my name is Alice.")

if __name__ == "__main":
    unittest.main()
