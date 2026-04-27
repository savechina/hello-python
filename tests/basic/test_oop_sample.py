import unittest
from hello_python.basic import oop_sample


class TestOOPSample(unittest.TestCase):
    def test_class_definition(self):
        """Verifies basic class creation."""
        oop_sample.class_definition_sample()

    def test_inheritance(self):
        """Verifies inheritance and method override."""
        oop_sample.inheritance_sample()

    def test_dunder_methods(self):
        """Verifies __str__ and __repr__."""
        oop_sample.dunder_methods_sample()


if __name__ == "__main__":
    unittest.main()
