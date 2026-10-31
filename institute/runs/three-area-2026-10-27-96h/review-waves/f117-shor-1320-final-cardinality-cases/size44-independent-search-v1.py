#!/usr/bin/env python3
"""size44-independent-search-v1.py -- f117 same-harness reviewer artifact (size-44 branch).

Written from scratch by the reviewer for review wave
f117-shor-1320-final-cardinality-cases.  It imports or executes NO author code.  All
quantities are exact Python integers; every search is finite and exhaustive unless a
section is explicitly labelled "first witness only".

Conditional premises (taken as given for this branch; NOT adopted or re-reviewed here,
they belong to f114 and its predecessors):
  (T) Z_1320 = P (+) Q is a direct tiling with A={0,3,8,11} subset P and
      Y={0,1,7,13,14} subset Q (actual border tiling/anchors).
  (S) Sands divisor-class disjointness: for p!=p' in P and q!=q' in Q,
      gcd(p-p',1320) != gcd(q-q',1320).
  (U) Cyclotomic uniformity: for each prime r in {3,5,11} (each divides 1320 exactly
      once) the factor whose cardinality r divides is equidistributed mod r.
Branch premise: |P| = 44, hence |Q| = 30.

Reviewer derivation that this program certifies finitely (see size44-review-v1.md):
  H1  P is uniform mod 11 (four per class);  classes 1 and 2 mod 11 contain no anchor,
      so P picks 4 of the GY-screened head candidates in each of those classes.
  H2  Every such admissible choice contains a pair with gcd class 55  =>  P uses 55,
      so by (S) Q must avoid 55.
  Q1  Q is uniform mod 3 (10 per class) and mod 5 (6 per class).
  Q2  Under forbidden classes G = GA u {55} no Y-screened candidate in mod-5 classes
      0 or 4 is 1 mod 3; hence the 12 Q-elements there are all in mod-3 classes 0,2,
      and the remaining 8 non-class-1 elements of Q lie in mod-5 classes 1,2,3 and are
      an 8-subset of the screened list X (|X| = 12  =>  C(12,8) = 495 seeds).
  Q3  Relaxed instance R(G): seed S (8 of X) + 6-set in class 0 mod 5 containing 0 +
      6-set in class 4 mod 5 containing 14, all pairwise G-free, with exactly 10
      elements = 0 mod 3 and 10 elements = 2 mod 3.  Any actual Q yields a solution of
      R(G) (take its non-class-1 part), so UNSAT of R(G) excludes the branch.
"""
import json
import sys
import time
from itertools import combinations
from math import comb, gcd

N = 1320
A = (0, 3, 8, 11)
Y = (0, 1, 7, 13, 14)


def gc(d):
    """gcd class of a difference of two residues (nonzero for distinct residues)."""
    return gcd(d % N, N)


def diff_classes(S):
    return {gc(a - b) for a, b in combinations(S, 2)}


def screen(anchors, forb):
    """residues whose difference from every anchor avoids the forbidden gcd classes."""
    return [x for x in range(N) if all(x == t or gc(x - t) not in forb for t in anchors)]


def pairwise_free(S, forb):
    return all(gc(a - b) not in forb for a, b in combinations(S, 2))


def cross_free(S, T, forb):
    return all(gc(a - b) not in forb for a in S for b in T)


def mask_of(idx_iter):
    m = 0
    for i in idx_iter:
        m |= 1 << i
    return m


# ----------------------------------------------------------------------------
# Head side: H1/H2 (forced gcd class 55 in P)
# ----------------------------------------------------------------------------
def head_side(GA, GY):
    PC = screen(A, GY)
    assert set(A) <= set(PC)
    by11 = {r: [x for x in PC if x % 11 == r] for r in range(11)}
    C1, C2 = by11[1], by11[2]
    edges55 = {
        "C1": [(a, b) for a, b in combinations(C1, 2) if gc(a - b) == 55],
        "C2": [(a, b) for a, b in combinations(C2, 2) if gc(a - b) == 55],
    }
    free1 = [s for s in combinations(C1, 4) if pairwise_free(s, {55})]
    free2 = [s for s in combinations(C2, 4) if pairwise_free(s, {55})]
    forced1 = sorted(set(C1).intersection(*map(set, free1))) if free1 else []
    forced2 = sorted(set(C2).intersection(*map(set, free2))) if free2 else []
    # Exhaustive statement actually needed: among ALL (4 of C1, 4 of C2) choices that are
    # GY-free internally and across (required by (S) with Y subset Q), none is 55-free.
    admissible = 0
    admissible_55free = []
    for s1 in combinations(C1, 4):
        if not pairwise_free(s1, GY):
            continue
        for s2 in combinations(C2, 4):
            if not pairwise_free(s2, GY) or not cross_free(s1, s2, GY):
                continue
            admissible += 1
            if pairwise_free(s1 + s2, {55}):
                admissible_55free.append(s1 + s2)
    forced_cross = [(a, b, gc(a - b)) for a in forced1 for b in forced2]
    return {
        "GA": sorted(GA),
        "GY": sorted(GY),
        "head_screen_size": len(PC),
        "head_screen_mod11_class_sizes": {r: len(by11[r]) for r in range(11)},
        "C1_mod11_class1": C1,
        "C2_mod11_class2": C2,
        "gcd55_edges": edges55,
        "fiftyfive_free_4subsets_C1": free1,
        "fiftyfive_free_4subsets_C2": free2,
        "forced_in_C1_if_P_avoids_55": forced1,
        "forced_in_C2_if_P_avoids_55": forced2,
        "forced_cross_differences_(a,b,gcd)": forced_cross,
        "forced_cross_gcd_in_GY": [t for t in forced_cross if t[2] in GY],
        "admissible_GYfree_choice_pairs": admissible,
        "admissible_choice_pairs_that_avoid_55": admissible_55free,
    }


# ----------------------------------------------------------------------------
# Tail side instance construction: Q1/Q2
# ----------------------------------------------------------------------------
def tail_instance(forb):
    C = screen(Y, forb)
    assert set(Y) <= set(C)
    class1_in_04 = [x for x in C if x % 5 in (0, 4) and x % 3 == 1]
    X = [x for x in C if x % 5 in (1, 2, 3) and x % 3 != 1]
    B0_all = [x for x in C if x % 5 == 0]
    B4_all = [x for x in C if x % 5 == 4]
    B0 = [x for x in B0_all if x % 3 != 1]
    B4 = [x for x in B4_all if x % 3 != 1]
    assert 0 in B0 and 14 in B4
    info = {
        "forbidden": sorted(forb),
        "screen_size": len(C),
        "class1_mod3_candidates_in_mod5_classes_0_4": class1_in_04,
        "X_nonclass1_in_mod5_classes_123": X,
        "X_size": len(X),
        "X_mod5": [x % 5 for x in X],
        "X_mod3": [x % 3 for x in X],
        "B0_size_unfiltered": len(B0_all),
        "B4_size_unfiltered": len(B4_all),
        "B0_size_nonclass1": len(B0),
        "B4_size_nonclass1": len(B4),
        "screen_mod5_x_mod3_counts": {
            f"mod5={r5},mod3={r3}": sum(1 for x in C if x % 5 == r5 and x % 3 == r3)
            for r5 in range(5) for r3 in range(3)
        },
    }
    return C, X, B0, B4, info


# ----------------------------------------------------------------------------
# Q3: seed enumeration (structure 1): all C(|X|,8) seeds, then all anchored 6-cliques
# per mod-5 class, then balance + cross test on every (left,right) pair.
# ----------------------------------------------------------------------------
def seed_search(forb, X, B0, B4, seed_size=8, quota=6, zeros_target=10, twos_target=10,
                check_seed=True, check_balance=True, check_cross=True, stop_first=False,
                limit_seeds=None):
    n0, n4 = len(B0), len(B4)
    i0, i4 = B0.index(0), B4.index(14)
    conf0 = [mask_of(j for j, y in enumerate(B0) if j != i and gc(x - y) in forb) for i, x in enumerate(B0)]
    conf4 = [mask_of(j for j, y in enumerate(B4) if j != i and gc(x - y) in forb) for i, x in enumerate(B4)]
    x04 = [mask_of(j for j, y in enumerate(B4) if gc(x - y) in forb) for x in B0]
    sx0 = [mask_of(j for j, y in enumerate(B0) if gc(s - y) in forb) for s in X]
    sx4 = [mask_of(j for j, y in enumerate(B4) if gc(s - y) in forb) for s in X]
    z0 = [int(x % 3 == 0) for x in B0]
    t0 = [int(x % 3 == 2) for x in B0]
    z4 = [int(x % 3 == 0) for x in B4]
    t4 = [int(x % 3 == 2) for x in B4]
    full0, full4 = (1 << n0) - 1, (1 << n4) - 1

    def cliques(conf, avail, anchor, size):
        out = []

        def rec(chosen, cand):
            need = size - len(chosen)
            if need == 0:
                out.append(tuple(chosen))
                return
            if cand.bit_count() < need:
                return
            c = cand
            while c:
                b = c & -c
                i = b.bit_length() - 1
                c ^= b
                rec(chosen + [i], c & ~conf[i])  # c now holds only indices > i

        rec([anchor], avail & ~conf[anchor] & ~(1 << anchor))
        return out

    st = {"seeds": 0, "seed_conflicts": 0, "compatible_seeds": 0, "left_sets_total": 0,
          "right_sets_total": 0, "pairs": 0, "balanced_pairs": 0, "cross_ok_pairs": 0,
          "balanced_and_cross_ok": 0, "accepted": 0}
    hist = {}
    witness = None
    for S in combinations(range(len(X)), seed_size):
        st["seeds"] += 1
        if limit_seeds and st["seeds"] > limit_seeds:
            break
        Sv = [X[i] for i in S]
        if check_seed and not pairwise_free(Sv, forb):
            st["seed_conflicts"] += 1
            continue
        st["compatible_seeds"] += 1
        av0, av4 = full0, full4
        for i in S:
            av0 &= ~sx0[i]
            av4 &= ~sx4[i]
        assert (av0 >> i0) & 1 and (av4 >> i4) & 1
        L = cliques(conf0, av0, i0, quota)
        R = cliques(conf4, av4, i4, quota)
        st["left_sets_total"] += len(L)
        st["right_sets_total"] += len(R)
        key = f"{len(L)},{len(R)}"
        hist[key] = hist.get(key, 0) + 1
        zS = sum(int(s % 3 == 0) for s in Sv)
        tS = sum(int(s % 3 == 2) for s in Sv)
        Rinfo = [(sum(z4[j] for j in r), sum(t4[j] for j in r), mask_of(r), r) for r in R]
        for l in L:
            zL = sum(z0[i] for i in l)
            tL = sum(t0[i] for i in l)
            cm = 0
            for i in l:
                cm |= x04[i]
            for zR, tR, rm, r in Rinfo:
                st["pairs"] += 1
                bal = (zS + zL + zR == zeros_target) and (tS + tL + tR == twos_target)
                cross = (cm & rm) == 0
                if bal:
                    st["balanced_pairs"] += 1
                if cross:
                    st["cross_ok_pairs"] += 1
                if bal and cross:
                    st["balanced_and_cross_ok"] += 1
                if (bal or not check_balance) and (cross or not check_cross):
                    st["accepted"] += 1
                    if witness is None:
                        witness = {"seed": Sv, "class0": [B0[i] for i in l], "class4": [B4[j] for j in r]}
                    if stop_first:
                        return st, hist, witness
    return st, hist, witness


# ----------------------------------------------------------------------------
# Q3: quota DFS (structure 2): one ordered include-enumeration over the merged
# universe with group quotas, anchors preselected, and mod-3 count pruning.
# ----------------------------------------------------------------------------
class _Stop(Exception):
    pass


def quota_dfs(forb, X, B0, B4, seed_size=8, quota=6, zeros_target=10, twos_target=10,
              stop_first=False, node_budget=None):
    U = [(x, 0) for x in X] + [(x, 1) for x in B0] + [(x, 2) for x in B4]
    n = len(U)
    conf = [mask_of(j for j, (y, _) in enumerate(U) if j != i and gc(x - y) in forb) for i, (x, _) in enumerate(U)]
    grp = [mask_of(i for i, (_, g) in enumerate(U) if g == k) for k in range(3)]
    zmask = mask_of(i for i, (x, _) in enumerate(U) if x % 3 == 0)
    tmask = mask_of(i for i, (x, _) in enumerate(U) if x % 3 == 2)
    need = [seed_size, quota, quota]
    avail = (1 << n) - 1
    chosen = []
    for a, k in ((0, 1), (14, 2)):
        i = U.index((a, k))
        chosen.append(i)
        avail &= ~conf[i] & ~(1 << i)
        need[k] -= 1
    z = sum(1 for i in chosen if (zmask >> i) & 1)
    t = sum(1 for i in chosen if (tmask >> i) & 1)
    state = {"nodes": 0, "solutions": 0, "first": None, "budget_exceeded": False}

    def rec(avail, need, z, t, chosen):
        state["nodes"] += 1
        if node_budget is not None and state["nodes"] > node_budget:
            state["budget_exceeded"] = True
            raise _Stop
        if z > zeros_target or t > twos_target:
            return
        for k in range(3):
            if (avail & grp[k]).bit_count() < need[k]:
                return
        if (avail & zmask).bit_count() + z < zeros_target or (avail & tmask).bit_count() + t < twos_target:
            return
        if need[0] == need[1] == need[2] == 0:
            if z == zeros_target and t == twos_target:
                state["solutions"] += 1
                if state["first"] is None:
                    state["first"] = sorted(U[i][0] for i in chosen)
                if stop_first:
                    raise _Stop
            return
        k = min((k for k in range(3) if need[k] > 0), key=lambda k: (avail & grp[k]).bit_count() - need[k])
        c = avail & grp[k]
        while c:
            b = c & -c
            i = b.bit_length() - 1
            c ^= b
            nn = list(need)
            nn[k] -= 1
            new_avail = ((avail & ~grp[k]) | c) & ~conf[i]
            rec(new_avail, nn, z + ((zmask >> i) & 1), t + ((tmask >> i) & 1), chosen + [i])

    try:
        rec(avail, need, z, t, chosen)
    except _Stop:
        pass
    return state


def check_T(T, forb, note):
    """Direct checker for a claimed 20-residue relaxed witness."""
    T = list(T)
    ok_distinct = len(T) == len(set(T)) == 20
    ok_anchor = 0 in T and 14 in T
    ok_screen = all(x in set(screen(Y, forb)) for x in T)
    ok_pairs = pairwise_free(T, forb)
    counts = [sum(x % m == r for x in T) for m, r in ((5, 0), (5, 4), (3, 0), (3, 2), (3, 1))]
    ok_quota = counts == [6, 6, 10, 10, 0]
    return {"note": note, "distinct20": ok_distinct, "anchors": ok_anchor, "Y_screen": ok_screen,
            "pairwise_free": ok_pairs, "counts_[5=0,5=4,3=0,3=2,3=1]": counts, "quotas": ok_quota,
            "all_ok": ok_distinct and ok_anchor and ok_screen and ok_pairs and ok_quota,
            "has_gcd55_pair_or_vs_Y": any(gc(a - b) == 55 for a, b in combinations(sorted(set(T) | set(Y)), 2))}


def main():
    t_start = time.time()
    out = {"program": "size44-independent-search-v1.py", "python": sys.version.split()[0],
           "utc_start": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(t_start))}

    GA, GY = diff_classes(A), diff_classes(Y)
    assert GA == {3, 5, 8, 11} and GY == {1, 2, 6, 12}
    out["head_side"] = head_side(GA, GY)
    hs = out["head_side"]
    assert hs["admissible_choice_pairs_that_avoid_55"] == [], "P could avoid 55: argument fails"

    G = GA | {55}
    C, X, B0, B4, info = tail_instance(G)
    out["tail_instance_G"] = info
    assert info["class1_mod3_candidates_in_mod5_classes_0_4"] == [], "Q2 fails"
    assert len(X) == 12, len(X)
    assert comb(len(X), 8) == 495

    # --- main exhaustive run (structure 1) ---
    t0 = time.time()
    st, hist, wit = seed_search(G, X, B0, B4)
    out["main_seed_search"] = {"stats": st, "hist_(|left|,|right|)->seeds": hist, "witness": wit,
                               "seconds": round(time.time() - t0, 3)}
    assert st["seeds"] == 495 and st["accepted"] == 0 and wit is None

    # --- main exhaustive run (structure 2) ---
    t0 = time.time()
    q = quota_dfs(G, X, B0, B4, stop_first=False)
    out["main_quota_dfs"] = dict(q, seconds=round(time.time() - t0, 3))
    assert q["solutions"] == 0 and not q["budget_exceeded"]

    # --- mutation controls on the real instance (each must change the outcome) ---
    muts = {}
    t0 = time.time()
    s_nocross, _, w_nocross = seed_search(G, X, B0, B4, check_cross=False)
    muts["skip_cross_check"] = {"accepted": s_nocross["accepted"], "balanced_pairs": s_nocross["balanced_pairs"],
                               "first_accepted": w_nocross, "seconds": round(time.time() - t0, 3)}
    t0 = time.time()
    s_nobal, _, w_nobal = seed_search(G, X, B0, B4, check_balance=False)
    muts["skip_balance_check"] = {"accepted": s_nobal["accepted"], "cross_ok_pairs": s_nobal["cross_ok_pairs"],
                                 "first_accepted": w_nobal, "seconds": round(time.time() - t0, 3)}
    t0 = time.time()
    s_noseed, _, w_noseed = seed_search(G, X, B0, B4, check_seed=False)
    muts["skip_seed_conflict_check"] = {"compatible_seeds": s_noseed["compatible_seeds"], "accepted": s_noseed["accepted"],
                                       "balanced_pairs": s_noseed["balanced_pairs"], "first_accepted": w_noseed,
                                       "seconds": round(time.time() - t0, 3)}
    if w_noseed is not None:
        T = w_noseed["seed"] + w_noseed["class0"] + w_noseed["class4"]
        muts["skip_seed_conflict_check"]["first_accepted_seed_internal_conflicts"] = [
            (a, b, gc(a - b)) for a, b in combinations(w_noseed["seed"], 2) if gc(a - b) in G]
    # anchor mutation: drop 14 from the forbidden-screen anchors (Y without 14) -- instance must change
    Ym = tuple(y for y in Y if y != 14)
    Cm = [x for x in range(N) if all(x == t or gc(x - t) not in G for t in Ym)]
    muts["anchor_mutation_drop_14_from_Y"] = {"screen_size": len(Cm), "X_size": len([x for x in Cm if x % 5 in (1, 2, 3) and x % 3 != 1]),
                                             "class1_in_04": len([x for x in Cm if x % 5 in (0, 4) and x % 3 == 1])}
    out["mutation_controls"] = muts

    # --- gcd55 relaxation positive controls ---
    pos = {}
    C2_, X2, B0_2, B4_2, info2 = tail_instance(GA)
    pos["instance_GA_only"] = info2
    # (a) same 12-extras seed search machinery, 55 dropped, bases re-screened under GA
    #     (bases restricted to non-class-1 so the 20-element shape is unchanged)
    t0 = time.time()
    Xsame = [x for x in X if x in set(X2)]
    sa, ha, wa = seed_search(GA, Xsame, B0_2, B4_2, stop_first=True)
    pos["seed_search_GA_same_12_extras_first_witness_only"] = {"X_used": Xsame, "stats": sa, "witness": wa,
                                                               "seconds": round(time.time() - t0, 3)}
    if wa is not None:
        pos["seed_search_GA_same_12_extras_first_witness_only"]["witness_check"] = check_T(
            wa["seed"] + wa["class0"] + wa["class4"], GA, "reviewer witness, GA only")
    # (b) full GA-relaxed instance via quota DFS, first witness only
    t0 = time.time()
    qa = quota_dfs(GA, X2, B0_2, B4_2, stop_first=True, node_budget=5_000_000)
    pos["quota_dfs_GA_full_instance_first_witness_only"] = dict(qa, seconds=round(time.time() - t0, 3))
    if qa["first"] is not None:
        pos["quota_dfs_GA_full_instance_first_witness_only"]["witness_check"] = check_T(qa["first"], GA, "reviewer witness, GA only")
    # (c) author-claimed 20-residue relaxation witness, checked by reviewer code only
    W_author = [0, 14, 54, 68, 120, 240, 288, 360, 386, 600, 614, 674, 716, 722, 840, 936, 1004, 1052, 1058, 1224]
    pos["author_claimed_witness_checked_by_reviewer_code"] = check_T(W_author, GA, "author list from p44-seed-check.py, GA only")
    pos["author_claimed_witness_fails_under_G_with_55"] = check_T(W_author, G, "same list under G = GA u {55}")
    out["positive_controls"] = pos

    out["seconds_total"] = round(time.time() - t_start, 3)
    out["utc_end"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    out["verdict_of_this_program"] = ("R(G) UNSAT by two structures; every enabled check is load-bearing per mutation runs; "
                                      "gcd55 relaxation SAT => the 55-ban is the operative constraint. "
                                      "Scope: relaxed necessary conditions at n=1320, |P|=44 only, conditional on (T),(S),(U).")
    text = json.dumps(out, indent=1, default=list) + "\n"
    if len(sys.argv) > 1:
        with open(sys.argv[1], "x") as fh:  # exclusive create: never overwrite
            fh.write(text)
    summary = {k: out[k] for k in ("utc_start", "utc_end", "seconds_total")}
    summary["main_seed_search_stats"] = out["main_seed_search"]["stats"]
    summary["main_quota_dfs"] = {k: out["main_quota_dfs"][k] for k in ("nodes", "solutions", "budget_exceeded")}
    summary["head_admissible_pairs"] = out["head_side"]["admissible_GYfree_choice_pairs"]
    summary["head_pairs_avoiding_55"] = len(out["head_side"]["admissible_choice_pairs_that_avoid_55"])
    summary["mutations"] = {k: {kk: vv for kk, vv in v.items() if kk != "first_accepted"} for k, v in out["mutation_controls"].items()}
    summary["positive_controls"] = {
        "GA_same12_witness_found": out["positive_controls"]["seed_search_GA_same_12_extras_first_witness_only"]["witness"] is not None,
        "GA_full_dfs_witness_found": out["positive_controls"]["quota_dfs_GA_full_instance_first_witness_only"]["first"] is not None,
        "author_W_ok_under_GA": out["positive_controls"]["author_claimed_witness_checked_by_reviewer_code"]["all_ok"],
        "author_W_ok_under_G55": out["positive_controls"]["author_claimed_witness_fails_under_G_with_55"]["all_ok"],
    }
    print(json.dumps(summary, indent=1, default=list))


if __name__ == "__main__":
    main()
