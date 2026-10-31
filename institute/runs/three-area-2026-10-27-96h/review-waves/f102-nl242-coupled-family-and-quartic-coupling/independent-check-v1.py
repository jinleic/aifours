#!/usr/bin/env python3
# Independent exact finite controls; observed clock before script creation: 2026-10-28T19:08:59-0700 PDT
import hashlib
import itertools
import json
import random
import subprocess
from collections import Counter
from functools import reduce
from operator import xor
from pathlib import Path

ROOT = Path('/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f102-nl242-coupled-family-and-quartic-coupling')
PLACEMENT = Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/balanced-nl242/frontier-20261028-four-zero-coupled-placement-result.json')
PLACEMENT_SHA = 'ba99cc035f8cc8bbbcb9edfc99d9068263e93bdb93dfa9e368b2219f1e223c0f'
rng = random.Random(20261028)


def parity(x):
    return x.bit_count() & 1


def rank(rows):
    pivots = {}
    for row in rows:
        while row:
            i = row.bit_length() - 1
            if i in pivots:
                row ^= pivots[i]
            else:
                pivots[i] = row
                break
    return len(pivots)


def polar(table, u, v):
    return table[u ^ v] ^ table[u] ^ table[v] ^ table[0]


def polar_rank(table, n):
    rows = [sum(polar(table, 1 << i, 1 << j) << j for j in range(n)) for i in range(n)]
    return rank(rows)


def pfaffian(table, vs):
    a, b, c, d = vs
    return ((polar(table, a, b) & polar(table, c, d)) ^
            (polar(table, a, c) & polar(table, b, d)) ^
            (polar(table, a, d) & polar(table, b, c)))


def span(vs):
    out = [0]
    for v in vs:
        out += [x ^ v for x in out]
    return out


def fwht(values):
    out = list(values)
    width = 1
    while width < len(out):
        for left in range(0, len(out), 2 * width):
            for i in range(left, left + width):
                a, b = out[i], out[i + width]
                out[i], out[i + width] = a + b, a - b
        width *= 2
    return out


def anf_degree(table, n):
    co = list(table)
    for i in range(n):
        for x in range(1 << n):
            if x & (1 << i):
                co[x] ^= co[x ^ (1 << i)]
    return max((i.bit_count() for i, c in enumerate(co) if c), default=-1)


def independent_vectors(n, count):
    out = []
    while len(out) < count:
        v = rng.randrange(1, 1 << n)
        if rank(out + [v]) == len(out) + 1:
            out.append(v)
    return out


# Exhaust every affine quadratic function on F_2^4, not just q(0)=0.
mons4 = [0] + [1 << i for i in range(4)] + [(1 << i) | (1 << j) for i, j in itertools.combinations(range(4), 2)]
rank_weights = Counter()
for mask in range(1 << len(mons4)):
    terms = [m for i, m in enumerate(mons4) if (mask >> i) & 1]
    table = [sum((x & m) == m for m in terms) & 1 for x in range(16)]
    r = polar_rank(table, 4)
    weight = sum(table)
    assert weight in {0: {0, 8, 16}, 2: {4, 8, 12}, 4: {6, 10}}[r]
    assert weight % 4 == (2 if r == 4 else 0)
    assert pfaffian(table, [1, 2, 4, 8]) == (r == 4)
    rank_weights[(r, weight)] += 1
assert sum(rank_weights.values()) == 2048

# Sample 125 independently randomized eight-variable symplectic forms and
# their Pfaffian quartics.  Check every coordinate-direction affine 4-flat,
# as well as non-coordinate directions, by evaluating truth tables.
coordinate_flats = []
for axes in itertools.combinations(range(8), 4):
    dirs = [1 << i for i in axes]
    free = [1 << i for i in range(8) if i not in axes]
    coordinate_flats.append((dirs, span(dirs), span(free)))
low_masks = [m for m in range(256) if m.bit_count() <= 3]
samples_by_rank = Counter()
coordinate_checks = 0
random_checks = 0
observed_z = {str(r): Counter() for r in range(0, 9, 2)}
for r in range(5):
    for _ in range(25):
        rows = independent_vectors(8, 8)
        pairs = list(zip(rows[:2*r:2], rows[1:2*r:2]))
        linear = rng.randrange(256)
        lower = [m for m in low_masks if rng.getrandbits(1)]
        q, p = [], []
        for x in range(256):
            active_pairs = sum(parity(a & x) * parity(b & x) for a, b in pairs)
            q.append((active_pairs + parity(linear & x)) & 1)
            lower_value = sum((x & m) == m for m in lower) & 1
            p.append(((active_pairs * (active_pairs - 1) // 2) & 1) ^ lower_value)
        actual_rank = polar_rank(q, 8)
        assert actual_rank == 2*r and q[0] == 0
        z = 256 - sum(q)
        observed_z[str(actual_rank)][z] += 1
        assert (z in (120, 136)) == (actual_rank == 8)
        expected_degree = 4 if r >= 2 else 3
        degree = anf_degree(p, 8)
        assert degree == 4 if r >= 2 else degree <= expected_degree
        assert sum(p) % 4 == (2 if r == 4 else 0)
        for dirs, offsets, bases in coordinate_flats:
            expected = pfaffian(q, dirs)
            for base in bases:
                assert (sum(p[base ^ d] for d in offsets) & 1) == expected
                coordinate_checks += 1
        for _ in range(32):
            dirs = independent_vectors(8, 4)
            base = rng.randrange(256)
            assert (sum(p[base ^ d] for d in span(dirs)) & 1) == pfaffian(q, dirs)
            random_checks += 1
        samples_by_rank[actual_rank] += 1
assert coordinate_checks == 140000 and random_checks == 4000

# A rogue quartic on rank-zero q must fail the Pfaffian derivative check.
qzero = [0] * 256
mutant = [int((x & 15) == 15) for x in range(256)]
mutation_parity = sum(mutant[x] for x in span([1, 2, 4, 8])) & 1
assert mutation_parity == 1 and pfaffian(qzero, [1, 2, 4, 8]) == 0

# Verify the pinned formal k directly, without importing the author's code.
raw = PLACEMENT.read_bytes()
assert hashlib.sha256(raw).hexdigest() == PLACEMENT_SHA
placement = json.loads(raw)
k = placement['spectrum_k']
assert len(k) == 512 and all(type(v) is int and abs(v) <= 7 for v in k)
qfamily = lambda x: (((x >> 0) & 1) & ((x >> 1) & 1)) ^ (((x >> 2) & 1) & ((x >> 3) & 1)) ^ (((x >> 4) & 1) & ((x >> 5) & 1))
pfamily = lambda x: 1 - int(((x >> 0) & 1) == 1 and ((x >> 2) & 1) == 0 and ((x >> 4) & 1) == 0)
for x in range(256):
    assert k[x] % 2 == 0 and (k[x] // 2) % 2 == qfamily(x)
    assert k[x + 256] % 2 == 1 and int(abs(k[x + 256]) in (1, 7)) == pfamily(x)
flat = [a for a in range(512) if (a & 195) == 195]
even_q1 = sum(qfamily(a) for a in flat if a < 256)
odd_p0 = sum(1 - pfamily(a & 255) for a in flat if a >= 256)
energy = sum(k[a] ** 2 for a in flat)
assert (len(flat), even_q1, odd_p0, energy, energy % 16) == (32, 10, 4, 984, 8)
mutated_k = list(k)
mutated_index = next(a for a in flat if a >= 256 and abs(k[a]) in (1, 7))
mutated_k[mutated_index] = 3
mutated_energy = sum(mutated_k[a] ** 2 for a in flat)
assert mutated_energy % 16 == 0 and int(abs(mutated_k[mutated_index]) in (1, 7)) != pfamily(mutated_index & 255)
qtable = [qfamily(x) for x in range(256)]
ptable = [pfamily(x) for x in range(256)]
assert polar_rank(qtable, 8) == 6 and anf_degree(ptable, 8) == 3
assert pfaffian(qtable, [1, 2, 4, 8]) == 1
assert sum(ptable[x] for x in range(16)) % 2 == 0
inverse = fwht(k)
inverse_nonsign = sum(abs(v) != 128 for v in inverse)
autocorr_nz = sum(sum(k[a] * k[a ^ b] for a in range(512)) != 0 for b in range(1, 512))
assert (inverse_nonsign, autocorr_nz) == (507, 508)

# A different, explicitly constructed balanced NL240 Boolean function is a
# genuine positive control for every one of the 16 frequency cosets of U.
ones = [x for x in range(512) if (((x >> 8) & 1) ^ (sum(((x >> (2*i)) & 1) * ((x >> (2*i+1)) & 1) for i in range(4)) & 1))]
assert len(ones) == 256 and reduce(xor, ones, 0) == 0
one_set = set(ones)
signs = [1 - 2 * (x in one_set) for x in range(512)]
walsh = fwht(signs)
assert walsh[0] == 0 and max(map(abs, walsh)) == 32 and all(w % 4 == 0 for w in walsh)
true_k = [w // 4 for w in walsh]
uaxes = [1, 2, 64, 128]
complement = [4, 8, 16, 32, 256]
uspace, representatives = span(uaxes), span(complement)
coset_energies = []
for lam in span(uaxes):
    frequencies = [a for a in range(512) if (a & 195) == lam]
    vs = [sum(signs[c ^ u] * (1 - 2 * parity(lam & u)) for u in uspace) for c in representatives]
    lhs = sum(walsh[a] ** 2 for a in frequencies)
    kval = sum(true_k[a] ** 2 for a in frequencies)
    assert all(v % 2 == 0 for v in vs)
    assert lhs == 32 * sum(v*v for v in vs) and kval == 2 * sum(v*v for v in vs)
    assert kval % 16 == 0
    coset_energies.append(kval)

# Rebuild the even-half quadratic directly from one-support parity counts on
# arbitrary balanced tables, including the above T=0 case; no peak bound used.
q_reconstructions = Counter()
for M in [ones] + [rng.sample(range(512), 256) for _ in range(5)]:
    T = reduce(xor, M, 0)
    signs = [1 - 2 * (x in set(M)) for x in range(512)]
    W = fwht(signs)
    kvals = [w // 4 for w in W]
    assert all(w % 4 == 0 for w in W)
    assert all((kvals[a] & 1) == parity(a & T) for a in range(512))
    expected_dim = 9 if T == 0 else 8
    basis = []
    for a in range(1, 512):
        if parity(a & T) == 0 and rank(basis + [a]) == len(basis) + 1:
            basis.append(a)
        if len(basis) == expected_dim:
            break
    assert len(basis) == expected_dim
    evals = [[parity(b & x) for x in M] for b in basis]
    assert all(sum(row) % 2 == 0 for row in evals)
    linear = [(sum(row) // 2) % 2 for row in evals]
    quadratic = {(i, j): sum(a*b for a, b in zip(evals[i], evals[j])) % 2 for i, j in itertools.combinations(range(expected_dim), 2)}
    for selection in range(1 << expected_dim):
        a = reduce(xor, (basis[i] for i in range(expected_dim) if (selection >> i) & 1), 0)
        predicted = sum(linear[i] for i in range(expected_dim) if (selection >> i) & 1)
        predicted += sum(c for (i, j), c in quadratic.items() if (selection >> i) & 1 and (selection >> j) & 1)
        assert (kvals[a] // 2) % 2 == predicted % 2
    q_reconstructions['T_zero' if T == 0 else 'T_nonzero'] += 1
assert q_reconstructions['T_zero'] >= 1 and q_reconstructions['T_nonzero'] >= 1

receipt = {
    'schema_version': 1,
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'placement_sha256': PLACEMENT_SHA,
    'seed': 20261028,
    'four_variable_quadratics_exhausted': sum(rank_weights.values()),
    'four_variable_rank_weight_counts': {f'{r}:{w}': c for (r, w), c in sorted(rank_weights.items())},
    'eight_variable_samples_by_rank': {str(k): v for k, v in sorted(samples_by_rank.items())},
    'eight_variable_observed_q_zero_counts': {r: dict(sorted(counts.items())) for r, counts in observed_z.items()},
    'coordinate_affine_4flat_checks': coordinate_checks,
    'noncoordinate_affine_4flat_checks': random_checks,
    'quartic_mutation_derivative': mutation_parity,
    'placement': {'size': len(k), 'even_q1': even_q1, 'odd_p0': odd_p0, 'flat_energy': energy,
                  'flat_energy_mod16': energy % 16, 'mutated_index': mutated_index,
                  'mutated_flat_energy': mutated_energy, 'polar_rank': polar_rank(qtable, 8),
                  'indicator_degree': anf_degree(ptable, 8), 'pfaffian_0123': 1,
                  'indicator_0123_derivative': 0, 'inverse_nonsign': inverse_nonsign,
                  'nonzero_shift_autocorrelations': autocorr_nz},
    'genuine_balanced_control': {'ones': len(ones), 'peak': 32, 'nonlinearity': 240,
                                  'cosets_verified': len(coset_energies), 'k_energies': coset_energies},
    'balanced_truth_table_q_reconstructions': dict(q_reconstructions),
    'scope': 'Finite controls only; no four-zero exclusion or witness follows.'
}
receipt['observed_clock_before_creation'] = subprocess.check_output(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], text=True).strip()
with (ROOT / 'independent-check-v1.json').open('x', encoding='utf-8') as out:
    json.dump(receipt, out, indent=2, sort_keys=True)
    out.write('\n')
print(json.dumps(receipt, indent=2, sort_keys=True))
