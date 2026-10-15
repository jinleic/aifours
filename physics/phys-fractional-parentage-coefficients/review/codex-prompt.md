You are a hostile, expert referee (mathematical physics: angular momentum algebra, seniority /
quasi-spin, SO(5) ⊃ SO(3), quadratic forms over function fields). Review the project in the current
directory, which attacks the book problem "Solve the recurrence relation of the fractional parentage
coefficients" (closed forms for one-body CFPs of N identical spin-f bosons in total-spin eigenstates,
beyond spin 1). Read README.md, STATUS.md, RESULTS.md, and the code in code/ (results in results/).
You may only read files in this directory. Do NOT write or modify any file and do NOT delegate to
other agents or tools. If your sandbox allows running Python, you may run the read-only checks
(e.g. `python code/selftest.py`), but none is required; the exact outputs are quoted in RESULTS.md.

Claims to referee (see RESULTS.md for full statements and proofs):
A. Theorem A: for every integer spin f (D = 2f+1) and N = v + 2n, the one-body CFP factorizes as
   sqrt(v(N+v+D-2)/(N(2v+D-2))) * r for seniority v -> v-1, and
   (-1)^(L+L') sqrt((N-v)(v+D-2)/(N(2v+D-2))) sqrt(dim_v(2L'+1)/(dim_{v+1}(2L+1))) * r' for v -> v+1,
   with r, r' the N = v reduced CFPs; spin-1 Bao-Li formula as f = 1.
B. Theorem B: closed forms (in v and f) of the five reduced CFPs of near-stretched states
   L = fv-2, fv-3 for all f >= 2, derived symbolically in "deficit coordinates".
C. Spin 2: top families L = 2v - k, k <= 8, exact rational functions of v in two Gram-Schmidt bases;
   reproduction of Pan, Bao, Zhang, Draayer, EPJ Plus 129, 169 (2014) Table III (14/14) and
   Table IV (8/8 multiplicity-free rows).
D. Theorem D (no-go): for the two-dimensional multiplicity families k in {6,8,9,10,11}, no
   Q(v)-rational unit vector has a CFP into a multiplicity-free daughter whose square is
   (rational)^2 * const * product of (v - t), t in an explicitly bounded set T; proof by quaternion
   algebra residues (tame symbols) plus a bounded search for rational points of w^2 = -Delta_k(s).
   Optimality claim: for k = 6 the trio-first basis has exactly one irreducible quadratic factor.
E1. Theorem E1: weight of a scalar (L'=0) parent: (2v+D-2)(v+D-3)/(D v (2v+D-4)).
E2. Conjecture E2: 26 product formulas for spin 2, L <= 5, arbitrary seniority, checked exactly
   at 800 table entries (v <= 88). Labelled as a conjecture, not a theorem.
Also referee STATUS.md (citations, what is called settled/open, reading-key honesty).

Your tasks, as a hostile referee:
1. Try to falsify each claim: check hypotheses, quantifiers, domains of validity (small v, v
   residues, existence of states), phase/sign conventions, and every step of the proofs of A, B, E1, D.
2. Theorem D specifically: is "q represents c iff (c*q11, -Delta) splits" correct for the binary form
   q = <q11, q11*Delta>? Are the residue (tame symbol) formulas, the treatment of constants c0, of
   places with even valuation, of the place at infinity, and of non-linear places correct and
   complete? Is the reduction "CFP^2 is Bao-Li type iff q(x) lies in L_T * squares" valid (C_d linear
   type, b_d(x) != 0)? Is the scope statement (rational bases only; T bounded; conditional beyond T)
   accurate, or is anything overstated? Is the optimality claim for k = 6 justified?
3. Check the symbolic method of B/C: is the deficit-coordinate reduction valid for all v >= v0 (no
   hidden degeneration at special v; multiplicity counts; harmonic projection formula)?
4. Check numerics/exactness: is any claim dependent on floating point or on unchecked ranges?
5. Check citations and novelty wording: anything that should be labelled known/reproduction rather
   than new; any wrong bibliographic detail you can detect from the text.
6. Point out unclear or misleading wording in README/RESULTS.

Output format: a numbered list of findings, each with severity (critical / major / minor / nit),
the exact file and section, what is wrong, and a concrete fix. Then a short overall verdict per
claim (A, B, C, D, E1, E2, STATUS): accept / accept with fixes / reject.
