import csv
import json
import os


class RankTranslator(object):
    COLUMN_PACK_TITLE = 'Pack Title'
    COLUMN_RANK = 'Rank'
    HEADERS = [
        COLUMN_PACK_TITLE,
        COLUMN_RANK
    ]

    def __init__(self, settings):
        self.settings = settings
        self.args = settings.args

        if settings.args.convert == 'NONE':
            self.check_files_exists()

            self.rank_data = self.read_csv(self.args.rank_csv)
            self.new_data = self.read_csv(self.args.new_csv)
            self.out_data = []
            self.out_file = self.args.new_csv.replace('.csv', '_TRANSLATED.csv')


    def check_files_exists(self):
        if not os.path.isfile(self.args.rank_csv):
            print(f'"{self.args.rank_csv}" is no file.')
            exit()
        if not os.path.isfile(self.args.new_csv):
            print(f'"{self.args.new_csv}" is no file.')
            exit()

    def read_csv(self, which):
        with open(which, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]
        return data

    def write_csv(self):
        with open(self.out_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.HEADERS)
            writer.writeheader()
            for row in self.out_data:
                writer.writerow(row)

    def translate(self):
        self.out_data = []
        DONE = []

        for new_pack in self.new_data:
            title_new = new_pack[self.COLUMN_PACK_TITLE]
            append_me = {
                self.COLUMN_PACK_TITLE: title_new,
                self.COLUMN_RANK: ''
            }

            for ranked_pack in self.rank_data:
                title_ranked = ranked_pack[self.COLUMN_PACK_TITLE]
                rank = ranked_pack[self.COLUMN_RANK]

                if title_new == title_ranked:
                    append_me = {
                        self.COLUMN_PACK_TITLE: title_new,
                        self.COLUMN_RANK: rank
                    }

            self.out_data.append(append_me)

        self.write_csv()

    def convert_json_to_csv(self, filename):
        if not os.path.isfile(filename):
            print(f'File "{filename}" odes not exist.')
            exit(1)

        with open(filename, 'r') as jsonfile:
            json_data = json.load(jsonfile)

        fieldnames = ['Pack Title', 'Rank']

        with open(filename.replace('.json', '.csv'), mode='w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for entry in json_data:
                row = {fieldnames[0]: entry['packTitle'], fieldnames[1]: entry['publishedMulti']}
                writer.writerow(row)
