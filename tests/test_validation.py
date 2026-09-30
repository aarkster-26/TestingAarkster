import unittest

from backend.greeter import farewell, greet


class TestValidation(unittest.TestCase):
    def test_invalid_names_raise(self):
        for fn in (greet, farewell):
            for bad in (None, 123, 1.5, [], b"x", "", "   ", "\t\n"):
                with self.subTest(fn=fn.__name__, bad=bad):
                    with self.assertRaises(ValueError):
                        fn(bad)

    def test_valid_names_still_work(self):
        self.assertEqual(greet("Ada"), "Hello, Ada!")
        self.assertEqual(farewell("Ada"), "Goodbye, Ada!")


if __name__ == "__main__":
    unittest.main()
