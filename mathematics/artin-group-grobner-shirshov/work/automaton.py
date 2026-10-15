"""Exact finite automata for the normal forms and for the leading words of the
reduced deg-lex Groebner-Shirshov basis of a finite-type Artin group in the
Artin-Garside generators (positive part), built directly from W.

Theory (proof.md, Lemmas 3-4): a positive word v_1..v_L is a normal form
(deg-lex-smallest representative, not divisible by Delta) iff for every k
  (L) for all t < v_k with m(t,v_k) < oo:  Pi(t,v_k) does not left-divide [v_{k+1}..v_L],
      where Pi(t,v_k) = v_k\\t is the alternating word t v_k t ... of length m(t,v_k)-1;
  (D) v_k^{-1} Delta does not left-divide [v_{k+1}..v_L].
Reading left to right we keep the antichain of pending 'obligations' (simple
elements that must not divide the rest); reading y maps c -> y\\c (right
complement) and the word dies when some obligation becomes 1.

Minimal reducible words (= leading words of the reduced GS basis restricted to
positive words) are u with u[:-1], u[1:] normal and u not normal; they are
counted with a pair automaton (full run, run started at the second letter).

Usage: python3 work/automaton.py TYPE n [--m M] [--order 0,2,1] [--L 60] [--monoid]
"""
from __future__ import annotations

import argparse
import json
import sys
from functools import lru_cache

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from coxeter import Coxeter, coxeter_matrix, letter, permute_matrix  # noqa: E402


class WTable:
    """Integer-indexed finite Coxeter group with multiplication by generators."""

    def __init__(self, W: Coxeter, limit: int = 200000):
        self.W = W
        n = self.n = W.n
        elems = [W.e]
        idx = {W.e: 0}
        frontier = [W.e]
        while frontier:
            new = []
            for w in frontier:
                for i in range(n):
                    v = W.rmul(w, i)
                    if v not in idx:
                        idx[v] = len(elems)
                        elems.append(v)
                        new.append(v)
                        if len(elems) > limit:
                            raise ValueError("group too large for tables")
            frontier = new
        self.size = len(elems)
        self.rmul = [[idx[W.rmul(w, i)] for i in range(n)] for w in elems]
        self.lmul = [[idx[W.lmul(i, w)] for w in elems] for i in range(n)]
        pos = W.positive
        posidx = [k for k in range(W.nroots) if pos[k]]
        self.length = []
        self.ld = []
        self.rd = []
        self.inv = []  # left inversion set bitmask: {alpha>0 : w^{-1} alpha < 0}
        for w in elems:
            wi = W.inv(w)
            self.length.append(sum(1 for k in posidx if not pos[w[k]]))
            self.rd.append(sum(1 << i for i in range(n) if not pos[w[W.sidx[i]]]))
            self.ld.append(sum(1 << i for i in range(n) if not pos[wi[W.sidx[i]]]))
            bits = 0
            for b, k in enumerate(posidx):
                if not pos[wi[k]]:
                    bits |= 1 << b
            self.inv.append(bits)
        self.e = 0
        self.w0 = idx[W.w0]
        self.gen = [idx[W.gen[i]] for i in range(n)]
        self.phi = W.phi
        self.M = W.M
        self._join = {}

    def leq(self, a: int, b: int) -> bool:
        """a <= b in the prefix (right weak) order = left divisibility of simples."""
        ia = self.inv[a]
        return ia & self.inv[b] == ia

    def word_elem(self, letters: list[int]) -> int:
        w = self.e
        for i in letters:
            w = self.rmul[w][i]
        return w

    def alt(self, s: int, t: int, k: int) -> int:
        return self.word_elem([s if j % 2 == 0 else t for j in range(k)])

    def join(self, a: int, b: int) -> int:
        if self.leq(a, b):
            return b
        if self.leq(b, a):
            return a
        key = (a, b)
        r = self._join.get(key)
        if r is not None:
            return r
        lda, ldb = self.ld[a], self.ld[b]
        common = lda & ldb
        if common:
            s = (common & -common).bit_length() - 1
            r = self.lmul[s][self.join(self.lmul[s][a], self.lmul[s][b])]
        else:
            s = (lda & -lda).bit_length() - 1
            t = (ldb & -ldb).bit_length() - 1
            # s v t: Delta_{st} = t * Pi_{m-1}(s,t); s v b = t * (Pi_{m-1}(s,t) v t^{-1}b)
            m = self.M[s][t]
            pst = self.alt(s, t, m - 1)
            sb = self.lmul[t][self.join(pst, self.lmul[t][b])]
            r = self.join(a, sb)
        self._join[key] = r
        return r

    def complement(self, y: int, c: int) -> int:
        """y\\c = y^{-1} (y v c) for an atom y and a simple element c."""
        if (self.ld[c] >> y) & 1:
            return self.lmul[y][c]
        return self.lmul[y][self.join(self.gen[y], c)]


class NFAutomaton:
    def __init__(self, T: WTable, monoid: bool = False):
        if T.W.N < 2:
            raise ValueError("Theorem B automaton needs N >= 2 (type A1 is treated by hand)")
        self.T = T
        self.monoid = monoid
        n = T.n
        # obligations created when reading letter y
        self.created = []
        for y in range(n):
            obs = set()
            for t in range(y):
                m = T.M[t][y]
                obs.add(T.alt(t, y, m - 1))
            if not monoid:
                obs.add(T.lmul[y][T.w0])
            self.created.append(frozenset(obs))
        self._trans = {}

    def minimal(self, S) -> frozenset:
        T = self.T
        S = list(S)
        out = [c for c in S if not any(d != c and T.leq(d, c) for d in S)]
        return frozenset(out)

    def step(self, O: frozenset, y: int):
        """Return the next state, or None if the word dies."""
        key = (O, y)
        r = self._trans.get(key, 0)
        if r != 0:
            return r
        T = self.T
        new = set(self.created[y])
        dead = False
        for c in O:
            d = T.complement(y, c)
            if d == T.e:
                dead = True
                break
            new.add(d)
        r = None if dead else self.minimal(new)
        self._trans[key] = r
        return r

    def count_nf(self, L: int) -> list[int]:
        cur = {frozenset(): 1}
        counts = [1]
        for _ in range(L):
            nxt = {}
            for O, k in cur.items():
                for y in range(self.T.n):
                    O2 = self.step(O, y)
                    if O2 is not None:
                        nxt[O2] = nxt.get(O2, 0) + k
            cur = nxt
            counts.append(sum(cur.values()))
        return counts, len(self._states_seen(cur))

    def _states_seen(self, cur):
        return {O for (O, _y), v in self._trans.items()} | set(cur)

    def count_minred(self, L: int) -> list[int]:
        """Number of minimal reducible positive words of each length <= L."""
        n = self.T.n
        counts = [0, 0]
        cur = {}
        for y in range(n):
            O1 = self.step(frozenset(), y)
            if O1 is not None:
                key = (O1, frozenset())
                cur[key] = cur.get(key, 0) + 1
        for _ in range(2, L + 1):
            nxt = {}
            c = 0
            for (Of, Os), k in cur.items():
                for y in range(n):
                    Os2 = self.step(Os, y)
                    if Os2 is None:
                        continue
                    Of2 = self.step(Of, y)
                    if Of2 is None:
                        c += k
                    else:
                        key = (Of2, Os2)
                        nxt[key] = nxt.get(key, 0) + k
            counts.append(c)
            cur = nxt
        return counts, len(cur)

    def minred_words(self, L: int):
        """Enumerate minimal reducible positive words of length <= L."""
        n = self.T.n
        out = []
        stack = []
        for y in range(n):
            O1 = self.step(frozenset(), y)
            if O1 is not None:
                stack.append((letter(y), O1, frozenset()))
        while stack:
            w, Of, Os = stack.pop()
            if len(w) >= L:
                continue
            for y in range(n):
                Os2 = self.step(Os, y)
                if Os2 is None:
                    continue
                Of2 = self.step(Of, y)
                if Of2 is None:
                    out.append(w + letter(y))
                else:
                    stack.append((w + letter(y), Of2, Os2))
        return sorted(out, key=lambda u: (len(u), u))


def build_table(typ, n=0, m=0, order=None) -> WTable:
    M = coxeter_matrix(typ, n, m)
    if order is not None:
        M = permute_matrix(M, order)
    return WTable(Coxeter(M))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("typ")
    ap.add_argument("n", type=int)
    ap.add_argument("--m", type=int, default=0)
    ap.add_argument("--order", default=None)
    ap.add_argument("--L", type=int, default=40)
    ap.add_argument("--monoid", action="store_true")
    a = ap.parse_args()
    order = [int(x) for x in a.order.split(",")] if a.order else None
    T = build_table(a.typ, a.n, a.m, order)
    A = NFAutomaton(T, monoid=a.monoid)
    nf, _ = A.count_nf(a.L)
    mr, pairs = A.count_minred(a.L)
    states = {O for (O, _y) in A._trans} | {v for v in A._trans.values() if v is not None}
    print(json.dumps({"type": a.typ, "n": a.n, "m": a.m, "order": order, "monoid": a.monoid,
                      "W": T.size, "nf_counts": nf, "minred_counts": mr,
                      "nf_states": len(states), "pair_states_at_L": pairs}))


if __name__ == "__main__":
    main()
