#!/usr/bin/env python3
"""reviewer-endpoints-v1.py  (review f137, reviewer-written; author checkers are NOT imported or executed)

(1) All 24 paths x all 72 phases z = zeta72^s: exact Q(zeta72) half graphs (Phi72 power basis, numpy subset sums),
    perfect-matching test by explicit 945-matching enumeration; Hadamard at every phase; scalar + numeric cross-checks
    on random samples.  Expectation under the candidate: cases 0-3,12-23 have NO matching E at any s; cases 4-11 have
    matching E only at s = 0,12,...,60 (mu6) and there exactly one complementary pair.
(2) Cases 4-11 at the six mu6 phases: direct Q(zeta6) recomputation of the 48 graphs, compared with the Phi72 graphs;
    the normalized matching half E0 (contains K-row 0) compared with the author certificate's even_half.
(3) 48 endpoints x 2880 normalized coordinate orders (sigma(0)=0, sigma(even)=E0, sigma(odd)=complement):
    for every QLS row r=1..9 and column d=1..9 the inner product <v_{0,0}, v_{r,d}> = sum_t zeta10^{rt} zeta6^{K[s(t)][d]-K[s(t)][0]}
    is computed EXACTLY in the reviewer's Q(zeta3)(x)Q(zeta5) tensor basis AND in the Phi30 power basis (must agree) and numerically;
    obstruction set O(sigma) = {r : no d has a vanishing inner product}.  The author's digit for each order must lie in O(sigma).
Writes reviewer-endpoints-result-v1.json with /bin/date receipts.
"""
import importlib.util, json, hashlib, subprocess, time, random
from itertools import combinations, permutations
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("rc", HERE / "reviewer-cyclo-v1.py")
rc = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(rc)
SRC = Path("/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/rqls10")
CAT = SRC / "frontier-20261028-aalto-bh10-6-catalog-v1.txt"
TF = SRC / "frontier-20261028-q18-nonbinary-twentyfour-v1.json"
CERT = SRC / "frontier-20261028-nonbinary-eight-endpoints-v1.json"
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def clock(): return subprocess.run(["/bin/date", "+%Y-%m-%dT%H:%M:%S%z %Z"], capture_output=True, text=True).stdout.strip()
T0 = clock(); t0 = time.monotonic()
inputs = {str(p): sha(p) for p in (CAT, TF, CERT)}

lines = [l for l in CAT.read_text().split("\n") if l]
catalog = [[[int(l[6 + 10 * t + c]) for c in range(10)] for t in range(10)] for l in lines]
recs = json.loads(TF.read_text())["records"]
def load_case(D):
    H = catalog[D["class"] - 1]; co = D["coefficients"]; rects = D["rectangles"]
    R = [[sum(co[j] * int(t in rects[j]["rows"] and c in rects[j]["columns"]) for j in range(4)) for c in range(10)] for t in range(10)]
    return np.array(H, dtype=np.int64), np.array(R, dtype=np.int64)

C72 = rc.Cyclo(72); T72 = np.array(C72.tab, dtype=np.int64)            # (72,24)
C6 = rc.Cyclo(6); C30 = rc.Cyclo(30)
SUB = list(combinations(range(10), 5)); SUBIDX = {E: i for i, E in enumerate(SUB)}
Msub = np.zeros((252, 10), dtype=np.int64)
for e, E in enumerate(SUB):
    Msub[e, list(E)] = 1
PI = np.array(rc.PAIRS, dtype=np.int64)                                  # (45,2)
PM = np.array(rc.PM10, dtype=np.uint64)
SHIFT = np.arange(45, dtype=np.uint64)

def graphs72(K72):
    """edge[e,p] = (sum_{t in SUB[e]} zeta72^{K[t][d]-K[t][c]} == 0) for pair p=(c,d); plus 45-bit masks per E"""
    ex = (K72[:, PI[:, 1]] - K72[:, PI[:, 0]]) % 72                       # (10,45)
    V = T72[ex]                                                          # (10,45,24)
    full_ok = not V.sum(axis=0).any()                                    # Hadamard at this phase (column orthogonality)
    S = np.einsum("es,spk->epk", Msub, V)                                # (252,45,24)
    edge = ~S.any(axis=2)                                                # (252,45)
    masks = (edge.astype(np.uint64) << SHIFT).sum(axis=1, dtype=np.uint64)
    return edge, masks, full_ok

def pm_rows(masks):
    return ((PM[None, :] & ~masks[:, None]) == 0).any(axis=1)            # (252,) bool

# ---------------- (1) all 24 x 72 ----------------
rng = random.Random(1371)
per_case = []; samples_checked = 0; sample_mismatch = 0; had_fail = 0
mu6_graphs = {}   # (case, s) -> edge array for cases 4..11, s%12==0
for i, D in enumerate(recs):
    H, R = load_case(D)
    pm_phases = {}
    for s in range(72):
        K72 = (12 * H + s * R) % 72
        edge, masks, ok = graphs72(K72)
        if not ok:
            had_fail += 1
        pm = pm_rows(masks)
        if pm.any():
            pm_phases[s] = [list(SUB[e]) for e in np.nonzero(pm)[0]]
        if 4 <= i <= 11 and s % 12 == 0:
            mu6_graphs[(i, s)] = edge
        for _ in range(2):   # scalar/numeric cross-check of random entries
            e = rng.randrange(252); p = rng.randrange(45); c, d = rc.PAIRS[p]
            exps = [int(K72[t, d] - K72[t, c]) for t in SUB[e]]
            a = C72.vanishes(exps); b = abs(C72.numeric(exps)) < 1e-9
            samples_checked += 1
            if not (a == b == bool(edge[e, p])):
                sample_mismatch += 1
    per_case.append(dict(case=i, **{"class": D["class"]}, phases_with_matching_E={str(k): v for k, v in pm_phases.items()},
                         n_phases_with_matching=len(pm_phases)))
    print(f"case {i:2d}: phases with a matching half: {sorted(pm_phases)}  (n E per phase: {[len(v) for _, v in sorted(pm_phases.items())]})", flush=True)

# ---------------- (2) mu6 graphs directly in Q(zeta6), and normalized E0 ----------------
cert = json.loads(CERT.read_text())
cert_rec = {(x["case"], x["phase6"]): x for x in cert["records"]}
assert len(cert_rec) == 48 == len(cert["records"])
mu6_summary = []; q6_agree = True
for (i, s), edge in sorted(mu6_graphs.items()):
    H, R = load_case(recs[i]); s6 = s // 12
    K6 = (H + s6 * R) % 6
    edge6 = np.zeros((252, 45), dtype=bool)
    for e, E in enumerate(SUB):
        for p, (c, d) in enumerate(rc.PAIRS):
            edge6[e, p] = C6.vanishes([int(K6[t, d] - K6[t, c]) for t in E])
    if not np.array_equal(edge6, edge):
        q6_agree = False
    masks6 = (edge6.astype(np.uint64) << SHIFT).sum(axis=1, dtype=np.uint64)
    pm = pm_rows(masks6); Es = [SUB[e] for e in np.nonzero(pm)[0]]
    pair_ok = len(Es) == 2 and set(Es[0]) == set(range(10)) - set(Es[1])
    E0 = [E for E in Es if 0 in E]
    E0 = E0[0] if len(E0) == 1 else None
    rec = cert_rec[(i, s6)]
    mu6_summary.append(dict(case=i, phase6=s6, matching_halves=[list(E) for E in Es], exactly_one_complementary_pair=pair_ok,
                            E0=list(E0) if E0 else None, author_even_half=rec["even_half"], E0_matches_author=(E0 is not None and list(E0) == rec["even_half"])))

# ---------------- (3) row-digit obstruction sets ----------------
TT = np.array(rc.TENSOR30, dtype=np.int16)                               # (30,8) reviewer tensor basis
TP = np.array(C30.tab, dtype=np.int16)                                   # (30,8) Phi30 power basis
TN = np.exp(2j * np.pi * np.arange(30) / 30)
tt = np.arange(10, dtype=np.int64)
digit_rows = []; total_orders = 0; digit_failures = 0; rep_disagree = 0
for m in mu6_summary:
    i, s6 = m["case"], m["phase6"]; E0 = tuple(m["E0"])
    H, R = load_case(recs[i]); K6 = (H + s6 * R) % 6
    ev = [t for t in E0 if t]; od = sorted(set(range(10)) - set(E0))
    orders = np.array([[0, b[0], a[0], b[1], a[1], b[2], a[2], b[3], a[3], b[4]]
                       for a in permutations(ev) for b in permutations(od)], dtype=np.int64)   # (2880,10)
    assert orders.shape == (2880, 10) and len({tuple(o) for o in orders}) == 2880
    Kd = K6[orders]                                                      # (2880,10,10) [o,t,c]
    diff = (Kd[:, :, 1:] - Kd[:, :, :1]) % 6                              # (2880,10,9) [o,t,d]
    rr = np.arange(1, 10, dtype=np.int64)
    ex = (3 * rr[None, :, None, None] * tt[None, None, :, None] + 5 * diff[:, None, :, :]) % 30   # (2880,9,10,9) [o,r,t,d]
    nz_t = TT[ex].sum(axis=2, dtype=np.int16).any(axis=3)                # (2880,9,9) nonzero in tensor basis
    nz_p = TP[ex].sum(axis=2, dtype=np.int16).any(axis=3)                # Phi30 power basis
    nz_n = np.abs(TN[ex].sum(axis=2)) > 1e-9                             # numeric
    if not (np.array_equal(nz_t, nz_p) and np.array_equal(nz_t, nz_n)):
        rep_disagree += 1
    obstruct = nz_t.all(axis=2)                                          # (2880,9) [o, r-1]
    digits = cert_rec[(i, s6)]["digits"]; assert len(digits) == 2880
    dig = np.array([int(ch) for ch in digits], dtype=np.int64)
    ok = obstruct[np.arange(2880), dig - 1]
    fails = int((~ok).sum()); digit_failures += fails; total_orders += 2880
    n_obs = obstruct.sum(axis=1)
    always = [int(r) for r in rr if obstruct[:, r - 1].all()]
    never = [int(r) for r in rr if not obstruct[:, r - 1].any()]
    # does any order have NO obstructing row? (then the row certificate could not exist)
    no_obs_orders = int((n_obs == 0).sum())
    # independent weaker check: bipartite candidate graph rows 1..9 x cols 1..9 has a perfect matching?
    digit_rows.append(dict(case=i, phase6=s6, E0=list(E0), author_digit_set=sorted(set(digits)), digit_failures=fails,
                           orders_with_no_obstructing_row=no_obs_orders, min_obstructing_rows=int(n_obs.min()), max_obstructing_rows=int(n_obs.max()),
                           rows_obstructing_for_all_orders=always, rows_never_obstructing=never,
                           row1_obstructs_all_orders=bool(obstruct[:, 0].all())))
    print(f"case {i:2d} phase6 {s6}: E0={list(E0)} digit-failures={fails} no-obstruction-orders={no_obs_orders} "
          f"obstructing-rows per order [{n_obs.min()},{n_obs.max()}] always={always}", flush=True)

out = dict(kind="REVIEWER_INDEPENDENT_ENDPOINT_CHECK", review="f137-rqls10-nonbinary-24paths-literal-no-transversal",
           clock_start=T0, inputs_sha256=inputs, hadamard_failures_over_24x72=had_fail,
           random_samples_checked=samples_checked, random_sample_mismatches=sample_mismatch,
           cases_with_no_matching_half_at_any_phase=[c["case"] for c in per_case if c["n_phases_with_matching"] == 0],
           cases_with_matching_half_only_at_mu6=[c["case"] for c in per_case if c["n_phases_with_matching"] > 0 and
                                                 all(int(s) % 12 == 0 for s in c["phases_with_matching_E"])],
           q6_direct_graphs_agree_with_phi72=q6_agree, mu6_all_exactly_one_pair=all(m["exactly_one_complementary_pair"] for m in mu6_summary),
           mu6_all_E0_match_author=all(m["E0_matches_author"] for m in mu6_summary),
           orders_total=total_orders, author_digit_failures=digit_failures, representation_disagreements=rep_disagree,
           orders_with_no_obstructing_row_total=sum(d["orders_with_no_obstructing_row"] for d in digit_rows),
           row1_obstructs_everywhere=all(d["row1_obstructs_all_orders"] for d in digit_rows),
           per_case=per_case, mu6=mu6_summary, digits=digit_rows, elapsed_seconds=time.monotonic() - t0)
out["clock_end"] = clock()
(HERE / "reviewer-endpoints-result-v1.json").write_text(json.dumps(out, indent=1, sort_keys=True) + "\n")
verdict = (had_fail == 0 and sample_mismatch == 0 and out["cases_with_no_matching_half_at_any_phase"] == list(range(4)) + list(range(12, 24))
           and out["cases_with_matching_half_only_at_mu6"] == list(range(4, 12)) and q6_agree and out["mu6_all_exactly_one_pair"]
           and out["mu6_all_E0_match_author"] and digit_failures == 0 and rep_disagree == 0 and total_orders == 138240)
print("REVIEWER ENDPOINT CHECK", "PASS" if verdict else "FAIL", json.dumps({k: out[k] for k in
      ["hadamard_failures_over_24x72", "random_samples_checked", "random_sample_mismatches", "cases_with_no_matching_half_at_any_phase",
       "cases_with_matching_half_only_at_mu6", "q6_direct_graphs_agree_with_phi72", "mu6_all_exactly_one_pair", "mu6_all_E0_match_author",
       "orders_total", "author_digit_failures", "representation_disagreements", "orders_with_no_obstructing_row_total",
       "row1_obstructs_everywhere", "clock_start", "clock_end", "elapsed_seconds"]}))
