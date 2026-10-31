#!/usr/bin/env python3
"""Exact independent triangular-kernel polygon integration, no author code.

Synthetic density only: S=D, b=1/2; this is not a LAW642 optimum assertion.
"""
from fractions import Fraction as Q


def clip(poly, a, b, c):
    """Clip a rational polygon against a*x+b*y <= c."""
    if not poly:
        return []
    out = []
    for p, q in zip(poly, poly[1:] + poly[:1]):
        dp = a * p[0] + b * p[1] - c
        dq = a * q[0] + b * q[1] - c
        if dp <= 0:
            out.append(p)
        if (dp < 0 < dq) or (dq < 0 < dp):
            s = dp / (dp - dq)
            out.append((p[0] + s * (q[0] - p[0]),
                        p[1] + s * (q[1] - p[1])))
    return out


def integral(poly, sx, sy):
    """Integrate (1-sx*x)(1-sy*y) by exact triangular moments."""
    if len(poly) < 3:
        return Q(0)
    p = poly[0]
    total = Q(0)
    for q, r in zip(poly[1:-1], poly[2:]):
        area = abs((q[0] - p[0]) * (r[1] - p[1]) -
                   (q[1] - p[1]) * (r[0] - p[0])) / 2
        xs = [p[0], q[0], r[0]]
        ys = [p[1], q[1], r[1]]
        ix = area * sum(xs) / 3
        iy = area * sum(ys) / 3
        ixy = area * (sum(xs) * sum(ys) + sum(x*y for x, y in zip(xs, ys))) / 12
        total += area - sx*ix - sy*iy + sx*sy*ixy
    return total


def quadrants():
    for sx in (-1, 1):
        for sy in (-1, 1):
            lo_x, hi_x = (Q(-1), Q(0)) if sx == -1 else (Q(0), Q(1))
            lo_y, hi_y = (Q(-1), Q(0)) if sy == -1 else (Q(0), Q(1))
            yield sx, sy, [(lo_x, lo_y), (hi_x, lo_y),
                           (hi_x, hi_y), (lo_x, hi_y)]


def kernel_mass():
    return sum((integral(poly, sx, sy) for sx, sy, poly in quadrants()), Q(0))


def tail_sum_gt_one():
    return sum((integral(clip(poly, -1, -1, -1), sx, sy)
                for sx, sy, poly in quadrants()), Q(0))


def synthetic_q(x1, x2, t):
    # x-tu is always in the positive quadrant for this fixed input family.
    if min(x1, x2) <= t:
        raise ValueError("synthetic quadrant condition not satisfied")
    z0 = x1 + x2 - 1
    total = Q(0)
    mass = Q(0)
    for k in range(1, 12):
        for sx, sy, poly in quadrants():
            # k-1 <= z0-t*(u+v) <= k; edges have zero area.
            poly = clip(poly, -t, -t, Q(k)-z0)
            poly = clip(poly, t, t, z0-Q(k-1))
            weight = integral(poly, sx, sy)
            mass += weight
            total += Q(1, 2)**k * weight
    if mass != 1:
        raise ValueError(f"shells did not cover entire kernel: {mass}")
    return total / 12


def main():
    norm = kernel_mass()
    alpha = tail_sum_gt_one()
    t = Q(1, 4)
    q = synthetic_q(Q(3), Q(13, 4), t)
    q_shift = synthetic_q(Q(4), Q(13, 4), t)
    print("kernel_mass:", norm)
    print("polygon_tail_mass_sum_gt_one:", alpha)
    print("independent_polygon_q:", q)
    print("independent_polygon_q_shift:", q_shift)
    print("exact_shift_ratio:", q_shift / q)
    if (norm, alpha, q, q_shift) != (Q(1), Q(1, 24), Q(25, 18432), Q(25, 36864)):
        raise SystemExit("FAIL: exact polygon result does not match")
    print("PASS: direct rational polygon integrals and shifted density agree")


if __name__ == "__main__":
    main()
