#!/usr/bin/env python3
"""rv163 reviewer-authored structural / exact-rank control (independent of all author code).

Reviewer's own reduction (derived in review-v1.md, section 3.2): for flat Z_m^2-diagonal vectors
psi_q(x)_j = zeta_m^{<c_j,x>} e^{i phi_{q,j}} / sqrt(2m) with the Theorem-B incidence
(AB: A_s B_t, AC: A_s C_{s+t}, BC: B_t C_{s+t}):
  * within-quadrant orthogonality  <=>  beta, alpha, alpha-beta each take every value of Z_m exactly twice;
  * cross-quadrant orthogonality   <=>  by Fourier inversion on Z_m, for every pair {j,k} sharing
        beta:        a_j - a_k = pi,  a = phi_AC - phi_AB
        alpha:       b_j - b_k = pi,  b = phi_BC - phi_AB
        alpha-beta:  (b-a)_j - (b-a)_k = pi                         (all mod 2 pi).
  Solvable iff every vector of a Z-basis of the integer left kernel of the equation matrix has even
  coordinate sum (RHS = pi in every row).  Reviewer's graph form: the left kernel has one generator per
  bipartite component C of the union of the three pairings, with coordinate sum = |C|*3/2 (mod 2), so the
  system is inconsistent iff some bipartite component has |C| = 2 mod 4.
This script (i) computes the Z-basis by unimodular integer row reduction and compares with the graph
criterion, (ii) enumerates ALL admissible character multisets for m = 3 (expect: all inconsistent,
an ansatz-restricted sanity control for Theorem A), (iii) checks m = 5 / m = 7 candidate data and the
QLS(10) data satisfy their pairing congruences exactly, (iv) runs an m = 5 negative control.
Run: /usr/bin/python3 -B rv163-flat-torus-parity-v1.py   (writes rv163-flat-torus-parity-v1.json)
"""
import hashlib
import itertools
import json
import subprocess
import sys
from pathlib import Path

SELF = Path(__file__).resolve()
OUT = SELF.parent / 'rv163-flat-torus-parity-v1.json'


def native_clock():
    return subprocess.run(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], capture_output=True,
                          text=True, check=True).stdout.strip()


CLOCK_START = native_clock()
FAILS = []


def require(c, msg):
    if not c:
        FAILS.append(msg)


def left_kernel_Z(M):
    E, n = len(M), len(M[0])
    A = [list(M[i]) + [1 if j == i else 0 for j in range(E)] for i in range(E)]
    row = 0
    for col in range(n):
        while True:
            nz = [r for r in range(row, E) if A[r][col] != 0]
            if not nz:
                break
            r0 = min(nz, key=lambda r: abs(A[r][col]))
            A[row], A[r0] = A[r0], A[row]
            clean = True
            for r in range(row + 1, E):
                if A[r][col] != 0:
                    f = A[r][col] // A[row][col]
                    A[r] = [x - f * y for x, y in zip(A[r], A[row])]
                    if A[r][col] != 0:
                        clean = False
            if clean:
                break
        if row < E and A[row][col] != 0:
            row += 1
        if row == E:
            break
    assert all(all(x == 0 for x in A[r][:n]) for r in range(row, E))
    K = [A[r][n:] for r in range(row, E)]
    for y in K:   # verify y^T M = 0 exactly
        assert all(sum(y[i] * M[i][c] for i in range(E)) == 0 for c in range(n))
    return row, K


def pairings(T, m):
    out = {}
    for name, f in (('alpha', lambda c: c[0]), ('beta', lambda c: c[1]), ('gamma', lambda c: c[0] - c[1])):
        pr = []
        for v in range(m):
            idx = [j for j, c in enumerate(T) if f(c) % m == v]
            if len(idx) != 2:
                return None
            pr.append(tuple(idx))
        out[name] = pr
    return out


def core_system(T, m):
    n = 2 * m
    pa = pairings(T, m)
    rows = []
    for (j, k) in pa['beta']:
        r = [0] * (2 * n)
        r[j] += 1
        r[k] -= 1
        rows.append(r)
    for (j, k) in pa['alpha']:
        r = [0] * (2 * n)
        r[n + j] += 1
        r[n + k] -= 1
        rows.append(r)
    for (j, k) in pa['gamma']:
        r = [0] * (2 * n)
        r[n + j] += 1
        r[j] -= 1
        r[n + k] -= 1
        r[k] += 1
        rows.append(r)
    return pa, rows


def graph_criterion(pa, n):
    adj = {v: [] for v in range(n)}
    for name in ('alpha', 'beta', 'gamma'):
        for j, k in pa[name]:
            adj[j].append(k)
            adj[k].append(j)
    color, comps = {}, []
    for s in range(n):
        if s in color:
            continue
        color[s] = 0
        stack, comp, bip = [s], [s], True
        while stack:
            v = stack.pop()
            for w in adj[v]:
                if w not in color:
                    color[w] = 1 - color[v]
                    stack.append(w)
                    comp.append(w)
                elif color[w] == color[v]:
                    bip = False
        comps.append((len(comp), bip))
    kernel_dim = sum(1 for sz, b in comps if b)
    obstructed = any(b and sz % 4 == 2 for sz, b in comps)
    return comps, kernel_dim, obstructed


def analyse(T, m):
    pa, M = core_system(T, m)
    rank, K = left_kernel_Z(M)
    odd = [y for y in K if sum(y) % 2 != 0]
    comps, kd, obs = graph_criterion(pa, 2 * m)
    return {'rank': rank, 'left_kernel_dim': len(K), 'odd_sum_generators': len(odd),
            'solvable': len(odd) == 0, 'graph_components_(size,bipartite)': comps,
            'graph_kernel_dim': kd, 'graph_obstructed': obs,
            'criteria_agree': (len(K) == kd) and ((len(odd) > 0) == obs)}


def check_phases(T, m, N, PH):
    """exact congruences of the candidate phases (units 2pi/N): pair differences must be N/2 mod N."""
    pa = pairings(T, m)
    a = [(PH[1][j] - PH[0][j]) for j in range(2 * m)]
    b = [(PH[2][j] - PH[0][j]) for j in range(2 * m)]
    c = [b[j] - a[j] for j in range(2 * m)]
    half = N // 2
    ok = {'beta_on_AC-AB': all((a[j] - a[k]) % N == half for j, k in pa['beta']),
          'alpha_on_BC-AB': all((b[j] - b[k]) % N == half for j, k in pa['alpha']),
          'gamma_on_BC-AC': all((c[j] - c[k]) % N == half for j, k in pa['gamma'])}
    return ok


def check_qls_phases(T, m, N, PH):
    pa = pairings(T, m)
    half = N // 2
    d = lambda p, q: [PH[p][j] - PH[q][j] for j in range(2 * m)]
    sysm = {'R0_rows_beta_on_Q01-Q00': ('beta', d(1, 0)), 'C0_cols_alpha_on_Q10-Q00': ('alpha', d(2, 0)),
            'R1_rows_beta_on_Q11-Q10': ('beta', d(3, 2)), 'C1_cols_alpha_on_Q11-Q01': ('alpha', d(3, 1)),
            'T1_labels_gamma_on_Q10-Q01': ('gamma', d(2, 1))}
    return {k: all((v[j] - v[kk]) % N == half for j, kk in pa[p]) for k, (p, v) in sysm.items()}


res = {'interpreter': sys.version.split()[0]}
# (ii) m = 3: all admissible multisets
pts3 = [(a, b) for a in range(3) for b in range(3)]
adm = []
for combo in itertools.combinations_with_replacement(range(9), 6):
    T = [pts3[i] for i in combo]
    if pairings(T, 3) is not None:
        adm.append(T)
m3 = [analyse(T, 3) for T in adm]
res['m3_admissible_multisets'] = len(adm)
res['m3_admissible_with_distinct_characters'] = sum(1 for T in adm if len(set(T)) == 6)
res['m3_solvable_count'] = sum(1 for r in m3 if r['solvable'])
res['m3_criteria_agree_all'] = all(r['criteria_agree'] for r in m3)
res['m3_examples'] = [{'T': T, **r} for T, r in list(zip(adm, m3))[:3]]
res['m3_distinct_examples'] = [{'T': T, **r} for T, r in zip(adm, m3) if len(set(T)) == 6]
require(res['m3_solvable_count'] == 0, 'some m=3 flat system solvable (would contradict Theorem A)')
require(res['m3_criteria_agree_all'], 'graph criterion disagrees with Z-kernel')

T5 = [(0, 0), (0, 1), (1, 0), (1, 3), (2, 2), (2, 4), (3, 1), (3, 4), (4, 2), (4, 3)]
PH5 = [[-35, -25, -25, -15, -20, -10, -15, -5, -10, 0], [-10, -10, -10, -5, 0, 5, -10, 0, 0, 0], [0] * 10]
T7 = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 3), (2, 5), (3, 5), (3, 6), (4, 2), (4, 6), (5, 2), (5, 4),
      (6, 3), (6, 4)]
PH7 = [[-63, -49, -14, 0, -84, -70, -56, -42, -42, -28, -28, -14, -14, 0],
       [-49, -70, -14, -35, -56, -14, -14, 0, -14, 0, -14, 0, 0, 0], [0] * 14]
PHH = [[-65, -40, -40, -25, -25, -15, -20, -10, -10, 0], [-40, -30, -25, -15, -15, -5, -20, -10, -10, 0],
       [-25, -10, -15, -10, -10, -10, 0, 0, 0, 0], [0] * 10]
res['m5_T5'] = analyse(T5, 5)
res['m5_T5_candidate_phase_congruences'] = check_phases(T5, 5, 20, PH5)
res['m7_T7'] = analyse(T7, 7)
res['m7_T7_candidate_phase_congruences'] = check_phases(T7, 7, 28, PH7)
res['qls10_phase_congruences'] = check_qls_phases(T5, 5, 20, PHH)
require(res['m5_T5']['solvable'] and all(res['m5_T5_candidate_phase_congruences'].values()), 'm5 positive failed')
require(res['m7_T7']['solvable'] and all(res['m7_T7_candidate_phase_congruences'].values()), 'm7 positive failed')
require(all(res['qls10_phase_congruences'].values()), 'qls10 congruences failed')
# (iv) negative control: admissible m = 5 multiset whose union graph is connected bipartite (size 10 = 2 mod 4)
Tneg = [(s, (2 * s) % 5) for s in range(5)] + [(s, (2 * s + 1) % 5) for s in range(5)]
res['m5_negative_T'] = Tneg
res['m5_negative'] = analyse(Tneg, 5)
require(pairings(Tneg, 5) is not None and not res['m5_negative']['solvable'], 'negative control did not fail')
# also: the candidate PH5 phases must violate a congruence when one entry is shifted by 1 unit
PHb = [list(p) for p in PH5]
PHb[1][0] += 1
res['m5_shifted_phase_congruences'] = check_phases(T5, 5, 20, PHb)
require(not all(res['m5_shifted_phase_congruences'].values()), 'shifted phase passed')

res['FAILS'] = FAILS
res['STATUS'] = 'ALL_CHECKS_AS_EXPECTED' if not FAILS else 'UNEXPECTED'
out = {'script': SELF.name, 'script_sha256': hashlib.sha256(SELF.read_bytes()).hexdigest(),
       'native_clock_start': CLOCK_START, 'native_clock_finish': native_clock(), 'results': res}
OUT.write_text(json.dumps(out, indent=1) + '\n')
print(json.dumps({'status': res['STATUS'], 'fails': FAILS, 'm3_admissible': res['m3_admissible_multisets'],
                  'm3_solvable': res['m3_solvable_count'], 'm5': res['m5_T5']['solvable'],
                  'm7': res['m7_T7']['solvable'], 'neg': res['m5_negative']['solvable']}, indent=1))
