"""Copyright 2016 Anna Eilering."""

from contextlib import contextmanager
from StringIO import StringIO
import unittest
import sys

from jenkins_report_builder import utils


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


class PrintHeaderTest(unittest.TestCase):
    """Tests to confirm print_header function works as expected."""

    def test_front_buffer_if_set_true(self):
        """Check if the buffer is set to true there is newline at front."""
        with captured_output() as (out, err):
            print utils.PPHeader(header='fake', buffer=True)
        output = out.getvalue().split('\n')
        self.assertTrue(output[0] == ' ')

    def test_rear_buffer_if_set_true(self):
        """Check if the buffer is set to true there is newline at rear."""
        with captured_output() as (out, err):
            print utils.PPHeader(header='fake', buffer=True)
        output = out.getvalue().split('\n')

        # Checking pos -2 because capturing from stdout results in an extra
        # line
        self.assertTrue(output[-2] == ' ')

    def test_PPHeader_header_list_if_buffer_set(self):
        """Check that the headers list is as expected if buffer is True."""
        h = utils.PPHeader(header='fake', buffer=True).header_list
        self.assertTrue(len(h) == 5)

    def test_front_buffer_if_set_false(self):
        """Check if the buffer is set to false there is no newline at front."""
        with captured_output() as (out, err):
            print utils.PPHeader(header='fake', buffer=False)
        output = out.getvalue().split('\n')
        self.assertTrue(output[0] != ' ')

    def test_rear_buffer_if_set_false(self):
        """Check if the buffer is set to false there is no newline at rear."""
        with captured_output() as (out, err):
            print utils.PPHeader(header='fake', buffer=False)
        output = out.getvalue().split('\n')

        # Checking pos -2 because capturing from stdout results in an extra
        # line
        self.assertTrue(output[-2] != ' ')

    def test_PPHeader_header_list_if_buffer_not_set(self):
        """Check that the headers list is as expected if buffer is False."""
        h = utils.PPHeader(header='fake', buffer=False).header_list
        self.assertTrue(len(h) == 3)
