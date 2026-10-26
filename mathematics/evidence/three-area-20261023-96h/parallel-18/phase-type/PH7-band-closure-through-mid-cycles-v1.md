# The band's natural closure: arbitrary cycles through the middle state cannot reach 8/9 (u ≥ 1)

The actual `/bin/date` returned before this manuscript was **Sun Oct 25 22:52:32 PDT 2026**. Owner MathResearch96h-2, math-1.

Status: AUTHOR-WRITTEN CANDIDATE. This is an exact RESTRICTED-FAMILY result. It is not an unrestricted 8/9 decision; the minimum stays in {7,8}.

No interpreter, eval, calculator, CAS, solver or replay was used. All identities below are hand-expanded polynomials.

Private approximate decimal comparisons that guided which inequality to try are disclosed in checkpoint059. They carry ZERO credit. The proof below does not use them.

## 1. Family

Use the y-coordinates of the band packet `PH7-rational-uniform-band-seven-ninths-v1.md` (SHA256 `ef6df980b2fbb5545a42ed7f3c72f17cea6f26f7148065670c104838f9a0c0f7`):

- d=1, D_z(y)=y((y+1)²+z)², target transfer K/D_z.

Take a chain 1→2→…→7 with positive forward rates. Back edges k→j (j<k) are allowed ONLY when the cycle segment [j..k] contains the middle state 4. There are 15 such segments, (j,k) with j≤4≤k, j<k.

The holdings, i.e. the diagonal of −G, are (u,u,u,w,1,1,1). Initial weights sit on {1,2,3} and the exit is state 7.

The actual band is the member that uses only the segments [4..7], [1..5], [1..6] and [1..7], with u=29/20.

## 2. Linearization lemma (exact)

Every allowed cycle contains state 4, so no two of them are disjoint. The determinant expansion therefore has no products of cycles:

    det(yI−G) = prod_i(y+lambda_i) − sum_c w_c prod_(i∉c)(y+lambda_i),

where w_c ≥ 0 is the cycle weight: forward rates along the segment times the back-edge rate.

Any w_c ≥ 0 is realizable. The only simple paths from i∈{1,2,3} to 7 go forward, and the principal blocks on {1..i−1} contain no cycle. Hence the numerator is

    beta_3'(y+u)² + beta_2'(y+u) + beta_1',

which is proportional to Q (Q = y² + py + q) iff p ≥ 2u and Q(−u) ≥ 0.

For these holdings, prod_(i∉[j..k])(y+lambda_i) = (y+u)^alpha (y+1)^beta with alpha=j−1 and beta=7−k. So the spectrum condition det = D_z Q is EXACTLY the cone membership

    R := (y+u)³(y+w)(y+1)³ − D_z(y)Q(y) ∈ cone{(y+u)^alpha (y+1)^beta : 0≤alpha,beta≤3, (alpha,beta)≠(3,3)}.

The trace condition is w = p + 1 − 3u, which removes the y⁶ term.

## 3. Exact cone characterization for u ≥ 1

Put x = y+1, delta = u−1 ≥ 0, P2 = p−2, Q0 = 1−p+q. Expanding by hand:

    R5 = 3delta(P2−1) − 6delta² − Q0 + P2 − 2z,
    R4 = 3delta²(P2−1) − 8delta³ + Q0 − 2zP2 + 2z,
    R3 = delta³(P2−1) − 3delta⁴ − 2zQ0 + 2zP2 − z²,
    R2 = 2zQ0 − z²P2 + z²,
    R1 = z²(P2−Q0),
    R0 = z²Q0.

Define

    L5 = R5,
    L4 = R4 − 2delta R5,
    L3 = R3 − delta R4 + delta² R5.

**Lemma.** R lies in the cone iff L5, L4, L3, R2, R1, R0 ≥ 0.

*Proof.* Necessity: each of the six functionals is nonnegative on all 15 generators (x+delta)^alpha x^beta. This was checked term by term; for example L4((x+delta)²x³)=0 and L3((x+delta)³x²)=delta².

Sufficiency: the explicit representation

    R = L5(x+delta)²x³ + L4(x+delta)x³ + L3x³ + R2x² + R1x + R0

reproduces every coefficient. ∎

**Validation against the supported band.** The band has R5 = R4 = 0. Solving these gives

    P2 = delta(3+9delta+8delta²)/(1+3delta+3delta²−2z).

At delta=9/20 the numerator is 7803/2000 and the denominator is 1183/400 − 2z = L. The band packet's p = N/L gives p − 2 = (19633/2000 − 4z − 2L)/L = (7803/2000)/L. The two agree EXACTLY. Its φ equals L3 there.

## 4. Theorem

Let z = 8/9 and u ≥ 1. No member of this family has the PH7 spectrum. In particular, NO choice of the 15 through-mid cycle weights, w > 0, p and q realizes the target.

*Proof.*

**(a) delta = 0.** L5 and L4 give Q0 ≤ P2 − 2z and Q0 ≥ 2z(P2 − 1). Together, P2(1−2z) ≥ 0. Since z > 1/2, P2 ≤ 0, and then Q0 ≤ −2z < 0, contradicting R0 ≥ 0. (For general z, this sub-family realizes the spectrum only when z ≤ 1/2.)

**(b) delta > 0.** Note w = P2 − 3delta > 0, so P2 > 0. Eliminating Q0 between the bounds L5 ≥ 0 and L4 ≥ 0 gives EXACTLY

    P2(3delta² + 3delta + 1 − 2z) ≥ delta(3 + 9delta + 8delta²).        (I)

Eliminating Q0 between L4 ≥ 0 and L3 ≥ 0 gives EXACTLY

    P2·Adiff ≤ Bdiff,                                                   (II)

where

    Adiff = delta⁴ + 2delta³ + (4z+1)delta² + 2z(2z−1) > 0,
    Bdiff = 2delta⁵ + 4delta⁴ + (8z+2)delta³ + 6z delta² + 6z² delta + 3z².

At z = 8/9, 3delta² + 3delta + 1 − 2z = 3delta² + 3delta − 7/9.

- If this is ≤ 0, then (I) fails, since its left side is ≤ 0 < its right side.
- Otherwise (I) and (II) together need Delta ≤ 0, where Delta := delta(3+9delta+8delta²)·Adiff − Bdiff·(3delta²+3delta−7/9). Expanding by hand:

      Delta = 2delta⁷ + 7delta⁶ + (59/3)delta⁵ + (61/9)delta⁴ + (43/27)delta³
              − (128/27)delta² + (176/243)delta + 448/243.

  The block (61/9)delta⁴ − (128/27)delta² + 448/243 is a quadratic in delta² with leading coefficient 61/9 > 0 and negative discriminant. Indeed (128/27)² = 49152/2187 < 4·(61/9)·(448/243) = 109312/2187. So that block is positive. Every remaining term is positive for delta > 0. Hence Delta > 0, a contradiction. ∎

## 5. Interpretation and limits

For each u ≥ 1, the condition "L5, L4, L3 ≥ 0 are compatible" is exactly Delta(u−1; z) ≤ 0. At the band's point this is the band's φ ≥ 0. So adding ANY of the 11 further through-mid cycles (2-cycles, 3-cycles and the others) cannot extend the band's z-range at a fixed u ≥ 1; the band is extremal inside its natural closure. The lower coefficients and the numerator still have to be checked separately; they only add constraints.

NOT covered:

- u < 1. That needs the expansion around y = −u.
- Unequal holdings inside the blocks, or downstream holding ≠ 1.
- Cycles that avoid state 4, which create disjoint-cycle products.
- Non-chain initial blocks, Case-I sub-types other than the chain order, and Case II.

So the unrestricted 8/9 question remains open, minimum {7,8}. No formal, kernel, cross-vendor or novelty acceptance is claimed. HOLD, root, cutoff and deadline are unchanged.
