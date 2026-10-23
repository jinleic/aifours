# Plan E14f: kills by patterns with few intervals in IIIb (R <= 2 kappa) (pre-registered before running)

Owner OlsonReflectionRigidity.  Pre-registered 2026-10-18 ~08:15 PDT.  Follows plan-E14e.md.  E14e found that every tested
interval-feasible leaf of the IIIa cells C1, C3, C4 and D2 (J != 0 and J = 0 alike) is killed by a 2-interval pattern.  This is a
finite aid and not a premise.
Question.  In IIIb the interval windows are empty when R < 2 kappa, and a single residue when R = 2 kappa.  What is the smallest
m whose patterns kill the interval-feasible leaves there?
Configurations (p, kappa, R), drawn as in E14b (code/e14b_cfunc_general_v2.py make_datum, seeded), with leaves enumerated by
e14's run_datum:
- F1 (7, 4, 7), 10 data, at most 300 leaves each;
- F2 (11, 6, 11), 8 data, at most 150 each;
- F3 (13, 7, 14) (R = 2 kappa), 8 data, at most 150 each;
- F4 (11, 6, 12) (R = 2 kappa), 8 data, at most 150 each.
Per leaf, m = 2, 3, 4 are tried in turn (m = 4 for at most 30 leaves per configuration), and the first m that kills is recorded.
Recorded: a histogram of the minimal killing m (or "none for m <= 4") and up to 3 examples of leaves not killed by m <= 3.
The code is code/e14f_kills_iiib.py, which imports killed_by from code/e14e_kills.py unchanged.
