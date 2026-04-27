import unittest
from hello_python.basic import list_dict_sample


class TestListDictSample(unittest.TestCase):
    def test_list_comprehension(self):
        """Verifies list comprehension output."""
        list_dict_sample.list_comprehension_sample()

    def test_dict_operations(self):
        """Verifies dict operations output."""
        list_dict_sample.dict_operations_sample()

    def test_set_tuple(self):
        """Verifies set and tuple output."""
        list_dict_sample.set_tuple_sample()


if __name__ == "__main__":
    unittest.main()
