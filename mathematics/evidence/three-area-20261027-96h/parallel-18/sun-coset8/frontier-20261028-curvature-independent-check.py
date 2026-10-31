#!/usr/bin/env python3
"""Independent exact split identity and bounded Volterra curvature example.

The floating midpoint calculation illustrates one deterministic SDE output,
not the universal theorem or the original strict-E2 endpoint question.
"""
from fractions import Fraction as Q
from math import cos, isqrt, pi, sin, sqrt


def exact_split():
    tested = 0
    for a in range(21):
        for b in range(21):
            c2 = a*a + b*b
            c = isqrt(c2)
            if not c or c*c != c2:
                continue
            n = Q(c)
            direct = (Q(b*b) - Q(b**4, c2)) / n
            split = Q(a*a*b*b, c**3)
            if direct != split or split > n/4 or split < 0:
                raise SystemExit("FAIL: rational split-curvature identity")
            tested += 1
    print("exact_pythagorean_split_cases:", tested)
    print("exact_split_identity_and_U_over_4_bound: PASS")


def volterra_example():
    n = 20000
    tau = 0.4
    h = 1.0/n
    w2_before = w2_after = z2 = ztail2 = z_dot_tail = 0.0
    for i in range(n):
        t = (i + 0.5)*h
        w = cos(pi*t/2)
        z = (2/pi)*sin(pi*t/2)
        ztail = 0.0 if t < tau else (2/pi)*(sin(pi*t/2)-sin(pi*tau/2))
        if t < tau:
            w2_before += w*w*h
        else:
            w2_after += w*w*h
        z2 += z*z*h
        ztail2 += ztail*ztail*h
        z_dot_tail += z*ztail*h
    u = sqrt(w2_before+w2_after)
    v = sqrt(z2)
    cin = w2_before*w2_after/(u**3)
    cout = (ztail2-(z_dot_tail/v)**2)/v
    margin = (2/pi)*cin-cout
    print("volterra_midpoint_n:", n)
    print("input_curvature:", format(cin, ".12g"))
    print("output_curvature:", format(cout, ".12g"))
    print("gamma_Cin_minus_Cout:", format(margin, ".12g"))
    if margin <= 0:
        raise SystemExit("FAIL: illustrative curvature comparison")
    print("volterra_curvature_example: PASS (numerical illustration only)")


if __name__ == "__main__":
    exact_split()
    volterra_example()
