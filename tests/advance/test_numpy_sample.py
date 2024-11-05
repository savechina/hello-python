"""
 datatype sample test
"""

import unittest
from hello_python.advance import numpy_sample


class TestNumpySample(unittest.TestCase):
    """
    TestNumpySample
    """

    def test_numpy_gradient_sample(self):
        """
        test numpy_sample gradient descent
        """

        # Running the gradient descent to minimize the function
        final_x = numpy_sample.gradient_descent(learning_rate=0.1, tolerance=1e-6)
        print(f"Final x after convergence: {final_x:.6f}")
