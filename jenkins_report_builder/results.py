"""Copyright 2016 Anna Eilering."""


class ChartResults(object):

    def __init__(self):
        self.results = {}

    def add_result(self, job_name, result, timestamp, trigger):
        self.results[job_name] = ChartResult(
            job_name, result, timestamp, trigger)


class ChartResult(object):
    def __init__(self, job_name, result, timestamp, trigger):
        for key, value in locals().items():
            if key != 'self':
                setattr(self, key, value)

    def report(self, report_output=None):
        pass
