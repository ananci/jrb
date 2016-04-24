"""Copyright 2016 Anna Eilering."""
import os

from jenkins_report_builder import custom_exceptions


class DirectoryUtilities(object):
    """Common Directory Utilities."""

    @classmethod
    def safe_create_dir(cls, directory_path):
        """Convenience method for safely creating a directory."""
        if not os.path.exists(directory_path):
            print '\tCreating path at {}'.format(directory_path)
            os.makedirs(directory_path)
        else:
            print '\tPath already exists at {}'.format(directory_path)


class FileUtilities(object):
    """Common File Utilities."""

    @classmethod
    def safe_config_create(cls, directory_path, config_name, config_data):
        """Safely create config, if it already exists raise an exception."""
        # make sure the directory is there
        DirectoryUtilities.safe_create_dir(directory_path)

        config_path = os.path.join(directory_path, config_name)
        if not os.path.isfile(config_path):
            print '\tCreating config at {}'.format(config_path)
            with open(config_path, 'w') as cf:
                cf.write(config_data)
        else:
            raise custom_exceptions.SafeConfigurationException(
                msg=('Configuration already exists at {0} \n'
                     '\t Please manually update the config.'))
