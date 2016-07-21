import datetime
from collections import OrderedDict
from prettytable import PrettyTable

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
    def __init__(self, job, build_info=None, console_output=None):
        # Pull out the data we want
        if build_info:
            self.display_name = build_info.get('fullDisplayName', 'UNKNOWN')
            self.timestamp = datetime.datetime.fromtimestamp(
                build_info.get('timestamp', 0) / 1000).strftime(
                '%Y-%m-%d %H:%M:%S CST')
            self.result = build_info.get('result', 'UNKNOWN')
            self.url = build_info.get('url', 'UNKNOWN')
            self.console_output = console_output

            # Try to find the trigger
            actions = build_info.get(
                'actions', [{}])
            self.trigger = 'UNKNOWN'
            for action in actions:
                self.trigger = (
                    action.get('causes', [{}])[0].get('shortDescription') or
                    self.trigger)

        # There's cases where a Job is present but there is no build
        # information. We still want this data.
        else:
            self.display_name = job.get('name', 'UNKNOWN')
            self.timestamp = ''
            self.result = ''
            self.url = job.get('url', 'UNKNOWN')
            self.trigger = ''
            self.console_output = ''
