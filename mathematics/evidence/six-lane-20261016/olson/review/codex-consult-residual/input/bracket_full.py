#!/usr/bin/env python3
"""Exact fullness of reflection-bracket units with their FULL option sets.

Shapes (letters in order):
  'fRf:m'   : f r^{2m} f              (bracket around an even rotation run)
  'frFrf:a' : f r f^{2a} r f          (bracket around r [ff..] r)
Values are enumerated up to the affine symmetry (rotation values scaled; reflection
values shifted/scaled consistently): we fix y_left = 0 and enumerate the rest.
Reports degenerate (non-full) assignments.
Usage: bracket_full.py p shape
"""
import sys, itertools
sys.path.insert(0, __import__('os').path.dirname(__file__))
from tiling import unit_points, depth_at_least

def main():
    p = int(sys.argv[1]); shape = sys.argv[2]
    kind, par = shape.split(':'); par = int(par)
    bad = []; total = 0
    if kind == 'fRf':
        m = par
        for C in range(p):           # y_right = -C  (C = y_left - y_right)
            for xs in itertools.combinations_with_replacement(range(p), 2 * m):
                unit = (('F', 0),) + tuple(('R', x) for x in xs) + (('F', (-C) % p),)
                total += 1
                if not depth_at_least(unit_points(unit, p), m + 1, p):
                    bad.append((C, xs))
    elif kind == 'frFrf':
        a = par
        for C in range(p):
            for x1 in range(p):
                for x2 in range(p):
                    for ys in itertools.product(range(p), repeat=2 * a) if a <= 1 else itertools.product(range(p), repeat=2 * a):
                        unit = (('F', 0), ('R', x1)) + tuple(('F', y) for y in ys) + (('R', x2), ('F', (-C) % p))
                        total += 1
                        if not depth_at_least(unit_points(unit, p), a + 2, p):
                            bad.append((C, x1, x2, ys))
    print('p', p, 'shape', shape, 'total', total, 'degenerate', len(bad))
    for b in bad[:60]:
        print('  ', b)

if __name__ == '__main__':
    main()
