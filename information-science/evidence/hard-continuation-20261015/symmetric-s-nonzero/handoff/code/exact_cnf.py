#!/usr/bin/env python3
"""104-orbit 3-DSBF exact feasibility: full FWHT circuit and nonzero support XOR."""
from pathlib import Path
import argparse
import gzip
import hashlib
import itertools
import json
import time

ROOT = Path(__file__).resolve().parents[1]


def neg(x):
    return not x if isinstance(x, bool) else -x


class CNF:
    def __init__(self, n):
        self.n = n
        self.rows = []
        self.gates = []
        self.cache = {}

    def gate(self, op, a, b):
        if isinstance(a, bool) and isinstance(b, bool):
            return {'xor': a != b, 'and': a and b, 'or': a or b}[op]
        if isinstance(a, bool):
            if op == 'xor': return neg(b) if a else b
            if op == 'and': return b if a else False
            return True if a else b
        if isinstance(b, bool):
            return self.gate(op, b, a)
        if a == b:
            return False if op == 'xor' else a
        if a == -b:
            return False if op == 'and' else True
        a, b = sorted((a, b))
        key = (op, a, b)
        if key in self.cache:
            return self.cache[key]
        self.n += 1
        z = self.n
        first = len(self.rows)
        for av, bv in itertools.product((False, True), repeat=2):
            out = (av != bv) if op == 'xor' else (av and bv) if op == 'and' else (av or bv)
            self.rows.append([neg(a) if av else a, neg(b) if bv else b, z if out else -z])
        self.gates.append({'op': op, 'a': a, 'b': b, 'out': z, 'first_clause': first})
        self.cache[key] = z
        return z

    def require(self, values):
        if True in [v for v in values if isinstance(v, bool)]:
            return
        self.rows.append([v for v in values if not isinstance(v, bool)])


def add(cnf, A, B, subtract=False):
    carry = bool(subtract)
    out, steps = [], []
    for a, oldb in zip(A, B):
        b = neg(oldb) if subtract else oldb
        cin = carry
        middle = cnf.gate('xor', a, b)
        bit = cnf.gate('xor', middle, cin)
        carry = cnf.gate('or', cnf.gate('and', a, b), cnf.gate('and', middle, cin))
        out.append(bit)
        steps.append([a, b, cin, bit, carry])
    return out, {'A': A, 'B': B, 'subtract': subtract, 'out': out, 'steps': steps}


def le(cnf, bits, cutoff):
    lower, equal = False, True
    for j in reversed(range(len(bits))):
        if cutoff >> j & 1:
            lower = cnf.gate('or', lower, cnf.gate('and', equal, neg(bits[j])))
            equal = cnf.gate('and', equal, bits[j])
        else:
            equal = cnf.gate('and', equal, neg(bits[j]))
    return cnf.gate('or', lower, equal)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--bound', type=int, default=28)
    ap.add_argument('--prefix', default='results/3-dsbf-snonzero')
    args = ap.parse_args()
    start = time.monotonic()
    input_raw = (ROOT / 'inputs/orbits.json.gz').read_bytes()
    allmeta = json.loads(gzip.decompress(input_raw))
    cls = allmeta['classes']['3-dsbf']
    orbits = cls['orbits']
    assert len(orbits) == 104
    where = [None] * 512
    for i, orb in enumerate(orbits):
        for x in orb: where[x] = i
    cnf = CNF(104)
    width = 11
    words = [[True] + [where[x] + 1] * (width - 1) for x in range(512)]
    layers = []
    stride = 1
    while stride < 512:
        new = [None] * 512
        adders = []
        for start_at in range(0, 512, stride * 2):
            for j in range(stride):
                left, right = words[start_at + j], words[start_at + stride + j]
                new[start_at + j], plus = add(cnf, left, right)
                new[start_at + stride + j], minus = add(cnf, left, right, True)
                adders += [plus, minus]
        layers.append({'stride': stride, 'adders': adders, 'outputs': new})
        words = new
        stride *= 2
    comparators = []
    requirements = []
    for a in cls['representatives']:
        biased = words[a][:-1] + [neg(words[a][-1])]
        low_cut = -args.bound - 1 + (1 << (width - 1))
        high_cut = args.bound + (1 << (width - 1))
        low = le(cnf, biased, low_cut)
        high = le(cnf, biased, high_cut)
        comparators += [{'bits': biased, 'cutoff': low_cut, 'out': low}, {'bits': biased, 'cutoff': high_cut, 'out': high}]
        requirements += [[neg(low)], [high]]
    sx = []
    for j in range(9):
        v = False
        for i, x in enumerate(cls['orbit_xors']):
            if x >> j & 1:
                v = cnf.gate('xor', v, i + 1)
        sx.append(v)
    requirements += [sx, [-1]]  # f(0)=0 is harmless output complementation.
    for req in requirements:
        cnf.require(req)
    text = f'p cnf {cnf.n} {len(cnf.rows)}\n' + ''.join(' '.join(map(str, row)) + ' 0\n' for row in cnf.rows)
    raw = text.encode()
    prefix = ROOT / args.prefix
    prefix.with_suffix('.cnf').write_bytes(raw)
    prefix.with_suffix('.cnf.gz').write_bytes(gzip.compress(raw, mtime=0))
    meta = {'kind': '3-dsbf', 'orbit_input_sha256': hashlib.sha256(input_raw).hexdigest(), 'bound': args.bound,
            'primary_variables': list(range(1, 105)), 'word_width': width,
            'gates': cnf.gates, 'layers': layers, 'outputs': words, 'comparators': comparators,
            'support_xor_literals': sx, 'requirements': requirements,
            'variables': cnf.n, 'clauses': len(cnf.rows), 'cnf_sha256': hashlib.sha256(raw).hexdigest(),
            'scope': 'All3-DSBF104 orbit assignments with nonzero support XOR, every weight parity, modulo harmless output complement.',
            'elapsed_seconds': time.monotonic() - start}
    payload = (json.dumps(meta, separators=(',', ':')) + '\n').encode()
    prefix.with_suffix('.encoding.json.gz').write_bytes(gzip.compress(payload, mtime=0))
    print(json.dumps({k: meta[k] for k in ['variables', 'clauses', 'cnf_sha256', 'elapsed_seconds']}, sort_keys=True))


if __name__ == '__main__':
    main()
