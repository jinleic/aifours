"""Smoke tests of the python-flint binding behaviours that the certified code RELIES ON (hostile review
me3-charts-codex-v1, finding 2). These are observations of the installed build, not proofs: correct Arb/FLINT
ball arithmetic remains an explicit trusted import; this file records which binding semantics the audited Python code
assumes and checks each once on the installed build.

B1  Python int operands enter arb/acb/fmpq arithmetic exactly (including big ints, on both sides of / + - *).
B2  fmpq -> arb gives an enclosure of the rational (radius > 0 when not dyadic).
B3  Python float -> arb is the exact binary value (so float rounding happens before Arb; demonstrates finding 1).
B4  Python int / int is a float (the defect class audited in proof/float-audit-v1.md).
B5  Comparisons of overlapping balls are False in both directions; comparisons with non-finite balls are False.
B6  Division by a ball containing 0, and log of a ball containing 0, give non-finite balls (is_finite() False).
B7  acb.arg of a ball straddling the negative real axis is not certified-positive nor certified-negative.
B8  union contains both arguments; intersection of overlapping balls contains the common points; upper() bounds
    every element; abs(acb) encloses the modulus.
B9  arb.pi(), exp, log, cos, sin, tan, sqrt enclose the exact values at sample points (checked against 60-digit mpmath).
argv[1] = run dir; writes binding.json (exclusive create).
"""
import sys
import json
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import lane_guard  # noqa: E402
import flint  # noqa: E402
from flint import arb, acb, fmpq  # noqa: E402
import mpmath  # noqa: E402

RUN = sys.argv[1]
flint.ctx.prec = 128
mpmath.mp.dps = 60
R = {}


def chk(name, cond, note=""):
    R[name] = {"ok": bool(cond), "note": note}


big = 10 ** 40
chk("B1_int_div_arb", (arb(1) / 3).contains(fmpq(1, 3)) and (acb(-3) / 5).real.contains(fmpq(-3, 5)))
chk("B1_int_rdiv", (3 / arb(7)).contains(fmpq(3, 7)) and (1 / acb(4)).real.contains(fmpq(1, 4)))
chk("B1_bigint_exact", (arb(big + 1) - big) == arb(1) and (big + 1) * arb(1) - big == 1)
chk("B1_int_plus_acb", (acb(arb(1) / 3) + 3 * (-1) ** 5).real.contains(fmpq(-8, 3)))
chk("B1_fmpq_int", fmpq(1, 2) / 3 == fmpq(1, 6) and 1 / (1 + fmpq(11, 50)) == fmpq(50, 61))
x = arb(fmpq(1, 3))
chk("B2_fmpq_enclosure", x.contains(fmpq(1, 3)) and x.rad() > 0)
f = arb(0.1)
chk("B3_float_exact_binary", f.rad() == 0 and not f.contains(fmpq(1, 10)), f.str(30))
chk("B4_int_int_div_is_float", isinstance(3 / 5, float) and isinstance(3 * (-1) ** 5 / 5, float)
    and not arb(3 * (-1) ** 5 / 5).contains(fmpq(-3, 5)))
a, b = arb(1).union(arb(2)), arb(fmpq(3, 2)).union(arb(3))
chk("B5_overlap_compare_false", not (a < b) and not (a > b) and not (a <= b) and not (a >= b) and not (a == b))
z = arb(-1).union(arb(1))
inf = arb(1) / z
lg = z.log()
chk("B6_div_by_zero_ball_nonfinite", not inf.is_finite() and not (inf < 0) and not (inf > 0) and not (inf >= 0))
chk("B6_log_zero_ball_nonfinite", not lg.is_finite() and not (lg < 1) and not (lg > -1))
w = acb(arb(-2), arb(-1).union(arb(1)) / 100)
ag = w.arg()
chk("B7_arg_branch_cut", not (ag > 0) and not (ag < 0), ag.str(10))
u = arb(fmpq(1, 7)).union(arb(fmpq(5, 7)))
it = (arb(0).union(arb(fmpq(1, 2)))).intersection(arb(fmpq(1, 4)).union(arb(1)))
chk("B8_union_intersection", u.contains(fmpq(1, 7)) and u.contains(fmpq(5, 7)) and it.contains(fmpq(1, 3))
    and it.contains(fmpq(1, 4)) and it.contains(fmpq(1, 2)))
chk("B8_upper", bool(u.upper() >= arb(fmpq(5, 7))) and bool(u.upper() >= arb(fmpq(1, 7))) and u.upper().rad() == 0)
q = acb(3, 4)
chk("B8_abs", abs(q).contains(5))
ok9 = True
for v in (fmpq(1, 3), fmpq(7, 5), fmpq(-2, 9)):
    av = arb(v)
    mv = mpmath.mpf(int(v.p)) / int(v.q)
    fns = [(lambda t: t.exp(), mpmath.exp), (lambda t: t.cos(), mpmath.cos), (lambda t: t.sin(), mpmath.sin),
           (lambda t: t.tan(), mpmath.tan)]
    if v > 0:
        fns += [(lambda t: t.log(), mpmath.log), (lambda t: t.sqrt(), mpmath.sqrt)]
    for fa, fm in fns:
        ref = arb(mpmath.nstr(fm(mv), 55) + " +/- 1e-50")
        ball_ = fa(av)
        ok9 = ok9 and bool(ball_.overlaps(ref)) and bool(ball_.rad() < arb("1e-30"))
chk("B9_elementary_functions_spot",
    ok9 and arb.pi().overlaps(arb("3.14159265358979323846264338327950288419716939937510 +/- 1e-48")))
res = {"python_flint": flint.__version__, "FLINT": getattr(flint, "__FLINT_VERSION__", None), "prec": flint.ctx.prec,
       "checks": R, "all_ok": all(v["ok"] for v in R.values())}
with lane_guard.xopen(RUN + "/binding.json") as fh:
    json.dump(res, fh, indent=1)
print(json.dumps(res, indent=1))
