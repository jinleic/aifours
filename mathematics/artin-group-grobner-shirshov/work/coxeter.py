"""Finite Coxeter groups as permutation groups on their root systems, and the
Garside structure of the associated Artin monoid / Artin group.

Independent of any rewriting system: elements of W are permutations of the
root system (computed numerically from the Tits bilinear form and identified
by rounding), and positive Artin-monoid elements are kept in left-greedy
(Garside) normal form, i.e. a list of simple elements (= elements of W).

Letters: generator i (0-based, i < n) is written chr(ord('a') + i); the
Garside element Delta is '1' and Delta^{-1} is '0'.  Python string order
'0' < '1' < 'a' < 'b' < ... is the letter order Delta^{-1} < Delta < s_1 < s_2 < ...
used by Bokut (arXiv:0806.1125); deg-lex = compare (len, string).
"""
from __future__ import annotations

import math
from functools import lru_cache

DINV, DELTA = "0", "1"


def letter(i: int) -> str:
    return chr(ord("a") + i)


def index(c: str) -> int:
    return ord(c) - ord("a")


# ---------------------------------------------------------------- Coxeter data
def coxeter_matrix(typ: str, n: int = 0, m: int = 0) -> list[list[int]]:
    """Coxeter matrix with Bourbaki numbering (node k -> row k-1)."""
    def chain(k: int) -> list[list[int]]:
        M = [[2] * k for _ in range(k)]
        for i in range(k):
            M[i][i] = 1
        for i in range(k - 1):
            M[i][i + 1] = M[i + 1][i] = 3
        return M

    if typ == "A":
        return chain(n)
    if typ == "B":  # s1 - s2 - ... - s_{n-1} =4= s_n
        M = chain(n)
        M[n - 2][n - 1] = M[n - 1][n - 2] = 4
        return M
    if typ == "D":  # chain s1..s_{n-1}, and s_n joined to s_{n-2}
        M = chain(n)
        M[n - 2][n - 1] = M[n - 1][n - 2] = 2
        M[n - 3][n - 1] = M[n - 1][n - 3] = 3
        return M
    if typ == "E":  # 1-3-4-5-6(-7-8), 2-4
        M = [[2] * n for _ in range(n)]
        for i in range(n):
            M[i][i] = 1
        edges = [(1, 3), (3, 4), (4, 5), (5, 6), (2, 4)] + [(k, k + 1) for k in range(6, n)]
        for i, j in edges:
            M[i - 1][j - 1] = M[j - 1][i - 1] = 3
        return M
    if typ == "F":  # 1 - 2 =4= 3 - 4
        M = chain(4)
        M[1][2] = M[2][1] = 4
        return M
    if typ == "H":  # 1 =5= 2 - 3 (- 4)
        M = chain(n)
        M[0][1] = M[1][0] = 5
        return M
    if typ == "I":
        return [[1, m], [m, 1]]
    raise ValueError(typ)


def permute_matrix(M: list[list[int]], order: list[int]) -> list[list[int]]:
    """Relabel: new generator k is old generator order[k]."""
    return [[M[order[i]][order[j]] for j in range(len(M))] for i in range(len(M))]


# ---------------------------------------------------------------- Coxeter group
class Coxeter:
    """Finite Coxeter group W acting on its root system by permutations."""

    def __init__(self, M: list[list[int]]):
        self.M = M
        n = self.n = len(M)
        B = [[1.0 if i == j else -math.cos(math.pi / M[i][j]) for j in range(n)] for i in range(n)]

        def refl(i: int, v: tuple[float, ...]) -> tuple[float, ...]:
            c = 2.0 * sum(B[i][j] * v[j] for j in range(n))
            return tuple(v[j] - (c if j == i else 0.0) for j in range(n))

        def key(v):
            return tuple(round(x, 7) + 0.0 for x in v)

        simple = [tuple(1.0 if j == i else 0.0 for j in range(n)) for i in range(n)]
        roots, idx = [], {}
        frontier = []
        for v in simple:
            k = key(v)
            if k not in idx:
                idx[k] = len(roots)
                roots.append(v)
                frontier.append(v)
        while frontier:
            new = []
            for v in frontier:
                for i in range(n):
                    w = refl(i, v)
                    k = key(w)
                    if k not in idx:
                        if len(roots) > 100000:
                            raise ValueError("infinite or too large Coxeter group")
                        idx[k] = len(roots)
                        roots.append(w)
                        new.append(w)
            frontier = new
        self.roots = roots
        self.nroots = len(roots)
        self.positive = [all(x > -1e-9 for x in v) for v in roots]
        assert all(self.positive[k] != all(x < 1e-9 for x in roots[k]) for k in range(len(roots)))
        self.N = sum(self.positive)  # number of positive roots = l(w0)
        self.gen = [tuple(idx[key(refl(i, v))] for v in roots) for i in range(n)]
        self.sidx = [idx[key(v)] for v in simple]
        self.e = tuple(range(self.nroots))
        # longest element: product of generators until no ascent
        w = self.e
        while True:
            asc = [i for i in range(n) if i not in self.rdesc(w)]
            if not asc:
                break
            w = self.rmul(w, asc[0])
        self.w0 = w
        assert self.length(w) == self.N
        # diagram automorphism phi: w0 s_i w0 = s_phi(i)
        self.phi = []
        for i in range(n):
            c = self.mul(self.mul(self.w0, self.gen[i]), self.w0)
            self.phi.append(self.gen.index(c))

    # permutations: p[k] = index of w(root_k)
    def mul(self, p, q):  # (pq)(r) = p(q(r))
        return tuple(p[k] for k in q)

    def rmul(self, w, i):  # w s_i
        g = self.gen[i]
        return tuple(w[k] for k in g)

    def lmul(self, i, w):  # s_i w
        g = self.gen[i]
        return tuple(g[k] for k in w)

    def inv(self, w):
        r = [0] * len(w)
        for k, v in enumerate(w):
            r[v] = k
        return tuple(r)

    def rdesc(self, w) -> frozenset[int]:
        pos = self.positive
        return frozenset(i for i in range(self.n) if not pos[w[self.sidx[i]]])

    def ldesc(self, w) -> frozenset[int]:
        return self.rdesc(self.inv(w))

    def length(self, w) -> int:
        pos = self.positive
        return sum(1 for k in range(self.nroots) if pos[k] and not pos[w[k]])

    def conj_w0(self, w):
        return self.mul(self.mul(self.w0, w), self.w0)


# ---------------------------------------------------------------- Garside normal form
class Garside:
    """Positive elements of the Artin monoid as left-greedy normal forms
    (lists of non-trivial simple elements), and the Artin group as pairs
    (k, F) meaning Delta^k * F with F not divisible by Delta."""

    def __init__(self, W: Coxeter):
        self.W = W
        self._ldesc = {}
        self._rdesc = {}

    def ld(self, w):
        r = self._ldesc.get(w)
        if r is None:
            r = self._ldesc[w] = self.W.ldesc(w)
        return r

    def rd(self, w):
        r = self._rdesc.get(w)
        if r is None:
            r = self._rdesc[w] = self.W.rdesc(w)
        return r

    def normalize(self, F: list) -> list:
        """Left-greedy normal form of a product of simple elements."""
        W = self.W
        F = [f for f in F if f != W.e]
        changed = True
        while changed:
            changed = False
            for j in range(len(F) - 1):
                a, b = F[j], F[j + 1]
                while True:
                    move = self.ld(b) - self.rd(a)
                    if not move:
                        break
                    s = min(move)
                    a = W.rmul(a, s)
                    b = W.lmul(s, b)
                    changed = True
                F[j], F[j + 1] = a, b
            if changed:
                F = [f for f in F if f != W.e]
        return F

    def times_atom(self, F: list, i: int) -> list:
        return self.normalize(F + [self.W.gen[i]])

    # ---- group elements: (k, F)
    def group_mul_letter(self, state, c: str):
        """Right multiplication by a letter: 'a'.. = s_i, '1' = Delta, '0' = Delta^{-1},
        'A'.. = s_i^{-1} (= Delta^{-1} * simple(w0 s_i))."""
        k, F = state
        W = self.W
        if c == DELTA:
            return (k + 1, [W.conj_w0(f) for f in F])
        if c == DINV:
            return (k - 1, [W.conj_w0(f) for f in F])
        if c.isupper():
            i = ord(c) - ord("A")
            F = self.normalize([W.conj_w0(f) for f in F] + [W.rmul(W.w0, i)])
            k -= 1
        else:
            F = self.times_atom(F, index(c))
        while F and F[0] == W.w0:
            F = F[1:]
            k += 1
        return (k, F)

    def group_state(self, word: str):
        st = (0, [])
        for c in word:
            st = self.group_mul_letter(st, c)
        return st

    def lexmin(self, F: list) -> str:
        """deg-lex smallest positive word for the positive element F."""
        W = self.W
        F = list(F)
        out = []
        while F:
            s = min(self.ld(F[0]))
            out.append(letter(s))
            F[0] = W.lmul(s, F[0])
            F = self.normalize(F)
        return "".join(out)

    def nf_state(self, state) -> str:
        k, F = state
        return (DELTA * k if k >= 0 else DINV * (-k)) + self.lexmin(F)

    def nf(self, word: str) -> str:
        return self.nf_state(self.group_state(word))

    def delta_word(self) -> str:
        return self.lexmin([self.W.w0])


def build(typ: str, n: int = 0, m: int = 0, order: list[int] | None = None) -> Garside:
    M = coxeter_matrix(typ, n, m)
    if order is not None:
        M = permute_matrix(M, order)
    return Garside(Coxeter(M))
