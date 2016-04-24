"""Copyright 2016 Anna Eilering."""
from argparse import ArgumentParser
import sys

from jenkins_report_builder import custom_exceptions
from jenkins_report_builder import initialization
from jenkins_report_builder.configuration.config import JRBConfig
from jenkins_report_builder.main import ViewReport


def get_args():
    """Get the command line arguments."""
    parser = ArgumentParser(
        description='Generate a report from a Jenkins View.')

    subparsers = parser.add_subparsers(help='Commands', dest='command')

    subparsers.add_parser(
        'init',
        help='Initialize Jenkins Report Viewer')

    subparsers.add_parser(
        'list',
        help='Display a list of available configurations.')

    run_parser = subparsers.add_parser(
        'run',
        help='Run the JRB against a targeted Jenkins.')
    run_parser.add_argument(
        'config',
        metavar='<configuration file path>',
        help='Name of the configuration file to be used.')
    run_parser.add_argument(
        'url',
        metavar='<URL to Jenkins view>',
        help='Name of the configuration file to be used.')
    return parser


def entry_point():
    """Entry Point to the Jenkins Report Builder Script."""
    # Get the command line arguments
    args = get_args().parse_args()

    if args.command == 'init':
        try:
            initialization.Initialize()
        except custom_exceptions.SafeConfigurationException:
            pass
        sys.exit(0)

    # Anything beyond this point would error if initialization has not occured.
    try:
        initialization.Initialize.is_initialized()
    except custom_exceptions.InitializationException:
        # JRB was not properly initialized.
        sys.exit(1)

    if args.command == 'list':
        try:
            JRBConfig.get_configs()
        except custom_exceptions.ConfigurationException:
            pass
        sys.exit(0)

    try:
        config = JRBConfig(args.config)
        print config
    except custom_exceptions.ConfigurationException:
        # JRB was not properly configured.
        sys.exit(1)

    # TODO - add options other than view reporting
    ViewReport(config=config, hr_view_url=args.url)


if __name__ == "__main__":
    """Alternate entry point to the Jenkins Report Builder Script."""
    entry_point()
