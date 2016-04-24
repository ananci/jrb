"""Copyright 2016 Anna Eilering."""
from argparse import ArgumentParser
import sys

from jenkins_report_builder import configuration


def get_args():
    """Get the command line arguments."""
    parser = ArgumentParser(
            description='Generate a report from a Jenkins View.')
    parser.add_argument(
        '--init',
        action='store_true',
        default=False,
        help="Initialize Jenkins Report Viewer")

    args = parser.parse_args()
    return args


def main():
    """Entry Point to the Jenkins Report Builder Script."""
    args = get_args()

    if args.init:
        configuration.Initialize()
        sys.exit(0)

    try:
        configuration.Initialize.is_initialized()
    except configuration.ConfigurationException as e:
        # JRB was not properly initialized.
        sys.exit(1)

    print "End of main."


if __name__ == "__main__":
    """Alternate entry point to the Jenkins Report Builder Script."""
    entry_point()
