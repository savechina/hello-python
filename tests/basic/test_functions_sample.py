import unittest
from hello_python.basic import functions_sample


class TestFunctionsSample(unittest.TestCase):
    def test_def_functions(self):
        """Verifies def_functions_sample prints expected output."""
        functions_sample.def_functions_sample()

    def test_args_kwargs(self):
        """Verifies args_kwargs_sample prints expected output."""
        functions_sample.args_kwargs_sample()

    def test_lambda_scope(self):
        """Verifies lambda_scope_sample prints expected output."""
        functions_sample.lambda_scope_sample()


if __name__ == "__main__":
    unittest.main()
