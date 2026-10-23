#!/usr/bin/env python3
"""rqls_exact_trades_v2: EXACT stdlib probe (fractions.Fraction only, no floats in any decision) of 2-dimensional
"trades" in classical 1-RQLS(10) (lane note evidence/exact-trades-lemma-v1.md).
v2 = v1 (sha256 4f8347e9...2967) plus: Part 1b (Parker pairs, both roles): for every permutation pi of the three corner
symbols, the "crossed mate" A_pi (A with its corner subsquare relabelled by pi) - its orthogonality to the resolution
and its pair graphs G_(a,s) with a finite; a disconnected one would allow trades that move finite-symbol cells in a
state where a block-F ray coincides with a different-symbol block-C ray. Part 2 beam enlarged (width 12, depth 6) and
run also from the classical configuration of every crossed mate. Everything else unchanged.

Trade lemma (proved in the note): if every line (row, column, resolution class) meeting a cell set C meets S_W = {p :
q_p in W} (W a 2-dimensional subspace) in exactly two cells whose vectors form an orthonormal basis of W, and C is a
union of connected components of the graph "two W-cells joined when they share a line", then rotating the vectors of
C by any unitary of W keeps every line an orthonormal basis. Here the rotation is the fixed rational orthogonal
R = [[3/5, -4/5], [4/5, 3/5]] in the line-supplied basis (v, w) of W, so every vector stays rational and every check
is exact.

Part 1 (all 5 Parker Z_7+3 pairs and all 20 Z_9+1 pairs of the lane, both roles: vectors from A with resolution B,
and the reverse): connected components of every pair graph G_(a,b) (the 20 cells with symbols a, b; one edge per line);
c_(a,b), sum (c - 1) and the unsymmetric first-order excess 2 sum (c - 1) of evidence/classical-tangent-theory-v1.md.
Part 2 (Parker pairs, both roles): the classical configuration and ONE trade (smallest non-gauge component at the
classical point), each with exact full verification (Gram = I on all 30 lines) and exact distinct-ray count (real
rational unit vectors, parallel iff equal up to sign). Commuting check: two trades on disjoint cell sets applied in
both orders. Search: general move generation at every state (every plane spanned by two vectors sharing a line;
valid components = no cell on a line meeting S_W only once; gauge moves = whole S_W with every other ray orthogonal
to W, skipped), beam search (width 6, depth 5) maximising the distinct-ray count; flag any move containing a cell
whose classical symbol is finite (0..6). The best state of each run is replayed from the classical start and verified
exactly. Budget 270 s (checked between units); output JSON (exclusive).
Usage: rqls_exact_trades_v2.py PARKER_JSON PARKER_SHA Z9_JSON Z9_SHA OUT.json
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


def over():
    return time.monotonic() - T0 > BUDGET


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
    rows = [[N * i + j for j in range(N)] for i in range(N)]
    cols = [[N * i + j for i in range(N)] for j in range(N)]
    cls = [[N * i + j for i in range(N) for j in range(N) if R[i][j] == s] for s in range(N)]
    return rows + cols + cls


PAIRS = []
for k, h in enumerate(parker["pairs"]):
    PAIRS.append(("parker%d" % k, h["A_array"], h["B_array"]))
for k, h in enumerate(z9["first_hits"]):
    bA = {int(x): int(y) for x, y in h["betaA"].items()}
    bB = {int(x): int(y) for x, y in h["betaB"].items()}
    PAIRS.append(("z9p1_%d" % k, z9_array(0, bA, int(h["gammaA"]), int(h["deltaA"])),
                  z9_array(int(h["e"]), bB, int(h["gammaB"]), int(h["deltaB"]))))


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


# ------------------------------------------------------------------ part 1: pair-graph components
part1 = []
for name, A, B in PAIRS:
    orth = latin(A) and latin(B) and len({(A[i][j], B[i][j]) for i in range(N) for j in range(N)}) == 100
    for role, Q, R in (("QA_resB", A, B), ("QB_resA", B, A)):
        L = lines_of(R)
        disc, sumc1 = [], 0
        for a in range(N):
            for b in range(a + 1, N):
                cells = [p for p in range(100) if Q[p // N][p % N] in (a, b)]
                uf = UF(cells)
                ok = True
                for line in L:
                    S = [p for p in line if Q[p // N][p % N] in (a, b)]
                    if len(S) != 2:
                        ok = False
                        break
                    uf.union(S[0], S[1])
                comps = uf.groups()
                if not ok:
                    disc.append({"pair": [a, b], "error": "line without exactly one a- and one b-cell"})
                    continue
                if len(comps) > 1:
                    disc.append({"pair": [a, b], "component_sizes": [len(c) for c in comps]})
                sumc1 += len(comps) - 1
        part1.append({"pair": name, "role": role, "orthogonal_pair": orth, "disconnected": disc,
                      "sum_c_minus_1": sumc1, "unsym_excess_2sum": 2 * sumc1})


def pair_graph_summary(Q, R):
    L = lines_of(R)
    out = []
    for a in range(N):
        for b in range(a + 1, N):
            cells = [p for p in range(100) if Q[p // N][p % N] in (a, b)]
            uf = UF(cells)
            for line in L:
                S = [p for p in line if Q[p // N][p % N] in (a, b)]
                if len(S) != 2:
                    return None
                uf.union(S[0], S[1])
            out.append(((a, b), len(uf.groups())))
    return out


PERMS = [(7, 8, 9), (7, 9, 8), (8, 7, 9), (8, 9, 7), (9, 7, 8), (9, 8, 7)]


def crossed(Q, perm):
    mp = {7 + k: perm[k] for k in range(3)}
    return [[(mp[Q[i][j]] if (i >= 7 and j >= 7) else Q[i][j]) for j in range(N)] for i in range(N)]


part1b = []
for name, A, B in PAIRS[:5]:
    for role, Q, R in (("QA_resB", A, B), ("QB_resA", B, A)):
        for perm in PERMS:
            Qp = crossed(Q, perm)
            orth = latin(Qp) and len({(Qp[i][j], R[i][j]) for i in range(N) for j in range(N)}) == 100
            pg = pair_graph_summary(Qp, R) if orth else None
            fin_disc = [list(ab) + [c] for (ab, c) in (pg or []) if c > 1 and min(ab) < 7]
            inf_disc = [list(ab) + [c] for (ab, c) in (pg or []) if c > 1 and min(ab) >= 7]
            part1b.append({"pair": name, "role": role, "perm": list(perm), "orthogonal": orth,
                           "finite_pairs_disconnected": fin_disc, "inf_pairs_disconnected": inf_disc})

# ------------------------------------------------------------------ exact linear algebra on rational vectors
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
                g = dot(cfg[line[x]], cfg[line[y]])
                if g != (ONE if x == y else ZERO):
                    bad += 1
    return bad


def unit(s):
    return tuple(ONE if k == s else ZERO for k in range(N))


def moves(cfg, lines, Q):
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
            elif len(T) > 2:
                raise ValueError("three W-vectors on one line")
        perp_all = all(dot(u, v) == ZERO and dot(u, w) == ZERO for r, u in enumerate(reps) if r not in inW)
        for C in uf.groups():
            if any(p in blocked for p in C):
                continue
            if len(C) == len(S) and perp_all:
                continue                                  # global unitary on W: gauge
            out.append({"v": v, "w": w, "C": tuple(C), "finite_cells": sum(1 for p in C if Q[p // N][p % N] < 7),
                        "W_rays": len(inW), "W": tuple(sorted(reps[r] for r in inW))})
    return out


def apply(cfg, mv):
    v, w = mv["v"], mv["w"]
    new = list(cfg)
    for p in mv["C"]:
        q = cfg[p]
        x, y = dot(q, v), dot(q, w)
        x2, y2 = RC * x - RS * y, RS * x + RC * y
        new[p] = tuple(x2 * a + y2 * b for a, b in zip(v, w))
    return new


def key_of(cfg):
    return tuple(canon(v) for v in cfg)


def describe(cfg, Q):
    inf_F = {canon(cfg[p]) for p in range(100) if Q[p // N][p % N] >= 7 and not (p // N >= 7 and p % N >= 7)}
    inf_C = {canon(cfg[p]) for p in range(100) if Q[p // N][p % N] >= 7 and (p // N >= 7 and p % N >= 7)}
    fin = {canon(cfg[p]) for p in range(100) if Q[p // N][p % N] < 7}
    return {"rays_finite_symbol_cells": len(fin), "rays_inf_cells_outside_corner": len(inf_F),
            "rays_inf_corner_cells": len(inf_C), "inf_F_and_C_shared": len(inf_F & inf_C)}


# ------------------------------------------------------------------ parts 2-3: Parker pairs
part2 = []
STARTS = [(name, role, list(perm), crossed(Q0, perm), R) for name, A, B in PAIRS[:5]
          for role, Q0, R in (("QA_resB", A, B), ("QB_resA", B, A)) for perm in PERMS]
for name, role, perm, Q, R in STARTS:
    if True:
        if over():
            part2.append({"pair": name, "role": role, "perm": perm, "status": "SKIPPED_BUDGET"})
            continue
        L = lines_of(R)
        cfg0 = [unit(Q[p // N][p % N]) for p in range(100)]
        rec = {"pair": name, "role": role, "perm": perm, "classical_bad_gram_entries": verify(cfg0, L),
               "classical_rays": nrays(cfg0)}
        mv0 = moves(cfg0, L, Q)
        rec["classical_nongauge_moves"] = len(mv0)
        rec["classical_move_component_sizes"] = sorted(len(m["C"]) for m in mv0)
        rec["classical_moves_with_finite_cells"] = sum(1 for m in mv0 if m["finite_cells"])
        if mv0:
            one = min(mv0, key=lambda m: (len(m["C"]), m["C"]))
            cfg1 = apply(cfg0, one)
            rec["one_trade"] = {"component": list(one["C"]), "bad_gram_entries": verify(cfg1, L), "rays": nrays(cfg1),
                                "describe": describe(cfg1, Q)}
        else:
            rec["one_trade"] = None
        # commuting check: two moves on disjoint cell sets, in DIFFERENT planes, from the classical state
        comm = None
        for m1 in mv0:
            for m2 in mv0:
                if set(m1["C"]) & set(m2["C"]) or m1["W"] == m2["W"] or m1["C"] >= m2["C"]:
                    continue
                c12 = apply(apply(cfg0, m1), m2)
                c21 = apply(apply(cfg0, m2), m1)
                comm = {"sizes": [len(m1["C"]), len(m2["C"])], "orders_equal": key_of(c12) == key_of(c21),
                        "bad_gram_entries": verify(c12, L), "rays": nrays(c12), "describe": describe(c12, Q)}
                break
            if comm:
                break
        rec["commuting_pair"] = comm
        # beam search
        width, depth = 12, 6
        beam = [(cfg0, [])]
        seen = {key_of(cfg0)}
        best = (nrays(cfg0), cfg0, [])
        finite_moves, expanded, children = 0, 0, 0
        best_by_depth = []
        for dpt in range(depth):
            if over():
                rec["beam_status"] = "BUDGET_AT_DEPTH_%d" % dpt
                break
            cand = []
            for cfg, hist in beam:
                ms = moves(cfg, L, Q)
                expanded += 1
                for mi, m in enumerate(ms):
                    finite_moves += int(m["finite_cells"] > 0)
                    c2 = apply(cfg, m)
                    k2 = key_of(c2)
                    if k2 in seen:
                        continue
                    seen.add(k2)
                    children += 1
                    cand.append((nrays(c2), c2, hist + [(len(m["C"]), list(m["C"]), m["W_rays"])]))
            if not cand:
                rec["beam_status"] = "NO_NEW_STATES_AT_DEPTH_%d" % dpt
                break
            cand.sort(key=lambda t: (-t[0], len(t[2]), str(t[2])))
            beam = [(c, h) for (_, c, h) in cand[:width]]
            best_by_depth.append(cand[0][0])
            if cand[0][0] > best[0]:
                best = cand[0]
        else:
            rec["beam_status"] = "COMPLETED"
        hsets = [set(h[1]) for h in best[2]]
        overl = any(hsets[x] & hsets[y] for x in range(len(hsets)) for y in range(x + 1, len(hsets)))
        rec["beam"] = {"width": width, "depth": depth, "states_expanded": expanded, "children": children,
                       "moves_containing_finite_symbol_cells": finite_moves, "best_rays": best[0],
                       "best_rays_by_depth": best_by_depth,
                       "best_history": [[h[0], h[1], h[2]] for h in best[2]],
                       "best_history_has_overlapping_(noncommuting)_moves": overl,
                       "best_bad_gram_entries": verify(best[1], L), "best_describe": describe(best[1], Q)}
        part2.append(rec)

out = {"probe": "rqls_exact_trades_v2", "arithmetic": "fractions.Fraction (exact)", "rotation": "[[3/5,-4/5],[4/5,3/5]]",
       "part1_pair_graphs": part1, "part1b_crossed_mates": part1b, "part2_parker_trades": part2,
       "elapsed_s": round(time.monotonic() - T0, 3)}
with open(OUT, "x", encoding="utf-8") as fh:
    json.dump(out, fh, indent=1)
summ = {"part1": {}, "part1b": {}, "part2": []}
for r in part1:
    k = "%s/%s" % (r["pair"].split("_")[0][:6], r["role"])
    summ["part1"].setdefault(k, set()).add((r["sum_c_minus_1"], r["orthogonal_pair"]))
summ["part1"] = {k: sorted(v) for k, v in summ["part1"].items()}
for r in part1b:
    k = "%s/%s/%s" % (r["pair"], r["role"], "".join(str(x) for x in r["perm"]))
    summ["part1b"][k] = [r["orthogonal"], len(r["finite_pairs_disconnected"]), len(r["inf_pairs_disconnected"])]
for r in part2:
    if "one_trade" in r:
        summ["part2"].append([r["pair"], r["role"], "".join(str(x) for x in r["perm"]), r["classical_rays"],
                              r["classical_bad_gram_entries"], r["classical_nongauge_moves"],
                              (r["one_trade"] or {}).get("rays"), (r["one_trade"] or {}).get("bad_gram_entries"),
                              (r["commuting_pair"] or {}).get("rays"), (r["commuting_pair"] or {}).get("orders_equal"),
                              r["beam"]["best_rays"], r["beam"]["best_bad_gram_entries"],
                              r["beam"]["moves_containing_finite_symbol_cells"], r.get("beam_status")])
    else:
        summ["part2"].append([r["pair"], r["role"], r.get("perm"), r.get("status")])
summ["elapsed_s"] = out["elapsed_s"]
print(json.dumps(summ))
