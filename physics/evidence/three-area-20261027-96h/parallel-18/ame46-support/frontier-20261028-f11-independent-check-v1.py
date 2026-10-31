#!/usr/bin/env python3
"""Check constructed projected grid-range vectors exactly over Q(i).

This independently implements the published Eq.(11) parametrization and
performs direct Gaussian-rational rank calculations. Finite examples are
controls, not a proof of the universal complex parameter argument.
"""
import argparse
from fractions import Fraction
import itertools
import json
from pathlib import Path
import sys


class QI:
    __slots__ = ("r", "i")

    def __init__(self, r=0, i=0):
        self.r, self.i = Fraction(r), Fraction(i)

    @staticmethod
    def cast(x):
        return x if isinstance(x, QI) else QI(x)

    def __add__(self, other):
        v = self.cast(other)
        return QI(self.r+v.r, self.i+v.i)

    __radd__ = __add__

    def __neg__(self):
        return QI(-self.r, -self.i)

    def __sub__(self, other):
        return self + (-self.cast(other))

    def __rsub__(self, other):
        return self.cast(other) - self

    def __mul__(self, other):
        v = self.cast(other)
        return QI(self.r*v.r-self.i*v.i, self.r*v.i+self.i*v.r)

    __rmul__ = __mul__

    def __truediv__(self, other):
        v = self.cast(other)
        denominator = v.r*v.r + v.i*v.i
        if not denominator:
            raise ZeroDivisionError("zero Gaussian rational")
        return QI((self.r*v.r+self.i*v.i)/denominator, (self.i*v.r-self.r*v.i)/denominator)

    def __eq__(self, other):
        v = self.cast(other)
        return self.r == v.r and self.i == v.i

    def __bool__(self):
        return bool(self.r or self.i)

    def text(self):
        return f"{self.r}+({self.i})i"


def rank(rows):
    a = [[QI.cast(x) for x in row] for row in rows]
    if not a:
        return 0
    m, n = len(a), len(a[0])
    r = 0
    for c in range(n):
        p = next((k for k in range(r, m) if a[k][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        pivot = a[r][c]
        a[r] = [x/pivot for x in a[r]]
        for k in range(r+1, m):
            scale = a[k][c]
            if scale:
                a[k] = [x-scale*y for x,y in zip(a[k],a[r])]
        r += 1
        if r == m:
            break
    return r


def product(a,b):
    return [[sum((a[r][k]*b[k][c] for k in range(len(b))), QI())
             for c in range(len(b[0]))] for r in range(len(a))]


def grid(params):
    a,b,c,d,e,f,g,i,h = [QI.cast(x) for x in params]
    z = QI()
    return [[a,b,c,z,h],[d,a,b,z,z],[e,-d,a,f,z],[g,z,i,e,c]]


def kernel_basis(s):
    pivot = next(j for j,x in enumerate(s) if x)
    others = [j for j in range(5) if j != pivot]
    p = [[QI() for _ in range(4)] for _ in range(5)]
    for k,j in enumerate(others):
        p[j][k] = QI(1)
        p[pivot][k] = -s[j]/s[pivot]
    return p


def flatten(m):
    return [v for row in m for v in row]


def rank_as_vectors(vectors):
    return rank(vectors)


def case_one(s):
    u,v,w,x,y = s
    if not u and not w:
        beta, alpha, gamma = v, QI(1), QI(1)
    else:
        beta = QI(1) if v != 1 else QI(2)
        rhs = beta*(v-beta)
        if not u:
            alpha, gamma = rhs/w, QI(1)
        else:
            alpha = QI(1)
            gamma = (alpha*w-rhs)/u
            if not gamma:
                alpha = QI(2)
                gamma = (alpha*w-rhs)/u
    if not alpha or not beta or not gamma or alpha*w-gamma*u != beta*(v-beta):
        raise ValueError("bad case-one parameters")
    b, d, f, h = (w-gamma)/beta, (u-alpha)/beta, x/gamma, y/alpha
    return [QI(1),b,QI(),d,QI(),f,QI(),QI(),h], (alpha,beta,gamma)


def case_two(s, b, d):
    u,v,w,x,y = s
    if u or v or w or (not x and not y):
        raise ValueError("bad case-two normal")
    return [QI(1),b,y,d,x,QI(),QI(),QI(),QI()]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    samples = [
        ("general", [1,2,3,4,5], None),
        ("u_zero", [0,2,1,3,1], None),
        ("w_zero", [1,2,0,-1,3], None),
        ("only_v", [0,1,0,2,-1], None),
        ("complex_general", [QI(1,1),2,3,QI(0,1),QI(1,-1)], None),
        ("complex_only_v", [0,QI(0,1),0,1,1], None),
        ("last_x_nonzero", [0,0,0,1,2], (QI(1),QI())),
        ("last_x_zero", [0,0,0,0,1], (QI(),QI(1))),
        ("last_complex_root", [0,0,0,0,-1], (QI(),QI(0,1))),
    ]
    basis = []
    for j in range(9):
        v = [QI() for _ in range(9)]
        v[j] = QI(1)
        basis.append(grid(v))
    if [rank(m) for m in basis] != [3,2,2,2,2,1,1,1,1]:
        raise ValueError("unexpected source basis ranks")
    results = []
    for label, normal, roots in samples:
        s = [QI.cast(x) for x in normal]
        p = kernel_basis(s)
        if rank(p) != 4 or any(sum((s[j]*p[j][k] for j in range(5)), QI()) for k in range(4)):
            raise ValueError(f"invalid hyperplane basis {label}")
        if roots is None:
            params, weights = case_one(s)
            m = grid(params)
            for col in range(5):
                if sum((weights[r]*m[r][col] for r in range(3)), QI()) != s[col]:
                    raise ValueError(f"row-space identity failure {label}")
        else:
            params = case_two(s,*roots)
            m = grid(params)
            if m[3] != s:
                raise ValueError(f"fourth-row identity failure {label}")
        if rank(m) != 3 or rank(product(m,p)) != 2:
            raise ValueError(f"rank construction failure {label}")
        images = [flatten(product(b,p)) for b in basis]
        eight_rank = rank_as_vectors(images[1:])
        full_rank = rank_as_vectors(images)
        constructed_rank = rank_as_vectors([flatten(product(m,p))]+images[1:])
        if full_rank != eight_rank+1 or constructed_rank != full_rank:
            raise ValueError(f"functional/span failure {label}")
        if any(rank(product(b,p)) > 2 for b in basis[1:]):
            raise ValueError(f"base vector Schmidt-rank failure {label}")
        results.append({"label": label, "normal_Qi": [x.text() for x in s],
                        "P_rank": 4, "unprojected_M0_rank": 3, "projected_M0_rank": 2,
                        "projected_eight_span_rank": eight_rank, "projected_full_range_rank": full_rank,
                        "projected_constructed_span_rank": constructed_rank})
    output = {"field": "Q(i) with Fraction components", "source_basis_ranks": [rank(m) for m in basis],
              "samples": results,
              "limits": "Finite exact sample checks do not prove the universal complex construction or Schmidt number of projected states."}
    with args.output.open("x", encoding="utf-8") as out:
        json.dump(output, out, indent=2)
        out.write("\n")
    json.dump(output, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
