import unittest
from io import StringIO
import sys
from hello_python.advance import dataclasses_sample


class TestDataclassesSample(unittest.TestCase):
    def test_basic_dataclass(self):
        captured = StringIO()
        sys.stdout = captured
        dataclasses_sample.basic_dataclass_sample()
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        self.assertIn("Point:", output)
        self.assertIn("Alice:", output)
        self.assertIn("p == Point(3.0, 4.0): True", output)

    def test_field_and_frozen(self):
        captured = StringIO()
        sys.stdout = captured
        dataclasses_sample.field_and_frozen_sample()
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        self.assertIn("Config: host=localhost, port=8080", output)
        self.assertIn("Python Team", output)

    def test_post_init(self):
        captured = StringIO()
        sys.stdout = captured
        dataclasses_sample.post_init_sample()
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        self.assertIn("area=15.0", output)


if __name__ == "__main__":
    unittest.main()
