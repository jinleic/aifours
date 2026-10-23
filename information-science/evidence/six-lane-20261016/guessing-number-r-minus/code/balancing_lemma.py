"""Balancing lemma for R^- (exact checks).

Lemma B.  Let C be an FD-consistent code on R^- whose vertex alphabets are A_v (A_v = projection of C on
v).  If |C|^3 > prod_v |A_v|^2, then gn(R^-) > 20/3.

Proof idea (triangle padding).  For a triangle T of R^- and an integer q >= 1 the clique code
K_T(q) = {x : x_a + x_b + x_c = 0 mod q on T, x_u = 0 off T} is FD-consistent, has q^2 words, alphabet q
on T and 1 elsewhere, so it contributes exactly 2 log q to log|.| and log q to each of its three
vertices.  Products of FD-consistent codes on the same graph are FD-consistent, and padding an alphabet
(embedding A_v into a larger set) keeps FD-consistency.  The 10 BCDRV cover triangles have an
invertible incidence matrix B (checked below), and B^{-1} 1 = (1/3) 1.  So the vertex log-sizes
k*alpha_v of C^k can be topped up to a common value L by nonnegative triangle exponents, with
rounding loss < 3 per vertex.  With g = 3 log2|C| - 2 sum_v log2|A_v| > 0, the padded product P over the
common alphabet s satisfies
    3 log2|P| - 20 log2 s = k*g - 2*sum_v delta_v,   0 <= delta_v < 3,
which is > 0 once k*g > 60.  Then gn(R^-) >= gn(R^-, s) > 20/3 (BCDRV Sec. 3: gn(G,s) <= gn(G)).

This script checks:
  (1) the triangle list of R^- and the exact invertibility of the cover-incidence matrix, and B^{-1}1 = 1/3;
  (2) pad(): for given (|C|, |A_v|) it returns (k, e_T) and verifies |P|^3 > s^20 by exact integer
      arithmetic, or refuses when g <= 0;
  (3) controls:
      - fan code 625 / alphabet 4: refuse (g < 0);
      - cover code 2^20 / alphabet 8: refuse (g = 0);
      - arithmetic-only synthetic inputs: accept;
      - mechanics: a real padded product built from the fan code and triangle codes is brute-force
        FD-checked (a mutated product must fail).
Synthetic inputs are NOT codes; they only test the arithmetic of the construction.
"""
import sys, os, json, math, itertools
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from graphs import R_MINUS_EDGES

E = {frozenset(e) for e in R_MINUS_EDGES}
V = list(range(1, 11))
TRI = sorted(tuple(t) for t in itertools.combinations(V, 3)
             if all(frozenset(p) in E for p in itertools.combinations(t, 2)))
COVER = [(1, 2, 3), (1, 4, 5), (1, 6, 7), (2, 3, 9), (2, 7, 10), (3, 8, 9), (4, 5, 10), (4, 8, 10), (5, 6, 9), (6, 7, 8)]

def inverse(M):
    n = len(M); A = [[F(x) for x in row] + [F(int(i == j)) for j in range(n)] for i, row in enumerate(M)]
    for c in range(n):
        p = next((r for r in range(c, n) if A[r][c] != 0), None)
        if p is None: return None
        A[c], A[p] = A[p], A[c]
        pv = A[c][c]; A[c] = [x / pv for x in A[c]]
        for r in range(n):
            if r != c and A[r][c] != 0:
                f = A[r][c]; A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    return [row[n:] for row in A]

B = [[int(v in T) for T in COVER] for v in V]          # rows vertices, columns cover triangles
BINV = inverse(B)

def pad(code_size, alph, kmax=10**6):
    """Return dict with k, exponents e_T (q_T = 2^e_T), s, and exact verdict |P|^3 > s^20."""
    g = 3 * math.log2(code_size) - 2 * sum(math.log2(a) for a in alph)
    # exact sign of g: |C|^3 vs prod |A_v|^2
    lhs, rhs = code_size ** 3, math.prod(a * a for a in alph)
    if lhs <= rhs:
        return dict(accepted=False, reason="|C|^3 <= prod|A_v|^2", g=g)
    k = max(1, math.ceil(61 / g))
    if k > kmax: return dict(accepted=False, reason="k too large", g=g)
    alpha = [k * math.log2(a) for a in alph]
    # y = B^{-1}(L*1 - alpha) = L/3 - B^{-1} alpha ; choose L so that min y >= 0
    Binv_alpha = [sum(float(BINV[t][v]) * alpha[v] for v in range(10)) for t in range(10)]
    L = 3 * max(Binv_alpha) + 1e-9
    y = [L / 3 - b for b in Binv_alpha]
    e = [max(0, math.floor(t)) for t in y]
    # exact verification
    size_P = code_size ** k * 2 ** (2 * sum(e))
    vert = [alph[v] ** k * 2 ** sum(e[t] for t in range(10) if (v + 1) in COVER[t]) for v in range(10)]
    s = max(vert)
    ok = size_P ** 3 > s ** 20
    return dict(accepted=ok, g=g, k=k, exponents=e, log2_s=math.log2(s), log2_P=math.log2(size_P),
                margin_log2=3 * math.log2(size_P) - 20 * math.log2(s))

def tri_code(T, q):
    out = []
    for a in range(q):
        for b in range(q):
            x = [0] * 10; x[T[0] - 1] = a; x[T[1] - 1] = b; x[T[2] - 1] = (-a - b) % q
            out.append(tuple(x))
    return out

def product(c1, c2):
    return [tuple((a, b) for a, b in zip(x, y)) for x in c1 for y in c2]

NB = {v: set() for v in V}
for a, b in R_MINUS_EDGES: NB[a].add(b); NB[b].add(a)
def fd_ok(code):
    for v in V:
        seen = {}
        for x in code:
            key = tuple(x[u - 1] for u in sorted(NB[v]))
            if seen.setdefault(key, x[v - 1]) != x[v - 1]: return False
    return True

def fan_code():
    W = ["00000", "00110", "10010", "11110", "10001"]
    FANS = [(1, 2, 3, 4, 5), (1, 2, 7, 6, 5), (8, 10, 4, 3, 9), (8, 10, 7, 6, 9)]
    code = set()
    for ch in itertools.product(range(5), repeat=4):
        sym = {v: "" for v in V}
        for f, c in zip(FANS, ch):
            for p, v in enumerate(f): sym[v] += W[c][p]
        code.add(tuple(sym[v] for v in V))
    return sorted(code)

if __name__ == "__main__":
    res = {}
    res["triangles"] = [list(t) for t in TRI]
    res["n_triangles"] = len(TRI)
    res["cover_subset_of_triangles"] = all(t in TRI for t in COVER)
    res["cover_each_vertex_in_3"] = all(sum(r) == 3 for r in B)
    res["B_invertible"] = BINV is not None
    res["Binv_times_1_equals_1_over_3"] = BINV is not None and all(sum(row) == F(1, 3) for row in BINV)
    res["Binv"] = [[str(x) for x in row] for row in BINV] if BINV else None
    # controls on the arithmetic
    res["control_fan_625_alph4"] = pad(625, [4] * 10)
    res["control_cover_2^20_alph8"] = pad(2 ** 20, [8] * 10)
    res["synthetic_102_alph2"] = pad(102, [2] * 10)
    res["synthetic_mixed"] = pad(3000, [2, 3, 3, 3, 2, 3, 3, 2, 3, 3])
    # mechanics: fan code x triangle codes on two cover triangles, brute-force FD
    fc = fan_code()
    P = product(product(fc, tri_code((4, 8, 10), 3)), tri_code((1, 2, 3), 2))
    P = [tuple((a[0][0], a[0][1], a[1]) for a in x) for x in P]   # flatten symbols
    res["mechanics_product_size"] = len(P)
    res["mechanics_product_fd"] = fd_ok(P)
    bad = list(P); x = list(bad[0]); x[2] = (x[2][0], x[2][1], (x[2][2] + 1) % 2); bad[0] = tuple(x)
    res["mechanics_mutated_fd"] = fd_ok(bad)
    ok = (res["cover_subset_of_triangles"] and res["cover_each_vertex_in_3"] and res["Binv_times_1_equals_1_over_3"]
          and not res["control_fan_625_alph4"]["accepted"] and not res["control_cover_2^20_alph8"]["accepted"]
          and res["synthetic_102_alph2"]["accepted"] and res["synthetic_mixed"]["accepted"]
          and res["mechanics_product_fd"] and not res["mechanics_mutated_fd"])
    res["all_checks_pass"] = ok
    json.dump(res, open(os.path.join(os.path.dirname(__file__), "..", "evidence", "balancing-lemma-check.json"), "w"), indent=1)
    print(json.dumps({k: v for k, v in res.items() if k not in ("Binv", "triangles")}, indent=1))
    sys.exit(0 if ok else 1)
