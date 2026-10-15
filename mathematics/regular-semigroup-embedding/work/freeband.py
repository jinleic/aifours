"""Free bands via the Green-Rees normal form, and verbal quotients of FB(n).

A word w over letters 0..n-1 is equal in the free band to 0(w) a(w) b(w) 1(w), where
0(w) is the longest prefix missing exactly one letter of the content, a(w) is that letter,
and dually for 1(w), b(w).  can() turns this into a canonical word, so two words are
equal in the free band iff their canonical words coincide.
"""
from __future__ import annotations

import itertools
from functools import lru_cache

import numpy as np


@lru_cache(maxsize=None)
def can(w: tuple[int, ...]) -> tuple[int, ...]:
    c = set(w)
    if len(c) <= 1:
        return w[:1]
    seen: set[int] = set()
    p = -1
    for i, ch in enumerate(w):
        if ch not in seen:
            seen.add(ch)
            if len(seen) == len(c):
                p = i
                break
    seen = set()
    q = -1
    for i in range(len(w) - 1, -1, -1):
        ch = w[i]
        if ch not in seen:
            seen.add(ch)
            if len(seen) == len(c):
                q = i
                break
    return can(w[:p]) + (w[p], w[q]) + can(w[q + 1:])


def free_band(n: int):
    """Return (elements as canonical words, index dict, multiplication table)."""
    gens = [(i,) for i in range(n)]
    elems = list(gens)
    index = {w: k for k, w in enumerate(elems)}
    frontier = list(gens)
    while frontier:
        nxt = []
        for w in frontier:
            for g in range(n):
                v = can(w + (g,))
                if v not in index:
                    index[v] = len(elems)
                    elems.append(v)
                    nxt.append(v)
        frontier = nxt
    m = len(elems)
    mult = np.empty((m, m), dtype=np.int32)
    for i, u in enumerate(elems):
        for j, v in enumerate(elems):
            mult[i, j] = index[can(u + v)]
    return elems, index, mult


class UF:
    def __init__(self, m: int):
        self.p = np.arange(m)

    def find(self, x: int) -> int:
        p = self.p
        r = x
        while p[r] != r:
            r = p[r]
        while p[x] != r:
            p[x], x = r, p[x]
        return r

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if ra < rb:
            ra, rb = rb, ra
        self.p[ra] = rb
        return True


def congruence_closure(mult: np.ndarray, gens: list[int], pairs: np.ndarray) -> np.ndarray:
    """Smallest congruence of the semigroup (mult) containing the given pairs.

    Returns an array lab with lab[x] == lab[y] iff x ~ y.  Closure under left/right
    multiplication by generators suffices because every element is a product of them.
    """
    m = mult.shape[0]
    uf = UF(m)
    queue = []
    for a, b in pairs:
        if uf.union(int(a), int(b)):
            queue.append((int(a), int(b)))
    while queue:
        a, b = queue.pop()
        for g in gens:
            for x, y in ((mult[g, a], mult[g, b]), (mult[a, g], mult[b, g])):
                if uf.union(int(x), int(y)):
                    queue.append((int(x), int(y)))
    return np.array([uf.find(x) for x in range(m)])


def word_value(mult: np.ndarray, index: dict, word: str, assign: dict) -> int:
    """Evaluate a word over variable letters using an assignment letter -> element index."""
    val = assign[word[0]]
    for ch in word[1:]:
        val = mult[val, assign[ch]]
    return int(val)


def verbal_pairs(mult: np.ndarray, lhs: str, rhs: str) -> np.ndarray:
    """All substitution instances (all variables range over all elements) of lhs = rhs."""
    m = mult.shape[0]
    vars_ = sorted(set(lhs) | set(rhs))
    out = set()
    for vals in itertools.product(range(m), repeat=len(vars_)):
        a = dict(zip(vars_, vals))
        x = word_value(mult, None, lhs, a)
        y = word_value(mult, None, rhs, a)
        if x != y:
            out.add((min(x, y), max(x, y)))
    return np.array(sorted(out), dtype=np.int64).reshape(-1, 2)
