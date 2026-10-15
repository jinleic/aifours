#!/usr/bin/env python3
"""Reproduce referee counterexamples directly as finite matrices."""
from collections import Counter
from fractions import Fraction
import json
from pathlib import Path
import sys


def weight(columns, rows):
    return sum(bool(c & rows) for c in columns)


def moment(white, black, rows):
    return sum(not (c & rows) for c in white) - sum(not (c & rows) for c in black)


def main():
    results = []
    white, black = [2], [3]
    assert Counter(c & 2 for c in white) == Counter(c & 2 for c in black)
    assert weight(black, 1)-weight(white, 1) == 1
    assert weight(black, 3)-weight(white, 3) == 0
    results.append({'case':'minimal-qualified-only is insufficient', 'n':2, 'm':1,
                    'white_columns':white, 'black_columns':black, 'singleton_gap':1, 'superset_gap':0})
    white, black = [1,0], [6,4]
    assert moment(white,black,3) == 0
    assert moment(white,black,1) == -1 and moment(white,black,2) == 1
    assert all(weight(black,q)-weight(white,q)>0 for q in (4,5,6,7))
    results.append({'case':'maximal-forbidden zero moments are insufficient', 'n':3, 'm':2,
                    'white_columns':white, 'black_columns':black, 'f12':0, 'f1':-1, 'f2':1})
    whites, blacks = [[0],[3]], [[1],[2]]
    for f in (1,2):
        assert Counter(tuple(c&f for c in m) for m in whites) == Counter(tuple(c&f for c in m) for m in blacks)
    expected = sum(Fraction(weight(b,3),2) for b in blacks)-sum(Fraction(weight(w,3),2) for w in whites)
    worst = min(weight(b,3) for b in blacks)-max(weight(w,3) for w in whites)
    assert expected == Fraction(1,2) and worst == 0
    results.append({'case':'expected separation is not deterministic gap', 'n':2, 'm':1,
                    'white_collection':whites, 'black_collection':blacks,
                    'expected_gap':str(expected), 'worst_gap':worst})
    white, black = [3,0,0], [1,2,0]
    assert all(Counter(c&f for c in white)==Counter(c&f for c in black) for f in (1,2))
    assert weight(black,3)-weight(white,3)==1 and len(white)%2 == 1
    results.append({'case':'optimum denominator need not divide suboptimal expansion',
                    'n':2, 'm':3, 'white_columns':white, 'black_columns':black,
                    'global_alpha':'1/2', 'actual_alpha':'1/3'})
    out = Path(__file__).resolve().parents[1]/'evidence/referee-controls.json'
    out.write_text(json.dumps({'command':' '.join(sys.argv), 'all_passed':True, 'controls':results}, indent=2)+'\n')
    print(json.dumps({'all_passed':True, 'controls':len(results), 'output':str(out)}))


if __name__ == '__main__':
    main()
