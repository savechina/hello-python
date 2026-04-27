import unittest
from hello_python.basic import loops_sample


class TestLoopsSample(unittest.TestCase):
    def test_for_loop(self):
        """Verifies for_loop_sample prints expected output."""
        loops_sample.for_loop_sample()

    def test_while_loop(self):
        """Verifies while_loop_sample prints expected output."""
        loops_sample.while_loop_sample()

    def test_enumerate_zip(self):
        """Verifies enumerate_zip_sample prints expected output."""
        loops_sample.enumerate_zip_sample()


if __name__ == "__main__":
    unittest.main()
