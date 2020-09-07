"""Finds the differences between two dictionaries and writes them to a csv."""

import csv


def diff_dictionaries(DCT1, DCT2):
    """Output a dictionary of the differences between two dictionaries."""
    return {player: DCT1[player] for player in set(DCT1) - set(DCT2)}


def write_to_csv(dct):
    """Write dictionary to csv."""
    with open("diffs.csv", "w") as out_file:
        out_csv = csv.writer(out_file)
        out_csv.writerow(["player", "number"])
        for player, jersey_number in dct.items():
            keys_values = (player, jersey_number)
            out_csv.writerow(keys_values)

    print('\n"diffs.csv" exported successfully\n')


DCT1 = {
    "boomer": "7",
    "muñoz": "78",
    }

DCT2 = {
    "montana": "16",
    "boomer": "7",
    }

DIFF1 = diff_dictionaries(DCT1, DCT2)
DIFF2 = diff_dictionaries(DCT2, DCT1)

MERGED_DIFFS = {**DIFF1, **DIFF2}

write_to_csv(MERGED_DIFFS)
