#!/usr/bin/env python3
"""size24-check-v1.py -- f117 reviewer's independent check of the |P|=24 branch of the
order-1320 Shor border no-go candidate (frontier-20261028-1320-border-no-go-candidate-v1.md, s.6).

Written from scratch by the f117 reviewer from the elementary integers n=1320,
A={0,3,8,11} (old heads, subset of P) and Y={0,1,7,13,14} (old tails, subset of Q).
No author program is imported, executed or copied.  The only author-originated data
reused here is the literal 22-residue positive-control list W_AUTHOR quoted from the
author's text, used solely as a *claim* to be verified by the reviewer's own verifier.

Premises taken as given (NOT established here; see size24-review-v1.md):
  (T) P + Q = Z_1320 is a direct tiling (border theorem), A subset P, Y subset Q, |P|=24.
  (S) Sands' theorem, necessary direction: no nonzero difference of P and nonzero
      difference of Q have the same gcd with 1320.
Everything else for the |P|=24 branch is rederived and recomputed below.

Search algorithms (both reviewer-designed):
  GB  -- group-branching, minimum-slack group selection, "smallest-remaining-element"
         branching: for the chosen group j, the solution's smallest remaining element e
         of group j is branched over in ascending order; elements of group j smaller than
         e are excluded in that branch.  Prunes: group with quota 0 is removed; a group
         with fewer available members than its remaining quota is infeasible.
  LAY -- layered: enumerate every exact pairwise-compatible fill of the two mod-11
         groups first (plain itertools.combinations), then fill the two mod-5 groups.
Both are complete (argument in size24-review-v1.md) and both are cross-checked against
brute-force enumeration on randomized sub-instances in this file.
"""
import hashlib
import json
import os
import platform
import random
import subprocess
import sys
import time
from itertools import combinations
from math import gcd

sys.setrecursionlimit(10000)

N = 1320
A = (0, 3, 8, 11)
Y = (0, 1, 7, 13, 14)
P_SIZE = 24
Q_SIZE = N // P_SIZE
assert P_SIZE * Q_SIZE == N

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_JSON = os.path.join(HERE, "size24-run-v1.json")

# Literal 22-residue control list quoted from the author's size24 program text; data only.
W_AUTHOR = [0, 14, 60, 110, 204, 230, 234, 300, 324, 444, 560, 564, 630, 680, 704, 800, 900, 924, 1034,
            1040, 1044, 1284]

REPORT = {}


def native_date():
    return subprocess.run(["/bin/date"], capture_output=True, text=True, check=True).stdout.strip()


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def gcd_classes(S):
    """gcd classes with N of all nonzero differences of a set of distinct residues."""
    return {gcd(a - b, N) for a, b in combinations(S, 2)}


# --------------------------------------------------------------------------- 1. arithmetic
def poly_mul(p, q):
    r = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i + j] += a * b
    return r


def section_arithmetic():
    out = {}
    GA = gcd_classes(A)
    GY = gcd_classes(Y)
    out["GA_classes_from_A_minus_A"] = sorted(GA)
    out["GY_classes_from_Y_minus_Y"] = sorted(GY)
    assert GA == {3, 5, 8, 11} and GY == {1, 2, 6, 12}
    assert not (GA & GY), "old anchors alone would already violate Sands"

    # prime balance at n = 2^3*3*5*11 with |P|=24, |Q|=55
    assert N == 2 ** 3 * 3 * 5 * 11
    bal = {}
    for p in (3, 5, 11):
        dp, dq = P_SIZE % p == 0, Q_SIZE % p == 0
        assert dp != dq, "primes 3,5,11 divide n once, so exactly one side is divisible"
        bal[str(p)] = "P uniform mod %d (%d per class)" % (p, P_SIZE // p) if dp else \
                      "Q uniform mod %d (%d per class)" % (p, Q_SIZE // p)
    out["prime_balance"] = bal
    # 2-part: |Q| odd => none of Phi_2, Phi_4, Phi_8 can divide the Q-mask (each would force
    # |Q| even: c_r = c_{r+4} mod 8 / c_r = c_{r+2} mod 4 / #even = #odd), hence all three divide
    # the P-mask, and Phi_2*Phi_4*Phi_8 = 1+x+...+x^7, so P is uniform mod 8.
    assert Q_SIZE % 2 == 1
    prod = poly_mul(poly_mul([1, 1], [1, 0, 1]), [1, 0, 0, 0, 1])
    assert prod == [1] * 8
    out["Phi2_Phi4_Phi8_product"] = prod
    out["P_uniform_mod_8_per_class"] = P_SIZE // 8
    assert P_SIZE % 8 == 0 and P_SIZE // 8 == 3

    # Head screen: necessary condition for x in P \ A from (S) against the known Q-classes GY.
    heads = [x for x in range(N) if all(x == a or gcd(x - a, N) not in GY for a in A)]
    out["head_screen_size"] = len(heads)
    mod8 = {r: sorted(x for x in heads if x % 8 == r) for r in range(8)}
    out["head_screen_mod8_counts"] = {str(r): len(mod8[r]) for r in range(8)}
    # A occupies mod-8 classes 0,3 only; classes 1,2,5,6 need exactly 3 new heads each.
    assert {a % 8 for a in A} == {0, 3}
    forced = []
    for r in (1, 2, 5, 6):
        assert len(mod8[r]) == 3, ("class %d has %d candidates" % (r, len(mod8[r])))
        forced += mod8[r]
    forced = sorted(forced)
    out["forced_heads"] = forced
    assert forced == [33, 198, 253, 418, 473, 638, 693, 858, 913, 1078, 1133, 1298]
    # closed form derived by hand: for x in classes 1,2,5,6 mod 8 no x-a is divisible by 4,
    # so the screen forces 5|x-a or 11|x-a for every a in A, which is only x = 33 mod 55.
    closed = sorted(x for x in range(N) if x % 55 == 33 and x % 8 in (1, 2, 5, 6))
    assert closed == forced
    out["forced_heads_closed_form"] = "x = 33 (mod 55) with x mod 8 in {1,2,5,6}"

    # all heads (A plus forced) must be pairwise compatible with GY, else the branch dies earlier
    full_heads = sorted(set(A) | set(forced))
    assert not (gcd_classes(full_heads) & GY)
    H = gcd_classes(forced)
    out["H_classes_forced_minus_forced"] = sorted(H)
    assert H == {55, 165, 220, 440, 660}
    extra = {gcd(f - a, N) for f in forced for a in A} - GA
    out["extra_classes_forced_minus_A_not_used_by_author"] = sorted(extra)
    assert extra == {10, 15, 22, 30, 33, 66}
    G = GA | H
    G_FULL = G | extra
    out["G_author_forbidden_for_Q"] = sorted(G)
    out["G_full_known_forbidden_for_Q"] = sorted(G_FULL)
    REPORT["arithmetic"] = out
    return G, G_FULL


# --------------------------------------------------------------------------- 2. instance
GROUP_PREDS = (lambda x: x % 5 == 0, lambda x: x % 5 == 4, lambda x: x % 11 == 0, lambda x: x % 11 == 3)
GROUP_NAMES = ("mod5=0", "mod5=4", "mod11=0", "mod11=3")
QUOTAS = (Q_SIZE // 5, Q_SIZE // 5, Q_SIZE // 11, Q_SIZE // 11)   # (11, 11, 5, 5)
ANCHORS = tuple(y for y in Y if any(pr(y) for pr in GROUP_PREDS))  # (0, 14)


def in_relaxed_classes(x):
    return any(pr(x) for pr in GROUP_PREDS)


def y_compatible(x, forb):
    return all(x == y or gcd(x - y, N) not in forb for y in Y)


class Instance:
    def __init__(self, cand, forb):
        self.cand = tuple(sorted(cand))
        self.forb = frozenset(forb)
        cs = set(self.cand)
        self.groups = tuple(frozenset(x for x in self.cand if pr(x)) for pr in GROUP_PREDS)
        self.conf = {x: frozenset(y for y in self.cand if y != x and gcd(x - y, N) in self.forb) for x in self.cand}
        self.member = {x: tuple(j for j, g in enumerate(self.groups) if x in g) for x in self.cand}
        assert all(x in cs for x in ANCHORS)


def build_instance(forb):
    cand = [x for x in range(N) if in_relaxed_classes(x) and y_compatible(x, forb)]
    return Instance(cand, forb)


def start_state(inst, quotas=QUOTAS, anchors=ANCHORS):
    av = set(inst.cand)
    need = list(quotas)
    for a in anchors:
        assert a in av
        av -= inst.conf[a]
        av.discard(a)
        for j in inst.member[a]:
            need[j] -= 1
    assert all(gcd(a - b, N) not in inst.forb for a, b in combinations(anchors, 2))
    return frozenset(av), tuple(need), list(anchors)


# --------------------------------------------------------------------------- 3. searches
def gb(inst, av, need, chosen, stats, active_groups=None):
    """Group-branching exact search.  Returns a full solution list or None."""
    stats["nodes"] += 1
    assert all(k >= 0 for k in need)
    groups = range(len(need)) if active_groups is None else active_groups
    av = set(av)
    for j in groups:
        if need[j] == 0:
            av -= inst.groups[j]
    for j in groups:
        if len(av & inst.groups[j]) < need[j]:
            stats["quota_prunes"] += 1
            return None
    if not any(need[j] for j in groups):
        return list(chosen)
    j = min((j for j in groups if need[j] > 0), key=lambda j: (len(av & inst.groups[j]) - need[j], j))
    excluded = set()
    for e in sorted(av & inst.groups[j]):
        new_av = (av - excluded - inst.conf[e])
        new_av.discard(e)
        new_need = list(need)
        for jj in inst.member[e]:
            new_need[jj] -= 1
        res = gb(inst, frozenset(new_av), tuple(new_need), chosen + [e], stats, active_groups)
        if res is not None:
            return res
        excluded.add(e)
    return None


def search_gb(inst, quotas=QUOTAS, anchors=ANCHORS):
    stats = {"nodes": 0, "quota_prunes": 0}
    av, need, chosen = start_state(inst, quotas, anchors)
    res = gb(inst, av, need, chosen, stats)
    return res, stats


def search_layered(inst, quotas=QUOTAS, anchors=ANCHORS):
    """Mod-11 groups first by plain combinations, then mod-5 groups by gb on groups (0,1)."""
    stats = {"mod11_sets_g2": 0, "mod11_sets_g3": 0, "mod11_pairs_compatible": 0,
             "nodes": 0, "quota_prunes": 0}
    av0, need0, chosen0 = start_state(inst, quotas, anchors)
    g2 = sorted(av0 & inst.groups[2])
    g3 = sorted(av0 & inst.groups[3])

    def compatible(S):
        return all(gcd(a - b, N) not in inst.forb for a, b in combinations(S, 2))

    fills2 = [s for s in combinations(g2, need0[2]) if compatible(s)]
    fills3 = [s for s in combinations(g3, need0[3]) if compatible(s)]
    stats["mod11_sets_g2"], stats["mod11_sets_g3"] = len(fills2), len(fills3)
    g23 = inst.groups[2] | inst.groups[3]
    for s2 in fills2:
        for s3 in fills3:
            if set(s2) & set(s3):
                continue   # an element in both mod-11 classes is impossible anyway (classes differ)
            T = s2 + s3
            if not all(gcd(a - b, N) not in inst.forb for a in s2 for b in s3):
                continue
            stats["mod11_pairs_compatible"] += 1
            av = set(av0) - g23
            for t in T:
                av -= inst.conf[t]
            need = list(need0)
            for t in T:
                for jj in inst.member[t]:
                    need[jj] -= 1
            need[2] = need[3] = 0
            if any(k < 0 for k in need):
                stats["quota_prunes"] += 1
                continue
            res = gb(inst, frozenset(av), tuple(need), chosen0 + list(T), stats, active_groups=(0, 1))
            if res is not None:
                return res, stats
    return None, stats


# --------------------------------------------------------------------------- 4. verifier
def verify(W, forb, quotas=QUOTAS, anchors=ANCHORS):
    """Independent of Instance: checks a claimed relaxed-Q witness against the actual constraints."""
    W = list(W)
    if len(set(W)) != len(W):
        return False, "duplicate residue"
    if not all(isinstance(x, int) and 0 <= x < N for x in W):
        return False, "residue out of range"
    if not set(anchors) <= set(W):
        return False, "anchor missing"
    bad = [x for x in W if not in_relaxed_classes(x)]
    if bad:
        return False, "outside relaxed classes: %s" % bad
    for x in W:
        for y in Y:
            if x != y and gcd(x - y, N) in forb:
                return False, "old-anchor conflict (%d,%d) gcd %d" % (x, y, gcd(x - y, N))
    for a, b in combinations(W, 2):
        if gcd(a - b, N) in forb:
            return False, "pair conflict (%d,%d) gcd %d" % (a, b, gcd(a - b, N))
    counts = [sum(1 for x in W if pr(x)) for pr in GROUP_PREDS]
    if counts != list(quotas):
        return False, "quota counts %s != %s" % (counts, list(quotas))
    return True, "ok"


# --------------------------------------------------------------------------- 5. brute-force completeness tests
def brute_force(inst, quotas, anchors):
    av, need, chosen = start_state(inst, quotas, anchors)
    av = sorted(av)
    for r in range(0, len(av) + 1):
        for S in combinations(av, r):
            full = chosen + list(S)
            if all(gcd(a - b, N) not in inst.forb for a, b in combinations(S, 2)):
                counts = [sum(1 for x in full if pr(x)) for pr in GROUP_PREDS]
                if counts == list(quotas):
                    return full
    return None


def completeness_tests(base_inst, trials, sub_size, seed):
    rng = random.Random(seed)
    others = [x for x in base_inst.cand if x not in ANCHORS]
    stats = {"trials": 0, "sat": 0, "unsat": 0, "planted": 0, "forb_variants": 0}
    for t in range(trials):
        sub = sorted(set(ANCHORS) | set(rng.sample(others, sub_size)))
        forb = set(base_inst.forb)
        if rng.random() < 0.3:          # vary the forbidden set too
            forb.discard(rng.choice(sorted(forb)))
            stats["forb_variants"] += 1
        inst = Instance(sub, forb)
        av0, need0, chosen0 = start_state(inst)
        if rng.random() < 0.5:          # plant a random compatible set and use its counts as quotas
            pool = list(av0)
            rng.shuffle(pool)
            planted = list(chosen0)
            for x in pool:
                if all(gcd(x - y, N) not in forb for y in planted):
                    planted.append(x)
                if len(planted) >= rng.randint(3, 7):
                    break
            quotas = tuple(sum(1 for x in planted if pr(x)) for pr in GROUP_PREDS)
            stats["planted"] += 1
        else:
            quotas = (rng.randint(1, 4), rng.randint(1, 4), rng.randint(1, 3), rng.randint(1, 3))
        bf = brute_force(inst, quotas, ANCHORS)
        r1, _ = search_gb(inst, quotas, ANCHORS)
        r2, _ = search_layered(inst, quotas, ANCHORS)
        exists = bf is not None
        if (r1 is not None) != exists or (r2 is not None) != exists:
            raise AssertionError("completeness/soundness mismatch on trial %d: bf=%s gb=%s lay=%s" % (t, bf, r1, r2))
        for r in (bf, r1, r2):
            if r is not None:
                ok, why = verify(r, forb, quotas, ANCHORS)
                assert ok, why
        stats["trials"] += 1
        stats["sat" if exists else "unsat"] += 1
    return stats


# --------------------------------------------------------------------------- main
def main():
    t_start = native_date()
    wall0 = time.time()
    G, G_FULL = section_arithmetic()

    inst = build_instance(G)
    inst_rep = {
        "candidates": len(inst.cand),
        "anchors": list(ANCHORS),
        "quotas": {GROUP_NAMES[j]: QUOTAS[j] for j in range(4)},
        "group_sizes": {GROUP_NAMES[j]: len(inst.groups[j]) for j in range(4)},
        "in_two_groups": sum(1 for x in inst.cand if len(inst.member[x]) == 2),
        "old_tails_1_7_13_outside_relaxed_classes": [y for y in Y if not in_relaxed_classes(y)],
    }
    assert len(inst.cand) == 144
    assert inst_rep["old_tails_1_7_13_outside_relaxed_classes"] == [1, 7, 13]
    REPORT["instance"] = inst_rep

    # ---- main exclusion under the author's nine classes
    res_gb, st_gb = search_gb(inst)
    res_lay, st_lay = search_layered(inst)
    REPORT["main_search_G"] = {"GB": {"result": "UNSAT" if res_gb is None else "SAT", **st_gb},
                               "LAY": {"result": "UNSAT" if res_lay is None else "SAT", **st_lay}}
    assert res_gb is None and res_lay is None, "unexpected relaxed witness under G"

    # ---- monotone sanity: strictly larger known forbidden set must also be UNSAT
    inst_full = build_instance(G_FULL)
    res_full, st_full = search_gb(inst_full)
    REPORT["search_G_full"] = {"candidates": len(inst_full.cand), "result": "UNSAT" if res_full is None else "SAT", **st_full}
    assert res_full is None

    # ---- positive control: remove only gcd class 220
    G220 = set(G) - {220}
    inst220 = build_instance(G220)
    w220, st220 = search_gb(inst220)
    assert w220 is not None, "control failed: expected SAT with gcd220 removed"
    ok, why = verify(w220, G220)
    assert ok, why
    ok_full, why_full = verify(w220, G)
    coll = sorted((a, b) for a, b in combinations(sorted(w220), 2) if gcd(a - b, N) == 220)
    REPORT["control_gcd220_removed"] = {
        "candidates": len(inst220.cand), "search": st220,
        "reviewer_witness": sorted(w220), "reviewer_witness_size": len(w220),
        "verified_under_G_minus_220": ok, "fails_under_G": (not ok_full), "failure_reason_under_G": why_full,
        "gcd220_collisions_in_reviewer_witness": coll,
    }
    assert not ok_full and coll

    # author's literal control list, treated as a claim and checked by the reviewer's verifier
    okA, whyA = verify(W_AUTHOR, G220)
    okA_G, whyA_G = verify(W_AUTHOR, G)
    collA = sorted((a, b) for a, b in combinations(sorted(W_AUTHOR), 2) if gcd(a - b, N) == 220)
    REPORT["author_control_list_check"] = {"size": len(W_AUTHOR), "verified_under_G_minus_220": okA, "reason": whyA,
                                           "fails_under_G": not okA_G, "reason_under_G": whyA_G,
                                           "gcd220_collisions": collA}
    assert okA and not okA_G and collA

    # ---- per-class sensitivity: drop one forbidden class at a time
    sens = {}
    for c in sorted(G):
        Gc = set(G) - {c}
        ic = build_instance(Gc)
        w, st = search_gb(ic)
        entry = {"candidates": len(ic.cand), "result": "UNSAT" if w is None else "SAT", **st}
        if w is not None:
            ok, why = verify(w, Gc)
            assert ok, why
            entry["witness"] = sorted(w)
        sens[str(c)] = entry
    REPORT["sensitivity_drop_one_class"] = sens
    # dropping all of H
    iGA = build_instance(set(G) - {55, 165, 220, 440, 660})
    wGA, stGA = search_gb(iGA)
    REPORT["search_GA_only"] = {"candidates": len(iGA.cand), "result": "UNSAT" if wGA is None else "SAT", **stGA}
    if wGA is not None:
        ok, why = verify(wGA, iGA.forb)
        assert ok, why
        REPORT["search_GA_only"]["witness"] = sorted(wGA)

    # ---- rejection mutations: the verifier must reject each corrupted claim
    muts = {}
    def expect_reject(name, W, forb, quotas=QUOTAS):
        ok, why = verify(W, forb, quotas)
        assert not ok, "mutation %s was NOT rejected" % name
        muts[name] = why
    base = list(W_AUTHOR)
    expect_reject("author_list_under_full_G", base, G)
    expect_reject("drop_anchor_14", [x for x in base if x != 14], G220)
    expect_reject("replace_60_by_61_outside_classes", [61 if x == 60 else x for x in base], G220)
    expect_reject("replace_60_by_55_conflicting_with_0", [55 if x == 60 else x for x in base], G220)
    expect_reject("duplicate_entry", base + [60], G220)
    expect_reject("quota_broken_drop_60", [x for x in base if x != 60], G220)
    expect_reject("reviewer_witness_under_full_G", sorted(w220), G)
    expect_reject("wrong_quota_vector", base, G220, (11, 11, 4, 4))
    REPORT["rejection_mutations"] = muts

    # ---- randomized brute-force completeness/soundness tests of both searches
    REPORT["completeness_tests"] = completeness_tests(inst, trials=400, sub_size=12, seed=20261028)
    assert REPORT["completeness_tests"]["sat"] > 50 and REPORT["completeness_tests"]["unsat"] > 50

    t_end = native_date()
    REPORT["receipt"] = {
        "checker_path": os.path.abspath(__file__),
        "checker_sha256": sha256_file(__file__),
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "native_date_before": t_start,
        "native_date_after": t_end,
        "wall_seconds": round(time.time() - wall0, 2),
        "verdict_scope": "relaxed four-quota Q instance of the |P|=24 branch at n=1320 only; conditional on premises (T),(S)",
        "result": "UNSAT under G; SAT control with gcd220 removed",
    }
    with open(OUT_JSON, "w") as f:
        json.dump(REPORT, f, indent=1, sort_keys=True)
        f.write("\n")
    print(json.dumps(REPORT, indent=1, sort_keys=True))


if __name__ == "__main__":
    main()
