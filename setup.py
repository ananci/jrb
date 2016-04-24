"""Copyright 2016 Anna Eilering."""

from setuptools import setup, find_packages


def get_long_description():
    """
    Get Long Description text for Jenkins Report Builder.

    :return: 'Stuff'
    :rtype: String
    """
    # TODO - Add better description here.
    return "Stuff"


def get_license():
    """
    Get License text for Jenkins Report Builder.

    :return: 'Stuff'
    :rtype: String
    """
    # TODO - Set up a license for this
    return "license"

# Normal Setup Stuff
setup(
    name='jenkins-report-builder',
    version='0.1.0',
    description='Report Generator tool for Jenkins 1.X',
    long_description=get_long_description(),
    author='Anna Eilering',
    author_email='nahkki@gmail.com',
    url='https://github.com/ananci/jrb',
    install_requires=[],
    packages=find_packages(),
    license=get_license(),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'License :: Freely Distributable',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Topic :: Office/Business',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Utilities'],
    entry_points={
        'console_scripts':
            [('jenkins-report-builder=jenkins_report_builder.command_line:'
              'entry_point')]})
