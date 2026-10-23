#!/usr/bin/env python3
"""Exact read-only cross-check of a NECESSARY condition for frozen independent-B ms09 skeletons (no solver).
Saturation (5*21+3*22=171=C(19,2)) makes every row pair agree exactly once. For a row in d P0 quads, its P1 pair
count p, P1-quad count q and triple count t satisfy q=p+2-d and t=1+d-2p, hence p=0 (d=0), p<=1 (d=1,2),
p in {1,2} (d=3), p=2 (d=4), p=3 (d=5). Each P1 column has exactly one 2-group, so there are exactly three pair
edges; partners agree there, so their P0-quad sets are disjoint and both have p>=1. This script exhaustively
checks all choices of three distinct disjoint-support edges against those exact row constraints.
A skeleton failing it is excluded mathematically; passing it proves nothing. Prints JSON; writes nothing.
"""
import hashlib
import itertools
import json
from pathlib import Path

L = Path(__file__).resolve().parent.parent
SK = L/'cycle2/skel-b/skeletons-b-ms09.json'
SK_SHA = '7c46ebbad3389476407e99807593287a8b3bb6c6a80f34574f0e9c00134293d0'


def rows_of(sk,c0=5):
    deg = [0]*c0
    for t in sk['types']:
        for x in t: deg[x] += 1
    rows = [frozenset(t) for t in sk['types']]
    for x in range(c0): rows += [frozenset([x])]*(4-deg[x])
    rows += [frozenset()]*sk['empty']
    assert len(rows) == 19 and all(d <= 4 for d in deg)
    return rows


ALLOWED = {0:{0},1:{0,1},2:{0,1},3:{1,2},4:{2},5:{3}}


def witness(rows):
    edges = [(i,j) for i,j in itertools.combinations(range(len(rows)),2) if rows[i] and rows[j] and not rows[i] & rows[j]]
    for choice in itertools.combinations(edges,3):
        p = [0]*len(rows)
        for i,j in choice: p[i] += 1; p[j] += 1
        if all(p[r] in ALLOWED[len(rows[r])] for r in range(len(rows))): return choice
    return None


def main():
    raw = SK.read_bytes(); assert hashlib.sha256(raw).hexdigest() == SK_SHA
    D = json.loads(raw); assert D['c0'] == 5 and D['L'] == 0 and len(D['skeletons']) == 71
    excluded = [bi for bi,sk in enumerate(D['skeletons']) if witness(rows_of(sk)) is None]
    print(json.dumps({'skeleton_sha256':SK_SHA,'cases':71,'excluded_by_necessary_pair_condition':excluded,
                      'scope':'necessary condition only; no solver/checker; non-excluded cases remain open'},indent=1))


if __name__ == '__main__':
    main()
