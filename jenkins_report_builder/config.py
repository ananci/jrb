"""Copyright 2016 Anna Eilering."""

from ConfigParser import ConfigParser
import os

from jenkins_report_builder.common import JRB_CONFIG_DIR
from jenkins_report_builder.initialization import Initialize
from jenkins_report_builder import utils


class ConfigException(Exception):
    """Custom Exception for reporting JRB configuration issues."""

    def __init__(self, msg, *args, **kwargs):
        """
        Initialization method for Configuration Exceptions.

        :param msg: Mesage desired to output to terminal on exception.
        :type msg: String
        """
        print utils.PPHeader(header="WARNING", buffer=True)
        print "The Jenkins-Report-Builder has not been configured properly."
        print "Please run 'Jenkins-Report-Builder --init'"
        print "{0}{1}".format('\t', msg)
        print utils.PPFooter(buffer=True)
        Exception.__init__(self, msg, *args, **kwargs)


class JRBConfig(object):
    """JRB Configuration object."""

    def __init__(self, config_name):
        """Initialization method for JRB Configurations."""
        self.config_path = os.path.join(
            JRB_CONFIG_DIR, config_name, '.config')
        # Check to make sure the file exists
        check = os.path.isfile(config_path)
        if not check:
            # Is the application even initialized? It would be really unusual
            # to get this far, but let's do a safety check.
            Initialize.is_initialized()

    @classmethod
    def is_configured(cls):
        """Check to confirm JRB has appropriate configuration files."""
        # check that there is at least one config file in the JRB Directory
        if not any('.config' in x for x in os.listdir(JRB_CONFIG_DIR)):
            raise InitializationException(
                msg=('No configurations found in {0}\n').format(
                    JRB_CONFIG_DIR))

    @classmethod
    def get_configs(cls):
        """Get a list of available configs."""
        print utils.PPHeader(header='AVAILABVLE CONFIGS')
        configs = [os.path.splitext(x)[0] for x in os.listdir(
            JRB_CONFIG_DIR) if x.endswith('.config')]
        sorted(configs)
        for config in configs:
            print '\t{}'.format(config)
        print utils.PPFooter()
