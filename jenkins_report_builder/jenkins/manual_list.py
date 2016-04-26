"""Copyright 2016 Anna Eilering."""
import jenkins

import pprint


class ManualList(object):

    def __init__(self, config, file_path):
        """Generate the necessary report from a View."""
        # Most of this should be moved out of __init__
        self.config = config

        self.url = config.url
        username = config.username
        password = config.password

        with open(file_path, 'r') as fp:
            # TODO - make sure this parses correctly.
            self.jobs = fp.readlines()

        self.server = jenkins.Jenkins(
            self.hr_view_url,
            username=username,
            password=password)

    def get_most_recent_run(self):
        """Get the jobs representing the most recent run."""
        pp = pprint.PrettyPrinter(indent=4)

        for job_name in self.jobs:
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
            pp.pprint(build_info)
            pp.pprint(console_output)
