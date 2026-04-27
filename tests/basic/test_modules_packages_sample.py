import unittest
from hello_python.basic import modules_packages_sample


class TestModulesPackagesSample(unittest.TestCase):
    def test_import_basics(self):
        """Verifies import output."""
        modules_packages_sample.import_basics()

    def test_name_check(self):
        """Verifies __name__ guard output."""
        modules_packages_sample.name_check()


if __name__ == "__main__":
    unittest.main()
