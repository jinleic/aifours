#!/usr/bin/env python3
"""Native exact determinant successor, retaining the published interpolation scheme.

Uses owner-local FLINT fmpz_mat.det for every triangular-grid determinant. Source
rows and the exact two-variable Newton/Stirling conversion are unchanged in
meaning; the older Python-Bareiss producer and every earlier output stay frozen.
"""
import argparse
import hashlib
import importlib.util
import json
import math
import sys
from fractions import Fraction as Q
from multiprocessing import Pool
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'frontier-20261028-fastalgebra'))
import flint


def load(name, file):
    spec = importlib.util.spec_from_file_location(name, ROOT / file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


prior = load('prior_interpolation', 'frontier-20261028-level6-minor-polynomial.py')
DATA = None


def init(data):
    global DATA
    DATA = data


def determinant(point):
    i, j = point
    matrix = [[a + i * b + j * c for a, b, c in row] for row in DATA]
    return i, j, int(flint.fmpz_mat(matrix).det())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--a', type=int, required=True)
    ap.add_argument('--b', type=int, required=True)
    ap.add_argument('--rows-file')
    ap.add_argument('--tag', required=True)
    ap.add_argument('--workers', type=int, default=4)
    args = ap.parse_args()
    assert flint.__version__ == '0.9.0'
    name = f'frontier-20261028-level6-free-{args.a}{args.b}-pencil-v1.json'
    raw = (ROOT / name).read_bytes()
    P = json.loads(raw)
    out = ROOT / f'frontier-20261028-level6-{args.a}{args.b}6-minor-{args.tag}-v1.json'
    if out.exists():
        raise FileExistsError(out)
    if args.rows_file:
        rows = prior.al6.full_rows(P)
        selected = json.loads((ROOT / args.rows_file).read_text())['rows']
        assert len(selected) == len(P['selected_target_words']) == len(set(selected))
        matrices = [rows[w] for w in selected]
    else:
        selected = P['selected_target_words']
        matrices = [[[Q(v) for v in entry] for entry in row] for row in P['matrix']]
    data, scale = prior.h.int_rows(matrices)
    n = len(data)
    points = [(i, j) for i in range(n + 1) for j in range(n + 1 - i)]
    with Pool(args.workers, initializer=init, initargs=(data,)) as pool:
        vals = {(i, j): v for i, j, v in pool.imap_unordered(determinant, points, chunksize=16)}
    dx, dxy = {}, {}
    for j in range(n + 1):
        work = [vals[i, j] for i in range(n + 1 - j)]
        for i in range(n + 1 - j):
            dx[i, j] = work[0]
            work = [b - a for a, b in zip(work, work[1:])]
    for i in range(n + 1):
        work = [dx[i, j] for j in range(n + 1 - i)]
        for j in range(n + 1 - i):
            dxy[i, j] = work[0]
            work = [b - a for a, b in zip(work, work[1:])]
    st = prior.stirling_rows(n)
    factorials = [math.factorial(i) for i in range(n + 1)]
    NF = factorials[n]
    mixed = [[0] * (n + 1) for _ in range(n + 1)]
    for (i, j), d in dxy.items():
        if d:
            multiplier = d * (NF // factorials[j])
            for v, c in enumerate(st[j]):
                if c:
                    mixed[i][v] += multiplier * c
    nums = {}
    for v in range(n + 1):
        for u in range(n + 1 - v):
            z = sum(st[i][u] * (NF // factorials[i]) * mixed[i][v]
                    for i in range(u, n + 1) if st[i][u] and mixed[i][v])
            if z:
                nums[u, v] = z
    for i in range(n + 1):
        powers = [i**u for u in range(n + 1)]
        inner = [0] * (n + 1)
        for (u, v), c in nums.items():
            inner[v] += c * powers[u]
        for j in range(n + 1 - i):
            z = 0
            for c in reversed(inner):
                z = z * j + c
            assert z == vals[i, j] * NF * NF
    coefficients = [{'x_power': u, 'y_power': v, 'coefficient': str(Q(c, NF * NF * scale))}
                    for (u, v), c in sorted(nums.items())]
    result = {'degree': [args.a, args.b, 6], 'variables': 'x=r-6,y=s-6', 'pencil': name,
              'pencil_sha256': hashlib.sha256(raw).hexdigest(), 'rows': selected, 'size': n,
              'grid_points': len(points), 'all_grid_values_reproduced': True, 'coefficients': coefficients,
              'determinant_backend': 'python-flint 0.9.0 exact fmpz_mat.det',
              'interpolation_backend': 'Python integers, exact Newton/Stirling factorial scaling',
              'source_interpolation_module_sha256': hashlib.sha256((ROOT / 'frontier-20261028-level6-minor-polynomial.py').read_bytes()).hexdigest(),
              'scope': 'exact stored pencil minor; actual-source and independent full verification are separate'}
    with out.open('x') as stream:
        json.dump(result, stream, indent=2)
        stream.write('\n')
    print('PASS native exact minor', P['degree'], 'size', n, 'terms', len(coefficients), out.name, flush=True)


if __name__ == '__main__':
    main()
