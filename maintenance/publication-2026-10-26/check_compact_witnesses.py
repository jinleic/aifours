"""Independent compact-witness audit; stdlib only, no repository writes."""
from pathlib import Path
from collections import Counter
from itertools import combinations
import json
import runpy

ROOT = Path(__file__).resolve().parents[2]
review = ROOT / 'institute/runs/six-lane-2026-10-16/review'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def cdf_ok(blocks, v):
    return (
        len(blocks) == (v - 1) // 20
        and all(len(b) == 5 and len(set(b)) == 5
                and all(0 <= x < v for x in b) for b in blocks)
        and Counter((x - y) % v for b in blocks for x in b for y in b if x != y)
        == Counter({x: 1 for x in range(1, v)})
    )


for v in (321, 501, 621, 681, 801, 901):
    path = review / f'cdf{v}-parent-inputs-v1' / f'cdf_{v}.txt'
    lines = path.read_text().splitlines()
    require(lines[0] == f'CDF {v} 5', f'CDF {v}: header mismatch')
    blocks = [list(map(int, line.split())) for line in lines[1:]]
    require(cdf_ok(blocks, v), f'CDF {v}: invalid witness')
    print(f'CDF({v},5,1): PASS; {len(blocks)} blocks, {v-1} distinct nonzero ordered differences')


def btd_ok(a):
    return (
        len(a) == 14
        and all(len(row) == 28 and set(row) <= {0, 1, 2}
                and row.count(1) == 8 and row.count(2) == 3 for row in a)
        and all(sum(a[i][j] for i in range(14)) == 7 for j in range(28))
        and all(sum(x*y for x, y in zip(a[i], a[j])) == 6
                for i, j in combinations(range(14), 2))
    )


path = review / 'btd14-28-parent-inputs-v1/btd14-28-witness-v1.btd'
lines = path.read_text().splitlines()
require(lines[0] == 'BTD 14 28 8 3 14 7 6', 'BTD: header mismatch')
btd = [list(map(int, line.split())) for line in lines[1:]]
require(btd_ok(btd), 'BTD: invalid witness')
print('BTD(14,28;8,3,14;7,6): PASS; 14 rows, 28 columns, 91 pairs')


def cfr_ok(a):
    return (
        len(a) == 5
        and all(sorted(row) == list(range(27)) for row in a)
        and len({(row[j], row[(j+d) % 27], d)
                 for row in a for j in range(27) for d in range(1, 27)}) == 3510
    )


cfrs = {}
for label in ('A', 'B'):
    path = review / f'cfr27-parent-inputs-v1/{label}-CFR.raw'
    a = [list(map(int, line.split())) for line in path.read_text().splitlines()]
    require(cfr_ok(a), f'CFR {label}: invalid witness')
    cfrs[label] = a
    print(f'CFR(5,27) witness {label}: PASS; 3510 unique circular events')

path = review / 'cdf321-parent-inputs-v1/cdf_321.txt'
a = [list(map(int, line.split())) for line in path.read_text().splitlines()[1:]]
b = [row[:] for row in a]
b[0][0] = b[0][1]
require(cdf_ok(a, 321) and not cdf_ok(b, 321), 'CDF corruption control failed')
print('CDF mutation duplicate block element: REJECTED')

b = [row[:] for row in btd]
b[0][0] = 0
require(btd_ok(btd) and not btd_ok(b), 'BTD corruption control failed')
print('BTD mutation wrong row/column counts: REJECTED')

b = [row[:] for row in cfrs['A']]
b[1] = b[0][:]
require(cfr_ok(cfrs['A']) and not cfr_ok(b), 'CFR corruption control failed')
print('CFR mutation repeated permutation row/event collisions: REJECTED')

# Reuse separately authored definition-first checkers for the two larger designs.
for script, certificate, order, digest in [
    ('check_rdsqs_independent.py',
     'rdsqs52-parent-inputs-v1/rdsqs52_z52_m23.txt', 52,
     '7ae0a828b5af08b4bd9b423564981d85e3703886553638024fdc812f564989a6'),
    ('check_mcdsqs_independent.py',
     'mcdsqs38-parent-inputs-v1/mcdsqs38_g342_s0.txt', 38,
     '973f93e4646e48df64b70b3a64811afcdc87b10a1767222f54ffe65d3a303f1c'),
]:
    checker = runpy.run_path(str(review / script))
    result = checker['check'](review / certificate, order, digest)
    print(json.dumps({key: value for key, value in result.items()
                      if key in {'status', 'v', 'blocks',
                                 'distinct_triples_covered', 'triple_universe',
                                 'points_resolved', 'points_coloured', 'colours'}}))
