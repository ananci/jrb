"""Copyright 2016 Anna Eilering."""
import jenkins

import pprint


class Results(object):

    def __init__(self):
        self.results = []

    def add_result(self, result):
        self.results.append(result)

    def __repr__(self):
        r_list = [str(r) for r in self.results]
        return '\n'.join(r_list)


class Result(object):
    def __init__(self, build_info, console_output):
        # Pull out the data we want
        self.display_name = build_info.get('fullDisplayName', 'UNKNOWN')
        self.timestamp = build_info.get('timestamp', 'UNKNOWN')
        self.result = build_info.get('result', 'UNKNOWN')
        self.url = build_info.get('url', 'UNKNOWN')
        self.console_output = console_output

    def __repr__(self):
        return '{}: {}: {}'.format(
            self.display_name, self.result, self.timestamp)


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
