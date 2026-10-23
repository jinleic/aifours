#!/usr/bin/env python3
"""Direct cyclic-DM SAT with a CANONICAL FIXED column involution.

Usage:
 encode N K OUT_CNF OUT_META --mu MU [--unit-anchor] [--plant DMRAW]
 encode N K OUT_CNF OUT_META --base [--plant DMRAW]
 decode META SOLVER_OUTPUT OUT_DMRAW

In paired mode K=1+2q, mu^2=1 in Z_N, N odd. Row0 is zero; pair a is
F_a(t), mu*F_a(h(t)). h has f=gcd(mu+1,N) fixed points0..f-1, followed
by consecutive transpositions. No identity row is assumed. Any model with
row action (0)(1 2)(3 4)... has exactly f fixed columns: the within-pair
permutation d satisfies d(h(t))=-mu*d(t), so h is conjugate to -mu on Z_N.
A common column relabelling puts h in this canonical form, and translation
at a fixed column makes all F_a(0)=0 without changing the pure action.

Each primary F_a is a permutation. Require each F_a-mu*F_a(h) to be a
permutation. For a<b require F_a-F_b and F_a-mu*F_b(h) permutations. The
other differences follow by h and unit multiplication, but decode checks
EVERY row pair directly. No field arithmetic at composite N is used.

Optional --unit-anchor is exact only when phi(N)>f and f<N. A primary
permutation has a unit value at some nonfixed column; permuting/swapping
h's2-cycles and multiplying all rows by its inverse makes F_0(f)=1.
No row order/lex heuristic is assumed. The option rejects if its premise
fails. Base mode provides independent-row controls, without claimed action.

CNF is streamed once with a calculated header and asserted emitted count.
One-hot difference D[t,v] plus X_r[t,a]&X_s[t,b]=>D[t,a-b] is sufficient:
exactly one X value per input forces its exact D value, and D is a permutation.
All files are exclusive creates. Encoder/decoder never invoke native children.
"""
import argparse
import hashlib
import json
from math import gcd
from pathlib import Path
import sys


def digest(path):
    with open(path, 'rb') as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()


def read_dm(path):
    rows = []
    for line in Path(path).read_text().splitlines():
        if line.strip():
            rows.append([int(x) for x in line.split()])
    return rows


def check_dm(dm, n, k):
    if len(dm) != k or any(len(row) != n or any(type(x) is not int or not 0 <= x < n for x in row) for row in dm):
        raise ValueError('DM dimensions/residues invalid')
    for i in range(k):
        for j in range(i):
            if sorted((dm[i][t] - dm[j][t]) % n for t in range(n)) != list(range(n)):
                raise ValueError('DM difference invalid for rows%d,%d' % (i, j))


def norm(dm, n):
    return [[(row[t] - dm[0][t] - row[0] + dm[0][0]) % n for t in range(n)] for row in dm]


def model(n, k, mu, base, unit_anchor):
    if not 3 <= n <= 31 or not 2 <= k <= n:
        raise ValueError('N/K outside bounded encoder range')
    if base:
        if mu is not None or unit_anchor:
            raise ValueError('base mode has no multiplier/unit-anchor option')
        m = k - 1
        h = list(range(n))
        rows = [{'map': a, 'column': list(range(n)), 'scale': 1} for a in range(m)]
        pairs = [(a, b) for a in range(m) for b in range(a)]
        f = None
        pi = None
    else:
        if n % 2 != 1 or k % 2 != 1 or mu is None or not 0 < mu < n or mu * mu % n != 1:
            raise ValueError('paired model needs odd N,K and a residue mu with mu^2=1')
        m = (k - 1) // 2
        f = gcd(mu + 1, n)
        h = list(range(n))
        for t in range(f, n, 2):
            h[t], h[t + 1] = t + 1, t
        rows = []
        for a in range(m):
            rows.extend(({'map': a, 'column': list(range(n)), 'scale': 1},
                         {'map': a, 'column': list(h), 'scale': mu}))
        pairs = [(2 * a, 2 * a + 1) for a in range(m)]
        for a in range(m):
            for b in range(a):
                pairs.extend(((2 * a, 2 * b), (2 * a, 2 * b + 1)))
        pi = [0] + [r + 1 if r % 2 else r - 1 for r in range(1, k)]
        if unit_anchor and not (f < n and sum(gcd(x, n) == 1 for x in range(n)) > f):
            raise ValueError('unit-anchor premise phi(N)>fixed_columns fails')
    return {'n': n, 'k': k, 'mu': mu, 'base': base, 'primary_maps': m, 'column_action': h,
            'fixed_columns': f, 'rows': rows, 'difference_pairs': pairs, 'row_action': pi,
            'unit_anchor': unit_anchor, 'zero_column_gauge': True}


def encode(args):
    spec = model(args.n, args.k, args.mu, args.base, args.unit_anchor)
    n, m, pairs, rows = args.n, spec['primary_maps'], spec['difference_pairs'], spec['rows']
    planted = None
    if args.plant:
        original = read_dm(args.plant)
        check_dm(original, n, args.k)
        planted = norm(original, n)
        for r, desc in enumerate(rows):
            primary_row = desc['map'] + 1 if args.base else 2 * desc['map'] + 1
            if any(planted[r + 1][t] != desc['scale'] * planted[primary_row][desc['column'][t]] % n for t in range(n)):
                raise ValueError('planted DM does not have the encoded paired form')
        if args.unit_anchor and planted[1][spec['fixed_columns']] != 1:
            raise ValueError('planted DM does not satisfy requested unit anchor')
    def X(a, t, v):
        return 1 + a * n * n + t * n + v
    def V(r, t, v):
        d = rows[r]
        return X(d['map'], d['column'][t], pow(d['scale'], -1, n) * v % n)
    def D(p, t, v):
        return 1 + (m + p) * n * n + t * n + v
    nv = (m + len(pairs)) * n * n
    permutation_clauses = 2 * n * (1 + n * (n - 1) // 2)
    links = 0
    for r, s in pairs:
        for t in range(n):
            same = rows[r]['map'] == rows[s]['map'] and rows[r]['column'][t] == rows[s]['column'][t]
            links += n if same else n * n
    nc = (m + len(pairs)) * permutation_clauses + links + m + int(args.unit_anchor)
    if planted is not None:
        nc += m * n
    emitted = 0
    with open(args.cnf, 'x') as f:
        f.write('p cnf %d %d\n' % (nv, nc))
        def add(values):
            nonlocal emitted
            f.write(' '.join(str(x) for x in values) + ' 0\n')
            emitted += 1
        def exactly_one(values):
            add(values)
            for a in range(len(values)):
                for b in range(a):
                    add((-values[a], -values[b]))
        for a in range(m + len(pairs)):
            for t in range(n):
                exactly_one([1 + a * n * n + t * n + v for v in range(n)])
            for v in range(n):
                exactly_one([1 + a * n * n + t * n + v for t in range(n)])
        for a in range(m):
            add((X(a, 0, 0),))
        if args.unit_anchor:
            add((X(0, spec['fixed_columns'], 1),))
        if planted is not None:
            for a in range(m):
                r = a + 1 if args.base else 2 * a + 1
                for t in range(n):
                    add((X(a, t, planted[r][t]),))
        for p, (r, s) in enumerate(pairs):
            dr, ds = rows[r], rows[s]
            for t in range(n):
                if dr['map'] == ds['map'] and dr['column'][t] == ds['column'][t]:
                    for value in range(n):
                        delta = (dr['scale'] - ds['scale']) * value % n
                        add((-X(dr['map'], dr['column'][t], value), D(p, t, delta)))
                else:
                    for a in range(n):
                        xa = V(r, t, a)
                        for b in range(n):
                            add((-xa, -V(s, t, b), D(p, t, (a - b) % n)))
    if emitted != nc:
        raise AssertionError('streamed CNF header count mismatch')
    spec.update({'variables': nv, 'clauses': nc, 'cnf_sha256': digest(args.cnf),
                 'encoder_source_sha256': digest(__file__),
                 'planted_control': planted is not None,
                 'plant_source_sha256': digest(args.plant) if args.plant else None,
                 'argv': sys.argv[1:]})
    with open(args.meta, 'x') as f:
        json.dump(spec, f, indent=1)
    print(json.dumps({key: spec[key] for key in ('n', 'k', 'base', 'variables', 'clauses', 'cnf_sha256', 'planted_control')}))


def decode(args):
    spec = json.loads(Path(args.meta).read_text())
    n, k, m = spec['n'], spec['k'], spec['primary_maps']
    assignment, sat = {}, False
    for line in Path(args.solver_output).read_text().splitlines():
        if line.strip() == 's SATISFIABLE':
            sat = True
        if line.startswith('v '):
            for token in line.split()[1:]:
                value = int(token)
                if not value:
                    continue
                variable, truth = abs(value), value > 0
                if not 1 <= variable <= spec['variables']:
                    raise ValueError('assignment variable out of range')
                if variable in assignment and assignment[variable] != truth:
                    raise ValueError('conflicting assignment')
                assignment[variable] = truth
    if not sat:
        raise ValueError('solver did not report SATISFIABLE')
    maps = []
    for a in range(m):
        row = []
        for t in range(n):
            ids = [1 + a * n * n + t * n + v for v in range(n)]
            if any(z not in assignment for z in ids):
                raise ValueError('partial primary assignment')
            values = [v for v, z in enumerate(ids) if assignment[z]]
            if len(values) != 1:
                raise ValueError('primary assignment is not one-hot')
            row.append(values[0])
        maps.append(row)
    dm = [[0] * n]
    for d in spec['rows']:
        dm.append([d['scale'] * maps[d['map']][d['column'][t]] % n for t in range(n)])
    check_dm(dm, n, k)
    if any(row[0] for row in dm):
        raise ValueError('zero-column gauge failed')
    if not spec['base']:
        columns = {tuple(dm[r][t] for r in range(k)) for t in range(n)}
        acted = {tuple(spec['mu'] * dm[spec['row_action'][r]][t] % n for r in range(k)) for t in range(n)}
        if columns != acted:
            raise ValueError('claimed column-multiset action failed')
    with open(args.dm, 'x') as f:
        for row in dm:
            f.write(' '.join(str(x) for x in row) + '\n')
    print(json.dumps({'status': 'DM-DIRECTLY-VERIFIED', 'n': n, 'k': k,
                      'raw_sha256': digest(args.dm), 'metadata_sha256': digest(args.meta),
                      'solver_output_sha256': digest(args.solver_output),
                      'action_claim': 'column-multiset invariance only' if not spec['base'] else None}))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    enc = sub.add_parser('encode')
    enc.add_argument('n', type=int); enc.add_argument('k', type=int)
    enc.add_argument('cnf'); enc.add_argument('meta')
    mode = enc.add_mutually_exclusive_group(required=True)
    mode.add_argument('--mu', type=int); mode.add_argument('--base', action='store_true')
    enc.add_argument('--unit-anchor', action='store_true'); enc.add_argument('--plant')
    dec = sub.add_parser('decode')
    dec.add_argument('meta'); dec.add_argument('solver_output'); dec.add_argument('dm')
    args = parser.parse_args()
    if args.command == 'encode':
        encode(args)
    else:
        decode(args)


if __name__ == '__main__':
    main()
