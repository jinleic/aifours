#!/usr/bin/env python3
"""Decode a SAT model of frontier-20261029-support-cnf-v1.py and check it exactly.

1. Re-verify every necessary support condition directly on the decoded words.
2. Report connected components of each cut's residual support (square or not).
3. If every residual line has exactly two entries (zero excess), solve the real
   sign system t_rc + t_rc' + t_r'c + t_r'c' = 1 over F2 for every 2x2 block of
   every cut. If solvable, build the real tensor with coefficients +-1 on E and
   sqrt2 on P (times 1/sqrt72) and verify all three flattenings F F^T = 2 I exactly
   in Z[sqrt2]; that is exactly the AME(4,6) condition.
"""
import argparse
from collections import Counter, defaultdict
import hashlib
import itertools
import json
from pathlib import Path

PAIRS = list(itertools.combinations(range(4), 2))
CUTS = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]
WORDS = list(itertools.product(range(6), repeat=4))


class Fail(ValueError):
    pass


def decode(path):
    true = set()
    for line in path.read_text().splitlines():
        if line.startswith('v '):
            for t in line[2:].split():
                v = int(t)
                if v > 0:
                    true.add(v)
    E = [w for k, w in enumerate(WORDS) if 1 + k in true]
    P = [w for k, w in enumerate(WORDS) if 1297 + k in true]
    return E, P


def check_support(E, P, maxm):
    if set(E) & set(P):
        raise Fail('E and P overlap')
    for i, j in PAIRS:
        cp = Counter((w[i], w[j]) for w in P)
        ce = Counter((w[i], w[j]) for w in E)
        for v in itertools.product(range(6), repeat=2):
            if cp[v] > 1 or (cp[v] == 1 and ce[v]):
                raise Fail('P value not isolated')
            if cp[v] == 0 and not (2 <= ce[v] <= maxm):
                raise Fail(f'E multiplicity {ce[v]} at {(i, j, v)}')
    comps = []
    for rows, cols in CUTS:
        R = defaultdict(set)
        C = defaultdict(set)
        for w in E:
            r = (w[rows[0]], w[rows[1]])
            c = (w[cols[0]], w[cols[1]])
            R[r].add(c)
            C[c].add(r)
        for M in (R, C):
            for x, y in itertools.combinations(M, 2):
                if len(M[x] & M[y]) == 1:
                    raise Fail('unique overlap')
        seen = set()
        shapes = []
        for r0 in R:
            if r0 in seen:
                continue
            rs, cs, stack = {r0}, set(), [('r', r0)]
            while stack:
                kind, x = stack.pop()
                nbrs = R[x] if kind == 'r' else C[x]
                for y in nbrs:
                    if kind == 'r' and y not in cs:
                        cs.add(y)
                        stack.append(('c', y))
                    if kind == 'c' and y not in rs:
                        rs.add(y)
                        stack.append(('r', y))
            seen |= rs
            nnz = sum(len(R[x]) for x in rs)
            shapes.append((len(rs), len(cs), nnz))
        comps.append(sorted(shapes))
    return comps


def solve_f2(rows):
    """rows: list of (bitmask, rhs). Returns solution bitmask or None."""
    piv = {}
    for m, b in rows:
        while m:
            h = m.bit_length() - 1
            if h in piv:
                pm, pb = piv[h]
                m ^= pm
                b ^= pb
            else:
                piv[h] = (m, b)
                break
        else:
            if b:
                return None
    x = 0
    for h in sorted(piv):
        m, b = piv[h]
        val = b ^ (bin((m & ~(1 << h)) & x).count('1') & 1)
        if val:
            x |= 1 << h
    return x


def zmul(a, b):
    return (a[0] * b[0] + 2 * a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def verify_ame(coef):
    for rows, cols in CUTS:
        F = defaultdict(dict)
        for w, v in coef.items():
            F[(w[rows[0]], w[rows[1]])][(w[cols[0]], w[cols[1]])] = v
        keys = list(itertools.product(range(6), repeat=2))
        for r1 in keys:
            for r2 in keys:
                s0 = s1 = 0
                for c, v in F[r1].items():
                    if c in F[r2]:
                        x, y = zmul(v, F[r2][c])
                        s0 += x
                        s1 += y
                if (s0, s1) != ((2 if r1 == r2 else 0), 0):
                    return False
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('model', type=Path)
    ap.add_argument('maxm', type=int)
    ap.add_argument('out', type=Path)
    a = ap.parse_args()
    if a.out.exists():
        raise SystemExit('refusing to overwrite')
    E, P = decode(a.model)
    res = {'model_sha256': hashlib.sha256(a.model.read_bytes()).hexdigest(), 'E': len(E), 'P': len(P),
           'support': len(E) + len(P)}
    comps = check_support(E, P, a.maxm)
    res['cut_components_rows_cols_nnz'] = comps
    res['all_components_square'] = all(r == c for cut in comps for r, c, _ in cut)
    zero_excess = all(nnz == 2 * r for cut in comps for r, c, nnz in cut)
    res['zero_excess'] = zero_excess
    if zero_excess and res['all_components_square']:
        idx = {w: k for k, w in enumerate(sorted(E))}
        eqs = []
        for rows, cols in CUTS:
            R = defaultdict(set)
            for w in E:
                R[(w[rows[0]], w[rows[1]])].add((w[cols[0]], w[cols[1]]))
            done = set()
            for r1 in R:
                if r1 in done:
                    continue
                c1, c2 = sorted(R[r1])
                r2 = next(r for r in R if r != r1 and R[r] == R[r1])
                done |= {r1, r2}
                m = 0
                for r in (r1, r2):
                    for c in (c1, c2):
                        w = [0] * 4
                        w[rows[0]], w[rows[1]] = r
                        w[cols[0]], w[cols[1]] = c
                        m ^= 1 << idx[tuple(w)]
                eqs.append((m, 1))
        x = solve_f2(eqs)
        res['real_sign_system_equations'] = len(eqs)
        res['real_sign_system_solvable'] = x is not None
        if x is not None:
            coef = {w: ((-1 if x >> idx[w] & 1 else 1), 0) for w in E}
            coef.update({w: (0, 1) for w in P})
            ok = verify_ame(coef)
            res['exact_AME_check_FFt_equals_2I_all_cuts'] = ok
            if ok:
                res['tensor_times_sqrt72'] = {'E_plus': sorted(w for w in E if coef[w][0] == 1),
                                              'E_minus': sorted(w for w in E if coef[w][0] == -1),
                                              'P_sqrt2': sorted(P)}
    res['E_words'] = sorted(E)
    res['P_words'] = sorted(P)
    with a.out.open('x') as f:
        f.write(json.dumps(res, indent=1) + '\n')
    print(json.dumps({k: v for k, v in res.items() if k not in ('E_words', 'P_words', 'tensor_times_sqrt72')}))


if __name__ == '__main__':
    main()
