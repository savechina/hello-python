"""
datatype sample test
"""

import unittest
from hello_python.basic import datatype_sample


class TestDataTypeSample(unittest.TestCase):
    """
    TestDataTypeSample
    """

    def test_string_sample(self):
        """
        test string sample
        """

        # datatype_sample
        print("string test case.")

        # call string sample
        datatype_sample.string_sample()

        self.assertEqual(1 + 1, 2)


if __name__ == "__main__":
    unittest.main()
