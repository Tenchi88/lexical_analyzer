# -*- coding: utf-8 -*-
import json
import csv

# def show_path_stat(path, top_function, top_size=10):
#     top = top_function(path, top_size=top_size)
#     for word, occurrence in top:
#         print(word, occurrence)


class OutputManager:
    def __init__(
            self,
            print_output=False,
            json_file_name=None,
            csv_file_name=None
    ):
        self.print = print_output
        self.json_file_name = json_file_name
        self.csv_file_name = csv_file_name

    @staticmethod
    def print_output(top):
        for word, occurrence in top:
            print(word, occurrence)

    def generate_json(self, top):
        with open(self.json_file_name, 'w') as json_file:
            json.dump(top, json_file, sort_keys=True, indent=4)

    def generate_csv(self, top):
        with open(self.csv_file_name, 'w') as csv_file:
            csv.writer(csv_file, delimiter=',').writerows(top)

    def generate_output(self, top):
        if self.print:
            self.print_output(top)
        if self.json_file_name:
            self.generate_json(top)
        if self.csv_file_name:
            self.generate_csv(top)
