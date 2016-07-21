"""Copyright 2016 Anna Eilering."""
import jenkins

from jenkins_report_builder.jenkins.results import Result, Results

import pprint


class View(object):

    def __init__(self, config, hr_view_url):
        """Generate the necessary report from a View."""
        # Most of this should be moved out of __init__
        self.config = config
        self.hr_view_url = hr_view_url

        # Because of how the Python Jenkins library works we must
        # monkey patch if using a self signed cert or otherwise unverified
        # cert
        if self.config.insecure:
            import ssl

            ssl._create_default_https_context = ssl._create_unverified_context

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
            job_info = self.server.get_job_info(job_name) or {}

            # pp.pprint(job_info)
            # from this we can get the last build number
            last_build = job_info.get('lastBuild') or {}
            last_build_number = last_build.get(
                'number', None)

            # This job was likely never run or there is no available
            # data for it on the Jenkins. Still report that there was a job.
            if not last_build_number:
                results.add_result(
                    Result(
                        job=job))
                continue

            build_info = self.server.get_build_info(
                job_name,
                last_build_number)
            # pp.pprint(build_info)
            console_output = self.server.get_build_console_output(
                job_name, last_build_number)
            results.add_result(
                Result(
                    job=job,
                    build_info=build_info,
                    console_output=console_output))

        return results
