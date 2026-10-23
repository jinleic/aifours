#!/usr/bin/env python3
"""
test_checker_v1.py -- unit tests and mutation tests for checker_v1.py (standard library only,
one process).  Real engine-v3 data are opened read-only; every mutation is applied to an
in-memory copy.  Results are written to a new file (open mode 'x').

Usage:
  TMPDIR=<own tmp dir> python3 test_checker_v1.py --checker checker_v1.py \
      --engine-dir <.../evidence/engine-v3-core56> --out MUTATION-TESTS-v1.json
"""
import argparse
import copy
import gzip
import hashlib
import importlib.util
import itertools
import json
import os
import random
import sys
import time
from fractions import Fraction


def load_checker(path):
    spec = importlib.util.spec_from_file_location("checker_under_test", path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


# ---------------------------------------------------------------- independent naive FH5 evaluator
def naive_fh5_counts(A, typ, a, b, V):
    """Full enumeration of the FH5 assignment space (no pruning), written separately from the
    checker directly from the CERT-FORMAT FH5 text.  Returns the number of NON-rejected
    assignments for each of the 7 E5 placements (None, 0..5).  SAT is 50 here (checker uses 30)."""
    SATX = 50

    def v_p(n, p):
        c = 0
        while n % p == 0:
            n //= p
            c += 1
        return c

    e2v, c2, e3v = typ

    def subsets(t):
        return [frozenset(c) for c in itertools.combinations(range(5), t)]

    doms = []
    for l in range(6):
        if l == a:
            doms.append([(1, frozenset([0]))])
        elif l == b or (l in V and A[l][a] == 1):
            doms.append([(1, frozenset([c])) for c in range(5)])
        elif l in V:
            doms.append([(A[l][a], s) for s in subsets(A[l][a])])
        else:
            doms.append([(t, s) for t in range(1, 6) for s in subsets(t)])

    def lam(l, t, e5):
        x2 = v_p(t, 2) + ((1 if c2 == 1 else SATX) if (e2v is not None and l == e2v) else 0)
        x3 = v_p(t, 3) + (SATX if (e3v is not None and l == e3v) else 0)
        x5 = v_p(t, 5) + (SATX if (e5 is not None and l == e5) else 0)
        return x2, x3, x5

    def fgcd(l, t, l2, t2, e5):
        p, q = lam(l, t, e5), lam(l2, t2, e5)
        return 2 ** min(p[0], q[0]) * 3 ** min(p[1], q[1]) * 5 ** min(p[2], q[2])

    counts = []
    for e5 in [None, 0, 1, 2, 3, 4, 5]:
        acc = 0
        for ch in itertools.product(*doms):
            rej = False
            for i in range(6):
                if ch[i][0] == 1 and any(l != i and A[i][l] > ch[l][0] for l in range(6)):
                    rej = True
                    break
            if not rej:
                for c in range(5):
                    M = [l for l in range(6) if c in ch[l][1]]
                    for r in range(2, len(M) + 1):
                        for T in itertools.combinations(M, r):
                            if all(fgcd(x, ch[x][0], y, ch[y][0], e5) < r for x, y in itertools.combinations(T, 2)):
                                rej = True
                                break
                        if rej:
                            break
                    if rej:
                        break
            acc += not rej
        counts.append(acc)
    return counts


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--checker", required=True)
    ap.add_argument("--engine-dir", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args(argv)
    t0 = time.time()
    C = load_checker(args.checker)
    results = []

    def record(name, kind, expected, observed, detail=""):
        results.append({"name": name, "kind": kind, "expected": expected, "observed": observed,
                        "pass": expected == observed, "detail": str(detail)[:400]})
        print("%-4s %-60s expected %-8s observed %-8s" % ("ok" if expected == observed else "FAIL", name, expected, observed), flush=True)

    def verdict(fn):
        try:
            fn()
            return "ACCEPT", ""
        except C.CertError as e:
            return "REJECT", str(e)

    inputs = {}
    raw = {}
    for name in ("run.json", "orbits.jsonl.gz", "rlp_duals.json", "survivors.json"):
        p = os.path.join(args.engine_dir, name)
        raw[name] = open(p, "rb").read()
        inputs[p] = hashlib.sha256(raw[name]).hexdigest()
    run = C.strict_loads(raw["run.json"])
    duals = C.strict_loads(raw["rlp_duals.json"])
    survivors = C.strict_loads(raw["survivors.json"])
    lines = []
    for n, rl in enumerate(gzip.decompress(raw["orbits.jsonl.gz"]).split(b"\n")):
        if rl.strip():
            lines.append((n, rl) + C.parse_line(rl))      # (n, raw, typ, rep, code, rule, wit)
    cache = C.RLPCache(duals)

    def first(rule, pred=lambda L: True):
        for L in lines:
            if L[5] == rule and pred(L):
                return L
        raise SystemExit("no line for %s" % rule)

    # ============================================================ unit tests (expected values)
    E = [(0, 1), (0, 2), (1, 2), (0, 3), (1, 3), (2, 3), (0, 4), (1, 4), (2, 4), (3, 4),
         (0, 5), (1, 5), (2, 5), (3, 5), (4, 5)]
    record("U01 edge order E", "unit", True, C.EDGES == E)

    def tri(typ, a01, a02, a12):
        A = [[0] * 6 for _ in range(6)]
        A[0][1] = A[1][0] = a01
        A[0][2] = A[2][0] = a02
        A[1][2] = A[2][1] = a12
        return (C.tau_min(A, typ, 0, 1, 2), C.tau_max(A, 0, 1, 2), C.tri_pass(A, typ, 0, 1, 2))

    hand = [  # (type, a01, a02, a12, tau_min, tau_max, pass) computed by hand from the section 2 table
        ((None, 0, None), 2, 3, 4, 12, 6, False),
        ((None, 0, None), 2, 3, 3, 6, 6, True),
        ((None, 0, None), 1, 2, 2, 2, 2, True),
        ((None, 0, None), 1, 1, 2, 2, 1, False),
        ((None, 0, None), 4, 4, 4, 4, 16, True),
        ((None, 0, None), 1, 1, 3, 3, 1, False),
        ((None, 0, 0), 1, 1, 3, 1, 1, True),          # alpha_12=3 opposite E3 -> 3/3 = 1
        ((0, 1, None), 1, 1, 2, 1, 1, True),          # alpha_12=2 opposite E2 -> 1
        ((0, 1, None), 1, 1, 4, 2, 1, False),         # 4/gcd(4, r_E2 class 1)=4/2=2
        ((0, 2, None), 1, 1, 4, 1, 1, True),          # 4/4 = 1
        ((0, 2, None), 1, 4, 4, 4, 4, True),
        ((0, 1, None), 2, 2, 4, 2, 4, True),
        ((0, 1, 1), 3, 3, 3, 3, 9, True),             # 3-edge opposite vertex 1 (E3) -> 1; others 3
    ]
    bad = [h for h in hand if tri(h[0], h[1], h[2], h[3]) != (h[4], h[5], h[6])]
    record("U02 rule T on 13 hand-computed triangles", "unit", True, not bad, bad)

    rng = random.Random(7)
    perms = list(itertools.permutations(range(6)))
    ok = True
    for _ in range(300):
        p, r = rng.choice(perms), rng.choice(perms)
        x = "".join(rng.choice("1234") for _ in range(15))
        pr = tuple(p[r[i]] for i in range(6))
        ok &= C.act(p, C.act(r, x)) == C.act(pr, x)
        A = C.alpha_matrix(x)
        B = C.alpha_matrix(C.act(p, x))
        ok &= all(B[p[i]][p[j]] == A[i][j] for i in range(6) for j in range(6) if i != j)
    record("U03 vertex-permutation action is a group action on codes", "unit", True, ok)

    tc = C.check_types_cover()
    record("U04 91 placements map to exactly one type; stabiliser sizes 720,120x5,24x2", "unit", True,
           tc["placements"] == 91 and sorted(tc["stabiliser_sizes"].values()) == [24, 24, 120, 120, 120, 120, 120, 720], tc)

    A1 = C.alpha_matrix("111111111111111")
    lo, hi, u = C.lohi(A1, (None, 0, None), 0, 1, 2)
    record("U05 grid rounding: cyclic index-5 data give lo = hi = 1/5 (not 1 and 0)", "unit",
           (Fraction(1, 5), Fraction(1, 5)), (lo, hi))

    A2 = [[0] * 6 for _ in range(6)]
    for (i, j) in E:
        A2[i][j] = A2[j][i] = 1
    A2[0][1] = A2[1][0] = 2
    A2[0][2] = A2[2][0] = 3
    A2[1][2] = A2[2][1] = 3
    lo2, hi2, u2 = C.lohi(A2, (None, 0, None), 0, 1, 2)
    record("U06 K2 bar: x_j=2/5<x_k=3/5, alpha_vj+alpha_kj=5>4 => hi=2/5-1/5", "unit", Fraction(1, 5), hi2)

    plain = [(0, 0)] * 5
    record("U07 allowed family, q=(1,1,1,1,1) no markers = 5 singletons", "unit", [1, 2, 4, 8, 16],
           list(C.allowed_masks((1, 1, 1, 1, 1), plain)))
    fam = C.allowed_masks((2, 2, 2, 1, 1), plain)
    record("U08 allowed family, q=(2,2,2,1,1): singletons + the three 2-pairs, no triple", "unit",
           sorted([1, 2, 4, 8, 16, 3, 5, 6]), sorted(fam))
    fam9 = set(C.allowed_masks((1, 4, 4, 4, 2), [(2, 0), (0, 0), (0, 0), (0, 0), (0, 0)]))
    record("U09 class-2 E2 neighbour: {0,1,2,3} allowed, {0,1,2,3,4} not", "unit", (True, False),
           (0b01111 in fam9, 0b11111 in fam9))
    record("U10 hand RLP dual: q all 1, y all 1 accepted", "unit", "ACCEPT",
           verdict(lambda: C.check_rlp_dual((1, 1, 1, 1, 1), plain, {"y": ["1"] * 5}))[0])

    # naive FH5 agreement on real small-space lines
    fh5_small = [L for L in lines if L[5] == "FH5" and L[6][2][0] == 25000][:3]
    agree = []
    for L in fh5_small:
        A = C.alpha_matrix(L[3])
        a, b = L[6][0]
        V = C.fh5_V(A, a, b)
        cnt = naive_fh5_counts(A, L[2], a, b, V)
        r = C.fh5_search(A, L[2], a, b, V)
        agree.append((L[0], cnt, r["status"]))
    record("U11 FH5: naive full enumeration (no pruning) also rejects everything on 3 real lines", "unit",
           True, all(all(c == 0 for c in x[1]) and x[2] == "REFUTED" for x in agree), agree)

    # crafted FH5 case with an accepted assignment
    fh5_typ, fh5_code, fh5_ab = (0, 1, None), "122442442144244", (0, 1)
    Af = C.alpha_matrix(fh5_code)
    Vf = C.fh5_V(Af, 0, 1)
    cntf = naive_fh5_counts(Af, fh5_typ, 0, 1, Vf)
    rf = C.fh5_search(Af, fh5_typ, 0, 1, Vf)
    record("U12 FH5: crafted pattern has accepted assignments (naive) and the search finds one", "unit",
           True, rf["status"] == "ACCEPTED" and all(c > 0 for c in cntf) and C.t_consistent(Af, fh5_typ), (cntf, rf.get("accepted")))

    # ============================================================ positive controls (real lines)
    for rule, pred in (("K", lambda L: True), ("RLP", lambda L: True), ("PB", lambda L: True),
                       ("N26", lambda L: L[2][2] is not None and L[6][0] == L[2][2]),
                       ("RPLP", lambda L: any(c[0] == "P" for c in L[6][1])), ("FH5", lambda L: True)):
        L = first(rule, pred)
        record("P-%s real line %d accepted" % (rule, L[0]), "control", "ACCEPT",
               verdict(lambda: C.check_rule(C.alpha_matrix(L[3]), L[2], L[5], L[6], cache))[0])

    # ============================================================ mutations (must be REJECTED)
    def rej(name, fn):
        v, msg = verdict(fn)
        record(name, "mutation", "REJECT", v, msg)

    # M01 RLP: perturb one y entry so that an allowed-subset sum exceeds 1
    key = "1,1,1,1,1|00;00;00;00;00"
    ent = copy.deepcopy(duals[key])
    ent["y"][2] = str(Fraction(ent["y"][2]) + Fraction(1, 7))
    rej("M01 RLP dual y entry +1/7 (allowed singleton sum > 1)",
        lambda: C.check_rlp_dual((1, 1, 1, 1, 1), plain, ent))

    # M02 RLP: allowed subset {0,4} is the only violated set; dropping it flips the verdict
    q2, st2 = (1, 1, 1, 1, 2), [(1, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
    y2 = {"y": ["1/2", "1/2", "1", "1", "1"]}
    famf = C.allowed_masks(q2, st2)
    v_full = verdict(lambda: C.check_rlp_dual(q2, st2, y2))[0]
    v_drop = verdict(lambda: C.check_rlp_dual(q2, st2, y2, allowed=tuple(S for S in famf if S != 0b10001)))[0]
    record("M02 RLP crafted y: full allowed family rejects; family minus {0,4} would accept", "mutation",
           ("REJECT", "ACCEPT"), (v_full, v_drop))

    # M03 K with a wrong v: a v' outside S with sum_{i in S} alpha_iv' < 5 (computed here directly)
    def k_wrong_v():
        for L in lines:
            if L[5] != "K":
                continue
            v0, S0 = L[6]
            alpha = {E[f]: int(L[3][f]) for f in range(15)}
            for v1 in range(6):
                if v1 == v0 or v1 in S0:
                    continue
                if sum(alpha[(min(i, v1), max(i, v1))] for i in S0) < 5:
                    return L, v0, S0, v1
        return None
    L, v0, S0, v1 = k_wrong_v()
    rej("M03 K witness with a wrong v (line %d, v %d->%d, alpha-sum < 5)" % (L[0], v0, v1),
        lambda: C.check_K(C.alpha_matrix(L[3]), L[2], [v1, S0]))

    # coverage material: real leaves of the smallest type
    t0typ = (None, 0, None)
    leaves0, _ = C.enumerate_leaves(t0typ)
    leafset0 = set(leaves0)
    L0 = [L for L in lines if L[2] == t0typ]
    reps0 = [L[3] for L in L0]
    record("C-cov real (None,0,None) coverage accepted", "control", True,
           C.check_orbit_coverage(t0typ, leafset0, reps0)["ok"])

    # M04 flip one alpha in a rep -> coverage must fail
    reps4 = list(reps0)
    r = reps4[10]
    reps4[10] = ("2" if r[0] != "2" else "3") + r[1:]
    cov4 = C.check_orbit_coverage(t0typ, leafset0, reps4)
    record("M04 one alpha flipped in one rep -> orbit coverage fails", "mutation", "REJECT",
           "ACCEPT" if cov4["ok"] else "REJECT", {k: cov4[k] for k in ("missing", "extra", "duplicate_elements")})

    # M05 duplicate orbit (second line with a rep of an existing orbit)
    reps5 = reps0 + [C.act((1, 0, 2, 3, 4, 5), reps0[20])]
    cov5 = C.check_orbit_coverage(t0typ, leafset0, reps5)
    record("M05 duplicate orbit line -> not disjoint", "mutation", "REJECT", "ACCEPT" if cov5["ok"] else "REJECT",
           {k: cov5[k] for k in ("disjoint", "duplicate_elements")})

    # M06 missing orbit
    cov6 = C.check_orbit_coverage(t0typ, leafset0, reps0[:-1])
    record("M06 one orbit line missing -> union != leaves", "mutation", "REJECT", "ACCEPT" if cov6["ok"] else "REJECT",
           {k: cov6[k] for k in ("missing", "union_equals_leaves")})

    # M07 RPLP P vector violating one column: raise b_x on the column of largest value until it exceeds 1
    L = first("RPLP", lambda L: any(c[0] == "P" for c in L[6][1]))
    wit = copy.deepcopy(L[6])
    pi = [i for i, c in enumerate(wit[1]) if c[0] == "P"][0]
    A7 = C.alpha_matrix(L[3])
    v7 = wit[0]
    sts7 = [C.st_of(j, L[2]) for j in C.nbrs(v7)]
    q7 = C.q_space(A7, v7)[pi]
    vals7 = [Fraction(s) for s in wit[1][pi][1]]

    def colval(Am, Sm):
        val = sum((vals7[x] for x in C.bits(Sm)), Fraction(0)) + sum((vals7[5 + x] for x in C.bits(Am)), Fraction(0))
        for p, (x, y) in enumerate(C.PAIRS5):
            if (Am >> x) & 1 and (Am >> y) & 1:
                val += vals7[20 + p] - vals7[10 + p]
        return val
    cols7 = C.rplp_columns(A7, L[2], v7, q7, sts7)
    Am7, Sm7 = max(cols7, key=lambda c: colval(*c))
    x7 = C.bits(Am7)[0]
    wit[1][pi][1][5 + x7] = str(vals7[5 + x7] + (1 - colval(Am7, Sm7)) + 1)
    rej("M07 RPLP P vector: b_%d raised so column A=%s S=%s exceeds 1, line %d" % (x7, C.bits(Am7), C.bits(Sm7), L[0]),
        lambda: C.check_RPLP(A7, L[2], wit, cache))

    # M08 PB valid only if hi were one unit smaller than the true hi (all-ones pattern, v=0, S={1,2})
    rej("M08 PB witness needing a deflated hi (true hi larger by u) on 111111111111111",
        lambda: C.check_PB(C.alpha_matrix("111111111111111"), (None, 0, None), [0, [1, 2]]))

    # M09 FH5 on a crafted case with an accepted assignment
    rej("M09 FH5 witness on crafted pattern with an accepted assignment",
        lambda: C.check_rule(Af, fh5_typ, "FH5", [[0, 1], Vf, [6250] * 7], cache))

    # M10 N26 at v = E3 with an all-4 neighbour triangle (admissible tau = 12)
    n26code = "224244244424444"     # alpha_0j = 2, alpha_jk = 4 for j,k >= 1
    rej("M10 N26 at v=E3 with (4,4,4) neighbour triangle (tau=12 admissible)",
        lambda: C.check_N26(C.alpha_matrix(n26code), (None, 0, 0), [0]))
    record("C-N26 same pattern at v=E3 with all alpha_jk=2 accepted", "control", "ACCEPT",
           verdict(lambda: C.check_N26(C.alpha_matrix("222222222222222"), (None, 0, 0), [0]))[0])

    # M11 RPLP with two R entries swapped (wrong q order / key)
    L = first("RPLP", lambda L: sum(1 for c in L[6][1] if c[0] == "R") >= 2)
    wit = copy.deepcopy(L[6])
    ri = [i for i, c in enumerate(wit[1]) if c[0] == "R"][:2]
    wit[1][ri[0]], wit[1][ri[1]] = wit[1][ri[1]], wit[1][ri[0]]
    rej("M11 RPLP certs with two R entries swapped (key/q order), line %d" % L[0],
        lambda: C.check_RPLP(C.alpha_matrix(L[3]), L[2], wit, cache))

    # M12 non-T-consistent rep
    badrep = "112" + reps0[0][3:]
    record("M12 rep with a T-forbidden triangle (1,1,2) is not a leaf", "mutation", "REJECT",
           "ACCEPT" if (badrep in leafset0 or C.t_consistent(C.alpha_matrix(badrep), t0typ)) else "REJECT")
    reps12 = list(reps0)
    reps12[0] = badrep
    cov12 = C.check_orbit_coverage(t0typ, leafset0, reps12)
    record("M12b coverage with that rep fails", "mutation", "REJECT", "ACCEPT" if cov12["ok"] else "REJECT")

    # M13 RLP negative y
    ent13 = copy.deepcopy(duals[key])
    ent13["y"][0] = "-1"
    rej("M13 RLP dual with a negative y entry", lambda: C.check_rlp_dual((1, 1, 1, 1, 1), plain, ent13))

    # M14 Ppair where lo <= hi
    rej("M14 Ppair witness on a pair with lo <= hi",
        lambda: C.check_Ppair(C.alpha_matrix("111111111111111"), (None, 0, None), [0, [1, 2]]))

    # M15 RPLP objective < 1: scale the P vector by 1/(2*objective) (columns stay <= 1)
    L = first("RPLP", lambda L: any(c[0] == "P" for c in L[6][1]))
    wit = copy.deepcopy(L[6])
    pi = [i for i, c in enumerate(wit[1]) if c[0] == "P"][0]
    A15 = C.alpha_matrix(L[3])
    v15 = wit[0]
    sts15 = [C.st_of(j, L[2]) for j in C.nbrs(v15)]
    q15 = C.q_space(A15, v15)[pi]
    yhi15, ylo15 = C.rplp_bounds(A15, L[2], v15)
    obj15 = C.check_rplp_vec(A15, L[2], v15, q15, wit[1][pi][1], C.rplp_columns(A15, L[2], v15, q15, sts15), yhi15, ylo15)
    wit[1][pi][1] = [str(Fraction(s) / (2 * obj15)) for s in wit[1][pi][1]]
    rej("M15 RPLP P vector scaled to objective 1/2, line %d" % L[0],
        lambda: C.check_RPLP(A15, L[2], wit, cache))

    # M16 RPLP negative u
    wit = copy.deepcopy(L[6])
    wit[1][pi][1][10] = "-1"
    rej("M16 RPLP P vector with u_0 = -1", lambda: C.check_RPLP(C.alpha_matrix(L[3]), L[2], wit, cache))

    # M17 FH5 wrong V ; M18 FH5 alpha_ab != 1
    L = first("FH5")
    A = C.alpha_matrix(L[3])
    w17 = copy.deepcopy(L[6])
    w17[1] = w17[1][:-1]
    rej("M17 FH5 witness V missing one vertex", lambda: C.check_FH5_witness(A, L[2], w17))
    a, b = L[6][0]
    c18 = [x for x in range(6) if x != a and A[a][x] != 1][0]
    rej("M18 FH5 witness with alpha_ab != 1", lambda: C.check_FH5_witness(A, L[2], [[a, c18], L[6][1], L[6][2]]))

    # M19 SURVIVE line ; M20 survivors.json non-empty ; M21 run.json hash mismatch
    record("M19 a SURVIVE line fails globally", "mutation", "REJECT",
           "REJECT" if C.global_survive_check(["K", "SURVIVE"], [], run) else "ACCEPT")
    rej("M19b check_rule on SURVIVE", lambda: C.check_rule(A, L[2], "SURVIVE", None, cache))
    record("M20 survivors.json non-empty fails globally", "mutation", "REJECT",
           "REJECT" if C.global_survive_check(["K"], [{"rep": "x"}], run) else "ACCEPT")
    k0 = C.tkey(t0typ)
    eng = copy.deepcopy(run["summary"][k0])
    eng["leafcodes_sha256"] = "0" * 64
    rc0 = {}
    for x in L0:
        rc0[x[5]] = rc0.get(x[5], 0) + 1
    real_ok = C.compare_type_summary(k0, len(leaves0), C.leaf_hash(leaves0), len(L0), rc0, run["summary"][k0])
    record("C-sum real run.json summary for (None,0,None) matches", "control", True, real_ok == [], real_ok)
    record("M21 run.json leaf hash altered -> mismatch", "mutation", "REJECT",
           "REJECT" if C.compare_type_summary(k0, len(leaves0), C.leaf_hash(leaves0), len(L0), rc0, eng) else "ACCEPT")

    # M22 N26 with v = E2
    rej("M22 N26 witness with v = E2", lambda: C.check_N26(C.alpha_matrix("222222222222222"), (0, 1, 1), [0]))

    # M23 K with an unlinked pair (add a vertex to S)
    def k_unlinked():
        for L in lines:
            if L[5] != "K":
                continue
            A = C.alpha_matrix(L[3])
            v, S = L[6]
            for w in range(6):
                if w == v or w in S:
                    continue
                if any(C.tau_min(A, L[2], i, v, w) != A[i][v] * A[v][w] for i in S):
                    return L, A, v, S + [w]
        return None
    L, A, v, S = k_unlinked()
    rej("M23 K witness with an added vertex that is not linked (line %d)" % L[0], lambda: C.check_K(A, L[2], [v, S]))

    # M24 RPLP certs list one short
    L = first("RPLP")
    wit = copy.deepcopy(L[6])
    wit[1] = wit[1][:-1]
    rej("M24 RPLP certs list one entry short", lambda: C.check_RPLP(C.alpha_matrix(L[3]), L[2], wit, cache))

    # M25 malformed rationals
    rej("M25 rational given as decimal '0.5'", lambda: C.check_rlp_dual((1, 1, 1, 1, 1), plain, {"y": ["0.5", "1", "1", "1", "1"]}))
    rej("M25b rational with zero denominator", lambda: C.check_rlp_dual((1, 1, 1, 1, 1), plain, {"y": ["1/0", "1", "1", "1", "1"]}))
    rej("M25c rational given as a JSON number", lambda: C.check_rlp_dual((1, 1, 1, 1, 1), plain, {"y": [1, 1, 1, 1, 1]}))

    # M26 malformed lines
    rawK = first("K")[1]

    def mutated_line(**changes):
        obj = json.loads(rawK)
        obj.update(changes)
        return json.dumps(obj).encode()
    record("C-line unmodified K line parses", "control", "ACCEPT", verdict(lambda: C.parse_line(rawK))[0])
    rej("M26 unknown rule name", lambda: C.parse_line(mutated_line(rule="K2")))
    rej("M26b duplicate JSON key in a line", lambda: C.parse_line(rawK[:-1] + b',"rule":"K"}'))
    rej("M26c type not among the 8", lambda: C.parse_line(mutated_line(type=[1, 1, None])))
    rej("M26d boolean in place of an integer type field", lambda: C.parse_line(mutated_line(type=[None, False, None])))
    rej("M26f extra key in a line", lambda: C.parse_line(mutated_line(extra=1)))
    rej("M26g SURVIVE-style line without witness but rule K", lambda: C.parse_line(rawK.split(b',"witness"')[0] + b"}"))
    rej("M26e duplicate key in rlp_duals.json text", lambda: C.strict_loads(b'{"a": {"y": []}, "a": {"y": []}}'))

    # M27 RPLP: a vector violating only an empty-S column
    L = first("RPLP", lambda L: any(c[0] == "P" for c in L[6][1]))
    A = C.alpha_matrix(L[3])
    v = L[6][0]
    N = C.nbrs(v)
    sts = [C.st_of(j, L[2]) for j in N]
    qs = C.q_space(A, v)
    pi = [i for i, c in enumerate(L[6][1]) if c[0] == "P"][0]
    q = qs[pi]
    forced = C.forced_pairs(A, L[2], v)
    cols_all = C.rplp_columns(A, L[2], v, q, sts, forced)
    cols_noempty = C.rplp_columns(A, L[2], v, q, sts, forced, include_empty_S=False)
    Aempty = [Am for (Am, Sm) in cols_all if Sm == 0][0]
    xs = C.bits(Aempty)[0]
    vec27 = ["-100"] * 5 + ["0"] * 5 + ["0"] * 20
    vec27[5 + xs] = "2"
    yhi, ylo = C.rplp_bounds(A, L[2], v)

    def cols_only(cols):
        def f():
            try:
                C.check_rplp_vec(A, L[2], v, q, vec27, cols, yhi, ylo)
            except C.CertError as e:
                if "objective" in str(e):
                    return
                raise
        return f
    record("M27 RPLP vector violating only an empty-S column: rejected with empty S, columns pass without", "mutation",
           ("REJECT", "ACCEPT"), (verdict(cols_only(cols_all))[0], verdict(cols_only(cols_noempty))[0]))

    # M28 RLP with a missing dual entry
    d28 = dict(duals)
    L = first("RLP")
    A = C.alpha_matrix(L[3])
    v = L[6][0]
    k28 = C.rlp_key(C.q_space(A, v)[0], [C.st_of(j, L[2]) for j in C.nbrs(v)])
    del d28[k28]
    rej("M28 RLP line whose first-q dual entry is missing (line %d)" % L[0],
        lambda: C.check_RLP(A, L[2], L[6], C.RLPCache(d28)))

    # M29 line moved to another type -> coverage fails for both types
    t1typ = (None, 0, 0)
    leaves1, _ = C.enumerate_leaves(t1typ)
    reps1 = [L[3] for L in lines if L[2] == t1typ]
    moved = reps1[5]
    cov29a = C.check_orbit_coverage(t1typ, set(leaves1), reps1[:5] + reps1[6:])
    cov29b = C.check_orbit_coverage(t0typ, leafset0, reps0 + [moved])
    record("M29 a line relabelled to another type -> coverage fails", "mutation", "REJECT",
           "ACCEPT" if (cov29a["ok"] and cov29b["ok"]) else "REJECT")

    # M30 N26 with some alpha_vj != 2
    rej("M30 N26 witness where some alpha_vj = 4", lambda: C.check_N26(C.alpha_matrix("422222222222222"), (None, 0, None), [0]))

    # M31 PB S containing v ; M32 K with duplicate S members ; M33 Ppair with j = k
    L = first("PB")
    rej("M31 PB witness whose S contains v", lambda: C.check_PB(C.alpha_matrix(L[3]), L[2], [L[6][0], L[6][1] + [L[6][0]]]))
    L = first("K", lambda L: len(L[6][1]) >= 2)
    rej("M32 K witness with a duplicated S member", lambda: C.check_K(C.alpha_matrix(L[3]), L[2], [L[6][0], L[6][1] + [L[6][1][0]]]))
    rej("M33 Ppair witness with j = k", lambda: C.check_Ppair(C.alpha_matrix("111111111111111"), (None, 0, None), [0, [1, 1]]))

    # M34 FH5 with SAT for prime 5 effectively zero would over-reject: E5-sensitive crafted check
    # (fgcd for e5 = l, t_l = 1 vs t_l' = 5 must be 5)
    record("M34 fgcd(l=e5,t=1 ; l',t'=5) equals 5 (SAT_5 >= 1)", "unit", 5,
           C.fh5_fgcd((None, 0, None), (2, 1), (3, 5), 2))

    # M35 forced containment pairs are ordered: check against a hand case
    # all-ones pattern at v=0: tau_min(0,w,j)=1 >= 1*1 for every ordered pair -> all 20 ordered pairs forced
    record("M35 forced pairs on the all-ones pattern at v=0: all 20 ordered pairs", "unit", 20,
           len(C.forced_pairs(C.alpha_matrix("111111111111111"), (None, 0, None), 0)))
    Ao = C.alpha_matrix("111111111111111")
    Ao[0][1] = Ao[1][0] = 2
    Ao[1][2] = Ao[2][1] = 2
    # v=0, w=1, j=2: tau_min(0,1,2) on (alpha01=2, alpha02=1, alpha12=2) = 2 ; alpha_01*alpha_12 = 4 -> not forced
    # v=0, w=2, j=1: alpha_02*alpha_21 = 2 <= 2 -> forced.  Ordered pairs differ.
    fp = C.forced_pairs(Ao, (None, 0, None), 0)
    record("M35b ordered forced pairs: (w=2,j=1) forced, (w=1,j=2) not", "unit", (True, False),
           ((1, 0) in fp, (0, 1) in fp))

    summary = {"tests": len(results), "passed": sum(1 for r in results if r["pass"]),
               "failed": [r["name"] for r in results if not r["pass"]],
               "mutations": sum(1 for r in results if r["kind"] == "mutation"),
               "mutations_rejected_as_expected": sum(1 for r in results if r["kind"] == "mutation" and r["pass"])}
    out = {"checker": {"path": os.path.abspath(args.checker),
                       "sha256": hashlib.sha256(open(args.checker, "rb").read()).hexdigest()},
           "test_file": {"path": os.path.abspath(__file__),
                         "sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest()},
           "inputs": inputs, "summary": summary, "results": results,
           "seconds": round(time.time() - t0, 1), "python": sys.version}
    with open(args.out, "x") as f:
        json.dump(out, f, indent=1, default=str)
        f.write("\n")
    print(json.dumps(summary, indent=1))
    return 0 if not summary["failed"] else 1


if __name__ == "__main__":
    sys.exit(main())
