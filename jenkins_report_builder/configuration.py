"""Copyright 2016 Anna Eilering."""

import os

from jenkins_report_builder.common import JRB_ROOT_DIR
from jenkins_report_builder.utils import print_header


class ConfigurationException(Exception):
    """Custom Exception for reporting JRB configuration issues."""

    def __init__(self, msg, *args, **kwargs):
        """
        Initialization method for Configuration Exceptions.

        :param msg: Mesage desired to output to terminal on exception.
        :type msg: String
        """
        print_header(header="WARNING", buffer=True)
        print "The Jenkins-Report-Builder has not been configured properly."
        print "Please run 'Jenkins-Report-Builder --init'"
        print "{0}{1}".format('\t', msg)
        Exception.__init__(self, msg, *args, **kwargs)


class Initialize(object):
    """Initializatizing the needed files for JRB to run."""

    # TODO - Make this interactive!

    def __init__(self):
        """Initialization method for the Initialize Object."""
        print_header(header="INITIALIZING JENKINS REPORT VIEWER", buffer=True)

    @classmethod
    def is_initialized(cls):
        """Check to see if JRB has been properly initialized."""
        # check that the jrb directory is present
        if not os.path.isdir(JRB_ROOT_DIR):
            raise ConfigurationException(
                msg='{0} directory is not present.'.format(JRB_ROOT_DIR))
        # check that there is at least one config file in the JRB Directory
        if not any('.config' in x for x in os.listdir(JRB_ROOT_DIR)):
            raise ConfigurationException(
                msg='No configurations found in {0}'.format(JRB_ROOT_DIR))
