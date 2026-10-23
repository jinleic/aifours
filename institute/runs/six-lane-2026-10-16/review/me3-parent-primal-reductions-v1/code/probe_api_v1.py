"""Parent desk ME3ParentPrimal: API probe of the read-only python-flint/sympy/mpmath environment (no science).
Prints library versions and the semantics of the ball operations the evaluators rely on."""
import sys
import flint
from flint import arb, acb, fmpq, ctx
import sympy
import mpmath

print("python", sys.version.split()[0], "flint", flint.__version__, "sympy", sympy.__version__, "mpmath", mpmath.__version__)
ctx.prec = 128
x = arb(fmpq(1, 3))
print("arb(1/3)", x.str(40, radius=True), "mid", x.mid(), "rad", x.rad())
u = arb(fmpq(1, 5)).union(arb(fmpq(2, 5)))
print("union [1/5,2/5]", u.str(20, radius=True), "lower", u.lower(), "upper", u.upper())
print("contains 1/5,2/5:", u.contains(arb(fmpq(1, 5))), u.contains(arb(fmpq(2, 5))))
print("cmp certain/uncertain:", u > 0, u > arb(fmpq(3, 10)), u < 1, u < arb(fmpq(3, 10)))
z = acb(u, arb(1))
print("acb", z.real.str(10, radius=True), z.imag.str(10, radius=True), "exp", z.exp().real.str(10, radius=True))
print("pi>3.14159", arb.pi() > arb(fmpq(314159, 100000)), "pi<3.1416", arb.pi() < arb(fmpq(31416, 10000)))
print("intersection", u.intersection(arb(fmpq(3, 10)).union(arb(1))).str(20, radius=True))
print("fmpq parse", fmpq(31416, 5000), fmpq(61, 50))
print("sin_cos", arb(1).sin_cos()[0].str(10), arb(1).sin_cos()[1].str(10))
print("is_finite", arb("inf").is_finite(), x.is_finite())
w = acb(1, 2)
print("acb conj", w.conjugate(), "abs", abs(w).str(10))
