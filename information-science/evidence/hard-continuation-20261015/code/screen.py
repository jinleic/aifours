#!/usr/bin/env python3
"""Exact quadratic/canonical-spectrum necessary-condition screen; integer only."""
import argparse
from collections import Counter
import gzip
import hashlib
import json
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parents[1]
INPUT_SHA = '200a4997f0a1bcc5c63eaf53f2602118395950ddb951b5bee43c23c92f32cf6d'
VALUES = (2, 6, 10, 14, 18, 22, 26)
MONOMIALS = (0,) + tuple(1 << i for i in range(8)) + tuple((1 << i) | (1 << j) for i in range(8) for j in range(i + 1, 8))


def parity(x):
    return x.bit_count() & 1


def fwht(values):
    a = list(values)
    step = 1
    while step < len(a):
        for start in range(0, len(a), 2 * step):
            for j in range(start, start + step):
                x, y = a[j], a[j + step]
                a[j], a[j + step] = x + y, x - y
        step *= 2
    return a


def points(normal):
    pivot = (normal & -normal).bit_length() - 1
    basis = [(1 << j) ^ ((1 << pivot) if (normal >> j) & 1 else 0) for j in range(9) if j != pivot]
    out = []
    for t in range(256):
        x = 0
        for i, b in enumerate(basis):
            if t >> i & 1:
                x ^= b
        out.append(x)
    return basis, out, 1 << pivot


def quadratic_bit(m):
    return ((m * m - 4) // 32) & 1


def canonical(m):
    return m if m % 8 == 2 else -m


def evaluation_row(b):
    return sum(1 << i for i, monomial in enumerate(MONOMIALS) if b & monomial == monomial)


def nullspace(rows, columns=37):
    # Pivot at the highest set bit.  Reduced rows give every null vector.
    pivots = {}
    for row in rows:
        for p in sorted(pivots, reverse=True):
            if row >> p & 1:
                row ^= pivots[p]
        if row:
            p = row.bit_length() - 1
            for q in pivots:
                if pivots[q] >> p & 1:
                    pivots[q] ^= row
            pivots[p] = row
    basis = []
    for f in range(columns):
        if f in pivots:
            continue
        v = 1 << f
        for p, row in pivots.items():
            if row >> f & 1:
                v |= 1 << p
        basis.append(v)
    return len(pivots), basis


def polynomial(coef):
    return [parity(coef & evaluation_row(b)) for b in range(256)]


def read_input():
    raw = (ROOT / 'inputs/slice-screen.json.gz').read_bytes()
    assert hashlib.sha256(raw).hexdigest() == INPUT_SHA
    data = json.loads(gzip.decompress(raw))
    assert data['total_cases'] == 31744 and data['excluded_cases'] == 31492
    surviving = [r for r in data['cases'] if not r['rejections']]
    assert surviving == data['unresolved_case_records'] and len(surviving) == 252
    return data, surviving


def analyze(data, record):
    source = data['sources'][record['source']]
    basis, pts, origin = points(record['normal'])
    bits = [int(source['bits'][x]) for x in pts]
    G = fwht([1 - 2 * b for b in bits])
    assert sum(bits) % 2 == 1 and max(map(abs, G)) == 26
    caps = [28 - abs(v) for v in G]
    Z = [b for b in range(256) if abs(G[b]) == 26]
    rank, kernel = nullspace([evaluation_row(b) for b in Z])
    candidates = []
    for mask in range(1 << len(kernel)):
        coef = 0
        for i, v in enumerate(kernel):
            if mask >> i & 1:
                coef ^= v
        Q = polynomial(coef)
        assert all(Q[b] == 0 for b in Z)
        domains = [[m for m in VALUES if m <= cap and quadratic_bit(m) == q] for cap, q in zip(caps, Q)]
        rec = {'coefficient_mask': coef}
        if any(not d for d in domains):
            rec['rejected_by'] = 'empty-domain'
            candidates.append(rec)
            continue
        maxima = [max(d) for d in domains]
        S = sum(m * m for m in maxima)
        zeros = [b for b, g in enumerate(G) if abs(g) in domains[b]]
        zero_capacity = max((S - maxima[b] ** 2 + G[b] ** 2 for b in zeros), default=-1)
        rec.update(square_capacity=S, zero_capacity=zero_capacity)
        if zero_capacity < 65536:
            rec['rejected_by'] = 'quadratic-Parseval-zero'
        else:
            # Odd-weight h has AC(d)=4 mod 8 for every nonzero d.
            T = fwht([m * m for m in maxima])
            gaps = [abs((v % 2048) - 1024) for v in T[1:]]
            ac_gap = max(gaps)
            rec.update(ac_max_residue_distance=ac_gap, ac_direction=1 + gaps.index(ac_gap))
            if ac_gap > S - 65536:
                rec['rejected_by'] = 'autocorrelation-residue-energy'
            else:
                K0 = [canonical(m) for m in maxima]
                A = fwht(K0)
                gaps = [abs(abs(v) - 256) for v in A]
                gap = max(gaps)
                rec.update(canonical_max_distance=gap, canonical_input=gaps.index(gap), canonical_energy_L1_bound=(S - 65536) // 4)
                if 4 * gap > S - 65536:
                    rec['rejected_by'] = 'canonical-inverse-energy'
                else:
                    rec['rejected_by'] = None
                    rec['magnitude_domains'] = domains
                    rec['maxima'] = maxima
                    rec['canonical_maximum_inverse'] = A
        candidates.append(rec)
    first_survivors = [c for c in candidates if c['rejected_by'] not in ('empty-domain', 'quadratic-Parseval-zero')]
    second_survivors = [c for c in first_survivors if c['rejected_by'] != 'autocorrelation-residue-energy']
    final_survivors = [c for c in second_survivors if c['rejected_by'] is None]
    stage = 'quadratic-Parseval-zero' if not first_survivors else 'autocorrelation-residue-energy' if not second_survivors else 'canonical-inverse-energy' if not final_survivors else 'UNKNOWN'
    return {'source': record['source'], 'normal': record['normal'], 'basis': basis, 'origin': origin,
            'fixed_bits': ''.join(map(str, bits)), 'G': G, 'kernel_rank': rank, 'kernel_basis': kernel,
            'quadratic_candidates': candidates, 'class_stage': stage}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default='results/screen.json.gz')
    args = parser.parse_args()
    start = time.monotonic()
    data, surviving = read_input()
    classes = [analyze(data, r) for r in surviving]
    # Only literal capacity equality is deduplicated.  Identity coordinate maps
    # cover every listed class; no inequivalence or full EA classification claim.
    groups = {}
    mapping = []
    for i, r in enumerate(classes):
        key = tuple(map(abs, r['G']))
        if key not in groups:
            groups[key] = len(groups)
        mapping.append(groups[key])
    out = {'input_sha256': INPUT_SHA, 'bit_order': 'bits[x]=f(x); x_i=(x>>i)&1',
           'class_count': len(classes), 'stage_counts': dict(Counter(r['class_stage'] for r in classes)),
           'literal_capacity_groups': len(groups), 'identity_spectral_group_for_all_252': mapping,
           'classes': classes, 'elapsed_seconds': time.monotonic() - start}
    payload = (json.dumps(out, separators=(',', ':')) + '\n').encode()
    (ROOT / args.output).write_bytes(gzip.compress(payload, mtime=0))
    print(json.dumps({k: out[k] for k in ('class_count', 'stage_counts', 'literal_capacity_groups', 'elapsed_seconds')}, sort_keys=True))


if __name__ == '__main__':
    main()
