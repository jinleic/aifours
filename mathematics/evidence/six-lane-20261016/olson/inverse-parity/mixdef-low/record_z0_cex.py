#!/usr/bin/env python3
"""Definition-first recheck of the p = 13 counterexample to the plain defect-set rule.

Claim refuted ([F]): "for every interval-feasible theta of a MIX_low word, the defect set
Z0 = {t : bh_t <= 0} of the interval-chain lifts satisfies Phi(Z0) >= 2g + 2".

This script starts from the explicit word, not from the window formulas:
  1. builds the RGR word (code/was_verify.word_of) and checks length, letters, runs,
     and the parameters k, A, B, R, F, H, kappa, g, D, o_F;
  2. evaluates Lemma GR (proof-GR.md Sec. 2, code/gr_window.ach / tau) for all 2^k sign
     vectors z with the word's own reflection values y; reports
       - every proper cyclic interval pattern: Ach(z) misses tau(z) + pZ (interval-feasible),
       - the patterns z that hit (the word is solvable);
  3. raw ordered-product DP (code/was_verify.dp_has) and an independent DP with
     back-pointers that extracts an explicit 2p-letter subword, re-multiplied letter by
     letter in D_{2p} (left convention (v,e)(v',e') = (v + e v', e e'));
  4. recomputes the singleton lifts x_t (the representative of u_t = theta_t/2 outside the
     singleton window, via Ach of the singleton pattern), checks sum x_t = p, recomputes
     bh_t = 2x_t - d_t, Z0 and Phi(Z0) = sum_{Z0} (d_t - bh_t) + 2 m(Z0).
Writes record_z0_cex.json next to this file.
"""
import itertools
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CODE = os.path.normpath(os.path.join(HERE, '..', '..', 'code'))
sys.path.insert(0, CODE)
import was_verify as wv  # noqa: E402
import gr_window as gw  # noqa: E402

p = 13
d = [-1, 1, 1, 1, 1, 3, 3, 3, 1, 1, 1, 1, 1]
x_claim = [-1, 0, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1]
k = len(d)
a = [max(t, 0) for t in d]
b = [1 if t < 0 else 0 for t in d]
R = sum(a) + sum(b)
F = 4 * p - 2 - R
l = [1] * k
for i in range((F - k) // 2):
    l[i % k] += 2
theta = [(2 * xc) % p for xc in x_claim]
out = {'p': p, 'a': a, 'b': b, 'l': l, 'theta': theta}

# 1. the word and its parameters
w = wv.word_of(a, b, l, theta, p)
assert len(w) == 4 * p - 2
assert all((c == 'R' and v in (1, p - 1)) or c == 'F' for c, v in w)
runs = []
for c, v in w:
    if runs and runs[-1][0] == c and (c == 'R' or runs[-1][1] == v):
        runs[-1][2] += 1
    else:
        runs.append([c, v if c == 'F' else None, 1])
if runs[0][0] == runs[-1][0] and len(runs) > 1 and (runs[0][0] == 'R' or runs[0][1] == runs[-1][1]):
    raise SystemExit('cyclic runs merge; representation not as declared')
rot_runs = [r for r in runs if r[0] == 'R']
ref_runs = [r for r in runs if r[0] == 'F']
y = [r[1] for r in ref_runs]
A = sum(1 for c, v in w if c == 'R' and v == 1)
B = sum(1 for c, v in w if c == 'R' and v == p - 1)
H = sum(r[2] // 2 for r in ref_runs)
kappa = p - 1 - H
g = kappa - B
oF = sum(r[2] % 2 for r in ref_runs)
D = A - B
params = {'N': len(w), 'k_rot_runs': len(rot_runs), 'k_ref_runs': len(ref_runs), 'A': A, 'B': B,
          'R': A + B, 'F': len(w) - A - B, 'H': H, 'kappa': kappa, 'g': g, 'o_F': oF, 'D': D,
          'D_formula_2p-k+2g': 2 * p - k + 2 * g, 'y': y}
out['params'] = params
assert len(rot_runs) == k and len(ref_runs) == k and oF == k
assert B >= 1 and A >= B and B < kappa <= k - 1 and k <= p and D == 2 * p - k + 2 * g

# 2. Lemma GR for all sign vectors
def hits(z):
    lo, hi = gw.ach(z, a, b, l, p)
    if lo > hi:
        return False
    tz = gw.tau(z, y, p)
    return any((t - tz) % p == 0 for t in range(lo, hi + 1, 2))

def z_of(P):
    return tuple(1 if t in P else -1 for t in range(k))

interval_hits = []
n_int = 0
for s in range(k):
    for L in range(1, k):
        P = {(s + j) % k for j in range(L)}
        n_int += 1
        if hits(z_of(P)):
            interval_hits.append(sorted(P))
all_hits = []
for z in itertools.product((1, -1), repeat=k):
    if hits(z):
        all_hits.append([t for t in range(k) if z[t] == 1])
out['GR'] = {'proper_intervals_checked': n_int, 'interval_patterns_hit': len(interval_hits),
             'sign_vectors_hit': len(all_hits),
             'smallest_hitting_patterns': sorted(all_hits, key=len)[:8],
             'pattern_1_3_hits': hits(z_of({1, 3}))}

# 3. raw DP and explicit witness
dp = wv.dp_has(w, p)
n2 = 2 * p
# parent[i][state] = (previous state, letter i-1 taken?) ; states (size, e, v)
parent = [dict() for _ in range(len(w) + 1)]
parent[0][(0, 1, 0)] = None
for i, (c, v) in enumerate(w):
    for st in parent[i]:
        if st not in parent[i + 1]:
            parent[i + 1][st] = (st, False)
        sz, e, val = st
        if sz < n2:
            nst = (sz + 1, e if c == 'R' else -e, (val + e * v) % p)
            if nst not in parent[i + 1]:
                parent[i + 1][nst] = (st, True)
witness = None
goal = (n2, 1, 0)
if goal in parent[len(w)]:
    idx = []
    st = goal
    for i in range(len(w), 0, -1):
        prev, took = parent[i][st]
        if took:
            idx.append(i - 1)
        st = prev
    assert st == (0, 1, 0)
    idx.reverse()
    witness = idx
ok_witness = None
if witness is not None:
    v_, e_ = 0, 1
    for j in witness:
        c, v = w[j]
        v_, e_ = (v_ + e_ * v) % p, e_ * (1 if c == 'R' else -1)
    ok_witness = (len(witness) == n2 and len(set(witness)) == n2 and v_ == 0 and e_ == 1)
out['DP'] = {'dp_has': dp, 'witness_positions': witness, 'witness_letters':
             [w[j] for j in witness] if witness else None, 'witness_product_identity': ok_witness}

# 4. singleton lifts, Z0, Phi
inv2 = pow(2, p - 2, p)
x = []
for t in range(k):
    lo, hi = gw.ach(z_of({t}), a, b, l, p)
    # singleton window of u_t is the integer interval [lo/2, hi/2]; the lift is the
    # representative of u_t in [hi/2 + 1, p + lo/2 - 1] (exists iff u_t is outside the window)
    u = (theta[t] * inv2) % p
    top = hi // 2
    rep = top + 1 + ((u - (top + 1)) % p)
    assert rep <= p + lo // 2 - 1, ('u_t in its singleton window', t)
    x.append(rep)
bh = [2 * x[t] - d[t] for t in range(k)]
Z0 = [t for t in range(k) if bh[t] <= 0]
mZ = sum(1 for t in Z0 if (t - 1) % k not in Z0) if len(Z0) < k else 1
Phi = sum(d[t] - bh[t] for t in Z0) + 2 * mZ
out['lifts'] = {'x': x, 'sum_x': sum(x), 'x_matches_claim': x == x_claim, 'bh': bh, 'Z0': Z0,
                'm_Z0': mZ, 'Phi_Z0': Phi, 'two_g_plus_2': 2 * g + 2,
                'Z0_pattern_hits': hits(z_of(set(Z0)))}
with open(os.path.join(HERE, 'record_z0_cex.json'), 'w') as fh:
    json.dump(out, fh, indent=1)
print(json.dumps({'params': params, 'GR': out['GR'], 'DP_has': dp,
                  'witness_ok': ok_witness, 'lifts': out['lifts']}, indent=1))
