import unittest
from io import StringIO
import sys
from hello_python.advance import context_managers_sample


class TestContextManagersSample(unittest.TestCase):
    def test_custom_cm(self):
        captured = StringIO()
        sys.stdout = captured
        context_managers_sample.custom_cm_sample()
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        self.assertIn("Elapsed:", output)
        self.assertIn("Sum:", output)

    def test_contextmanager_decorator(self):
        captured = StringIO()
        sys.stdout = captured
        context_managers_sample.contextmanager_decorator_sample()
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        self.assertIn("Opening /tmp/test_cm.txt", output)
        self.assertIn("Content: Hello, Context Manager!", output)
        self.assertIn("Closing /tmp/test_cm.txt", output)

    def test_suppress(self):
        captured = StringIO()
        sys.stdout = captured
        context_managers_sample.suppress_sample()
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        self.assertIn("1", output)
        self.assertIn("3", output)


if __name__ == "__main__":
    unittest.main()
