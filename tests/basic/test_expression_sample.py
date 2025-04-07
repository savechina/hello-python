"""
expression sample unittest for basic.expression_sample module
"""

import unittest
from hello_python.basic import datatype_sample, expression_sample


class TestExpressioneSample(unittest.TestCase):
    """
    TestExpressioneSample expression_sample module unit test
    """

    def test_number_calc(self):
        """unittest number_calc"""
        expression_sample.number_calc()


if __name__ == "__main__":
    unittest.main()
