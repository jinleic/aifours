"""Exact verification of the IL counterexample found by il_check.py (p = 11)."""
import sys, os
sys.path.insert(0, '..')
from hw import dp_has, word_of, hw_avoids
from scl_closure import tables
from il_check import gap_rep
p = 11
a = [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1]
b = [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0]
l = [1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1]
phi = [1, 1, 1, 1, 1, 1, 0, 4, 5, 1, 1, 4, 5, 1, 4, 7, 1, 4, 1]
k = len(a); A, B = sum(a), sum(b); H = sum(x // 2 for x in l); kappa = p - 1 - H
print('k', k, 'A', A, 'B', B, 'R', A + B, 'F', sum(l), 'N', A + B + sum(l), 'kappa', kappa, 'kappa_B', kappa - B,
      'all l odd', all(x % 2 for x in l), 'sum phi mod p', sum(phi) % p)
U, L = tables(a, b, l, p); full = (1 << k) - 1
print('any full window:', any(U[P] + L[P] + 1 >= p for P in range(1, full)))
ivals = [sum(1 << ((i + j) % k) for j in range(ln)) for i in range(k) for ln in range(1, k)]
hit = [Q for Q in ivals if (lambda lo, hi, s: lo <= hi and (s - lo) % p <= hi - lo)(-L[Q], U[Q], sum(phi[t] for t in range(k) if (Q >> t) & 1) % p)]
print('interval windows hit:', len(hit), '(0 = interval-feasible); P=empty ok (B <= kappa):', B <= kappa)
x = [gap_rep(U, L, 1 << t, phi[t], p) for t in range(k)]
print('canonical singleton lifts', x, 'sum', sum(x), '= %d p' % (sum(x) // p))
bad = [(Q, gap_rep(U, L, Q, sum(phi[t] for t in range(k) if (Q >> t) & 1) % p, p), sum(x[t] for t in range(k) if (Q >> t) & 1)) for Q in ivals]
bad = [z for z in bad if z[1] != z[2]]
print('intervals with lift != sum of canonical lifts:', len(bad), 'shortest:', min(bad, key=lambda z: bin(z[0]).count('1')) if bad else None)
# reflection values y realising phi: phi_t = (y_{t-1} - y_t)/2, y_{k-1} = 0
inv2 = (p + 1) // 2
y = [0] * k; prev = 0
for t in range(k):
    y[t] = (prev - 2 * phi[t]) % p; prev = y[t]
print('y consistent (y_{k-1} = 0):', y[-1] == 0)
w = word_of(a, b, l, y, p)
print('raw DP: word has an identity 2p-subword:', dp_has(w, p), '| HW avoids:', hw_avoids(a, b, l, y, p))
kills = [P for P in range(1, full) if (lambda lo, hi, s: lo <= hi and (s - lo) % p <= hi - lo)(-L[P], U[P], sum(phi[t] for t in range(k) if (P >> t) & 1) % p)]
def comps(P):
    return sum(1 for j in range(k) if (P >> j) & 1 and not (P >> ((j - 1) % k)) & 1)
best = min(kills, key=lambda P: (comps(P), bin(P).count('1'))) if kills else None
print('number of killed patterns:', len(kills), '; a kill with fewest intervals:', [t for t in range(k) if best and (best >> t) & 1], 'm =', comps(best) if best else None)
