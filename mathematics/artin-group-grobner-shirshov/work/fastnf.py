"""Fast Garside normal form on the validated integer tables of automaton.WTable
(same algorithm as coxeter.Garside, elements of W as integers).  Used only to
speed up family extraction; certificates re-check with coxeter.Garside.

Letters: 'a'.. = s_i, 'A'.. = s_i^{-1}, '1' = Delta, '0' = Delta^{-1}.
"""
from __future__ import annotations


class FastGarside:
    def __init__(self, T):
        self.T = T
        n = T.n
        conj = [None] * T.size
        conj[T.e] = T.e
        frontier = [T.e]
        while frontier:
            nxt = []
            for w in frontier:
                for i in range(n):
                    v = T.rmul[w][i]
                    if conj[v] is None:
                        conj[v] = T.rmul[conj[w]][T.phi[i]]
                        nxt.append(v)
            frontier = nxt
        self.conj = conj
        self.w0s = [T.rmul[T.w0][i] for i in range(n)]

    def normalize(self, F):
        T = self.T
        rmul, lmul, ld, rd = T.rmul, T.lmul, T.ld, T.rd
        F = [f for f in F if f != T.e]
        changed = True
        while changed:
            changed = False
            for j in range(len(F) - 1):
                a, b = F[j], F[j + 1]
                move = ld[b] & ~rd[a]
                while move:
                    s = (move & -move).bit_length() - 1
                    a = rmul[a][s]
                    b = lmul[s][b]
                    changed = True
                    move = ld[b] & ~rd[a]
                F[j], F[j + 1] = a, b
            if changed:
                F = [f for f in F if f != T.e]
        return F

    def mul(self, state, c):
        k, F = state
        T = self.T
        if c == "1":
            return (k + 1, [self.conj[f] for f in F])
        if c == "0":
            return (k - 1, [self.conj[f] for f in F])
        if c.isupper():
            F = self.normalize([self.conj[f] for f in F] + [self.w0s[ord(c) - 65]])
            k -= 1
        else:
            F = self.normalize(F + [T.gen[ord(c) - 97]])
        while F and F[0] == T.w0:
            F = F[1:]
            k += 1
        return (k, F)

    def lexmin(self, F):
        T = self.T
        F = list(F)
        out = []
        while F:
            b = T.ld[F[0]]
            s = (b & -b).bit_length() - 1
            out.append(chr(97 + s))
            F[0] = T.lmul[s][F[0]]
            F = self.normalize(F)
        return "".join(out)

    def nf(self, word):
        st = (0, [])
        for c in word:
            st = self.mul(st, c)
        k, F = st
        return ("1" * k if k >= 0 else "0" * (-k)) + self.lexmin(F)
