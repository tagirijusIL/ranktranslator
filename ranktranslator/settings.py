"""The class holding all the settings."""

import argparse


class Settings(object):
    """Settings class."""

    def __init__(
        self
    ):
        """Initialize the class and hard code defaults, if no file is given."""
        self.initArguments()

    def initArguments(self):
        self.args = argparse.ArgumentParser(
            description=(
                'A script for getting ranks for a pack from one CSV onto another CSV, while keeping the sorting of the new CSV.'
            )
        )

        self.args.add_argument(
            'rank_csv',
            nargs='?',
            default='NONE',
            help='The CSV with the pack title and their rank.'
        )

        self.args.add_argument(
            'new_csv',
            nargs='?',
            default='NONE',
            help='The CSV with only the pack title but no rank, yet the new sorting.'
        )

        self.args = self.args.parse_args()
