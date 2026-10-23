#!/usr/bin/env python3
"""core56_engine_v1 -- frozen pattern engine for rules-k6-v1.md (lane sun-coset6).

Standard library only, deterministic, single process.
  python3 core56_engine_v1.py MODE OUTDIR
MODE = core56  : Core5(6) (d=5, k=6, alpha in 1..4), rules T,K,RLP,P,FH5
MODE = core45  : control Core(5) (d=4, k=5, alpha in 1..3), rules T,K,RLP,P; full enumeration (no T pruning)
MODE = core34  : control Core_3(4) (d=3, k=4, alpha in 1..2), rules T,K,RLP,P; full enumeration
Outputs (exclusive create): run.json, orbits.tsv.gz (one line per canonical leaf orbit: type, code, rule,
witness), survivors.json, forbidden_triangles.json (T-forbidden triangle types met while pruning).
"""
import gzip
import hashlib
import itertools
import json
import os
import platform
import sys
import time
from fractions import Fraction as F
from math import gcd

BIG = 50


def lcm(a, b):
    return a * b // gcd(a, b)


def vp(n, p):
    c = 0
    while n % p == 0:
        n //= p
        c += 1
    return c


class Shape:
    def __init__(self, mode):
        self.mode = mode
        if mode == "core56":
            self.d, self.k, self.amax = 5, 6, 4
            self.e2classes = (1, 2)
            self.use_fh5 = True
            self.prune = True
        elif mode == "core45":
            self.d, self.k, self.amax = 4, 5, 3
            self.e2classes = (2,)  # E2 with unbounded v2 (k=5 model has no class split)
            self.use_fh5 = False
            self.prune = False
        elif mode == "core34":
            self.d, self.k, self.amax = 3, 4, 2
            self.e2classes = (2,)
            self.use_fh5 = False
            self.prune = False
        else:
            raise ValueError(mode)
        k = self.k
        self.V = list(range(k))
        self.E = sorted(itertools.combinations(range(k), 2), key=lambda e: (e[1], e[0]))
        self.EI = {e: i for i, e in enumerate(self.E)}
        self.tri_at = {}
        for t, (i, j) in enumerate(self.E):
            self.tri_at[t] = [(a, i, j) for a in range(k) if a < j and a != i
                              and self.EI[tuple(sorted((a, i)))] < t and self.EI[tuple(sorted((a, j)))] < t]
        # special placement types: (e2 vertex or None, e2 class, e3 vertex or None)
        types = [(None, 0, None), (None, 0, 0)]
        for c in self.e2classes:
            types += [(0, c, None), (0, c, 0), (0, c, 1)]
        self.types = types


def gcd_alpha_r(alpha, z, sp):
    """gcd(alpha, r_z) from special status (rules-k6-v1 L1 table)."""
    e2, c2, e3 = sp
    if alpha == 1:
        return 1
    if alpha == 2:
        return 2 if z == e2 else 1
    if alpha == 3:
        return 3 if z == e3 else 1
    if alpha == 4:
        if z == e2:
            return 4 if c2 == 2 else 2
        return 1
    raise ValueError(alpha)


def taumin(A, a, b, c, sp):
    t = 1
    for x, y, z in ((a, b, c), (a, c, b), (b, c, a)):
        al = A[x][y]
        t = lcm(t, al // gcd_alpha_r(al, z, sp))
    return t


def taumax(A, a, b, c):
    x, y, z = A[a][b], A[a][c], A[b][c]
    return min(x * y, x * z, y * z)


def status(v, sp):
    e2, c2, e3 = sp
    return ((c2 if v == e2 else 0), (1 if v == e3 else 0))


# ------------------------------------------------------------------ rules
def rule_K(S, A, sp):
    k, d = S.k, S.d
    for v in range(k):
        oth = [w for w in range(k) if w != v]
        for r in range(2, len(oth) + 1):
            for T in itertools.combinations(oth, r):
                if sum(A[i][v] for i in T) >= d and all(taumin(A, i, v, j, sp) == A[i][v] * A[v][j]
                                                        for i, j in itertools.combinations(T, 2)):
                    return ("K", v, list(T))
    return None


def simplex_packing(sets, c):
    """max sum c_j y_j s.t. sum_{j in S} y_j <= 1 (S in sets), y >= 0; exact, Bland's rule."""
    n, m = len(c), len(sets)
    Tb = [[F(1 if j in S else 0) for j in range(n)] + [F(1 if r == i else 0) for r in range(m)] + [F(1)]
          for i, S in enumerate(sets)]
    obj = [-F(x) for x in c] + [F(0)] * m + [F(0)]
    basis = [n + i for i in range(m)]
    while True:
        enter = next((j for j in range(n + m) if obj[j] < 0), None)
        if enter is None:
            return obj[-1]
        leave = None
        best = None
        for i in range(m):
            if Tb[i][enter] > 0:
                ratio = Tb[i][-1] / Tb[i][enter]
                if best is None or ratio < best or (ratio == best and basis[i] < basis[leave]):
                    best, leave = ratio, i
        pv = Tb[leave][enter]
        Tb[leave] = [x / pv for x in Tb[leave]]
        for i in range(m):
            if i != leave and Tb[i][enter] != 0:
                f = Tb[i][enter]
                Tb[i] = [a - f * b for a, b in zip(Tb[i], Tb[leave])]
        f = obj[enter]
        obj = [a - f * b for a, b in zip(obj, Tb[leave])]
        basis[leave] = enter


_LP = {}


def lp_min(qs, stats, d):
    key = (qs, stats, d)
    if key in _LP:
        return _LP[key]
    n = len(qs)
    vals = []
    for x in range(n):
        a = vp(qs[x], 2) + (0 if stats[x][0] == 0 else (1 if stats[x][0] == 1 else BIG))
        b = vp(qs[x], 3) + (BIG if stats[x][1] else 0)
        vals.append((a, b))

    def mg(x, y):
        return 2 ** min(vals[x][0], vals[y][0]) * 3 ** min(vals[x][1], vals[y][1])
    allowed = []
    for r in range(1, n + 1):
        for T in itertools.combinations(range(n), r):
            if r == 1 or (all(mg(x, y) >= 2 for x, y in itertools.combinations(T, 2))
                          and any(mg(x, y) >= r for x, y in itertools.combinations(T, 2))):
                allowed.append(frozenset(T))
    maximal = [T for T in allowed if not any(T < U for U in allowed)]
    res = simplex_packing(maximal, [F(q, d) for q in qs])
    _LP[key] = res
    return res


def rule_RLP(S, A, sp):
    k, d = S.k, S.d
    for v in range(k):
        oth = [w for w in range(k) if w != v]
        stats = tuple(status(j, sp) for j in oth)
        dead = True
        for q in itertools.product(*[range(1, d - A[v][j] + 1) for j in oth]):
            if lp_min(tuple(q), stats, d) < 1:
                dead = False
                break
        if dead:
            return ("RLP", v)
    return None


def rule_P(S, A, sp):
    k, d = S.k, S.d
    for v in range(k):
        oth = [w for w in range(k) if w != v]
        X = {j: F(A[v][j], d) for j in oth}
        his = {}
        for j, kk in itertools.combinations(oth, 2):
            a = A[j][kk]
            u = F(1, d * gcd_alpha_r(a, v, sp))
            lo = max(F(taumin(A, v, j, kk, sp), d * a), X[j] + X[kk] - 1, F(0))
            q = lo / u
            lo = (-((-q.numerator) // q.denominator)) * u
            m = min(X[j], X[kk])
            q = m / u
            hi = (q.numerator // q.denominator) * u
            if hi == m:
                def k2(v_, j_, k_):
                    return A[v_][j_] + A[k_][j_] <= d - 1
                if X[j] < X[kk]:
                    ok = k2(v, j, kk)
                elif X[kk] < X[j]:
                    ok = k2(v, kk, j)
                else:
                    ok = k2(v, j, kk) and k2(v, kk, j)
                if not ok:
                    hi -= u
            if lo > hi:
                return ("Ppair", v, [j, kk])
            his[(j, kk)] = hi
        for r in range(2, len(oth) + 1):
            for T in itertools.combinations(oth, r):
                tot = sum(1 - X[j] for j in T) - sum(1 - X[j] - X[kk] + his[(j, kk)] for j, kk in itertools.combinations(T, 2))
                if tot >= 1:
                    return ("PB", v, list(T))
    return None


def fibre_vals(l, t, sp, e5):
    e2, c2, e3 = sp
    a, b, c = vp(t, 2), vp(t, 3), vp(t, 5)
    if l == e2:
        a += 1 if c2 == 1 else BIG
    if l == e3:
        b += BIG
    if l == e5:
        c += BIG
    return a, b, c


def fibre5_feasible(S, A, sp, e5, inside, fixed):
    k, m = S.k, 5
    opts = []
    for l in range(k):
        if l in inside:
            ts = [1]
        elif l in fixed:
            ts = [fixed[l]]
        else:
            ts = range(1, m + 1)
        o = [(t, M) for t in ts for M in itertools.combinations(range(m), t)]
        if l == inside[0]:
            o = [(1, (0,))]
        opts.append(o)
    for combo in itertools.product(*opts):
        t = [c[0] for c in combo]
        bad = False
        for i in range(k):
            if t[i] == 1:
                for l in range(k):
                    if l != i and A[i][l] > t[l]:
                        bad = True
                        break
            if bad:
                break
        if bad:
            continue
        Vv = [fibre_vals(l, t[l], sp, e5) for l in range(k)]
        for c in range(m):
            Sc = [l for l in range(k) if c in combo[l][1]]
            s = len(Sc)
            if s >= 2 and not any(2 ** min(Vv[x][0], Vv[y][0]) * 3 ** min(Vv[x][1], Vv[y][1]) * 5 ** min(Vv[x][2], Vv[y][2]) >= s
                                  for x, y in itertools.combinations(Sc, 2)):
                bad = True
                break
        if not bad:
            return True
    return False


def rule_FH5(S, A, sp):
    k = S.k
    for a, b in itertools.combinations(range(k), 2):
        if A[a][b] != 1:
            continue
        Vs = {v: A[v][a] for v in range(k) if v not in (a, b) and A[v][a] == A[v][b]}
        if not Vs:
            continue
        inside = [a, b] + sorted(v for v, c in Vs.items() if c == 1)
        fixed = {v: c for v, c in Vs.items() if c > 1}
        if all(not fibre5_feasible(S, A, sp, e5, inside, fixed) for e5 in [None] + list(range(k))):
            return ("FH5", [a, b], sorted(Vs))
    return None


# ------------------------------------------------------------- canonical form
def canon(S, A, sp):
    """Canonical code under the stabiliser of the special placement (refinement + permutations)."""
    k = S.k
    col = []
    for v in range(k):
        col.append((status(v, sp), tuple(sorted(A[v][w] for w in range(k) if w != v))))
    for _ in range(3):
        col = [(col[v], tuple(sorted((A[v][w], col[w]) for w in range(k) if w != v))) for v in range(k)]
    classes = {}
    for v in range(k):
        classes.setdefault(col[v], []).append(v)
    order = sorted(classes)
    best = None
    for parts in itertools.product(*[itertools.permutations(classes[c]) for c in order]):
        seq = [v for part in parts for v in part]  # seq[newpos] = old vertex
        key = tuple(A[seq[i]][seq[j]] for i, j in S.E)
        if best is None or key < best:
            best = key
    return best


# ------------------------------------------------------------------ enumerate
def run(mode, outdir):
    S = Shape(mode)
    os.makedirs(outdir, exist_ok=False)
    t0 = time.time()
    with open(os.path.abspath(__file__), "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    k = S.k
    rules = [("K", rule_K), ("RLP", rule_RLP), ("P", rule_P)] + ([("FH5", rule_FH5)] if S.use_fh5 else [])
    lines = []
    survivors = []
    forb = {}
    summary = {}
    for sp in S.types:
        tt = time.time()
        A = [[0] * k for _ in range(k)]
        seen = {}
        nleaf = 0
        npruned = 0

        def rec(t):
            nonlocal nleaf, npruned
            if t == len(S.E):
                nleaf += 1
                c = canon(S, A, sp)
                if c not in seen:
                    seen[c] = [row[:] for row in A]
                return
            i, j = S.E[t]
            for al in range(1, S.amax + 1):
                A[i][j] = A[j][i] = al
                ok = True
                if S.prune:
                    for (a, b, c) in S.tri_at[t]:
                        tm, tM = taumin(A, a, b, c, sp), taumax(A, a, b, c)
                        if tm > tM:
                            key = (tuple(sorted([A[a][b], A[a][c], A[b][c]])), "%d-%d-%d" % (a, b, c), str(sp), tm, tM)
                            forb[str(key)] = forb.get(str(key), 0) + 1
                            ok = False
                            break
                if ok:
                    rec(t + 1)
                else:
                    npruned += 1
            A[i][j] = A[j][i] = 0
        rec(0)
        counts = {}
        for c, M in sorted(seen.items()):
            w = None
            if not S.prune:
                for tri in itertools.combinations(range(k), 3):
                    tm, tM = taumin(M, *tri, sp), taumax(M, *tri)
                    if tm > tM:
                        w = ("T", list(tri), tm, tM)
                        break
            if w is None:
                for name, f in rules:
                    w = f(S, M, sp)
                    if w is not None:
                        break
            code = "".join(map(str, c))
            if w is None:
                counts["SURVIVE"] = counts.get("SURVIVE", 0) + 1
                survivors.append({"type": list(sp), "code": code,
                                  "alpha": {"%d%d" % (i, j): M[i][j] for i, j in S.E}})
                lines.append("%s\t%s\tSURVIVE\t-" % (json.dumps(list(sp)), code))
            else:
                counts[w[0]] = counts.get(w[0], 0) + 1
                lines.append("%s\t%s\t%s\t%s" % (json.dumps(list(sp)), code, w[0], json.dumps(list(w[1:]), separators=(",", ":"))))
        summary[str(sp)] = {"leaves_labelled": nleaf, "pruned_nodes": npruned, "orbits": len(seen),
                            "orbit_rule_counts": counts, "seconds": round(time.time() - tt, 1)}
        print(mode, sp, summary[str(sp)], flush=True)
    blob = ("\n".join(lines) + "\n").encode()
    with open(os.path.join(outdir, "orbits.tsv.gz"), "xb") as f:
        f.write(gzip.compress(blob, mtime=0))
    with open(os.path.join(outdir, "survivors.json"), "x") as f:
        json.dump(survivors, f, indent=1)
    with open(os.path.join(outdir, "forbidden_triangles.json"), "x") as f:
        json.dump(forb, f, indent=1, sort_keys=True)
    runrec = {"engine": "core56_engine_v1", "sha256": sha, "mode": mode, "python": sys.version,
              "platform": platform.platform(), "types": [list(t) for t in S.types], "summary": summary,
              "total_orbits": sum(v["orbits"] for v in summary.values()),
              "total_survivors": len(survivors), "orbits_tsv_sha256_uncompressed": hashlib.sha256(blob).hexdigest(),
              "lp_cache_entries": len(_LP), "seconds": round(time.time() - t0, 1)}
    with open(os.path.join(outdir, "run.json"), "x") as f:
        json.dump(runrec, f, indent=1)
    print(json.dumps({"mode": mode, "total_orbits": runrec["total_orbits"], "survivors": len(survivors),
                      "seconds": runrec["seconds"]}))


if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2])
