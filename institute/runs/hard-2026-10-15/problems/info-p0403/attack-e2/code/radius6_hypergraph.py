"""Exact six-flip search using the saturated-coefficient four-hypergraph.

For six flips at |W_g|=28, at most three selected signs may oppose W_g.
Thus every four-subset must have empty common opposing-coefficient mask.
Most admissible fours have XOR zero. Any five distinct points have at
most one XOR-zero four-subset, so every possible six-set has a nonzero-
XOR admissible four anchor. We retain all such anchors, extend them using
the complete hypergraph oracle, then check all six-set Walsh spectra.
No SAT solver or floating-point arithmetic is used.
"""
import argparse
from collections import Counter
import hashlib
import gzip
from itertools import combinations
import json
from pathlib import Path
import time
from seeds import SEEDS, decode, fwht
from extra_seeds import EXTRA_SEEDS

TABLES = dict(SEEDS, **EXTRA_SEEDS)


def build(bits, chunk=7, bound=28):
    W = fwht(bits)
    high = [a for a in range(512) if abs(W[a]) == bound]
    assert high and max(map(abs, W)) <= bound
    if bound == 28:
        assert set(map(abs, W)) == {4, 12, 20, 28}
    bad = []
    columns = [0] * len(high)
    for x in range(512):
        mask = 0
        for j, a in enumerate(high):
            sign = 1 - 2 * (bits[x] ^ (bin(a & x).count('1') & 1))
            if sign * W[a] < 0:
                mask |= 1 << j
                columns[j] |= 1 << x
        bad.append(mask)
    full = (1 << 512) - 1
    tables = []
    for begin in range(0, len(high), chunk):
        row = [full] * (1 << chunk)
        for value in range(1, 1 << chunk):
            low = value & -value
            j = begin + low.bit_length() - 1
            row[value] = row[value ^ low] & (full ^ columns[j]) if j < len(high) else row[value ^ low]
        tables.append(row)
    cmask = (1 << chunk) - 1
    def fourths(common, candidates=full):
        k = 0
        while common and candidates:
            value = common & cmask
            if value:
                candidates &= tables[k][value]
            common >>= chunk
            k += 1
        return candidates
    return W, bad, fourths


def search(name, max_x=510):
    started = time.monotonic()
    bits = decode(TABLES[name])
    W, bad, fourths = build(bits)
    full = (1 << 512) - 1
    upper = [full ^ ((1 << (z + 1)) - 1) for z in range(512)]
    anchors = []
    triples = 0
    zero_xor_fours = 0
    for x in range(min(max_x, 510)):
        for y in range(x + 1, 511):
            common = bad[x] & bad[y]
            for z in range(y + 1, 512):
                triples += 1
                candidates = fourths(common & bad[z], upper[z])
                flat_fourth = x ^ y ^ z
                if candidates & (1 << flat_fourth):
                    zero_xor_fours += 1
                    candidates ^= 1 << flat_fourth
                while candidates:
                    low = candidates & -candidates
                    candidates ^= low
                    anchors.append((x, y, z, low.bit_length() - 1))
                assert len(anchors) < 3000000, 'memory cap: inconclusive'
        if x % 16 == 0:
            print(name, 'x', x, 'triples', triples, 'nonzero-XOR fours', len(anchors),
                  'zero-XOR fours', zero_xor_fours, 'seconds', round(time.monotonic()-started, 3), flush=True)
    if max_x < 510:
        return {'status': 'incomplete feasibility probe', 'triples': triples,
                'nonzero_xor_fours': len(anchors), 'zero_xor_fours': zero_xor_fours}
    assert triples == 22238720
    cache = {}
    def extension(points):
        allowed = full
        for triple in combinations(points, 3):
            if triple not in cache:
                x, y, z = triple
                cache[triple] = fourths(bad[x] & bad[y] & bad[z])
            allowed &= cache[triple]
            if not allowed:
                break
        for x in points:
            allowed &= full ^ (1 << x)
        return allowed
    fives = set()
    for anchor in anchors:
        allowed = extension(anchor)
        while allowed:
            low = allowed & -allowed
            allowed ^= low
            fives.add(tuple(sorted(anchor + (low.bit_length()-1,))))
        assert len(fives) < 1000000, 'memory cap: inconclusive'
    sixes = set()
    for five in sorted(fives):
        allowed = extension(five)
        while allowed:
            low = allowed & -allowed
            allowed ^= low
            sixes.add(tuple(sorted(five + (low.bit_length()-1,))))
        assert len(sixes) < 1000000, 'memory cap: inconclusive'
    survivors = []
    targets = []
    for points in sorted(sixes):
        g = bits.copy()
        for x in points:
            g[x] ^= 1
        wg = fwht(g)
        if max(map(abs, wg)) <= 28:
            zeros = [a for a in range(512) if wg[a] == 0]
            record = {'flips': list(points), 'zero_indices': zeros}
            survivors.append(record)
            if zeros:
                targets.append(record)
    digest = hashlib.sha256()
    for anchor in anchors:
        for x in anchor:
            digest.update(x.to_bytes(2, 'little'))
    out = {'status': 'complete', 'seed': name, 'seed_hex': TABLES[name],
           'radius_exact': 6, 'bound': 28, 'triples_examined': triples,
           'admissible_zero_xor_fours': zero_xor_fours,
           'admissible_nonzero_xor_fours': [list(x) for x in anchors],
           'anchor_sha256_u16le': digest.hexdigest(),
           'admissible_fives_count': len(fives), 'admissible_sixes_count': len(sixes),
           'six_sets_preserving_bound': survivors, 'target_six_sets': targets}
    print(name, 'complete anchors', len(anchors), 'fives', len(fives), 'sixes', len(sixes),
          'bound-preserving', len(survivors), 'zero-bearing', len(targets),
          'seconds', round(time.monotonic()-started, 3), flush=True)
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--seed', choices=TABLES, default='dsbf40')
    p.add_argument('--max-x', type=int, default=510)
    p.add_argument('--compare', action='store_true')
    p.add_argument('--output')
    a = p.parse_args()
    out = search(a.seed, a.max_x)
    if a.output:
        path = Path(a.output)
        def read():
            if str(path).endswith('.gz'):
                with gzip.open(path, 'rt') as fh:
                    return json.load(fh)
            return json.loads(path.read_text())
        if a.compare:
            assert read() == out
        else:
            data = (json.dumps(out, separators=(',', ':')) + '\n').encode()
            path.write_bytes(gzip.compress(data, mtime=0) if str(path).endswith('.gz') else data)


if __name__ == '__main__':
    main()
