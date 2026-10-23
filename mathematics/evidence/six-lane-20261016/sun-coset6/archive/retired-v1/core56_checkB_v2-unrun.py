#!/usr/bin/env python3
"""core56_checkB_v2 -- separately coded checker for the engine-v3 certificates of Core5(6).

This is a lane SELF-REPORT: same author as the engine, so it is not parent-independent.
It imports nothing from the engines; everything is recomputed from rules-k6-v1/v2/v3:
  1. Derives the 8 special-placement types from first principles, with stabilisers that fix the
     E2 vertex (and its class) and the E3 vertex; E2 and E3 are never exchanged.
  2. Re-enumerates every T-consistent labelled leaf, using lexicographic edge order and its own
     tau computation. Counts are compared with the engine, and so is the sha256 of the sorted leaf
     codes, written in the engine's edge order.
  3. Recomputes the orbits with its own canonical form: lexicographic minimum over the stabiliser,
     restricted to permutations that respect a vertex-invariant ordering. Checks that the engine's
     orbit list is exactly this set.
  4. Verifies every certificate exactly:
       K, P, N26     recomputed;
       RLP           exact check of the engine's dual for EVERY admissible q, against ALL
                     hereditary-allowed supports recomputed here;
       FH5           its own exhaustive fibre search, for all 7 E5 placements;
       RPLP          rebuilds columns, bounds and forced containments, then checks every dual inequality.
Usage: python3 core56_checkB_v2.py ENGINE_OUTDIR OUTDIR
"""
import gzip
import hashlib
import itertools
import json
import os
import sys
import time
from fractions import Fraction as Q
from math import gcd

NV = 6
LEX = [(i, j) for i in range(NV) for j in range(i + 1, NV)]
ENG = sorted(LEX, key=lambda e: (e[1], e[0]))  # the engine's edge order (only for codes/hashes)
SAT = 30


def types_from_first_principles():
    """Orbit representatives of special placements (E2 vertex+class or none; E3 vertex or none) under S6."""
    reps = []
    for e2 in (None, 0):
        for c2 in ((0,) if e2 is None else (1, 2)):
            e3opts = [None, 0] if e2 is None else [None, 0, 1]
            for e3 in e3opts:
                reps.append((e2, c2, e3))
    return reps


def stabiliser(t):
    e2, c2, e3 = t
    out = []
    for p in itertools.permutations(range(NV)):
        if e2 is not None and p[e2] != e2:
            continue
        if e3 is not None and p[e3] != e3:
            continue
        out.append(p)
    return out


def v2_(n):
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


def v3_(n):
    c = 0
    while n % 3 == 0:
        n //= 3
        c += 1
    return c


def v5_(n):
    c = 0
    while n % 5 == 0:
        n //= 5
        c += 1
    return c


class Cfg:
    def __init__(self, al, t):
        self.al = al  # 6x6 list
        self.e2, self.c2, self.e3 = t

    def g_ar(self, alpha, z):
        if alpha == 2 and z == self.e2:
            return 2
        if alpha == 3 and z == self.e3:
            return 3
        if alpha == 4 and z == self.e2:
            return 2 if self.c2 == 1 else 4
        return 1

    def tmin(self, x, y, z):
        t = 1
        for p, q, o in ((x, y, z), (x, z, y), (y, z, x)):
            A = self.al[p][q]
            need = A // self.g_ar(A, o)
            t = t * need // gcd(t, need)
        return t

    def tmax(self, x, y, z):
        a, b, c = self.al[x][y], self.al[x][z], self.al[y][z]
        return min(a * b, a * c, b * c)

    def st(self, j):
        return ((self.c2 if j == self.e2 else 0), (1 if j == self.e3 else 0))


def herok(members, g):
    for r in range(2, len(members) + 1):
        for T in itertools.combinations(members, r):
            if max(g(x, y) for x, y in itertools.combinations(T, 2)) < r:
                return False
    return True


def qexp(q, st):
    a = v2_(q) + (0 if st[0] == 0 else (1 if st[0] == 1 else SAT))
    b = v3_(q) + (SAT if st[1] else 0)
    return a, b


def allowed_supports(qs, sts):
    n = len(qs)
    ex = [qexp(qs[x], sts[x]) for x in range(n)]

    def g(x, y):
        return (2 ** min(ex[x][0], ex[y][0])) * (3 ** min(ex[x][1], ex[y][1]))
    return [T for r in range(1, n + 1) for T in itertools.combinations(range(n), r) if r == 1 or herok(T, g)]


_RLPOK = {}


def rlp_dual_ok(key, qs, sts, duals):
    if key in _RLPOK:
        return _RLPOK[key]
    ok = False
    if key in duals:
        y = [Q(s) for s in duals[key]["y"]]
        if len(y) == len(qs) and all(x >= 0 for x in y):
            if all(sum(y[j] for j in T) <= 1 for T in allowed_supports(qs, sts)):
                ok = sum(Q(qs[j], 5) * y[j] for j in range(len(qs))) >= 1
    _RLPOK[key] = ok
    return ok


def key_of(qs, sts):
    return "%s|%s" % (",".join(map(str, qs)), ";".join("%d%d" % s for s in sts))


def check_K(C, v, S):
    if sum(C.al[i][v] for i in S) < 5:
        return False
    return all(C.tmin(i, v, j) == C.al[i][v] * C.al[v][j] for i, j in itertools.combinations(S, 2))


def check_RLP(C, v, duals):
    nb = [w for w in range(NV) if w != v]
    sts = tuple(C.st(j) for j in nb)
    for qs in itertools.product(*[range(1, 6 - C.al[v][j]) for j in nb]):
        if not rlp_dual_ok(key_of(qs, sts), qs, sts, duals):
            return False
    return True


def pbounds(C, v, j, k):
    a = C.al[j][k]
    unit = Q(1, 5 * C.g_ar(a, v))
    xj, xk = Q(C.al[v][j], 5), Q(C.al[v][k], 5)
    low = max(Q(C.tmin(v, j, k), 5 * a), xj + xk - 1, Q(0))
    low = (-((-low) // unit)) * unit
    sm = min(xj, xk)
    hi = (sm // unit) * unit
    if hi == sm:
        cj = C.al[v][j] + C.al[k][j] <= 4
        ck = C.al[v][k] + C.al[j][k] <= 4
        allow = cj if xj < xk else (ck if xk < xj else (cj and ck))
        if not allow:
            hi -= unit
    return low, hi


def check_P(C, v, kind, wit):
    nb = [w for w in range(NV) if w != v]
    if kind == "Ppair":
        j, k = wit
        lo, hi = pbounds(C, v, j, k)
        return lo > hi
    S = wit
    tops = {}
    for j, k in itertools.combinations(nb, 2):
        lo, hi = pbounds(C, v, j, k)
        if lo > hi:
            return True
        tops[(j, k)] = hi
    x = {j: Q(C.al[v][j], 5) for j in nb}
    lhs = sum(1 - x[j] for j in S) - sum(1 - x[j] - x[k] + tops[tuple(sorted((j, k)))] for j, k in itertools.combinations(S, 2))
    return lhs >= 1


def check_N26(C, v):
    if v == C.e2:
        return False
    nb = [w for w in range(NV) if w != v]
    if any(C.al[v][j] != 2 for j in nb):
        return False
    if any(C.al[j][k] not in (2, 4) for j, k in itertools.combinations(nb, 2)):
        return False
    if v == C.e3:
        for j, k, l in itertools.combinations(nb, 3):
            tm, tM = C.tmin(j, k, l), C.tmax(j, k, l)
            if tm % 3 != 0 and tM >= 3 * tm:
                return False
    return True


def fib_ex(C, l, t, e5):
    a, b, c = v2_(t), v3_(t), v5_(t)
    if l == C.e2:
        a += 1 if C.c2 == 1 else SAT
    if l == C.e3:
        b += SAT
    if l == e5:
        c += SAT
    return a, b, c


def fibre_any(C, e5, inside, forced):
    menu = []
    for l in range(NV):
        if l == inside[0]:
            menu.append([(1, frozenset([0]))])
        elif l in inside:
            menu.append([(1, frozenset([c])) for c in range(5)])
        elif l in forced:
            menu.append([(forced[l], frozenset(M)) for M in itertools.combinations(range(5), forced[l])])
        else:
            menu.append([(t, frozenset(M)) for t in range(1, 6) for M in itertools.combinations(range(5), t)])
    for pick in itertools.product(*menu):
        t = [p[0] for p in pick]
        if any(t[i] == 1 and C.al[i][l] > t[l] for i in range(NV) for l in range(NV) if l != i):
            continue
        ex = [fib_ex(C, l, t[l], e5) for l in range(NV)]

        def g(x, y):
            return (2 ** min(ex[x][0], ex[y][0])) * (3 ** min(ex[x][1], ex[y][1])) * (5 ** min(ex[x][2], ex[y][2]))
        if all(herok([l for l in range(NV) if cst in pick[l][1]], g) for cst in range(5)
               if len([l for l in range(NV) if cst in pick[l][1]]) >= 2):
            return True
    return False


def check_FH5(C, ab):
    a, b = ab
    if C.al[a][b] != 1:
        return False
    Vs = {v: C.al[v][a] for v in range(NV) if v not in (a, b) and C.al[v][a] == C.al[v][b]}
    if not Vs:
        return False
    inside = [a, b] + sorted(v for v in Vs if Vs[v] == 1)
    forced = {v: c for v, c in Vs.items() if c > 1}
    return not any(fibre_any(C, e5, inside, forced) for e5 in [None] + list(range(NV)))


def rplp_columns(C, v, qs):
    nb = [w for w in range(NV) if w != v]
    qd = dict(zip(nb, qs))
    ex = {j: qexp(qd[j], C.st(j)) for j in nb}

    def g(x, y):
        return (2 ** min(ex[x][0], ex[y][0])) * (3 ** min(ex[x][1], ex[y][1]))
    forced = [(w, j) for w in nb for j in nb if w != j and C.tmin(v, w, j) >= C.al[v][w] * C.al[w][j]]
    cols = []
    for r in range(1, 6):
        for Aset in itertools.combinations(nb, r):
            As = set(Aset)
            if any(j in As and w not in As for (w, j) in forced):
                continue
            for rr in range(0, r + 1):
                for Ss in itertools.combinations(Aset, rr):
                    if rr >= 2 and not herok(Ss, g):
                        continue
                    cols.append((As, set(Ss)))
    return nb, cols


def check_RPLP(C, v, certs, duals):
    nb = [w for w in range(NV) if w != v]
    sts = tuple(C.st(j) for j in nb)
    pairs = list(itertools.combinations(nb, 2))
    qlist = list(itertools.product(*[range(1, 6 - C.al[v][j]) for j in nb]))
    if len(certs) != len(qlist):
        return False
    for qs, cert in zip(qlist, certs):
        if cert[0] == "R":
            if cert[1] != key_of(qs, sts) or not rlp_dual_ok(cert[1], qs, sts, duals):
                return False
            continue
        vec = [Q(s) for s in cert[1]]
        if len(vec) != 30:
            return False
        a = dict(zip(nb, vec[0:5]))
        b = dict(zip(nb, vec[5:10]))
        u = dict(zip(pairs, vec[10:20]))
        l = dict(zip(pairs, vec[20:30]))
        if any(x < 0 for x in vec[10:30]):
            return False
        _, cols = rplp_columns(C, v, qs)
        for As, Ss in cols:
            lhs = sum(a[j] for j in Ss) + sum(b[j] for j in As)
            lhs += sum(-u[p] + l[p] for p in pairs if p[0] in As and p[1] in As)
            if lhs > 1:
                return False
        qd = dict(zip(nb, qs))
        obj = sum(a[j] * Q(qd[j], 5) for j in nb) + sum(b[j] * Q(5 - C.al[v][j], 5) for j in nb)
        for p in pairs:
            lo, hi = pbounds(C, v, p[0], p[1])
            base = 1 - Q(C.al[v][p[0]] + C.al[v][p[1]], 5)
            obj += -u[p] * (base + hi) + l[p] * (base + lo)
        if obj < 1:
            return False
    return True


def invariant_order(C, stab_fixed):
    inv = []
    for x in range(NV):
        inv.append((C.st(x), tuple(sorted(C.al[x][y] for y in range(NV) if y != x))))
    return inv


def canon_lex(al, t, stab):
    """Lexicographic-min code (LEX edge order) over stabiliser permutations that preserve the
    sorted-star invariant; the invariant pruning keeps the result a canonical form."""
    C = Cfg(al, t)
    inv = invariant_order(C, None)
    best = None
    for p in stab:
        # p maps old vertex x -> new position p[x]; require invariants non-decreasing in new positions
        newinv = [None] * NV
        for x in range(NV):
            newinv[p[x]] = inv[x]
        if any(newinv[i] > newinv[i + 1] for i in range(NV - 1)):
            continue
        q = [0] * NV
        for x in range(NV):
            q[p[x]] = x
        code = tuple(al[q[i]][q[j]] for i, j in LEX)
        if best is None or code < best:
            best = code
    return best


def main():
    eng, out = sys.argv[1], sys.argv[2]
    os.makedirs(out, exist_ok=False)
    t0 = time.time()
    with open(os.path.abspath(__file__), "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    with open(os.path.join(eng, "run.json")) as f:
        erun = json.load(f)
    with open(os.path.join(eng, "rlp_duals.json")) as f:
        duals = json.load(f)
    with gzip.open(os.path.join(eng, "orbits.jsonl.gz"), "rt") as f:
        elines = [json.loads(x) for x in f if x.strip()]
    types = types_from_first_principles()
    report = {"checker": "core56_checkB_v2", "sha256": sha, "engine_dir": eng, "types": [list(t) for t in types], "by_type": {}}
    tri_last = {}
    for tri in itertools.combinations(range(NV), 3):
        last = max(LEX.index((tri[0], tri[1])), LEX.index((tri[0], tri[2])), LEX.index((tri[1], tri[2])))
        tri_last.setdefault(last, []).append(tri)
    allfail = []
    total_surv = 0
    for t in types:
        tt = time.time()
        stab = stabiliser(t)
        al = [[0] * NV for _ in range(NV)]
        leafcodes = []
        orbs = set()

        def rec(pos):
            if pos == len(LEX):
                leafcodes.append("".join(str(al[i][j]) for i, j in ENG))
                orbs.add(canon_lex(al, t, stab))
                return
            i, j = LEX[pos]
            for x in (1, 2, 3, 4):
                al[i][j] = al[j][i] = x
                C = Cfg(al, t)
                if all(C.tmin(*tr) <= C.tmax(*tr) for tr in tri_last.get(pos, [])):
                    rec(pos + 1)
            al[i][j] = al[j][i] = 0
        rec(0)
        leafcodes.sort()
        lh = hashlib.sha256(("\n".join(leafcodes) + "\n").encode()).hexdigest()
        es = erun["summary"].get(str(tuple(t)), {})
        mine = [e for e in elines if tuple(e["type"]) == tuple(t)]
        # map engine representatives to my canonical forms
        emapped = set()
        fails = []
        rules = {}
        for e in mine:
            rep = e["rep"]
            A = [[0] * NV for _ in range(NV)]
            for (i, j), ch in zip(ENG, rep):
                A[i][j] = A[j][i] = int(ch)
            C = Cfg(A, t)
            if not all(C.tmin(*tr) <= C.tmax(*tr) for tr in itertools.combinations(range(NV), 3)):
                fails.append(("rep_not_T_consistent", rep))
            emapped.add(canon_lex(A, t, stab))
            r = e["rule"]
            rules[r] = rules.get(r, 0) + 1
            w = e.get("witness")
            ok = False
            if r == "K":
                ok = check_K(C, w[0], w[1])
            elif r == "RLP":
                ok = check_RLP(C, w[0], duals)
            elif r in ("PB", "Ppair"):
                ok = check_P(C, w[0], r, w[1])
            elif r == "FH5":
                ok = check_FH5(C, w[0])
            elif r == "N26":
                ok = check_N26(C, w[0])
            elif r == "RPLP":
                ok = check_RPLP(C, w[0], w[1], duals)
            elif r == "SURVIVE":
                total_surv += 1
                ok = True
            if not ok:
                fails.append((r, rep))
        rep_t = {"my_leaves": len(leafcodes), "engine_leaves": es.get("leaves_labelled"),
                 "leafhash_match": lh == es.get("leafcodes_sha256"), "my_orbits": len(orbs),
                 "engine_orbit_lines": len(mine), "orbit_sets_equal": emapped == orbs and len(mine) == len(orbs),
                 "engine_rules": rules, "certificate_failures": fails[:20], "n_failures": len(fails),
                 "seconds": round(time.time() - tt, 1)}
        report["by_type"][str(tuple(t))] = rep_t
        allfail += fails
        print(t, rep_t, flush=True)
    report["total_certificate_failures"] = len(allfail)
    report["total_survivors_in_engine_list"] = total_surv
    report["seconds"] = round(time.time() - t0, 1)
    with open(os.path.join(out, "summary.json"), "x") as f:
        json.dump(report, f, indent=1)
    print(json.dumps({"failures": len(allfail), "survivors": total_surv, "seconds": report["seconds"]}))


if __name__ == "__main__":
    main()
