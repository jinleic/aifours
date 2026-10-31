#!/usr/bin/env python3
"""Verify an exact integer/Fraction source-link spectral gap, not a target no-go."""
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
wts = src["wts"]
N = 20
# The nine source vectors are mutually orthogonal; 6*P_K is integer.
P6 = [[6 * int(i == j) for j in range(N)] for i in range(N)]
for v in vecs:
    norm = sum(x*x for x in v)
    assert 6 % norm == 0
    for i in range(N):
        for j in range(N):
            P6[i][j] -= (6 // norm) * v[i] * v[j]
L6 = [[0] * 25 for _ in range(25)]
for wt, v in zip(wts, vecs):
    U = [[0] * 25 for _ in range(N)]
    for p in range(5):
        for q in range(5):
            for alice in range(4):
                U[alice*5+p][p*5+q] = v[alice*5+q]
    P6U = [[sum(P6[i][k] * U[k][j] for k in range(N))
             for j in range(25)] for i in range(N)]
    for a in range(25):
        for b in range(25):
            L6[a][b] += wt * sum(U[k][a] * P6U[k][b] for k in range(N))
u = [int(i // 5 == i % 5) for i in range(25)]
assert all(sum(L6[i][j]*u[j] for j in range(25)) == 0 for i in range(25))
# 5 L6 - 15 I + 3 [u] = 5 (L6 - 3 (I - [u]/5)).
H = [[F(5*L6[i][j] - 15*int(i == j) + 3*u[i]*u[j])
      for j in range(25)] for i in range(25)]
rank = src["psd_rank"](H)
assert rank == 24
assert 18 * 10**10 - 348 > 0
assert F(300, 10) - F(3, 5) * 6 == F(132, 5)
print(json.dumps({
    "integer_link_dimension": 25,
    "scalar_identity_is_null": True,
    "exact_psd_rank_of_5L6_minus_15I_plus_3uu": rank,
    "consequence": "Q_PK(T) >= (1/2)||T-Tr(T)I/5||_F^2",
    "rank_at_most_four_consequence": "Q_PK(T) >= ||T||_F^2/10",
    "explicit_integer_detector_rank_at_most_four_margin": str(18*10**10-348),
    "earlier_unverified_candidate_rank_at_most_four_margin": "132/5",
    "scope": "For the fixed 4x5 source and specified witnesses only; no 4x4 or other-source conclusion. Exact arithmetic, not formal verification."
}, indent=2))
