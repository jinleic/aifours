#!/usr/bin/env python3
"""Check Weisner (1963), Fig. 3, and all paired-color component sizes.

The extracted web PDF omitted the first table cell.  The other nine symbols
in the first row force 00 if both component rows are Latin; 00 is a proposed
completion here and the full pair is then independently checked.
"""
import importlib.util
from pathlib import Path
from collections import Counter
from itertools import combinations

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('switch', ROOT / 'frontier-20261028-ols10-switch-v1.py')
switch = importlib.util.module_from_spec(spec)
spec.loader.exec_module(switch)
ROWS = (
    '00 65 18 52 96 29 47 81 34 73',
    '45 11 76 20 63 97 39 58 02 84',
    '13 56 22 87 31 74 98 49 60 05',
    '71 24 67 33 08 42 85 90 59 16',
    '69 82 35 78 44 10 53 06 91 27',
    '92 79 03 46 80 55 21 64 17 38',
    '28 93 89 14 57 01 66 32 75 40',
    '86 30 94 09 25 68 12 77 43 51',
    '54 07 41 95 19 36 70 23 88 62',
    '37 48 50 61 72 83 04 15 26 99',
)
switch.TABLE = tuple(tuple(tuple(map(int, word)) for word in row.split()) for row in ROWS)
switch.check_table()
histogram = Counter()
for a,b in combinations(range(10), 2):
    comps = switch.components(a,b)
    histogram[tuple(sorted(map(len, comps)))] += 1
    if len(comps) > 1:
        print('nontrivial switch',a,b,'sizes',tuple(sorted(map(len,comps))))
print('Fig.3 table (first cell completion inferred) exact OLS check: PASS')
print('Fig.3 45 pair graph component sizes:',dict(sorted(histogram.items())))
