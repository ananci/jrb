"""Copyright 2016 Anna Eilering."""
from jenkins_report_builder.utils.output_utils import PPHeader, PPFooter


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


class ConfigurationException(Exception):
    """Custom Exception for reporting JRB configuration issues."""

    def __init__(self, msg, *args, **kwargs):
        """
        Initialization method for Configuration Exceptions.

        :param msg: Mesage desired to output to terminal on exception.
        :type msg: String
        """
        print PPHeader(header="WARNING", buffer=True)
        print 'The Jenkins-Report-Builder has not been configured properly.'
        print ('Please review the README to create appropriate configuration '
               'files.')
        print '{0}{1}'.format('\t', msg)
        print PPFooter(buffer=True)
        Exception.__init__(self, msg, *args, **kwargs)


class SafeConfigurationException(Exception):
    """Custom Exception for reporting JRB safe configuration issues."""

    def __init__(self, msg, *args, **kwargs):
        """
        Initialization method for Safe Configuration Exceptions.

        :param msg: Mesage desired to output to terminal on exception.
        :type msg: String
        """
        print PPHeader(header="WARNING", buffer=True)
        print ('There was an issue when attempting to manipulate a '
               'configuration file.')
        print ('Please check the location and manually adjust the '
               'configuration as desired.')
        print "{0}{1}".format('\t', msg)
        print PPFooter(buffer=True)
        Exception.__init__(self, msg, *args, **kwargs)
