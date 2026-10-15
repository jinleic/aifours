You are a hostile, expert referee (integrable systems, Hirota bilinear method, computer algebra). Review the
research folder in the current working directory. Do NOT delegate to other agents. Do NOT create, modify or
delete any file. You may read every file in this folder, and you may run read-only computations, e.g.

    cd code && /Users/jinleic/jinleic-workspace/scratch/ai4s-venv/bin/python -c "import two_function_3ss as T; print(T.part_C({}))"

(the part_* functions take a dict and do not write; the scripts' main() functions write results/*.json, so do
not run main()). Precomputed outputs are in results/*.json. You may use web search only to check literature.

## Context

Book problem (source/problem.zh.txt, page images source/*.png): Lou & Li conjecture that if the bilinear
system (1) P(D_x,D_t)F·G = 0, Q(D_x)P(D_x,D_t)F·G = 0 is integrable then (2) P F·G = 0, R(S)P F·G = 0 may be
integrable (S an extra-dimension / discrete / supersymmetric Hirota operator, often R = Q). STATUS.md gives the
literature; RESULTS.md the definitions, claims and proofs; README.md the summary.

## Claims to attack (details and proofs in RESULTS.md)

- C1: diagonal reduction, (2) passes the generic N-soliton test ⇒ (1) passes (Q = D_x, R = D_y).
- C2: for odd P the two-function recursion at a_i = b_i reproduces the single-function Hirota test; so a
  single-function three-soliton failure implies the two-function failure.
- C3: for P = D_t + p(D_x), deg p ≤ 3, systems (1) and (2) pass the generic three-soliton test (two free
  amplitudes for odd p; all F/G patterns otherwise), by exact symbolic identities (code/two_function_3ss.py
  Part A).
- C4 (main theorem, Theorem 4.4): for P = D_t + p(D_x) with deg p ≥ 4 both systems fail the 3-soliton test;
  hence (1) passes ⇔ (2) passes ⇔ deg p ≤ 3; Li–Lou's family (D_t + D_x^n) passes only for n = 2, 3. Proof:
  Lemma 4.1 (F F G pattern closed form, multiplier-independent criterion Φ ≠ 0), Lemma 4.2 (Φ_d < 0 for all
  d ≥ 4 at k = (1,2,−4): exact for d ≤ 60, inequality for d ≥ 30), Lemma 4.3 (lower-order terms via a
  polynomial-in-s argument).
- C5 (counterexample to the single-function reading): D_x(D_t + D_x^5) f·f = 0 (Sawada–Kotera) is integrable
  but D_y(D_t + D_x^5) f·f = 0 fails Hirota's three-soliton condition; the exact obstruction factorization in
  results/single_function_3ss.json; witness k = (1,2,3), l = (1,3,7) with coefficient 3600/247; independent
  check in code/direct_substitution_check.py.
- C6–C8: N = 4, 5 checks (exact random points; symbolic N = 4 status in RESULTS.md), discrete R(S) = sinh(D_n),
  floating-point exploratory scan outside the class.

## What to do

1. Falsify. Check every definition (seeds, generic test, type patterns), quantifier, hidden assumption and
   degenerate case. Is the "generic N-soliton test" a fair operationalization of "integrable" for these
   two-function systems? Could the systems admit other multi-soliton families that the test misses, and does
   that weaken any stated claim as worded?
2. Check the proofs line by line, especially Lemma 4.1 (re-derive the closed form), Lemma 4.2 (the bounds and
   all nondegeneracy conditions for every d ≥ 4), Lemma 4.3 (does the leading-coefficient argument hold for
   every p of degree ≥ 4, including odd p with two-amplitude seeds and p with mixed parity?), C1 (the
   specialisation l = k) and C2.
3. Check the code: does hirota_ns.py implement the coefficient formula and recursion correctly (signs,
   submask enumeration, the 2x2 solve, callable symbols)? Do the scripts test what RESULTS.md says they test?
   Re-run small pieces if useful.
4. Check the wording: overclaims, "proved", "counterexample", novelty statements, and whether the verdict
   (PARTIAL for the literal reading, COUNTEREXAMPLE for the single-function reading) is justified. Check the
   literature claims in STATUS.md (especially: is Theorem 4.4 or the single-function counterexample already in
   the literature, e.g. Hietarinta 1987 papers II/III, Wang et al. 2024, or later work?).

## Output format

A numbered list of findings. For each: severity (fatal / major / minor / nit), the exact location
(file and section or line), what is wrong, and a concrete fix. Then a short overall assessment of each claim
C1–C8 (correct / correct with fixes / wrong / unverifiable). Be concise and specific.
