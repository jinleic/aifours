#!/usr/bin/env python3
"""reviewer-f128 exact integer control v2 (independently written for review wave
f128-shor-660-exclusion-and-divisibility; imports no author or reviewer code).

v2 corrects a reviewer bug in v1's enumerate_P (it compared the number of
NON-anchor picks against the full |P|, so v1's exact-cover section enumerated
zero P-sets and its 'tilings_found == 0' assertions were vacuous).  v2 asserts a
positive admissible count where one must exist, and replaces the out-of-scope
k=3 search by a bounded exact-cover over sizes 4,5,6 at n=660 (the sizes the
candidate excludes only through the seven-head predecessor).

Checks, with exact Python integers only:
  (A) all-order anchor-only Sands screen: passing n in [2,NMAX] == {660|n or 2310|n};
  (B) order 660: head screen, size list, capacities, size10/12/22 residue facts,
      PLUS exact-cover search for Q >= Y over every balance-admissible P (sizes 7..42)
      and a bounded exact-cover over sizes 4,5,6;
  (C) universal 55-tail: all-k rectangle (mod4 x mod165 enumeration), forced
      classes, projection injectivity, projected class-7 shortage, k=2..9 controls;
  (D) positive and negative controls for every primitive used.
Premises used (stated, from the adopted order1320 disposition): direct tiling
P+Q=Z_n, anchors A<=P, Y<=Q, prime balance, Sands gcd-class disjointness.
"""
import hashlib, json, sys, time
from math import gcd
from itertools import combinations, permutations

A = (0, 3, 8, 11)
Y = (0, 1, 7, 13, 14)
R = {}


def classes(S, n):
    """gcd classes with n of nonzero differences of DISTINCT residues of S mod n."""
    T = sorted({s % n for s in S})
    return {gcd(a - b, n) for a, b in combinations(T, 2)}


def screen(n, anchors, forbidden):
    """x in Z_n with x an anchor, or gcd(x-y,n) outside `forbidden` for every anchor y."""
    anc = {y % n for y in anchors}
    return [x for x in range(n) if x in anc or all(gcd(x - y, n) not in forbidden for y in anc)]


def is_direct_tiling(P, Q, n):
    seen = set()
    for p in P:
        for q in Q:
            s = (p + q) % n
            if s in seen:
                return False
            seen.add(s)
    return len(seen) == n


def sands_disjoint(P, Q, n):
    return not (classes(P, n) & classes(Q, n))


def exact_cover_Q(P, n, forced, node_cap=20_000_000, pclasses=None):
    """Search Q >= forced with P (+) Q = Z_n.  If pclasses is given, additionally
    prune q whose difference with an already chosen q' has gcd in pclasses (Sands).
    Returns (Q or None, nodes, capped)."""
    P = sorted({p % n for p in P})
    full = (1 << n) - 1
    masks = []
    for q in range(n):
        m = 0
        for p in P:
            m |= 1 << ((p + q) % n)
        masks.append(m)
    covered = 0
    Q = []
    for q in forced:
        q %= n
        if masks[q] & covered:
            return None, 0, False
        covered |= masks[q]
        Q.append(q)
    if pclasses and not all(gcd(a - b, n) not in pclasses for a, b in combinations(Q, 2)):
        return None, 0, False
    nodes = [0]
    capped = [False]

    def rec(cov):
        nodes[0] += 1
        if nodes[0] > node_cap:
            capped[0] = True
            return False
        if cov == full:
            return True
        e = (~cov & (cov + 1)).bit_length() - 1   # lowest uncovered residue
        for p in P:
            q = (e - p) % n
            m = masks[q]
            if m & cov == 0:
                if pclasses and any(gcd(q - r, n) in pclasses for r in Q):
                    continue
                Q.append(q)
                if rec(cov | m):
                    return True
                Q.pop()
        return False

    ok = rec(covered)
    return (sorted(Q) if ok else None), nodes[0], capped[0]


def enumerate_P(n, PC, size, caps, limit=None):
    """All P with A<=P<=PC, |P|=size, pairwise P-differences avoiding GY (Sands vs old tails),
    and for each (modulus, per-class count) in caps exactly that many per class."""
    GY = classes(Y, n)
    rest = [x for x in PC if x not in A]
    out = []
    want = size - len(A)
    need = {m: {r: c - sum(1 for a in A if a % m == r) for r in range(m)} for m, c in caps.items()}
    if any(v < 0 for m in need for v in need[m].values()):
        return out
    avail = {m: {r: sum(1 for x in rest if x % m == r) for r in range(m)} for m in caps}
    if any(avail[m][r] < need[m][r] for m in need for r in need[m]):
        return out

    def rec(i, chosen):
        if limit is not None and len(out) >= limit:
            return
        if len(chosen) == want:
            out.append(tuple(sorted(A + tuple(chosen))))
            return
        if i == len(rest) or len(rest) - i < want - len(chosen):
            return
        for m in need:
            if any(avail[m][r] < need[m][r] for r in need[m]):
                return
        x = rest[i]
        if all(need[m][x % m] > 0 for m in need) and all(gcd(x - c, n) not in GY for c in chosen):
            for m in need:
                need[m][x % m] -= 1
                avail[m][x % m] -= 1
            chosen.append(x)
            rec(i + 1, chosen)
            chosen.pop()
            for m in need:
                need[m][x % m] += 1
                avail[m][x % m] += 1
        for m in need:
            avail[m][x % m] -= 1
        rec(i + 1, chosen)
        for m in need:
            avail[m][x % m] += 1

    rec(0, [])
    return out


def crt_pair(r, m, s, k165=165):
    """unique x mod m*165 with x==r (mod m), x==s (mod 165); gcd(m,165)=1 assumed."""
    n = m * k165
    for x in range(s, n, k165):
        if x % m == r:
            return x
    raise ValueError


t0 = time.time()
# ---------------------------------------------------------------- (D) primitive controls
n = 660
Pint, Qint = list(range(10)), [10 * t for t in range(66)]
assert is_direct_tiling(Pint, Qint, n)
assert not is_direct_tiling(Pint, [10 * t for t in range(65)] + [5], n)
assert sands_disjoint(Pint, Qint, n)
assert not sands_disjoint([0, 1], [0, 1], 4)                 # overlapping class {1}
assert is_direct_tiling([0, 3], [0, 1, 2], 6) and sands_disjoint([0, 3], [0, 1, 2], 6)
q, nodes, capped = exact_cover_Q(Pint, n, [0])
assert q is not None and is_direct_tiling(Pint, q, n)
qs, _, _ = exact_cover_Q(Pint, n, [0], pclasses=classes(Pint, n))
assert qs is not None and is_direct_tiling(Pint, qs, n)
q6, _, _ = exact_cover_Q([0, 3], 6, [0])
assert q6 == [0, 1, 2]
for nn in (12, 30, 60):
    qq, _, _ = exact_cover_Q([0, 1, 3], nn, [0])
    assert qq is None                                        # {0,1,3} tiles no Z_n
assert exact_cover_Q(Pint, n, [0, 1])[0] is None             # overlapping forced translates
# enumerate_P positive control: at n=660 size 10 with mod5 caps the set A+{132,407,264,539,275,396} must appear
PC0 = screen(n, A, classes(Y, n))
E10 = enumerate_P(n, PC0, 10, {5: 2})
assert (0, 3, 8, 11, 132, 264, 275, 396, 407, 539) in E10 and all(len(P) == 10 for P in E10)
# enumerate_P negative control: impossible caps give nothing
assert enumerate_P(n, PC0, 11, {11: 1}) == []
R["D_primitive_controls"] = {"tiling_pos": True, "tiling_neg": True, "sands_pos": True, "sands_neg": True,
                            "cover_pos_n660_interval10_nodes": nodes, "cover_pos_sands_pruned": True,
                            "cover_neg_013": True, "enumerate_P_pos_size10_count": len(E10), "enumerate_P_neg_size11": True}

# ---------------------------------------------------------------- (A) divisibility, all n<=NMAX
NMAX = 30000
passing = [m for m in range(2, NMAX + 1) if not (classes(A, m) & classes(Y, m))]
predicted = [m for m in range(2, NMAX + 1) if m % 660 == 0 or m % 2310 == 0]
assert passing == predicted
for m in range(2, NMAX + 1):
    if m % 330:
        assert 1 in classes(A, m) and 1 in classes(Y, m)         # some old P-difference is a unit
    elif m % 4 and m % 7:
        assert gcd(8, m) == 2 == gcd(14, m) and 2 in classes(A, m) and 2 in classes(Y, m)
R["A_divisibility"] = {"NMAX": NMAX, "passing_count": len(passing), "first_passing": passing[:8],
                       "equals_660_or_2310_multiples": True,
                       "negatives": {m: not (classes(A, m) & classes(Y, m)) for m in (330, 990, 1650, 2970, 1980, 2310, 4620)},
                       "below_1980_passing": [m for m in passing if m < 1980]}

# ---------------------------------------------------------------- (B) order 660
n = 660
GA, GY = classes(A, n), classes(Y, n)
assert GA == {3, 4, 5, 11} and GY == {1, 2, 6, 12}
PC = screen(n, A, GY)
QC = screen(n, Y, GA)
assert len(PC) == 42 and set(A) <= set(PC)
sizes = [d for d in range(7, len(PC) + 1) if n % d == 0]
assert sizes == [10, 11, 12, 15, 20, 22, 30, 33]
cnt = lambda S, m, r: sum(1 for x in S if x % m == r)
assert cnt(PC, 3, 1) == 6 and cnt(PC, 5, 2) == 2 and cnt(PC, 5, 4) == 2
B = {"GA": sorted(GA), "GY": sorted(GY), "PC_count": len(PC), "QC_count": len(QC), "PC": PC,
     "size_list": sizes, "PC_mod3": [cnt(PC, 3, r) for r in range(3)], "PC_mod5": [cnt(PC, 5, r) for r in range(5)],
     "PC_mod4": [cnt(PC, 4, r) for r in range(4)], "PC_mod11": [cnt(PC, 11, r) for r in range(11)]}
B["capacity_exclusions"] = {"33": cnt(PC, 3, 1) < 11, "15": cnt(PC, 5, 2) < 3, "20": cnt(PC, 5, 2) < 4,
                            "30": cnt(PC, 5, 2) < 6, "11": (0 % 11 == 11 % 11)}
# size10
c2 = [x for x in PC if x % 5 == 2]; c4 = [x for x in PC if x % 5 == 4]
assert c2 == [132, 407] and c4 == [264, 539]
assert gcd(132 - 407, n) == 55 and gcd(132 - 0, n) == 132
G10 = GA | {55, 132}
Q10 = screen(n, Y, G10)
assert not any(x % 6 == 4 for x in Q10)
ones = [x for x in Q10 if x % 3 == 1]
assert all(x % 2 == 1 for x in ones)
slots10 = {(x % 11, x % 4) for x in ones}
assert len(slots10) == 18 < 22
assert all(gcd(132 * t, n) == 132 for t in range(1, 5))
full10 = classes(A + (132, 407, 264, 539), n)
Q10full = screen(n, Y, full10)
B["size10"] = {"class2": c2, "class4": c4, "Q10_count": len(Q10), "no_4_mod_6": True,
               "ones_count": len(ones), "slots": len(slots10), "needed": 22,
               "full_forced_classes": sorted(full10), "slots_under_full_classes": len({(x % 11, x % 4) for x in Q10full if x % 3 == 1}),
               "sensitivity_slots_without_132": len({(x % 11, x % 4) for x in screen(n, Y, GA | {55}) if x % 3 == 1}),
               "sensitivity_4mod6_without_132": sum(1 for x in screen(n, Y, GA | {55}) if x % 6 == 4)}
# size12
f1 = [x for x in PC if x % 4 == 1]; f2 = [x for x in PC if x % 4 == 2]
assert f1 == [33, 253, 473] and f2 == [198, 418, 638]
F12 = classes(A + tuple(f1 + f2), n)
assert {55, 165, 220} <= F12
G12 = GA | {55, 165, 220}
Q12 = screen(n, Y, G12)
L = [x for x in Q12 if x % 11 == 0 and x != 0]; Rr = [x for x in Q12 if x % 11 == 3 and x != 14]
assert L == [44, 110, 264, 374, 594, 627] and Rr == [47, 80, 300, 410, 564, 630]
assert [y for y in Y if y % 11 == 0] == [0] and [y for y in Y if y % 11 == 3] == [14]
forb = lambda a, b: gcd(a - b, n) in G12
bad = sum(1 for SL in combinations(L, 4) for SR in combinations(Rr, 4) if not any(forb(a, b) for a in SL for b in SR))
assert bad == 0
matchings = [list(zip(L, perm)) for perm in permutations(Rr) if all(forb(a, b) for a, b in zip(L, perm))]
assert matchings
author_pairs = {(110, 47), (264, 80), (594, 410), (627, 564), (374, 630), (44, 300)}
assert all(forb(a, b) for a, b in author_pairs) and {a for a, _ in author_pairs} == set(L) and {b for _, b in author_pairs} == set(Rr)
Q12full = screen(n, Y, F12)
G12m = GA | {165, 220}
Lm = [x for x in screen(n, Y, G12m) if x % 11 == 0 and x != 0]; Rm = [x for x in screen(n, Y, G12m) if x % 11 == 3 and x != 14]
B["size12"] = {"f1": f1, "f2": f2, "forced_classes_all": sorted(F12), "Q12_count": len(Q12), "L": L, "R": Rr,
               "bad_4x4_selections": bad, "perfect_forbidden_matchings": len(matchings), "one_matching": matchings[0],
               "author_matching_verified": True,
               "L_under_all_forced_classes": [x for x in Q12full if x % 11 == 0 and x != 0],
               "R_under_all_forced_classes": [x for x in Q12full if x % 11 == 3 and x != 14],
               "sensitivity_without_55": {"L": Lm, "R": Rm,
                                          "bad_4x4": sum(1 for SL in combinations(Lm, 4) for SR in combinations(Rm, 4)
                                                         if not any(gcd(a - b, n) in G12m for a in SL for b in SR))}}
# size22
k1 = [x for x in PC if x % 11 == 1]
assert k1 == [188, 243] and gcd(188 - 243, n) == 55
G22 = GA | {55}
Q22 = screen(n, Y, G22)
assert not any(x % 5 in (0, 4) and x % 3 == 1 for x in Q22)
extra = [x for x in Q22 if x % 5 in (1, 2, 3) and x % 3 != 1]
assert extra == [47, 627]
B["size22"] = {"class1": k1, "Q22_count": len(Q22), "Q22_mod5": [cnt(Q22, 5, r) for r in range(5)],
               "no_1mod3_in_mod5_classes_0_4": True, "extra_non1_outside": extra,
               "max_non1_in_Q": 12 + len(extra), "needed_non1": 20,
               "sensitivity_extra_without_55": [x for x in screen(n, Y, GA) if x % 5 in (1, 2, 3) and x % 3 != 1]}
# exact-cover confirmation over all balance-admissible P for every size in the list (pure directness search)
EC = {}
for s in sizes:
    caps = {}
    for p in (3, 5, 11):
        if s % p == 0:
            caps[p] = s // p
    if (n // s) % 2 == 1:          # |Q| odd -> Phi_2,Phi_4 divide P -> P uniform mod 4
        caps[4] = s // 4
    Ps = enumerate_P(n, PC, s, caps)
    found, maxnodes, capped_any, sumnodes = 0, 0, False, 0
    for P in Ps:
        q, nodes, capped = exact_cover_Q(P, n, Y)
        maxnodes = max(maxnodes, nodes); sumnodes += nodes
        capped_any |= capped
        if q is not None:
            found += 1
    EC[str(s)] = {"caps": {str(k): v for k, v in caps.items()}, "admissible_P": len(Ps), "tilings_found": found,
                  "max_nodes": maxnodes, "total_nodes": sumnodes, "node_cap_hit": capped_any}
    assert found == 0 and not capped_any
assert EC["10"]["admissible_P"] > 0 and EC["12"]["admissible_P"] > 0 and EC["22"]["admissible_P"] > 0
B["exact_cover_sizes_7_to_42"] = EC
# bounded exact cover for sizes 4,5,6 (excluded by the seven-head predecessor); pure directness first,
# Sands-pruned (P-classes) fallback if the pure search hits the node cap.
EC2 = {}
for s in (4, 5, 6):
    Ps = enumerate_P(n, PC, s, {})
    found, capped_pure, capped_sands, maxn = 0, 0, 0, 0
    for P in Ps:
        q, nodes, capped = exact_cover_Q(P, n, Y, node_cap=300_000)
        maxn = max(maxn, nodes)
        if capped:
            capped_pure += 1
            q, nodes, capped = exact_cover_Q(P, n, Y, node_cap=3_000_000, pclasses=classes(P, n))
            if capped:
                capped_sands += 1
        if q is not None:
            found += 1
    EC2[str(s)] = {"admissible_P": len(Ps), "tilings_found": found, "pure_capped": capped_pure,
                   "sands_pruned_capped": capped_sands, "max_pure_nodes": maxn}
B["exact_cover_sizes_4_to_6"] = EC2
R["B_order660"] = B

# ---------------------------------------------------------------- (C) universal 55-tail
C = {}
def v2fixed(r4, a):
    d = (r4 - a) % 4
    assert d != 0
    return 0 if d % 2 else 1
rect = {}
for r4 in (1, 2):
    surv = [s for s in range(165)
            if all((2 ** v2fixed(r4, a)) * gcd(s - a, 165) not in {1, 2, 6, 12} for a in A)]
    rect[r4] = surv
    assert surv == [33, 88, 143]
# the two excluded CRT cases named in the written proof fail exactly as stated
assert all(any((2 ** v2fixed(1, a)) * gcd(s - a, 165) in {1, 2, 6, 12} for a in A) for s in range(165) if s % 5 == 1 and s % 11 == 3)
assert all(any((2 ** v2fixed(2, a)) * gcd(s - a, 165) in {1, 2, 6, 12} for a in A) for s in range(165) if s % 5 == 0 and s % 11 == 8)
C["rectangle_all_k"] = rect
fam = {}
H = {3, 5, 11, 15, 30, 55}
for k in range(2, 10):
    m = 2 ** k; n = 165 * m
    assert classes(Y, n) == {1, 2, 6, 12}
    GYn = classes(Y, n)
    PCn = screen(n, A, GYn)
    forced = {}
    for r in range(m):
        if r % 4 in (1, 2):
            cls = [x for x in PCn if x % m == r]
            exp = sorted(crt_pair(r, m, s) for s in (33, 88, 143))
            assert cls == exp, (k, r, cls, exp)
            forced[r] = cls
    x143 = crt_pair(1, m, 143); x33 = crt_pair(1, m, 33); y88 = crt_pair(2, m, 88)
    assert gcd(x143 - 8, n) == 15 and gcd(x33 - 3, n) == 30 and gcd(x33 - y88, n) == 55
    inj = {}
    for a in range(2, k):
        xa = crt_pair((1 + 2 ** a) % m, m, 33)
        assert (1 + 2 ** a) % 4 == 1
        inj[a] = gcd(xa - x33, n)
        assert inj[a] == 165 * 2 ** a
    for t in range(1, m // 4):
        assert gcd(660 * t, n) in {165 * 2 ** a for a in range(2, k)}
    assert all(gcd(d, n) == gcd(d, 660) for d in range(1, 660) if gcd(d, 660) in H)
    proj7 = [x for x in screen(660, Y, H) if x % 11 == 7]
    assert proj7 == [7, 73, 337, 601]
    assert (3 * m) % 11 != 0 and 55 % 11 == 0
    fam[k] = {"n": n, "forced_heads": forced if k <= 3 else {"classes": len(forced)}, "injectivity_gcds": inj,
              "projected_class7": proj7}
C["family_k2_to_k9"] = fam
C["H"] = sorted(H)
C["projected_counts_mod11_under_H"] = [sum(1 for x in screen(660, Y, H) if x % 11 == r) for r in range(11)]
C["sensitivity_class7_without"] = {str(c): [x for x in screen(660, Y, H - {c}) if x % 11 == 7] for c in (15, 30, 55)}
R["C_55_tail"] = C

R["elapsed_s"] = round(time.time() - t0, 2)
R["script_sha256"] = hashlib.sha256(open(sys.argv[0], "rb").read()).hexdigest()
R["verdict_controls"] = "ALL ASSERTIONS PASSED"
print(json.dumps(R, indent=1, default=str))
