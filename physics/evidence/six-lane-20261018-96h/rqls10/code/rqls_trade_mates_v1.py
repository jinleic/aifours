#!/usr/bin/env python3
"""rqls_trade_mates_v1: EXACT stdlib probe (integers and fractions.Fraction only): do OTHER classical OLS(10) offer
richer exact trades (evidence/exact-trades-lemma-v1.md, Lemma T2) than the Parker points?

For each resolution square S in {Parker A, Parker B_0..B_4, the A and B squares of the first 3 Z_9+1 pairs}:
enumerate transversals (row-by-row backtracking, cap 300,000), then orthogonal mates M (10 disjoint transversals;
Knuth's Algorithm X on the 100 cells, cap 300 mates and 12 s per square, transversal order = enumeration order). For
every mate: pair graphs G_(a,b) of (M, S) and sigma = sum (c_(a,b) - 1). For the 4 mates with the largest sigma: the
exact trade beam search of rqls_exact_trades_v2 (moves, apply, verify unchanged in logic: all planes spanned by two
vectors on a common line, admissible components, gauge moves skipped, rotation [[3/5,-4/5],[4/5,3/5]]; width 12,
depth 6) with exact verification (Gram = I on all 30 lines) of the best state and exact distinct-ray counts.
Budget 270 s; output JSON (exclusive).
Usage: rqls_trade_mates_v1.py PARKER_JSON PARKER_SHA Z9_JSON Z9_SHA OUT.json
"""
import hashlib, json, sys, time
from fractions import Fraction as Fr

T0 = time.monotonic()
BUDGET = 270.0
pk_raw, z9_raw = open(sys.argv[1], "rb").read(), open(sys.argv[3], "rb").read()
if hashlib.sha256(pk_raw).hexdigest() != sys.argv[2] or hashlib.sha256(z9_raw).hexdigest() != sys.argv[4]:
    sys.exit(9)
parker, z9 = json.loads(pk_raw), json.loads(z9_raw)
OUT = sys.argv[5]
N = 10
ZERO, ONE = Fr(0), Fr(1)
RC, RS = Fr(3, 5), Fr(4, 5)


def z9_array(d_inf, beta, gamma, delta):
    X = [[None] * 10 for _ in range(10)]
    for i in range(9):
        for d in range(9):
            X[i][(i + d) % 9] = 9 if d == d_inf else (i + beta[d]) % 9
    for j in range(9):
        X[9][j] = (j + gamma) % 9
    for i in range(9):
        X[i][9] = (i + delta) % 9
    X[9][9] = 9
    return X


def latin(X):
    f = list(range(N))
    return all(sorted(r) == f for r in X) and all(sorted(X[i][j] for i in range(N)) == f for j in range(N))


def lines_of(R):
    return ([[N * i + j for j in range(N)] for i in range(N)] + [[N * i + j for i in range(N)] for j in range(N)]
            + [[N * i + j for i in range(N) for j in range(N) if R[i][j] == s] for s in range(N)])


SQUARES = [("parkerA", parker["pairs"][0]["A_array"])]
for k, h in enumerate(parker["pairs"]):
    SQUARES.append(("parkerB%d" % k, h["B_array"]))
for k, h in enumerate(z9["first_hits"][:3]):
    bA = {int(x): int(y) for x, y in h["betaA"].items()}
    bB = {int(x): int(y) for x, y in h["betaB"].items()}
    SQUARES.append(("z9A%d" % k, z9_array(0, bA, int(h["gammaA"]), int(h["deltaA"]))))
    SQUARES.append(("z9B%d" % k, z9_array(int(h["e"]), bB, int(h["gammaB"]), int(h["deltaB"]))))


def transversals(S, cap):
    out, cols, used = [], [None] * N, [False] * N
    syms = set()

    def rec(i):
        if len(out) >= cap or (i < 4 and time.monotonic() - T0 > BUDGET - 100):
            return
        if i == N:
            out.append(tuple(N * r + cols[r] for r in range(N)))
            return
        for j in range(N):
            if not used[j] and S[i][j] not in syms:
                used[j] = True
                syms.add(S[i][j])
                cols[i] = j
                rec(i + 1)
                used[j] = False
                syms.discard(S[i][j])
    rec(0)
    return out


def mates(trs, cap, tmax):
    X = {c: set() for c in range(100)}
    for t, cells in enumerate(trs):
        for c in cells:
            X[c].add(t)
    Y = {t: cells for t, cells in enumerate(trs)}
    sols, sol, t0, stop = [], [], time.monotonic(), [False]

    def select(r):
        cols = []
        for j in Y[r]:
            for i in X[j]:
                for k in Y[i]:
                    if k != j:
                        X[k].discard(i)
            cols.append(X.pop(j))
        return cols

    def deselect(r, cols):
        for j in reversed(Y[r]):
            X[j] = cols.pop()
            for i in X[j]:
                for k in Y[i]:
                    if k != j:
                        X[k].add(i)

    def solve():
        if stop[0]:
            return
        if not X:
            sols.append(list(sol))
            if len(sols) >= cap:
                stop[0] = True
            return
        if time.monotonic() - t0 > tmax or time.monotonic() - T0 > BUDGET - 120:
            stop[0] = True
            return
        c = min(X, key=lambda cc: len(X[cc]))
        for r in sorted(X[c]):
            sol.append(r)
            cols = select(r)
            solve()
            deselect(r, cols)
            sol.pop()
            if stop[0]:
                return
    solve()
    return sols, stop[0]


class UF:
    def __init__(self, items):
        self.p = {x: x for x in items}

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        self.p[self.find(a)] = self.find(b)

    def groups(self):
        g = {}
        for x in self.p:
            g.setdefault(self.find(x), []).append(x)
        return sorted((sorted(v) for v in g.values()), key=lambda c: (len(c), c))


def sigma(Q, R):
    L = lines_of(R)
    tot, disc = 0, []
    for a in range(N):
        for b in range(a + 1, N):
            cells = [p for p in range(100) if Q[p // N][p % N] in (a, b)]
            uf = UF(cells)
            for line in L:
                S = [p for p in line if Q[p // N][p % N] in (a, b)]
                uf.union(S[0], S[1])
            g = uf.groups()
            if len(g) > 1:
                disc.append([a, b] + [len(x) for x in g])
            tot += len(g) - 1
    return tot, disc


def dot(u, v):
    s = ZERO
    for x, y in zip(u, v):
        if x and y:
            s += x * y
    return s


def canon(v):
    for x in v:
        if x:
            return tuple(v) if x > 0 else tuple(-y for y in v)
    raise ValueError("zero vector")


def nrays(cfg):
    return len({canon(v) for v in cfg})


def verify(cfg, lines):
    bad = 0
    for line in lines:
        for x in range(len(line)):
            for y in range(x, len(line)):
                if dot(cfg[line[x]], cfg[line[y]]) != (ONE if x == y else ZERO):
                    bad += 1
    return bad


def moves(cfg, lines):
    cano = [canon(v) for v in cfg]
    rid, reps = {}, []
    for c in cano:
        if c not in rid:
            rid[c] = len(reps)
            reps.append(c)
    cell_ray = [rid[c] for c in cano]
    planes = {}
    for line in lines:
        for x in range(len(line)):
            for y in range(x + 1, len(line)):
                r1, r2 = cell_ray[line[x]], cell_ray[line[y]]
                key = (min(r1, r2), max(r1, r2))
                if key not in planes:
                    planes[key] = (cfg[line[x]], cfg[line[y]])
    out, seenW = [], set()
    for key in sorted(planes):
        v, w = planes[key]
        inW = frozenset(r for r, u in enumerate(reps) if dot(u, v) ** 2 + dot(u, w) ** 2 == ONE)
        if inW in seenW:
            continue
        seenW.add(inW)
        S = [p for p in range(100) if cell_ray[p] in inW]
        Sset = set(S)
        uf = UF(S)
        blocked = set()
        for line in lines:
            T = [p for p in line if p in Sset]
            if len(T) == 2:
                uf.union(T[0], T[1])
            elif len(T) == 1:
                blocked.add(T[0])
        perp_all = all(dot(u, v) == ZERO and dot(u, w) == ZERO for r, u in enumerate(reps) if r not in inW)
        for C in uf.groups():
            if any(p in blocked for p in C):
                continue
            if len(C) == len(S) and perp_all:
                continue
            out.append({"v": v, "w": w, "C": tuple(C)})
    return out


def apply(cfg, mv):
    v, w = mv["v"], mv["w"]
    new = list(cfg)
    for p in mv["C"]:
        x, y = dot(cfg[p], v), dot(cfg[p], w)
        x2, y2 = RC * x - RS * y, RS * x + RC * y
        new[p] = tuple(x2 * a + y2 * b for a, b in zip(v, w))
    return new


def key_of(cfg):
    return tuple(canon(v) for v in cfg)


def beam(Q, R, width=12, depth=6):
    L = lines_of(R)
    cfg0 = [tuple(ONE if k == Q[p // N][p % N] else ZERO for k in range(N)) for p in range(100)]
    rec = {"classical_bad": verify(cfg0, L), "classical_rays": nrays(cfg0), "classical_moves": len(moves(cfg0, L))}
    bm, seen, best, by_depth = [(cfg0, [])], {key_of(cfg0)}, (nrays(cfg0), cfg0, []), []
    status = "COMPLETED"
    for dpt in range(depth):
        if time.monotonic() - T0 > BUDGET:
            status = "BUDGET_AT_DEPTH_%d" % dpt
            break
        cand = []
        for cfg, hist in bm:
            for m in moves(cfg, L):
                c2 = apply(cfg, m)
                k2 = key_of(c2)
                if k2 in seen:
                    continue
                seen.add(k2)
                cand.append((nrays(c2), c2, hist + [len(m["C"])]))
        if not cand:
            status = "NO_NEW_STATES_AT_DEPTH_%d" % dpt
            break
        cand.sort(key=lambda t: (-t[0], len(t[2]), str(t[2])))
        bm = [(c, h) for (_, c, h) in cand[:width]]
        by_depth.append(cand[0][0])
        if cand[0][0] > best[0]:
            best = cand[0]
    rec.update({"status": status, "best_rays": best[0], "best_rays_by_depth": by_depth, "best_history_sizes": best[2],
                "best_bad": verify(best[1], L), "states_seen": len(seen)})
    return rec


squares_out, all_mates = [], []
for name, S in SQUARES:
    if time.monotonic() - T0 > BUDGET - 120:
        squares_out.append({"square": name, "status": "SKIPPED_BUDGET"})
        continue
    t1 = time.monotonic()
    trs = transversals(S, 300000)
    t2 = time.monotonic()
    sols, stopped = mates(trs, 300, 12.0)
    t3 = time.monotonic()
    sig = []
    for sol in sols:
        M = [[None] * N for _ in range(N)]
        for sym, t in enumerate(sol):
            for c in trs[t]:
                M[c // N][c % N] = sym
        ok = latin(M) and len({(M[i][j], S[i][j]) for i in range(N) for j in range(N)}) == 100
        s, disc = sigma(M, S)
        sig.append(s)
        all_mates.append((s, name, M, ok, disc))
    hist = {}
    for s in sig:
        hist[str(s)] = hist.get(str(s), 0) + 1
    squares_out.append({"square": name, "latin": latin(S), "transversals": len(trs), "transversal_cap_hit": len(trs) >= 300000,
                        "mates_found": len(sols), "mate_search_stopped_by_cap_or_time": stopped,
                        "sigma_histogram": hist, "secs_transversals": round(t2 - t1, 2), "secs_mates": round(t3 - t2, 2)})

all_mates.sort(key=lambda t: (-t[0], t[1]))
top = []
for s, name, M, ok, disc in all_mates[:4]:
    if time.monotonic() - T0 > BUDGET - 20:
        top.append({"square": name, "sigma": s, "status": "SKIPPED_BUDGET"})
        continue
    S = dict(SQUARES)[name]
    rec = beam(M, S)
    rec.update({"resolution_square": name, "sigma": s, "orthogonal_mate_ok": ok, "disconnected_pairs": disc, "mate": M})
    top.append(rec)
out = {"probe": "rqls_trade_mates_v1", "arithmetic": "integers + fractions.Fraction (exact)", "squares": squares_out,
       "mates_total": len(all_mates), "max_sigma": all_mates[0][0] if all_mates else None, "top_trade_searches": top,
       "elapsed_s": round(time.monotonic() - T0, 3)}
with open(OUT, "x", encoding="utf-8") as fh:
    json.dump(out, fh, indent=1)
print(json.dumps({"squares": [(q["square"], q.get("transversals"), q.get("mates_found"), q.get("sigma_histogram"))
                              for q in squares_out],
                  "mates_total": out["mates_total"], "max_sigma": out["max_sigma"],
                  "top": [(t.get("resolution_square"), t.get("sigma"), t.get("best_rays"), t.get("best_bad"), t.get("status"),
                           t.get("best_rays_by_depth")) for t in top], "elapsed_s": out["elapsed_s"]}))
