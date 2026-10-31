#!/usr/bin/env python3
"""Exact rational independent sign brackets; no numerical source solver."""
from fractions import Fraction as F
import json


def parts(m, g):
    a = m + 2*m*m
    b = m + 6*m*m + 6*m*m*m
    c = m + 14*m*m + 36*m*m*m + 24*m*m*m*m
    d = g*g + 2*m*g + a
    n = g**4 + 4*m*g**3 + 6*a*g*g + 4*b*g + c
    dp = 2*g + 2*m
    np = 4*g**3 + 12*m*g*g + 12*a*g + 4*b
    return d, n, np*d - n*dp


def bracket(m, lo, hi, steps=60):
    if not (parts(m, lo)[2] < 0 < parts(m, hi)[2]):
        raise RuntimeError("invalid sign bracket")
    for _ in range(steps):
        mid = (lo + hi) / 2
        if parts(m, mid)[2] < 0:
            lo = mid
        else:
            hi = mid
    return lo, hi


def main():
    low_m = F(1, 100000000)
    s = F(1, 100)
    lo, hi = bracket(low_m, s / 2, 2*s)
    pred = s + s*s/2 - F(5,8)*s**3
    midpoint = (lo + hi) / 2
    d, n, _ = parts(low_m, midpoint)
    root_beyond_s4 = hi < pred - s**4
    root_within_10s4 = pred - 10*s**4 < lo and hi < pred + 10*s**4
    third_term_bound = abs(midpoint - pred) < s**4
    w_mid_bound = abs(n/(2*d) - (s*s + 2*s**3 + F(3,2)*s**4)) < s**5
    if not (root_beyond_s4 and root_within_10s4 and not third_term_bound and w_mid_bound):
        raise RuntimeError("low-privacy rational diagnostic disagrees")
    high_m = F(1000)
    hlo, hhi = bracket(high_m, F(1,2), F(1))
    hd, hn, _ = parts(high_m, (hlo+hhi)/2)
    scaled = high_m*(hn/(2*hd) - 6*high_m*(high_m+1) - F(1,2))
    if not (-F(1,20) < scaled < -F(1,25)):
        raise RuntimeError("high-privacy diagnostic disagrees")
    print(json.dumps({
        "method": "60-step exact Fraction bisection on sign of independently differentiated N/D",
        "low_m": str(low_m), "low_root_lo": str(lo), "low_root_hi": str(hi),
        "entire_low_root_bracket_farther_than_s4": root_beyond_s4,
        "entire_low_root_bracket_within_10s4": root_within_10s4,
        "midpoint_within_s4_of_three_term_offset": third_term_bound,
        "midpoint_cost_within_s5_of_three_term_cost": w_mid_bound,
        "high_m": str(high_m), "high_root_lo": str(hlo), "high_root_hi": str(hhi),
        "high_scaled_correction_in_minus_1over20_to_minus_1over25": True,
        "limits": "Only selected rational diagnostic; optimizer branch/uniqueness and asymptotic big-O require the separate written arguments."
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
