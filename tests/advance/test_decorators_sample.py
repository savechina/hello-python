import unittest
from io import StringIO
import sys
from hello_python.advance import decorators_sample


class TestDecoratorsSample(unittest.TestCase):
    def test_basic_decorator(self):
        captured = StringIO()
        sys.stdout = captured
        decorators_sample.basic_decorator_sample()
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        self.assertIn("Calling add", output)
        self.assertIn("add returned", output)
        self.assertIn("Calling greet", output)

    def test_decorator_with_args(self):
        captured = StringIO()
        sys.stdout = captured
        decorators_sample.decorator_with_args_sample()
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        self.assertIn("Iteration 1", output)
        self.assertIn("Iteration 2", output)
        self.assertIn("Iteration 3", output)

    def test_wraps_preserves_metadata(self):
        captured = StringIO()
        sys.stdout = captured
        decorators_sample.wraps_sample()
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        self.assertIn("compute(100000)", output)
        self.assertIn("Function name preserved: compute", output)
        self.assertIn("Docstring preserved:", output)


if __name__ == "__main__":
    unittest.main()
