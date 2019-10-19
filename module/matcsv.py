#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import os
import pprint
import re
import sys


def read_csv(csv_file_path):
    title_label, player_list = [], []
    with open(csv_file_path, "r") as f:
        reader = csv.reader(f)
        for i,row in enumerate(reader):
            if i == 0:
                title_label = row
            else:
                player_list.append(row)
    print(title_label[1])



def main(args):
    read_csv(args[1])

# if __name__ == '__main__':
#     configs = glob.glob('etc/mock/*.cfg')
#     configs.sort()
#     for c in configs:
#         if os.path.basename(c).startswith('site-defaults'):
#             continue
#         Config(c).check_urls()

if __name__ == "__main__":
    main(sys.argv)
