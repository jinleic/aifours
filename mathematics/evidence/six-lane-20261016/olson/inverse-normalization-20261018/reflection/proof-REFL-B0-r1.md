# Corollary REFL-B0: REFL(p) for avoiders with all rotation letters equal, without a bound on o_F

Owner OlsonReflectionRigidity.  Written after host clock 2026-10-18T12:06:01-0700.  Status: written proof [W], UNREVIEWED.
It is a short composition of accepted results (imports below).  Its only new content is the observation that for B = 0 the
reduction process of Theorem RED uses only the moves P1 and P2, which keep R and do not increase kappa.
Scope: words whose rotation letters are all EQUAL.  Nothing about mixed rotation letters, rotation values in general,
INV*(p) as a whole, or ordered Olson.

## Statement

**Corollary REFL-B0.**  Let p >= 5 be prime, and let w0 be an avoider of length 4p - 2 over D_(2p) all of whose rotation letters
are equal to one rho_x, x != 0.  Put R := the number of rotation letters and kappa := p - 1 - sum_i floor(l_i/2), the sum running
over the MAXIMAL CONSTANT reflection blocks of w0.  Suppose
   R >= 4 kappa - 4,   2 kappa <= p - 1,   and   ( R >= p + kappa - 2  or  5R >= 4p + 6 kappa - 10 ).
Then every maximal cyclic reflection run of w0 is constant.
There is no hypothesis on o_F(w0); compare proof-REFL-fewodd-r5.md, which needs o_F <= p but allows rho_(+-x) mixed.

## Imports (accepted texts)

* Theorem RED and its proof: proof-RED-r2.md (c4e7697f...d3d7), parent-accepted (R/olson-reflection-K0star-RED-parent-verdict-v1.md,
  879aeee7...c02a), with its standing imports (I1)-(I4), K0*, and the move lemmas of proof-K0star-r2.md (6681676e...96e1).
  As in proof-REFL-fewodd-r5.md Sec. 2, every citation is to the accepted r2 texts.
* The small-k verdict: R/olson-reflection-smallk-parent-verdict-v1.md (b71fcaf4...13b8), L3 and L13: no RES_<(p) avoider with
  k <= p.
* Theorem B0S-CJ''' with Corollary 2: proof-B0SCJx-r4.md (f2779c24...843d), read with proof-B0SCJ-r2.md (f90c8b53...c0ed) and
  the parent overlay R/olson-cj-cjx-parent-verdict-v1.md (5cfd6a4f...45f6d; CORRECTNESS-ACCEPTED at its exact partial scopes).
  Used: if a B = 0 word with all blocks odd, kappa >= 1, k >= p + 1, R >= 4 kappa - 4 and 2 kappa <= p - 1 avoids, then
  Delta >= 2 and p < kappa + 5 Delta - 5, where Delta = k - p - kappa - 1.

## Proof

Suppose w0 violates the conclusion.  The proof of Theorem RED (RED-r2 L136-164) first normalises x = 1.  Then every rotation is
rho_1, so A = R and B = 0, and A >= B holds already.  It then applies P1-P4.
* P3 needs a run with a, b >= 1, and P4 needs a (1,1)-run.  Neither exists when B = 0, and B stays 0 under P1 and P2
  (RED-r2 L137: "TR keeps A, B; M0' lowers both by 1; the other moves keep them").  So only P1 (FUS) and P2 (PM0) occur.
* Neither move changes any rotation letter, so R is constant.
* kappa is non-increasing.  FUS changes H only in an odd-odd double fusion, where H rises by 1 (K0star-r2 L95-97).  PM0 appends an
  even block to an odd one and keeps H, since floor(l/2) + l'/2 = floor((l + l')/2) for l' even.
The exits with g = 0 are contradictory there.  So the terminal state w_T is an avoider in RES_<(p) with B = 0 and
kappa' := kappa(w_T) >= 2, kappa' <= kappa, R(w_T) = R, all blocks odd.  Hence k' := k(w_T) = 2p - R + 2 kappa' by (0.1).
* If k' <= p, the small-k verdict excludes w_T.
* If k' >= p + 1: R >= 4 kappa - 4 >= 4 kappa' - 4 and 2 kappa' <= 2 kappa <= p - 1.  So B0S-CJ''' applies to w_T, and it forces
  Delta' >= 2 and p < kappa' + 5 Delta' - 5, with Delta' := k' - p - kappa' - 1 = p + kappa' - 1 - R.
  - Delta' >= 2 means R <= p + kappa' - 3 <= p + kappa - 3, which contradicts the first alternative.
  - p < kappa' + 5 Delta' - 5 means 5R < 4p + 6 kappa' - 10 <= 4p + 6 kappa - 10, which contradicts the second.
Either way w_T cannot exist: a contradiction.  []

## Remarks

(1) Example of the range at p = 31, kappa = 7: the conditions hold for every R >= max(24, 36) = 36, i.e. for R in [36, 61].  Since
R >= 4 kappa - 4 = 24 and p + kappa - 2 = 36 (and 5R >= 156, i.e. R >= 32), they hold for all R >= 32.  The words may have any
number of odd blocks; for comparison k = 2p - R + 2 kappa is as large as 44 at R = 32, while o_F(w0) can be larger still.
(2) The same composition with the original B0S-CJ (R >= 4 kappa + 1) is contained in this one.
(3) Mixed rotation letters (B >= 1 after normalisation) are not covered.  There P3 and P4 change R, kappa and B, and no B >= 1
analogue of B0S-CJ for k >= p + 1 exists yet.
