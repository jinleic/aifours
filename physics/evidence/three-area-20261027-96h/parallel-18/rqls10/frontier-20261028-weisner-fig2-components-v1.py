#!/usr/bin/env python3
"""Check Weisner (1963), Fig. 2, and all paired-color component sizes."""
import importlib.util
from pathlib import Path
from collections import Counter
from itertools import combinations

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('switch', ROOT / 'frontier-20261028-ols10-switch-v1.py')
switch = importlib.util.module_from_spec(spec)
spec.loader.exec_module(switch)
ROWS = (
    '96 64 41 13 38 87 72 25 59 00',
    '69 97 75 52 24 40 08 83 36 11',
    '47 79 98 86 63 35 51 10 04 22',
    '15 58 89 90 07 74 46 62 21 33',
    '32 26 60 09 91 18 85 57 73 44',
    '84 43 37 71 19 92 20 06 68 55',
    '70 05 54 48 82 29 93 31 17 66',
    '28 81 16 65 50 03 39 94 42 77',
    '53 30 02 27 76 61 14 49 95 88',
    '01 12 23 34 45 56 67 78 80 99',
)
switch.TABLE = tuple(tuple(tuple(map(int, word)) for word in row.split()) for row in ROWS)
switch.check_table()
histogram = Counter()
for a, b in combinations(range(10), 2):
    comp = switch.components(a, b)
    histogram[tuple(sorted(map(len, comp)))] += 1
    if len(comp) > 1:
        print('nontrivial switch', a, b, 'sizes', tuple(sorted(map(len, comp))))
print('Fig.2 exact OLS check: PASS')
print('Fig.2 45 pair graph component sizes:', dict(sorted(histogram.items())))
