#!/usr/bin/env python3
"""rf164-illustration-v1.py -- one fully explicit, hand-checkable example for the
review of wave f164 (reviewer ReviewF164SemigroupQ1).  Standalone; no author code.

Source S = B x| Z2 with B = free right regular band monoid on {a,b}
(elements 1,a,b,ab,ba; u.v = (u minus letters of v) followed by v),
Z2 acting by the letter swap, product (u,g)(v,h) = (u . swap^g(v), g+h),
actor q(u,g) = g  (pure, onto the completely simple semigroup Z2).
Prints table, E(S), Green's R/L/H, local bands, local R/L pairs, lambda_S, rho_S,
and checks the source-reduction claims and the instance identity literally.
Usage: python3 -B rf164-illustration-v1.py
"""
import itertools

W = [(), ('a',), ('b',), ('a', 'b'), ('b', 'a')]
NAME = {(): '1', ('a',): 'a', ('b',): 'b', ('a', 'b'): 'ab', ('b', 'a'): 'ba'}
ix = {w: i for i, w in enumerate(W)}


def bmul(u, v):
    return tuple(z for z in u if z not in v) + v


def swap(u):
    return tuple({'a': 'b', 'b': 'a'}[z] for z in u)


EL = [(u, g) for g in (0, 1) for u in W]
EI = {x: i for i, x in enumerate(EL)}


def smul(x, y):
    (u, g), (v, h) = x, y
    return (bmul(u, swap(v) if g else v), (g + h) % 2)


n = len(EL)
T = [[EI[smul(x, y)] for y in EL] for x in EL]
nm = [f"({NAME[u]},{g})" for (u, g) in EL]
q = [g for (u, g) in EL]
assoc = all(T[T[a][b]][c] == T[a][T[b][c]] for a in range(n) for b in range(n) for c in range(n))
print("elements:", ", ".join(f"{i}={s}" for i, s in enumerate(nm)))
print("table (row*col):")
for a in range(n):
    print("  ", " ".join(f"{T[a][b]:>2}" for b in range(n)))
E = [a for a in range(n) if T[a][a] == a]
R = [frozenset([a] + T[a]) for a in range(n)]
L = [frozenset([a] + [T[s][a] for s in range(n)]) for a in range(n)]
regular = all(any(T[T[a][x]][a] == a for x in range(n)) for a in range(n))
pure = all(T[a][a] == a for a in range(n) if q[a] == 0)
print("associative:", assoc, "| regular:", regular, "| q pure:", pure)
print("E(S):", [nm[e] for e in E])


def classes(keys):
    d = {}
    for a in range(n):
        d.setdefault(keys[a], []).append(nm[a])
    return list(d.values())


print("R-classes:", classes(R))
print("L-classes:", classes(L))
print("H-classes:", classes([(R[a], L[a]) for a in range(n)]))
pr, pl = set(), set()
for g in E:
    M = [x for x in E if T[T[g][x]][g] == x]
    rr = all(T[T[x][y]][x] == T[y][x] for x in M for y in M)
    print(f"local band E({nm[g]} S {nm[g]}) = {[nm[x] for x in M]}  right regular: {rr}")
    for x, y in itertools.combinations(M, 2):
        if R[x] == R[y]:
            pr.add((x, y))
        if L[x] == L[y]:
            pl.add((x, y))
print("local R-pairs:", [(nm[x], nm[y]) for x, y in sorted(pr)], "| local L-pairs:",
      [(nm[x], nm[y]) for x, y in sorted(pl)])


def cong(pairs):
    par = list(range(n))

    def f(x):
        while par[x] != x:
            x = par[x]
        return x
    st = list(pairs)
    while st:
        a, b = st.pop()
        ra, rb = f(a), f(b)
        if ra == rb:
            continue
        par[ra] = rb
        for s in range(n):
            st.append((T[s][a], T[s][b]))
            st.append((T[a][s], T[b][s]))
    return [f(x) for x in range(n)]


lam, rho = cong(pr), cong(pl)
print("lambda_S classes:", classes(lam))
print("rho_S classes:", classes(rho))
lamR = all(R[a] == R[b] for a in range(n) for b in range(n) if lam[a] == lam[b])
lamq = all(q[a] == q[b] for a in range(n) for b in range(n) if lam[a] == lam[b])
Hq = all(a == b for a in range(n) for b in range(n) if R[a] == R[b] and L[a] == L[b] and q[a] == q[b])
print("lambda_S <= R:", lamR, "| lambda_S <= ker q:", lamq, "| rho_S = Delta:", len(set(rho)) == n,
      "| H meet ker q = Delta:", Hq)
# S/lambda_S: local bands must be semilattices (left regular by (3), right regular as images)
reps = {}
for a in range(n):
    reps.setdefault(lam[a], a)
cl = sorted(reps)
Q = {(c, d): lam[T[reps[c]][reps[d]]] for c in cl for d in cl}
EQ = [c for c in cl if Q[(c, c)] == c]
semil = True
for g in EQ:
    M = [x for x in EQ if Q[(Q[(g, x)], g)] == x]
    semil = semil and all(Q[(x, y)] == Q[(y, x)] for x in M for y in M)
print(f"|S/lambda_S| = {len(cl)}; its local bands are semilattices (locally inverse): {semil}")
viol = tested = 0
for e in range(n):
    for x in range(n):
        for y in range(n):
            exe, eye = T[T[e][x]][e], T[T[e][y]][e]
            if q[exe] == q[e] == q[eye]:
                tested += 1
                lhs = T[T[T[T[T[T[e][x]][e]][y]][e]][x]][e]
                rhs = T[T[T[T[e][y]][e]][x]][e]
                viol += (lhs != rhs)
print(f"instance identity e x e y e x e = e y e x e on admissible triples: tested={tested}, violations={viol}")
ok = assoc and regular and pure and lamR and lamq and Hq and len(set(rho)) == n and semil and viol == 0 and pr
print("ILLUSTRATION:", "AS EXPECTED" if ok else "SURPRISE")
