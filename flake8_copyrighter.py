#
# flake8_copyrighter.py
#
# Copyright (c) 2018 Joshua Hadley
#

"""
Flake8 plugin to check for presence of a copyright string and to compare
copyright date against file modification date.
"""

from datetime import datetime
import os
import platform
import re

DEFAULT_LINE_PATTERN = r'copyright .+ [0-9][0-9][0-9][0-9]'
DEFAULT_YEAR_PATTERN = r'\d{4}'
DEFAULT_CODE_BASE = 'CRC000'


def get_file_mod_year_string(path_to_file):
    """
    Get modification year (as a string) of the file at `path_to_file`.
    Based on http://stackoverflow.com/a/39501288/1709587
    """
    if platform.system() == 'Windows':
        mt = os.path.getmtime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        mt = stat.st_mtime

    return datetime.fromtimestamp(mt).strftime('%Y')


class CopyrightDateChecker(object):
    name = 'copyrighter-plugin'
    version = '1.0.0'

    def __init__(self, tree, lines=[], filename=None):
        self.lines = lines
        self.filename = filename
        self.foundcw = False

        if filename is not None:
            self.modyear = get_file_mod_year_string(filename)
        else:
            self.modyear = str(datetime.now().year)

    @classmethod
    def add_options(cls, option_manager):
        """
        Add option flags to be recognized by flake8.
        """
        option_manager.add_option(
            '--crc-line-pattern',
            type='str',
            default=DEFAULT_LINE_PATTERN,
            parse_from_config=True,
        )

        option_manager.add_option(
            '--crc-year-pattern',
            type='str',
            default=DEFAULT_YEAR_PATTERN,
            parse_from_config=True,
        )

        option_manager.add_option(
            '--crc-code-base',
            type='str',
            default=DEFAULT_CODE_BASE,
            parse_from_config=True,
        )

    @classmethod
    def parse_options(cls, optmanager, options, extra_args):
        """
        Parse the supplied options
        """
        cls.line_pattern = options.crc_line_pattern
        cls.year_pattern = options.crc_year_pattern
        cls.msg_code_base = options.crc_code_base

    def run(self):
        """Perform the check."""
        if len(self.lines) == 0:
            return  # don't check (and don't error on) empty files

        for lineno, line in enumerate(self.lines):
            m = re.search(self.line_pattern, line, flags=re.IGNORECASE)
            if m:
                self.foundcw = True
                all_cw_years = sorted(re.findall(self.year_pattern, line))
                if all_cw_years[-1] != self.modyear:
                    yield (
                        lineno + 1,
                        line.find("Copyright"),
                        '{}0 Copyright string does not contain '
                        'file modification year '
                        '({})'.format(self.msg_code_base, self.modyear),
                        type(self),
                    )

                break  # after first instance of matched line

        if not self.foundcw:
            yield (
                1,
                0,
                '{}1 Copyright string not found'.format(self.msg_code_base),
                type(self),
            )
