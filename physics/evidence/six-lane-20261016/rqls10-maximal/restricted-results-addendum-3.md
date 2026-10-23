# Addendum 3: flat 5th-root half-splits (a clean open family, with one closed sub-case)

Written about 15:00 PDT, 2026-10-18. Lane-internal, **unreviewed**, restricted only.

## Family

- Split C^10 = W_A (+) W_B with dim 5 each and a global qubit-type label. Every cell vector lies in W_A or W_B, and
  every line meets each half in 5 cells.
- Each cell vector is flat with 5th-root entries: (1/sqrt5) (zeta^{F_p(t)})_{t in Z_5} in the half's basis, with
  F_p: Z_5 -> Z_5.
- Rays correspond to F mod constants: V = Z_5^{Z_5}/<1>, which is AG(4,5) with 625 points.

Facts:
- Two such vectors are orthogonal iff F - G takes all 5 values (a 5-term sum of 5th roots vanishes iff the exponents
  are distinct).
- Every flat ONB of C^5 is equivalent to the Fourier matrix [IMPORT: Haagerup, order-5 complex Hadamard
  classification]. So a 5th-root flat ONB is an affine line {F + lambda pi : lambda in Z_5} with pi a permutation.
- There are 6 *permutation directions*: the permutation classes of Z_5 modulo pi ~ a pi + b. Each point lies on
  exactly 6 ONB-lines, and there are 750 such lines.

The problem in this family is purely combinatorial: find
- a Latin square B;
- a 5/5 half pattern;
- injective maps F_A and F_B from half-cells to AG(4,5);

such that every half-line maps onto a permutation-direction line. A solution is automatically exact over Q(zeta_5).
- R7 does not cover this family. The 625 flat rays include non-MUB vectors, and each ray lies in 6 ONBs.
- R5 excludes only rectangular half patterns.

## Closed sub-case: uniform directions

**Claim.** Suppose all half-rows of half A map to lines of one direction d_R and all half-columns to one direction
d_C != d_R. Then half A is rectangular, and Mann parity (R5) excludes it.

*Proof.*
1. The image X (50 points) is a union of d_R-lines and also a union of d_C-lines.
2. For x in X, the d_C-line through x lies in X, and every d_R-line through its points lies in X. So
   x + span(d_R, d_C) is contained in X, and X consists of exactly two parallel planes.
3. Each A-cell (r,c) maps to the meeting point of the lines of row r and column c. So rows of one plane have their
   A-cells exactly in the columns of the same plane.
4. Hence P_A = (R0 x C0) u (R1 x C1). QED

## Open

- Mixed directions (half-lines of one parallel class mapped to lines of several of the 6 directions) are open.
- This is a natural candidate for a future *authorised* exact combinatorial search (SAT/CSP), with results checked by
  exact_rqls_checker_v1.py over Q(zeta_5). No such search was run in this lane.
