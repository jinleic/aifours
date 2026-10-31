#!/usr/bin/env python3
"""Check a replacement integer polynomial identity for cited grid minors."""
import argparse
import importlib.util
import json
from pathlib import Path
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("ring_implementation", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    spec = importlib.util.spec_from_file_location("poly", args.ring_implementation)
    poly = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(poly)
    add, neg, mul = poly.add, poly.neg, poly.mul
    a,b,c,d,e = ({tuple(1 if i==j else 0 for i in range(5)):1} for j in range(5))
    a2, bd = mul(a,a), mul(b,d)
    g1 = mul(e,add(a2,neg(bd)))
    g2 = mul(c,add(a2,bd))
    g3 = mul(e,add(mul(b,b),neg(mul(a,c))))
    g4 = neg(mul(c,add(mul(d,d),mul(a,e))))
    g5 = add(mul(a,mul(a,a)),mul(mul(b,b),e),neg(mul(mul(d,d),c)),neg(mul(mul(a,c),e)))
    term = mul(a,add(g5,neg(g3),neg(g4)))
    lhs = add(term,term,neg(mul(c,g1)),neg(mul(e,g2)))
    a4 = mul(a,mul(a,mul(a,a)))
    rhs = add(a4,a4)
    residual = add(lhs,neg(rhs))
    if residual:
        raise ValueError(f"corrected polynomial identity fails: {residual}")
    result = {"identity": "2*a*(g5-g3-g4)-c*g1-e*g2 = 2*a^4",
              "residual_polynomial": residual,
              "domain": "integer polynomial ring Z[a,b,c,d,e]",
              "consequence_scope": "over characteristic not 2, simultaneous g1=...=g5=0 implies a=0",
              "limitations": "Does not independently establish the projected-state claims; mathematical review remains separate."}
    with args.output.open("x", encoding="utf-8") as out:
        json.dump(result,out,indent=2)
        out.write("\n")
    json.dump(result,sys.stdout,indent=2)
    print()


if __name__ == "__main__":
    main()
