# Plan E14e: are the interval-feasible J != 0 leaves killed by patterns with 2 or 3 intervals? (pre-registered before running)

Owner OlsonReflectionRigidity.  Pre-registered 2026-10-18 ~08:10 PDT.  Follows plan-E14c.md and plan-E14d.md.  E14c and E14d found
interval-feasible data with J != 0 in regime III cells (C1-C4, D2).  Every proper interval avoids its window there, so if those
data were avoiders they would be RES_<(p) avoiders.  This is a finite aid and not a premise.
Test.  Leaves are regenerated with the same seeds and the same functions as E14c/E14d, via code/e14e_kills.py.
- For every leaf with J != 0 (at most 400 per configuration) and for a control sample of J = 0 leaves (at most 100 per
  configuration), every pattern with m = 2 is tested against its window.  The window is that of B0S-r4 Imports:
  I(P) = [-g_m(R - E), g_m(E)], g_m(E) = min(p - m, E + m - kappa - 1, floor(E/2)).
- Leaves not killed by m = 2 are then tested with m = 3.
Configurations C1 (13, 6, 13), C3 (13, 6, 14), C4 (11, 5, 11) and D2 (17, 7, 18).  C2 (k = 33) is too large for m = 3 in this budget.
Recorded per configuration:
- the number of leaves tested;
- the number killed at m = 2;
- the number killed at m = 3;
- the number not killed by any pattern with m <= 3;
- for the first 3 unkilled leaves, the datum and the values.
An unkilled leaf is NOT a counterexample: patterns with m >= 4 are not tested, and an unkilled leaf would be reported as such.
