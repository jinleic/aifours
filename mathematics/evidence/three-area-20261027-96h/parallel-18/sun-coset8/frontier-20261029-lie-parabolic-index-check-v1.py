#!/usr/bin/env python3
"""Exact integer-polynomial checks for the Lie-type parabolic-index packet.

Checks, by exact division of integer polynomials:
  1. untwisted types: [G:P_J](x) = W(x)/W_J(x) (Poincare polynomials) is divisible by
     Phi_h(x) for every maximal J (exceptional types; classical types in finite rank ranges);
  2. twisted types: |G|_{p'}(x) / |L_J|_{p'}(x) is an exact polynomial divisible by Phi_e(x)
     for the listed maximal F-stable Levi p'-orders (3D4, 2E6, 2F4, 2B2, 2G2, and 2A_n, 2D_n
     in finite rank ranges);
  3. Phi_e(q) in {1,7} only for (e,q) in {(3,2),(6,3)} among tested e and prime powers q<2000;
  4. pairwise gcds of maximal parabolic indices in the seven q=3, e=6 groups.
Finite checks only: the general-rank arguments are written in the packet.
"""
from functools import lru_cache
from math import gcd


def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def pmul(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                r[i + j] += x * y
    return trim(r)


def pdivmod(a, b):
    a = a[:]
    db = len(b) - 1
    if abs(b[-1]) != 1:
        raise ValueError("non-unit leading coefficient")
    q = [0] * max(1, len(a) - db)
    while len(a) - 1 >= db and any(a):
        k = len(a) - 1 - db
        c = a[-1] * b[-1]
        q[k] = c
        for i, y in enumerate(b):
            a[i + k] -= c * y
        trim(a)
        if len(a) - 1 < db:
            break
    return trim(q), a


def exactdiv(a, b):
    q, r = pdivmod(a, b)
    if any(r):
        raise ValueError("not an exact polynomial division")
    return q


def divides(b, a):
    return not any(pdivmod(a, b)[1])


def xm(d, eps):
    r = [0] * (d + 1)
    r[d] = 1
    r[0] = -eps
    return r


def prod(fs):
    r = [1]
    for f in fs:
        r = pmul(r, f)
    return r


def peval(a, x):
    s = 0
    for c in reversed(a):
        s = s * x + c
    return s


@lru_cache(None)
def cyclo(n):
    p = xm(n, 1)
    for d in range(1, n):
        if n % d == 0:
            p = exactdiv(p, list(cyclo(d)))
    return tuple(p)


DEG = {"A": lambda k: list(range(2, k + 2)), "B": lambda k: [2 * i for i in range(1, k + 1)],
       "C": lambda k: [2 * i for i in range(1, k + 1)],
       "D": lambda k: [2 * i for i in range(1, k)] + [k], "E6": lambda k: [2, 5, 6, 8, 9, 12],
       "E7": lambda k: [2, 6, 8, 10, 12, 14, 18], "E8": lambda k: [2, 8, 12, 14, 18, 20, 24, 30],
       "F4": lambda k: [2, 6, 8, 12], "G2": lambda k: [2, 6]}
COX = {"A": lambda n: n + 1, "B": lambda n: 2 * n, "C": lambda n: 2 * n, "D": lambda n: 2 * n - 2,
       "E6": lambda n: 12, "E7": lambda n: 18, "E8": lambda n: 30, "F4": lambda n: 12, "G2": lambda n: 6}


def degs(comp):
    t, k = comp
    if t == "D" and k == 3:
        return DEG["A"](3)
    if t == "D" and k == 2:
        return DEG["A"](1) * 2
    if t in ("B", "C") and k == 1:
        return DEG["A"](1)
    return DEG[t](k)


def poincare(comps):
    return prod([[1] * d for c in comps for d in degs(c)])


EXC = {("G2", 2): [[("A", 1)], [("A", 1)]],
       ("F4", 4): [[("C", 3)], [("A", 1), ("A", 2)], [("A", 2), ("A", 1)], [("B", 3)]],
       ("E6", 6): [[("D", 5)], [("A", 5)], [("A", 1), ("A", 4)], [("A", 2), ("A", 1), ("A", 2)],
                   [("A", 4), ("A", 1)], [("D", 5)]],
       ("E7", 7): [[("D", 6)], [("A", 6)], [("A", 1), ("A", 5)], [("A", 2), ("A", 1), ("A", 3)],
                   [("A", 4), ("A", 2)], [("D", 5), ("A", 1)], [("E6", 6)]],
       ("E8", 8): [[("D", 7)], [("A", 7)], [("A", 1), ("A", 6)], [("A", 2), ("A", 1), ("A", 4)],
                   [("A", 4), ("A", 3)], [("D", 5), ("A", 2)], [("E6", 6), ("A", 1)], [("E7", 7)]]}


def classical_levis(t, n):
    out = []
    for k in range(1, n + 1):
        left = [("A", k - 1)] if k >= 2 else []
        r = n - k
        if t == "A":
            right = [("A", r)] if r >= 1 else []
        elif t in ("B", "C"):
            right = [(t, r)] if r >= 1 else []
        else:
            if k <= n - 2:
                right = [("D", r)]
            else:
                left, right = [("A", n - 1)], []
        out.append(left + right)
    return out


def untwisted_levis(t, n):
    return EXC[(t, n)] if (t, n) in EXC else classical_levis(t, n)


def untwisted_indices(t, n):
    w = poincare([(t, n)])
    return [exactdiv(w, poincare(j) if j else [1]) for j in untwisted_levis(t, n)]


def su(m):
    return prod([xm(c, (-1) ** c) for c in range(2, m + 1)])


def levi_2a(m, k):
    if 2 * k < m:
        return pmul(prod([xm(2 * c, 1) for c in range(1, k + 1)]), su(m - 2 * k))
    return pmul(xm(1, 1), prod([xm(2 * c, 1) for c in range(2, k + 1)]))


def ominus(r):
    return pmul(xm(r, -1), prod([xm(2 * c, 1) for c in range(1, r)]))


def levi_2d(n, k):
    if k <= n - 2:
        return prod([xm(1, 1), prod([xm(c, 1) for c in range(2, k + 1)]), ominus(n - k)])
    return pmul(xm(2, 1), prod([xm(c, 1) for c in range(2, n)]))


def twisted_cases():
    x8 = exactdiv(xm(12, 1), xm(4, 1))
    cases = [("3D4", 12, prod([xm(2, 1), x8, xm(6, 1)]),
              [pmul(xm(2, 1), xm(3, 1)), pmul(xm(6, 1), xm(1, 1))]),
             ("2E6", 18, prod([xm(2, 1), xm(5, -1), xm(6, 1), xm(8, 1), xm(9, -1), xm(12, 1)]),
              [prod([xm(1, 1), xm(2, 1), xm(3, -1), xm(4, 1), xm(5, -1), xm(6, 1)]),
               prod([xm(1, 1), xm(2, 1), xm(4, 1), xm(6, 1)]),
               prod([xm(1, 1), xm(1, -1), xm(4, 1), xm(2, 1), xm(3, 1)]),
               prod([xm(1, 1), xm(1, -1), xm(2, 1), xm(4, 1), xm(4, -1), xm(6, 1)])]),
             ("2F4", 12, prod([xm(6, -1), xm(4, 1), xm(3, -1), xm(1, 1)]),
              [prod([xm(2, -1), xm(1, 1), xm(1, 1)]), pmul(xm(2, 1), xm(1, 1))]),
             ("2B2", 4, pmul(xm(2, -1), xm(1, 1)), [xm(1, 1)]),
             ("2G2", 6, pmul(xm(3, -1), xm(1, 1)), [xm(1, 1)])]
    for m in range(3, 21):
        e = 2 * m if m % 2 else 2 * (m - 1)
        cases.append((f"2A{m - 1}", e, su(m), [levi_2a(m, k) for k in range(1, m // 2 + 1)]))
    for n in range(4, 17):
        cases.append((f"2D{n}", 2 * n, ominus(n), [levi_2d(n, k) for k in range(1, n)]))
    return cases


def is_prime_power(q):
    if q < 2:
        return False
    p = 2
    while p * p <= q:
        if q % p == 0:
            while q % p == 0:
                q //= p
            return q == 1
        p += 1
    return True


def main():
    count = 0
    for key in EXC:
        h = COX[key[0]](key[1])
        for idx in untwisted_indices(*key):
            if not divides(list(cyclo(h)), idx):
                raise SystemExit(f"FAIL untwisted {key}")
            count += 1
    for t, rng in (("A", range(1, 21)), ("B", range(2, 16)), ("C", range(2, 16)), ("D", range(4, 16))):
        for n in rng:
            h = COX[t](n)
            for idx in untwisted_indices(t, n):
                if not divides(list(cyclo(h)), idx):
                    raise SystemExit(f"FAIL untwisted {(t, n)}")
                count += 1
    print(f"PASS untwisted: {count} maximal-parabolic index polynomials divisible by Phi_h")
    tcount = 0
    for name, e, g, levis in twisted_cases():
        if not divides(list(cyclo(e)), g):
            raise SystemExit(f"FAIL {name}: Phi_e does not divide |G|_p'")
        for lev in levis:
            if not divides(list(cyclo(e)), exactdiv(g, lev)):
                raise SystemExit(f"FAIL twisted {name}")
            tcount += 1
    print(f"PASS twisted: {tcount} maximal-parabolic index polynomials divisible by Phi_e")
    es = set()
    for t, rng in (("A", range(1, 60)), ("B", range(2, 60)), ("C", range(2, 60)), ("D", range(4, 60))):
        es |= {COX[t](n) for n in rng}
    es |= {12, 18, 30, 6, 4} | {2 * m if m % 2 else 2 * (m - 1) for m in range(3, 60)} | {2 * n for n in range(4, 60)}
    hits = sorted((e, q) for e in es for q in range(2, 2000) if is_prime_power(q) and peval(list(cyclo(e)), q) in (1, 7))
    print("Phi_e(q) in {1,7} exactly for", hits)
    if hits != [(3, 2), (6, 3)]:
        raise SystemExit("FAIL exception list")
    groups = {"PSL6(3)": untwisted_indices("A", 5), "Omega7(3)": untwisted_indices("B", 3),
              "PSp6(3)": untwisted_indices("C", 3), "POmega8+(3)": untwisted_indices("D", 4),
              "G2(3)": untwisted_indices("G2", 2),
              "PSU3(3)": [exactdiv(su(3), levi_2a(3, 1))],
              "PSU4(3)": [exactdiv(su(4), levi_2a(4, k)) for k in (1, 2)]}
    for name, polys in groups.items():
        vals = [peval(f, 3) for f in polys]
        gs = sorted({gcd(a, b) for a in vals for b in vals})
        if any(7 % g == 0 for g in gs):
            raise SystemExit(f"FAIL {name}")
        print(f"{name}: indices {vals}; pairwise gcds {gs}; none divides 7")
    print("PASS all checks")


if __name__ == "__main__":
    main()
