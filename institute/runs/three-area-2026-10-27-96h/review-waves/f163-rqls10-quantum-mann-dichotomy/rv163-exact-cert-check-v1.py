#!/usr/bin/env python3
"""rv163 reviewer-authored EXACT checker for wave f163-rqls10-quantum-mann-dichotomy.

Independent of all author code: nothing is imported from, or executed of, the author's scripts.
Integer data were transcribed by the reviewer from the frozen bundle:
  * T5, PHI2(K555), incidence      : dichotomy candidate section 2 (text)
  * T5, grid placement (QLS10)     : half-resolved packet section 1 (text)
  * T7                             : half-resolved packet section 2 (text)
  * PHI2(K777), PHI2(QLS10)        : literals PH7 / PHH of the author replay script (input 4, read only);
                                     these phases are NOT printed in either packet.

Arithmetic (two independent exact zero tests, both reviewer-written):
  M1  reduction of the group-ring element sum_k c_k x^k modulo the cyclotomic polynomial Phi_N,
      computed here from x^N - 1 by exact integer division (no tables).
  M2  evaluation at an element g of exact order N in F_P, P prime, P = 1 mod 140, with
      P > (sum_k |c_k|)^phi(N) asserted per call.  If s != 0 in Z[zeta_N], its norm is a nonzero
      integer of absolute value <= (sum |c_k|)^phi(N) < P that lies in the prime (P, zeta - g);
      hence s(g) = 0 mod P forces s = 0.  So M2 is an exact test, not a heuristic.
Run: /usr/bin/python3 -B rv163-exact-cert-check-v1.py   (writes rv163-exact-cert-check-v1.json)
"""
import hashlib
import itertools
import json
import platform
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SELF = Path(__file__).resolve()
OUT = HERE / 'rv163-exact-cert-check-v1.json'


def native_clock():
    return subprocess.run(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], capture_output=True,
                          text=True, check=True).stdout.strip()


CLOCK_START = native_clock()
FAILS = []


def require(cond, msg):
    if not cond:
        FAILS.append(msg)
    return bool(cond)

# ------------------------------------------------------------------ integer polynomials


def exact_div(a, b):
    a = list(a)
    db = len(b) - 1
    assert b[-1] == 1
    q = [0] * (len(a) - db)
    for i in range(len(a) - 1, db - 1, -1):
        c = a[i]
        if c:
            q[i - db] = c
            for j in range(db + 1):
                a[i - db + j] -= c * b[j]
    assert all(x == 0 for x in a), 'non-exact division'
    return q


_CYC = {}


def cyclotomic(n):
    if n not in _CYC:
        p = [-1] + [0] * (n - 1) + [1]
        for d in range(1, n):
            if n % d == 0:
                p = exact_div(p, cyclotomic(d))
        _CYC[n] = p
    return _CYC[n]


def reduce_mod(a, phi):
    d = len(phi) - 1
    r = list(a) + [0] * max(0, d - len(a))
    for i in range(len(r) - 1, d - 1, -1):
        c = r[i]
        if c:
            r[i] = 0
            for j in range(d):
                r[i - d + j] -= c * phi[j]
    return r[:d]


def m1_zero(c, N):
    return all(x == 0 for x in reduce_mod(c, cyclotomic(N)))

# ------------------------------------------------------------------ modular exact test


def is_prime(n):
    if n < 2:
        return False
    small = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for p in small:
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in small:  # deterministic for n < 3.3e24
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


P = 10 ** 15 - (10 ** 15 % 140) + 1
while not is_prime(P):
    P += 140
assert P > 10 ** 15 and P % 140 == 1


def element_of_order(N):
    qs = [q for q in range(2, N + 1) if N % q == 0 and all(q % r for r in range(2, q))]
    for h in range(2, 10 ** 6):
        g = pow(h, (P - 1) // N, P)
        if pow(g, N, P) == 1 and all(pow(g, N // q, P) != 1 for q in qs):
            return g
    raise RuntimeError


GEN = {20: element_of_order(20), 28: element_of_order(28)}
PHI_EULER = {20: 8, 28: 12}


def m2_zero(c, N):
    bound = sum(abs(x) for x in c) ** PHI_EULER[N]
    assert bound < P, 'norm bound violated'
    g = GEN[N]
    return sum(ck * pow(g, k, P) for k, ck in enumerate(c)) % P == 0

# ------------------------------------------------------------------ flat vectors


def ip_counts(u, v, N):
    """N-term group-ring coefficients of <u,v> = sum_j conj(zeta^u_j) zeta^v_j (unnormalised)."""
    c = [0] * N
    for a, b in zip(u, v):
        c[(b - a) % N] += 1
    return c


def gr_mul(a, b, N):
    r = [0] * N
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    r[(i + j) % N] += x * y
    return r


def gr_conj(a, N):
    return [a[(-k) % N] for k in range(N)]


def is_zero_both(c, N):
    z1, z2 = m1_zero(c, N), m2_zero(c, N)
    require(z1 == z2, f'M1/M2 disagree on {c}')
    return z1


def parallel_comb(u, v, N):
    return len({(b - a) % N for a, b in zip(u, v)}) == 1


def parallel_exact(u, v, N):
    s = ip_counts(u, v, N)
    r = gr_mul(s, gr_conj(s, N), N)
    r[0] -= len(u) ** 2
    return m1_zero(r, N)

# ------------------------------------------------------------------ F_P linear algebra


def fp_left_kernel(rows, p):
    d = len(rows)
    L = len(rows[0])
    A = [list(rows[k]) + [1 if i == k else 0 for i in range(d)] for k in range(d)]
    pr = 0
    for col in range(L):
        piv = next((r for r in range(pr, d) if A[r][col] % p), None)
        if piv is None:
            continue
        A[pr], A[piv] = A[piv], A[pr]
        inv = pow(A[pr][col], p - 2, p)
        A[pr] = [(x * inv) % p for x in A[pr]]
        for r in range(d):
            if r != pr and A[r][col] % p:
                f = A[r][col]
                A[r] = [(x - f * y) % p for x, y in zip(A[r], A[pr])]
        pr += 1
        if pr == d:
            break
    assert all(all(x % p == 0 for x in A[r][:L]) for r in range(pr, d))
    return pr, [A[r][L:] for r in range(pr, d)]


def fp_rank(rows, p):
    return fp_left_kernel(rows, p)[0]


def commutant_dim(vecs, N, n):
    """dim over F_P of {X : X Q_i = Q_i X for all i}, Q_i = v_i v_i^*; >= dim over Q(zeta_N) >= 1."""
    g = GEN[N]
    pw = [pow(g, k, P) for k in range(N)]
    basis = [[1 if i == k else 0 for i in range(n * n)] for k in range(n * n)]
    for e in vecs:
        v = [pw[x % N] for x in e]
        vb = [pw[(-x) % N] for x in e]
        imgs = []
        for B in basis:
            X = [B[r * n:(r + 1) * n] for r in range(n)]
            Xv = [sum(X[r][j] * v[j] for j in range(n)) % P for r in range(n)]
            vX = [sum(vb[j] * X[j][c] for j in range(n)) % P for c in range(n)]
            imgs.append([(Xv[r] * vb[c] - v[r] * vX[c]) % P for r in range(n) for c in range(n)])
        _, ker = fp_left_kernel(imgs, P)
        basis = [[sum(l[k] * basis[k][i] for k in range(len(basis))) % P for i in range(n * n)]
                 for l in ker]
    ident = [1 if i % (n + 1) == 0 else 0 for i in range(n * n)]
    in_span = fp_rank(basis + [ident], P) == fp_rank(basis, P)
    return len(basis), in_span

# ------------------------------------------------------------------ data (transcribed)


T5 = [(0, 0), (0, 1), (1, 0), (1, 3), (2, 2), (2, 4), (3, 1), (3, 4), (4, 2), (4, 3)]
PH5 = [[-35, -25, -25, -15, -20, -10, -15, -5, -10, 0],
       [-10, -10, -10, -5, 0, 5, -10, 0, 0, 0],
       [0] * 10]
T7 = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 3), (2, 5), (3, 5), (3, 6), (4, 2), (4, 6), (5, 2), (5, 4),
      (6, 3), (6, 4)]
PH7 = [[-63, -49, -14, 0, -84, -70, -56, -42, -42, -28, -28, -14, -14, 0],
       [-49, -70, -14, -35, -56, -14, -14, 0, -14, 0, -14, 0, 0, 0],
       [0] * 14]
PHH = [[-65, -40, -40, -25, -25, -15, -20, -10, -10, 0],
       [-40, -30, -25, -15, -15, -5, -20, -10, -10, 0],
       [-25, -10, -15, -10, -10, -10, 0, 0, 0, 0],
       [0] * 10]


def flat_vec(N, m, T, phase, x):
    step = N // m
    return tuple((step * ((c[0] * x[0] + c[1] * x[1]) % m) + phase[j]) % N for j, c in enumerate(T))


def uniform_alpha_beta_gamma(T, m):
    cnt = lambda f: sorted(sum(1 for c in T if f(c) % m == v) for v in range(m))
    return {k: cnt(f) == [2] * m for k, f in
            (('alpha', lambda c: c[0]), ('beta', lambda c: c[1]), ('alpha_minus_beta', lambda c: c[0] - c[1]))}


def check_tripartite(name, m, N, T, PH, perturb=None, clone=None, do_commutant=True):
    n = 2 * m
    cells = []
    for q in range(3):
        for s in range(m):
            for t in range(m):
                e = list(flat_vec(N, m, T, PH[q], (s, t)))
                u = (s + t) % m
                edge = [(('A', s), ('B', t)), (('A', s), ('C', u)), (('B', t), ('C', u))][q]
                cells.append([q, (s, t), e, edge])
    if perturb is not None:          # negative control: shift one exponent of one vector
        k, j, dlt = perturb
        cells[k][2][j] = (cells[k][2][j] + dlt) % N
    if clone is not None:            # negative control: make vector k2 a phase multiple of k1
        k1, k2, ph = clone
        cells[k2][2] = [(x + ph) % N for x in cells[k1][2]]
    vecs = [tuple(c[2]) for c in cells]
    res = {'m': m, 'N': N, 'dimension': n, 'rays': len(cells), 'cyclotomic_poly_coeffs_low_to_high': cyclotomic(N)}
    res['T_distinct'] = len(set(T)) == len(T)
    res['T_uniformity'] = uniform_alpha_beta_gamma(T, m)
    edges = [frozenset(c[3]) for c in cells]
    allE = {frozenset(((P1, i), (P2, j))) for P1, P2 in (('A', 'B'), ('A', 'C'), ('B', 'C'))
            for i in range(m) for j in range(m)}
    res['edge_map_bijective_onto_E(Kmmm)'] = len(set(edges)) == len(edges) == 3 * m * m and set(edges) == allE
    verts = [(Pp, i) for Pp in 'ABC' for i in range(m)]
    ctx = {v: [k for k, e in enumerate(edges) if v in e] for v in verts}
    res['contexts'] = len(ctx)
    res['context_sizes_all_2m'] = all(len(c) == n for c in ctx.values())
    inter = []
    for v, w in itertools.combinations(verts, 2):
        inter.append((v[0] == w[0], len(set(ctx[v]) & set(ctx[w]))))
    res['same_part_contexts_disjoint'] = all(k == 0 for same, k in inter if same)
    res['cross_part_contexts_meet_in_exactly_one_ray'] = all(k == 1 for same, k in inter if not same)
    adj = set()
    for v in verts:
        for a, b in itertools.combinations(ctx[v], 2):
            adj.add((min(a, b), max(a, b)))
    res['line_graph_edges'] = len(adj)
    res['line_graph_edges_expected_3m*C(2m,2)'] = 3 * m * (n * (n - 1) // 2)
    orth = {}
    for a, b in itertools.combinations(range(len(cells)), 2):
        orth[(a, b)] = is_zero_both(ip_counts(vecs[a], vecs[b], N), N)
    bad_adj = [(a, b) for (a, b) in sorted(adj) if not orth[(a, b)]]
    res['adjacent_pairs_exactly_orthogonal'] = len(adj) - len(bad_adj)
    res['adjacent_pairs_NOT_orthogonal'] = len(bad_adj)
    res['first_bad_adjacent_pairs'] = [[cells[a][:2], cells[b][:2]] for a, b in bad_adj[:5]]
    res['all_pairs'] = len(orth)
    res['orthogonal_pairs_total'] = sum(orth.values())
    res['orthogonal_nonadjacent_pairs'] = sum(1 for k, z in orth.items() if z and k not in adj)
    par_c = [(a, b) for a, b in orth if parallel_comb(vecs[a], vecs[b], N)]
    par_e = [(a, b) for a, b in orth if parallel_exact(vecs[a], vecs[b], N)]
    res['parallel_pairs_combinatorial'] = len(par_c)
    res['parallel_pairs_exact_abs_ip_sq_eq_n2'] = len(par_e)
    res['parallel_tests_agree'] = par_c == par_e
    res['rays_nonzero_exact_norm_sq_equals_n'] = all(
        m1_zero([x - (n if k == 0 else 0) for k, x in enumerate(ip_counts(v, v, N))], N) for v in vecs)
    res['flat_all_entries_zetaN_power_over_sqrt_n'] = all(len(v) == n and all(isinstance(x, int) for x in v)
                                                          for v in vecs)
    # frame identity: for each quadrant Q, sum_{cells in Q} v v^* = m^2 I exactly (unnormalised)
    frame = {}
    for q in range(3):
        ok = True
        for j in range(n):
            for k in range(n):
                c = [0] * N
                for cc in cells:
                    if cc[0] == q:
                        c[(cc[2][j] - cc[2][k]) % N] += 1
                if j == k:
                    c[0] -= m * m
                ok = ok and m1_zero(c, N)
        frame[['AB', 'AC', 'BC'][q]] = ok
    res['frame_identity_sum_over_quadrant_vvstar_eq_m2_I'] = frame
    if do_commutant:
        dim, ident_in = commutant_dim(vecs, N, n)
        res['commutant_dim_over_F_P_upper_bound_for_exact'] = dim
        res['identity_in_commutant'] = ident_in
    res['PASS'] = (res['edge_map_bijective_onto_E(Kmmm)'] and res['context_sizes_all_2m'] and
                   len(bad_adj) == 0 and len(par_c) == 0 and res['parallel_tests_agree'] and
                   res['line_graph_edges'] == res['line_graph_edges_expected_3m*C(2m,2)'])
    return res

# ------------------------------------------------------------------ transversal census


def transversal_census(n, orthfun):
    cells = [(r, c) for r in range(n) for c in range(n)]
    adjm = [0] * (n * n)
    for i, a in enumerate(cells):
        for j, b in enumerate(cells):
            if i != j and orthfun(a, b):
                adjm[i] |= 1 << j
    found = []

    def dfs(r, used, chosen, cand):
        if r == n:
            found.append(tuple(chosen))
            return
        for c in range(n):
            if used >> c & 1:
                continue
            idx = r * n + c
            if cand >> idx & 1:
                dfs(r + 1, used | (1 << c), chosen + [c], cand & adjm[idx])
    dfs(0, 0, [], (1 << (n * n)) - 1)
    return found, adjm


def max_cliques(adjm, nv):
    out = []

    def bk(R, Pm, Xm):
        if Pm == 0 and Xm == 0:
            out.append(R)
            return
        best, piv, i, tmp = -1, None, 0, Pm | Xm
        while tmp:
            if tmp & 1:
                k = bin(Pm & adjm[i]).count('1')
                if k > best:
                    best, piv = k, i
            tmp >>= 1
            i += 1
        cand = Pm & ~adjm[piv]
        i = 0
        while cand:
            if cand & 1:
                bk(R | (1 << i), Pm & adjm[i], Xm & adjm[i])
                Pm &= ~(1 << i)
                Xm |= 1 << i
            cand >>= 1
            i += 1
    bk(0, (1 << nv) - 1, 0)
    return out


def classical_census(L):
    n = len(L)
    f, _ = transversal_census(n, lambda a, b: L[a[0]][a[1]] != L[b[0]][b[1]])
    return len(f)


def check_qls10(PHq):
    N, m, n = 20, 5, 10
    pos = {0: lambda x: (x[0], x[1]), 1: lambda x: (x[0], 5 + x[1]), 2: lambda x: (5 + x[0], x[1]),
           3: lambda x: (5 + x[0], 5 + x[1])}
    grid = {}
    for q in range(4):
        for x in itertools.product(range(m), repeat=2):
            grid[pos[q](x)] = flat_vec(N, m, T5, PHq[q], x)
    res = {'cells': len(grid)}
    cells = sorted(grid)
    O = {}
    for a, b in itertools.combinations(cells, 2):
        O[(a, b)] = O[(b, a)] = is_zero_both(ip_counts(grid[a], grid[b], N), N)
    res['rows_onb'] = all(O[((r, a), (r, b))] for r in range(n) for a, b in itertools.combinations(range(n), 2))
    res['cols_onb'] = all(O[((a, c), (b, c))] for c in range(n) for a, b in itertools.combinations(range(n), 2))
    T1 = [[(x0, 5 + x1) for x0 in range(m) for x1 in range(m) if (x0 + x1) % m == u] +
          [(5 + x0, x1) for x0 in range(m) for x1 in range(m) if (x0 + x1) % m == u] for u in range(m)]
    res['T1_classes_are_transversals'] = all(sorted(r for r, _ in cl) == list(range(n)) and
                                             sorted(c for _, c in cl) == list(range(n)) for cl in T1)
    res['T1_classes_disjoint_cover_Q01_Q10'] = (len({c for cl in T1 for c in cl}) == 50 and
                                                {c for cl in T1 for c in cl} ==
                                                {(r, c) for r in range(n) for c in range(n) if (r < 5) != (c < 5)})
    res['T1_onb'] = all(O[(a, b)] for cl in T1 for a, b in itertools.combinations(cl, 2))
    res['orthogonal_pairs'] = sum(O.values()) // 2
    par_c = [(a, b) for a, b in itertools.combinations(cells, 2) if parallel_comb(grid[a], grid[b], N)]
    par_e = [(a, b) for a, b in itertools.combinations(cells, 2) if parallel_exact(grid[a], grid[b], N)]
    res['parallel_pairs_combinatorial'] = len(par_c)
    res['parallel_pairs_exact'] = len(par_e)
    trans, adjm = transversal_census(n, lambda a, b: O[(a, b)])
    res['orthogonal_transversals_dfs'] = len(trans)
    t1set = {tuple(sorted(cl)) for cl in T1}
    tr_cells = [tuple(sorted((r, c) for r, c in enumerate(t))) for t in trans]
    res['dfs_transversals_equal_T1_classes'] = set(tr_cells) == t1set
    cl = max_cliques(adjm, n * n)
    ten = [c for c in cl if bin(c).count('1') == 10]
    def cells_of(mask):
        return [cells[i] for i in range(n * n) if mask >> i & 1]
    kinds = {'row': 0, 'column': 0, 'transversal': 0, 'other': 0}
    other_examples = []
    tcount_clique = 0
    for c in ten:
        cs = cells_of(c)
        rs, cs2 = {r for r, _ in cs}, {cc for _, cc in cs}
        if len(rs) == 1:
            kinds['row'] += 1
        elif len(cs2) == 1:
            kinds['column'] += 1
        elif len(rs) == 10 and len(cs2) == 10:
            kinds['transversal'] += 1
            tcount_clique += 1
        else:
            kinds['other'] += 1
            if len(other_examples) < 3:
                other_examples.append(cs)
    res['max_clique_size'] = max(bin(c).count('1') for c in cl)
    res['ten_cliques_total'] = len(ten)
    res['ten_cliques_by_kind'] = kinds
    res['ten_clique_other_examples'] = other_examples
    res['orthogonal_transversals_clique_method'] = tcount_clique
    # forced Q11: for r in R1, c in C1, the 5 Q10 vectors of row r and 5 Q01 vectors of column c
    g = GEN[20]
    pw = [pow(g, k, P) for k in range(20)]
    ranks, q11_orth = [], True
    for r in range(5, 10):
        for c in range(5, 10):
            vs = [grid[(r, cc)] for cc in range(5)] + [grid[(rr, c)] for rr in range(5)]
            ranks.append(fp_rank([[pw[x] for x in v] for v in vs], P))
            q11_orth = q11_orth and all(O[((r, c), (rr, cc))] for rr, cc in
                                        [(r, cc) for cc in range(5)] + [(rr, c) for rr in range(5)])
    res['R1C1_complement_rank_over_F_P_min_max'] = [min(ranks), max(ranks)]
    res['Q11_vector_orthogonal_to_those_10'] = q11_orth
    res['PASS_claims'] = (res['rows_onb'] and res['cols_onb'] and res['T1_onb'] and
                          res['T1_classes_are_transversals'] and len(par_c) == 0 and par_c == par_e and
                          res['orthogonal_pairs'] == 1225 and len(trans) == 5 and tcount_clique == 5)
    return res, grid

# ------------------------------------------------------------------ run


results = {'interpreter': sys.version.split()[0], 'platform': platform.platform()}
results['prime_P'] = P
results['generator_order20'] = GEN[20]
results['generator_order28'] = GEN[28]
results['Phi20'] = cyclotomic(20)
results['Phi28'] = cyclotomic(28)
require(cyclotomic(20) == [1, 0, -1, 0, 1, 0, -1, 0, 1], 'Phi20 mismatch with candidate statement')
require(cyclotomic(28) == [1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1], 'Phi28 mismatch')

# zero-test sanity controls (known values)
sanity = {}
def counts(N, exps):
    c = [0] * N
    for e in exps:
        c[e % N] += 1
    return c
sanity['1+z^10 (=0)'] = is_zero_both(counts(20, [0, 10]), 20)
sanity['1+z^5 (=1+i, !=0)'] = is_zero_both(counts(20, [0, 5]), 20)
sanity['sum_k z^(4k), k<5 (=0)'] = is_zero_both(counts(20, [0, 4, 8, 12, 16]), 20)
sanity['sum_k z^(5k), k<4 (=0)'] = is_zero_both(counts(20, [0, 5, 10, 15]), 20)
sanity['1+z^4+z^8 (!=0)'] = is_zero_both(counts(20, [0, 4, 8]), 20)
sanity['sum_k z28^(4k), k<7 (=0)'] = is_zero_both(counts(28, [4 * k for k in range(7)]), 28)
sanity['1+z28^14 (=0)'] = is_zero_both(counts(28, [0, 14]), 28)
sanity['1+z28^7 (!=0)'] = is_zero_both(counts(28, [0, 7]), 28)
expect = [True, False, True, True, False, True, True, False]
results['zero_test_sanity'] = sanity
results['zero_test_sanity_as_expected'] = list(sanity.values()) == expect
require(results['zero_test_sanity_as_expected'], 'zero-test sanity failed')

# census-code controls on classical cyclic Latin squares (known transversal counts 15, 0, 133, 0)
cyc = lambda n: [[(r + c) % n for c in range(n)] for r in range(n)]
cens = {f'cyclic_Z{n}': classical_census(cyc(n)) for n in (5, 6, 7, 10)}
results['census_controls_classical_cyclic'] = cens
results['census_controls_as_expected'] = cens == {'cyclic_Z5': 15, 'cyclic_Z6': 0, 'cyclic_Z7': 133,
                                                  'cyclic_Z10': 0}
require(results['census_controls_as_expected'], 'census control failed')

results['K555'] = check_tripartite('K555', 5, 20, T5, PH5)
require(results['K555']['PASS'], 'K555 failed')
require(results['K555']['commutant_dim_over_F_P_upper_bound_for_exact'] == 1 and
        results['K555']['identity_in_commutant'], 'K555 commutant not trivial')
# commutant-code controls: reducible families must give the textbook dimensions 1+81 and 10
v5 = [flat_vec(20, 5, T5, PH5[q], (s, t)) for q in range(3) for s in range(5) for t in range(5)]
results['commutant_controls'] = {'single_ray_expect_82': commutant_dim(v5[:1], 20, 10)[0],
                                 'one_ONB_context_A0_expect_10': commutant_dim(v5[:5] + v5[25:30], 20, 10)[0]}
require(results['commutant_controls'] == {'single_ray_expect_82': 82, 'one_ONB_context_A0_expect_10': 10},
        'commutant control failed')
results['K777'] = check_tripartite('K777', 7, 28, T7, PH7)
require(results['K777']['PASS'], 'K777 failed')
q, _ = check_qls10(PHH)
results['QLS10'] = q
require(q['PASS_claims'], 'QLS10 failed')

# negative controls (must FAIL for the intended reason)
neg = {}
r1 = check_tripartite('K555-perturbed', 5, 20, T5, PH5, perturb=(0, 3, 1), do_commutant=False)
neg['K555_one_exponent_of_ray0_shifted_by_+1'] = {
    'PASS': r1['PASS'], 'adjacent_pairs_NOT_orthogonal': r1['adjacent_pairs_NOT_orthogonal'],
    'first_bad_adjacent_pairs': r1['first_bad_adjacent_pairs']}
r2 = check_tripartite('K555-clone', 5, 20, T5, PH5, clone=(0, 40, 7), do_commutant=False)
neg['K555_ray40_replaced_by_phase_multiple_of_ray0'] = {
    'PASS': r2['PASS'], 'parallel_pairs_combinatorial': r2['parallel_pairs_combinatorial'],
    'parallel_pairs_exact': r2['parallel_pairs_exact_abs_ip_sq_eq_n2']}
PHbad = [list(p) for p in PHH]
PHbad[2][0] = (PHbad[2][0] + 5)
qb, _ = check_qls10(PHbad)
neg['QLS10_Q10_phase0_shifted_by_+5'] = {k: qb[k] for k in ('rows_onb', 'cols_onb', 'T1_onb',
                                                             'orthogonal_pairs', 'PASS_claims')}
results['negative_controls'] = neg
require(not r1['PASS'] and r1['adjacent_pairs_NOT_orthogonal'] > 0, 'neg control 1 did not fail')
require(not r2['PASS'] and r2['parallel_pairs_combinatorial'] == 1 and
        r2['parallel_pairs_exact_abs_ip_sq_eq_n2'] == 1, 'neg control 2 did not fail as intended')
require(not qb['PASS_claims'], 'neg control 3 did not fail')

results['FAILS'] = FAILS
results['STATUS'] = 'ALL_CHECKS_AS_EXPECTED' if not FAILS else 'UNEXPECTED'
out = {'script': SELF.name, 'script_sha256': hashlib.sha256(SELF.read_bytes()).hexdigest(),
       'native_clock_start': CLOCK_START, 'native_clock_finish': native_clock(), 'results': results}
OUT.write_text(json.dumps(out, indent=1, default=str) + '\n')
print(json.dumps({'status': results['STATUS'], 'fails': FAILS, 'clock_start': CLOCK_START,
                  'clock_finish': out['native_clock_finish']}, indent=1))
