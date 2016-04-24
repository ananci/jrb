"""Copyright 2016 Anna Eilering."""

from ConfigParser import ConfigParser
import os

from jenkins_report_builder.common import JRB_CONFIG_DIR
from jenkins_report_builder import custom_exceptions
from jenkins_report_builder.initialization import Initialize
from jenkins_report_builder.utils.output_utils import (
    PPHeader, PPFooter)


class JRBConfig(object):
    """JRB Configuration object."""

    def __init__(self, config_name):
        """Initialization method for JRB Configurations."""
        if not config_name.endswith('.config'):
            config_name = '{0}{1}'.format(config_name, '.config')

        self.config_path = os.path.join(
            JRB_CONFIG_DIR, config_name)

        # Check to make sure the file exists
        check = os.path.isfile(self.config_path)
        if not check:
            # Is the application even initialized? It would be really unusual
            # to get this far, but let's do a safety check.
            Initialize.is_initialized()
            raise custom_exceptions.ConfigurationException(
                msg=('Unable to find a config file at {0}\n').format(
                    self.config_path))

    @classmethod
    def get_configs(cls):
        """Get a list of available configs."""
        if not any(x.endswith('.config') for x in os.listdir(JRB_CONFIG_DIR)):
            raise custom_exceptions.ConfigurationException(
                msg=('Unable to find any config files at {0}\n').format(
                    JRB_CONFIG_DIR))
        print PPHeader(header='AVAILABVLE CONFIGS')
        configs = [os.path.splitext(x)[0] for x in os.listdir(
            JRB_CONFIG_DIR) if x.endswith('.config')]
        sorted(configs)
        for config in configs:
            print '\t{}'.format(config)
        print PPFooter()