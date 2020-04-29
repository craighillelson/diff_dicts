"""Finds the differences between two dictionaries and writes them to a csv."""

import csv


def write_to_csv(name_of_file, dct):
    """Write dictionary to csv."""
    with open(name_of_file, 'w') as out_file:
        out_csv = csv.writer(out_file)
        out_csv.writerow(['player', 'number'])
        for player, jersey_num in dct.items():
            keys_values = (player, jersey_num)
            out_csv.writerow(keys_values)


DCT1 = {
    'boomer': '7',
    'muñoz': '78',
    }

DCT2 = {
    'montana': '16',
    'boomer': '7',
    }

DIFF1 = {k: DCT1[k] for k in set(DCT1) - set(DCT2)}
DIFF2 = {k: DCT2[k] for k in set(DCT2) - set(DCT1)}

MERGED_DIFFS = {**DIFF1, **DIFF2}

write_to_csv('diffs.csv', MERGED_DIFFS)
print('"diffs.csv" exported successfully')
