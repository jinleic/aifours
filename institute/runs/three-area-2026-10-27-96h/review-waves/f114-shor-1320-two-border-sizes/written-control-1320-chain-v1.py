#!/usr/bin/env python3
"""Reviewer-written independent finite control for review f114-shor-1320-two-border-sizes.

Written from scratch by the same-harness reviewer.  It does NOT import or execute
any author script.  The author's packing certificate JSON is read as DATA only and
re-verified with reviewer code.  Every claim below is a finite exact-integer check.

Output: a JSON receipt written next to this file (written-control-1320-chain-output-v1.json)
plus a stdout summary.  Nothing outside the review directory is written.
"""
import hashlib
import json
import os
import re
import sys
import time
from collections import Counter, defaultdict
from itertools import combinations, product
from math import comb, gcd

N = 1320
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "written-control-1320-chain-output-v1.json")
CERT = ("/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/"
        "parallel-18/shor-completion/frontier-20261028-1320-divisor-packing-v1.json")
CERT_SHA = "eb73d65b4e9d2f79b917e4da2d390cd157388341bb75e5c5049a914cf6ef39cb"

results = {}
failures = []
order = []


def check(name, ok, **info):
    results[name] = {"pass": bool(ok), **info}
    order.append(name)
    if not ok:
        failures.append(name)


def sha256_file(p):
    with open(p, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


t0 = time.time()
clock_start = time.strftime("%Y-%m-%dT%H:%M:%S%z")

# ---------------------------------------------------------------------------
# 0. Literal Shor code from the book formula; UD sanity; genuine anchors.
#    C = b{1,a,a^7,a^13,a^14} U {a^3,a^8} b {1,a^2,a^4,a^6} U a^11 b {1,a,a^2}
# ---------------------------------------------------------------------------
def word(i, j):
    return "a" * i + "b" + "a" * j


CODE = sorted(
    {word(0, j) for j in (0, 1, 7, 13, 14)}
    | {word(i, j) for i in (3, 8) for j in (0, 2, 4, 6)}
    | {word(11, j) for j in (0, 1, 2)},
    key=lambda s: (len(s), s),
)
check("code_has_16_words", len(CODE) == 16, words=CODE, max_len=max(map(len, CODE)))


def sardinas_patterson(words):
    S = set(words)
    cur = {y[len(x):] for x in S for y in S if x != y and y.startswith(x)}
    seen = set()
    while cur:
        if "" in cur:
            return False
        key = frozenset(cur)
        if key in seen:
            return True
        seen.add(key)
        nxt = {y[len(x):] for x in cur for y in S if y.startswith(x)}
        nxt |= {x[len(y):] for x in cur for y in S if x.startswith(y)}
        cur = nxt
    return True


check("code_is_UD_sardinas_patterson", sardinas_patterson(CODE))

HEADS = tuple(sorted({len(m.group(1)) for s in CODE for m in [re.fullmatch(r"(a*)(b+)", s)] if m}))
TAILS = tuple(sorted({len(m.group(2)) for s in CODE for m in [re.fullmatch(r"(b+)(a*)", s)] if m}))
TWO_SIDED = [s for s in CODE if not re.fullmatch(r"(a*)(b+)", s) and not re.fullmatch(r"(b+)(a*)", s)]
check("anchor_heads_A", HEADS == (0, 3, 8, 11), heads=HEADS)
check("anchor_tails_Y", TAILS == (0, 1, 7, 13, 14), tails=TAILS)
check("two_sided_words_do_not_feed_borders", len(TWO_SIDED) == 8, two_sided=TWO_SIDED)

# feasible n: A+Y must be direct (all 20 sums distinct mod n); smallest such n
sums = [a + y for a in HEADS for y in TAILS]
def anchors_direct(n):
    return len({s % n for s in sums}) == len(sums)
first_feasible = next(n for n in range(1, 200) if anchors_direct(n))
infeasible_above = [n for n in range(first_feasible, 2 * N + 1) if not anchors_direct(n)]
check("anchor_directness_forces_n_ge_26", first_feasible == 26 and infeasible_above == [],
      first_feasible_n=first_feasible, counterexamples_above=infeasible_above)
check("1320_anchors_direct", anchors_direct(N))

# P != A and Q != Y for every n in [26, 2*N]: residue 6 (resp. 2) is uncovered and
# every candidate complement element collides with an existing anchor pair.
def complement_blocked(n, P, Q, target, grow_Q):
    base = {(p + q) % n for p in P for q in Q}
    if target % n in base:
        return False, "target already covered"
    if grow_Q:
        cands = {(target - p) % n for p in P}
        for q in cands:
            pairs = [((p, qq), (p + qq) % n) for p in P for qq in list(Q) + [q]]
            if len({v for _, v in pairs}) == len(pairs):
                return False, f"q={q} extends directly"
    else:
        cands = {(target - q) % n for q in Q}
        for p in cands:
            pairs = [((pp, q), (pp + q) % n) for pp in list(P) + [p] for q in Q]
            if len({v for _, v in pairs}) == len(pairs):
                return False, f"p={p} extends directly"
    return True, "all candidates collide"

bad_P_eq_A = [n for n in range(26, 2 * N + 1) if not complement_blocked(n, HEADS, TAILS, 6, True)[0]]
bad_Q_eq_Y = [n for n in range(26, 2 * N + 1) if not complement_blocked(n, HEADS, TAILS, 2, False)[0]]
check("P_ne_A_all_n_26_to_2640", bad_P_eq_A == [], failing_n=bad_P_eq_A)
check("Q_ne_Y_all_n_26_to_2640", bad_Q_eq_Y == [], failing_n=bad_Q_eq_Y)

# prime-balance anchor multiplicities quoted in the border note
def class_counts(S, m):
    return dict(sorted(Counter(x % m for x in S).items()))
check("balance_examples_anchor_class_counts", True,
      A_mod5=class_counts(HEADS, 5), A_mod11=class_counts(HEADS, 11), A_mod3=class_counts(HEADS, 3),
      Y_mod3=class_counts(TAILS, 3), Y_mod7=class_counts(TAILS, 7), Y_mod13=class_counts(TAILS, 13),
      A_mod2=class_counts(HEADS, 2), A_mod4=class_counts(HEADS, 4), A_mod8=class_counts(HEADS, 8))

# ---------------------------------------------------------------------------
# 1. Sands necessary direction: brute-force sanity on all normalized tilings of Z_n, n<=18.
# ---------------------------------------------------------------------------
def all_tilings(n):
    out = []
    for d in range(2, n):
        if n % d:
            continue
        e = n // d
        if e < 2:
            continue
        for P in combinations(range(1, n), d - 1):
            P = (0,) + P
            for Q in combinations(range(1, n), e - 1):
                Q = (0,) + Q
                if len({(p + q) % n for p in P for q in Q}) == n:
                    out.append((P, Q))
    return out

sands_viol = []
tiling_count = 0
for n in range(2, 19):
    for P, Q in all_tilings(n):
        tiling_count += 1
        dP = {gcd(p - q, n) for p, q in combinations(P, 2)}
        dQ = {gcd(p - q, n) for p, q in combinations(Q, 2)}
        if dP & dQ:
            sands_viol.append((n, P, Q))
check("sands_necessary_direction_bruteforce_n_le_18", not sands_viol and tiling_count > 0,
      tilings_checked=tiling_count, violations=sands_viol[:3])

# ---------------------------------------------------------------------------
# 2. gcd classes, candidate screens, certificate re-verification at n=1320.
# ---------------------------------------------------------------------------
def gcd_classes(S):
    return {gcd(abs(x - y), N) for x, y in combinations(S, 2)}

GA = gcd_classes(HEADS)
GY = gcd_classes(TAILS)
check("GA_classes", GA == {3, 5, 8, 11}, GA=sorted(GA))
check("GY_classes", GY == {1, 2, 6, 12}, GY=sorted(GY))
check("GA_GY_disjoint", not (GA & GY))

def screened(anchors, forbidden):
    return [x for x in range(N) if all(x == a or gcd(x - a, N) not in forbidden for a in anchors)]

CP = screened(HEADS, GY)
CQ = screened(TAILS, GA)
CPs, CQs = set(CP), set(CQ)
check("CP_has_112", len(CP) == 112, size=len(CP), contains_A=set(HEADS) <= CPs)
check("CQ_has_286", len(CQ) == 286, size=len(CQ), contains_Y=set(TAILS) <= CQs)

def p_conflict(x, y):
    return x != y and gcd(x - y, N) in GY

def q_conflict(x, y):
    return x != y and gcd(x - y, N) in GA

with open(CERT, "rb") as fh:
    raw = fh.read()
check("certificate_sha256", hashlib.sha256(raw).hexdigest() == CERT_SHA, bytes=len(raw))
cert = json.loads(raw)
check("certificate_n", cert.get("n") == N)

tris = cert["P_triangles"]
flat = [x for t in tris for x in t]
ok = (len(tris) == 16 and all(len(t) == 3 and len(set(t)) == 3 for t in tris)
      and len(set(flat)) == 48 and set(flat) <= CPs
      and all(p_conflict(x, y) for t in tris for x, y in combinations(t, 2)))
check("P_16_disjoint_GY_triangles_in_CP", ok, implied_P_upper_bound=len(CP) - 2 * len(tris))

cliques = cert["Q_conflict_cliques"]
flatq = [x for g in cliques for x in g]
ok = (len(cliques) == 130 and all(len(g) >= 1 and len(set(g)) == len(g) for g in cliques)
      and len(flatq) == len(set(flatq)) and set(flatq) == CQs
      and all(q_conflict(x, y) for g in cliques for x, y in combinations(g, 2)))
check("Q_130_GA_cliques_partition_CQ", ok, implied_Q_upper_bound=len(cliques),
      clique_size_histogram=dict(sorted(Counter(len(g) for g in cliques).items())))

wit = cert["P80_divisor_screen_witness"]
ok = (len(wit) == 80 and len(set(wit)) == 80 and set(HEADS) <= set(wit) and set(wit) <= CPs
      and not any(p_conflict(x, y) for x, y in combinations(wit, 2)))
check("P80_witness_is_GY_independent_superset_of_A", ok)

# reviewer-only greedy clique covers (independent of the certificate; may be weaker)
def greedy_cover(vertices, conflict):
    remaining = list(vertices)
    groups = []
    while remaining:
        v = remaining.pop(0)
        g = [v]
        rest = []
        for u in remaining:
            if all(conflict(u, w) for w in g):
                g.append(u)
            else:
                rest.append(u)
        remaining = rest
        groups.append(g)
    return groups

gP = greedy_cover(CP, p_conflict)
gQ = greedy_cover(CQ, q_conflict)
check("reviewer_greedy_cover_bounds", len(gP) >= 80 and len(gQ) >= 130,
      P_greedy_bound=len(gP), Q_greedy_bound=len(gQ),
      note="certificate bounds 80/130 are what the chain uses; greedy is only a sanity cross-check")

divisors = [d for d in range(1, N + 1) if N % d == 0]
cands13 = [d for d in divisors if d <= 80 and N // d <= 130]
check("thirteen_divisor_candidates", cands13 == [11, 12, 15, 20, 22, 24, 30, 33, 40, 44, 55, 60, 66], cands=cands13)
# |P|=11 impossible: P uniform mod 11 (11 | |P|, 11 does not divide |Q|=120) with one element per class, but 0,11 in A share class 0
check("P11_excluded_by_mod11_uniformity", class_counts(HEADS, 11)[0] == 2 and 120 % 11 != 0)
twelve = [d for d in cands13 if d != 11]
check("twelve_sizes", twelve == [12, 15, 20, 22, 24, 30, 33, 40, 44, 55, 60, 66])
# Reviewer recount of the pre-80/130 candidate set from |P|>=5,|Q|>=6 plus prime balance only
def balance_ok(dP):
    dQ = N // dP
    # P side minimums from anchors when p | |P|: uniform mod p requires |P| >= p*max class count of A
    # Q side minimums when p | |Q|
    for p in (3, 5, 11):
        if dP % p == 0:
            if dP < p * max(class_counts(HEADS, p).values()):
                return False
        else:
            if dQ < p * max(class_counts(TAILS, p).values()):
                return False
    return True
pre = [d for d in divisors if d >= 5 and N // d >= 6 and balance_ok(d)]
check("reviewer_recount_pre_divisor_candidates", True, count=len(pre), sizes=pre,
      note="packet quotes 'preceding 17'; this reviewer recount from (|P|>=5,|Q|>=6)+balance alone gives the listed count; the '17' is not derivable from manifest inputs and is not load-bearing")

# ---------------------------------------------------------------------------
# 3. Four-border deductions.
# ---------------------------------------------------------------------------
P1 = [x for x in CP if x % 3 == 1]
check("CP_mod3_class1_list", P1 == [88, 253, 256, 415, 418, 583, 748, 913, 916, 1075, 1078, 1243], list=P1,
      CP_mod3_counts=class_counts(CP, 3))
pairs4 = [(88, 916), (256, 748), (253, 415), (583, 1075)]
ok = len({x for p in pairs4 for x in p}) == 8 and all(x in P1 and y in P1 and p_conflict(x, y) for x, y in pairs4)
check("P1_four_disjoint_GY_pairs", ok, gcds=[gcd(x - y, N) for x, y in pairs4])


def max_independent(vs, conflict, extra_ok=lambda chosen: True):
    best = [0, None]
    vs = list(vs)

    def rec(i, chosen):
        if len(chosen) + len(vs) - i <= best[0]:
            return
        if i == len(vs):
            if len(chosen) > best[0]:
                best[0] = len(chosen)
                best[1] = list(chosen)
            return
        v = vs[i]
        if all(not conflict(v, c) for c in chosen) and extra_ok(chosen + [v]):
            rec(i + 1, chosen + [v])
        rec(i + 1, chosen)

    rec(0, [])
    return best[0], best[1]

mis_P1, mis_P1_set = max_independent(P1, p_conflict)
check("P1_exact_max_GY_independent_is_8", mis_P1 == 8, size=mis_P1, example=mis_P1_set,
      note="uniform-mod-3 sizes 30,33,60,66 need 10,11,20,22 in this class")
P2m5 = [x for x in CP if x % 5 == 2]
check("CP_mod5_class2_list", P2m5 == [132, 407, 792, 872, 987, 1067], list=P2m5, CP_mod5_counts=class_counts(CP, 5),
      note="uniform-mod-5 sizes 40,55 need 8,11 in this class")

# |P|=15: P uniform mod 3 and mod 5. Need 5 elements ==1 mod 3 of which <=1 is ==3 mod 5.
not3 = [x for x in P1 if x % 5 != 3]
check("P1_outside_mod5_class3", not3 == [256, 415, 916, 1075], list=not3)
block_ok = all(any(p_conflict(x, y) for y in not3) for x in P1 if x % 5 == 3)
exhaustive15 = all(
    (sum(1 for x in S if x % 5 == 3) > 1) or any(p_conflict(x, y) for x, y in combinations(S, 2))
    for S in combinations(P1, 5)
)
check("P15_excluded_blocking_and_exhaustive_5subsets", block_ok and exhaustive15,
      five_subsets_checked=comb(12, 5))

# |P|=22: Q uniform mod 3 (20 per class) and mod 5 (12 per class).
check("CQ_has_no_residue_4_mod_6", not any(x % 6 == 4 for x in CQ), CQ_mod6_counts=class_counts(CQ, 6))
q22 = {}
q22_ok = True
for r in (1, 2, 3):
    non1 = [x for x in CQ if x % 5 == r and x % 3 != 1]
    odd = [x for x in non1 if x % 2]
    even = [x for x in non1 if not x % 2]
    mis, _ = max_independent(non1, q_conflict)
    ones = [x for x in CQ if x % 5 == r and x % 3 == 1]
    ones_odd_all = all(x % 2 for x in ones)
    # proof step: any even non-1 candidate e conflicts (gcd exactly 5) with at least one of any two
    # odd 1-mod-3 candidates in this class with distinct mod-11 residues
    step = all(
        (gcd(e - o1, N) == 5) or (gcd(e - o2, N) == 5)
        for e in even for o1, o2 in combinations(ones, 2) if o1 % 11 != o2 % 11
    )
    per330 = max(Counter((x % 11) for x in ones).values()) if ones else 0
    q22[r] = {"non1_count": len(non1), "odd_count": len(odd), "even_count": len(even),
              "non1_max_GA_independent": mis, "ones_count": len(ones), "ones_all_odd": ones_odd_all,
              "even_vs_two_odd_ones_distinct_mod11_always_gcd5": step,
              "max_ones_sharing_mod11": per330}
    q22_ok &= (len(non1) == 10 and len(odd) == 4 and mis <= 6 and ones_odd_all and step and per330 <= 4)
check("Q22_three_mod5_classes_force_ge8_ones_each", q22_ok, classes=q22,
      conclusion="ge 8 ones per class r=1,2,3 -> ge 24 > 20 required by mod-3 uniformity")
qedges = {1: [(891, 386), (971, 276), (561, 716), (641, 1266)],
          2: [(627, 722), (707, 282), (47, 612), (1287, 1052)],
          3: [(363, 68), (443, 618), (693, 1058), (773, 948)]}
edges_ok = all(
    len({x for e in es for x in e}) == 8 and all(x in CQs and y in CQs and x % 5 == r and y % 5 == r
                                                 and x % 3 != 1 and y % 3 != 1 and gcd(x - y, N) == 5
                                                 for x, y in es)
    for r, es in qedges.items())
check("Q22_listed_gcd5_pairs", edges_ok)

# ---------------------------------------------------------------------------
# 4. Three-border Hall counts for |P|=12,|Q|=110 (Q uniform mod 11, 10 per class).
# ---------------------------------------------------------------------------
L = [x for x in CQ if x % 11 == 0 and x != 0]
R = [x for x in CQ if x % 11 == 3 and x != 14]
check("hall_L_R_sizes_25", len(L) == 25 and len(R) == 25, L=L, R=R, CQ_mod11_counts=class_counts(CQ, 11))
check("hall_edge_set_equals_3_5_8", all(gcd(x - y, N) != 11 for x in L for y in R))
masksL = [sum(1 << j for j, y in enumerate(R) if q_conflict(x, y)) for x in L]
masksR = [sum(1 << i for i, x in enumerate(L) if q_conflict(x, y)) for y in R]

def hall_scan(masks, k):
    hist = Counter()
    best = 10 ** 9
    arg = None
    cnt = 0
    for grp in combinations(range(len(masks)), k):
        m = 0
        for i in grp:
            m |= masks[i]
        s = bin(m).count("1")
        hist[s] += 1
        cnt += 1
        if s < best:
            best, arg = s, grp
    return cnt, best, hist[best], dict(sorted(hist.items())), arg

cntF, minF, nminF, histF, argF = hall_scan(masksL, 9)
cntR, minR, nminR, histR, argR = hall_scan(masksR, 8)
check("hall_forward_9subsets_of_L", cntF == comb(25, 9) and minF == 18 and nminF == 11,
      subsets=cntF, min_neighbors=minF, minimizers=nminF, histogram=histF,
      example=[L[i] for i in argF], deduction="25-18=7 < 9 required from R")
check("hall_reverse_8subsets_of_R", cntR == comb(25, 8) and minR == 17 and nminR == 10,
      subsets=cntR, min_neighbors=minR, minimizers=nminR, histogram=histR,
      example=[R[i] for i in argR], deduction="25-17=8 < 9 required from L")

# ---------------------------------------------------------------------------
# 5. Two-border: exclude (20,66) via forced gcd class 264 on both sides.
# ---------------------------------------------------------------------------
c2 = [x for x in CP if x % 5 == 2]
c4 = [x for x in CP if x % 5 == 4]
check("CP_mod5_class4_list", c4 == [264, 344, 459, 539, 924, 1199], list=c4)
match = [(132, 924), (407, 1199), (792, 264), (872, 344), (987, 459), (1067, 539)]
ok = ({x for x, _ in match} == set(c2) and {y for _, y in match} == set(c4)
      and all(gcd(x - y, N) == 264 for x, y in match))
# brute force: every (4 of c2) x (4 of c4) choice contains >= 2 matched pairs
min_hits = min(sum(1 for x, y in match if x in S and y in T) for S in combinations(c2, 4) for T in combinations(c4, 4))
check("P20_forces_gcd264_perfect_matching", ok and min_hits >= 1, min_matched_pairs_over_all_choices=min_hits,
      A_mod5_counts=class_counts(HEADS, 5))

G264 = GA | {264}
def q2_conflict(x, y):
    return x != y and gcd(x - y, N) in G264

ones_all = [x for x in CQ if x % 3 == 1]
check("CQ_ones_all_odd", all(x % 2 for x in ones_all), count=len(ones_all))
slots = defaultdict(list)
for x in ones_all:
    slots[(x % 11, x % 8)].append(x)
check("ones_occupy_44_odd_slots", len(slots) == 44 and all(k[1] in (1, 3, 5, 7) for k in slots),
      slot_size_histogram=dict(sorted(Counter(len(v) for v in slots.values()).items())))
# slot capacity 1 under no-264: two 1-mod-3 elements in one slot differ by a nonzero multiple of 264 -> gcd 264
check("same_slot_pairs_have_gcd_264", all(gcd(x - y, N) == 264 for v in slots.values() for x, y in combinations(v, 2)))

non1_by11 = {j: [x for x in CQ if x % 11 == j and x % 3 != 1] for j in range(11)}
check("non1_candidates_per_mod11_class", all(len(non1_by11[j]) == 10 for j in (1, 2, 7)),
      sizes={j: len(v) for j, v in non1_by11.items()},
      Y_mod11={y: y % 11 for y in TAILS})
JS = (1, 2, 7)
pool = sorted({x for j in JS for x in non1_by11[j]})
anchor_bad = {x for x in pool if any(q2_conflict(x, y) for y in TAILS)}
pool_conf = {x: {y for y in pool if q2_conflict(x, y)} for x in pool}
slot_block = {k: [frozenset(y for y in pool if q2_conflict(c, y)) for c in v] for k, v in slots.items()}
anchors_vs_pool_in_class = {j: [x for x in non1_by11[j] if x in anchor_bad] for j in JS}

total = compatible = slot_rej = quota_rej = residual = 0
residual_examples = []
for trip in product(*(list(combinations(non1_by11[j], 2)) for j in JS)):
    total += 1
    seed = {x for pr in trip for x in pr}
    if seed & anchor_bad or any(b in pool_conf[a] for a, b in combinations(seed, 2)):
        continue
    compatible += 1
    open_by_j = Counter()
    for (j, m8), blocks in slot_block.items():
        if any(not (seed & blk) for blk in blocks):
            open_by_j[j] += 1
    if sum(open_by_j.values()) < 22:
        slot_rej += 1
        continue
    bad = False
    for j in JS:
        in_seed = [x for x in non1_by11[j] if x in seed]
        extra = [x for x in non1_by11[j] if x not in seed and x not in anchor_bad and not (pool_conf[x] & seed)]
        if len(in_seed) + open_by_j[j] + len(extra) < 6:
            bad = True
            break
    if bad:
        quota_rej += 1
    else:
        residual += 1
        if len(residual_examples) < 5:
            residual_examples.append(sorted(seed))
check("Q66_no264_relaxed_seed_test", (total, compatible, slot_rej, quota_rej, residual) == (91125, 1143, 1089, 54, 0),
      seeds=total, compatible_seeds=compatible, slot_rejections=slot_rej, quota_rejections=quota_rej,
      residual=residual, residual_examples=residual_examples,
      anchors_vs_pool_264_or_GA_bad_in_class=anchors_vs_pool_in_class)

# Independent sanity on the no-264 premise logic: under no-264 at most 4 ones per mod-11 class.
check("ones_per_mod11_class_cap_4_under_no264", all(
    len({k[1] for k in slots if k[0] == j}) <= 4 for j in range(11)),
    open_slot_counts_per_class={j: len([k for k in slots if k[0] == j]) for j in range(11)})

# ---------------------------------------------------------------------------
# 6. Final cardinality status after the chain (reviewer summary table).
# ---------------------------------------------------------------------------
excluded = {
    11: "mod-11 uniformity vs anchors 0,11",
    15: "P15 blocking (sec.3 four-border)", 22: "Q22 mod5/mod3 (sec.4 four-border)",
    30: "mod3 class cap 8", 33: "mod3 class cap 8", 60: "mod3 class cap 8 / mod5 cap 6", 66: "mod3 class cap 8",
    40: "mod5 class-2 cap 6", 55: "mod5 class-2 cap 6",
    12: "Hall two-class obstruction", 20: "gcd-264 on both sides (Sands)",
}
surviving = [d for d in cands13 if d not in excluded]
check("surviving_pairs", surviving == [24, 44], surviving_P=surviving, surviving_pairs=[(d, N // d) for d in surviving])

# sharpness/status of the two survivors against the same elementary screens (NOT an exclusion attempt)
# (24,55): 3|24 -> P uniform mod 3 -> exactly 8 in class 1 mod 3; exact max is 8 (tight).  5,11 | 55 -> Q uniform mod 5 and 11.
# (44,30): 11|44 -> P uniform mod 11 (4 per class); 3,5 | 30 -> Q uniform mod 3 (10) and mod 5 (6).
check("survivor_screen_status_informational", True,
      P24_class1_mod3_required=8, P24_class1_mod3_exact_max=mis_P1,
      P44_mod11_required_per_class=4, CP_mod11_counts=class_counts(CP, 11),
      Q30_mod5_required_per_class=6, Q30_mod3_required_per_class=10,
      note="informational only; this review does not attempt to exclude or construct (24,55)/(44,30)")

# ---------------------------------------------------------------------------
# receipt
# ---------------------------------------------------------------------------
clock_end = time.strftime("%Y-%m-%dT%H:%M:%S%z")
receipt = {
    "control": "written-control-1320-chain-v1.py",
    "control_sha256": sha256_file(os.path.abspath(__file__)),
    "python": sys.version.split()[0],
    "clock_start_local": clock_start,
    "clock_end_local": clock_end,
    "elapsed_seconds": round(time.time() - t0, 3),
    "certificate_path": CERT,
    "n": N,
    "check_order": order,
    "failures": failures,
    "all_pass": not failures,
    "results": results,
}
with open(OUT, "w") as fh:
    json.dump(receipt, fh, indent=1, sort_keys=False)
    fh.write("\n")
print(json.dumps({"all_pass": not failures, "failures": failures, "checks": len(order),
                  "elapsed_seconds": receipt["elapsed_seconds"], "output": OUT}, indent=1))
