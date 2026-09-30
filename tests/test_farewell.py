import unittest

from backend.greeter import farewell, greet


class TestFarewell(unittest.TestCase):
    def test_farewell_by_name(self):
        self.assertEqual(farewell("Ada"), "Goodbye, Ada!")

    def test_farewell_excited(self):
        self.assertEqual(farewell("Ada", excited=True), "GOODBYE, ADA!!")

    def test_farewell_not_excited_explicit(self):
        self.assertEqual(farewell("Ada", excited=False), "Goodbye, Ada!")


class TestGreetExcited(unittest.TestCase):
    def test_greet_default_unchanged(self):
        self.assertEqual(greet("Ada"), "Hello, Ada!")

    def test_greet_excited(self):
        self.assertEqual(greet("Ada", excited=True), "HELLO, ADA!!")


if __name__ == "__main__":
    unittest.main()
