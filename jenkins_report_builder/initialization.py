"""Copyright 2016 Anna Eilering."""

import os

from jenkins_report_builder.constants import (
    JRB_ROOT_DIR, JRB_LOG_DIR, JRB_CONFIG_DIR, JRB_ENGINE_CONFIG_NAME)
from jenkins_report_builder.utils.io_utils import (
    DirectoryUtilities, FileUtilities)
from jenkins_report_builder.utils.output_utils import (
    PPHeader, PPFooter)
from jenkins_report_builder import custom_exceptions


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

        with open(os.path.join(
                'jenkins_report_builder',
                'configuration',
                'default_engine_config.config'), 'r') as dec:
            engine_config_data = dec.read().format(
                default_results_path=os.path.join(JRB_ROOT_DIR, 'results'))

        # Create the JRB Engine configuration file
        FileUtilities.safe_config_create(
            JRB_ROOT_DIR,
            JRB_ENGINE_CONFIG_NAME,
            engine_config_data)

        with open(os.path.join(
                'jenkins_report_builder',
                'configuration',
                'sample_config.config'), 'r') as dec:
            sample_config_data = dec.read().format(
                default_results_path=JRB_ROOT_DIR)

        # Create the JRB Engine configuration file
        FileUtilities.safe_config_create(
            JRB_CONFIG_DIR,
            'sample.config',
            sample_config_data)

        print PPFooter(buffer=True)

    @classmethod
    def is_initialized(cls):
        """Check to see if JRB has been properly initialized."""
        # check that the jrb directory is present
        if not os.path.isdir(JRB_ROOT_DIR):
            raise custom_exceptions.InitializationException(
                msg='{0} directory is not present.'.format(JRB_ROOT_DIR))
        if not os.path.isdir(JRB_LOG_DIR):
            raise custom_exceptions.InitializationException(
                msg='{0} directory is not present.'.format(JRB_LOG_DIR))
        if not os.path.isdir(JRB_CONFIG_DIR):
            raise custom_exceptions.InitializationException(
                msg='{0} directory is not present.'.format(JRB_CONFIG_DIR))
