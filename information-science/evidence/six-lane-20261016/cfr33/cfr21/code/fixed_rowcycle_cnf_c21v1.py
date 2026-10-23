#!/usr/bin/env python3
"""Cyclic-DM SAT with fixed column actions of length2 or3, or an unpaired base.

encode N K OUT_CNF OUT_META --mu MU [--cycle 2|3] [--fixed F]
       [--canonical-columns] [--unit-anchor] [--plant DMRAW]
encode N K OUT_CNF OUT_META --base [--plant DMRAW]
decode META SOLVER_STDOUT OUT_DMRAW

Rows are0 and, for every primary permutation F, the block
  F(t), mu*F(h^-1(t)), ..., mu^(ell-1)*F(h^-(ell-1)(t)).
The row generator pi advances each ell-block. Thus D[pi(r),h(t)]=mu*D[r,t].
Only ell=2,3 are implemented. One within-block difference suffices; for each
pair of blocks, differences from its first row to ALL rows of the other block
suffice. The remaining differences follow by h, unit multiplication and sign.
Decode nevertheless tests every pair and the actual column-multiset action.

Completeness is for the RESTRICTED pure row action, never all CFRs. A common
column relabelling puts h into F fixed points followed by consecutive ell-cycles.
For ell2, d=F-mu*F(h) is a permutation and d(h)=-mu*d, so F=gcd(mu+1,N) is
forced. For ell3, specify F with F==N mod3 and F<=N/gcd(1-mu,N); at a fixed
column the within-block difference is (1-mu)*F(t), whose range has that size.
For N21,mu4 these possible counts are0,3,6; their union covers this row action.

Gauge: subtract the group-fixed row vector (a,mu*a,...), independently per block,
with a=F(0). This makes each PRIMARY F(0)=0 even if h is free. It does NOT
make the virtual rows zero at column0 when h(0)!=0; the decoder never assumes so.

Optional centralizer normalization: order F on fixed columns; rotate each
nonfixed ell-cycle so its minimum F value is first; order cycles by these minima.
All these are common column permutations commuting with h. They preserve F(0)=0
and every other primary's zero gauge: when h is free the cycle containing0 is
already first and its minimum is0; when h fixes0 the fixed minimum is0. No
comparison among the other entries of an ell3 cycle is imposed (reversal is NOT
in the centralizer). This is exact symmetry reduction, not heuristic pruning.

Optional unit anchor, only if0<F<N and phi(N)>F: some unit value of the first
primary is outside the fixed points. Multiply all entries by its inverse and
permute h-cycles to put it at the first nonfixed point, making it1. Subsequent
centralizer sorting preserves this:1 is the smallest nonzero residue, so its
cycle is first and it is that cycle's minimum. No such anchor is used for F=0.

All files exclusive-create; no child processes. Streamed CNF, calculated count,
<=1000000 clauses,<=64MiB encoded file. Every one-hot difference is linked
forward from its two unique input values; exactly-one makes reverse links
unnecessary. Base mode is only an explicitly labelled generic/planted control.
Library _encode_in_memory(args) regenerates the same CNF into ONE bounded buffer
and returns a read-only memoryview plus metadata, with no CNF files or copies.
"""
import argparse
from collections import Counter
from contextlib import nullcontext
import hashlib
import json
from math import gcd
from pathlib import Path
import sys

CLAUSE_CAP = 1_000_000
BYTE_CAP = 64 * 1024 ** 2


def digest(path):
    with open(path, 'rb') as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()


def read_dm(path):
    return [[int(x) for x in line.split()] for line in Path(path).read_text().splitlines() if line.strip()]


def check_dm(dm, n, k):
    if len(dm) != k or any(len(row) != n or any(type(x) is not int or not 0 <= x < n for x in row) for row in dm):
        raise ValueError('DM dimensions/residues invalid')
    for i in range(k):
        for j in range(i):
            if sorted((dm[i][t] - dm[j][t]) % n for t in range(n)) != list(range(n)):
                raise ValueError('DM difference invalid for rows%d,%d' % (i, j))


def normalized(dm, n):
    return [[(row[t] - dm[0][t] - row[0] + dm[0][0]) % n for t in range(n)] for row in dm]


class _MemoryCnf:
    def __init__(self):
        self.data = bytearray()
        self.hasher = hashlib.sha256()
        self.metadata = None

    def write(self, text):
        data = text.encode('ascii')
        if len(self.data) + len(data) > BYTE_CAP:
            raise ValueError('in-memory CNF byte cap exceeded')
        self.data.extend(data)
        self.hasher.update(data)
        return len(text)


def make_spec(args):
    n, k = args.n, args.k
    if not 3 <= n <= 31 or not 2 <= k <= 7:
        raise ValueError('N/K outside bounded encoder range')
    if args.base:
        if args.mu is not None or args.fixed is not None or args.canonical_columns or args.unit_anchor:
            raise ValueError('base mode has no group/centralizer options')
        m, ell, f, h, pi = k - 1, 1, n, list(range(n)), None
        rows = [{'map': a, 'column': list(range(n)), 'scale': 1} for a in range(m)]
        pairs = [(a, b) for a in range(m) for b in range(a)]
    else:
        ell, mu = args.cycle, args.mu
        if mu is None or not 0 < mu < n or gcd(mu, n) != 1 or pow(mu, ell, n) != 1 or (k - 1) % ell:
            raise ValueError('invalid cyclic row-action parameters')
        m = (k - 1) // ell
        if ell == 2:
            if n % 2 != 1:
                raise ValueError('paired normalization currently requires odd N')
            f = gcd(mu + 1, n)
            if args.fixed is not None and args.fixed != f:
                raise ValueError('involution fixed count is forced by within-pair permutation')
        else:
            if args.fixed is None:
                raise ValueError('cycle3 needs an explicit fixed-column count')
            f = args.fixed
            if not 0 <= f <= n or (n - f) % 3 or f > n // gcd(1 - mu, n):
                raise ValueError('invalid cycle3 fixed-column count')
        h = list(range(n))
        for start in range(f, n, ell):
            for j in range(ell):
                h[start + j] = start + (j + 1) % ell
        powers = [list(range(n))]
        for power in range(1, ell):
            powers.append([h[powers[-1][t]] for t in range(n)])
        rows = []
        for a in range(m):
            for j in range(ell):
                rows.append({'map': a, 'column': powers[(-j) % ell], 'scale': pow(mu, j, n)})
        pairs = [(ell * a, ell * a + 1) for a in range(m)]
        for a in range(m):
            for b in range(a):
                pairs.extend((ell * a, ell * b + j) for j in range(ell))
        pi = [0] + [1 + ell * (r // ell) + (r + 1) % ell for r in range(k - 1)]
        if args.unit_anchor and not (0 < f < n and sum(gcd(x, n) == 1 for x in range(n)) > f):
            raise ValueError('unit-anchor premise0<fixed<N and phi(N)>fixed fails')
    order_pairs = []
    if args.canonical_columns:
        order_pairs.extend((t, t + 1) for t in range(f - 1))
        starts = list(range(f, n, ell))
        for start in starts:
            order_pairs.extend((start, start + j) for j in range(1, ell))
        order_pairs.extend(zip(starts, starts[1:]))
    return {'n': n, 'k': k, 'base': args.base, 'cycle_length': ell,
            'mu': args.mu, 'primary_maps': m, 'fixed_columns': f, 'column_action': h,
            'row_action': pi, 'rows': rows, 'difference_pairs': pairs,
            'primary_zero_gauge': True, 'all_rows_zero_column': args.base or f > 0,
            'canonical_columns': args.canonical_columns, 'order_pairs': order_pairs,
            'unit_anchor': args.unit_anchor}


def encode(args):
    spec = make_spec(args)
    n, m, rows, pairs = args.n, spec['primary_maps'], spec['rows'], spec['difference_pairs']
    invscale = [pow(d['scale'], -1, n) for d in rows]
    planted = None
    if args.plant:
        original = read_dm(args.plant)
        check_dm(original, n, args.k)
        if args.base:
            planted = normalized(original, n)
        else:
            # Columnwise subtraction of the fixed row preserves the action.
            # Only the group-fixed primary shift is allowed for a FREE action;
            # subtracting every virtual row's column0 would break that action.
            planted = [[(original[r][t] - original[0][t]) % n for t in range(n)] for r in range(args.k)]
            ell = spec['cycle_length']
            for a in range(m):
                shift = planted[1 + ell * a][0]
                for j in range(ell):
                    r, delta = 1 + ell * a + j, pow(args.mu, j, n) * shift % n
                    planted[r] = [(x - delta) % n for x in planted[r]]
        for r, d in enumerate(rows):
            primary_row = d['map'] + 1 if args.base else spec['cycle_length'] * d['map'] + 1
            if any(planted[r + 1][t] != d['scale'] * planted[primary_row][d['column'][t]] % n for t in range(n)):
                raise ValueError('plant is not in encoded fixed-column-action form')
        first = planted[1]
        if any(first[a] >= first[b] for a, b in spec['order_pairs']):
            raise ValueError('plant does not have requested centralizer normalization')
        if args.unit_anchor and first[spec['fixed_columns']] != 1:
            raise ValueError('plant does not satisfy unit anchor')
    def X(a, t, v):
        return 1 + a * n * n + t * n + v
    def V(r, t, v):
        return X(rows[r]['map'], rows[r]['column'][t], invscale[r] * v % n)
    def D(p, t, v):
        return 1 + (m + p) * n * n + t * n + v
    nv = (m + len(pairs)) * n * n
    perm_clauses = 2 * n * (1 + n * (n - 1) // 2)
    links = sum(n if rows[r]['map'] == rows[s]['map'] and rows[r]['column'][t] == rows[s]['column'][t]
                else n * n for r, s in pairs for t in range(n))
    nc = (m + len(pairs)) * perm_clauses + links + m + int(args.unit_anchor)
    nc += len(spec['order_pairs']) * n * (n + 1) // 2
    if planted is not None:
        nc += m * n
    if nc > CLAUSE_CAP:
        raise ValueError('CNF clause cap exceeded before file creation')
    emitted, written = 0, 0
    memory = getattr(args, '_memory_sink', None)
    with (nullcontext(memory) if memory is not None else open(args.cnf, 'x')) as f:
        header = 'p cnf %d %d\n' % (nv, nc)
        f.write(header); written += len(header)
        def add(values):
            nonlocal emitted, written
            line = ' '.join(str(x) for x in values) + ' 0\n'
            written += len(line)
            if written > BYTE_CAP:
                raise ValueError('CNF byte cap exceeded; incomplete file retained without metadata')
            f.write(line); emitted += 1
        def one(values):
            add(values)
            for a in range(len(values)):
                for b in range(a):
                    add((-values[a], -values[b]))
        for a in range(m + len(pairs)):
            for t in range(n):
                one([1 + a * n * n + t * n + v for v in range(n)])
            for v in range(n):
                one([1 + a * n * n + t * n + v for t in range(n)])
        for a in range(m):
            add((X(a, 0, 0),))
        if args.unit_anchor:
            add((X(0, spec['fixed_columns'], 1),))
        for a, b in spec['order_pairs']:
            for va in range(n):
                for vb in range(va + 1):
                    add((-X(0, a, va), -X(0, b, vb)))
        if planted is not None:
            for a in range(m):
                r = a + 1 if args.base else spec['cycle_length'] * a + 1
                for t in range(n):
                    add((X(a, t, planted[r][t]),))
        for p, (r, s) in enumerate(pairs):
            dr, ds = rows[r], rows[s]
            for t in range(n):
                if dr['map'] == ds['map'] and dr['column'][t] == ds['column'][t]:
                    for value in range(n):
                        add((-X(dr['map'], dr['column'][t], value),
                             D(p, t, (dr['scale'] - ds['scale']) * value % n)))
                else:
                    for a in range(n):
                        xa = V(r, t, a)
                        for b in range(n):
                            add((-xa, -V(s, t, b), D(p, t, (a - b) % n)))
    if emitted != nc:
        raise AssertionError('streamed CNF header count mismatch')
    spec.update({'variables': nv, 'clauses': nc, 'cnf_bytes': written,
                 'cnf_sha256': memory.hasher.hexdigest() if memory is not None else digest(args.cnf),
                 'encoder_source_sha256': digest(__file__),
                 'planted_control': planted is not None,
                 'plant_source_sha256': digest(args.plant) if args.plant else None,
                 'argv': sys.argv[1:]})
    if memory is not None:
        if len(memory.data) != written:
            raise AssertionError('in-memory CNF byte count mismatch')
        memory.metadata = spec
    else:
        with open(args.meta, 'x') as f:
            json.dump(spec, f, indent=1)
        print(json.dumps({key: spec[key] for key in ('n', 'k', 'base', 'cycle_length', 'fixed_columns', 'variables', 'clauses', 'cnf_sha256', 'planted_control')}))


def _encode_in_memory(args):
    private = argparse.Namespace(**vars(args))
    sink = _MemoryCnf()
    private._memory_sink, private.cnf, private.meta = sink, None, None
    encode(private)
    if sink.metadata is None:
        raise AssertionError('missing in-memory model metadata')
    return memoryview(sink.data).toreadonly(), sink.metadata


def decode(args):
    spec = json.loads(Path(args.meta).read_text())
    if spec['encoder_source_sha256'] != digest(__file__):
        raise ValueError('metadata source pin mismatch')
    n, k, m = spec['n'], spec['k'], spec['primary_maps']
    assignment, statuses = {}, []
    for line in Path(args.solver_output).read_text().splitlines():
        if line.startswith('s '):
            statuses.append(line.strip())
        if line.startswith('v '):
            for token in line.split()[1:]:
                value = int(token)
                if not value:
                    continue
                var, truth = abs(value), value > 0
                if not 1 <= var <= spec['variables'] or (var in assignment and assignment[var] != truth):
                    raise ValueError('out-of-range/conflicting assignment')
                assignment[var] = truth
    if statuses != ['s SATISFIABLE']:
        raise ValueError('not exactly one SATISFIABLE status')
    maps = []
    for a in range(m):
        row = []
        for t in range(n):
            ids = [1 + a * n * n + t * n + v for v in range(n)]
            if any(z not in assignment for z in ids):
                raise ValueError('partial primary assignment')
            values = [v for v, z in enumerate(ids) if assignment[z]]
            if len(values) != 1:
                raise ValueError('primary assignment not one-hot')
            row.append(values[0])
        maps.append(row)
    dm = [[0] * n] + [[d['scale'] * maps[d['map']][d['column'][t]] % n for t in range(n)] for d in spec['rows']]
    check_dm(dm, n, k)
    if any(row[0] for row in maps):
        raise ValueError('primary-zero gauge failed')
    if spec['all_rows_zero_column'] and any(row[0] for row in dm):
        raise ValueError('fixed-column zero gauge failed')
    if not spec['base']:
        pi, h, mu = spec['row_action'], spec['column_action'], spec['mu']
        if any(dm[pi[r]][h[t]] != mu * dm[r][t] % n for r in range(k) for t in range(n)):
            raise ValueError('fixed column-action relation failed')
        columns = Counter(tuple(dm[r][t] for r in range(k)) for t in range(n))
        images = []
        for t in range(n):
            vector = [None] * k
            for r in range(k):
                vector[pi[r]] = mu * dm[r][t] % n
            images.append(tuple(vector))
        if columns != Counter(images):
            raise ValueError('column-multiset invariance failed')
    if any(maps[0][a] >= maps[0][b] for a, b in spec['order_pairs']):
        raise ValueError('centralizer normalization failed')
    if spec['unit_anchor'] and maps[0][spec['fixed_columns']] != 1:
        raise ValueError('unit anchor failed')
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
    enc.add_argument('--cycle', type=int, choices=[2, 3], default=2); enc.add_argument('--fixed', type=int)
    enc.add_argument('--canonical-columns', action='store_true'); enc.add_argument('--unit-anchor', action='store_true')
    enc.add_argument('--plant')
    dec = sub.add_parser('decode')
    dec.add_argument('meta'); dec.add_argument('solver_output'); dec.add_argument('dm')
    args = parser.parse_args()
    if args.command == 'encode':
        encode(args)
    else:
        decode(args)


if __name__ == '__main__':
    main()
