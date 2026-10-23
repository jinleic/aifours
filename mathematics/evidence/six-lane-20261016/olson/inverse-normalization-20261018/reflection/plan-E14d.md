# Plan E14d: IIIa cells with theta+ >= 1 but theta- <= 0 (pre-registered before running)

Owner OlsonReflectionRigidity.  Pre-registered 2026-10-18 ~08:00 PDT.  Follows plan-E14c.md.  E14c found c != 0 and J != 0 in
interval-feasible data whenever theta+ := 2R - p - 3 kappa + 3 <= 0.  Its fourth cell (11, 5, 11) has theta+ = -1; the plan
misprinted it as 0.  This is a finite aid and not a premise.
Question.  A downward wrap between two middle parts is arithmetically possible iff theta- := R - 3 kappa + 3 <= 0.  Is c = 0
still observed when theta+ >= 1 and theta- <= 0?
Configurations (p, kappa, R), all IIIa:
- D1 (19, 8, 21): theta+ = 2, theta- = 0;
- D2 (17, 7, 18): theta+ = 1, theta- = 0.
Controls with theta+ >= 1 and theta- >= 1:
- D3 (17, 6, 18): theta+ = 4, theta- = 3;
- D4 (19, 7, 20): theta+ = 3, theta- = 2.
Each configuration uses 12 random data with at most 500 leaves each.  The driver is code/e14d_driver.py; the functions of
e14/e14b_v2 are reused unchanged.
Recorded: as E14c, plus theta-.
