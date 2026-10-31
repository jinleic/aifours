#!/usr/bin/env python3
"""Exact polynomial check of the five published Eq.(12) generators/identity."""
import argparse
import json
from pathlib import Path
import sys

N = 5  # a,b,c,d,e


def add(*polys):
    out = {}
    for poly in polys:
        for k,v in poly.items():
            out[k] = out.get(k,0) + v
    return {k:v for k,v in out.items() if v}


def neg(poly):
    return {k:-v for k,v in poly.items()}


def mul(x,y):
    out = {}
    for p,a in x.items():
        for q,b in y.items():
            key = tuple(i+j for i,j in zip(p,q))
            out[key] = out.get(key,0) + a*b
    return {k:v for k,v in out.items() if v}


def val(poly, point):
    return sum(v * __import__('math').prod(x**e for x,e in zip(point,p)) for p,v in poly.items())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    a,b,c,d,e = ({tuple(1 if i==j else 0 for i in range(N)):1} for j in range(N))
    a2 = mul(a,a)
    bd = mul(b,d)
    g1 = mul(e,add(a2,neg(bd)))
    g2 = mul(c,add(a2,bd))
    g3 = mul(e,add(mul(b,b),neg(mul(a,c))))
    g4 = neg(mul(c,add(mul(d,d),mul(a,e))))
    g5 = add(mul(a,mul(a,a)),mul(mul(b,b),e),neg(mul(mul(d,d),c)),neg(mul(mul(a,c),e)))
    lhs = add(mul(a,add(g5,neg(g3),neg(g4))),neg(mul(c,g1)),mul(e,g2))
    rhs = mul(a,mul(a,mul(a,a)))
    residual = add(lhs,neg(rhs))
    expected = mul(mul(c,e),add(a2,add(bd,bd)))
    if residual != expected or not residual:
        raise ValueError(f"unexpected symbolic residual {residual}")
    one = (1,1,1,1,1)
    result = {"source": "https://arxiv.org/html/2509.07086v1#S0.E12",
              "generators": "g1=e(a²-bd), g2=c(a²+bd), g3=e(b²-ac), g4=-c(d²+ae), g5=a³+b²e-d²c-ace",
              "displayed_claim": "a(g5-g3-g4)-c*g1+e*g2 = a^4",
              "actual_residual": "c*e*(a^2+2*b*d)",
              "exact_residual_terms_abcde": [{"exponents": k,"coefficient":v} for k,v in sorted(residual.items())],
              "all_ones_control": {"lhs": val(lhs,one), "rhs": val(rhs,one), "residual": val(residual,one)},
              "scope": "The arbitrary-parameter polynomial identity is false; this is NOT a counterexample to the source's rank<=2 implication, which requires all generators zero."}
    with args.output.open("x", encoding="utf-8") as out:
        json.dump(result,out,indent=2)
        out.write("\n")
    json.dump(result,sys.stdout,indent=2)
    print()


if __name__ == "__main__":
    main()
