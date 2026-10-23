# Corollary REFL-B0: REFL(p) for avoiders with all rotation letters equal, with no imposed bound o_F <= p (r3)

Owner OlsonReflectionRigidity.  r3 written after host clock 2026-10-18T12:12:35-0700: wording only (Main's note).  At length 4p - 2, o_F is
determined: o_F = 2p - R + 2 kappa.  So the corollary imposes no bound o_F <= p, but it does not allow arbitrary o_F at fixed p.
r2 (32671067...c475b) is kept unchanged.  r2 was written after host clock 2026-10-18T12:06:27-0700: Remark (1) corrected (r1, 66375f8f...020e,
printed contradictory ranges; never sent).  Fix map at the end.  r1 was written after host clock 2026-10-18T12:06:01-0700.  Status: written proof [W], UNREVIEWED.
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
[r3] No bound o_F <= p is imposed.  At length 4p - 2, o_F(w0) = 2p - R + 2 kappa (eq. (0.1) of proof-K0star-r2.md); under the
hypotheses this gives o_F <= 2p + 4 - 2 kappa, and o_F > p is allowed.  Compare proof-REFL-fewodd-r5.md, which needs o_F <= p but
allows rho_(+-x) mixed.

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

(1) Examples of the range (R >= p always holds for avoiders, by P0, and R <= 2p - 1 after the trivial cut):
* p = 31, kappa = 7.  4 kappa - 4 = 24; p + kappa - 2 = 36; 5R >= 4p + 6 kappa - 10 = 156 means R >= 32.  So the conditions
  hold exactly for R in [32, 61]; only R = 31 is left.  For R = 32, o_F(w0) = 2p - R + 2 kappa = 44 > p [r3].
* p = 7.
  - kappa = 2 needs R >= 6, i.e. every R >= 7.
  - kappa = 3 needs R >= 8 (4 kappa - 4 = 8; the alternatives give R >= 8 and R >= 36/5).
  - kappa >= 4 violates 2 kappa <= p - 1.
(2) The same composition with the original B0S-CJ (R >= 4 kappa + 1) is contained in this one.
(3) Mixed rotation letters (B >= 1 after normalisation) are not covered.  There P3 and P4 change R, kappa and B, and no B >= 1
analogue of B0S-CJ for k >= p + 1 exists yet.

## Fix map r1 -> r2

Remark (1) only.  r1 said both "R >= 36" and "R >= 32" for p = 31, kappa = 7; the correct range is R in
[32, 61].  The p = 7 examples were added.  Statement and proof unchanged.

## Fix map r2 -> r3

Wording only: the title and Sec. Statement say "no imposed bound o_F <= p", and record that at length 4p - 2
o_F = 2p - R + 2 kappa is determined by R and kappa.  Remark (1)'s p = 31 example is stated with the exact o_F.
Statement hypotheses and proof are unchanged.
