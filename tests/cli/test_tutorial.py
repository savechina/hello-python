import unittest
from click.testing import CliRunner
from hello_python.cli.commands.tutorial import basic, advance


class TestTutorialSample(unittest.TestCase):
    def test_basic_list_topics(self):
        runner = CliRunner()
        result = runner.invoke(basic)
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Basic Topics", result.output)

    def test_basic_run_topic(self):
        runner = CliRunner()
        result = runner.invoke(basic, ["expression"])
        self.assertIn("c result:3", result.output)

    def test_basic_nonexistent_topic(self):
        runner = CliRunner()
        result = runner.invoke(basic, ["nonexistent"])
        self.assertIn("not found", result.output)
        self.assertIn("Basic Topics", result.output)

    def test_advance_list_topics(self):
        runner = CliRunner()
        result = runner.invoke(advance)
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Advance Topics", result.output)


if __name__ == "__main__":
    unittest.main()
