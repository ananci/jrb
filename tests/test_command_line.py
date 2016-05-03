"""Copyright 2016 Anna Eilering."""

import unittest

from jenkins_report_builder import command_line


class CommandLineTests(unittest.TestCase):
    """Tests to confirm command_line methods work as expected."""

    def setUp(self):
        """Set up method for command line tests."""
        self.parser = command_line.get_args()

    def test_arg_parser_init(self):
        """Test that passing in init results in the correct command."""
        args = self.parser.parse_args(['init'])
        self.assertEqual(args.command, 'init')

    def test_arg_parser_list(self):
        """Test that passing in list results in the correct command."""
        args = self.parser.parse_args(['list'])
        self.assertEqual(args.command, 'list')

    def test_arg_parser_run_no_req_args(self):
        """Test that passing in run without required commands fails."""
        with self.assertRaises(SystemExit):
            self.parser.parse_args(['view-report'])
