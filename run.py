"""
A script for getting ranks for a pack from one
CSV onto another CSV, while keeping the sorting
of the new CSV.

Author: Manuel Senfft (www.tagirijus.de)
"""

from ranktranslator.settings import Settings
from ranktranslator.ranktranslator import RankTranslator


def main(settings):
    """Run the programm."""
    S = Settings()
    RT = RankTranslator(S)

    if S.args.convert == 'NONE':
        RT.translate()
    else:
        RT.convert_json_to_csv(S.args.convert)


if __name__ == '__main__':
    main(Settings())
