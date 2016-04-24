"""Copyright 2016 Anna Eilering."""

import os

from jenkins_report_builder.common import (
    JRB_ROOT_DIR, JRB_LOG_DIR, JRB_CONFIG_DIR)
from jenkins_report_builder.utils import (
    PPHeader, DirectoryUtilities, PPFooter)


class InitializationException(Exception):
    """Custom Exception for reporting JRB configuration issues."""

    def __init__(self, msg, *args, **kwargs):
        """
        Initialization method for Configuration Exceptions.

        :param msg: Mesage desired to output to terminal on exception.
        :type msg: String
        """
        print PPHeader(header="WARNING", buffer=True)
        print "The Jenkins-Report-Builder has not been initialized properly."
        print "Please run 'Jenkins-Report-Builder init'"
        print "{0}{1}".format('\t', msg)
        print PPFooter(buffer=True)
        Exception.__init__(self, msg, *args, **kwargs)


class Initialize(object):
    """Initializatizing the needed files for JRB to run."""

    # TODO - Make this interactive!
    def __init__(self):
        """Initialization method for the Initialize Object."""
        print PPHeader(
            header="INITIALIZING JENKINS REPORT VIEWER",
            buffer=True)

        # Create the .jrb directory in the user's home directory
        DirectoryUtilities.safe_create_dir(JRB_ROOT_DIR)
        DirectoryUtilities.safe_create_dir(JRB_LOG_DIR)
        DirectoryUtilities.safe_create_dir(JRB_CONFIG_DIR)
        print PPFooter(buffer=True)

    @classmethod
    def is_initialized(cls):
        """Check to see if JRB has been properly initialized."""
        # check that the jrb directory is present
        if not os.path.isdir(JRB_ROOT_DIR):
            raise InitializationException(
                msg='{0} directory is not present.'.format(JRB_ROOT_DIR))
        if not os.path.isdir(JRB_LOG_DIR):
            raise InitializationException(
                msg='{0} directory is not present.'.format(JRB_LOG_DIR))
        if not os.path.isdir(JRB_CONFIG_DIR):
            raise InitializationException(
                msg='{0} directory is not present.'.format(JRB_CONFIG_DIR))
