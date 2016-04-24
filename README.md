# JRB - Jenkins Report Builder
---

## Table of Contents

1. [Motivation](Motivation)
2. [Installation and Initialization](Installation)
3. [Configuration](Configuration)
4. [Basic Usage](Basic Usage)
---

## Motivation
Teams that use Jenkins to deploy, test, or even just as a CI/CD pipeline for
their code often need a way to report on the results of that test.

The purpose of this application is to provide a mechanism to report on
Jenkins job results without being tied to the target Jenkins. This python
application can be run on the target Jenkins, any Jenkins or, in fact,
anywhere that python code can be run.

This application was bourn of a need to meet compliance(SOX in particular)
requirements around Jenkins jobs. It generates a report in the format chosen(
pdf, html, text) and outputs it to a configured directory. This report includes
a chart representing all the names of all jobs selected by the user, their
results, and their last run date.

If desired this application can also output the console output from all jobs
following the chart.

## Installation
### To install JRB from github:
* You must have pip and setuptools installed
* It is recommended to install it in a virtualenv
* It is only tested on Python 2.7.X

Clone the repository locally.
Enter the repository:

`$ cd jrb`

pip install the application:

`$ pip install .`

### Initialization
To run JRB you must first initialize and configure the application.

Initialize jrb:

`(jrb) anna@anna-desktop:~/work/git-repos/jrb$ jenkins-report-builder init`

You will recieve similar output:

```================================================================================
                       INITIALIZING JENKINS REPORT VIEWER
--------------------------------------------------------------------------------

	Creating path at /home/anna/.jrb
	Creating path at /home/anna/.jrb/logs
	Creating path at /home/anna/.jrb/configs
	Path already exists at /home/anna/.jrb
	Creating config at /home/anna/.jrb/jrb_engine.config
	Path already exists at /home/anna/.jrb/configs
	Creating config at /home/anna/.jrb/configs/sample.config

================================================================================
 ```

Initialization will create a `.jrb` directory in your home directory. In this
directory you will find:

```
$ ls .jrb
configs  jrb_engine.config  logs
```

If you attempt to reinitialize and the initialization process has already been
run the application will exit and request that you manually reconfigured the
existing files.

#### To Force Automation Reconfiguration
Delete the `.jrb` directory in your home directory.

## Configuration
There are two configurations required to run JRB.

### JRB Engine Configuration
The first is an jrb_engine.config file that exists in the `.jrb` directory.
This controls common JRB configuration options:
* Results location - directory where results will be saved
* Resulted file name prefix - prefix for results files
* Default output format - defaults to 'PDF'
* Optional Header Information - additional data to inject into reports

You are not required to edit this configuration in order to run the
application. This configuration is generated on JRB Initialization and
provides advanced users a mechanism to customize their JRB setup.

### JRB Jenkins Configuration
The Second is at least one jenkins configuration file. These files exist in
the `.jrb/config` directory and each represents a common Jenkins you run JRB
reports against. This configuration file includes:
* Base URL for the targetted Jenkins for reporting purposes.
* Username and password for the target Jenkins (leave blank if not required.)
* Default Generator - a default user to put on reports generated.
* A label to represent the target Jenkins (A human readable tag.)

A `sample.config` file is automatically generated and placed in the
`.jrb/configs` directory on initialization.

You are required to provide a valid configuration for any Jenkins you wish
to run against.

## Basic Usage

### To list available configurations

`$ jenkins-report-builder list`

```
================================================================================
                               AVAILABVLE CONFIGS
--------------------------------------------------------------------------------
	sample
	production_jenkins
	staging_jenkins
	other_teams_jenkins
================================================================================
```
