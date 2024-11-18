import unittest

# import coverage

from hello_python.cli import cli
from click.testing import CliRunner
from unittest.mock import patch
import click


class TestCliCase(unittest.TestCase):
    """
    TestCliExample
    """

    @patch("click.echo")
    def test_cli_greet(self, mock_echo):
        """test cli entry"""
        runner = CliRunner()
        result = runner.invoke(cli, ["greet", "Alice"])
        # self.assertEqual(result.return_value, "ok", "not equal message")


if __name__ == "__main__":
    unittest.main()
