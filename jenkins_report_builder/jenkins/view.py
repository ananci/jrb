"""Copyright 2016 Anna Eilering."""
import jenkins
from collections import OrderedDict
from prettytable import PrettyTable
import datetime

import pprint


class Results(object):

    # Order matters in the heading
    headers = OrderedDict()
    headers['display_name'] = 'Display Name'
    headers['url'] = 'URL'
    headers['trigger'] = 'Trigger'
    headers['timestamp'] = 'Time Stamp'
    headers['result'] = 'Result'

    def __init__(self):
        self.results = []
        self.p_table = PrettyTable(self.headers.values())

    def add_result(self, result):
        self.results.append(result)
        table_order_list = []
        for k in self.headers.keys():
            table_order_list.append(getattr(result, k, 'FAILURE'))
        self.p_table.add_row(table_order_list)

    def __repr__(self):
        return str(self.p_table)


class Result(object):
    def __init__(self, build_info, console_output):
        # Pull out the data we want
        self.display_name = build_info.get('fullDisplayName', 'UNKNOWN')
        self.timestamp = datetime.datetime.fromtimestamp(
            build_info.get('timestamp', '0') / 1000).strftime(
            '%Y-%m-%d %H:%M:%S CST')
        self.result = build_info.get('result', 'UNKNOWN')
        self.url = build_info.get('url', 'UNKNOWN')
        self.trigger = build_info.get(
            'actions', [{}])[0].get(
            'causes', [{}])[0].get('shortDescription', 'UNKOWN')
        self.console_output = console_output


class View(object):

    def __init__(self, config, hr_view_url):
        """Generate the necessary report from a View."""
        # Most of this should be moved out of __init__
        self.config = config
        self.hr_view_url = hr_view_url

        username = config.username
        password = config.password

        self.server = jenkins.Jenkins(
            self.hr_view_url,
            username=username,
            password=password)

    def get_most_recent_run(self):
        """Get the jobs representing the most recent run."""
        pp = pprint.PrettyPrinter(indent=4)

        results = Results()

        # get the jobs
        self.jobs = self.server.get_jobs()
        for job in self.jobs:
            job_name = job.get('name')
            job_info = self.server.get_job_info(job_name)

            # pp.pprint(job_info)
            # from this we can get the last build number
            last_build_number = job_info.get('lastBuild', {}).get(
                'number', None)
            if not last_build_number:
                # TODO - still report what we found.
                continue

            build_info = self.server.get_build_info(
                job_name,
                last_build_number)
            console_output = self.server.get_build_console_output(
                job_name, last_build_number)
            results.add_result(
                Result(build_info=build_info, console_output=console_output))

        print results
