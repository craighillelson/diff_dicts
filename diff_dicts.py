""" __doc__ """

import csv

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

DIFF = set(DCT1.items()) ^ set(DCT2.items())

with open("diff.csv", "w") as OUT_FILE:
    OUT_CSV = csv.writer(OUT_FILE)
    OUT_CSV.writerow(HEADERS) # define HEADERS before running function
    for player in DIFF:
        OUT_CSV.writerow(player)
