"""Copyright 2016 Anna Eilering."""
from contextlib import contextmanager
from StringIO import StringIO
import sys
import unittest

from jenkins_report_builder import custom_exceptions


@contextmanager
def captured_output():
    """STDOUT context manager for testing prints to terminal."""
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class CustomExceptionTests(unittest.TestCase):
    """Tests to confirm Custom Exceptions work as expected."""

    def test_initialization_exception(self):
        """Confirm that the initialization exception prints what we expect."""
        with captured_output() as (out, err):
            custom_exceptions.InitializationException(msg='fake')
        output = out.getvalue()
        self.assertEqual(
            output,
            (" \n============================================================="
             "===================\n                                     "
             "WARNING\n-------------------------------------------------------"
             "-------------------------\n \n"
             "The Jenkins-Report-Builder has not been initialized properly.\n"
             "Please run 'Jenkins-Report-Builder init'\n"
             "\tfake\n \n"
             "================================================================"
             "================\n \n"))

    def test_configuration_exception(self):
        """Confirm that the configuration exception prints what we expect."""
        with captured_output() as (out, err):
            custom_exceptions.ConfigurationException(msg='fake')
        output = out.getvalue()
        self.assertEqual(
            output,
            (' \n============================================================='
             '===================\n                                     '
             'WARNING\n-------------------------------------------------------'
             '-------------------------\n \n'
             'The Jenkins-Report-Builder has not been configured properly.\n'
             'Please review the README to create appropriate configuration '
             'files.\n'
             '\tfake\n \n'
             '================================================================'
             '================\n \n'))

    def test_safe_configuration_exception(self):
        """Confirm that the safe configuration exception prints."""
        with captured_output() as (out, err):
            custom_exceptions.SafeConfigurationException(msg='fake')
        output = out.getvalue()
        self.assertEqual(
            output,
            (' \n============================================================='
             '===================\n                                     '
             'WARNING\n-------------------------------------------------------'
             '-------------------------\n \n'
             'There was an issue when attempting to manipulate a '
             'configuration file.\nPlease check the location and manually '
             'adjust the configuration as desired.\n'
             '\tfake\n \n'
             '================================================================'
             '================\n \n'))
