#!/usr/bin/env python3
"""ReviewF174ShorQ55 independent exact control, version 1.

Wave: f174-shor-55-tail-infinite-branch
Manifest SHA-256: 6694b67a997163c5999eed791c577679d06403d62990334be19a4ca53c93f5da

Independently authored by reviewer ReviewF174ShorQ55.  Uses only the Python
standard library and exact integer arithmetic.  It does not read, import or
execute any author script or any other run artifact.

Usage: python3 ReviewF174ShorQ55-exact-control-v1.py RESULT_JSON_PATH
Exit status 0 iff every positive check passes AND every pre-registered
negative/countercontrol prediction (written below before the first run) matches.
"""
import itertools
import json
import platform
import sys
from math import gcd

A = (0, 3, 8, 11)              # old head anchors (P side)
Y = (0, 1, 7, 13, 14)          # old tail anchors (Q side)
TAIL = (1, 2, 6, 12)           # claimed tail difference classes for every k >= 2
RECT = (33, 88, 143)           # claimed forced odd-part residues modulo 165
H = (3, 5, 11, 15, 30, 55)     # claimed P-difference classes with v2 <= 1
SCREEN = [7, 73, 337, 601]     # claimed class-7-mod-11 projected tail candidates

CHECKS = []
INFO = {}


def check(name, cond, detail=None):
    CHECKS.append({"name": name, "pass": bool(cond), "detail": detail})


def crt2(r1, m1, r2, m2):
    """Unique x mod m1*m2 with x = r1 (m1), x = r2 (m2); gcd(m1, m2) = 1."""
    t = ((r2 - r1) * pow(m1, -1, m2)) % m2
    return (r1 + m1 * t) % (m1 * m2)


def classes(S, n):
    return sorted({gcd((s - t) % n, n) for s in S for t in S if (s - t) % n})


def admissible(x, n, anchors, forbidden):
    """x avoids every forbidden gcd class against every anchor distinct from x."""
    return all(gcd((x - a) % n, n) not in forbidden
               for a in anchors if (x - a) % n)


def v2(x):
    return (x & -x).bit_length() - 1


# ---------------------------------------------------------------- T: anchor classes
for k in range(2, 13):
    n = 165 << k
    tail = classes(Y, n)
    head = classes(A, n)
    check(f"T.tail_classes.k{k}", tail == list(TAIL), tail)
    check(f"T.head_classes.k{k}", head == sorted([3, 5, 11, 4 if k == 2 else 8]), head)


# ------------------------------------------- R: forced rectangle, k-independent form
# Lemma R0: for x = 1,2 (mod 4) and every anchor a, x-a is not 0 mod 4, so
# v2(x-a) <= 1 and gcd(x-a, n) = gcd(x-a, 660) for every k >= 2.
check("R0.v2_le_1_mod4", all((r - a) % 4 != 0 for r in (1, 2) for a in A))
for k in range(2, 9):
    n = 165 << k
    ok = all(gcd((x - a) % n, n) == gcd((x - a) % 660, 660)
             for x in range(n) if x % 4 in (1, 2) for a in A)
    check(f"R0.gcd_transfer_numeric.k{k}", ok)


def rect_profile(anchors, forbidden):
    """Over Z_660 (valid for every k by Lemma R0): admissible odd-part residues per r mod 4."""
    prof = {}
    for r in (1, 2):
        adm = sorted(x % 165 for x in range(660)
                     if x % 4 == r and admissible(x, 660, anchors, forbidden))
        prof[r] = adm
    return prof


full = rect_profile(A, set(TAIL))
check("R1.rect_r1_mod4_over_Z660", full[1] == list(RECT), full[1])
check("R1.rect_r2_mod4_over_Z660", full[2] == list(RECT), full[2])

# The two-step mechanism of the written proof.
def pairs(anchors, r):
    return sorted({(x % 5, x % 11) for x in range(660)
                   if x % 4 == r and admissible(x, 660, anchors, set(TAIL))})

check("R2.r1_valuation1_pair_3_11", pairs((3, 11), 1) == [(1, 3), (3, 0)], pairs((3, 11), 1))
check("R2.r2_valuation1_pair_0_8", pairs((0, 8), 2) == [(0, 8), (3, 0)], pairs((0, 8), 2))
u_r1_0 = sorted({x % 3 for x in range(660) if x % 4 == 1 and (x % 5, x % 11) == (1, 3)
                 and admissible(x, 660, (0,), set(TAIL))})
u_r1_8 = sorted({x % 3 for x in range(660) if x % 4 == 1 and (x % 5, x % 11) == (1, 3)
                 and admissible(x, 660, (8,), set(TAIL))})
u_r2_3 = sorted({x % 3 for x in range(660) if x % 4 == 2 and (x % 5, x % 11) == (0, 8)
                 and admissible(x, 660, (3,), set(TAIL))})
u_r2_11 = sorted({x % 3 for x in range(660) if x % 4 == 2 and (x % 5, x % 11) == (0, 8)
                  and admissible(x, 660, (11,), set(TAIL))})
check("R2.r1_branch13_anchor0_forces_u0", u_r1_0 == [0], u_r1_0)
check("R2.r1_branch13_anchor8_forces_u2", u_r1_8 == [2], u_r1_8)
check("R2.r2_branch08_anchor3_forces_u0", u_r2_3 == [0], u_r2_3)
check("R2.r2_branch08_anchor11_forces_u2", u_r2_11 == [2], u_r2_11)

# Direct brute force in Z_n (no reduction) for small k, every residue class r mod m.
for k in range(2, 9):
    n, m = 165 << k, 1 << k
    tail = set(classes(Y, n))
    ok, other = True, []
    for r in range(m):
        adm = [x for x in range(r, n, m) if admissible(x, n, A, tail)]
        if r % 4 in (1, 2):
            want = sorted(crt2(r, m, s, 165) for s in RECT)
            ok = ok and sorted(adm) == want
        else:
            other.append(len(adm))
    check(f"R3.direct_Zn_every_r_class.k{k}", ok)
    INFO[f"R3.unforced_r_mod4_0_3_admissible_count_range.k{k}"] = [min(other), max(other)]


# ------------------------------------------------- G: gcd witnesses 15/30/55, 165*2^a
def in_rect(x, m):
    return (x % m) % 4 in (1, 2) and x % 165 in RECT

for k in range(2, 17):
    n, m = 165 << k, 1 << k
    x15 = crt2(1, m, 143, 165)
    x30 = crt2(1, m, 33, 165)
    y55 = crt2(2, m, 88, 165)
    g = [gcd((x15 - 8) % n, n), gcd((x30 - 3) % n, n), gcd((x30 - y55) % n, n)]
    wit = [in_rect(x15, m), in_rect(x30, m), in_rect(y55, m)]
    ga = []
    for a in range(2, k):
        xa = crt2((1 + (1 << a)) % m, m, 33, 165)
        wit.append(in_rect(xa, m))
        ga.append(gcd((xa - x30) % n, n) == 165 << a)
    check(f"G.witness_15_30_55.k{k}", g == [15, 30, 55] and all(wit) and all(ga), g)

check("G.H_v2_le_1", all(v2(h) <= 1 for h in H))


# ------------------------------------------------------------- J: injectivity classes
for k in range(2, 17):
    n = 165 << k
    got = sorted({gcd(660 * j, n) for j in range(1, 1 << (k - 2))})
    want = [165 << a for a in range(2, k)]
    check(f"J.mod660_collision_classes.k{k}", got == want, got[:4])


# -------------------------------------------------------- M: mod-660 transfer for H
for k in range(2, 9):
    n = 165 << k
    ok = True
    for d in range(n):
        g6, gn = gcd(d, 660), gcd(d, n)
        if (g6 in H or gn in H) and g6 != gn:
            ok = False
            break
    check(f"M.H_class_transfer_exhaustive.k{k}", ok)


# ------------------------------------------------------ S: four-candidate tail screen
def screen(cls, anchors, forb, n=660):
    return [z for z in range(n) if z % 11 == cls and admissible(z, n, anchors, forb)]

s7 = screen(7, Y, set(H))
check("S1.class7_screen_Z660", s7 == SCREEN, s7)
by_t = {t: [z for z in s7 if z % 4 == t] for t in range(4)}
check("S1.hand_derivation_by_z_mod4", by_t == {0: [], 1: [73, 337, 601], 2: [], 3: [7]}, by_t)
INFO["S1.all_mod11_class_counts_Z660_H"] = [len(screen(c, Y, set(H))) for c in range(11)]
check("S1.anchors_mod11", sorted(y % 11 for y in Y) == [0, 1, 2, 3, 7])

for k in range(2, 9):
    n = 165 << k
    cand = screen(7, Y, set(H), n)
    proj = sorted({q % 660 for q in cand})
    J = {165 << a for a in range(2, k)}
    same = all(gcd((p - q) % n, n) in J for p, q in itertools.combinations(cand, 2)
               if (p - q) % 660 == 0)
    check(f"S2.Zn_projection_and_collisions.k{k}",
          proj == SCREEN and len(cand) == (1 << k) and same, [len(cand), proj])


# ------------------------------------- N: negative / intended-reason countercontrols
# Predictions below were derived by hand (reviewer notes) before the first run.
PRED_N1 = {0: (4, 14), 3: (8, 4), 8: (4, 8), 11: (14, 4)}      # drop one head anchor
for a, want in PRED_N1.items():
    prof = rect_profile(tuple(x for x in A if x != a), set(TAIL))
    got = (len(prof[1]), len(prof[2]))
    check(f"N1.drop_head_anchor_{a}_rectangle_breaks_as_predicted", got == want, got)

for t in TAIL:                                                   # drop one tail class
    prof = rect_profile(A, set(TAIL) - {t})
    got = (len(prof[1]), len(prof[2]))
    if t == 12:
        check("N2.drop_class12_is_harmless_discrimination", got == (3, 3), got)
    elif t == 1:
        check("N2.drop_class1_breaks_as_predicted", got == (6, 6), got)
    else:
        check(f"N2.drop_class{t}_breaks", got[0] > 3 or got[1] > 3, got)

PRED_N3 = {3: 22, 5: 8, 11: 10, 15: 8, 30: 6, 55: 8}             # drop one H class
for h, want in PRED_N3.items():
    got = len(screen(7, Y, set(H) - {h}))
    check(f"N3.drop_H_class_{h}_count_as_predicted_ge5", got == want and got >= 5, got)

PRED_N4 = {0: 14, 1: 5, 7: 14, 13: 5, 14: 14}                    # drop one tail anchor
for y, want in PRED_N4.items():
    got = len(screen(7, tuple(v for v in Y if v != y), set(H)))
    check(f"N4.drop_tail_anchor_{y}_count_as_predicted_ge5", got == want and got >= 5, got)

for k in range(3, 9):                                            # no injectivity
    n = 165 << k
    got = len(screen(7, Y, set(H), n))
    check(f"N5.without_injectivity_Zn_count.k{k}", got == (1 << k) and got >= 5, got)

got = len(screen(7, Y, {3, 5, 11}))                              # no rectangle classes
check("N6.old_head_classes_only_count_as_predicted", got == 14, got)


# ------------------------------- N7: machinery positive/negative on genuine tilings
def is_direct_tiling(P, Q, n):
    seen = bytearray(n)
    for p in P:
        for q in Q:
            c = (p + q) % n
            if seen[c]:
                return False
            seen[c] = 1
    return all(seen)


def uniform(S, mod):
    cnt = [0] * mod
    for s in S:
        cnt[s % mod] += 1
    return len(set(cnt)) == 1

for k in range(2, 6):
    n, m = 165 << k, 1 << k
    P0 = list(range(3 * m))
    Q0 = [3 * m * j for j in range(55)]
    ok = (is_direct_tiling(P0, Q0, n)
          and not set(classes(P0, n)) & set(classes(Q0, n))
          and uniform(Q0, 11) and uniform(P0, m))
    check(f"N7.genuine_tiling_positive.k{k}", ok)
    Q1 = [q for q in Q0 if q != 3 * m] + [3 * m + 1]
    bad = (not is_direct_tiling(P0, Q1, n)) and bool(set(classes(P0, n)) & set(classes(Q1, n)))
    check(f"N7.perturbed_nontiling_negative.k{k}", bad)


# ------------------ N8: bounded sanity of standard imports on tiny cyclic groups
def tilings_with(Aset, n):
    Al = sorted(Aset)
    size = n // len(Al)
    covered = bytearray(n)
    for a in Al:
        covered[a] = 1
    B, out = [0], []

    def rec():
        if len(B) == size:
            out.append(tuple(B))
            return
        u = covered.index(0)
        for a in Al:
            b = (u - a) % n
            cells = [(b + x) % n for x in Al]
            if not any(covered[c] for c in cells):
                for c in cells:
                    covered[c] = 1
                B.append(b)
                rec()
                B.pop()
                for c in cells:
                    covered[c] = 0
    rec()
    return out


def prime_powers(n):
    res, p = [], 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            res.append((p, e))
        p += 1
    if n > 1:
        res.append((n, 1))
    return res

for n in (12, 16, 18, 20):
    pp = prime_powers(n)
    tiles, viol = 0, 0
    for s in range(2, n):
        if n % s:
            continue
        for rest in itertools.combinations(range(1, n), s - 1):
            Aset = (0,) + rest
            for Bset in tilings_with(Aset, n):
                tiles += 1
                if set(classes(Aset, n)) & set(classes(Bset, n)):
                    viol += 1
                for p, e in pp:
                    if len(Bset) % p and not uniform(Aset, p ** e):
                        viol += 1
                    if len(Aset) % p and not uniform(Bset, p ** e):
                        viol += 1
    check(f"N8.sands_primepower_ownership_sanity.n{n}", tiles > 0 and viol == 0, [tiles, viol])


# ----------------- B1: background consistency with the adopted n=1320 disposition
n, m = 1320, 8
F = sorted(set(A) | {crt2(r, m, s, 165) for r in range(m) if r % 4 in (1, 2) for s in RECT})
DF = set(classes(F, n))
counts = [len(screen(c, Y, DF, n)) for c in range(11)]
INFO["B1.n1320_forced_heads"] = len(F)
INFO["B1.n1320_forced_classes"] = sorted(DF)
INFO["B1.n1320_mod11_counts"] = counts
INFO["B1.matches_input1_15_classes_and_counts"] = (
    len(F) == 16 and len(DF) == 15 and counts == [4, 5, 5, 4, 14, 14, 14, 3, 14, 14, 14])


# ------------------------------------------------------------------------ report
failed = [c["name"] for c in CHECKS if not c["pass"]]
report = {
    "reviewer": "ReviewF174ShorQ55",
    "wave": "f174-shor-55-tail-infinite-branch",
    "python": sys.version.split()[0],
    "platform": platform.platform(),
    "n_checks": len(CHECKS),
    "n_failed": len(failed),
    "failed": failed,
    "checks": CHECKS,
    "info": INFO,
    "verdict": "PASS" if not failed else "FAIL",
}
with open(sys.argv[1], "x", encoding="utf-8") as fh:
    json.dump(report, fh, indent=1, sort_keys=True)
    fh.write("\n")
print(json.dumps({"verdict": report["verdict"], "n_checks": len(CHECKS),
                  "failed": failed, "info": INFO}, sort_keys=True))
sys.exit(0 if not failed else 1)
