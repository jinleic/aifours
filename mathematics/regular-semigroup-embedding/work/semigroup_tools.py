"""Shared finite-semigroup utilities (pure Python, no dependencies).

A finite semigroup is a list-of-lists multiplication table T with T[x][y] = xy on {0..N-1}.
"""
from __future__ import annotations

import itertools


def is_associative(T) -> bool:
    N = len(T)
    return all(T[T[x][y]][z] == T[x][T[y][z]] for x in range(N) for y in range(N) for z in range(N))


def idempotents(T) -> list[int]:
    return [x for x in range(len(T)) if T[x][x] == x]


def inverses(T, x) -> list[int]:
    N = len(T)
    return [y for y in range(N) if T[T[x][y]][x] == x and T[T[y][x]][y] == y]


def is_regular(T) -> bool:
    return all(inverses(T, x) for x in range(len(T)))


def is_band(T, elems=None) -> bool:
    elems = range(len(T)) if elems is None else elems
    return all(T[x][x] == x for x in elems) and all(T[x][y] in set(elems) for x in elems for y in elems)


def prod(T, *xs) -> int:
    v = xs[0]
    for x in xs[1:]:
        v = T[v][x]
    return v


def band_is_regular(T, elems) -> tuple[bool, tuple | None]:
    """regular band identity a x y a = a x a y a on the subband elems; returns (ok, witness)."""
    for a, x, y in itertools.product(elems, repeat=3):
        if prod(T, a, x, y, a) != prod(T, a, x, a, y, a):
            return False, (a, x, y)
    return True, None


def local_submonoid(T, e, elems) -> list[int]:
    return sorted({prod(T, e, x, e) for x in elems})


def band_is_locally_regular(T, elems) -> tuple[bool, tuple | None]:
    """every local submonoid eBe (e in elems) is a regular band."""
    for e in elems:
        loc = local_submonoid(T, e, elems)
        ok, w = band_is_regular(T, loc)
        if not ok:
            return False, (e, w)
    return True, None


def nat_leq(T, a, b, E) -> bool:
    """natural partial order of a regular semigroup: a = e b = b f for idempotents e, f."""
    return any(T[e][b] == a for e in E) and any(T[b][f] == a for f in E)


def is_weakly_E_unitary(T) -> bool:
    E = set(idempotents(T))
    N = len(T)
    return all(a in E for a in range(N) for e in E if nat_leq(T, e, a, E))


def is_E_unitary(T) -> bool:
    E = set(idempotents(T))
    N = len(T)
    for e in E:
        for a in range(N):
            if (T[e][a] in E or T[a][e] in E) and a not in E:
                return False
    return True


def is_orthodox(T) -> bool:
    E = idempotents(T)
    return is_regular(T) and all(T[e][f] in set(E) for e in E for f in E)


def is_locally_r_orthodox(T) -> tuple[bool, str]:
    """for every idempotent e: eSe orthodox (E(eSe) a subsemigroup) and E(eSe) a regular band."""
    N = len(T)
    E = idempotents(T)
    if not is_regular(T):
        return False, "not regular"
    for e in E:
        loc = sorted({prod(T, e, x, e) for x in range(N)})
        Eloc = [x for x in loc if T[x][x] == x]
        if not all(T[a][b] in set(Eloc) for a in Eloc for b in Eloc):
            return False, f"eSe not orthodox at e={e}"
        ok, w = band_is_regular(T, Eloc)
        if not ok:
            return False, f"E(eSe) not regular at e={e}, witness {w}"
    return True, "ok"


def min_group_congruence_classes(T):
    """least group congruence sigma for a finite E-unitary orthodox semigroup:
    a sigma b iff e a f = e b f for some idempotents e, f  (valid for orthodox semigroups).
    Returned as a list of classes (we verify it is a congruence with group quotient)."""
    N = len(T)
    E = idempotents(T)
    rel = [[any(prod(T, e, a, f) == prod(T, e, b, f) for e in E for f in E) for b in range(N)] for a in range(N)]
    classes = []
    seen = set()
    for a in range(N):
        if a in seen:
            continue
        cls = [b for b in range(N) if rel[a][b]]
        classes.append(cls)
        seen.update(cls)
    return classes, rel
