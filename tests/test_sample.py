"""
 sample test
"""

import unittest


class TestExample(unittest.TestCase):
    """
    TestExample
    """

    def test_addition(self):
        """
        test addition
        """

        print("first test case.")

        self.assertEqual(1 + 1, 2)


if __name__ == "__main__":
    unittest.main()
