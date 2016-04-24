"""Copyright 2016 Anna Eilering."""
from argparse import ArgumentParser
import sys

from jenkins_report_builder import initialization
from jenkins_report_builder.config import ConfigurationException, JRBConfig
from jenkins_report_builder.main import main


def get_args():
    """Get the command line arguments."""
    parser = ArgumentParser(
            description='Generate a report from a Jenkins View.')

    subparsers = parser.add_subparsers(help='Commands', dest='command')

    init_parser = subparsers.add_parser(
        'init',
        help='Initialize Jenkins Report Viewer')

    list_parser = subparsers.add_parser(
        'list',
        help='Display a list of available configurations.')

    run_parser = subparsers.add_parser(
        'run',
        help='Run the JRB against a targeted Jenkins.')
    run_parser.add_argument(
        'config',
        metavar='<configuration file path>',
        help='Name of the configuration file to be used.')

    args = parser.parse_args()
    return args


def entry_point():
    """Entry Point to the Jenkins Report Builder Script."""
    args = get_args()

    if args.command == 'init':
        initialization.Initialize()
        sys.exit(0)

    if args.command == 'list':
        JRBConfig.get_configs()
        sys.exit(0)

    try:
        initialization.Initialize.is_initialized()
    except initialization.InitializationException as e:
        # JRB was not properly initialized.
        sys.exit(1)

    try:
        config = JRBConfig(args.config)
    except ConfigurationException as e:
        # JRB was not properly configured.
        sys.exit(1)

    main(config=config)


if __name__ == "__main__":
    """Alternate entry point to the Jenkins Report Builder Script."""
    entry_point()
