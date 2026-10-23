#!/usr/bin/env python3
"""k1_phase_cert.py: exact checker (stdlib only) for the phase contradiction refuting the unique non-classical K1
support pattern on the Desarguesian equianharmonic 4-net (class 6 of evidence/nets7_classes.json). Lane moqls7-maximum.

Statement checked: in the weight-4 pattern (every point p off the frame line has support exactly its allowed set
A(p), all 4 coefficients nonzero), the seven listed collinear pairs (p,q) have supports meeting in exactly two
coordinates {k,k'}. Orthogonality conj(c_pk) c_qk + conj(c_pk') c_qk' = 0 with nonzero coefficients gives the
phase relation (arg c_qk' - arg c_pk') - (arg c_qk - arg c_pk) = pi (mod 2 pi), i.e. an integer row vector r with
r . theta = 1/2 (mod 1) where theta = arg/(2 pi). The signed sum of the seven rows is the zero vector while the
right-hand sides add to (odd)/2, a contradiction 0 = 1/2 (mod 1).
Usage: /usr/bin/python3 k1_phase_cert.py CLASSFILE K1A_SUMMARY CERT_OUT
"""
import json
import sys

PAIRS = [  # (sign, p, q) with point index = position in the class-6 net list
    (+1, 29, 28), (-1, 33, 28), (+1, 34, 28), (-1, 34, 29), (+1, 33, 26), (+1, 34, 26), (-1, 29, 26)]


def main(classfile, summary, out):
    net = [tuple(q) for q in json.load(open(classfile))["classes"][6]["net"]]
    assert json.load(open(classfile))["classes"][6]["origin"] == "desarguesian-equianharmonic"
    frame = [p for p in range(49) if net[p][0] == 0]
    lab = {p: net[p][1] for p in frame}
    A = {}
    for p in range(49):
        if p in lab:
            A[p] = {lab[p]}
        else:
            bad = {lab[q] for c in (1, 2, 3) for q in frame if net[q][c] == net[p][c]}
            assert len(bad) == 3
            A[p] = set(range(7)) - bad
    # the unique non-classical model of the K1A enumeration must be exactly the weight-4 pattern
    cls6 = json.load(open(summary))["classes"][6]
    nonclassical = [m for m, w in zip(cls6["models"], cls6["model_weight_sets"]) if w != [1]]
    assert len(nonclassical) == 1
    supp = {}
    for s in nonclassical[0]:
        p, k = map(int, s.split(":"))
        supp.setdefault(p, set()).add(k)
    for p in range(49):
        assert supp[p] == A[p], p
        assert len(A[p]) == (1 if p in lab else 4)
    total = {}
    half_sum = 0
    rows = []
    for sign, p, q in PAIRS:
        assert p not in lab and q not in lab
        shared = [c for c in range(4) if net[p][c] == net[q][c]]
        assert len(shared) == 1, (p, q, shared)            # collinear (exactly one common line)
        ov = sorted(A[p] & A[q])
        assert len(ov) == 2, (p, q, ov)
        k, k2 = ov
        r = {(q, k2): 1, (p, k2): -1, (q, k): -1, (p, k): 1}
        rows.append({"sign": sign, "p": p, "q": q, "class_of_common_line": shared[0], "overlap": ov})
        for v, c in r.items():
            total[v] = total.get(v, 0) + sign * c
        half_sum += sign            # each right-hand side is 1/2
    assert all(c == 0 for c in total.values())
    assert half_sum % 2 == 1
    cert = {"net_class": 6, "rows": rows, "signed_sum_of_rows": "zero vector",
            "signed_sum_of_rhs": "%d/2 (odd numerator)" % half_sum, "conclusion": "0 = 1/2 mod 1: contradiction"}
    json.dump(cert, open(out, "w"), indent=1)
    print("PHASE CERTIFICATE OK", json.dumps(cert["rows"]))


if __name__ == "__main__":
    main(*sys.argv[1:4])
