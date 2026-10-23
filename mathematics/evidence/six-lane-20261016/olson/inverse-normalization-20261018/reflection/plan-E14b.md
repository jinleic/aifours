# Plan E14b: c-function structure in regime (III) with general masses, and in R <= 2 kappa (pre-registered before running)

Owner OlsonReflectionRigidity.  Pre-registered 2026-10-18 ~07:30 PDT.  Follows plan-E14.md (84784dc0...f442): E14 found c = 0 on
every proper interval of 152,000 leaves, all of them all-ones data with Delta = kappa - 1.  This is a finite aid and not a premise.
The code is code/e14b_cfunc_general.py, the same DFS and c computation as E14 (ce09e887...9892) with a different data generator.

Question.  Do c = 0 on every proper interval, and J = 0, persist when:
- (A) nonempty runs carry several rotations and Delta < kappa - 1, inside 2 kappa < R <= 4 kappa - 3 ("IIIa");
- (B) R <= 2 kappa ("IIIb")?  Interval windows are empty there, so J != 0 is expected to occur.

Configurations (p, kappa, R).  Each has k = 2p - R + 2 kappa, n_E drawn uniformly from [k - R, 2 kappa], a random composition of R
into k - n_E positive parts, and a random cyclic arrangement:
- A1 (11, 5, 13), Delta = 2;
- A2 (13, 5, 16), Delta = 1;
- A3 (13, 6, 17), Delta = 1;
- A4 (11, 4, 12), Delta = 2;
- A5 (7, 3, 8), Delta = 1;
- B1 (7, 4, 7), all ones, n_E = 8.
Each configuration uses 20 random data (seeded) with at most 1000 leaves per datum.

Recorded per configuration: the number of leaves, the min and max of c, the distribution of J, the number of leaves with some
c != 0, and up to 5 examples.
Decision use.  If (A) shows c = 0 throughout, attempt a proof of "c = 0 on all proper intervals" in IIIa.  (B) only tests whether
IIIb needs multi-interval patterns.  No outcome is a premise.
