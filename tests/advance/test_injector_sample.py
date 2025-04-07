"""
datatype sample test
"""

import unittest
from hello_python.advance import injector_sample


class TestInjectorSample(unittest.TestCase):
    """
    TestInjectorSample
    """

    def test_injector_greet_sample(self):
        """
        test object injector sample
        """
        injector_sample.inject_main()
