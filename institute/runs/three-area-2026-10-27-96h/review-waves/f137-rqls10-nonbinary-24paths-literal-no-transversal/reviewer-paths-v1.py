#!/usr/bin/env python3
"""reviewer-paths-v1.py  (review f137, reviewer-written; author checkers are NOT imported or executed)

Reconstructs the 24 literal paths K(z) = H (.) z^{sum_j co_j M_j} from the literal catalog line (class) and the
rectangle/coefficient records, then checks with the reviewer's own exact arithmetic (reviewer-cyclo-v1.py):
 (a) every catalog line used is BH(10,6); K(z) is Hadamard IDENTICALLY in z (exact Laurent coefficients in Q(omega));
 (b) the record field K_exponents_mod18 equals 3H+R mod 18 (ties the path to its q18 endpoint K(zeta18));
 (c) all 24*252*45 = 272160 half-polynomials P_{E,c,d}(z) = sum_{t in E} zeta6^{H[t][d]-H[t][c]} z^{R[t][d]-R[t][c]};
     identity edges (P == 0) and distinct monic normal forms of the nonzero ones;
 (d) mu72 root closure for EVERY distinct nonzero P by the reviewer's layer-stripping method, plus census of
     non-constant gcd(P,P*), repeated roots, and failures of the earlier too-strong test G | z^72-1;
 (e) the identity-edge graph of every (case, E) has no perfect matching (explicit 945-matching enumeration);
 (f) numeric cross-check (numpy.roots) that every unit-modulus root of every distinct P is numerically a 72nd root of unity;
 (g) exceptional phase census: which exponents k (zeta72^k) occur as roots of some gcd(P,P*) per case.
Writes reviewer-paths-result-v1.json with /bin/date clock receipts and input SHA-256s.
"""
import importlib.util, json, hashlib, subprocess, time
from itertools import combinations
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("rc", HERE / "reviewer-cyclo-v1.py")
rc = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(rc)
SRC = Path("/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/rqls10")
CAT = SRC / "frontier-20261028-aalto-bh10-6-catalog-v1.txt"
TF = SRC / "frontier-20261028-q18-nonbinary-twentyfour-v1.json"

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def clock(): return subprocess.run(["/bin/date", "+%Y-%m-%dT%H:%M:%S%z %Z"], capture_output=True, text=True).stdout.strip()

T0 = clock(); t0 = time.monotonic()
inputs = {str(CAT): sha(CAT), str(TF): sha(TF)}

# ---------------- literal catalog lines ----------------
C6 = rc.Cyclo(6)
lines = [l for l in CAT.read_text().split("\n") if l]
assert len(lines) == 34
catalog = []
cat_hadamard = []
for l in lines:
    assert l.startswith("BH1::6") and len(l) == 106 and set(l[6:]) <= set("012345"), l[:12]
    H = [[int(l[6 + 10 * t + c]) for c in range(10)] for t in range(10)]
    ok = all(C6.vanishes([H[r][c] - H[s][c] for c in range(10)]) for r, s in combinations(range(10), 2))
    catalog.append(H); cat_hadamard.append(ok)

# ---------------- the 24 literal cases ----------------
tf = json.loads(TF.read_text()); recs = tf["records"]; assert len(recs) == 24
Z6 = rc.ZETA6
def load_case(D):
    H = catalog[D["class"] - 1]
    co = D["coefficients"]; rects = D["rectangles"]; assert len(co) == 4 == len(rects)
    R = [[sum(co[j] * int(t in rects[j]["rows"] and c in rects[j]["columns"]) for j in range(4)) for c in range(10)] for t in range(10)]
    return H, R

def hadamard_identically(H, R):
    """K(z)K(z)^* = 10 I as Laurent identity: for rows r != s, sum_c zeta6^{H[r][c]-H[s][c]} z^{R[r][c]-R[s][c]} == 0"""
    for r, s in combinations(range(10), 2):
        acc = {}
        for c in range(10):
            k = R[r][c] - R[s][c]
            acc[k] = acc.get(k, rc.Qw(0)) + Z6[(H[r][c] - H[s][c]) % 6]
        if any(not v.iszero() for v in acc.values()):
            return False
    return True

closure_cache = {}
def closure_info(key):
    if key not in closure_cache:
        P = list(key)
        G = rc.qgcd(P, rc.reciprocal_conj(P))
        nonconst = len(G) > 1
        rep = nonconst and len(rc.qgcd(G, rc.qderiv(G))) > 1
        closure = rc.unit_root_closure(P)
        naive = rc.naive_closure(P)
        # exceptional exponents: k with G(zeta72^k) = 0, found exactly by gcd with (z - zeta72^k)? zeta72 not in Q(omega);
        # instead record deg G and which cyclotomic factors Phi_d (d | 72) divide G (exact division test).
        facs = []
        if nonconst:
            for d in rc.divisors(72):
                phid = [rc.Qw(c) for c in rc.cyclotomic(d)]
                # Phi_d may split over Q(omega) (d divisible by 3): test gcd degree instead of divisibility
                g = rc.qgcd(G, phid)
                if len(g) > 1:
                    facs.append([d, len(g) - 1])
        closure_cache[key] = dict(nonconst_gcd=nonconst, deg_gcd=len(G) - 1 if nonconst else 0,
                                  repeated_root=rep, closure=closure, naive=naive, cyclotomic_parts=facs)
    return closure_cache[key]

results = []
total_polys = 0
for i, D in enumerate(recs):
    assert D["case"] == i
    H, R = load_case(D)
    nmax = max(map(max, R)); nmin = min(map(min, R))
    k18 = D["K_exponents_mod18"]
    k18_match = all((3 * H[t][c] + R[t][c]) % 18 == k18[t][c] for t in range(10) for c in range(10))
    had = hadamard_identically(H, R)
    distinct = set(); n_identity_edges = 0; pm_count = 0; n_nonzero = 0
    for E in combinations(range(10), 5):
        edges = []
        for c, d in rc.PAIRS:
            acc = {}
            for t in E:
                k = R[t][d] - R[t][c]
                acc[k] = acc.get(k, rc.Qw(0)) + Z6[(H[t][d] - H[t][c]) % 6]
            key = rc.laurent_to_poly(acc)
            if key is None:
                edges.append((c, d)); n_identity_edges += 1
            else:
                distinct.add(key); n_nonzero += 1
        if rc.has_pm(rc.edges_to_mask(edges)):
            pm_count += 1
    total_polys += n_nonzero + n_identity_edges
    infos = [closure_info(k) for k in distinct]
    nonconst = sum(1 for x in infos if x["nonconst_gcd"]); rep = sum(1 for x in infos if x["repeated_root"])
    naive_fail = sum(1 for x in infos if not x["naive"]); closure_fail = sum(1 for x in infos if not x["closure"])
    parts = {}
    for x in infos:
        for d, m in x["cyclotomic_parts"]:
            parts[d] = parts.get(d, 0) + 1
    results.append(dict(case=i, **{"class": D["class"]}, coefficients=D["coefficients"], catalog_line_hadamard=cat_hadamard[D["class"] - 1],
                        R_min=nmin, R_max=nmax, hadamard_identically_in_z=had, K_exponents_mod18_equals_3H_plus_R=k18_match,
                        halfpolys_total=n_nonzero + n_identity_edges, identity_edges=n_identity_edges,
                        distinct_nonzero_monic=len(distinct), identity_graphs_with_perfect_matching=pm_count,
                        distinct_with_nonconstant_gcd=nonconst, distinct_with_repeated_gcd_root=rep,
                        naive_test_failures=naive_fail, reviewer_closure_failures=closure_fail,
                        gcd_cyclotomic_parts_count_by_d={str(k): v for k, v in sorted(parts.items())}))
    print(f"case {i:2d} class {D['class']:2d} had={had} k18={k18_match} distinct={len(distinct)} pm={pm_count} "
          f"nonconst={nonconst} rep={rep} naive_fail={naive_fail} closure_fail={closure_fail}", flush=True)

# ---------------- numeric cross-check of every distinct polynomial ----------------
worst_unit = 0.0; n_unit_roots = 0; n_checked = 0
z72 = np.exp(2j * np.pi * np.arange(72) / 72)
for key in closure_cache:
    coeffs = np.array([x.complex() for x in reversed(key)])
    roots = np.roots(coeffs) if len(coeffs) > 1 else np.array([])
    n_checked += 1
    for r in roots:
        if abs(abs(r) - 1) < 1e-5:
            n_unit_roots += 1
            worst_unit = max(worst_unit, float(np.min(np.abs(z72 - r))))
numeric_ok = worst_unit < 1e-3   # repeated roots lose precision in np.roots; this is a sanity check, not the proof

out = dict(kind="REVIEWER_INDEPENDENT_PATH_CHECK", review="f137-rqls10-nonbinary-24paths-literal-no-transversal",
           clock_start=T0, inputs_sha256=inputs, catalog_lines=len(lines), catalog_lines_hadamard=sum(cat_hadamard),
           total_halfpolynomials=total_polys, distinct_nonzero_monic_global=len(closure_cache),
           all_hadamard_identically=all(r["hadamard_identically_in_z"] for r in results),
           all_k18_match=all(r["K_exponents_mod18_equals_3H_plus_R"] for r in results),
           all_R_max_6=all(r["R_max"] == 6 for r in results), all_R_min_0=all(r["R_min"] == 0 for r in results),
           identity_graphs_with_pm_total=sum(r["identity_graphs_with_perfect_matching"] for r in results),
           reviewer_closure_failures_total=sum(r["reviewer_closure_failures"] for r in results),
           naive_failures_total=sum(r["naive_test_failures"] for r in results),
           cases_with_naive_failures=[r["case"] for r in results if r["naive_test_failures"]],
           cases_with_repeated_gcd_roots=[r["case"] for r in results if r["distinct_with_repeated_gcd_root"]],
           numeric_unit_roots_checked=n_unit_roots, numeric_polys_checked=n_checked,
           numeric_worst_distance_to_mu72=worst_unit, numeric_ok=numeric_ok,
           cases=results, elapsed_seconds=time.monotonic() - t0)
out["clock_end"] = clock()
(HERE / "reviewer-paths-result-v1.json").write_text(json.dumps(out, indent=1, sort_keys=True) + "\n")
verdict = (out["all_hadamard_identically"] and out["all_k18_match"] and out["identity_graphs_with_pm_total"] == 0
           and out["reviewer_closure_failures_total"] == 0 and total_polys == 24 * 252 * 45 and numeric_ok)
print("REVIEWER PATH CHECK", "PASS" if verdict else "FAIL", json.dumps({k: out[k] for k in
      ["total_halfpolynomials", "distinct_nonzero_monic_global", "identity_graphs_with_pm_total", "reviewer_closure_failures_total",
       "naive_failures_total", "cases_with_naive_failures", "cases_with_repeated_gcd_roots", "numeric_worst_distance_to_mu72",
       "clock_start", "clock_end", "elapsed_seconds"]}))
