#!/usr/bin/env python3
"""Exact-arithmetic check of the explicit 4x5 PPT detector and its written bounds.

The actual 2-block-positivity argument is in the accompanying JSON; this program
checks its source polynomial identity, integer witness construction, PPT source,
negative pairing, and every numerical inequality used in the argument.  It is
not a proof-assistant kernel and does not search or certify the 4x4 target.
"""
from contextlib import redirect_stdout
from fractions import Fraction as F
from io import StringIO
from pathlib import Path
import json
import runpy

here = Path(__file__).resolve().parent
with redirect_stdout(StringIO()):
    src = runpy.run_path(str(here / "frontier-20261029-kg45-source-check.py"))
vecs = src["vecs"]
rho = src["rho"]
N = len(rho)
assert N == 20 and len(vecs) == 9
assert src["r_rho"] == 9 and src["r_pt"] == 10
assert src["identity"] == {(4, 0, 0, 0, 0, 0, 0, 0, 0): 1}

def outer(v):
    return [[F(v[i] * v[j]) for j in range(N)] for i in range(N)]

def trprod(a, b):
    return sum(a[i][j] * b[j][i] for i in range(N) for j in range(N))

for i, v in enumerate(vecs):
    for j, u in enumerate(vecs):
        assert sum(x*y for x, y in zip(v, u)) == (sum(x*x for x in v) if i == j else 0)

projectors = []
for v in vecs:
    o = outer(v)
    norm2 = sum(x*x for x in v)
    projectors.append([[x / norm2 for x in row] for row in o])
PR = [[sum(projectors[k][i][j] for k in range(9)) for j in range(N)] for i in range(N)]
PK = [[F(i == j) - PR[i][j] for j in range(N)] for i in range(N)]
PK0 = [[PR[i][j] - projectors[0][i][j] for j in range(N)] for i in range(N)]
AA = outer(vecs[0])
W = [[18 * 10**11 * PK[i][j] + 18 * PK0[i][j] - 58 * AA[i][j]
      for j in range(N)] for i in range(N)]
assert all(x.denominator == 1 for row in W for x in row)
assert sum(rho[i][i] for i in range(N)) == 31
assert trprod(PK, rho) == 0
assert trprod(PK0, rho) == 28
assert trprod(AA, rho) == 9
assert trprod(W, rho) == -18
assert trprod(W, AA) == -522
alpha = F(1, 10**11)
margin = alpha / 33
assert alpha <= 33
assert F(1, 2) - 29 * alpha >= margin
assert F(1, 144 * 66**4) - 29 * alpha >= margin
assert 18 * 10**11 * margin == F(6, 11)
print(json.dumps({
    "source_trace": 31,
    "source_and_partial_transpose_exact_psd_ranks": [src["r_rho"], src["r_pt"]],
    "source_five_minor_polynomial_identity": "exact_integer_and_fraction_assertions_passed",
    "integer_witness_formula": "18*10^11*P_K + 18*P_K0 - 58*[A]",
    "integer_entries": True,
    "pairing_with_unnormalized_source": -18,
    "pairing_with_A_projector": -522,
    "normalized_source_pairing": "-18/31",
    "certified_rank_at_most_two_margin": "6/11",
    "margin_arithmetic": "exact_Fraction_assertions_passed",
    "scope": "The rank-two margin relies on the written determinant perturbation and case proof in the accompanying JSON; these checks do not establish any 4x4 witness or proof-assistant verification."
}, indent=2))
