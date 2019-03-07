""" __doc__ """

import csv

def write_to_csv(name_of_file, dct):
    """ write dictionary to csv """
    with open(name_of_file, "w") as out_file:
        out_csv = csv.writer(out_file)
        out_csv.writerow(HEADERS) # define HEADERS before running function
        for k, v_number in dct.items():
            keys_values = (k, v_number)
            out_csv.writerow(keys_values)


HEADERS = [
    'player',
    'number',
    ]

DCT1 = {
    'boomer': '7',
    'munoz': '78',
    }

DCT2 = {
    'montana': '16',
    'boomer': '7',
    }

DIFF1 = {k: DCT1[k] for k in set(DCT1) - set(DCT2)}
DIFF2 = {k: DCT2[k] for k in set(DCT2) - set(DCT1)}

MERGED_DIFFS = {**DIFF1, **DIFF2}

write_to_csv('diffs.csv', MERGED_DIFFS)
