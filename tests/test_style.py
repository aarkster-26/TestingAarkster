import unittest

from backend.greeter import greet


class TestGreetStyle(unittest.TestCase):
    def test_default_is_casual(self):
        self.assertEqual(greet("Ada"), "Hello, Ada!")

    def test_casual(self):
        self.assertEqual(greet("Ada", style="casual"), "Hello, Ada!")

    def test_formal(self):
        self.assertEqual(greet("Ada", style="formal"), "Good day, Ada.")

    def test_unsupported_style(self):
        for style in ("pirate", "", None, "Formal"):
            with self.assertRaises(ValueError):
                greet("Ada", style=style)

    def test_name_still_validated(self):
        with self.assertRaises(ValueError):
            greet("", style="formal")


if __name__ == "__main__":
    unittest.main()
