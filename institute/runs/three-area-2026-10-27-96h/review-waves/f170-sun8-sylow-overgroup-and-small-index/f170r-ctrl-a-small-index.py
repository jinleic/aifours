#!/usr/bin/env python3
"""f170r control A -- independently authored by reviewer ReviewF170Sun8Sylow.

Exact, CFSG-free computational control for claim (a):
  every finite nonabelian simple group with a proper subgroup of index <= 7
  is isomorphic to A5, A6, A7 or GL3(2).

Reduction (hand-verified in the review, elementary): an index-m subgroup of a
nonabelian simple S gives a faithful action whose image lies in A_m <= A7.
Hence it suffices to enumerate ALL subgroups of A7 up to conjugacy (cyclic
extension method: every subgroup is a join of cyclic subgroups) and identify
every nonabelian simple one up to isomorphism by explicit isomorphisms.

Also checks the individual elementary steps of the candidate (Sylow counts,
normalizer parities, order lists, the order-168 point-stabilizer / matching /
Steiner-triple / Fano steps) and runs intended-reason negative controls.
No author code is imported or executed. Usage: python3 -B this.py OUTFILE
"""
import itertools
import sys
from collections import Counter

import numpy as np

OUTPATH = sys.argv[1]
LINES = []
RESULTS = []


def log(*a):
    s = " ".join(str(x) for x in a)
    LINES.append(s)
    print(s, flush=True)


def check(name, ok, detail=""):
    RESULTS.append((name, bool(ok)))
    log(("PASS " if ok else "FAIL ") + name + ((" :: " + detail) if detail else ""))


def neg(name, rejected, detail=""):
    # negative control: the planted false statement MUST be rejected
    RESULTS.append(("NEG " + name, bool(rejected)))
    log(("NEG-REJECTED-AS-INTENDED " if rejected else "NEG-NOT-REJECTED(BAD) ") + name
        + ((" :: " + detail) if detail else ""))


def cycle_type(p):
    n = len(p)
    seen = [False] * n
    ct = []
    for i in range(n):
        if not seen[i]:
            j, L = i, 0
            while not seen[j]:
                seen[j] = True
                j = p[j]
                L += 1
            ct.append(L)
    return tuple(sorted(ct, reverse=True))


def sign(p):
    return -1 if sum(L - 1 for L in cycle_type(p)) % 2 else 1


def compose(a, b):
    # (a*b)(x) = a(b(x))
    return tuple(a[b[x]] for x in range(len(b)))


def pinv(a):
    r = [0] * len(a)
    for i, x in enumerate(a):
        r[x] = i
    return tuple(r)


class Table:
    """Finite group: explicit element list + multiplication table (int32)."""

    def __init__(self, elems, mult, e):
        self.elems = elems
        self.mult = mult
        self.N = len(elems)
        self.e = int(e)
        inv = np.empty(self.N, dtype=np.int64)
        r, c = np.nonzero(mult == self.e)
        inv[r] = c
        self.inv = inv
        self._conj = None
        self._order = None

    @property
    def conj(self):
        if self._conj is None:
            C = np.empty((self.N, self.N), dtype=np.int32)
            for g in range(self.N):
                C[g] = self.mult[self.mult[g], self.inv[g]]  # g x g^-1
            self._conj = C
        return self._conj

    @property
    def order(self):
        if self._order is None:
            o = np.ones(self.N, dtype=np.int64)
            for i in range(self.N):
                x, k = i, 1
                while x != self.e:
                    x = int(self.mult[x, i])
                    k += 1
                o[i] = k
            self._order = o
        return self._order

    def closure(self, gens, limit=None):
        mask = np.zeros(self.N, dtype=bool)
        mask[self.e] = True
        gens = np.array(sorted(set(int(g) for g in gens)), dtype=np.int64)
        if gens.size == 0:
            return mask
        frontier = np.array([self.e], dtype=np.int64)
        count = 1
        while frontier.size:
            prods = np.unique(self.mult[frontier[:, None], gens[None, :]].ravel())
            new = prods[~mask[prods]]
            mask[new] = True
            count += new.size
            if limit is not None and count > limit:
                return None
            frontier = new
        return mask


def perm_table(perms):
    perms = [tuple(p) for p in perms]
    n = len(perms[0])
    N = len(perms)
    P = np.array(perms, dtype=np.int64)
    w = n ** np.arange(n, dtype=np.int64)
    lookup = -np.ones(n ** n, dtype=np.int64)
    lookup[P @ w] = np.arange(N)
    mult = np.empty((N, N), dtype=np.int32)
    for i in range(N):
        mult[i] = lookup[P[i][P] @ w]  # row j: perm_i o perm_j
    assert (mult >= 0).all(), "element list not closed"
    return Table(perms, mult, perms.index(tuple(range(n))))


def generic_table(elems, mul, e):
    index = {x: i for i, x in enumerate(elems)}
    N = len(elems)
    mult = np.empty((N, N), dtype=np.int32)
    for i, a in enumerate(elems):
        for j, b in enumerate(elems):
            mult[i, j] = index[mul(a, b)]
    return Table(elems, mult, index[e])


def key_of(mask):
    return np.packbits(mask).tobytes()


def subgroup_classes(T):
    """All subgroups of T up to conjugacy by the cyclic extension method."""
    cyc = {}
    for g in range(T.N):
        k = key_of(T.closure([g]))
        if k not in cyc:
            cyc[k] = g
    cyc_gens = list(cyc.values())
    reps = []
    key2cls = {}

    def classify(mask, gens):
        k = key_of(mask)
        if k in key2cls:
            return key2cls[k]
        idx = np.nonzero(mask)[0]
        inv = (int(idx.size), tuple(sorted(Counter(T.order[idx].tolist()).items())))
        for c, R in enumerate(reps):
            if R["inv"] == inv and R["mask"][T.conj[:, idx]].all(axis=1).any():
                key2cls[k] = c
                return c
        reps.append(dict(mask=mask, idx=idx, gens=list(gens), inv=inv))
        key2cls[k] = len(reps) - 1
        return len(reps) - 1

    triv = np.zeros(T.N, dtype=bool)
    triv[T.e] = True
    classify(triv, [])
    q = 0
    joins = 0
    while q < len(reps):
        H = reps[q]
        q += 1
        for g in cyc_gens:
            if H["mask"][g]:
                continue
            gens = H["gens"] + [g]
            classify(T.closure(gens), gens)
            joins += 1
    for R in reps:
        R["norm"] = int(R["mask"][T.conj[:, R["idx"]]].all(axis=1).sum())
        R["clsize"] = T.N // R["norm"]
    return reps, cyc_gens, joins


def is_abelian(T, idx):
    sub = T.mult[np.ix_(idx, idx)]
    return bool((sub == sub.T).all())


def is_simple_nonabelian(T, idx):
    if idx.size == 1 or is_abelian(T, idx):
        return False
    done = np.zeros(T.N, dtype=bool)
    done[T.e] = True
    for x in idx:
        if done[x]:
            continue
        cls = np.unique(T.conj[idx, x])
        done[cls] = True
        if T.closure(cls).sum() != idx.size:
            return False
    return True


def subtable(T, idx):
    pos = -np.ones(T.N, dtype=np.int64)
    pos[idx] = np.arange(idx.size)
    sub = pos[T.mult[np.ix_(idx, idx)]]
    assert (sub >= 0).all()
    return Table([int(i) for i in idx], sub.astype(np.int32), int(pos[T.e]))


def find_iso(A, B):
    """Explicit isomorphism A -> B (as index map) or None."""
    if A.N != B.N:
        return None
    oA, oB = A.order, B.order
    gen = None
    order_rank = sorted(range(A.N), key=lambda i: -oA[i])
    for x in order_rank:
        for y in range(A.N):
            m = A.closure([x, y], limit=None)
            if m.sum() == A.N:
                gen = (x, y)
                break
        if gen:
            break
    x, y = gen
    oxy = oA[A.mult[x, y]]
    X = [i for i in range(B.N) if oB[i] == oA[x]]
    for xp in X:
        for yp in range(B.N):
            if oB[yp] != oA[y] or oB[B.mult[xp, yp]] != oxy:
                continue
            phi = -np.ones(A.N, dtype=np.int64)
            phi[A.e] = B.e
            stack = [A.e]
            ok = True
            while stack and ok:
                k = stack.pop()
                for s, sp in ((x, xp), (y, yp)):
                    k2 = int(A.mult[k, s])
                    v = int(B.mult[phi[k], sp])
                    if phi[k2] < 0:
                        phi[k2] = v
                        stack.append(k2)
                    elif phi[k2] != v:
                        ok = False
                        break
            if ok and (phi >= 0).all() and len(set(phi.tolist())) == A.N:
                # full homomorphism re-check on every pair
                lhs = phi[A.mult]
                rhs = B.mult[phi[:, None], phi[None, :]]
                if (lhs == rhs).all():
                    return phi
    return None


def orbits_of(gens_perms, n):
    parent = list(range(n))

    def f(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    for p in gens_perms:
        for i in range(n):
            a, b = f(i), f(p[i])
            if a != b:
                parent[a] = b
    groups = {}
    for i in range(n):
        groups.setdefault(f(i), []).append(i)
    return sorted(groups.values(), key=lambda g: (-len(g), g))


def main():
    log("f170r control A: A7 subgroup lattice + small-index candidate step checks")
    # ---------------- A7 ----------------
    S7 = list(itertools.permutations(range(7)))
    A7 = [p for p in S7 if sign(p) == 1]
    check("|S7|=5040,|A7|=2520", len(S7) == 5040 and len(A7) == 2520)
    T = perm_table(A7)
    reps, cyc_gens, joins = subgroup_classes(T)
    log("A7: cyclic subgroups =", len(cyc_gens), "; joins computed =", joins,
        "; conjugacy classes of subgroups =", len(reps),
        "; total subgroups =", sum(R["clsize"] for R in reps))
    # cross-check the number of cyclic subgroups by a direct element count
    by_order = Counter(T.order.tolist())
    phi_ = {1: 1, 2: 1, 3: 2, 4: 2, 5: 4, 6: 2, 7: 6}
    direct_cyc = sum(cnt // phi_[o] for o, cnt in by_order.items())
    cyc_from_classes = sum(R["clsize"] for R in reps
                           if any(T.order[R["idx"]] == R["idx"].size))
    check("cyclic-subgroup count: direct element count == lattice count",
          direct_cyc == len(cyc_gens) == cyc_from_classes,
          f"direct={direct_cyc} cyc={len(cyc_gens)} lattice={cyc_from_classes}")
    # describe every class
    rows = []
    for c, R in enumerate(reps):
        idx = R["idx"]
        gens = [T.elems[g] for g in R["gens"]]
        orb = orbits_of(gens, 7)
        simple = is_simple_nonabelian(T, idx)
        rows.append((int(idx.size), tuple(len(o) for o in orb), simple, R["clsize"], c))
    rows.sort()
    log("class table (order, orbit sizes on 7 points, simple-nonabelian?, #conjugates):")
    for r in rows:
        log("  ", r[:4])
    simple_classes = [r for r in rows if r[2]]
    log("nonabelian simple classes:", [(r[0], r[1]) for r in simple_classes])
    orders_simple = sorted(set(r[0] for r in simple_classes))
    check("orders of nonabelian simple subgroups of A7 are exactly {60,168,360,2520}",
          orders_simple == [60, 168, 360, 2520], str(orders_simple))
    # ---------------- reference groups ----------------
    A5 = perm_table([p for p in itertools.permutations(range(5)) if sign(p) == 1])
    A6 = perm_table([p for p in itertools.permutations(range(6)) if sign(p) == 1])

    def matmul2(a, b):
        return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(3)) % 2 for j in range(3))
                     for i in range(3))

    mats = []
    for bits in range(512):
        m = tuple(tuple((bits >> (3 * i + j)) & 1 for j in range(3)) for i in range(3))
        det = (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
               - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
               + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])) % 2
        if det == 1:
            mats.append(m)
    I3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    GL32 = generic_table(mats, matmul2, I3)
    check("|GL3(2)| = 168 = (8-1)(8-2)(8-4)", GL32.N == 168 == 7 * 6 * 4)
    ref = {60: ("A5", A5), 168: ("GL3(2)", GL32), 360: ("A6", A6)}
    for r in simple_classes:
        order, orb, _, _, c = r
        idx = reps[c]["idx"]
        if order == 2520:
            check("order-2520 simple class is A7 itself", idx.size == T.N)
            continue
        name, Ref = ref[order]
        phi = find_iso(subtable(T, idx), Ref)
        check(f"simple class order {order} orbits {orb} is isomorphic to {name} (explicit iso)",
              phi is not None)
    # each of the four groups has a proper subgroup of index <= 7
    stab5 = A5.closure([i for i, p in enumerate(A5.elems) if p[0] == 0])
    stab6 = A6.closure([i for i, p in enumerate(A6.elems) if p[0] == 0])
    stab7 = T.closure([i for i, p in enumerate(T.elems) if p[0] == 0])
    v = (1, 0, 0)
    stabv = GL32.closure([i for i, m in enumerate(GL32.elems)
                          if tuple(sum(m[r][k] * v[k] for k in range(3)) % 2 for r in range(3)) == v])
    check("A5,A6,A7,GL3(2) have subgroups of index 5,6,7,7",
          (60 // stab5.sum(), 360 // stab6.sum(), 2520 // stab7.sum(), 168 // stabv.sum())
          == (5, 6, 7, 7))
    neg("planted classification 'simple subgroups of A7 have orders only in {60,360,2520}'",
        any(r[0] == 168 for r in simple_classes),
        "rejected because the exhaustive lattice contains nonabelian simple classes of order 168")
    # ---------------- Section 2 arithmetic and A6 facts ----------------
    div72 = [d for d in range(1, 73) if 72 % d == 0]
    check("Sylow-3 options (divisors of 8, =1 mod 3) are {1,4}",
          [d for d in range(1, 9) if 8 % d == 0 and d % 3 == 1] == [1, 4])
    check("Sylow-5 options (divisors of 72, =1 mod 5) are {1,6,36}",
          [d for d in div72 if d % 5 == 1] == [1, 6, 36])
    check("multiples of 30 dividing 360 are {30,60,90,120,180,360}",
          [d for d in range(1, 361) if 360 % d == 0 and d % 30 == 0] == [30, 60, 90, 120, 180, 360])
    a6_orders = sorted(set(r[0] for r in rows if 1 in r[1]))  # classes with a fixed point
    check("A6 (classes of A7 with a fixed point) has no subgroup of order 30,90,120,180",
          not ({30, 90, 120, 180} & set(a6_orders)), f"A6 subgroup orders={a6_orders}")
    check("order-30 count argument: 24 (order 5) + 20 (order 3) > 29", 24 + 20 > 29)
    # order 60: facts in the standard A5
    syl5 = {key_of(A5.closure([i])) for i in range(60) if A5.order[i] == 5}
    syl3 = {key_of(A5.closure([i])) for i in range(60) if A5.order[i] == 3}
    inv2 = [i for i in range(60) if A5.order[i] == 2]
    syl2 = set()
    for a in inv2:
        for b in inv2:
            m = A5.closure([a, b])
            if m.sum() == 4:
                syl2.add(key_of(m))
    cent = sorted(set(int((A5.mult[x] == A5.mult[:, x]).sum()) for x in inv2))
    check("standard A5: n5=6, n3=10, n2=5, Sylow-2 = V4, involution centralizers of order 4",
          (len(syl5), len(syl3), len(syl2), cent) == (6, 10, 5, [4])
          and not any(A5.order[i] == 4 for i in range(60)),
          f"n5={len(syl5)} n3={len(syl3)} n2={len(syl2)} C(inv)={cent}")
    check("order-60 count: 2 generators x 15 cyclic C4 = 30 > 15 remaining", 30 > 60 - 1 - 24 - 20)
    check("order-60 count: 15 disjoint V4 give 45 involutions > 15", 15 * 3 > 15)
    # ---------------- Section 3 ----------------
    c7 = tuple((x + 1) % 7 for x in range(7))
    C7 = set()
    x = tuple(range(7))
    for _ in range(7):
        C7.add(x)
        x = compose(c7, x)
    normS7 = [p for p in S7 if compose(compose(p, c7), pinv(p)) in C7]
    normA7 = [p for p in normS7 if sign(p) == 1]
    neg_one = tuple((-x) % 7 for x in range(7))
    two = tuple((2 * x) % 7 for x in range(7))
    check("N_S7(<7-cycle>) has order 42, N_A7 has order 21",
          (len(normS7), len(normA7)) == (42, 21))
    check("x->-x on F7 is odd (fixes 0, three 2-cycles); x->2x is even",
          sign(neg_one) == -1 and cycle_type(neg_one) == (2, 2, 2, 1) and sign(two) == 1)
    div360_1mod7 = [d for d in range(1, 361) if 360 % d == 0 and d % 7 == 1]
    check("divisors of 360 that are 1 mod 7 are {1,8,15,36,120}", div360_1mod7 == [1, 8, 15, 36, 120])
    cand = sorted({n * k for n in [8, 15, 36, 120] for k in [7, 21] if 2520 % (n * k) == 0})
    check("candidate order list = {56,105,168,252,315,840,2520}",
          cand == [56, 105, 168, 252, 315, 840, 2520], str(cand))
    seven_orders = sorted(set(r[0] for r in rows if r[0] % 7 == 0))
    trans = sorted(set(r[0] for r in rows if r[1] == (7,)))
    check("A7 subgroups of order divisible by 7 have orders {7,21,168,2520} only",
          seven_orders == [7, 21, 168, 2520], str(seven_orders))
    check("transitive subgroups of A7 have orders {7,21,168,2520}", trans == [7, 21, 168, 2520], str(trans))
    check("no subgroup of A7 has order 56,105,252,315,840 or 504",
          not ({56, 105, 252, 315, 840, 504} & set(r[0] for r in rows)))
    # the parity step is load-bearing: with S7-normalizer orders the list would grow
    candS = sorted({n * k for n in [8, 15, 36, 120] for k in [7, 14, 21, 42] if 2520 % (n * k) == 0})
    neg("planted variant ignoring parity (normalizer orders 7,14,21,42) gives the same order list",
        candS != cand, f"list without parity step = {candS}; extra = {sorted(set(candS) - set(cand))}")
    c5 = (1, 2, 3, 4, 0, 5)
    S6 = list(itertools.permutations(range(6)))
    C5 = set()
    x = tuple(range(6))
    for _ in range(5):
        C5.add(x)
        x = compose(c5, x)
    nS6 = [p for p in S6 if compose(compose(p, c5), pinv(p)) in C5]
    check("N_S6(C5)=20 contains odd elements; N_A6(C5)=10",
          len(nS6) == 20 and len([p for p in nS6 if sign(p) == 1]) == 10)
    check("Sylow-5 count in order 45: divisors of 9 that are 1 mod 5 = {1}",
          [d for d in (1, 3, 9) if d % 5 == 1] == [1])
    check("Sylow-5 count in order 105: divisors of 21 that are 1 mod 5 = {1,21}",
          [d for d in (1, 3, 7, 21) if d % 5 == 1] == [1, 21])
    check("order-105 count: 90 + 84 > 104", 90 + 84 > 104)
    check("order-56 count: 56 - 48 = 8 elements left", 56 - 8 * 6 == 8)
    check("order-252 count: 252 - 36*6 = 36 = |point stabilizer|", 252 - 36 * 6 == 36)
    # ---------------- Section 4 (order 168) ----------------
    A6on = [p for p in itertools.permutations(range(1, 7))]

    def even6(p):
        return sign((0,) + tuple(p)) == 1

    check("3-set stabilizer in A6 has order 18; 2-point stabilizer in A7 has order 60; (S2)^3 in A6 has order 4",
          len([p for p in A6on if even6(p) and set(p[:3]) == {1, 2, 3}]) == 18
          and len([p for p in A7 if p[0] == 0 and p[1] == 1]) == 60
          and len([p for p in A6on if even6(p) and all({p[2 * i], p[2 * i + 1]} == {2 * i + 1, 2 * i + 2}
                                                         for i in range(3))]) == 4)
    fano_ok = True
    blocks_seen = []
    for r in simple_classes:
        if r[0] != 168:
            continue
        idx = reps[r[4]]["idx"]
        K = [T.elems[i] for i in idx]
        H = [p for p in K if p[0] == 0]
        Horb = orbits_of(H, 7)
        ok1 = len(H) == 24 and sorted(len(o) for o in Horb) == [1, 6]
        Hidx = np.array([T.elems.index(p) for p in H])
        # Sylow 2-subgroups of H: all subgroups of order 8 generated by <= 3 two-elements
        # (every group of order 8 is generated by at most 3 elements)
        twos = [int(i) for i in Hidx if T.order[i] in (1, 2, 4, 8)]
        syl = {}
        for a in twos:
            for b in twos:
                for c3 in twos:
                    m = T.closure([a, b, c3])
                    if m.sum() == 8:
                        syl[key_of(m)] = np.nonzero(m)[0]
        sylL = list(syl.values())
        ok2 = len(sylL) == 3
        kern = [int(g) for g in Hidx
                if all(set(T.conj[g, s].tolist()) == set(s.tolist()) for s in sylL)]
        korb = orbits_of([T.elems[g] for g in kern], 7)
        ok3 = len(kern) == 4 and sorted(len(o) for o in korb) == [1, 2, 2, 2]
        matching = [set(o) for o in korb if len(o) == 2]
        mstab = [p for p in A7 if p[0] == 0 and all({p[a] for a in mset} in matching for mset in matching)]
        ok4 = len(mstab) == 24 and set(mstab) == set(H)
        blocks = set()
        ok5 = True
        for pp in range(7):
            for qq in range(7):
                if pp == qq:
                    continue
                J = [p for p in K if p[pp] == pp and p[qq] == qq]
                fix = frozenset(i for i in range(7) if all(p[i] == i for p in J))
                ok5 &= (len(J) == 4 and len(fix) == 3)
                blocks.add(fix)
        ok6 = len(blocks) == 7 and all(sum(1 for b in blocks if {u, w} <= b) == 1
                                       for u in range(7) for w in range(u + 1, 7))
        aut = [p for p in S7 if {frozenset(p[i] for i in b) for b in blocks} == blocks]
        ok7 = len(aut) == 168 and set(K) <= set(aut)
        fano_ok &= ok1 and ok2 and ok3 and ok4 and ok5 and ok6 and ok7
        blocks_seen.append(blocks)
        check(f"order-168 class {r[4]}: H=24 transitive on 6; n2(H)=3; kernel 4 with three 2-orbits; "
              f"H = even matching stabilizer; |S_pq|=4 with 3 fixed points; STS(7); Aut order 168 contains S",
              ok1 and ok2 and ok3 and ok4 and ok5 and ok6 and ok7,
              f"{ok1,ok2,ok3,ok4,ok5,ok6,ok7}")
    # subdegrees of transitive subgroups (2+4 never occurs; the argument shows it cannot)
    subdeg = {}
    for r in rows:
        if r[1] == (7,):
            K = [T.elems[i] for i in reps[r[4]]["idx"]]
            H = [p for p in K if p[0] == 0]
            subdeg[r[0], r[4]] = tuple(len(o) for o in orbits_of(H, 7))
    log("subdegrees of transitive subgroups of A7 (order, class) -> orbit sizes of a point stabilizer:", subdeg)
    check("no transitive subgroup of A7 has subdegrees {1,2,4}",
          all(sorted(s) != [1, 2, 4] for s in subdeg.values()))
    # all labelled STS(7): 30 of them, a single S7-orbit (so any STS(7) is the Fano plane)
    pairs = [(u, w) for u in range(7) for w in range(u + 1, 7)]
    triples = [frozenset(t) for t in itertools.combinations(range(7), 3)]
    systems = []

    def bt(chosen, covered):
        if len(covered) == 21:
            systems.append(frozenset(chosen))
            return
        u, w = next(pq for pq in pairs if pq not in covered)
        for t in triples:
            if u in t and w in t:
                tp = [(a, b) for a in sorted(t) for b in sorted(t) if a < b]
                if not any(pq in covered for pq in tp):
                    bt(chosen + [t], covered | set(tp))

    bt([], set())
    fano = frozenset(frozenset(t) for t in [(0, 1, 2), (0, 3, 4), (0, 5, 6), (1, 3, 5), (1, 4, 6), (2, 3, 6), (2, 4, 5)])
    orbit = {frozenset(frozenset(p[i] for i in b) for b in fano) for p in S7}
    check("there are exactly 30 labelled STS(7), forming one S7-orbit of the candidate's labelled Fano system",
          len(set(systems)) == 30 and set(systems) == orbit)
    vec = {0: (1, 0, 0), 1: (0, 1, 0), 3: (0, 0, 1)}
    vec[2] = tuple((a + b) % 2 for a, b in zip(vec[0], vec[1]))
    vec[4] = tuple((a + b) % 2 for a, b in zip(vec[0], vec[3]))
    vec[5] = tuple((a + b) % 2 for a, b in zip(vec[1], vec[3]))
    vec[6] = (1, 1, 1)
    check("candidate labelling p,1,3 -> basis makes every Fano triple zero-sum in F2^3",
          len(set(vec.values())) == 7
          and all(tuple(sum(vec[i][k] for i in b) % 2 for k in range(3)) == (0, 0, 0) for b in fano))
    if blocks_seen:
        check("each order-168 class's fixed-point triple system is isomorphic to the Fano labelling",
              all(bl in orbit for bl in blocks_seen))
    # negative: in A7 itself S_pq has only 2 fixed points -> no triple system
    J = [p for p in A7 if p[0] == 0 and p[1] == 1]
    fixA7 = [i for i in range(7) if all(p[i] == i for p in J)]
    neg("planted 'S_pq always has a unique third fixed point' tested in S=A7",
        len(fixA7) == 2, f"Fix(S_01) in A7 = {fixA7}")
    # negative: isomorphism finder must reject non-isomorphic groups of equal order
    S4 = perm_table(list(itertools.permutations(range(4))))

    def mm3(a, b):
        return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2)) % 3 for j in range(2)) for i in range(2))

    sl23 = [((a, b), (c, d)) for a in range(3) for b in range(3) for c in range(3) for d in range(3)
            if (a * d - b * c) % 3 == 1]
    SL23 = generic_table(sl23, mm3, ((1, 0), (0, 1)))
    relabel = (2, 0, 3, 1)
    S4b = perm_table([compose(compose(relabel, p), pinv(relabel)) for p in itertools.permutations(range(4))][::-1])
    check("isomorphism finder positive control: S4 ~ relabelled S4", find_iso(S4, S4b) is not None)
    neg("isomorphism finder asked to identify S4 with SL(2,3) (both order 24)",
        SL23.N == 24 and find_iso(S4, SL23) is None)
    # ---------------- cross-check: PSL(2,8), order 504 dividing 2520 ----------------

    def gf8mul(a, b):
        r = 0
        for i in range(3):
            if (b >> i) & 1:
                r ^= a << i
        for i in (4, 3):
            if (r >> i) & 1:
                r ^= 0b1011 << (i - 3)
        return r

    def m8(a, b):
        (a11, a12), (a21, a22) = a
        (b11, b12), (b21, b22) = b
        return ((gf8mul(a11, b11) ^ gf8mul(a12, b21), gf8mul(a11, b12) ^ gf8mul(a12, b22)),
                (gf8mul(a21, b11) ^ gf8mul(a22, b21), gf8mul(a21, b12) ^ gf8mul(a22, b22)))

    sl28 = [((a, b), (c, d)) for a in range(8) for b in range(8) for c in range(8) for d in range(8)
            if gf8mul(a, d) ^ gf8mul(b, c) == 1]
    L28 = generic_table(sl28, m8, ((1, 0), (0, 1)))
    r28, _, _ = subgroup_classes(L28)
    o28 = sorted(set(int(R["idx"].size) for R in r28))
    simple28 = is_simple_nonabelian(L28, np.arange(L28.N))
    check("PSL(2,8)=SL(2,8): order 504, simple, no subgroup of index <= 7 (orders 72, 84 absent); min index 9",
          L28.N == 504 and simple28 and 72 not in o28 and 84 not in o28
          and min(504 // o for o in o28 if o < 504) == 9, f"subgroup orders={o28}")
    # ---------------- summary ----------------
    npass = sum(1 for _, ok in RESULTS if ok)
    log(f"SUMMARY: {npass}/{len(RESULTS)} checks as expected; failures: "
        f"{[n for n, ok in RESULTS if not ok]}")
    with open(OUTPATH, "w") as fh:
        fh.write("\n".join(LINES) + "\n")


if __name__ == "__main__":
    main()
