"""
 sample test
"""

import unittest

# import coverage


class TestSample(unittest.TestCase):
    """
    TestExample
    """

    def test_upper(self):
        """test string upper"""
        self.assertEqual("foo".upper(), "FOO")

    def test_isupper(self):
        """test string isupper"""
        self.assertTrue("FOO".isupper())
        self.assertFalse("Foo".isupper())

    def test_split(self):
        """test string split"""
        s = "hello world"
        self.assertEqual(s.split(), ["hello", "world"])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_addition(self):
        """
        test addition
        """

        print("first test case.")

        self.assertEqual(1 + 1, 2)


if __name__ == "__main__":
    unittest.main()
