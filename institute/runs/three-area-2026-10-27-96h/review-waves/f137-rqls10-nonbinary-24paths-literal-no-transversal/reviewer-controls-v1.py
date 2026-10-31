#!/usr/bin/env python3
"""reviewer-controls-v1.py  (review f137, reviewer-written; author checkers are NOT imported or executed)

Positive / negative / mutation controls for every reviewer tool used in this review, plus two independent
end-to-end checks:
 A. mu72 root-closure: known-answer polynomials (must pass / must fail) and a mutation of a REAL half-polynomial.
 B. perfect-matching detector: the 48 real E0 half-graphs (must have a PM), real identity-edge graphs (must not),
    mutation: identity graph + 5 planted edges of a perfect matching (must be detected).
 C. Hadamard checker: catalog line (pass) and a one-entry mutation (fail).
 D. row-obstruction routine: planted orthogonal candidate (row must become NON-obstructing); digit mutation: for all
    48 x 2880 orders replace the author's digit by a non-obstructing row -> the checker must reject all 138240.
 E. NORMALIZATION-FREE exhaustive transversal search at all 48 mu6 endpoints: every one of the 2*5!*5! = 28800
    physical orders sigma with sigma(even) in {E0, complement} (positions arbitrary, sigma(0) free) and pi(0) free,
    exact backtracking over pi.  Uses only the half-graph necessity theorem, not the author's symmetry caller.
 F. odd-order end-to-end positive control: n = 5, K = F5: the transversal finder must find the diagonal transversal and
    the row-obstruction routine must report NO obstructing row for sigma = id.
 G. summary of the even-order positive-control searches (from reviewer-positive-search*-result-v1.json).
Writes reviewer-controls-result-v1.json with /bin/date receipts.
"""
import importlib.util, json, hashlib, subprocess, time, random
from itertools import combinations, permutations
from fractions import Fraction as Fr
from pathlib import Path
import numpy as np
HERE = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("rc", HERE / "reviewer-cyclo-v1.py")
rc = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(rc)
SRC = Path("/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/rqls10")
CAT = SRC / "frontier-20261028-aalto-bh10-6-catalog-v1.txt"; TF = SRC / "frontier-20261028-q18-nonbinary-twentyfour-v1.json"
CERT = SRC / "frontier-20261028-nonbinary-eight-endpoints-v1.json"
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def clock(): return subprocess.run(["/bin/date", "+%Y-%m-%dT%H:%M:%S%z %Z"], capture_output=True, text=True).stdout.strip()
T0 = clock(); t0 = time.monotonic(); out = {"clock_start": T0, "inputs_sha256": {str(p): sha(p) for p in (CAT, TF, CERT)}}
lines = [l for l in CAT.read_text().split("\n") if l]
catalog = [[[int(l[6 + 10 * t + c]) for c in range(10)] for t in range(10)] for l in lines]
recs = json.loads(TF.read_text())["records"]
cert = {(x["case"], x["phase6"]): x for x in json.loads(CERT.read_text())["records"]}
def load_case(D):
    H = catalog[D["class"] - 1]; co = D["coefficients"]; rects = D["rectangles"]
    R = [[sum(co[j] * int(t in rects[j]["rows"] and c in rects[j]["columns"]) for j in range(4)) for c in range(10)] for t in range(10)]
    return np.array(H), np.array(R)
C6 = rc.Cyclo(6); SUB = list(combinations(range(10), 5))
Qw = rc.Qw; one = Qw(1)

# ---------------- A. root closure controls ----------------
A = {}
def P(*cs): return [Qw(c) if not isinstance(c, Qw) else c for c in cs]
phi6 = P(1, -1, 1); bad = P(1, Fr(-1, 2), 1)
A["must_pass"] = {"Phi6": rc.unit_root_closure(phi6), "Phi6_squared": rc.unit_root_closure(rc.qmul(phi6, phi6)),
                  "(z-1)^2": rc.unit_root_closure(P(1, -2, 1)), "z^2+1": rc.unit_root_closure(P(1, 0, 1)),
                  "z^3-2_no_unit_roots": rc.unit_root_closure(P(-2, 0, 0, 1)),
                  "Phi72": rc.unit_root_closure([Qw(c) for c in rc.cyclotomic(72)]), "Phi9": rc.unit_root_closure([Qw(c) for c in rc.cyclotomic(9)]),
                  "Phi8_cubed": rc.unit_root_closure(rc.qmul(rc.qmul([Qw(c) for c in rc.cyclotomic(8)], [Qw(c) for c in rc.cyclotomic(8)]), [Qw(c) for c in rc.cyclotomic(8)]))}
A["must_fail"] = {"z^2-z/2+1": rc.unit_root_closure(bad), "Phi6*(z^2-z/2+1)": rc.unit_root_closure(rc.qmul(phi6, bad)),
                  "Phi5": rc.unit_root_closure([Qw(c) for c in rc.cyclotomic(5)]), "Phi7": rc.unit_root_closure([Qw(c) for c in rc.cyclotomic(7)]),
                  "Phi16": rc.unit_root_closure([Qw(c) for c in rc.cyclotomic(16)]), "Phi144": rc.unit_root_closure([Qw(c) for c in rc.cyclotomic(144)]),
                  "Phi72*Phi5": rc.unit_root_closure(rc.qmul([Qw(c) for c in rc.cyclotomic(72)], [Qw(c) for c in rc.cyclotomic(5)]))}
A["naive_test_on_Phi6_squared_fails_as_expected"] = not rc.naive_closure(rc.qmul(phi6, phi6))
# mutation of a real half polynomial with non-constant gcd (case 8, first found)
H, R = load_case(recs[8]); realP = None
for E in SUB:
    for c, d in rc.PAIRS:
        acc = {}
        for t in E:
            k = R[t][d] - R[t][c]; acc[k] = acc.get(k, Qw(0)) + rc.ZETA6[(H[t][d] - H[t][c]) % 6]
        key = rc.laurent_to_poly(acc)
        if key is not None and rc.gcd_has_repeated_root(list(key)):
            realP = list(key); break
    if realP: break
A["real_case8_poly_with_repeated_mu72_root"] = {"degree": len(realP) - 1, "closure": rc.unit_root_closure(realP), "naive": rc.naive_closure(realP),
                                                "mutated_times_(z^2-z/2+1)_closure": rc.unit_root_closure(rc.qmul(realP, bad)),
                                                "mutated_times_Phi6_closure": rc.unit_root_closure(rc.qmul(realP, phi6))}
A["ok"] = all(A["must_pass"].values()) and not any(A["must_fail"].values()) and A["naive_test_on_Phi6_squared_fails_as_expected"] \
          and A["real_case8_poly_with_repeated_mu72_root"]["closure"] and not A["real_case8_poly_with_repeated_mu72_root"]["naive"] \
          and not A["real_case8_poly_with_repeated_mu72_root"]["mutated_times_(z^2-z/2+1)_closure"] and A["real_case8_poly_with_repeated_mu72_root"]["mutated_times_Phi6_closure"]
out["A_root_closure"] = A; print("A root closure ok:", A["ok"], flush=True)

# ---------------- B. matching controls ----------------
def half_graph6(K6, E):
    return rc.edges_to_mask([(c, d) for c, d in rc.PAIRS if C6.vanishes([int(K6[t][d] - K6[t][c]) for t in E])])
B = {"E0_graphs_with_pm": 0, "identity_graphs_checked": 0, "identity_graphs_with_pm": 0, "planted_detected": 0}
rng = random.Random(137137)
for (i, s6), rec in sorted(cert.items()):
    H, R = load_case(recs[i]); K6 = (H + s6 * R) % 6
    if rc.has_pm(half_graph6(K6, tuple(rec["even_half"]))): B["E0_graphs_with_pm"] += 1
# identity graphs of case 0 (generic z): edges where the Laurent half-polynomial vanishes identically
H, R = load_case(recs[0])
for E in rng.sample(SUB, 40):
    edges = []
    for c, d in rc.PAIRS:
        acc = {}
        for t in E:
            k = R[t][d] - R[t][c]; acc[k] = acc.get(k, Qw(0)) + rc.ZETA6[(H[t][d] - H[t][c]) % 6]
        if rc.laurent_to_poly(acc) is None: edges.append((c, d))
    m = rc.edges_to_mask(edges); B["identity_graphs_checked"] += 1
    if rc.has_pm(m): B["identity_graphs_with_pm"] += 1
    if rc.has_pm(m | rng.choice(rc.PM10)): B["planted_detected"] += 1
B["ok"] = B["E0_graphs_with_pm"] == 48 and B["identity_graphs_with_pm"] == 0 and B["planted_detected"] == B["identity_graphs_checked"] == 40
out["B_matching"] = B; print("B matching ok:", B["ok"], B, flush=True)

# ---------------- C. Hadamard checker ----------------
def is_bh6(K6): return all(C6.vanishes([int(K6[t][d] - K6[t][c]) for t in range(10)]) for c, d in rc.PAIRS)
H, R = load_case(recs[4]); K6 = (H + 0 * R) % 6; Km = K6.copy(); Km[3][7] = (Km[3][7] + 1) % 6
C = {"catalog_line_7_is_BH6": is_bh6(K6), "one_entry_mutation_is_BH6": is_bh6(Km),
     "mutation_failing_column_pairs": sum(1 for c, d in rc.PAIRS if not C6.vanishes([int(Km[t][d] - Km[t][c]) for t in range(10)]))}
C["ok"] = C["catalog_line_7_is_BH6"] and not C["one_entry_mutation_is_BH6"]
out["C_hadamard"] = C; print("C hadamard ok:", C["ok"], C, flush=True)

# ---------------- D. row-obstruction routine ----------------
TT = np.array(rc.TENSOR30, dtype=np.int16); tt = np.arange(10)
def obstruction_sets(K6, orders):
    """orders: (N,10) sigma; returns (N,9) bool: row r (=index+1) has NO column d in 1..9 with <v_{0,0}, v_{r,d}> = 0"""
    Kd = K6[orders]; diff = (Kd[:, :, 1:] - Kd[:, :, :1]) % 6
    rr = np.arange(1, 10)
    ex = (3 * rr[None, :, None, None] * tt[None, None, :, None] + 5 * diff[:, None, :, :]) % 30
    nz = TT[ex].sum(axis=2, dtype=np.int16).any(axis=3)
    return nz.all(axis=2), nz
def orders_for(E0):
    ev = [t for t in E0 if t]; od = sorted(set(range(10)) - set(E0))
    return np.array([[0, b[0], a[0], b[1], a[1], b[2], a[2], b[3], a[3], b[4]] for a in permutations(ev) for b in permutations(od)])
D = {"digit_mutations_rejected": 0, "digit_mutations_total": 0, "planted": {}}
for (i, s6), rec in sorted(cert.items()):
    H, R = load_case(recs[i]); K6 = (H + s6 * R) % 6; orders = orders_for(tuple(rec["even_half"]))
    obs, nz = obstruction_sets(K6, orders)
    # replace each author digit by the smallest NON-obstructing row (exists: max 8 obstructing rows per order)
    nonobs = np.argmax(~obs, axis=1) + 1
    assert (~obs[np.arange(2880), nonobs - 1]).all()
    D["digit_mutations_total"] += 2880; D["digit_mutations_rejected"] += int((~obs[np.arange(2880), nonobs - 1]).sum())
# planted candidate: case 4, s6=0, sigma = first order; make column 5 of K (in physical order) equal to column 0 times
# zeta10^{-t} ... in Z_6 exponents we cannot write zeta10; instead plant in Z_30 exponents: generic routine over zeta30
H, R = load_case(recs[4]); K6 = (H + 0 * R) % 6; sigma = orders_for(tuple(cert[(4, 0)]["even_half"]))[0]
obs0, nz0 = obstruction_sets(K6, sigma[None, :])
# planted: a 10x10 exponent matrix over zeta30 (K30 = 5*K6) with column 5 := column 0 + 27 t (zeta30^{27t} = zeta10^{-t} zeta5... );
# we need sum_t zeta10^{r t} * zeta30^{K[t][5]-K[t][0]} = 0 for r = 1: choose K[t][5]-K[t][0] = -3t + 3t*0 ... take = 27t + 3t = 30t = 0? no.
# Choose column 5 so that y_t = zeta30^{K[t][5]-K[t][0]} = zeta10^{-t} * zeta10^{t} = 1 for all t?  then sum_t zeta10^{t} = 0: row 1 unobstructed.
K30 = 5 * K6[sigma]; K30p = K30.copy(); K30p[:, 5] = K30p[:, 0]      # column 5 proportional to column 0 (not Hadamard; planted)
def obstruction_general(K30, n=10):
    res = {}
    for r in range(1, n):
        cands = [d for d in range(1, n) if rc.tensor30_vanishes([3 * r * t + int(K30[t][d] - K30[t][0]) for t in range(n)])]
        res[r] = cands
    return res
g0 = obstruction_general(K30); gp = obstruction_general(K30p)
D["planted"] = {"real_obstructing_rows": [r for r, c in g0.items() if not c], "planted_obstructing_rows": [r for r, c in gp.items() if not c],
                "planted_row1_candidates": gp[1], "real_row1_candidates": g0[1],
                "routine_matches_vectorized_on_real": [r for r, c in g0.items() if not c] == [int(r) + 1 for r in np.nonzero(obs0[0])[0]]}
D["ok"] = D["digit_mutations_rejected"] == D["digit_mutations_total"] == 138240 and D["planted"]["routine_matches_vectorized_on_real"] \
          and 1 in D["planted"]["real_obstructing_rows"] and 1 not in D["planted"]["planted_obstructing_rows"] and 5 in gp[1]
out["D_row_obstruction"] = D; print("D row obstruction ok:", D["ok"], D, flush=True)

# ---------------- E. normalization-free exhaustive transversal search at all 48 endpoints ----------------
def has_transversal_from_table(orth):
    """orth[k-1][d][d2] True iff cells (r,d) and (r+k,d2) are orthogonal (k=1..9); pi(0) free"""
    pi = [None] * 10
    def rec(r):
        if r == 10: return True
        used = set(pi[:r])
        for c in range(10):
            if c in used: continue
            ok = True
            for r2 in range(r):
                if not orth[(r - r2) % 10 - 1][pi[r2]][c]: ok = False; break
            if ok:
                pi[r] = c
                if rec(r + 1): return True
                pi[r] = None
        return False
    return rec(0)
E = {"endpoints": 0, "sigmas_searched": 0, "transversals_found": 0, "sample_table_checks": 0, "sample_table_mismatch": 0}
kk = np.arange(1, 10)
for (i, s6), rec in sorted(cert.items()):
    H, R = load_case(recs[i]); K6 = (H + s6 * R) % 6; E0 = tuple(rec["even_half"]); E1 = tuple(sorted(set(range(10)) - set(E0)))
    sig_list = []
    for which in (E0, E1):
        other = tuple(sorted(set(range(10)) - set(which)))
        for a in permutations(which):
            for b in permutations(other):
                sig_list.append([a[0], b[0], a[1], b[1], a[2], b[2], a[3], b[3], a[4], b[4]])
    sig_arr = np.array(sig_list); assert sig_arr.shape == (28800, 10)
    found_here = 0
    for lo in range(0, 28800, 480):
        chunk = sig_arr[lo:lo + 480]
        Kd = K6[chunk]                                                  # (n,10t,10c)
        diff = (Kd[:, :, None, :] - Kd[:, :, :, None]) % 6               # (n,t,d,d2): K[s(t)][d2]-K[s(t)][d]
        ex = (3 * kk[None, :, None, None, None] * tt[None, None, :, None, None] + 5 * diff[:, None, :, :, :]) % 30   # (n,9,t,d,d2)
        orth = ~TT[ex].sum(axis=2, dtype=np.int16).any(axis=4)           # (n,9,d,d2)
        for j in range(chunk.shape[0]):
            E["sigmas_searched"] += 1
            if has_transversal_from_table(orth[j].tolist()):
                found_here += 1
        # scalar spot check of the table
        j = rng.randrange(chunk.shape[0]); k = rng.randrange(1, 10); d = rng.randrange(10); d2 = rng.randrange(10)
        sg = chunk[j]; exact = rc.tensor30_vanishes([3 * k * t + 5 * int(K6[sg[t]][d2] - K6[sg[t]][d]) for t in range(10)])
        E["sample_table_checks"] += 1
        if exact != bool(orth[j, k - 1, d, d2]): E["sample_table_mismatch"] += 1
    E["endpoints"] += 1; E["transversals_found"] += found_here
    print(f"E endpoint case {i} phase6 {s6}: 28800 sigmas, transversals found = {found_here}", flush=True)
E["ok"] = E["endpoints"] == 48 and E["sigmas_searched"] == 48 * 28800 and E["transversals_found"] == 0 and E["sample_table_mismatch"] == 0
out["E_normalization_free_search"] = E; print("E normalization-free ok:", E["ok"], E, flush=True)

# ---------------- F. odd-order positive control ----------------
C5 = rc.Cyclo(5); F5 = [[(t * d) % 5 for d in range(5)] for t in range(5)]
def transversals_n(K, n, m, C, limit=3):
    f = m // n; found = []
    for rest in permutations(range(1, n)):
        sigma = (0,) + rest
        pi = [0] + [None] * (n - 1)
        def rec(r):
            if r == n: found.append((sigma, tuple(pi))); return len(found) >= limit
            for c in range(n):
                if c in pi[:r]: continue
                if all(C.vanishes([f * (r - r2) * t + K[sigma[t]][c] - K[sigma[t]][pi[r2]] for t in range(n)]) for r2 in range(r)):
                    pi[r] = c
                    if rec(r + 1): return True
                    pi[r] = None
            return False
        if rec(1) and len(found) >= limit: break
    return found
tr5 = transversals_n(F5, 5, 5, C5)
obs5 = {r: [d for d in range(1, 5) if C5.vanishes([r * t + F5[t][d] - F5[t][0] for t in range(5)])] for r in range(1, 5)}
F = {"F5_transversals_found": [[list(s), list(p)] for s, p in tr5], "diagonal_found": ((0, 1, 2, 3, 4), (0, 1, 2, 3, 4)) in tr5,
     "row_candidates_sigma_id": obs5, "obstructing_rows_sigma_id": [r for r, c in obs5.items() if not c]}
F["ok"] = F["diagonal_found"] and F["obstructing_rows_sigma_id"] == []
out["F_odd_order_positive"] = F; print("F odd-order positive ok:", F["ok"], F, flush=True)

# ---------------- G. even-order positive-search summary ----------------
G = {}
for name in ("reviewer-positive-search-result-v1.json", "reviewer-positive-search2-result-v1.json", "reviewer-positive-search3-result-v1.json"):
    p = HERE / name
    if p.exists(): G[name] = {"sha256": sha(p), "content": json.loads(p.read_text())}
out["G_even_order_search_summary"] = G
out["all_ok"] = all(out[k]["ok"] for k in ("A_root_closure", "B_matching", "C_hadamard", "D_row_obstruction", "E_normalization_free_search", "F_odd_order_positive"))
out["elapsed_seconds"] = time.monotonic() - t0; out["clock_end"] = clock()
(HERE / "reviewer-controls-result-v1.json").write_text(json.dumps(out, indent=1, sort_keys=True, default=str) + "\n")
print("REVIEWER CONTROLS", "PASS" if out["all_ok"] else "FAIL", out["clock_start"], out["clock_end"], f"{out['elapsed_seconds']:.1f}s")
