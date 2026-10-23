#!/usr/bin/env python3
"""Exact controls for the candidate zero/Pfaffian and quartic-residue lemmas.

The generated vectors obey the weaker integral Fourier hypotheses, not the
full odd-half hypothesis. They are not balanced NL242 examples or a proof.
"""
import argparse
from collections import Counter
from functools import lru_cache
import hashlib
from itertools import combinations
import json
from pathlib import Path
import random
import time


class Failed(Exception):
    pass


def need(ok, message):
    if not ok:
        raise Failed(message)


def transform(values):
    out = list(values)
    step = 1
    while step < len(out):
        for start in range(0, len(out), 2*step):
            for j in range(start, start+step):
                u, v = out[j], out[j+step]
                out[j], out[j+step] = u+v, u-v
        step *= 2
    return out


def anf(values):
    out = list(values)
    for i in range(8):
        for mask in range(256):
            if mask & (1 << i):
                out[mask] ^= out[mask ^ (1 << i)]
    return out


def rank(rows):
    basis = {}
    for row in rows:
        while row:
            bit = row.bit_length()-1
            if bit in basis:
                row ^= basis[bit]
            else:
                basis[bit] = row
                break
    return len(basis)


def polar(values):
    return tuple(sum((values[(1 << i) ^ (1 << j)] ^ values[1 << i]
                      ^ values[1 << j] ^ values[0]) << j for j in range(8))
                 for i in range(8))


@lru_cache(maxsize=None)
def pfaffian(rows, indices):
    if not indices:
        return 1
    first, rest = indices[0], indices[1:]
    result = 0
    for j in rest:
        if rows[first] & (1 << j):
            result ^= pfaffian(rows, tuple(i for i in rest if i != j))
    return result


def audit_vector(p, corrupt=False):
    need(len(p) == 256 and all(-3 <= v <= 3 for v in p), 'vector domain')
    hp = transform(p)
    need(set(hp) <= {-64, 0, 64}, 'Fourier alphabet')
    D = [v % 2 for v in p]
    need(all(not bit or mask.bit_count() <= 2 for mask, bit in enumerate(anf(D))),
         'D is not quadratic')
    need(all(v % 32 == 0 for v in transform([v*v for v in p])), 'square-transform divisibility')
    for v, d in zip(p, D):
        need(v*v == 4+5*d-4*(v == 0)-8*(abs(v) == 1), 'square decomposition')
    B = polar(D)
    zeros = [a for a, v in enumerate(p) if v == 0]
    xor = 0
    moment = [0]*8
    for a in zeros:
        xor ^= a
        for i in range(8):
            if a & (1 << i):
                moment[i] ^= a
    need(len(zeros) % 2 == 0 and xor == 0, 'zero-set parity/XOR')
    for i in range(8):
        for j in range(8):
            expected = 0 if i == j else pfaffian(B, tuple(k for k in range(8) if k not in (i,j)))
            need((moment[i] >> j) & 1 == expected, 'zero-set second moment')
    E = [((v-d)//2) % 2 for v, d in zip(p, D)]
    coefficients = anf(E)
    need(all(not bit or mask.bit_count() <= 4 for mask, bit in enumerate(coefficients)),
         'next-bit degree')
    for indices in combinations(range(8), 4):
        expected = pfaffian(B, indices)
        if corrupt and indices == (0,1,2,3):
            expected ^= 1
        need(coefficients[sum(1 << i for i in indices)] == expected, 'next-bit Pfaffian coefficient')
    r, z, d = rank(B), len(zeros), sum(D)
    if r <= 4 and z:
        need(z >= 8 and z != 10, 'low-rank zero count')
        if z == 8:
            need(rank([a ^ zeros[0] for a in zeros]) == 3, 'eight zeros are not an affine three-flat')
    if r == 6:
        need(z >= (8 if d == 128 else 4), 'rank-six zero count')
    if r == 8:
        need(z >= (12 if d == 136 else 10), 'rank-eight zero count')
        if z == 10:
            need(d == 120, 'rank-eight ten-zero weight')
    return r, d, z


def vector_controls(number):
    rng = random.Random(20261016)
    yield [0]*256
    for trial in range(number):
        terms = (1, 2, 4, 6)[trial % 4]
        used, p = set(), [0]*256
        for j in range(terms):
            while True:
                u, v = rng.sample(range(1,256), 2)
                support = {u, v, u ^ v}
                if not used.intersection(support):
                    break
            used.update(support)
            b, c = rng.randrange(2), rng.randrange(2)
            sign = 1 if terms == 1 or j < terms//2 else -1
            for a in range(256):
                if ((a & u).bit_count() % 2 == b and (a & v).bit_count() % 2 == c):
                    p[a] += sign
        yield p


def genuine_pair_controls():
    """Actual odd truth tables outside the cap, as suggested by the Opus referee."""
    cases = [
        ('rank8', {0,3,12,15,48,192,240}, {0,1,2,4,8,16,32,64,128,255}, 8, 126),
        ('rank6', {192,65,129}, {0,1,2,4,8,16,32,63}, 6, 140),
    ]
    results = []
    for name, support, flip, expected_rank, expected_zeros in cases:
        g = [int(x in support) for x in range(256)]
        h = [bit ^ int(x in flip) for x,bit in enumerate(g)]
        need(sum(g) % 2 == sum(h) % 2 == 1, 'genuine odd weights')
        G, H = transform([1-2*b for b in g]), transform([1-2*b for b in h])
        K, L = [], []
        for spectrum, canonical in ((G,K),(H,L)):
            for value in spectrum:
                magnitude = abs(value)
                canonical.append(magnitude if magnitude % 8 == 2 else -magnitude)
            need(set(transform(canonical)) <= {-256,256}, 'genuine canonical inverse')
        R = [k-l for k,l in zip(K,L)]
        need(all(r % 8 == 0 for r in R), 'genuine R divisibility')
        r, d, z = audit_vector([value//8 for value in R])
        need((r,z) == (expected_rank,expected_zeros), 'genuine-pair stated rank/zeros')
        cap = max(abs(a)+abs(b) for a,b in zip(G,H))
        need(cap > 28, 'controls must not be misreported as cap-28 examples')
        results.append(dict(name=name, weights=[sum(g),sum(h)], peak_pair_capacity=cap,
                            rank=r, residue_weight=d, zeros=z,
                            scope='Actual Boolean pair, but not a cap-28 or balanced NL242 witness.'))
    return results


def scalar_audit():
    canonical = [-22, -14, -6, 2, 10, 18, 26]
    pairs = [(k,l) for k in canonical for l in canonical if abs(k)+abs(l) <= 28]
    need(len(pairs) == 28, 'canonical pair domain')
    for k, l in pairs:
        S, R = k+l, k-l
        D = ((k*k+l*l-8)//32) % 2
        T = (-1 if D else 1)*S
        need(T*T+8*T == 560-512*(abs(S) in (4,12)), 'S slack identity')
        need(R*R == 256+320*D-256*(R == 0)-512*(abs(R) == 8), 'R slack identity')
        if abs(S) not in (4,12) and abs(R) != 8:
            need((S*R-2*R) % 3 == 0, 'mod-three pointwise identity')
    triples = [(z,c,a) for z in (8,12,14,16) for c in range(9) for a in range(9)
               if z+2*(a+c) <= 16 and (z+2*c) % 8 == 0 and (z+2*(a+c)) % 4 == 0]
    need(triples == [(8,0,0),(8,0,2),(8,0,4),(8,4,0),(12,2,0),(14,1,0),(16,0,0)],
         'rank-four integer triples')
    for z, c, a in triples[3:]:
        gamma = 40*128-6656-64*(a+c)-32*z
        need(a == 0 and (gamma+7168) % 48 != 0, 'a=0 gamma contradiction')
    need(512 % 48 != 0 and 512 % 3 != 0, 'remaining a=0 mean contradiction')
    histograms = [[8,2,0,0,120,108,128,146], [8,4,0,0,120,104,128,148],
                  [8,1,0,3,120,105,128,147]]
    for counts in histograms:
        need(sum(counts) == 512 and sum(n*m*m for n,m in zip(counts, range(0,29,4))) == 2**18,
             'histogram Parseval')
    return {'canonical_pairs':len(pairs), 'triples':triples, 'histograms':histograms}


def fake_audit():
    monomials = {0,4,5,12,17,20,24,32,40,64,65,72,96,128,129,160,192}
    J = [sum((a & m) == m for m in monomials) % 2 for a in range(256)]
    D = [((a & 3) == 3) ^ ((a & 12) == 12) ^ bool(a & 16) for a in range(256)]
    H = [j ^ d for j,d in zip(J,D)]
    cells = {(b,c):[a for a in range(256) if (J[a],H[a]) == (b,c)] for b in (0,1) for c in (0,1)}
    need([len(cells[b,c]) for b,c in ((0,0),(0,1),(1,0),(1,1))] == [48,64,64,80], 'fake cells')
    K, L = [None]*256, [None]*256
    table = [(-22,-6,40),(-22,2,29),(-14,-14,1),(-14,10,1),(-6,-22,32),(-6,10,1),
             (2,-22,25),(2,18,29),(2,26,38),(10,10,7),(18,2,18),(26,2,35)]
    for k,l,count in table:
        cell = cells[((k*k-4)//32)%2, ((l*l-4)//32)%2]
        need(len(cell) >= count, 'fake cell capacity')
        for _ in range(count):
            a = cell.pop(0)
            K[a], L[a] = k,l
    need(all(k is not None for k in K) and all(l is not None for l in L), 'fake assignment')
    need(sum(K) == -256 and sum(L) == 256 and sum(k*k for k in K) == sum(l*l for l in L) == 65536,
         'fake means/Parseval')
    need(rank(polar(J)) == rank(polar(H)) == 6 and rank(polar(D)) == 4 and sum(D) == 128,
         'fake quadratic ranks')
    S, R = [k+l for k,l in zip(K,L)], [k-l for k,l in zip(K,L)]
    need(all(abs(k)+abs(l) <= 28 for k,l in zip(K,L)) and sum(s*r for s,r in zip(S,R)) == 0,
         'fake cap/cross energy')
    need(sum((-1 if d else 1)*s for d,s in zip(D,S)) == -1920, 'fake correlation')
    zeros = [a for a,r in enumerate(R) if r == 0]
    xor = 0
    for a in zeros:
        xor ^= a
    need(zeros == [4,233,234,247,251,252,253,254] and xor == 244, 'fake zero location control')
    need(not set(transform([r//8 for r in R])) <= {-64,0,64}, 'fake unexpectedly has valid Fourier alphabet')
    return {'scalar_fake_is_not_a_witness':True, 'zero_set':zeros, 'zero_xor':xor}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--controls', type=int, default=600)
    parser.add_argument('--corrupt-pfaffian', action='store_true')
    args = parser.parse_args()
    began = time.monotonic()
    counts = Counter()
    zero_counts = []
    for p in vector_controls(args.controls):
        r, d, z = audit_vector(p, corrupt=args.corrupt_pfaffian)
        counts[r] += 1
        zero_counts.append((r,d,z))
    need(set(counts) == {0,2,4,6,8}, 'controls do not cover all even polar ranks')
    result = {'status':'PASS', 'scope':'Exact controls, not a universal proof or a balanced NL242 construction.',
              'candidate_sha256':hashlib.sha256((Path(__file__).parent/'info-odd-pair-codex-attempt.md').read_bytes()).hexdigest(),
              'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'vector_controls':len(zero_counts), 'rank_counts':dict(sorted(counts.items())),
              'vector_generation':'Signed sums of codimension-two affine indicators with disjoint nonzero Fourier supports; equal positive/negative terms except the one-flat controls.',
              'scalar_audit':scalar_audit(), 'fake_audit':fake_audit(),
              'genuine_pair_controls':genuine_pair_controls(),
              'seconds':round(time.monotonic()-began,3)}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    try:
        main()
    except Failed as error:
        raise SystemExit('CHECK FAILED: '+str(error))
