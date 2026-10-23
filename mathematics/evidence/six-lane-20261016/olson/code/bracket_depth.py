#!/usr/bin/env python3
"""Depth of reflection-bracket units f [U] f where U is tiled by atoms (alpha_j, 1).

Point set (Z_p^2, coordinates (value, half-size)):
  P_J = (sum_{j in J} alpha_j, |J|)          J nonempty  (inner selection only)
  Q_J = (C - sum_{j in J} alpha_j, |J| + 1)  all J       (both reflections + inner)
Full depth = d+1 (d = #atoms) iff no polynomial of degree <= d vanishes on all
points and is nonzero at the origin.  Enumerates all atom multisets for small d
and reports degenerate (not full) configurations.
Usage: bracket_depth.py p d [C]
"""
import sys, itertools
sys.path.insert(0, __import__('os').path.dirname(__file__))
from tiling import depth_at_least

def points(alphas, C, p):
    d = len(alphas)
    pts = set()
    for r in range(0, d + 1):
        for J in itertools.combinations(range(d), r):
            s = sum(alphas[j] for j in J) % p
            if r:
                pts.add((s, r % p))
            pts.add(((C - s) % p, (r + 1) % p))
    return pts

def main():
    p = int(sys.argv[1]); d = int(sys.argv[2])
    Cs = [int(sys.argv[3])] if len(sys.argv) > 3 else range(p)
    for C in Cs:
        bad = []
        for alphas in itertools.combinations_with_replacement(range(p), d):
            pts = points(alphas, C, p)
            if not depth_at_least(pts, d + 1, p):
                bad.append(alphas)
        print('p', p, 'd', d, 'C', C, 'degenerate', len(bad), bad[:20])

if __name__ == '__main__':
    main()
