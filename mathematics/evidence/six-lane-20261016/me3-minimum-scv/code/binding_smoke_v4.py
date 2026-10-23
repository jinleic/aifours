"""Binding smoke, version 4 (v3 kept: its B10a expectation was wrong, see B10a below; all other checks are
unchanged): the COMPARISON CONTRACT relied on by the certified code. It supplements
binding_smoke_v2.py, which is kept. v2's docstring sentence "comparisons of overlapping balls are False" was too broad for
non-strict comparisons (hostile delta review me3-charts-v2-delta-codex-v1, finding 6). These are observations of the
installed build (python-flint 0.9.0, FLINT 3.6.0), not proofs; Arb's comparison semantics remain a trusted import.

Contract (Arb arb_lt / arb_le / arb_gt / arb_ge, exposed by python-flint's rich comparisons):
  for finite balls x, y, `x < y` (resp. <=, >, >=) is True iff a < b (resp. <=, >, >=) for EVERY a in x and b in y.
  Hence a strict comparison of overlapping balls is False; a non-strict comparison of overlapping balls is True only when
  the relation still holds for every pair (balls touching at an exact common endpoint, or equal exact points); and every
  comparison involving an indeterminate ball (NaN midpoint, e.g. a quotient by a ball containing 0) is False.
B10a union-built [1,2] versus the exact point 2 (v3 wrongly expected `<=` to be True: the union's radius is stored
     rounded UP, so the stored ball extends above 2, and Arb correctly refuses `<= 2`): x.upper() > 2 True,
     x <= 2 False, x < 2 False, 2 > x False. A False comparison therefore carries no information.
B10b equal exact points: 1 <= 1 and 1 >= 1 True, 1 < 1 and 1 > 1 False (also for the exact dyadic 1/2).
B10c coincident inexact balls (positive radius, arb(1/3)): <= and >= False.
B10d overlapping interiors [1,2] vs [3/2,3]: <, <=, >, >= all False.
B10e indeterminate q = 1/[-1,1]: q < 0, q <= 0, q > 0, q >= 0, q <= q all False; q.is_finite() False.
B10f mixed operands: arb(1) >= 1 True; arb(1/3) > fmpq(1/3) False; arb(1/3) >= fmpq(1/4) True.
B10g (information only, no expectation): log of [-1,1], of [0,1] and of exact 0, with is_finite() and the comparisons
     with 0. Certified paths take logs only of balls certified positive (G: aW > 0 is tested first), of W on a branch
     mode that excludes 0 (Im W > 0, Im W < 0 or Re W < 0, MVF), or of quantities whose true value is positive
     (SWB: Nt/N1 > 0 and 1 + delta >= 1), so an exact 0 never reaches log.
argv[1] = run dir; writes binding.json (exclusive create).
"""
import sys
import json
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import lane_guard  # noqa: E402
import flint  # noqa: E402
from flint import arb, fmpq  # noqa: E402

RUN = sys.argv[1]
flint.ctx.prec = 128
R = {}


def chk(name, observed, expected):
    R[name] = {"observed": observed, "expected": expected, "ok": observed == expected}


x12, two = arb(1).union(arb(2)), arb(2)
chk("B10a_union_vs_endpoint", [x12.upper() > 2, x12 <= two, x12 < two, two > x12], [True, False, False, False])
one, half = arb(1), arb(fmpq(1, 2))
chk("B10b_equal_exact", [one <= one, one >= one, one < one, one > one, half <= half, half >= half, half < half],
    [True, True, False, False, True, True, False])
t = arb(fmpq(1, 3))
chk("B10c_coincident_inexact", [bool(t.rad() > 0), t <= t, t >= t], [True, False, False])
y = arb(fmpq(3, 2)).union(arb(3))
chk("B10d_overlapping_interiors", [x12 < y, x12 <= y, x12 > y, x12 >= y], [False, False, False, False])
q = arb(1) / (arb(-1).union(arb(1)))
chk("B10e_indeterminate", [q < 0, q <= 0, q > 0, q >= 0, q <= q, q.is_finite()], [False] * 6)
chk("B10f_mixed_operands", [one >= 1, t > fmpq(1, 3), t >= fmpq(1, 4)], [True, False, True])
info = {}
for label, ball_ in (("log[-1,1]", arb(-1).union(arb(1))), ("log[0,1]", arb(0).union(arb(1))), ("log(0)", arb(0))):
    try:
        v = ball_.log()
        info[label] = {"value": v.str(radius=True), "is_finite": v.is_finite(), "lt0": v < 0, "le0": v <= 0,
                       "gt0": v > 0, "ge0": v >= 0}
    except Exception as exc:  # recorded, not expected
        info[label] = {"exception": repr(exc)}
res = {"python_flint": flint.__version__, "FLINT": getattr(flint, "__FLINT_VERSION__", None), "prec": flint.ctx.prec,
       "checks": R, "all_ok": all(v["ok"] for v in R.values()), "B10g_information": info}
with lane_guard.xopen(RUN + "/binding.json") as fh:
    json.dump(res, fh, indent=1)
print(json.dumps(res, indent=1))
