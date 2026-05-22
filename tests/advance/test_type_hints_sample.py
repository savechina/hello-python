import unittest
from io import StringIO
import sys
from hello_python.advance import type_hints_sample


class TestTypeHintsSample(unittest.TestCase):
    def test_basic_annotations(self):
        captured = StringIO()
        sys.stdout = captured
        type_hints_sample.basic_annotations_sample()
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        self.assertIn("Alice is 30 years old", output)
        self.assertIn("Average: 2.0", output)
        self.assertIn("User 3: None", output)

    def test_union_type(self):
        captured = StringIO()
        sys.stdout = captured
        type_hints_sample.union_type_sample()
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        self.assertIn("String: HELLO", output)
        self.assertIn("Number: 84", output)
        self.assertIn("Top student:", output)

    def test_typed_dict(self):
        captured = StringIO()
        sys.stdout = captured
        type_hints_sample.typed_dict_sample()
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        self.assertIn("Alice (30) - alice@example.com", output)


if __name__ == "__main__":
    unittest.main()
