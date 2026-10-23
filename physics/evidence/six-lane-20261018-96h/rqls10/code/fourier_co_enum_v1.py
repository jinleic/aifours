#!/usr/bin/env python3
"""fourier_co_enum_v1: EXACT finite enumeration of the Fourier-type clock-orbit family FCO(n) (lane note
evidence/fourier-co-ansatz-v1.md b3a79dd2a87f8d4477188f91e2777c2afc2efa41e431316b028a6c7e49f844bf).

Family. omega = exp(2 pi i / n). For permutations pi, rho of Z_n: q_ij(t) = omega^(t j + pi(t) rho(i)) / sqrt n
(i row, j column, t component); resolution classes C_s = {(i, j): j - i = s mod n} (B = Cay(Z_n) up to isotopy).
Rows and columns are orthonormal for all pi, rho (F1); FCO(n) is a 1-RQLS(n) iff S_pi(i'-i, rho(i')-rho(i)) = 0 for all
i != i', where S_pi(a, b) = sum_t omega^(a t + b pi(t)) (F2).
Exact arithmetic. sum_t omega^(e_t) = 0 iff the integer histogram c_m = #{t: e_t = m mod n}, read as sum_m c_m x^m, is
divisible by the cyclotomic polynomial Phi_n (exact monic integer division; Phi_n built by exact division of x^n - 1).
All norms are exactly 1 by construction (n entries of modulus 1/sqrt n).
Normalisation and coverage. (pi, rho) is a solution iff (pi + d, rho + d') is, for all d, d' in Z_n (F3). For each n the
probe enumerates EVERY permutation pi of Z_n with pi(0) = 0 (no prefilter, no sampling); for each it computes the exact
zero table Z_pi[a][b] (a, b != 0) row by row (row n/2 first for even n) and drops pi as soon as a row has no zero (every
a != 0 occurs as i' - i, so no rho exists); otherwise it finds EVERY rho with rho(0) = 0 and Z_pi[i'-i][rho(i')-rho(i)]
for all i < i' by exhaustive depth-first search (pruning only by that exact condition). Status COMPLETE for n: every
solution of FCO(n) is (pi + d, rho + d') for exactly one enumerated normalised solution and one (d, d'). INCOMPLETE_TIME
or TERMINATED: no conclusion for that n. No fallback, sampling or constraint widening. Lemma F5 (n = 10) is NOT used
for coverage; it is checked as a prediction (row 5 for every pi, column 5 for every pi with a complete table).
Rays (exact). For unit-modulus entries |<q, q'>| = 1 iff t -> e'(t) - e(t) is constant mod n, so two cells hold the same
projective ray iff that difference is constant; this covers every coefficient c = rho(i) - rho(i'), including zero
divisors at even n. Two code paths: R1 union-find over (c, k) with t -> c pi(t) + k t constant (lemma F4); R2 explicit
exponent table of all n^2 vectors and ALL n^2 (n^2 - 1) / 2 cell pairs. G = exact Gram check of all 3n lines
(row / column / class pair counts). R2 and G run for EVERY n = 10 solution and for the first KEEP_FIRST solutions and
every kept maximal example at other n; R1 != R2, or G failing on a solution, is an internal defect (exit 8).
Order and gates (exit 3 on failure; nothing later runs): self-tests (Phi_n degree and value at omega; exact vs floating
test on random histograms incl. constructed vanishing ones); controls n = 2, 4, 6 (COMPLETE, no solution) and n = 3, 5
(COMPLETE, solutions exist, all with exactly n rays) - imports: Zhang-Cao arXiv:2608.29201v2 Sec. 3 (citing
Ball-Simoens): no 1-RQLS(2), 1-RQLS(6); every 1-RQLS(3), 1-RQLS(4), 1-RQLS(5) classical with cardinality v; Cay(Z_4) has
no transversal; n = 7 Huang-Li control; Z symmetry; mutation controls M1-M5. Then n = 8 (recorded), n = 10 (TARGET),
n = 9 (recorded if time remains).
n = 7 control, normalisations stated. Over ALL 5040 permutations mu of Z_7 (no normalisation): complete mappings (mu and
mu + id permutations; expected 133 as in evidence/fixedb_anchors_v1.result.json), affine ones (mu(x) = a x + b; expected
35), non-affine 98. Translation mu -> mu + d acts freely and preserves both properties, so among mu with mu(0) = 0:
19 complete mappings, 5 affine, 14 non-affine (computed directly too). Gate: the FCO(7) normalised solutions with
rho = id are exactly those 19 (set equality) and the ones among them with 49 rays (R1) are exactly the 14 non-affine.
Mutation controls (intended reason): M1 transposing pi(1), pi(2) of a maximal n = 7 solution keeps rows and columns
exact and breaks classes only (t + pi(t) stops being a permutation); M2 adding 1 to one exponent of one cell breaks
exactly the 3 (n - 1) pairs through that cell, n - 1 in each of its row, column and class; M3 pi = 2t, rho = id at
n = 7 is a solution with 7 rays by R1 and R2; M4 (zero divisor, n = 10) pi = [0,3,4,1,2,7,8,9,6,5] (parity preserving,
affine in no direction c != 5), rho = id: R1 = R2 = 50 and every coincident pair has rho(i) - rho(i') = 5 and
j - j' = 5 mod 10; M5 pi = rho = id at n = 10 is not a solution: rows and columns exact, classes fail.
Immediate stop: the first n = 10 solution with 100 rays by R1 or R2 is written in full (pi, rho, conventions, exponent
table, G, R1, R2) and the probe exits 7 at once.
Protocol: reads one line from stdin and requires "GO" (else exit 6, no output); SIGTERM sets a flag honoured by the
cooperative checks (status TERMINATED, exit 5). Cooperative self budget 240 s (checked per pi, every 2048 search nodes
and every 256 solutions). Single process, standard library, no input files; output one JSON (exclusive create).
Usage: fourier_co_enum_v1.py OUT.json. Exit: 0 finished (per-n status recorded), 3 gate failure, 5 SIGTERM,
6 no GO, 7 maximal n = 10 candidate, 8 internal defect.
"""
import cmath, itertools, json, math, random, signal, sys, time

TERM = [False]
signal.signal(signal.SIGTERM, lambda s, f: TERM.__setitem__(0, True))
if sys.stdin.readline().strip() != "GO":
    sys.exit(6)
T0 = time.monotonic()
OUT = sys.argv[1]
BUDGET = 240.0
KEEP_FIRST, KEEP_MAX, KEEP_N10 = 5, 20, 50


class Timeout(Exception):
    pass


class Terminated(Exception):
    pass


class Stop(Exception):
    def __init__(self, code, reason, payload):
        Exception.__init__(self, reason)
        self.code, self.reason, self.payload = code, reason, payload


def check_time():
    if TERM[0]:
        raise Terminated()
    if time.monotonic() - T0 > BUDGET:
        raise Timeout()


def pdiv(a, b):
    a = list(a)
    db = len(b) - 1
    q = [0] * (len(a) - db)
    for i in range(len(a) - 1, db - 1, -1):
        c = a[i]
        if c:
            q[i - db] = c
            for j in range(db + 1):
                a[i - db + j] -= c * b[j]
    assert not any(a[:db])
    return q


CYC = {}


def cyclo(n):
    if n not in CYC:
        num = [-1] + [0] * (n - 1) + [1]
        for d in range(1, n):
            if n % d == 0:
                num = pdiv(num, cyclo(d))
        CYC[n] = num
    return CYC[n]


def vanish(c, n):
    a = list(c)
    b = cyclo(n)
    db = len(b) - 1
    for i in range(len(a) - 1, db - 1, -1):
        x = a[i]
        if x:
            for j in range(db + 1):
                a[i - db + j] -= x * b[j]
    return not any(a[:db])


def row_order(n):
    if n % 2 == 0:
        return [n // 2] + [a for a in range(1, n) if a != n // 2]
    return list(range(1, n))


def ztable(pi, n):
    Z = [[False] * n for _ in range(n)]
    for a in row_order(n):
        hit = False
        for b in range(1, n):
            c = [0] * n
            for t in range(n):
                c[(a * t + b * pi[t]) % n] += 1
            if vanish(c, n):
                Z[a][b] = True
                hit = True
        if not hit:
            return Z, a
    return Z, None


def enumerate_rho(Z, n, on_solution, stats):
    rho = [0] * n
    used = [False] * n
    used[0] = True

    def rec(i):
        if i == n:
            on_solution(tuple(rho))
            return
        for v in range(1, n):
            if used[v]:
                continue
            stats["nodes"] += 1
            if stats["nodes"] % 2048 == 0:
                check_time()
            ok = True
            for ip in range(i):
                if not Z[i - ip][(v - rho[ip]) % n]:
                    ok = False
                    break
            if ok:
                rho[i] = v
                used[v] = True
                rec(i + 1)
                used[v] = False
    rec(1)


def exps(pi, rho, n):
    return [[[(t * j + pi[t] * rho[i]) % n for t in range(n)] for j in range(n)] for i in range(n)]


def gram_check(E, n):
    fams = (("rows", [[(i, j) for j in range(n)] for i in range(n)]),
            ("columns", [[(i, j) for i in range(n)] for j in range(n)]),
            ("classes", [[(i, (i + s) % n) for i in range(n)] for s in range(n)]))
    bad, bad_pairs = {}, []
    for f, lines in fams:
        cnt = 0
        for L in lines:
            for x in range(n):
                for y in range(x + 1, n):
                    e1, e2 = E[L[x][0]][L[x][1]], E[L[y][0]][L[y][1]]
                    c = [0] * n
                    for t in range(n):
                        c[(e2[t] - e1[t]) % n] += 1
                    if not vanish(c, n):
                        cnt += 1
                        if len(bad_pairs) < 64:
                            bad_pairs.append([f, list(L[x]), list(L[y])])
        bad[f] = cnt
    return bad, bad_pairs


def rays_r1(pi, rho, n):
    parent = list(range(n * n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    dirs = set()
    for i in range(n):
        for ip in range(i + 1, n):
            c = (rho[i] - rho[ip]) % n
            for k in range(n):
                v0 = (c * pi[0]) % n
                if all((c * pi[t] + k * t) % n == v0 for t in range(1, n)):
                    dirs.add((c, k))
                    for j in range(n):
                        parent[find(i * n + j)] = find(ip * n + (j - k) % n)
    return len({find(x) for x in range(n * n)}), sorted(dirs)


def rays_r2(E, n):
    cells = [(i, j) for i in range(n) for j in range(n)]
    parent = list(range(n * n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    pairs = []
    npairs = 0
    for a in range(n * n):
        ea = E[cells[a][0]][cells[a][1]]
        for b in range(a + 1, n * n):
            eb = E[cells[b][0]][cells[b][1]]
            d0 = (eb[0] - ea[0]) % n
            if all((eb[t] - ea[t]) % n == d0 for t in range(1, n)):
                npairs += 1
                parent[find(a)] = find(b)
                pairs.append((cells[a], cells[b]))
    return len({find(x) for x in range(n * n)}), npairs, pairs


def affine_direction(pi, n):
    for c in range(1, n):
        for k in range(n):
            v0 = (c * pi[0]) % n
            if all((c * pi[t] + k * t) % n == v0 for t in range(1, n)):
                return [c, k]
    return None


def full_record(pi, rho, n, r1, dirs):
    E = exps(pi, rho, n)
    g, gp = gram_check(E, n)
    r2, npairs, _ = rays_r2(E, n)
    rec = {"n": n, "pi": list(pi), "rho": list(rho), "rays_R1": r1, "rays_R2": r2, "coincident_pairs_R2": npairs,
           "R1_directions": [list(d) for d in dirs], "gram_bad_pairs": g, "gram_bad_examples": gp,
           "affine_direction": affine_direction(pi, n)}
    return rec, E


out = {"probe": "fourier_co_enum_v1", "budget_s": BUDGET, "per_n": {}, "self_tests": {}, "controls": {}, "gates": {},
       "convention": "q_ij(t) = omega^(t*j + pi(t)*rho(i)) / sqrt(n), omega = exp(2 pi i / n), classes {(i,j): j - i = s mod n}"}
P = out["per_n"]
F5 = {"row5_mismatch": 0, "row5_checked": 0, "col5_mismatch": 0, "col5_checked": 0}
ZSYM = [0]
N7 = {"rho_id": set(), "rho_id_max": set()}
N10 = []


def gate(name, ok, detail):
    out["gates"][name] = {"pass": bool(ok), "detail": detail}
    if not ok:
        raise Stop(3, "gate failed: " + name, None)


def run_n(n):
    R = {"status": "RUNNING", "pi_total": math.factorial(n - 1), "pi_enumerated": 0, "pi_row_fail_hist": {},
         "pi_full_table": 0, "pi_with_solution": 0, "solutions": 0, "maximal": 0, "rays_hist": {}, "nodes": 0,
         "max_nodes_per_pi": 0, "first": [], "maximal_examples": []}
    P[str(n)] = R
    t1 = time.monotonic()
    IDN = tuple(range(n))
    try:
        for perm in itertools.permutations(range(1, n)):
            check_time()
            R["pi_enumerated"] += 1
            pi = (0,) + perm
            Z, fa = ztable(pi, n)
            if n == 10:
                F5["row5_checked"] += 1
                row5 = any(Z[5][b] for b in range(1, 10))
                F5["row5_mismatch"] += int(row5 != (len({pi[t] % 5 for t in (0, 2, 4, 6, 8)}) == 5))
            if fa is not None:
                R["pi_row_fail_hist"][str(fa)] = R["pi_row_fail_hist"].get(str(fa), 0) + 1
                continue
            R["pi_full_table"] += 1
            ZSYM[0] += sum(1 for a in range(1, n) for b in range(1, n) if Z[a][b] != Z[n - a][n - b])
            if n == 10:
                F5["col5_checked"] += 1
                col5 = any(Z[a][5] for a in range(1, 10))
                F5["col5_mismatch"] += int(col5 != (len({t % 5 for t in range(10) if pi[t] % 2 == 0}) == 5))
            st = {"nodes": 0}
            found = [0]

            def on_solution(rho):
                found[0] += 1
                R["solutions"] += 1
                if R["solutions"] % 256 == 0:
                    check_time()
                r1, dirs = rays_r1(pi, rho, n)
                R["rays_hist"][str(r1)] = R["rays_hist"].get(str(r1), 0) + 1
                if r1 == n * n:
                    R["maximal"] += 1
                if n == 7 and rho == IDN:
                    N7["rho_id"].add(pi)
                    if r1 == 49:
                        N7["rho_id_max"].add(pi)
                full = n == 10 or len(R["first"]) < KEEP_FIRST or (r1 == n * n and len(R["maximal_examples"]) < KEEP_MAX)
                if not full:
                    return
                rec, E = full_record(pi, rho, n, r1, dirs)
                if rec["rays_R2"] != r1 or sum(rec["gram_bad_pairs"].values()) != 0:
                    raise Stop(8, "internal defect: R1/R2 disagree or exact Gram fails on a solution",
                               dict(rec, exponent_table=E))
                if n == 10 and (r1 == 100 or rec["rays_R2"] == 100):
                    raise Stop(7, "maximal FCO(10) solution: CANDIDATE pending independent verification",
                               dict(rec, exponent_table=E))
                if n == 10 and len(N10) < KEEP_N10:
                    N10.append(rec)
                if len(R["first"]) < KEEP_FIRST:
                    R["first"].append(rec)
                if r1 == n * n and len(R["maximal_examples"]) < KEEP_MAX:
                    R["maximal_examples"].append(rec)

            enumerate_rho(Z, n, on_solution, st)
            R["nodes"] += st["nodes"]
            R["max_nodes_per_pi"] = max(R["max_nodes_per_pi"], st["nodes"])
            if found[0]:
                R["pi_with_solution"] += 1
        R["status"] = "COMPLETE"
    except Timeout:
        R["status"] = "INCOMPLETE_TIME"
    except Terminated:
        R["status"] = "TERMINATED"
        raise
    finally:
        R["elapsed_s"] = round(time.monotonic() - t1, 3)
    return R


def controls():
    rng = random.Random(20261019)
    st = {}
    for n in range(2, 11):
        ph = cyclo(n)
        w = cmath.exp(2j * math.pi / n)
        st[str(n)] = {"degree": len(ph) - 1, "phi_n": sum(1 for k in range(1, n + 1) if math.gcd(k, n) == 1),
                      "abs_at_omega": abs(sum(cf * w ** k for k, cf in enumerate(ph)))}
    mism, nvan = 0, 0
    for _ in range(3000):
        n = rng.randint(2, 10)
        w = cmath.exp(2j * math.pi / n)
        if rng.random() < 0.5:
            c = [rng.randint(0, 3) for _ in range(n)]
        else:
            c = [0] * n
            for _ in range(rng.randint(1, 4)):
                q = rng.choice([d for d in range(2, n + 1) if n % d == 0])
                r = rng.randrange(n // q)
                for m in range(q):
                    c[r + m * (n // q)] += 1
            if rng.random() < 0.3:
                c[rng.randrange(n)] += 1
        fl = abs(sum(cf * w ** m for m, cf in enumerate(c))) < 1e-9
        ex = vanish(c, n)
        nvan += int(ex)
        mism += int(fl != ex)
    out["self_tests"] = {"phi": st, "exact_vs_float": {"n": 3000, "vanishing": nvan, "mismatches": mism}}
    gate("self_tests", mism == 0 and nvan > 0 and all(v["degree"] == v["phi_n"] and v["abs_at_omega"] < 1e-9
                                                      for v in st.values()), {"mismatches": mism, "vanishing": nvan})
    for n in (2, 3, 4, 5, 6, 7):
        run_n(n)
    for n in (2, 4, 6):
        gate("n%d_no_solution" % n, P[str(n)]["status"] == "COMPLETE" and P[str(n)]["solutions"] == 0,
             {"status": P[str(n)]["status"], "solutions": P[str(n)]["solutions"]})
    for n in (3, 5):
        gate("n%d_only_%d_rays" % (n, n), P[str(n)]["status"] == "COMPLETE" and P[str(n)]["solutions"] > 0
             and set(P[str(n)]["rays_hist"]) == {str(n)}, {"status": P[str(n)]["status"], "rays_hist": P[str(n)]["rays_hist"]})
    cm_all, aff_all = [], []
    for mu in itertools.permutations(range(7)):
        if len({(mu[x] + x) % 7 for x in range(7)}) == 7:
            cm_all.append(mu)
            a = (mu[1] - mu[0]) % 7
            aff_all.append(all(mu[x] == (a * x + mu[0]) % 7 for x in range(7)))
    cm0 = {mu for mu in cm_all if mu[0] == 0}
    na0 = {mu for mu, af in zip(cm_all, aff_all) if mu[0] == 0 and not af}
    hl = {"complete_mappings_all": len(cm_all), "affine_all": sum(aff_all), "nonaffine_all": len(cm_all) - sum(aff_all),
          "normalised_mu0_0": len(cm0), "normalised_nonaffine": len(na0),
          "fco7_rho_id": len(N7["rho_id"]), "fco7_rho_id_49_rays": len(N7["rho_id_max"]),
          "set_equal_rho_id": N7["rho_id"] == cm0, "set_equal_maximal": N7["rho_id_max"] == na0}
    out["controls"]["n7_huang_li"] = hl
    gate("n7_huang_li", P["7"]["status"] == "COMPLETE" and hl["complete_mappings_all"] == 133 and hl["affine_all"] == 35
         and hl["normalised_mu0_0"] == 19 and hl["normalised_nonaffine"] == 14 and hl["set_equal_rho_id"]
         and hl["set_equal_maximal"], hl)
    gate("z_symmetry", ZSYM[0] == 0, {"violations": ZSYM[0]})
    # M1, M2: maximal n = 7 solution (first non-affine normalised complete mapping, rho = id)
    pis = sorted(na0)[0]
    E = exps(pis, tuple(range(7)), 7)
    g0, _ = gram_check(E, 7)
    pm = list(pis)
    pm[1], pm[2] = pm[2], pm[1]
    g1, _ = gram_check(exps(tuple(pm), tuple(range(7)), 7), 7)
    E2 = [[list(v) for v in row] for row in E]
    E2[2][3][4] = (E2[2][3][4] + 1) % 7
    g2, bp2 = gram_check(E2, 7)
    m2_cell_in_all = all([2, 3] in (p[1], p[2]) for p in bp2)
    out["controls"]["M1_M2"] = {"pi": list(pis), "base": g0, "M1_transposed": g1, "M2_one_exponent": g2,
                                "M2_all_bad_pairs_contain_cell": m2_cell_in_all}
    gate("M1_classes_only", sum(g0.values()) == 0 and g1["rows"] == 0 and g1["columns"] == 0 and g1["classes"] > 0,
         {"base": g0, "mutated": g1})
    gate("M2_lines_through_cell", g2 == {"rows": 6, "columns": 6, "classes": 6} and m2_cell_in_all, {"bad": g2})
    # M3: affine solution, 7 rays
    p3 = tuple((2 * t) % 7 for t in range(7))
    r1, _ = rays_r1(p3, tuple(range(7)), 7)
    E3 = exps(p3, tuple(range(7)), 7)
    r2, _, _ = rays_r2(E3, 7)
    g3, _ = gram_check(E3, 7)
    out["controls"]["M3"] = {"R1": r1, "R2": r2, "gram": g3}
    gate("M3_affine_7_rays", r1 == 7 and r2 == 7 and sum(g3.values()) == 0, out["controls"]["M3"])
    # M4: zero-divisor coincidences at n = 10
    p4 = (0, 3, 4, 1, 2, 7, 8, 9, 6, 5)
    id10 = tuple(range(10))
    r1, dirs = rays_r1(p4, id10, 10)
    r2, npairs, pairs = rays_r2(exps(p4, id10, 10), 10)
    only55 = all(((a[0] - b[0]) % 10 == 5 and (a[1] - b[1]) % 10 == 5) for a, b in pairs)
    out["controls"]["M4"] = {"R1": r1, "R2": r2, "pairs": npairs, "R1_directions": [list(d) for d in dirs],
                             "all_pairs_c5_k5": only55}
    gate("M4_zero_divisor", r1 == 50 and r2 == 50 and npairs == 50 and only55 and {d[0] for d in dirs} == {5},
         out["controls"]["M4"])
    # M5: pi = rho = id at n = 10 is not a solution
    g5, _ = gram_check(exps(id10, id10, 10), 10)
    out["controls"]["M5"] = g5
    gate("M5_not_solution", g5["rows"] == 0 and g5["columns"] == 0 and g5["classes"] > 0, g5)


code = 0
try:
    controls()
    run_n(8)
    R10 = run_n(10)
    out["F5_prediction_checks"] = dict(F5)
    if R10["status"] == "COMPLETE":
        run_n(9)
    else:
        P["9"] = {"status": "NOT_DONE"}
except Stop as ex:
    code = ex.code
    out["stop"] = {"code": ex.code, "reason": ex.reason, "payload": ex.payload}
except Terminated:
    code = 5
    out["stop"] = {"code": 5, "reason": "SIGTERM"}
for n in (2, 3, 4, 5, 6, 7, 8, 10, 9):
    if str(n) not in P:
        P[str(n)] = {"status": "NOT_DONE"}
    elif P[str(n)].get("status") == "RUNNING":
        P[str(n)]["status"] = "INCOMPLETE_STOPPED"
out["F5_prediction_checks"] = dict(F5)
out["n10_solution_records"] = N10
out["n10"] = {k: P["10"].get(k) for k in ("status", "pi_total", "pi_enumerated", "pi_full_table", "pi_with_solution",
                                           "solutions", "maximal", "rays_hist")}
out["exit_code"] = code
out["elapsed_s"] = round(time.monotonic() - T0, 3)
with open(OUT, "x", encoding="utf-8") as fh:
    json.dump(out, fh)
print(json.dumps({"exit": code, "gates": {k: v["pass"] for k, v in out["gates"].items()}, "n10": out["n10"],
                  "F5": out["F5_prediction_checks"],
                  "per_n": {k: {kk: v.get(kk) for kk in ("status", "pi_enumerated", "pi_full_table", "pi_with_solution",
                                                         "solutions", "maximal", "rays_hist", "elapsed_s")}
                            for k, v in P.items()},
                  "stop": out.get("stop", {}).get("reason"), "elapsed_s": out["elapsed_s"]}))
sys.exit(code)
