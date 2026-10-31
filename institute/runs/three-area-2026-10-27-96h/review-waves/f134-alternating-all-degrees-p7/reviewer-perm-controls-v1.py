#!/usr/bin/env python3
"""f134 reviewer-written exact permutation-group controls (independent of the author's checker).

Usage: python3 reviewer-perm-controls-v1.py OUTPUT_LOG

Part A  Full subgroup lattices of A5 and A6 (double-coset join closure, exact); A7 lattice up to
        conjugacy with class sizes from normalizers (sum = total subgroup count).  From these:
        index sets, the A5 witness (5,6,15,20), the A7 repeated-index-7 counterexample, the largest
        distinct-index sets with pairwise gcd <= 7 and exactly 7, and the largest subgroup MULTISETS
        with pairwise index gcd exactly 7.
Part B  Explicit A8 four-index witness {8,15,28,35} by closure.
Part C  Negative controls: mutated generators must change orders/indices as predicted.
Exit status 0 iff every positive control passes and every negative control breaks as predicted.
"""
import sys, time, datetime, itertools
from math import gcd
import numpy as np


class Tee:
    def __init__(self, path):
        self.f = open(path, "w")
    def __call__(self, s=""):
        print(s)
        self.f.write(s + "\n")
        self.f.flush()


out = Tee(sys.argv[1])
BAD = 0


def pos(tag, ok, detail):
    global BAD
    if not ok:
        BAD += 1
    out(f"[{tag}] {'PASS' if ok else 'FAIL'}: {detail}")


def neg(tag, violated, detail):
    global BAD
    if not violated:
        BAD += 1
    out(f"[{tag}] {'NEG-OK' if violated else 'NEG-FAIL'}: {detail}")


# ------------------------------------------------------------------ permutation primitives (tuples, p[i] = image of i)
def sign(p):
    n = len(p)
    seen = [False] * n
    s = 0
    for i in range(n):
        if not seen[i]:
            j, L = i, 0
            while not seen[j]:
                seen[j] = True
                j = p[j]
                L += 1
            s += L - 1
    return -1 if s % 2 else 1


def cyc(n, *cycles):
    p = list(range(n))
    for c in cycles:
        for k in range(len(c)):
            p[c[k] - 1] = c[(k + 1) % len(c)] - 1
    return tuple(p)


def mul(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def closure_perm(gens):
    n = len(gens[0])
    e = tuple(range(n))
    seen = {e}
    frontier = [e]
    while frontier:
        nxt = []
        for x in frontier:
            for g in gens:
                y = mul(x, g)
                if y not in seen:
                    seen.add(y)
                    nxt.append(y)
        frontier = nxt
    return seen


# ------------------------------------------------------------------ table-based group machinery
class AltGroup:
    def __init__(self, n):
        self.n = n
        elems = sorted(p for p in itertools.permutations(range(n)) if sign(p) == 1)
        self.elems = elems
        N = self.N = len(elems)
        P = np.array(elems, dtype=np.int64)
        w = n ** np.arange(n, dtype=np.int64)
        codes = P @ w
        order = np.argsort(codes)
        sc = codes[order]
        T = np.empty((N, N), dtype=np.int32)
        for i in range(N):
            comp = P[i][P]            # (p_i o q)(k) = p_i[q[k]] for all q
            T[i] = order[np.searchsorted(sc, comp @ w)]
        self.T = T
        self.e = int(np.searchsorted(sc, (np.arange(n, dtype=np.int64) @ w)))
        self.e = int(order[self.e])
        inv = np.empty(N, dtype=np.int32)
        for i, p in enumerate(elems):
            q = [0] * n
            for a, b in enumerate(p):
                q[b] = a
            inv[i] = order[np.searchsorted(sc, np.array(q, dtype=np.int64) @ w)]
        self.inv = inv
        assert all(int(T[i, inv[i]]) == self.e for i in range(N))
        self.index_of = {p: i for i, p in enumerate(elems)}

    def closure(self, gens):
        T, seen = self.T, np.zeros(self.N, bool)
        seen[self.e] = True
        frontier = np.array([self.e], dtype=np.int32)
        while frontier.size:
            new = []
            for g in gens:
                Y = T[frontier, g]
                Y = np.unique(Y[~seen[Y]])
                if Y.size:
                    seen[Y] = True
                    new.append(Y)
            frontier = np.concatenate(new) if new else np.empty(0, dtype=np.int32)
        return np.flatnonzero(seen).astype(np.int32)

    def double_coset_reps(self, H):
        T, N = self.T, self.N
        covered = np.zeros(N, bool)
        covered[H] = True
        reps = []
        for g in range(N):
            if covered[g]:
                continue
            left = T[H, g]
            covered[T[left[:, None], H[None, :]].ravel()] = True
            reps.append(g)
        return reps

    def full_lattice(self):
        triv = np.array([self.e], dtype=np.int32)
        found = {triv.tobytes(): (triv, [])}
        queue = [triv.tobytes()]
        qi = 0
        while qi < len(queue):
            H, gens = found[queue[qi]]
            qi += 1
            if H.size == self.N:
                continue
            for g in self.double_coset_reps(H):
                J = self.closure(gens + [g])
                k = J.tobytes()
                if k not in found:
                    found[k] = (J, gens + [g])
                    queue.append(k)
        return [J for J, _ in found.values()]

    def canonical(self, J):
        """(canonical bytes of the conjugacy class of J, |N_G(J)|)."""
        T, inv, N = self.T, self.inv, self.N
        A = T[inv[:, None], J[None, :]]
        B = T[A, np.arange(N, dtype=np.int32)[:, None]]
        B.sort(axis=1)
        norm = int(np.count_nonzero((B == J[None, :]).all(axis=1)))
        best = min(B[i].tobytes() for i in range(N))
        return best, norm

    def lattice_classes(self):
        """Subgroup classes: list of (rep elements, |N_G(rep)|)."""
        triv = np.array([self.e], dtype=np.int32)
        key0, _ = self.canonical(triv)
        classes = {key0: (triv, [], self.N)}
        queue = [key0]
        qi = 0
        G_key = None
        while qi < len(queue):
            H, gens, _ = classes[queue[qi]]
            qi += 1
            if H.size == self.N:
                continue
            for g in self.double_coset_reps(H):
                J = self.closure(gens + [g])
                if J.size == self.N:
                    if G_key is None:
                        G_key = J.tobytes()
                        classes[G_key] = (J, gens + [g], self.N)
                    continue
                key, norm = self.canonical(J)
                if key not in classes:
                    classes[key] = (J, gens + [g], norm)
                    queue.append(key)
        return [(J, norm) for J, _, norm in classes.values()]


def max_clique(vertices, compatible):
    adj = {v: {w for w in vertices if w != v and compatible(v, w)} for v in vertices}
    best = []

    def bk(R, P, X):
        nonlocal best
        if not P and not X:
            if len(R) > len(best):
                best = list(R)
            return
        if len(R) + len(P) <= len(best):
            return
        u = max(P | X, key=lambda v: len(adj[v] & P))
        for v in list(P - adj[u]):
            bk(R + [v], P & adj[v], X & adj[v])
            P.remove(v)
            X.add(v)

    bk([], set(vertices), set())
    return sorted(best)


out(f"reviewer-perm-controls-v1 start {datetime.datetime.now(datetime.timezone.utc).isoformat()}")
t0 = time.time()

# ================================================================== Part A
summary = {}
for n in (5, 6, 7):
    t1 = time.time()
    G = AltGroup(n)
    N = G.N
    if n <= 6:
        subs = G.full_lattice()
        orders = sorted(J.size for J in subs)
        mult = {}
        for o in orders:
            mult[o] = mult.get(o, 0) + 1
        total = len(subs)
    else:
        classes = G.lattice_classes()
        mult = {}
        for J, norm in classes:
            o = int(J.size)
            mult[o] = mult.get(o, 0) + N // norm
        total = sum(mult.values())
        orders = sorted(mult)
    idx_mult = {N // o: c for o, c in mult.items()}           # index -> number of subgroups with that index
    distinct_proper = sorted(i for i in idx_mult if i > 1)
    best_le7 = max_clique(distinct_proper, lambda a, b: gcd(a, b) <= 7)
    best_eq7 = max_clique(distinct_proper, lambda a, b: gcd(a, b) == 7)
    # largest multiset of proper subgroups with all pairwise index gcds exactly 7:
    # values v with gcd(v,v)=v=7 may repeat (up to idx_mult[7]); other values at most once.
    rep7 = idx_mult.get(7, 0)
    best_multi = max_clique([i for i in distinct_proper if i != 7], lambda a, b: gcd(a, b) == 7 and a != 7 and b != 7)
    if rep7:
        best_multi = [v for v in best_multi if gcd(v, 7) == 7]  # must also be compatible with 7
        multi_size = rep7 + len(best_multi)
    else:
        multi_size = len(best_eq7)
    summary[n] = dict(total=total, idx_mult=idx_mult, best_le7=best_le7, best_eq7=best_eq7, rep7=rep7, multi=best_multi, multi_size=multi_size)
    out(f"A{n}: |A_n|={N}; total subgroups={total} [{time.time()-t1:.1f}s]; (index:count) = {dict(sorted(idx_mult.items()))}")
    out(f"A{n}: largest DISTINCT proper index set with pairwise gcd<=7: {best_le7} (size {len(best_le7)}); with pairwise gcd==7: {best_eq7} (size {len(best_eq7)})")
    out(f"A{n}: subgroups of index exactly 7: {rep7}; largest proper-subgroup MULTISET with all pairwise index gcds exactly 7: size {multi_size} = {rep7}x[7] + {best_multi}")

known_counts = {5: 59, 6: 501, 7: 3786}   # OEIS A029725 values quoted from reviewer memory (web_search prohibited); informational cross-check only
for n in (5, 6, 7):
    pos(f"A-count-n{n}", summary[n]["total"] == known_counts[n], f"computed total subgroups of A_{n} = {summary[n]['total']} (memory-quoted published count {known_counts[n]})")

s5 = summary[5]
pos("A5-orders", sorted(s5["idx_mult"]) == [1, 5, 6, 10, 12, 15, 20, 30, 60], f"A5 index set = {sorted(s5['idx_mult'])}")
pos("A5-witness", all(i in s5["idx_mult"] for i in (5, 6, 15, 20)), "indices 5,6,15,20 are realized by actual subgroups of A5 (orders 12,10,4,3)")
pos("A5-no-three-false", len(s5["best_le7"]) >= 4, f"A5 has {len(s5['best_le7'])} distinct proper indices with pairwise gcd<=7: {s5['best_le7']} -> the all-degree no-three and no-four statements are FALSE at n=5")
pos("A5-eq7", len(s5["best_eq7"]) <= 1, "A5 has no two indices with gcd exactly 7 (7 does not divide 60)")
s6 = summary[6]
pos("A6-eq7", len(s6["best_eq7"]) <= 1 and 5 not in s6["idx_mult"], f"A6: no gcd-7 pair; index 5 absent (no subgroup of order 72): index set {sorted(s6['idx_mult'])}")
s7 = summary[7]
pos("A7-index7", s7["rep7"] == 7, f"A7 has exactly {s7['rep7']} subgroups of index 7 (the point stabilizers A6)")
pos("A7-seven-indices-FALSIFIED", s7["rep7"] >= 7, "seven distinct proper subgroups of A7 (the seven A6 point stabilizers) have indices 7,7,7,7,7,7,7 with every pairwise gcd exactly 7: the candidate's n=7 seven-index exclusion is FALSE as a subgroup-index statement")
pos("A7-multiset", s7["multi_size"] >= 8, f"A7 proper-subgroup multiset with all pairwise index gcds exactly 7 has size {s7['multi_size']}: {s7['rep7']}x[7] + {s7['multi']} (so even eight or nine such subgroup indices exist)")
pos("A7-distinct-eq7", len(s7["best_eq7"]) <= 4, f"A7 largest DISTINCT index set with pairwise gcd exactly 7: {s7['best_eq7']} (size {len(s7['best_eq7'])}) <= table bound 4")
pos("A7-le7", len(s7["best_le7"]) >= 4, f"A7 distinct proper indices with pairwise gcd<=7: {s7['best_le7']} -> no-four is FALSE at n=7")
pos("A7-missing", all(i not in s7["idx_mult"] for i in (14, 28, 56, 63)), "A7 has no subgroup of index 14, 28, 56 or 63 (orders 180, 90, 45, 40)")

# explicit A7 point-stabilizer and coset check with tuples (independent of the table code)
A7 = closure_perm([cyc(7, (1, 2, 3)), cyc(7, (1, 2, 3, 4, 5, 6, 7))])
stabs = [{g for g in A7 if g[p] == p} for p in range(7)]
cosets = {}
for g in A7:
    cosets.setdefault(g[6], set()).add(g)          # left cosets of Stab(7): determined by the image of point 7
pos("A7-stab", len(A7) == 2520 and all(len(S) == 360 for S in stabs) and len({frozenset(S) for S in stabs}) == 7,
    "A7 generated as 2520 elements; seven distinct point stabilizers each of order 360 (index 7)")
pos("A7-cosets", len(cosets) == 7 and all(len(c) == 360 for c in cosets.values()) and sum(len(c) for c in cosets.values()) == 2520,
    "the seven left cosets of one A6 are pairwise disjoint, each of size 360, and partition A7 (seven-coset family with all pairwise index gcds 7; NOT an eight-coset family)")
S5 = closure_perm([cyc(7, (1, 2, 3, 4, 5)), cyc(7, (1, 2), (6, 7))])
K72 = closure_perm([cyc(7, (1, 2, 3, 4)), cyc(7, (1, 2)), cyc(7, (5, 6, 7)), cyc(7, (5, 6))])
K72 = {g for g in K72 if sign(g) == 1}
pos("A7-21-35", len(S5) == 120 and all(sign(g) == 1 for g in S5) and len(K72) == 72 and all(mul(a, b) in K72 for a in list(K72)[:20] for b in list(K72)[:20]),
    f"explicit even subgroups of A7 of orders 120 (index 21, twisted S5) and 72 (index 35, (S4xS3) cap A7): {len(S5)}, {len(K72)}")

# ================================================================== Part B: A8 witness {8,15,28,35}
A7in8 = closure_perm([cyc(8, (1, 2, 3)), cyc(8, (1, 2, 3, 4, 5, 6, 7))])
# AGL(3,2) on F_2^3 labelled 1..8 by x+2y+4z+1
def affine(mat, vec):
    p = []
    for v in range(8):
        x = [(v >> k) & 1 for k in range(3)]
        y = [(sum(mat[r][c] * x[c] for c in range(3)) + vec[r]) % 2 for r in range(3)]
        p.append(y[0] + 2 * y[1] + 4 * y[2])
    return tuple(p)
I3 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
AGL = closure_perm([affine(I3, [1, 0, 0]), affine(I3, [0, 1, 0]), affine(I3, [0, 0, 1]),
                    affine([[1, 1, 0], [0, 1, 0], [0, 0, 1]], [0, 0, 0]), affine([[0, 0, 1], [1, 0, 0], [0, 1, 0]], [0, 0, 0])])
S6tw = closure_perm([cyc(8, (1, 2), (7, 8)), cyc(8, (1, 2, 3, 4, 5, 6), (7, 8))])
W = closure_perm([cyc(8, (1, 2)), cyc(8, (1, 2, 3, 4)), cyc(8, (5, 6)), cyc(8, (5, 6, 7, 8)), cyc(8, (1, 5), (2, 6), (3, 7), (4, 8))])
Weven = {g for g in W if sign(g) == 1}
orders8 = (len(A7in8), len(AGL), len(S6tw), len(Weven))
idx8 = tuple(20160 // o for o in orders8)
g8 = [gcd(a, b) for k, a in enumerate(idx8) for b in idx8[k + 1:]]
pos("A8-witness", orders8 == (2520, 1344, 720, 576) and idx8 == (8, 15, 28, 35) and all(sign(g) == 1 for S in (A7in8, AGL, S6tw, Weven) for g in S) and all(x <= 7 for x in g8),
    f"A8 even subgroups of orders {orders8}, indices {idx8}, pairwise gcds {g8} (all <= 7): no-four is FALSE at n=8 as well")

# ================================================================== Part C: negative controls (reviewer-chosen mutations, not the author's)
A5 = closure_perm([cyc(5, (1, 2, 3)), cyc(5, (1, 2, 3, 4, 5))])
H1 = closure_perm([cyc(5, (1, 2, 3)), cyc(5, (1, 2, 4))])
H2 = closure_perm([cyc(5, (1, 2, 3, 4, 5)), cyc(5, (2, 5), (3, 4))])
H3 = closure_perm([cyc(5, (1, 2), (3, 4)), cyc(5, (1, 3), (2, 4))])
H4 = closure_perm([cyc(5, (1, 2, 3))])
pos("A5-gens", len(A5) == 60 and (len(H1), len(H2), len(H3), len(H4)) == (12, 10, 4, 3) and all(H <= A5 for H in (H1, H2, H3, H4)),
    f"candidate's generators give orders {(len(H1), len(H2), len(H3), len(H4))} inside A5 (indices {tuple(60//len(H) for H in (H1,H2,H3,H4))})")
M2 = closure_perm([cyc(5, (1, 2, 3, 4, 5)), cyc(5, (1, 2), (3, 4))])     # wrong reflection -> whole A5
M1 = closure_perm([cyc(5, (1, 2, 3)), cyc(5, (3, 4, 5))])                # two 3-cycles sharing one point -> A5
M3 = closure_perm([cyc(5, (1, 2), (3, 4)), cyc(5, (1, 2), (3, 5))])      # -> S3-type? order check
neg("NEG-H2", len(M2) == 60, f"replacing (2 5)(3 4) by (1 2)(3 4) gives order {len(M2)} (index 1, not proper)")
neg("NEG-H1", len(M1) == 60, f"replacing (1 2 4) by (3 4 5) gives order {len(M1)} (index 1, not proper)")
neg("NEG-H3", len(M3) != 4, f"replacing (1 3)(2 4) by (1 2)(3 5) gives order {len(M3)} != 4")
neg("NEG-A7", len({g for g in A7 if g[6] == 6 and g[5] == 5}) == 60, "fixing two points of A7 gives order 60 (index 42, gcd(42,7)=7 but 42 != 7): the index-7 count depends on fixing exactly one point")

out(f"SUMMARY: {'ALL CONTROLS AS EXPECTED' if BAD == 0 else str(BAD) + ' UNEXPECTED RESULT(S)'}; elapsed {time.time()-t0:.1f}s; end {datetime.datetime.now(datetime.timezone.utc).isoformat()}")
sys.exit(0 if BAD == 0 else 1)
