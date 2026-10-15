"""Exact scientific replay for the paired generic three-super-soliton obstruction.

Independent of the old Hirota engine: body tau coefficients are reconstructed by
Euler differentiation and SymPy linear elimination. A separate sparse exterior
algebra implements anticommutation, LEFT odd derivatives, separate theta1/theta2,
and diagonal evaluation. All arithmetic is exact; no float/solver tolerance.
The universal n>=4 conclusion is the written proof in RESULTS.md, supported by
its explicit finite integer certificate and this replay, not by extrapolation.
"""
from __future__ import annotations

import itertools
import json
import math
import platform
from dataclasses import dataclass
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parent.parent
Z = s.symbols("z1 z2 z3")


@dataclass
class Exterior:
    # Order: theta1 (bit0), theta2 (bit1), zeta1 (bit2), zeta2 (bit3), zeta3 (bit4).
    terms: dict

    def __post_init__(self):
        self.terms = {m: s.expand(v) for m, v in self.terms.items() if s.expand(v) != 0}

    @staticmethod
    def scalar(value):
        return Exterior({0: s.sympify(value)})

    @staticmethod
    def gen(index):
        return Exterior({1 << index: s.Integer(1)})

    def __add__(self, other):
        if not isinstance(other, Exterior):
            other = Exterior.scalar(other)
        out = dict(self.terms)
        for m, v in other.terms.items():
            out[m] = out.get(m, 0) + v
        return Exterior(out)

    __radd__ = __add__

    def __neg__(self):
        return Exterior({m: -v for m, v in self.terms.items()})

    def __sub__(self, other):
        return self + (-other if isinstance(other, Exterior) else -s.sympify(other))

    def __mul__(self, other):
        if not isinstance(other, Exterior):
            other = Exterior.scalar(other)
        out = {}
        for a, ca in self.terms.items():
            for b, cb in other.terms.items():
                if a & b:
                    continue
                inv = sum((b & ((1 << i) - 1)).bit_count()
                          for i in range(a.bit_length()) if a & (1 << i))
                mask = a | b
                out[mask] = out.get(mask, 0) + (-1) ** inv * ca * cb
        return Exterior(out)

    __rmul__ = __mul__

    def left_derivative(self, index):
        bit = 1 << index
        return Exterior({m ^ bit: (-1) ** ((m & (bit - 1)).bit_count()) * v
                         for m, v in self.terms.items() if m & bit})

    def map_coefficients(self, fn):
        return Exterior({m: fn(v) for m, v in self.terms.items()})

    def parameter_projection(self):
        return Exterior({m: v for m, v in self.terms.items() if not m & ~3})

    def theta_diagonal(self):
        out = {}
        for mask, value in self.terms.items():
            if mask & 3 == 3:
                continue  # theta1 theta2 -> theta^2=0
            target = (mask & ~3) | (1 if mask & 3 else 0)
            out[target] = out.get(target, 0) + value
        return Exterior(out)

    def is_zero(self):
        return not self.terms

    def parity_even(self):
        return all(m.bit_count() % 2 == 0 for m in self.terms)


def lift_operator(fn):
    return lambda value: value.map_coefficients(fn) if isinstance(value, Exterior) else fn(value)


def pn(f, g, n, dx, dt):
    """Ordinary Hirota derivative from its binomial definition, on scalars or Exterior."""
    fx, gx = [f], [g]
    for _ in range(n):
        fx.append(dx(fx[-1]))
        gx.append(dx(gx[-1]))
    out = dt(f) * g - f * dt(g)
    for j in range(n + 1):
        out = out + (-1) ** j * math.comb(n, j) * fx[n - j] * gx[j]
    return out


def dy_pn(f, g, n, dx, dy, dt):
    return pn(dy(f), g, n, dx, dt) - pn(f, dy(g), n, dx, dt)


def super_pn(f, g, n, dx, dy, dt):
    """Separate theta1/theta2 until after both left odd derivatives have acted."""
    th1, th2 = Exterior.gen(0), Exterior.gen(1)
    out = pn(f.left_derivative(0), g, n, dx, dt)
    out -= pn(f, g.left_derivative(1), n, dx, dt)
    out += th1 * pn(dy(f), g, n, dx, dt)
    out -= th2 * pn(f, dy(g), n, dx, dt)
    return out.theta_diagonal()


def exterior_controls():
    th1, th2, za, zb, zc = [Exterior.gen(i) for i in range(5)]
    assert (za * zb + zb * za).is_zero()
    assert (za * za).is_zero()
    assert (za * th1).left_derivative(0).terms == (-za).terms
    assert (th1 * za).left_derivative(0).terms == za.terms
    assert (th1 * th2).theta_diagonal().is_zero()
    x, y, t = s.symbols("x y t")
    dx = lift_operator(lambda v: s.diff(v, x))
    dy = lift_operator(lambda v: s.diff(v, y))
    dt = lift_operator(lambda v: s.diff(v, t))
    rows = []
    for n in range(2, 7):
        f = x ** n * y + y * t + 1
        g = 1 + x + y * t
        ff = (Exterior.scalar(f) + th1 * za * (x ** 2 + y * t)
              + za * zb * (x + y) + th1 * zb * t)
        gg = (Exterior.scalar(g) + th2 * zc * (x * y + t)
              + za * zc * (x ** 2 + y))
        assert ff.parity_even() and gg.parity_even()
        projected_p = pn(ff, gg, n, dx, dt).theta_diagonal().parameter_projection()
        projected_s = super_pn(ff, gg, n, dx, dy, dt).parameter_projection()
        expected_p = Exterior.scalar(s.expand(pn(f, g, n, dx, dt)))
        expected_s = th1 * s.expand(dy_pn(f, g, n, dx, dy, dt))
        assert (projected_p - expected_p).is_zero()
        assert (projected_s - expected_s).is_zero()
        # Negative control: killing external theta erases a genuine bosonic constraint.
        simple = super_pn(Exterior.scalar(x ** n * y), Exterior.scalar(1), n, dx, dy, dt)
        assert simple.terms == {1: s.Integer(math.factorial(n))}
        assert simple.terms.get(0, 0) == 0
        rows.append({"n": n, "projection_identities": True,
                     "external_theta_coefficient": math.factorial(n),
                     "incorrect_theta_zero_projection": 0})
    return rows


def euler(weights):
    return lambda expr: s.expand(sum(w * z * s.diff(expr, z) for w, z in zip(weights, Z)))


def reconstruct_body(n):
    """Unique pair/triple coefficients from independent Euler/binomial differentiation."""
    k, ell = [s.Integer(1), s.Integer(2), s.Integer(-4)], [s.Integer(1), s.Integer(3), s.Integer(7)]
    omega = [s.Integer(-1), -s.Integer(2) ** n, s.Integer(4) ** n]
    dx, dy, dt = euler(k), euler(ell), euler(omega)
    fc = {0: s.Integer(1), 1: s.Integer(1), 2: s.Integer(1), 4: s.Integer(0)}
    gc = {0: s.Integer(1), 1: s.Integer(0), 2: s.Integer(0), 4: s.Integer(1)}

    def monomial(mask):
        return s.prod(Z[i] for i in range(3) if mask & (1 << i))

    def polynomial(coeff):
        return sum(value * monomial(mask) for mask, value in coeff.items())

    for mask in (3, 5, 6, 7):
        u, v = s.symbols(f"F{mask} G{mask}")
        fc[mask], gc[mask] = u, v
        f, g = polynomial(fc), polynomial(gc)
        p = s.Poly(s.expand(pn(f, g, n, dx, dt)), *Z)
        q = s.Poly(s.expand(dy_pn(f, g, n, dx, dy, dt)), *Z)
        equations = (p.coeff_monomial(monomial(mask)), q.coeff_monomial(monomial(mask)))
        solutions = s.solve(equations, (u, v), dict=True)
        assert len(solutions) == 1 and set(solutions[0]) == {u, v}
        fc[mask], gc[mask] = solutions[0][u], solutions[0][v]
    f, g = s.expand(polynomial(fc)), s.expand(polynomial(gc))
    p = s.Poly(s.expand(pn(f, g, n, dx, dt)), *Z)
    q = s.Poly(s.expand(dy_pn(f, g, n, dx, dy, dt)), *Z)
    residuals = [{str(m): str(c) for m, c in poly.terms() if c != 0} for poly in (p, q)]
    coefficient = p.coeff_monomial(Z[0] ** 2 * Z[1] * Z[2])
    phi = phi_value(n)
    predicted = s.Rational(7 * phi, 11 * (2 + 2 ** n - 4 ** n) * (1 + 3 ** n - 4 ** n))
    assert coefficient == predicted
    if n in (2, 3):
        assert p.is_zero and q.is_zero
    else:
        assert coefficient != 0
    # Genuine but restricted common-fermion lift at the passing body boundaries.
    if n in (2, 3):
        dxs, dys, dts = [lift_operator(op) for op in (dx, dy, dt)]
        zeta = Exterior.gen(2)
        ff = Exterior.scalar(f) + Exterior.gen(0) * zeta * dy(f)
        gg = Exterior.scalar(g) + Exterior.gen(1) * zeta * dy(g)
        assert pn(ff, gg, n, dxs, dts).theta_diagonal().is_zero()
        assert super_pn(ff, gg, n, dxs, dys, dts).is_zero()
    else:
        # Arbitrary explicit nilpotent dressings leave the forbidden body residual intact.
        ff = Exterior.scalar(f) + Exterior.gen(0) * Exterior.gen(2) * Z[0]
        ff += Exterior.gen(2) * Exterior.gen(3) * Z[0] * Z[2]
        gg = Exterior.scalar(g) + Exterior.gen(1) * Exterior.gen(4) * Z[2]
        dxs, dys, dts = [lift_operator(op) for op in (dx, dy, dt)]
        assert pn(ff, gg, n, dxs, dts).theta_diagonal().parameter_projection().terms == {0: p.as_expr()}
        assert super_pn(ff, gg, n, dxs, dys, dts).parameter_projection().terms == {1: q.as_expr()}
    return {"n": n, "k": [str(v) for v in k], "l": [str(v) for v in ell],
            "omega": [str(v) for v in omega], "F_coefficients": {str(m): str(v) for m, v in sorted(fc.items())},
            "G_coefficients": {str(m): str(v) for m, v in sorted(gc.items())},
            "R211_direct_Euler": str(coefficient), "R211_closed_form": str(predicted),
            "full_P_nonzero_coefficients": residuals[0], "full_DyP_nonzero_coefficients": residuals[1],
            "common_parameter_super_lift": "both residuals zero" if n in (2, 3) else "not asserted",
            "nilpotent_cannot_cancel_body_control": n >= 4}


def phi_value(n):
    return ((6 ** n - 4 ** n - 2 ** n) * (3 ** n + 2 ** n - 4 ** n - 1) * (3 ** n + 1 - 4 ** n)
            + (5 ** n - 4 ** n - 1) * (5 ** n - 4 ** n - 2 ** n + 1) * (2 ** (n + 1) - 4 ** n))


def degree_certificate():
    rows = []
    for n in range(2, 30):
        phi = phi_value(n)
        pvalues = [3 ** n - 2 ** n - 1, 1 + 2 ** n + (-3) ** n,
                   4 ** n - 1 + (-3) ** n, 1 + 3 ** n - 4 ** n,
                   4 ** n - 2 ** n + (-2) ** n, 2 ** (n + 1) - 4 ** n,
                   4 ** n - 2 ** n - 1 + (-1) ** n, 2 + 2 ** n - 4 ** n]
        assert all(pvalues)
        assert phi == 0 if n in (2, 3) else phi < 0
        assert 4 ** n + 11 * 2 ** n - 26 > 0
        rows.append({"n": n, "Phi": str(phi), "nonzero_recursion_factors": list(map(str, pvalues))})
    gap = (5 ** 30 - 2 * 4 ** 30) ** 2 - 2 * 24 ** 30
    assert gap >= 0
    return {"finite_signs": rows, "tail_threshold": 30, "tail_integer_gap": str(gap),
            "tail_argument": "For n>=30, (1-2(4/5)^n)^2 increases and 2(24/25)^n decreases; RESULTS.md Lemma3.1 proves the infinite tail."}


def main():
    exterior = exterior_controls()
    degrees = degree_certificate()
    witnesses = [reconstruct_body(n) for n in (2, 3, 4, 5)]
    report = {"python": platform.python_version(), "sympy": s.__version__, "arithmetic": "exact; no floats",
              "external_theta_retained": True, "old_engine_imported": False,
              "exterior_controls": exterior, "degree_certificate": degrees, "witnesses_and_boundaries": witnesses}
    output = ROOT / "results/replay.json"
    output.write_text(json.dumps(report, indent=2) + "\n")
    print("Exterior algebra: anticommutation, left derivatives, separate theta1/theta2 and projection identities PASS (n=2..6)")
    print("Negative control: setting external theta=0 loses the nonzero theta*n! constraint, as expected")
    print("Degree certificate: Phi2=Phi3=0; Phi_n<0 for n=4..29; exact tail inequality at n=30 PASS")
    for row in witnesses:
        print(f"n={row['n']}: R211={row['R211_direct_Euler']}; full residual counts P={len(row['full_P_nonzero_coefficients'])}, DyP={len(row['full_DyP_nonzero_coefficients'])}; common-parameter lift={row['common_parameter_super_lift']}")
    print("n=4,5 Euler/binomial witnesses match closed form; nilpotent-dressing projection controls PASS")
    print(f"wrote {output}")


if __name__ == "__main__":
    main()
