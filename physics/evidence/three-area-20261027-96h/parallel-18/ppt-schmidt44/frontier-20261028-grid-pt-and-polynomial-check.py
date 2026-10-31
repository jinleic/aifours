#!/usr/bin/env python3
"""Exact rational PPT block certificate and polynomial minor identities."""
from fractions import Fraction as F
from pathlib import Path
import json
import runpy


src = runpy.run_path(str(Path(__file__).with_name("frontier-20261028-grid-state-sr2-check.py")))


def ppt_certificate():
    rho = src["state"]()
    actual = [[0 for _ in range(20)] for _ in range(20)]
    for a in range(4):
        for b in range(5):
            for c in range(4):
                for d in range(5):
                    actual[5*a+d][5*c+b] = rho[5*a+b][5*c+d]
    proposed = [[F(0) for _ in range(20)] for _ in range(20)]
    terms = [
        (1, src["ket"]((0, 1, 1), (1, 0, 1))),
        (1, src["ket"]((1, 2, 1), (2, 1, 1))),
        (F(1, 3), src["ket"]((0, 2, 3), (1, 1, 1), (2, 0, 1))),
        (F(2, 3), src["ket"]((1, 1, 1), (2, 0, -2))),
        (3, src["ket"]((0, 4, 1), (3, 2, 1))),
        (3, src["ket"]((2, 3, 1), (3, 0, 1))),
        (1, src["ket"]((0, 0, 1))), (1, src["ket"]((2, 2, 1))),
        (3, src["ket"]((3, 3, 1))), (3, src["ket"]((3, 4, 1))),
    ]
    for weight, v in terms:
        src["add_outer"](proposed, weight, v)
    mismatches = [(i, j) for i in range(20) for j in range(20)
                  if actual[i][j] != proposed[i][j]]
    if mismatches:
        raise AssertionError({"PPT_certificate_mismatches": mismatches})
    return {"checked_entries": 400, "projector_terms": len(terms), "mismatches": 0}


NAMES = ("a", "b", "c", "d", "e", "f", "g", "i", "h")


def clean(p):
    return {k: v for k, v in p.items() if v}


def add(p, q):
    d = dict(p)
    for k, v in q.items():
        d[k] = d.get(k, 0) + v
    return clean(d)


def scale(p, n):
    return clean({k: n*v for k,v in p.items()})


def mul(p, q):
    out = {}
    for a, x in p.items():
        for b, y in q.items():
            m = tuple(i+j for i,j in zip(a,b))
            out[m] = out.get(m,0) + x*y
    return clean(out)


def minor(m, rows, cols):
    a,b,c = rows
    x,y,z = cols
    return add(add(mul(m[a][x], add(mul(m[b][y],m[c][z]),scale(mul(m[b][z],m[c][y]),-1))),
                   scale(mul(m[a][y], add(mul(m[b][x],m[c][z]),scale(mul(m[b][z],m[c][x]),-1))),-1)),
               mul(m[a][z], add(mul(m[b][x],m[c][y]),scale(mul(m[b][y],m[c][x]),-1))))


def poly_text(p):
    return [{"coefficient": v, "powers": {NAMES[i]: e for i,e in enumerate(k) if e}}
            for k,v in sorted(p.items())]


def polynomial_certificate():
    v = []
    for i in range(len(NAMES)):
        powers = tuple(int(i==j) for j in range(len(NAMES)))
        v.append({powers:1})
    a,b,c,d,e,f,g,i,h = v
    m = [[a,b,c,{},h],[d,a,b,{},{}],[e,scale(d,-1),a,f,{}],[g,{},i,e,c]]
    g1=minor(m,(0,1,3),(0,1,3))
    g2=minor(m,(1,2,3),(1,2,4))
    g3=minor(m,(0,1,3),(1,2,3))
    g4=minor(m,(1,2,3),(0,1,4))
    g5=minor(m,(0,1,2),(0,1,2))
    a4=mul(mul(a,a),mul(a,a))
    bracket=add(add(g5,scale(g3,-1)),scale(g4,-1))
    old=add(add(mul(a,bracket),scale(mul(c,g1),-1)),mul(e,g2))
    fixed=add(add(scale(mul(a,bracket),2),scale(mul(c,g1),-1)),scale(mul(e,g2),-1))
    residual=add(old,scale(a4,-1))
    wanted=add(mul(mul(mul(a,a),c),e),scale(mul(mul(mul(b,c),d),e),2))
    if residual != wanted or add(fixed,scale(a4,-2)):
        raise AssertionError("unexpected symbolic identity")
    return {"minors_checked":5, "published_lhs_minus_rhs":poly_text(residual),
            "corrected_lhs_minus_rhs":poly_text(add(fixed,scale(a4,-2)))}


print(json.dumps({"ppt_projector_certificate":ppt_certificate(),
                  "source_polynomial":polynomial_certificate()}, indent=2))
