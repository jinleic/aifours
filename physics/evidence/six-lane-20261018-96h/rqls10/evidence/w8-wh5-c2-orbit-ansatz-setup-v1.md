# W8: the projective Z_5^2-orbit ansatz for B = Cay(Z_10) (WH_5 (x) C^2) - setup for a cheap numerical test

Recorded 2026-10-19T01:09:04-0700. Lane-internal; unreviewed; restricted ansatz; no existence claim. Companion of R11
(evidence/restricted-results-v4-z5sq-linear-orbit.md, sha256 30b3a3a0f68e78f455160d111615aeb14c8ee9c85b86270b7439f5b64c3fc469),
which excludes the linear (character) case.

**Ansatz.** As in R11 but pi(a,b) = X^a Z^b (x) I_2 on C^5 (x) C^2 (the nontrivial cocycle class of Z_5^2; its irreducible
representation is Weyl-Heisenberg of dimension 5, here with a 2-dimensional multiplicity space). Representatives
x_ab (a, b in Z_2) are 5 x 2 matrices; for a basis vector e of C^5 write e(x) = (<e| (x) I) x in C^2.

**Reduction (exact).** Rows: for every vector t of the computational basis (eigenbasis of Z), ||t(x_r)||^2 = 1/5 for all
four r and t(x_00) orthogonal to t(x_01), t(x_10) orthogonal to t(x_11). Columns: the same in the Fourier basis (eigenbasis
of X) for the couples 00-10, 01-11. Classes: the same in the eigenbasis of X Z^-1 for the couples 00-11, 01-10.
(Each line is a union of two orbits of a cyclic maximal isotropic subgroup; Fourier inversion on Z_5 gives the
per-basis-vector conditions.) Unknowns: 80 real minus U(2) x phases; conditions: 3 bases x 5 vectors x 8 real = 120.
Maximal cardinality is generic: (W (x) I) x_r is parallel to x_r only if x_r lies in an eigenspace of W (x) I.

**Controls available.** The same construction with p = 3 (WH_3 (x) C^2, B = Cay(Z_6)) must have no solution because no
1-RQLS(6) exists [IMPORT Ball-Simoens via Zhang-Cao] - a negative control. The p = 7 analogue concerns order 14 (also
open). Proposed as a cheap Levenberg-Marquardt stage (seconds per thousand starts) in a later assay version, after the
pending v7 calibration; nothing has been run for it.
