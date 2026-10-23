#!/usr/bin/env python3
"""Build checker-format control instances from source Example 2.4 (v=8), plus mutations.
Standard library only. Writes each output file exclusively, so existing files are never overwritten.

C1 positive: Example 2.4 as published. Expect ALL_PASS with 64 distinct rays.
C2 nonparallel negative: classical mate A0(i,j) = (2*i in GF(8)) XOR j of B = i XOR j. Expect P1-P3 to pass,
   P4 to fail, and exactly 8 distinct rays.
C3 orthogonality negative: C1 with cell (1,0) phase omega^3 changed to omega^4. Expect P3 to fail.
C4 Latin negative: C1 with B[0][0] and B[0][1] swapped. Expect P1 to fail.
C5 norm negative: C1 with cell (2,0) n changed from 4 to 3. Expect P2 to fail.
"""
import copy
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
N = 8  # omega = zeta_8; sqrt2 = zeta_8 + zeta_8^7
SQRT2 = [[1, 1], [7, 1]]
TERM = re.compile(r'(\\sqrt2)?(\\omega(?:\^\{(\d+)\})?)?\\ket\{(\d)\}')


def parse_cell(s, v):
    s = s.strip()
    if s.startswith('\\tfrac{1}{\\sqrt2}'):
        n = 2
        body = s[len('\\tfrac{1}{\\sqrt2}'):]
    elif s.startswith('\\tfrac12'):
        n = 4
        body = s[len('\\tfrac12'):]
    else:
        n = 1
        body = s
    x = [[] for _ in range(v)]
    terms = TERM.findall(body)
    assert terms, s
    # every non-space character must be consumed by terms, '+', parentheses
    rest = TERM.sub('', body).replace('+', '').replace('(', '').replace(')', '').strip()
    assert rest == '', (s, rest)
    for sq, om, ex, k in terms:
        e = 0
        if om:
            e = int(ex) if ex else 1
        k = int(k)
        if sq:
            x[k] += [[(a + e) % N, c] for a, c in SQRT2]
        else:
            x[k].append([e % N, 1])
    return {"n": n, "x": x}


def gf8_mul2(i):
    # GF(8) = F2[x]/(x^3+x+1); multiply by x
    i <<= 1
    if i & 8:
        i ^= 0b1011
    return i


def write_x(name, obj):
    path = os.path.join(HERE, name)
    with open(path, 'x') as fh:
        json.dump(obj, fh)
    print('wrote', name)


def main():
    with open(os.path.join(HERE, 'zhang_cao_ex24_cells.json')) as fh:
        src = json.load(fh)
    v = src['v']
    B = src['B']
    cells = [[parse_cell(c, v) for c in row] for row in src['cells_tex']]
    c1 = {"v": v, "N": N, "B": B, "cells": cells, "note": "C1 positive: Example 2.4"}
    write_x('C1_ex24_positive.json', c1)
    A0 = [[gf8_mul2(i) ^ j for j in range(v)] for i in range(v)]
    c2 = {"v": v, "N": N, "B": B,
          "cells": [[{"n": 1, "x": [[[0, 1]] if k == A0[i][j] else [] for k in range(v)]} for j in range(v)]
                    for i in range(v)],
          "note": "C2 classical mate, expect P4 fail with 8 rays"}
    write_x('C2_classical_nonparallel_negative.json', c2)
    c3 = copy.deepcopy(c1)
    cell = c3['cells'][1][0]
    assert cell['x'][3] == [[3, 1]], cell['x'][3]
    cell['x'][3] = [[4, 1]]
    c3['note'] = 'C3 phase mutation at cell (1,0), coordinate 3: omega^3 -> omega^4'
    write_x('C3_phase_mutation_negative.json', c3)
    c4 = copy.deepcopy(c1)
    c4['B'][0][0], c4['B'][0][1] = c4['B'][0][1], c4['B'][0][0]
    c4['note'] = 'C4 B[0][0] <-> B[0][1] swap'
    write_x('C4_latin_mutation_negative.json', c4)
    c5 = copy.deepcopy(c1)
    assert c5['cells'][2][0]['n'] == 4
    c5['cells'][2][0]['n'] = 3
    c5['note'] = 'C5 norm mutation at cell (2,0): n 4 -> 3'
    write_x('C5_norm_mutation_negative.json', c5)
    return 0


if __name__ == '__main__':
    sys.exit(main())
