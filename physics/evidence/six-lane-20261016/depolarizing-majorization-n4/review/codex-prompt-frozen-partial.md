You are a hostile referee. Read-only sandbox (write nothing). Working directory: a frozen proof package for a
PARTIAL result on the four-qubit case (d = 2, n = 4) of the depolarizing-output majorization conjecture, Eq. (2) of
arXiv:2609.37240v1 (`swtf-2609.37240v1.pdf` / `.txt` here). Main document: `PROOF.md`. Supporting files:
`u2_dual_certificates.json` (rational dual certificates), `u2_dual_cert.py` (generator + exact checker),
`twirl_lp_exact.py` (closed-form exact LP via sympy), `twirl_ppt_lp.py` (independent float build with explicit
256x256 matrices), `n4.py`, logs (`u2_dual_cert.log`, `u2_lp_mutation_controls.log`, `exact_U2.log`, `exact_U3.log`),
`SHA256SUMS`.

Check adversarially and independently:
1. Section 1: expansion coefficients a_s; the common-order lemma and the Hamming alignment of the T_s; every
   "trivial index" claim for U_0..U_4; Consequence R1.
2. Section 2: the n = 4 spin-flip identity, D = D+ - a_3 rho~, the exact sign conditions (b_1 >= 0 iff p >= 2/3),
   Y+ = Y + a_3 |1111><1111| and K_k(Y+) = K_k(Y) for k <= 15; the reflection p -> 2 - p.
3. Section 3: validity of every relaxation constraint for sigma (x) Pi; the bilinear form with J; G-invariance of
   the constraint set AND of the objective (including the partial-transpose conjugation formula); the commutant claim
   (multiplicity-free, 16 projectors E_S); the closed forms (traces, Tr_Pi, partial transposes, eigenvalues g, the
   objective C(|S|,s) 2^s 3^{4-|S|}); the dual LP and weak duality.
4. Recompute exactly (your own Fraction/sympy code, not the provided checker) that each stored certificate in
   `u2_dual_certificates.json` is dual-feasible with bound equal to K_k(T_2) for k = 1..5 and 11..15. Also verify
   independently (e.g. by building J and E_S explicitly) a few objective coefficients and PPT rows.
5. Section 4: do the stated conclusions follow exactly? Anything overstated? Are any of these indices already
   implied by known results (King's multiplicativity; SWTF's own theorems, e.g. log-determinant / Schur-concave
   results in the pinned paper)?
Output a JSON object: {"verdict": "ACCEPT" | "ACCEPT-WITH-FIXES" | "REJECT", "checks": [{"item","pass","note"}],
"independent_tests": {...}, "findings": [{"severity","issue","fix"}], "novelty_assessment": {...}}.
