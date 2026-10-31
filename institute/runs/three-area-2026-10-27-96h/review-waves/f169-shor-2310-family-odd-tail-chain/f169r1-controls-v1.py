#!/usr/bin/env python3
"""f169r1 independent exact controls -- reviewer ReviewF169ShorOddTail.

Wave f169-shor-2310-family-odd-tail-chain (aifours run three-area-2026-10-27-96h).
Independently authored by the reviewer; it does not import or execute any author
code. Certificate/data lists are parsed from the frozen packets (SHA-256, bytes and
LF re-verified below) and cross-checked against an independent transcription.
Only exact integer arithmetic (math.gcd, sets, loops, CRT by search).

Abstract "all-k" checks use representatives x in [0, 2*1155) (resp. [0, 2*165)):
such an x fixes parity and all odd-prime residues. For an ODD difference d the gcd
with n = 2^t * oddpart equals gcd(d mod oddpart, oddpart) for every t >= 1, so any
check that only constrains odd differences is exact for every k simultaneously.
Even differences are handled concretely or by the stated pure-2-power rule.

Without --dry-run it writes exactly two new files next to itself (exclusive
creation, never overwrite):
  f169r1-controls-v1.out.txt
  f169r1-controls-v1.receipt.json
"""
import hashlib
import itertools
import json
import math
import os
import platform
import re
import subprocess
import sys

DRY = "--dry-run" in sys.argv
HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.abspath(__file__)
OUT = os.path.join(HERE, "f169r1-controls-v1.out.txt")
RECEIPT = os.path.join(HERE, "f169r1-controls-v1.receipt.json")
EVID = ("/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/"
        "parallel-18/shor-completion/")
INPUTS = [
    ("P1", EVID + "frontier-20261028-2310-family-odd-tail-joint-prime-obstruction-v1.md",
     "b61890594ce5233fd0050d5524a4318a29020aa0ed0d30bded1d37d976d0db80", 11601, 119),
    ("P2", EVID + "frontier-20261028-2310-family-odd-tail-three-residuals-v1.md",
     "fce25631427ffa6e6d128383ebe3afcd4c69abbd46e73a31bc372dbfe166c23b", 11764, 136),
    ("P3", EVID + "frontier-20261028-2310-family-q165-coupled-gcd-obstruction-v1.md",
     "33c641153358510430cd78e5568d7e565129eba71a07c7d88d5be9b8fa5e49b2", 12257, 138),
    ("P4", EVID + "frontier-20261028-165-family-odd-tail-only-55-v1.md",
     "fe70ca41666dc5d6e0675787a519fefd92f37dcda93bf1f52dab82edfe65c62b", 6328, 65),
]
MANIFEST = os.path.join(HERE, "manifest-v1.json")
MANIFEST_SHA = "c93b4a887950735b1a5ea215da629f3a26191fbb6a29fc84f88800377fd3ff00"


def native_date():
    return subprocess.run(["/bin/date", "+%Y-%m-%dT%H:%M:%S%z %Z"],
                          capture_output=True, text=True, check=True).stdout.strip()


DATE_START = native_date()
LOG = []
RESULTS = []  # (label, kind, ok)   kind in POS / NEG / CLAIM


def log(*parts):
    LOG.append(" ".join(str(p) for p in parts))


def check(label, expected, observed, kind="POS"):
    ok = expected == observed
    RESULTS.append((label, kind, ok))
    log(f"[{kind} {'PASS' if ok else 'FAIL'}] {label} | expected={expected!r} | observed={observed!r}")
    return ok


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


# ----------------------------------------------------------------- S00 binding
log("== S00 frozen input binding ==")
check("S00 manifest sha256", MANIFEST_SHA, sha256_bytes(open(MANIFEST, "rb").read()))
TEXT = {}
for tag, path, sha, nbytes, nlf in INPUTS:
    raw = open(path, "rb").read()
    check(f"S00 {tag} sha256/bytes/LF", (sha, nbytes, nlf),
          (sha256_bytes(raw), len(raw), raw.count(b"\n")))
    TEXT[tag] = raw.decode("utf-8")
check("S00 P2 cites P1 sha", True, INPUTS[0][2] in TEXT["P2"])
check("S00 P3 cites P1 and P2 sha", True, INPUTS[0][2] in TEXT["P3"] and INPUTS[1][2] in TEXT["P3"])

# ----------------------------------------------------------------- helpers
A = (0, 3, 8, 11)          # anchored heads (P)
Y = (0, 1, 7, 13, 14)      # anchored tails (Q)
ODD = 1155                 # 3*5*7*11, odd part of n = 2310*2^k
TWO_ODD = 2 * ODD


def g(d, n):
    return math.gcd(d % n, n)


def divset(S, n):
    R = sorted({s % n for s in S})
    return {g(x - y, n) for x in R for y in R if x != y}


def odd_conflict(d, bans, odd=ODD):
    """True iff d is odd and gcd(d, n) (for any n = 2^t*odd) lies in bans."""
    return d % 2 != 0 and math.gcd(d % odd, odd) in bans


def heads_ok_odd(x, bans, odd=ODD):
    return not any(odd_conflict(x - a, bans, odd) for a in A)


def tails_ok_odd(x, bans, odd=ODD):
    return not any(odd_conflict(x - y, bans, odd) for y in Y)


def lab7(x):
    return ("O" if x % 2 else "E") + str(x % 7)


def trip(x):
    return (x % 3, x % 5, x % 11)


def consistent_count(doms, bans, odd=ODD, keep=3):
    keys = list(doms)
    cnt, sols = 0, []
    for combo in itertools.product(*(doms[r] for r in keys)):
        if all(not odd_conflict(combo[i] - combo[j], bans, odd)
               for i in range(len(keys)) for j in range(i + 1, len(keys))):
            cnt += 1
            if len(sols) < keep:
                sols.append(dict(zip(keys, combo)))
    return cnt, sols


def concrete_tail_doms(n, q, residues, bans):
    return {r: [x for x in range(r, n, q) if all(g(x - y, n) not in bans for y in Y)]
            for r in residues}


def concrete_count(n, doms, bans):
    keys = list(doms)
    cnt = 0
    for combo in itertools.product(*(doms[r] for r in keys)):
        if all(g(combo[i] - combo[j], n) not in bans
               for i in range(len(keys)) for j in range(i + 1, len(keys))):
            cnt += 1
    return cnt


# ----------------------------------------------------------------- S01 anchors
log("== S01 anchor divisor sets ==")
for k in range(0, 6):
    n = 2310 * 2 ** k
    DA, DY = divset(A, n), divset(Y, n)
    log(f"   2310-family k={k} n={n}: Div(A)={sorted(DA)} Div(Y)={sorted(DY)}")
    check(f"S01 2310 k={k} Div(A)", sorted({3, 5, 11, math.gcd(8, n)}), sorted(DA))
    check(f"S01 2310 k={k} Div(A) cap Div(Y) empty", [], sorted(DA & DY))
check("S01 G_0", [1, 6, 7, 14], sorted(divset(Y, 2310)))
for k in range(1, 6):
    check(f"S01 G_{k}", [1, 6, 7, 12, 14], sorted(divset(Y, 2310 * 2 ** k)))
for t in range(1, 7):
    n = 165 * 2 ** t
    DA, DY = divset(A, n), divset(Y, n)
    log(f"   165-family t={t} n={n}: Div(A)={sorted(DA)} Div(Y)={sorted(DY)}")
    check(f"S01 165 t={t} Div(A) cap Div(Y)", [2] if t == 1 else [], sorted(DA & DY))

# ----------------------------------------------------------------- S1 P1 sec.3
log("== S1 P1 sec.3 joint-prime missing head classes ==")
JP = [(15, 4), (33, 1), (55, 2)]
for m, c in JP:
    surv = [x for x in range(TWO_ODD) if x % m == c and heads_ok_odd(x, {1, 7})]
    check(f"S1 all-k abstract: no head state in class {c} mod {m} survives odd bans {{1,7}}", [], surv)
for k in range(0, 4):
    n = 2310 * 2 ** k
    for m, c in JP:
        surv = [x for x in range(c, n, m)
                if not any((x - a) % 2 and g(x - a, n) in (1, 7) for a in A)]
        check(f"S1 concrete k={k}: class {c} mod {m} empty", [], surv)
surv = [x for x in range(TWO_ODD) if x % 15 == 4 and heads_ok_odd(x, {1})]
check("S1 NEG without ban 7 the class 4 mod 15 has surviving states", True, len(surv) > 0, "NEG")
log(f"   NEG detail: {len(surv)} survivors, first {surv[:4]}")

# ----------------------------------------------------------------- S2 lists
log("== S2 P1 lists (2) and (1) ==")
cands = [d for d in range(5, ODD + 1) if ODD % d == 0]
log(f"   odd divisors q>=5 of 1155: {cands}")
rem2 = [q for q in cands if sum(1 for p in (3, 5, 11) if q % p) <= 1]
check("S2 list (2)", [15, 33, 55, 105, 165, 231, 385, 1155], rem2)
check("S2 list (1) = (2) minus {15,33,1155}", [55, 105, 165, 231, 385],
      [q for q in rem2 if q not in (15, 33, 1155)])

# ----------------------------------------------------------------- S3 q=1155
log("== S3 P1 sec.4 q=1155 ==")
B_P_ODD = {3, 5, 11}
states = [x for x in range(TWO_ODD) if x % ODD == 2]
for x in states:
    w = [(y, math.gcd((x - y) % ODD, ODD)) for y in Y if odd_conflict(x - y, B_P_ODD)]
    log(f"   state {x} ({'odd' if x % 2 else 'even'}): conflicting old tails (y,gcd) = {w}")
check("S3 all-k abstract: both parities of class 2 mod 1155 excluded", [],
      [x for x in states if tails_ok_odd(x, B_P_ODD)])
check("S3 author witnesses: even x vs 7 gcd 5, odd x vs 14 gcd 3", (5, 3),
      (math.gcd((2 - 7) % ODD, ODD), math.gcd((1157 - 14) % ODD, ODD)))
for k in range(0, 5):
    n = 2310 * 2 ** k
    DA = divset(A, n)
    check(f"S3 concrete k={k}: every x = 2 mod 1155 conflicts with Y via Div(A)", [],
          [x for x in range(2, n, ODD) if not any(g(x - y, n) in DA for y in Y)])
check("S3 NEG without ban 3 the odd state survives", [1157],
      [x for x in states if tails_ok_odd(x, {5, 11})], "NEG")

# ----------------------------------------------------------------- S4 P1 sec.5
log("== S4 P1 sec.5 q=33 / q=15 counting + matching certificates ==")
SC = {}
for k in range(0, 5):
    n = 2310 * 2 ** k
    G = divset(Y, n)
    C = {x for x in range(n) if all(x == a or g(x - a, n) not in G for a in A)}
    SC[k] = (n, G, C)
    cnt = [sum(1 for x in C if x % m == c) for (m, c) in ((5, 2), (5, 4), (11, 1), (11, 6))]
    log(f"   k={k} n={n} |C_k|={len(C)} counts[mod5:2,4 mod11:1,6]={cnt}")
    check(f"S4 k={k} candidates per screened class", [[14, 30, 72, 144, 288][k]] * 4, cnt)
check("S4 no old head in classes 2,4 mod 5 or 1,6 mod 11", [],
      [a for a in A if a % 5 in (2, 4) or a % 11 in (1, 6)])

TRANSCRIBED = {
    (33, 0): [(2192, 129), (1977, 344)],
    (33, 1): [(1067, 129), (4287, 344), (2192, 2439), (792, 2654), (4502, 3564), (1977, 3839)],
    (15, 0): [(1145, 336), (1596, 2195)],
    (15, 1): [(3455, 336), (1145, 963), (3906, 1568), (1596, 2195), (2828, 2646), (2223, 4505)],
    (33, 2): [(5687, 129), (7587, 209), (8907, 344), (1397, 459), (6152, 594),
              (4422, 1664), (2717, 1779), (7472, 1914), (792, 2654), (987, 2849),
              (1122, 2984), (4037, 3099), (8792, 3234), (9122, 3564), (1977, 3839),
              (2307, 4169), (2442, 4304), (737, 4419), (872, 4554), (1067, 4749),
              (4287, 4964), (3627, 5489), (3762, 5624), (2057, 5739), (4947, 6809),
              (462, 6944), (3512, 7194), (5412, 7274), (6267, 8129), (4502, 8184),
              (1782, 8264), (77, 8379), (6597, 8459), (4832, 8514)],
    (15, 2): [(8075, 336), (7536, 578), (5435, 633), (3213, 875), (5765, 963),
              (8526, 1568), (1838, 1656), (8856, 1898), (6755, 1953), (7448, 2646),
              (3158, 2976), (936, 3218), (1233, 3515), (4478, 4296), (2223, 4505),
              (2256, 4538), (155, 4593), (2553, 4835), (3455, 4956), (1145, 5583),
              (1178, 5616), (3576, 5858), (1475, 5913), (3873, 6155), (3906, 6188),
              (2498, 6936), (4896, 7178), (2795, 7233), (2828, 7266), (573, 7475),
              (3818, 8256), (4115, 8553), (1893, 8795), (6843, 9125)],
}


def between(text, start, end):
    i = text.index(start)
    j = text.index(end, i + len(start))
    return text[i + len(start):j]


def pairs_in(seg):
    return [(int(a), int(b)) for a, b in re.findall(r"\((\d+),(\d+)\)", seg)]


T1 = TEXT["P1"]
PARSED = {
    (33, 0): pairs_in(between(T1, "q=33, k=0:", "q=33, k=1:")),
    (33, 1): pairs_in(between(T1, "q=33, k=1:", "q=15, k=0:")),
    (15, 0): pairs_in(between(T1, "q=15, k=0:", "q=15, k=1:")),
    (15, 1): pairs_in(between(T1, "q=15, k=1:", "The 34 disjoint pairs for q=33")),
    (33, 2): pairs_in(between(T1, "The 34 disjoint pairs for q=33 at n=9240 are",
                              "The 34 disjoint pairs for q=15")),
    (15, 2): pairs_in(between(T1, "The 34 disjoint pairs for q=15 at n=9240 are",
                              "In each list the first endpoint")),
}
for key in TRANSCRIBED:
    check(f"S4 certificate {key} parsed == independent transcription", TRANSCRIBED[key], PARSED[key])
CLS = {33: (5, 2, 4), 15: (11, 1, 6)}


def verify_pairs(q, n, G, C, pairs):
    m, c1, c2 = CLS[q]
    probs = []
    ends = [e for p in pairs for e in p]
    if len(set(ends)) != len(ends):
        probs.append("endpoints not distinct")
    for x, y in pairs:
        if x % m != c1:
            probs.append(f"{x} not in class {c1} mod {m}")
        if y % m != c2:
            probs.append(f"{y} not in class {c2} mod {m}")
        if x not in C:
            probs.append(f"{x} not in C")
        if y not in C:
            probs.append(f"{y} not in C")
        if g(x - y, n) not in G:
            probs.append(f"gcd({x}-{y},{n})={g(x - y, n)} not in G")
    return probs


for (q, k), pairs in PARSED.items():
    n, G, C = SC[k]
    m, c1, c2 = CLS[q]
    check(f"S4 certificate q={q} k={k} ({len(pairs)} pairs) valid", [], verify_pairs(q, n, G, C, pairs))
    cand = sum(1 for x in C if x % m in (c1, c2))
    need = 2 * 14 * 2 ** k
    check(f"S4 q={q} k={k} contradiction {cand}-{len(pairs)} < {need}", True, cand - len(pairs) < need)


def max_matching(n, G, C, m, c1, c2):
    L = sorted(x for x in C if x % m == c1)
    R = sorted(x for x in C if x % m == c2)
    adj = {u: [v for v in R if g(u - v, n) in G] for u in L}
    owner = {}

    def augment(u, seen):
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                if v not in owner or augment(owner[v], seen):
                    owner[v] = u
                    return True
        return False

    size = sum(1 for u in L if augment(u, set()))
    return size, len(L), len(R)


MAXM = {}
for q in (33, 15):
    for k in range(0, 4):
        n, G, C = SC[k]
        m, c1, c2 = CLS[q]
        nu, nl, nr = max_matching(n, G, C, m, c1, c2)
        MAXM[(q, k)] = nu
        need = 2 * 14 * 2 ** k
        log(f"   q={q} k={k}: maximum cross matching {nu}; |L|={nl} |R|={nr}; bound {nl + nr - nu} vs quota {need}")
        check(f"S4 q={q} k={k} maximum-matching bound below quota", True, nl + nr - nu < need)

n2, G2, C2 = SC[2]
for k in (3, 4):
    n, G, C = SC[k]
    M = 2 ** (k - 2)
    for q in (33, 15):
        m, c1, c2 = CLS[q]
        for c in (c1, c2):
            lifted = {x0 + 9240 * t for x0 in C2 if x0 % m == c for t in range(M)}
            check(f"S4 lift k={k} q={q} class {c} mod {m}: C_k class == lift of C_2 class", True,
                  lifted == {x for x in C if x % m == c})
        lp = [(x + 9240 * t, y + 9240 * t) for (x, y) in PARSED[(q, 2)] for t in range(M)]
        check(f"S4 lift k={k} q={q}: {len(lp)} lifted pairs valid", [], verify_pairs(q, n, G, C, lp))
        check(f"S4 lift k={k} q={q}: 144M-34M < 112M (M={M})", True, 144 * M - 34 * M < 112 * M)

n0, G0, C0 = SC[0]
alt = next(y for y in sorted(C0) if y % 5 == 4 and g(2192 - y, n0) not in G0)
probs = verify_pairs(33, n0, G0, C0, [(2192, alt), (1977, 344)])
check(f"S4 NEG corrupted pair (2192,{alt}) rejected for gcd not in G_0", True,
      any("not in G" in p for p in probs), "NEG")
check("S4 NEG only 32 of 34 pairs at k=2 gives no contradiction (144-32 not < 112)", False,
      144 - 32 < 112, "NEG")

# ----------------------------------------------------------------- S5 P2 sec.3-4
log("== S5 P2 sec.3-4 q=385 and q=231 ==")
B3 = {3, 5, 11}


def doms_abstract(q, residues, bans):
    return {r: [x for x in range(r, TWO_ODD, q) if tails_ok_odd(x, bans)] for r in residues}


d385 = doms_abstract(385, (3, 24, 25), B3)
check("S5 q=385 domain table (parity, mod 3)", {3: [(1, 2)], 24: [(1, 2)], 25: [(0, 0), (0, 2)]},
      {r: sorted((x % 2, x % 3) for x in d385[r]) for r in d385})
check("S5 q=385 all-k abstract: no consistent (x3,x24,x25)", 0, consistent_count(d385, B3)[0])


def rep(q, r, par, pm, pv):
    return next(x for x in range(r, TWO_ODD, q) if x % 2 == par and x % pm == pv)


check("S5 q=385 cited gcds: x25(E,0)-x3 = 11, x25(E,2)-x24 = 3", (11, 3),
      (math.gcd((rep(385, 25, 0, 3, 0) - rep(385, 3, 1, 3, 2)) % ODD, ODD),
       math.gcd((rep(385, 25, 0, 3, 2) - rep(385, 24, 1, 3, 2)) % ODD, ODD)))
d231 = doms_abstract(231, (22, 25, 26, 36), B3)
check("S5 q=231 domain table (parity, mod 5)",
      {22: [(1, 0)], 25: [(1, 4)], 26: [(0, 0), (0, 4), (1, 4)], 36: [(0, 0), (0, 1), (0, 4)]},
      {r: sorted((x % 2, x % 5) for x in d231[r]) for r in d231})
check("S5 q=231 all-k abstract: no consistent (x22,x25,x26,x36)", 0, consistent_count(d231, B3)[0])
og = lambda u, v: math.gcd((u - v) % ODD, ODD)  # noqa: E731  (odd differences only)
check("S5 q=231 cited gcds", (5, 5, 11, 11, 5),
      (og(rep(231, 26, 0, 5, 0), rep(231, 22, 1, 5, 0)), og(rep(231, 26, 0, 5, 4), rep(231, 25, 1, 5, 4)),
       og(rep(231, 36, 0, 5, 0), rep(231, 25, 1, 5, 4)), og(rep(231, 36, 0, 5, 1), rep(231, 25, 1, 5, 4)),
       og(rep(231, 36, 0, 5, 4), rep(231, 26, 1, 5, 4))))
for k in (0, 1, 2):
    n = 2310 * 2 ** k
    check(f"S5 q=385 concrete k={k}: no consistent triple", 0,
          concrete_count(n, concrete_tail_doms(n, 385, (3, 24, 25), B3), B3))
    check(f"S5 q=231 concrete k={k}: no consistent quadruple", 0,
          concrete_count(n, concrete_tail_doms(n, 231, (22, 25, 26, 36), B3), B3))
c = consistent_count(doms_abstract(385, (3, 24, 25), {3, 5}), {3, 5})[0]
check("S5 NEG q=385 without ban 11 a consistent triple exists", True, c > 0, "NEG")
c = consistent_count(doms_abstract(231, (22, 25, 26, 36), {3, 11}), {3, 11})[0]
check("S5 NEG q=231 without ban 5 a consistent quadruple exists", True, c > 0, "NEG")

# ----------------------------------------------------------------- S6 P2 sec.5
log("== S6 P2 sec.5 q=105 ==")
for t in range(1, 7):
    n = ODD * 2 ** t
    xs = list(range(1, n, 11 * 2 ** t))
    passing = [x for x in xs if not any((x - a) % 2 and g(x - a, n) in (1, 7) for a in A)]
    check(f"S6.1 t={t}: screen survivors have (x mod 3, x mod 5) in {{(0,3),(2,0)}}", True,
          all((x % 3, x % 5) in ((0, 3), (2, 0)) for x in passing))
    check(f"S6.1 t={t}: designated difference has gcd in {{2,14}}", True,
          all(g(x - (11 if x % 3 == 0 else 3), n) in (2, 14) for x in passing))
    full = [x for x in xs if all(g(x - a, n) not in (1, 7, 14) for a in A)]
    check(f"S6.1 t={t}: every head in class 1 mod 11*2^t avoiding gcds 1,7,14 uses gcd 2 ({len(full)} heads)",
          True, all(any(g(x - a, n) == 2 for a in A) for x in full) and len(passing) > 0)

R105 = [0, 1, 7, 13, 14, 5, 10, 11, 16, 71, 72]
CONF105 = [d % 2 == 1 and math.gcd(d % ODD, ODD) in B3 for d in range(TWO_ODD)]


def solve105(conf):
    doms = {r: ([r] if r in Y else list(range(r, TWO_ODD, 105))) for r in R105}
    sols = []

    def bt(i, assign):
        if i == len(R105):
            sols.append(dict(assign))
            return
        r = R105[i]
        for x in doms[r]:
            if all(not conf[(x - z) % TWO_ODD] for z in assign.values()):
                assign[r] = x
                bt(i + 1, assign)
                del assign[r]

    bt(0, {})
    return sols


sols = solve105(CONF105)
check("S6.2 all-k abstract: exactly one consistent assignment on the 11 residues", 1, len(sols))
EXP105 = {0: (0, 0), 1: (1, 1), 5: (0, 0), 7: (1, 7), 10: (1, 0), 11: (0, 1), 13: (1, 2),
          14: (0, 3), 16: (1, 1), 71: (0, 1), 72: (0, 7)}
check("S6.2 forced (parity, mod 11) table", EXP105,
      {r: (sols[0][r] % 2, sols[0][r] % 11) for r in sorted(sols[0])} if sols else None)
check("S6.2 chain residues differ mod 3,5,7 and in forced mod-11 values", True,
      all((r - s) % p for (r, s) in ((0, 71), (71, 72), (72, 14)) for p in (3, 5, 7))
      and all(EXP105[r][1] != EXP105[s][1] for (r, s) in ((0, 71), (71, 72), (72, 14))))


def ac_full105(bans):
    conf = [d % 2 == 1 and math.gcd(d % ODD, ODD) in bans for d in range(TWO_ODD)]
    D = {r: ([r] if r in Y else list(range(r, TWO_ODD, 105))) for r in range(105)}
    changed = True
    while changed:
        changed = False
        for r in range(105):
            for s in range(105):
                if r != s:
                    keep = [x for x in D[r] if any(not conf[(x - z) % TWO_ODD] for z in D[s])]
                    if len(keep) != len(D[r]):
                        D[r] = keep
                        changed = True
    return D


D105 = ac_full105(B3)
log(f"   full-105 arc consistency: min domain {min(len(v) for v in D105.values())}, "
    f"singletons {sum(1 for v in D105.values() if len(v) == 1)}")
check("S6.2 CLAIM full-105 propagation gives the same singletons on the 11 residues", EXP105,
      {r: ((D105[r][0] % 2, D105[r][0] % 11) if len(D105[r]) == 1 else tuple(D105[r])) for r in sorted(EXP105)},
      "CLAIM")
for t in range(1, 7):
    n = ODD * 2 ** t
    X71 = [x for x in range(71, n, 105) if x % 2 == 0 and x % 11 == 1]
    X72 = [x for x in range(72, n, 105) if x % 2 == 0 and x % 11 == 7]
    triples = [(g(u, n), g(v - u, n), g(14 - v, n)) for u in X71 for v in X72]
    check(f"S6.2 t={t}: all chain gcds are pure 2-powers and gcd 2 always occurs ({len(triples)} choices)",
          True, all(all(z & (z - 1) == 0 for z in tr) and 2 in tr for tr in triples) and len(triples) > 0)
negs = solve105([d % 2 == 1 and math.gcd(d % ODD, ODD) in {5, 11} for d in range(TWO_ODD)])
check("S6.2 NEG without ban 3 the 11-residue system is no longer uniquely forced", True, len(negs) > 1, "NEG")
log(f"   NEG detail: {len(negs)} assignments")

# ----------------------------------------------------------------- S7 P3 Q165
log("== S7 P3 Q165 coupled gcd ==")


def dom165(r, F):
    return [x for x in range(r, TWO_ODD, 165) if tails_ok_odd(x, F)]


F1 = {3, 5, 11}
F2 = F1 | {105, 231}
F3 = F1 | {105, 385}
F4 = F1 | {231, 385}
EALL = [f"E{v}" for v in range(7)]
O16 = [f"O{v}" for v in range(1, 7)]
TABLES = {
    "F={3,5,11}": (F1, {2: ["O0"], 3: ["E6", "O0"], 4: ["O0"], 10: ["O0"], 11: ["E1", "O0"], 12: ["O0"]}),
    "F={3,5,11,105,231}": (F2, {2: ["O0"], 11: ["E1", "O0"], 44: EALL}),
    "F={3,5,11,105,385}": (F3, {2: ["O0"], 44: EALL, 55: O16}),
    "F={3,5,11,231,385}": (F4, {2: ["O0"], 4: ["O0"], 8: ["E6", "O0"], 33: ["E6"] + O16, 69: EALL}),
}
for name, (F, tab) in TABLES.items():
    check(f"S7 domain table {name}", {r: sorted(v) for r, v in tab.items()},
          {r: sorted(lab7(x) for x in dom165(r, F)) for r in tab})
doms = {r: dom165(r, F1) for r in (2, 3, 10, 11, 12)}
allsol = [dict(zip(doms, cmb)) for cmb in itertools.product(*doms.values())
          if all(not odd_conflict(a - b, F1) for a, b in itertools.combinations(cmb, 2))]
check("S7 forced x3,x10,x11 states", [("O0", "O0", "O0")],
      sorted({(lab7(s[3]), lab7(s[10]), lab7(s[11])) for s in allsol}))
check("S7 forced gcds vs old tail 0", [(21, 35, 77)],
      sorted({tuple(math.gcd(s[r] % ODD, ODD) for r in (3, 10, 11)) for s in allsol}))
for name, F, rs in (("avoid 105,231", F2, (2, 11, 44)), ("avoid 105,385", F3, (2, 44, 55)),
                    ("avoid 231,385", F4, (2, 4, 8, 33, 69))):
    check(f"S7 all-k abstract {name}: residues {rs} admit no assignment", 0,
          consistent_count({r: dom165(r, F) for r in rs}, F)[0])
    for k in (0, 1):
        n = 2310 * 2 ** k
        check(f"S7 concrete k={k} {name}: no assignment", 0, concrete_count(n, concrete_tail_doms(n, 165, rs, F), F))
    check(f"S7 NEG {name}: with only F={{3,5,11}} the same residues are satisfiable", True,
          consistent_count({r: dom165(r, F1) for r in rs}, F1)[0] > 0, "NEG")

BP = {1, 7, 21, 35, 77}


def heads(par, cls7, bans):
    return [x for x in range(TWO_ODD) if x % 2 == par and x % 7 == cls7 and heads_ok_odd(x, bans)]


check("S7 P cannot avoid all of 105,231,385: no odd head in class 0 mod 7", [],
      heads(1, 0, BP | {105, 231, 385}))
Bh = BP | {231, 385}
U, V = heads(1, 0, Bh), heads(0, 4, Bh)
check("S7 h=105 forced triples (odd class0, even class4)", ([(0, 0, 8)], [(2, 1, 3)]),
      (sorted({trip(x) for x in U}), sorted({trip(x) for x in V})))
check("S7 h=105 no compatible (u,v)", [], [(u, v) for u in U for v in V if not odd_conflict(u - v, Bh)])
Bh = BP | {105, 385}
U, V = heads(1, 1, Bh), heads(0, 3, Bh)
check("S7 h=231 forced triples (odd class1, even class3)", ([(2, 0, 8)], [(0, 1, 3)]),
      (sorted({trip(x) for x in U}), sorted({trip(x) for x in V})))
check("S7 h=231 no compatible (u,v)", [], [(u, v) for u in U for v in V if not odd_conflict(u - v, Bh)])
Bh = BP | {105, 231}
U, V = heads(1, 0, Bh), heads(1, 1, Bh)
check("S7 h=385 forced triples (odd class0, odd class1)", ([(2, 0, 0)], [(0, 3, 8)]),
      (sorted({trip(x) for x in U}), sorted({trip(x) for x in V})))
check("S7 h=385 cross differences have odd part 1", True, all(math.gcd((u - v) % ODD, ODD) == 1 for u in U for v in V))
for t in range(1, 6):
    n = ODD * 2 ** t
    Ut = [x for x in range(n) if x % 2 == 1 and x % 7 == 0 and trip(x) == (2, 0, 0)]
    Vt = [x for x in range(n) if x % 2 == 1 and x % 7 == 1 and trip(x) == (0, 3, 8)]
    odds = list(range(1, 2 ** t, 2))
    check(f"S7 h=385 t={t}: forced odd heads realise every odd residue mod 2^t once", True,
          sorted(x % 2 ** t for x in Ut) == odds and sorted(x % 2 ** t for x in Vt) == odds)
    check(f"S7 h=385 t={t}: cross gcds are exactly 2..2^t", [2 ** j for j in range(1, t + 1)],
          sorted({g(u - v, n) for u in Ut for v in Vt}))


def x2_reason(x):
    for y in Y:
        d = x - y
        if odd_conflict(d, F1):
            return (y, math.gcd(d % ODD, ODD))
        if d % 2 == 0 and math.gcd(d % ODD, ODD) == 1:
            return (y, "pure-2-power")
    return None


reasons = {lab7(x): x2_reason(x) for x in range(2, TWO_ODD, 165)}
log(f"   x2 state -> first conflict: {reasons}")
check("S7 all-k abstract: all 14 states of x2 conflict", [], [s for s, v in reasons.items() if v is None])
for t in range(1, 6):
    n = ODD * 2 ** t
    bans = F1 | {2 ** j for j in range(1, t + 1)}
    check(f"S7 concrete t={t}: every x = 2 mod 165 conflicts", [],
          [x for x in range(2, n, 165) if not any(g(x - y, n) in bans for y in Y)])
n = ODD * 8
surv = [x for x in range(2, n, 165) if not any(g(x - y, n) in {3, 5, 11, 2, 4} for y in Y)]
check("S7 NEG t=3 without 2^t=8 in P-bans some x2 survives", True, len(surv) > 0, "NEG")
log(f"   NEG detail: survivors {surv[:4]}")

# author positive Q-only control at n=18480 (non-load-bearing)
n = 18480


def wv(r):
    if r in (0, 17, 56, 68, 69, 72, 110, 111, 123):
        return 0, 0
    if r in (1, 55, 124, 127):
        return 1, 1
    return {7: (7, 0), 13: (13, 6), 14: (14, 0)}.get(r, (1, 0))


Qc = []
for r in range(165):
    w, v = wv(r)
    sol = [x for x in range(r, n, 165) if x % 7 == v and x % 16 == w]
    Qc.append(sol[0] if len(sol) == 1 else None)
DQ = divset(Qc, n) if None not in Qc else set()
check("S7 CLAIM n=18480 control: 165 distinct, contains Y, avoids {2,3,5,8,11,385}, uses 105,231,4,16",
      (165, True, [], True), (len(set(Qc)), set(Y) <= set(Qc), sorted(DQ & {2, 3, 5, 8, 11, 385}),
                               {105, 231, 4, 16} <= DQ), "CLAIM")

# ----------------------------------------------------------------- S8 P4 165 family
log("== S8 P4 165-family only-55 ==")
check("S8 odd |Q| list", [5, 11, 15, 33, 55, 165], [d for d in range(5, 166) if 165 % d == 0])
for m, c in ((33, 1), (15, 4)):
    check(f"S8 all-t abstract: class {c} mod {m} excluded by odd ban {{1}}", [],
          [x for x in range(330) if x % m == c and heads_ok_odd(x, {1}, odd=165)])
for t in range(1, 7):
    n = 165 * 2 ** t
    DA, DY = divset(A, n), divset(Y, n)

    def hscreen(xs, bans):
        return [x for x in xs if all(x == a or g(x - a, n) not in bans for a in A)]

    check(f"S8 t={t} Q5: class 1 mod 33 empty (full Div(Y))", [], hscreen(range(1, n, 33), DY))
    check(f"S8 t={t} Q11: class 4 mod 15 empty (full Div(Y))", [], hscreen(range(4, n, 15), DY))
    check(f"S8 t={t} Q15: class 1 mod 11*2^t empty (written bans 1,2)", [], hscreen(range(1, n, 11 * 2 ** t), {1, 2}))
    check(f"S8 t={t} Q33: class 1 mod 5*2^t empty (written bans 1,2,6)", [], hscreen(range(1, n, 5 * 2 ** t), {1, 2, 6}))
    check(f"S8 t={t} Q165: tail class 2 mod 165 empty (written bans 3,11)", [],
          [x for x in range(2, n, 165) if all(g(x - y, n) not in (3, 11) for y in Y)])
    s55 = hscreen(range(1, n, 3 * 2 ** t), DY)
    log(f"   t={t} Q55 head class 1 mod 3*2^t survivors under full Div(Y): {len(s55)}")
    if t >= 2:
        check(f"S8 NEG t={t} Q55: same single-class screen does NOT exclude 55", True, len(s55) > 0, "NEG")

# ----------------------------------------------------------------- S9 P2 sec.6 nonvacuity claims
log("== S9 P2 sec.6 nonvacuity relaxations (non-load-bearing) ==")
T2 = TEXT["P2"]
i0 = T2.index("[0,3,8,11,1793")
H = [int(z) for z in re.findall(r"\d+", T2[i0:T2.index("]", i0)])]
H_TR = [0, 3, 8, 11, 1793, 1738, 1573, 1518, 1353, 1298, 1133, 1078, 913, 858,
        693, 638, 473, 418, 253, 198, 33, 3058, 2893, 2838, 2673, 2618, 2453,
        2398, 2233, 2178, 2013, 1958, 396, 63, 68, 183, 128, 243, 132, 303, 248,
        363, 88, 483, 428, 543, 264, 603, 548, 663, 608, 275, 143, 668, 308, 671]
check("S9 head list parsed == transcription", H_TR, H)
n = 9240
DH = divset(H, n)
check("S9 CLAIM 56-head set: contains A, 56 classes mod 56, avoids {1,2,6,7,12,14}",
      (True, 56, 56, []), (set(A) <= set(H), len(set(H)), len({x % 56 for x in H}),
                           sorted(DH & {1, 2, 6, 7, 12, 14})), "CLAIM")
# The packet's "54 individually compatible tail candidates" is ambiguous; both
# readings (old tails excluded / included) are computed and logged; the CLAIM check
# uses the reading that includes the five old tails (dry run: 49 excluded-reading).
TC = [x for x in range(n) if x not in Y and all(g(x - y, n) not in DH for y in Y)]
TCA = [x for x in range(n) if all(x == y or g(x - y, n) not in DH for y in Y)]
cls165 = {x % 165 for x in TC}
clsA = {x % 165 for x in TCA}
log(f"   tail candidates vs Div(H): excluding Y {len(TC)} (mod-165 classes hit {len(cls165)}, absent "
    f"{165 - len(cls165)}); including Y {len(TCA)} (classes hit {len(clsA)}, absent {165 - len(clsA)})")
check("S9 CLAIM 54 compatible tail candidates (old tails included) and >=116 absent mod-165 classes",
      (54, True), (len(TCA), 165 - len(clsA) >= 116), "CLAIM")
Qr = []
for r in range(165):
    m7 = 1 if r == 1 else (6 if r == 13 else 0)
    m8 = {0: 0, 1: 1, 7: 7, 13: 5, 14: 6}.get(r, 3)
    sol = [x for x in range(r, n, 165) if x % 7 == m7 and x % 8 == m8]
    Qr.append(sol[0] if len(sol) == 1 else None)
DQr = divset(Qr, n) if None not in Qr else set()
check("S9 CLAIM 165-tail relaxation at 9240: distinct, contains Y, avoids {3,5,8,11}",
      (165, True, []), (len(set(Qr)), set(Y) <= set(Qr), sorted(DQr & {3, 5, 8, 11})), "CLAIM")

# ----------------------------------------------------------------- S10 P1 sec.6 reported numbers
log("== S10 P1 sec.6 reported matching sizes ==")
check("S10 CLAIM reported matchings 2,6,36 equal maximum cross matchings (q=33)", [2, 6, 36],
      [MAXM[(33, k)] for k in (0, 1, 2)], "CLAIM")
check("S10 CLAIM reported matchings 2,6,36 equal maximum cross matchings (q=15)", [2, 6, 36],
      [MAXM[(15, k)] for k in (0, 1, 2)], "CLAIM")

# ----------------------------------------------------------------- S11 lemma sanity
log("== S11 transversal consequence of the T2 import on small exhaustive tilings ==")


def all_tilings(n, s):
    """All (S, T), 0 in S and T, |S| = s, S (+) T = Z_n: exact cover by translates of S,
    branching on the uncovered point with the fewest admissible translates (bitmasks)."""
    out = []
    full = (1 << n) - 1
    for rest in itertools.combinations(range(1, n), s - 1):
        S = (0,) + rest
        bm = [sum(1 << ((t + b) % n) for b in S) for t in range(n)]
        cand = [[(z - a) % n for a in S] for z in range(n)]

        def rec(cov, T):
            if cov == full:
                out.append((S, tuple(sorted(T))))
                return
            best = None
            for z in range(n):
                if not (cov >> z) & 1:
                    opts = [t for t in cand[z] if not (bm[t] & cov)]
                    if best is None or len(opts) < len(best):
                        best = opts
                        if len(opts) <= 1:
                            break
            for t in best:
                rec(cov | bm[t], T + [t])

        rec(bm[0], [0])
    return out


def transversal(S, m):
    return len(S) == m and len({x % m for x in S}) == m


# Exhaustive only where the number of tilings is small (subgroup-coset factors make
# larger moduli such as 42, 60, 210 explode combinatorially; they were dropped).
for n, s in ((12, 3), (12, 4), (20, 4), (20, 5), (30, 2), (30, 3), (30, 5)):
    assert math.gcd(s, n // s) == 1
    tl = all_tilings(n, s)
    bad = [(S, T) for S, T in tl if not (transversal(S, s) and transversal(T, n // s))]
    check(f"S11 Z_{n} sizes ({s},{n // s}) coprime: all {len(tl)} normalized tilings are transversal pairs",
          (True, []), (len(tl) > 0, bad[:3]))
S8, T8 = (0, 1, 4, 5), (0, 2)
check("S11 NEG Z_8 = {0,1,4,5}+{0,2} (non-coprime sizes) is a tiling whose 4-set is not a transversal mod 4",
      (True, False), (sorted((a + b) % 8 for a in S8 for b in T8) == list(range(8)), transversal(S8, 4)), "NEG")

# ----------------------------------------------------------------- summary / receipt
DATE_END = native_date()
summ = {kind: (sum(1 for _, kk, ok in RESULTS if kk == kind and ok),
               sum(1 for _, kk, _ok in RESULTS if kk == kind)) for kind in ("POS", "NEG", "CLAIM")}
fails = [lbl for lbl, _k, ok in RESULTS if not ok]
SUMMARY = (f"SUMMARY total={len(RESULTS)} passed={sum(ok for *_, ok in RESULTS)} "
           f"POS={summ['POS'][0]}/{summ['POS'][1]} NEG={summ['NEG'][0]}/{summ['NEG'][1]} "
           f"CLAIM={summ['CLAIM'][0]}/{summ['CLAIM'][1]} failed={fails}")
script_sha = sha256_bytes(open(SCRIPT, "rb").read())
head = ["f169r1-controls-v1 output (reviewer ReviewF169ShorOddTail)",
        f"date_start(/bin/date)={DATE_START}",
        f"python={sys.version.split()[0]} platform={platform.platform()}",
        f"script={SCRIPT}", f"script_sha256={script_sha}"]
body = "\n".join(head + LOG + [SUMMARY, f"date_end(/bin/date)={DATE_END}"]) + "\n"
if DRY:
    for line in LOG:
        if "FAIL]" in line:
            print(line)
    print(SUMMARY)
    sys.exit(0)
with open(OUT, "x", encoding="utf-8") as fh:
    fh.write(body)
receipt = {
    "kind": "f169r1 control receipt",
    "reviewer": "ReviewF169ShorOddTail",
    "date_start_bin_date": DATE_START,
    "date_end_bin_date": DATE_END,
    "python": sys.version.split()[0],
    "platform": platform.platform(),
    "script": SCRIPT,
    "script_sha256": script_sha,
    "output": OUT,
    "output_sha256": sha256_bytes(body.encode("utf-8")),
    "output_bytes": len(body.encode("utf-8")),
    "checks_total": len(RESULTS),
    "checks_passed": sum(ok for *_, ok in RESULTS),
    "by_kind_passed_total": summ,
    "failed_labels": fails,
}
with open(RECEIPT, "x", encoding="utf-8") as fh:
    json.dump(receipt, fh, indent=2)
    fh.write("\n")
print(SUMMARY)
print("output_sha256", receipt["output_sha256"])
