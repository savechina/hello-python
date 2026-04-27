import unittest
from hello_python.basic import string_advanced_sample


class TestStringAdvancedSample(unittest.TestCase):
    def test_re_module(self):
        """Verifies regex operations."""
        string_advanced_sample.re_module_sample()

    def test_string_methods(self):
        """Verifies split/join operations."""
        string_advanced_sample.string_methods_sample()

    def test_fstring_advanced(self):
        """Verifies advanced f-string formatting."""
        string_advanced_sample.fstring_advanced_sample()


if __name__ == "__main__":
    unittest.main()
