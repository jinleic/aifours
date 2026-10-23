# k62-m13-mixed checkpoint 001 — scope frozen; input change recorded; first new mixed-family tool found (unwritten)

- **Written:** `/bin/date` read at 2026-10-19T12:46:29-0700, immediately before this file. Work started 2026-10-19T12:29:49-0700.
- Owner SunM13MixedFibres; written mathematics only; no computation, process, model call or nested agent. Python is
  used only as an exclusive-create (`open(path, 'x')`) file writer and for sha256 of my own files.
- **Frozen scope:** `K62-M13X-SCOPE-v1.md`, sha256 072c509805f89b8cfff7f57c97ff4508f1a7aca6925977fb341198881497bf01 (written before any derivation).

## Input change (parent IRC 12:42:57, recorded as required)
M13 A-D is now CORRECTNESS_ACCEPTED_SCOPED_PARTIAL: verdict
`RUN/review/sun7-K62-M13-parent-verdict-v1.md` sha256 2fac7a30ab4b832166c770492fdd6d0f555660e5c3eabcb95d514797a39c4e34,
read in the order A-D, worker overlay K62-M13-erratum-v1 (a4c476c1…), parent erratum
`RUN/review/sun7-K62-M13-parent-erratum-v1.md` (99276f6d66c15c15d55cfa0346440d9db3b244a8a4b5eb40e5bae5a92d549e29). Its 8
statements may be cited exactly at that scope (unmarked centres/apexes; DG* only under each family's r_Q <= 4). Rows at t
and p, global graph conclusions, (4,4,4) tau = 8 and the e_d >= 5 alternative stay OPEN and are not premises. R2MIX stays a
candidate: re-prove or label conditional. The frozen scope is unchanged; this widens only the citable premise set.

## Actual result so far (thought only; nothing yet frozen as a claim; all CANDIDATE_UNVERIFIED)
1. **Subset granularity (SG), mixed-family:** for x in {alpha, alpha*} and R a non-empty subset of O, the chain for
   T_x({d} cup R) taken d first has every multiplier after the first O-step in {1, 2}: a multiplier 3 forces
   (Pi^x_d cap Pi^x_e)(Pi^x_d cap Pi^x_c) = Pi^x_d, which by product separation (R2MIX Lemma 2, to be re-proved) forbids c, e from
   sharing a d-fibre of the x-configuration; but deg_d(c) + deg_d(e) = n_d there, so #both = #neither >= 1 (d's own fibre).
   Hence gcd(n_v, T_x'(V minus {v, i*})) = 6 at EVERY v in O, marked (t, p) or not.
2. **Consequence (subset row bound):** at every v in O, both families, every feasible weight with y_(i*) = 0 has value <= 5/6.
   With plain LFC this gives, at t and p as well: each O-row (both families) has at least one entry 4 and at most one
   entry 1; no R2-row at t in either family (the (1,1) lemma L-R2 of R2MIX follows the same way without its Prop. 5).
3. **Tightness reformulation at d (M13 only):** alpha_dj + alpha*_dj = g_dj for every j != d, so with g_d = 1 a left
   U_d-coset F has S_F = {j : F cap U*_j = empty} in Gamma and S*_F = {j : F cap U_j = empty} in Gamma*.
4. **Inverted d-count with alpha-granularity at (c, i*):** #{F : c, i* in S*_F} >= n_d/4 + n_d/gcd(n_d, T_alpha({c, i*}));
   summed over O' with the cap structure: sum over u in O' of 1/gcd(n_d, T_alpha({u, i*})) <= 1/2.

## Blocker
No exclusion of M13 yet: items 1-4 are necessary constraints. The (1,1) route of R2MIX fails verbatim here (inverted
d-system has i*-degree 3n_d/4 and four-piece {t, i*, u, u'} fibres; gcd 9 for t/i* labels), as expected.

## Next bounded action
Write items 1-4 with full proofs into the candidate file; then attack the full target by coupling the four-piece
inverted d-fibres with the t-row and i*-row (subset granularity, product separation at t/i*), retaining every failed
arithmetic. Next checkpoint by 13:15 (target), 13:25 at the latest.
