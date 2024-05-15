import csv
import os


class RankTranslator(object):
    def __init__(self, settings):
        self.settings = settings
        self.args = settings.args

        self.check_files_exists()

        self.rank_data = self.read_csv(self.args.rank_csv)
        self.new_data = self.read_csv(self.args.new_csv)
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
            writer = csv.DictWriter(csvfile, fieldnames=self.master_headers())
            writer.writeheader()
            for row in self.new_data:
                writer.writerow(row)

    def translate(self):
        

        self.write_csv()
