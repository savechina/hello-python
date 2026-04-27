import unittest
from hello_python.basic import exception_sample


class TestExceptionSample(unittest.TestCase):
    def test_try_except_simple(self):
        """Verifies basic try/except output."""
        exception_sample.try_except_simple()

    def test_try_except_finally(self):
        """Verifies try/except/finally output."""
        exception_sample.try_except_finally()

    def test_custom_exception(self):
        """Verifies custom exception output."""
        exception_sample.custom_exception_sample()


if __name__ == "__main__":
    unittest.main()
