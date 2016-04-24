"""Copyright 2016 Anna Eilering."""
import os


# TODO - seperate buffers

class PPHeader(object):
    """Pretty print a centered header."""

    TERMINAL_WIDTH = 80

    def __init__(self, header, buffer=False):
        """Initialization method for pretty print header."""
        self.header_list = []
        if buffer:
            self.header_list.append(' ')
        self.header_list.append('=' * self.TERMINAL_WIDTH)
        # Let's format this all pretty like
        offset = 0
        if len(header) < self.TERMINAL_WIDTH:
            offset = (self.TERMINAL_WIDTH / 2) - (len(header) / 2)
        spaces = ' ' * offset
        self.header_list.append('{}{}'.format(spaces, header))
        self.header_list.append('-' * self.TERMINAL_WIDTH)
        if buffer:
            self.header_list.append(' ')

    def __str__(self):
        """String method for PPFooter."""
        return '\n'.join(self.header_list)


class PPFooter(object):
    """Pretty print a Footer."""

    TERMINAL_WIDTH = 80

    def __init__(self, buffer=False):
        """Initialization method for pretty print footer."""
        self.footer_list = []
        if buffer:
            self.footer_list.append(' ')
        self.footer_list.append('=' * self.TERMINAL_WIDTH)
        if buffer:
            self.footer_list.append(' ')

    def __str__(self):
        """String method for PPFooter."""
        return '\n'.join(self.footer_list)


class DirectoryUtilities(object):
    """Common Directory Utilities."""

    @classmethod
    def safe_create_dir(cls, directory_path):
        """Convenience method for safely creating a directory."""
        if not os.path.exists(directory_path):
            print '\tCreating path at {}'.format(directory_path)
            os.makedirs(directory_path)
        else:
            print '\tPath already exists at {}'.format(directory_path)
