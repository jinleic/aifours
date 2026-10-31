#!/usr/bin/env python3
"""Exact bivariate maximal minor of a level-six free-Levi D3 pencil, in parallel.

The minor uses the baseline selected rows, optionally with one slot replaced.
Exact integer fraction-free determinants are evaluated on the unisolvent
triangular grid i+j<=n by a process pool; exact integer Newton differences and
Stirling conversion give the monomial coefficients.  Every grid value is
re-checked against the final polynomial.  Exact computation for review only.
"""
import argparse
import hashlib
import importlib.util
import json
import math
from fractions import Fraction as Q
from multiprocessing import Pool
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load(name, file):
    spec = importlib.util.spec_from_file_location(name, ROOT / file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


al6 = load('al6', 'frontier-20261028-level6-alternate-type-minor-search.py')
h = al6.h
DATA = None


def init(data):
    global DATA
    DATA = data


def det_at(point):
    i, j = point
    return i, j, h.value(DATA, i, j)


def stirling_rows(n):
    """rows[k] = coefficients (low-to-high) of the falling factorial x(x-1)...(x-k+1)."""
    rows = [[1]]
    for k in range(1, n + 1):
        prev = rows[-1]
        nxt = [0] * (k + 1)
        for u, c in enumerate(prev):
            nxt[u] -= (k - 1) * c
            nxt[u + 1] += c
        rows.append(nxt)
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--a', type=int, required=True)
    ap.add_argument('--b', type=int, required=True)
    ap.add_argument('--slot', type=int)
    ap.add_argument('--word')
    ap.add_argument('--rows-file')
    ap.add_argument('--tag', required=True)
    ap.add_argument('--workers', type=int, default=8)
    args = ap.parse_args()
    name = f'frontier-20261028-level6-free-{args.a}{args.b}-pencil-v1.json'
    raw = (ROOT / name).read_bytes()
    P = json.loads(raw)
    out = ROOT / f'frontier-20261028-level6-{args.a}{args.b}6-minor-{args.tag}-v1.json'
    if out.exists():
        raise FileExistsError(out)
    rows = al6.full_rows(P)
    words = P['selected_target_words'][:]
    if args.word is not None:
        assert args.word in rows and args.word not in words
        words[args.slot] = args.word
    if args.rows_file is not None:
        assert args.word is None
        chosen = json.loads((ROOT / args.rows_file).read_text())['rows']
        assert len(chosen) == len(words) == len(set(chosen)) and all(w in rows for w in chosen)
        words = chosen
    data, scale = h.int_rows([rows[w] for w in words])
    n = len(data)
    points = [(i, j) for i in range(n + 1) for j in range(n + 1 - i)]
    with Pool(args.workers, initializer=init, initargs=(data,)) as pool:
        values = {(i, j): v for i, j, v in pool.imap_unordered(det_at, points, chunksize=8)}
    # Newton forward differences on the triangle: first along x, then along y.
    D = {}
    for j in range(n + 1):
        col = [values[i, j] for i in range(n + 1 - j)]
        k = 0
        while col:
            D[k, j] = col[0]
            col = [b - a for a, b in zip(col, col[1:])]
            k += 1
    E = {}
    for i in range(n + 1):
        row = [D[i, j] for j in range(n + 1 - i)]
        k = 0
        while row:
            E[i, k] = row[0]
            row = [b - a for a, b in zip(row, row[1:])]
            k += 1
    st = stirling_rows(n)
    fact = [1] * (n + 1)
    for k in range(1, n + 1):
        fact[k] = fact[k - 1] * k
    NF = fact[n]
    # T[i][v] = sum_j E[i,j] s(j,v) NF/j!
    T = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(n + 1 - i):
            e = E[i, j]
            if e:
                w = e * (NF // fact[j])
                for v, c in enumerate(st[j]):
                    if c:
                        T[i][v] += w * c
    num = {}
    for v in range(n + 1):
        for u in range(n + 1 - v):
            s = 0
            for i in range(u, n + 1):
                c = st[i][u] if u < len(st[i]) else 0
                if c and T[i][v]:
                    s += c * (NF // fact[i]) * T[i][v]
            if s:
                num[u, v] = s
    den = NF * NF
    # integer re-check of every grid value: P(i,j)*den == value*den, Horner in u then v
    for i in range(n + 1):
        inner = [0] * (n + 1)
        for (u, v), s in num.items():
            inner[v] += s * i**u
        for j in range(n + 1 - i):
            z = 0
            for v in range(n, -1, -1):
                z = z * j + inner[v]
            assert z == values[i, j] * den, (i, j)
    coef = {key: Q(s, den * scale) for key, s in num.items()}
    result = {
        'degree': [args.a, args.b, 6], 'variables': 'x=r-6,y=s-6', 'pencil': name,
        'pencil_sha256': hashlib.sha256(raw).hexdigest(), 'rows': words,
        'replaced_slot': args.slot, 'new_word': args.word, 'size': n,
        'grid_points': len(points), 'all_grid_values_reproduced': True,
        'coefficients': [{'x_power': u, 'y_power': v, 'coefficient': str(c)} for (u, v), c in sorted(coef.items())],
        'scope': 'exact free-Levi pencil minor; source identification is a written input',
        'not_formal_or_external_model_review': True,
    }
    out.write_text(json.dumps(result, indent=2) + '\n')
    print('DONE minor', (args.a, args.b, 6), args.tag, 'size', n, 'terms', len(coef), out.name, flush=True)


if __name__ == '__main__':
    main()
