import unittest
from io import StringIO
import sys
from hello_python.advance import generators_sample


class TestGeneratorsSample(unittest.TestCase):
    def test_fibonacci(self):
        captured = StringIO()
        sys.stdout = captured
        generators_sample.fibonacci_sample()
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        self.assertIn("0 1 1 2 3 5 8 13 21 34", output)

    def test_generator_expression(self):
        captured = StringIO()
        sys.stdout = captured
        generators_sample.generator_expression_sample()
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        self.assertIn("Generator expression:", output)
        self.assertIn("First: 1", output)
        self.assertIn("Second: 4", output)

    def test_send(self):
        captured = StringIO()
        sys.stdout = captured
        generators_sample.send_sample()
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        self.assertIn("After 5: 5", output)
        self.assertIn("After 10: 15", output)
        self.assertIn("After -3: 12", output)


if __name__ == "__main__":
    unittest.main()
