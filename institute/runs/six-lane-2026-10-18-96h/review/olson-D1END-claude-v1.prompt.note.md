# D1-END endpoint review: **ACCEPT-WITH-FIXES (0 FATAL / 0 MAJOR / 4 MINOR)**

The candidate is `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/proof-RPdelta1-boundary-v1.md`, lines 1–138 as supplied. The proof is correct at its stated scope. Every MINOR is about self-containment or wording; none changes the statement, a constant, a range or the case structure.

**Limits of this review**
- I checked only the supplied text, by reading it.
- I did not verify the SHA256 values; I had no tools.
- I did not read the bodies of Theorem P, (H0), CONNECT, LIGHT or `proof-RPdelta-two-neutral-v1.md`.
  - The first four are used only at their accepted literal statements.
  - The last is not needed (MINOR-1).
- The hand checks below are sanity checks, not premises.

## 1. Parameters, window, lift: ✓

- **Parameters.** All blocks are odd, so R = 2p−k+2κ.
  - This gives k = 2p−4 = 2M−2, with M = 2p−R = p−1, even and ≥ 6.
  - L = κ+1 = (p−1)/2 = p−⌊(p+1)/2⌋ = U, so a single layer m = M/2 is used.
  - 2m = p−1 < 2p−4 = k, so CONNECT is in scope, including complements and an edge toggling each index.
- **Fact 2.1 at m = M/2.** Here κ+1−m = 0 and p−m = (p+1)/2 = ⌊R/2⌋.
  - So γ_m(E) = ⌊E/2⌋ for every E ∈ [0, p+1], with equality of the bound at E = R.
  - The same holds for E⁻ = R−E.
  - No bound E ≤ p is used anywhere.
- **Lift.** e(x) = (p+1)x is a well-defined homomorphism Z_p → Z/2p, because p(p+1) ≡ 0 (mod 2p).
  - Since E(P) = B + D_P, we get ψ(P) = e(θ_P) − E(P).
  - u_P hits I(P) iff there is an even t ∈ [−(R−E), E] with t ≡ e(2u_P) (mod 2p).
  - That holds iff ψ(P) has a representative in [−R, 0].
  - The complementary classes are [1, 2p−R−1] = [1, M−1].
  - Hand check at p=7, E ∈ {0, 3, 4, 8}: the non-hit ψ-classes are {2,4}, {1,3,5}, {2,4}, {2,4}, all inside [1,5].
- **Increments.** Increments lie in [−(M−2), M−2], an interval of 2M−3 = 2p−5 < 2p integers, so each h_i is unique.
  - CONNECT gives N = c + h_P on F_m.
  - P^c is also in F_m, which gives (1).

## 2. Zeros and marked set: ✓ (e0 > z kept)

- **Parity and zeros.** h_i ≡ α_i ≡ d_i ≡ r_i (mod 2).
  - h_i = 0 ⇔ e(θ_i) ≡ d_i (mod 2p) ⇔ d_i is even and θ_i ≡ d_i (mod p).
  - Odd runs have odd h_i.
  - Empty runs have even h_i ≠ 0, so |h_i| ≥ 2.
- **P0.** P0 is equivalent to R + o_R ≥ 2p, so o ≥ M. Because o ≡ R (mod 2) and R = M+2, there are exactly three run profiles:

  | Profile | v | e0 |
  |---|---|---|
  | p+1 singleton runs | 0 | p−5 |
  | p−1 odd runs, one of length 3 | 0 | p−3 |
  | p−1 singletons plus one 2-run | 1 | p−4 |

  - Hence z ≤ v ≤ 1 and e0−z ≥ p−5 ≥ 2.
  - The bound e0−z ≥ p−5 is attained by the all-singleton profile.
  - S ≥ k+e0−z ≥ k+2.
- **ANY B.**
  - B enters only as an additive constant in ψ.
  - The normalisation A ≥ B is never used.
  - No purity, B<κ or reflection-value assumption appears.

## 3. SIGN-1Z-END: ✓ in all cases

- **Case A.** S > k > M−2.
- **Case B.**
  - Same-parity stretch indices differ by a nonzero even amount mod 2m0, while neighbours differ by ±1, so same-parity stretches are nonadjacent.
  - Each boundary touches at most one flipped stretch, and no boundary is created, so exactly 2m changes remain.
  - The signed sum is ≥ Sm/m0 ≥ (2m0−z)m/m0 > M−1.
  - An independent route: 2m0 ≤ k and S > k give Sm/m0 > 2m.
- **Case C**, including n = 2f and γ = 1.
  - n ≥ k−4m0, so n−2f ≥ M−2−2m0 ≥ 0.
  - Both endpoints of every old boundary are non-interior, so old boundaries are untouched.
  - Each independent interior flip adds two new, distinct boundaries, giving exactly 2m.
  - Set c_i = 1+1_Z−1_0. Using only 1−γ ≥ 0:

    `W_{J^c} + (1−γ)W_J ≥ (k+e0−z) − γ(n+e_J−z_J) = k−2f+e0−z−γe_J+γz_J ≥ M−2 + (2m0−z) + (1−γ)e0 ≥ M−1`

  - γ = 1 forces m0 = m−1, f = 1 and n = 2. This is attainable, for example p=7 with stretch lengths 3,3,2,2.
    - In that case the bound is 2M−4−z ≥ M+1, so the boundary case has wide slack.
  - LIGHT at n = 2f is inside its accepted statement n ≥ 2f. It is also elementary there: the two alternating f-sets of the concatenated 2f-cycle split the weight.
  - Case C does not use e0.
- **Case D.**
  - n = k ≥ 2f = M.
  - Flips that are independent on the cycle give exactly 2m changes.
  - The signed sum is ≥ S(M−2)/k ≥ (k+2)(M−2)/k > M−2.
  - This is the only case that uses e0 > z.
- **Conclusion.** The resulting positive set has m intervals and is proper, so it lies in F_m and contradicts (1).

## 4. p = 7: ✓

Parameters: M=6, k=10, m=3, κ=2.
- The window is floor-type for all E ≤ 8.
- The non-hit classes are [1,5].
- Increments lie in [−4,4], which is 9 < 14 values.
- (e0, z) ∈ {(2,0), (4,0), (3, ≤1)}.

By case:
- **Case B:** m0 ∈ {4,5}.
- **Case C:** m0 ∈ {1,2}. n = 2f is possible at m0=2, where the bound is ≥ 7 > 4.
- **Case D:** the signed sum is ≥ 12·4/10 > 4.

## 5. Ledger: ✓ (numerical set differences only)

The universe is [2, p−1]_Z.

- **δ1, p ≥ 11:**
  - RP-2NE gives [2,(p−5)/2], which contains SEG-num.
  - K2P+ gives [(p+3)/2, p−4].
  - The new point (p−3)/2 lies in neither band.
  - What remains is exactly {(p−1)/2, (p+1)/2} ∪ {p−3, p−2, p−1}.
    - p=11: {5,6} ∪ {8,9,10}.
    - p=13: {6,7} ∪ {10,11,12}.
- **δ1, p=7:** every accepted δ1 band is empty, so the remainder is {3,4,5,6}.
- **δ1, p=5:** untouched by this packet.
- **δ2:** unchanged. Formula (4) is exact, including p=11, where the K2P+ band [7,6] is empty and (4) reads {2} ∪ [4,10].
- **Premises:** there is no SEG-k, TRANSFER, region-B, B′, STAB or RPδ premise. V2NE contributes only binding 1 (the definition of e) and binding 4 (e0 > z is not weakened).

## MINOR fixes

1. **Make Sec. 2 self-contained (L22–23, L53–54, L61).**
   - Replace "Import … fixed-window calculation and zero-increment criterion" and "even-integer test from V2NE" with "re-derived here; no step of proof-RPdelta-two-neutral-v1.md is used".
   - Add the one-liners from §1–2 above:
     - e is well-defined and additive;
     - E(P) = B + D_P;
     - the CRT zero criterion;
     - h_i ≡ r_i (mod 2);
     - the converse of the even-integer test: t ≡ e(2u_P) implies t is even and t/2 ≡ u_P.
   - Open Sec. 2 with "Assume w avoids", so P0's avoider hypothesis is visibly discharged.
   - Rename the shifted integer `s` in L54; it collides with the signs s_i.
2. **Case B (L79–82).** "since m0 ≥ m+1 ≥ 4" is not the actual reason.
   - State the parity argument, as worded in V2NE binding 5.
   - State that no boundary is created.
3. **Case C (L89–92).** The "(VL binding5)" citation is phrased for RP-LIFT's SIGN case 3.
   - Replace it with its one-line generic proof: a J-neighbour of i shares i's initial sign, so it lies in i's stretch; m0 ≥ 1, so every stretch is a proper interval.
   - State that old boundaries are untouched.
   - Optionally record that γ=1 implies m0=m−1, f=1, n=2.
4. **Sec. 4 (L116–126).**
   - State the universe [2, p−1]_Z explicitly (κ ≤ p−1 from H ≥ 0; κ ≥ 2 by the I.14 residual convention), so (3) is literally a set difference.
   - Note that δ2's K2P+ band is empty at p=11.

## Scope if the parent concurs

**What is accepted:** D1-END exactly as stated at L9–14.
- **Hypotheses:**
  - p ≥ 7 prime.
  - Length 4p−2 over D_2p.
  - Exactly R = p+1 rotation letters, all in one pair {ρ_x, ρ_−x} with x ≠ 0.
  - Every maximal cyclic constant reflection block has odd length.
  - κ = (p−3)/2, so k = 2p−4.
  - Any B, with no purity, B<κ, inherited or reflection-value hypothesis.
- **Conclusion:** an identity subword of exactly 2p letters in increasing original index order.

**Imports it relies on:**
- W and Fact 2.1 (V5, setting S).
- P0 (K0star-r2 L73–75, accepted at 879aeee7, per V2NE binding 3).
- CONNECT and LIGHT (VL).
- The definition of e(·) from V2NE binding 1.

**Not covered:**
- p=5, κ=1.
- Any other κ at δ=1.
- All of δ=2, including (δ,κ)=(2,2).
- R ≥ p+2.
- Words with even blocks.

REFL(p), REFL-HI, RES-HI, INV\* and ordered Olson remain open. No novelty, priority or major-result designation follows from this review.
