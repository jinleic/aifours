# Plan E14c: IIIa cells where middle-middle wraps are arithmetically possible (pre-registered before running)

Owner OlsonReflectionRigidity.  Pre-registered 2026-10-18 ~07:55 PDT.  Follows plan-E14b.md (d71ab2d0...ccfa).  This is a finite
aid and not a premise.  The code is code/e14b_cfunc_general_v2.py (f8729c90...b905), imported unchanged by a new driver
code/e14c_driver.py, which only changes the configuration list.

Motivation.  In IIIa (2 kappa < R <= 4 kappa - 3), an upward wrap in a split of an interval needs
beta(m1) + beta(m2) + alpha(m1 + m2) >= theta+ := 2R - p - 3 kappa + 3.  The E14/E14b cells all had theta+ >= 1, where wraps need
light or heavy extensions.  Cells with theta+ <= 0 allow wraps between two middle parts.  Does c = 0 survive there?

Configurations (p, kappa, R), all IIIa:
- C1 (13, 6, 13), theta+ = -2;
- C2 (17, 8, 17), theta+ = -4;
- C3 (13, 6, 14), theta+ = 0;
- C4 (11, 5, 11), theta+ = 0.
Data are random (seeded) as in E14b: 15 data per configuration, at most 600 leaves each.
Recorded: the same statistics as E14b.
Decision use.  If c = 0 holds here too, exact additivity is a general IIIa phenomenon, and a proof must not rely on theta+ >= 1.
If c != 0 occurs, the examples show which split fails.
