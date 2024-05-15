"""
A script for getting ranks for a pack from one
CSV onto another CSV, while keeping the sorting
of the new CSV.

Author: Manuel Senfft (www.tagirijus.de)
"""

from sheettranslator.settings import Settings
from sheettranslator.sheettranslator import RankTranslator


def main(settings):
    """Run the programm."""
    RT = RankTranslator(settings)
    RT.translate()


if __name__ == '__main__':
    main(Settings())
