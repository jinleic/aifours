#!/usr/bin/env python3
"""Certified checks for the genuine-Fourier joint IF/GD counterexample.

Signal s(t)=pi^(-1/4) exp(-t^2/2) (1+i p(t)/14), p=4t^4-12t^2+3.
With E=55/49, rho=|s|^2/E=RHO(t)e^(-t^2)/(220 sqrt(pi)) and
J=f rho=CUR(t)e^(-t^2)/(220 sqrt(pi)), RHO=196+p^2, CUR=14p'.

Every accepted decision uses exact rationals (fractions / FLINT fmpq_poly) or
FLINT arb balls. Floating point is never used to accept a claim.
"""
import argparse
import datetime
from fractions import Fraction
import json
from pathlib import Path
import flint
from flint import arb, fmpq, fmpq_poly, fmpz_poly, ctx

ctx.prec = 256
P = fmpq_poly([3, 0, -12, 0, 4])
RHO = 196 + P * P
CUR = 14 * P.derivative()
T = fmpq_poly([0, 1])
SQRT_PI = arb.pi().sqrt()
NORM = 220 * SQRT_PI


def fq(x):
    x = Fraction(x)
    return fmpq(x.numerator, x.denominator)


def ab(x):
    return arb(fq(x))


def dyadic(x):
    mantissa, exponent = x.man_exp()
    return fmpq(mantissa) * fmpq(2) ** exponent if exponent >= 0 \
        else fmpq(mantissa, 2 ** (-exponent))


def moments_0x(x, degree):
    e = (-x * x).exp()
    out = [SQRT_PI / 2 * x.erf(), (1 - e) / 2]
    for m in range(2, degree + 1):
        out.append(arb(m - 1) / 2 * out[m - 2] - x ** (m - 1) * e / 2)
    return out


def moments_tail(x, degree):
    e = (-x * x).exp()
    out = [SQRT_PI / 2 * x.erfc(), e / 2]
    for m in range(2, degree + 1):
        out.append(arb(m - 1) / 2 * out[m - 2] + x ** (m - 1) * e / 2)
    return out


def integral_0x(poly, x):
    """int_0^x poly(t) exp(-t^2) dt for an arb x (ball endpoints allowed)."""
    coeffs = poly.coeffs()
    moments = moments_0x(x, max(1, len(coeffs) - 1))
    return sum((arb(c) * moments[m] for m, c in enumerate(coeffs)), arb(0))


def integral_tail(poly, x):
    coeffs = poly.coeffs()
    moments = moments_tail(x, max(1, len(coeffs) - 1))
    return sum((arb(c) * moments[m] for m, c in enumerate(coeffs)), arb(0))


def gaussian_moment(n):
    """Exact int t^n exp(-t^2) dt / sqrt(pi)."""
    if n % 2:
        return Fraction(0)
    out = Fraction(1)
    for j in range(1, n, 2):
        out *= Fraction(j, 2)
    return out


def exact_full_integral(poly):
    return sum(Fraction(int(c.p), int(c.q)) * gaussian_moment(m)
               for m, c in enumerate(poly.coeffs()))


def sturm_count(poly, lower_zero):
    """Distinct real roots in (0,inf) if lower_zero else in (-inf,inf)."""
    seq = [poly, poly.derivative()]
    while seq[-1].degree() > 0:
        seq.append(-(seq[-2] % seq[-1]))
    seq = [p for p in seq if not p.is_zero()]

    def variations(signs):
        signs = [s for s in signs if s != 0]
        return sum(1 for a, b in zip(signs, signs[1:]) if a != b)

    def lead_sign(p, at_minus):
        c = p.coeffs()[-1]
        sign = 1 if c > 0 else -1
        return -sign if at_minus and p.degree() % 2 else sign

    at_inf = variations([lead_sign(p, False) for p in seq])
    if lower_zero:
        values = [p(fmpq(0)) for p in seq]
        if values[0] == 0:
            raise ValueError('Sturm count requires poly(0)!=0')
        at_low = variations([(v > 0) - (v < 0) for v in values])
    else:
        at_low = variations([lead_sign(p, True) for p in seq])
    return at_low - at_inf


def positive_simple_roots(poly):
    roots = []
    for z, multiplicity in fmpz_poly(poly.numer()).complex_roots():
        if not z.imag.is_zero():
            continue
        if multiplicity != 1:
            raise ValueError('multiple real root')
        if z.real > 0:
            roots.append(z.real)
        elif not z.real < 0:
            raise ValueError('real root ball meets zero')
    roots.sort(key=lambda r: dyadic(r.mid()))
    for left, right in zip(roots, roots[1:]):
        if not left < right:
            raise ValueError('root balls overlap')
    if len(roots) != sturm_count(poly, True):
        raise ValueError('FLINT root count disagrees with exact Sturm count')
    return roots


def sign_intervals(poly, want_positive):
    """Intervals in (0,inf) where poly has the requested sign; arb endpoints."""
    roots = positive_simple_roots(poly)
    points = [arb(0)] + roots
    intervals = []
    for index, left in enumerate(points):
        right = roots[index] if index < len(roots) else None
        if right is None:
            sign = 1 if poly.coeffs()[-1] > 0 else -1
        else:
            lo = fmpq(0) if index == 0 else dyadic(left.upper())
            sample = (lo + dyadic(right.lower())) / 2
            value = poly(sample)
            sign = (value > 0) - (value < 0)
            if sign == 0:
                raise ValueError('sample hit a root')
        if (sign > 0) == want_positive:
            intervals.append((left, right))
    return intervals


def positive_part_integral(poly, sign):
    """int_0^inf (sign*poly)_+ exp(-t^2) dt."""
    total = arb(0)
    for left, right in sign_intervals(poly, sign > 0):
        if right is None:
            raise ValueError('unbounded positivity interval')
        piece = integral_0x(poly, right) - integral_0x(poly, left)
        total += piece if sign > 0 else -piece
    return total


def call_signal(k):
    """C_f(k)=E(|f(T)|-k)_+, k>0, as an arb enclosure."""
    k = fq(k)
    upper = positive_part_integral(CUR - k * RHO, 1)
    lower = positive_part_integral(CUR + k * RHO, -1)
    return 2 * (upper + lower) / NORM


def call_time(k):
    """C_T(k)=E(|T|-k)_+, k>=0."""
    k = fq(k)
    return 2 * (integral_tail(T * RHO, arb(k)) - arb(k) * integral_tail(RHO, arb(k))) / NORM


def first_absolute_if():
    """E|f(T)| = 7(16 e^{-3/2}+4)/(55 sqrt(pi)), from int |p'|e^{-t^2}."""
    return 7 * (16 * arb(fmpq(-3, 2)).exp() + 4) / (55 * SQRT_PI)


def convex_order_certificate(step, cap):
    bounds = (fq(cap) * RHO - CUR, fq(cap) * RHO + CUR)
    if any(sturm_count(poly, False) for poly in bounds):
        return {'accepted': False, 'reason': 'cap*RHO-|CUR| has a real root'}
    if any(z.imag.is_zero() for poly in bounds
           for z, _ in fmpz_poly(poly.numer()).complex_roots()):
        return {'accepted': False, 'reason': 'FLINT found a real root'}
    grid = [Fraction(0)]
    while grid[-1] < cap:
        grid.append(min(grid[-1] + step, cap))
    worst = None
    rows = []
    for left, right in zip(grid, grid[1:]):
        signal = first_absolute_if() if left == 0 else call_signal(left)
        margin = call_time(right) - signal
        if not margin > 0:
            return {'accepted': False, 'reason': f'margin not certified on [{left},{right}]'}
        lower_bound = dyadic(margin.lower())
        rows.append({'k_left': str(left), 'k_right': str(right),
                     'margin_lower_bound': str(Fraction(int(lower_bound.p), int(lower_bound.q)))})
        if worst is None or lower_bound < worst[0]:
            worst = (lower_bound, left, right)
    return {'accepted': True, 'sup_abs_IF_cap': str(cap), 'grid_step': str(step),
            'intervals': len(rows),
            'minimum_margin_lower_bound': float(Fraction(int(worst[0].p), int(worst[0].q))),
            'minimum_margin_interval': [str(worst[1]), str(worst[2])],
            'E_abs_T': str(call_time(0)), 'E_abs_IF': str(first_absolute_if()),
            'rows': rows}


def load_certificate(path, entry):
    data = json.loads(Path(path).read_text())['results'][entry]
    return {key: [Fraction(v) for v in data[key]] for key in ('edges', 'a', 'b', 'h', 'k')}


def corner_minimum(cert):
    e, a, b, h, k = (cert[x] for x in ('edges', 'a', 'b', 'h', 'k'))
    n = len(a)
    if len(e) != n + 1 or any(len(cert[x]) != n for x in 'bhk') or \
            any(x >= y for x, y in zip(e, e[1:])) or e[0] != -e[-1]:
        raise ValueError('malformed certificate')
    return min(a[i] + b[j] + h[i] * w + k[j] * t
               for i in range(n) for j in range(n)
               for t in (e[i], e[i + 1]) for w in (e[j], e[j + 1]))


def outside_constants(cert):
    a, b, h, k = (cert[x] for x in 'abhk')
    return (max([Fraction(0)] + [-x for x in a]), max([Fraction(0)] + [-x for x in b]),
            max(abs(x) for x in h), max(abs(x) for x in k))


def certificate_total(cert, data):
    """Evaluate E[a(T)+b(W)+h(T)W+k(W)T] forced by marginals and both regressions.

    data(edge_left, edge_right) returns arb tuple
    (mu(cell), int_cell f dmu, nu(cell), int_cell g dnu), and data.tail(L)
    returns (mu(|t|>L), int_{|t|>L}|t|dmu, nu(|w|>L), int_{|w|>L}|w|dnu).
    """
    e, a, b, h, k = (cert[x] for x in ('edges', 'a', 'b', 'h', 'k'))
    a_minus, b_minus, h_max, k_max = outside_constants(cert)
    total = arb(0)
    for i in range(len(a)):
        mu, fmu, nu, gnu = data.cell(ab(e[i]), ab(e[i + 1]))
        total += ab(a[i]) * mu + ab(b[i]) * nu + ab(h[i]) * fmu + ab(k[i]) * gnu
    mu_tail, mu_abs, nu_tail, nu_abs = data.tail(ab(e[-1]))
    # Outside the box: a(t)=B^- + K|t|, h=0; b(w)=A^- + H|w|, k=0.
    total += ab(b_minus) * mu_tail + ab(k_max) * mu_abs
    total += ab(a_minus) * nu_tail + ab(h_max) * nu_abs
    return total


class HermiteData:
    """The counterexample: nu=mu and g=-f."""

    def cell(self, left, right):
        mu = (integral_0x(RHO, right) - integral_0x(RHO, left)) / NORM
        fmu = (integral_0x(CUR, right) - integral_0x(CUR, left)) / NORM
        return mu, fmu, mu, -fmu

    def tail(self, limit):
        mu_tail = 2 * integral_tail(RHO, limit) / NORM
        mu_abs = 2 * integral_tail(T * RHO, limit) / NORM
        return mu_tail, mu_abs, mu_tail, mu_abs


class ChirpData:
    """Feasible control: Gaussian chirp, whose nonnegative Wigner law has IF and GD.

    T~N(0,1/2), f(t)=beta t, W~N(0,(1+beta^2)/2), g(w)=beta w/(1+beta^2).
    """

    def __init__(self, beta):
        self.beta = ab(beta)
        self.sigma = (1 + self.beta ** 2).sqrt()

    def _gauss(self, left, right, scale):
        mass = ((right / scale).erf() - (left / scale).erf()) / 2
        first = scale * ((-(left / scale) ** 2).exp() - (-(right / scale) ** 2).exp()) / (2 * SQRT_PI)
        return mass, first

    def cell(self, left, right):
        mu, tmu = self._gauss(left, right, arb(1))
        nu, wnu = self._gauss(left, right, self.sigma)
        return mu, self.beta * tmu, nu, self.beta / self.sigma ** 2 * wnu

    def tail(self, limit):
        out = []
        for scale in (arb(1), self.sigma):
            out += [(limit / scale).erfc(), scale * (-(limit / scale) ** 2).exp() / SQRT_PI]
        return tuple(out)


def check_certificate(cert, label):
    corner = corner_minimum(cert)
    total = certificate_total(cert, HermiteData())
    accepted = corner >= 0 and total < 0
    return {'label': label, 'corner_minimum': str(corner), 'corner_ok': corner >= 0,
            'hermite_total': str(total), 'hermite_total_certified_negative': bool(total < 0),
            'accepted': bool(accepted)}


def fourier_image_of_even_polynomial(poly):
    """F[q(t)e^{-t^2/2}] = sum_n q_n (-i)^n He_n(w) e^{-w^2/2} for even q.

    Uses F[e^{-t^2/2}]=e^{-w^2/2}, F[t u]=i(Fu)' and
    (d/dw)^n e^{-w^2/2}=(-1)^n He_n(w)e^{-w^2/2}.
    """
    hermite = [fmpq_poly([1]), fmpq_poly([0, 1])]
    for n in range(1, poly.degree()):
        hermite.append(T * hermite[n] - n * hermite[n - 1])
    image = fmpq_poly([0])
    for n, coefficient in enumerate(poly.coeffs()):
        if coefficient == 0:
            continue
        if n % 2:
            raise ValueError('odd term would contribute an imaginary part')
        image += (-1) ** (n // 2) * coefficient * hermite[n]
    return image


def phase_derivative_identity():
    """s=G(u+iv), G real with G'=-tG: Im(conj(s)s')/|s|^2=(uv'-vu')/(u^2+v^2)."""
    u, v = fmpq_poly([1]), P / 14
    numerator = u * v.derivative() - v * u.derivative()
    denominator = u * u + v * v
    return CUR * denominator == RHO * numerator and 196 * denominator == RHO


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--certificate', type=Path, required=True)
    parser.add_argument('--entry', type=int, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()

    exact = {
        'normalization_int_rho': str(exact_full_integral(RHO) / 220),
        'IF_cross_moment_int_t_f_dmu_times_220sqrtpi': str(exact_full_integral(T * CUR)),
        'first_moment_int_f_dmu_times_220sqrtpi': str(exact_full_integral(CUR)),
        'fourier_image_of_p_times_gaussian_equals_p': fourier_image_of_even_polynomial(P) == P,
        'phase_derivative_equals_CUR_over_RHO': phase_derivative_identity(),
    }
    assert exact_full_integral(RHO) == 220
    assert exact_full_integral(T * CUR) == 0 and exact_full_integral(CUR) == 0
    assert exact['fourier_image_of_p_times_gaussian_equals_p']
    assert exact['phase_derivative_equals_CUR_over_RHO']
    # Negative control: a non-invariant even polynomial must be rejected.
    exact['control_t2_not_invariant'] = fourier_image_of_even_polynomial(T * T) != T * T
    assert exact['control_t2_not_invariant']
    # Exact witness that the cap cannot be lowered to 3: f(9/5) > 3.
    witness = CUR(fmpq(9, 5)) / RHO(fmpq(9, 5))
    exact['f_at_9_over_5'] = str(witness)
    assert witness > 3

    cx = convex_order_certificate(Fraction(1, 100), Fraction(301, 100))
    cert = load_certificate(args.certificate, args.entry)
    main_check = check_certificate(cert, 'submitted certificate')
    controls = []
    for beta in ('0', '1', '-41/25', '3'):
        total = certificate_total(cert, ChirpData(Fraction(beta)))
        controls.append({'chirp_beta': beta, 'total': str(total),
                         'nonnegative_as_required_by_feasible_wigner': bool(total >= 0)})
    mutations = []
    negated = dict(cert, h=[-x for x in cert['h']], k=[-x for x in cert['k']])
    mutations.append(check_certificate(negated, 'negate h and k'))
    lowered = dict(cert, a=[x - Fraction(1, 50) for x in cert['a']])
    mutations.append(check_certificate(lowered, 'subtract 1/50 from a'))
    bad_cap = convex_order_certificate(Fraction(1, 10), Fraction(3))
    result = {
        'started_utc': started,
        'python_flint': flint.__version__, 'arb_precision_bits': ctx.prec,
        'exact_identities': exact,
        'convex_order': cx,
        'joint_certificate': {**main_check,
                              'cells': len(cert['a']), 'box_half_width': str(cert['edges'][-1]),
                              'outside_constants_Aminus_Bminus_H_K':
                                  [str(x) for x in outside_constants(cert)]},
        'feasible_chirp_controls': controls,
        'mutation_controls': mutations,
        'mutation_cap_3_convex_order': {k: v for k, v in bad_cap.items() if k != 'rows'},
    }
    result['verdict'] = bool(cx['accepted'] and main_check['accepted'] and
                             all(c['nonnegative_as_required_by_feasible_wigner'] for c in controls) and
                             not any(m['accepted'] for m in mutations) and not bad_cap['accepted'])
    result['ended_utc'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    summary = {k: v for k, v in result.items() if k != 'convex_order'}
    summary['convex_order'] = {k: v for k, v in cx.items() if k != 'rows'}
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
