"""Copyright 2016 Anna Eilering."""


class ChartResults(object):

    def __init__(self):
        self.results = []


class ChartResult(object):
    def __init__(self, job_name, result, timestamp, trigger):
        for key, value in locals().items():
            if key != 'self':
                setattr(self, key, value)
