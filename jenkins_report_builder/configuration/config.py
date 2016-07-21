"""Copyright 2016 Anna Eilering."""

from ConfigParser import ConfigParser
import os

from jenkins_report_builder.constants import (JRB_ENGINE_PATH, JRB_CONFIG_DIR)
from jenkins_report_builder import custom_exceptions
from jenkins_report_builder.initialization import Initialize
from jenkins_report_builder.utils.output_utils import (
    PPHeader, PPFooter)


class ConfigParseInterface(object):
    def __init__(self):
        self.config = ConfigParser()
        if not os.path.exists(self.config_path):
            raise custom_exceptions.ConfigurationException(
                msg="Config File does not exist at {0} as expected".format(
                    self.config_path))
        try:
            self.config.read(self.config_path)
        except Exception as e:
            raise custom_exceptions.ConfigurationException(
                msg=e.message)

    def get(self, item_name, default=None):
        try:
            return self.config.get(self.section_name, item_name)
        except:
            return default


class EngineConfig(ConfigParseInterface):
    """JRB Engine Configuration Object."""
    config_path = JRB_ENGINE_PATH
    section_name = 'engine'

    @property
    def results_path(self):
        return self.get('results_path')


class JRBConfig(ConfigParseInterface):
    """JRB Configuration object."""
    section_name = 'jenkins'

    def __init__(self, config_name):
        """Initialization method for JRB Configurations."""
        if not config_name.endswith('.config'):
            config_name = '{0}{1}'.format(config_name, '.config')

        self.config_path = os.path.join(
            JRB_CONFIG_DIR, config_name)
        super(JRBConfig, self).__init__()

    @property
    def username(self):
        return self.get('username', None)

    @property
    def password(self):
        return self.get('password', None)

    @property
    def url(self):
        return self.get('base_url', None)

    @property
    def default_generator(self):
        return self.get('default_generator', 'Jenkins Report Viewer User')

    @property
    def jenkins_label(self):
        return self.get('jenkins_label', 'Jenkins')

    @property
    def insecure(self):
        insecure = self.get('insecure', 'False')
        if insecure.lower() == 'True'.lower():
            insecure = True
        return insecure

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
