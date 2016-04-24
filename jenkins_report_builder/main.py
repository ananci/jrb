"""Copyright 2016 Anna Eilering."""
import jenkins

import pprint

class ChartResults(object):

    def __init__(object):
        self.results = []

class ChartResult(object):
    def __init__(self, job_name, result, timestamp, trigger):
        for key, value in locals().items():
            if key != 'self':
                setattr(self, key, value)


class ViewReport(object):

    def __init__(self, config, hr_view_url):
        """Generate the neccesary report from a View."""
        # Most of this should be moved out of __init__
        self.config = config
        self.hr_view_url = hr_view_url

        username = config.username
        password = config.password

        server = jenkins.Jenkins(
            self.hr_view_url,
            username=username,
            password=password)

        pp = pprint.PrettyPrinter(indent=4)

        # get the jobs
        self.jobs = server.get_jobs()
        for job in self.jobs:
            job_name = job.get('name')
            job_info = server.get_job_info(job_name)

            # pp.pprint(job_info)
            # from this we can get the last build number
            last_build_number = job_info.get('lastBuild', {}).get(
                'number', None)
            if not last_build_number:
                # TODO - still report what we found.
                continue

            build_info = server.get_build_info(job_name, last_build_number)
            console_output = server.get_build_console_output(
                job_name, last_build_number)
            pp.pprint(build_info)
            pp.pprint(console_output)
