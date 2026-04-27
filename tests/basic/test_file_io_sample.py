import unittest
from hello_python.basic import file_io_sample


class TestFileIOSample(unittest.TestCase):
    def test_open_read_write(self):
        """Verifies file open/read/write output."""
        file_io_sample.open_read_write_sample()

    def test_context_manager(self):
        """Verifies context manager output."""
        file_io_sample.context_manager_sample()

    def test_pathlib(self):
        """Verifies pathlib output."""
        file_io_sample.pathlib_sample()


if __name__ == "__main__":
    unittest.main()
