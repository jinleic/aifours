# SCW hostile written review: Theorem SCW (p = 4κ−3, κ ≥ 4, k = p+1, κ̂ = κ)

**Counts: FATAL 0 · MAJOR 0 · MINOR 1.** The one MINOR is about input provenance and does not bear on the proof. All checks were done by hand from the pasted text only: no tools, no computation, no enumeration.

**Correctness.** I re-derived every load-bearing step from the literal supplied interfaces, and none failed. Theorem SCW (LF13–17, LF360–362) is proved for every κ ≥ 4 with p = 4κ−3 prime, under the full existential NF/word antecedent. This holds relative to the accepted inputs: NF, the GRX if-direction, SC0, and ZSTRUCT/FB in (S′). The contradiction is reached in an arbitrary fixed frame (LF99–100), so nothing remains conditional on the frame, unlike K3-11.

## Claim-wise verdicts

| Claim (proof LF) | Verdict | Decisive checks |
|---|---|---|
| (SR) 40–41 | correct | Re-derived from GRX LF18–19 and NF LF37–43, instantiated as in PL LF48–50: Φ = 2m (LOWER erratum LF7), δ = N−Φ, C_max = 2m+2H, n = 2p−C, and 2p−2H = 2κ+2. It does not depend on where the extra pairs sit. |
| L1 43–46 | correct | 2p−2κ = R−2; 2p−2κ−2 = R−4; 2p−2 ≥ R. |
| L2 48–72 | correct | (b) is direct; S1(a) is not used. (c) z ≠ 0, and Y′z is minimal whether or not z lies in the subsequence; length L+1 ≥ p+2 = ⌊2p/2⌋+2; so ord g = 2p, W = 2p−x(z) ≤ 2p−1, and g₁ = 1. (d) Every (S′) clause of FB LF11–15 holds at (p−1, κ−1): \|Y\| = 2p+2κ′−k′ = R, (S1) at κ′ from (b), t ≤ κ′, L ≥ 2p−k′ = p+1, and g is an odd index-<1 generator. ZSTRUCT comes in via balfull overlay LF33, and FB holds for every Z and g (FB verdict LF7). |
| L3 74–83 | correct | κ ≥ 4 is used at LF79 (m1 ≥ 10) and LF82 (m1−b ≥ κ ≥ 4); both are tight at κ = 4. |
| Normalisation / light side 84–94 | correct | The exchange keeps the labels (−Y, −g, same coefficients). The light side is chosen before setting γ = 1. |
| L4 102–113 | correct | Needs only max\|c\| ≤ u1+1. Neither PL Lemma D nor the Setting fact is used. |
| L5 117–123 | correct | The c < 0 types are exhaustive. The margin is ≥ 2κ−1+E/2; at κ = 4 that is exactly 7, which is exactly what L9 needs. |
| L6–L7 131–170 | correct | Focus (1). |
| L8 172–197 | correct | Focus (2). |
| L9–L10 198–206 | correct | L9: Δ ≡ 0 (mod 2p) and 1 ≤ Δ ≤ 4p+6−B* < 4p, so Δ = 2p. L10: the interval has length 4p+8−2B* < 2p ⇔ B* > p+4, and contains Π0−ν0+2p ⇔ B* ≤ 2p+4. |
| L11 210–252 | correct | Focus (3). |
| Sec. 5 256–289 | correct | Focus (4). |
| Sec. 6 297–326 | correct | Every instantiation recomputed; focus (5). |

## Focus items

**1. Truncated realisation (L7).**
- (a) A minimal J contains no zero-signed subset, while the full letter set contains Z0, so \|J\| ≤ R−2. The value v = 0 is realised by Z0, since \|Z0\| ≤ 3κ−2 ≤ R−2.
- (b) Exact as stated.
- (c) \|J\| ≥ R−2 forces both signs into J. With no ±1 pair, J contains at least u1−2 unit letters of the other sign, and b ≤ u1−4, so a zero-signed subset exists.
- (d) The u1−4 count gives J ⊆ Pos(P). The replacement sets for q = 2, 1, 0 have size ≤ R−4 (using u1−1 ≥ x and u1 ≥ x₂+4), and the removed unit letters are distinct from l₁.
- (e) Follows by P^c duality.
- The case split is complete: q ≤ 2 and q′ ≤ 2 cannot both hold, because q+q′ = R ≥ 20.
- Each listed exception is genuinely unrealisable, so widening the window is necessary. Only the upper-bound direction is used.

**2. Common window I* = [Π0−2, 2p+2−ν0] (L8).**
- I recomputed every [a, b] in cases (A), (B) and (C), with parity (q or q′ = 1 makes Π(P) and ν(P) odd). In each case b−a ≥ B*−4.
- Each [b+2, a+2p−2] lies inside I*. I* is exactly the hull of the q = 0 and q′ = 0 sub-windows.
- B* ≤ 2p.
- Uniqueness holds: \|I*\| = 2p+4−B* ≤ 2κ+2 < 2p, and p is odd, so the residues mod p and mod 2 fix one integer.
- The m = κ sub-windows used in Sec. 5 are correct.

**3. θ, connectivity and the κ = 4 pair (L11).**
- (F1) Q_i and Q_i∪{i} are in F, with 2κ−3 and 2κ−4 ≥ 1 separators. Both \|d\| and \|θ_i\| are ≤ 2κ+2, so two candidates differ by at most 4κ+4 < 2p and must coincide. For an empty run, θ_e ≡ τ_e ≢ 0 (mod p) and θ_e is even.
- (F2) Every toggle stays in F. The gaps sum to 3κ−3, the normal form is (1,…,1, 2κ−3), and the shift order is valid.
- (F4) 3κ−2 runs in κ gaps force some gap ≥ 3.
- (F5) P1 and P2 are independent and disjoint, and P1∪P2 has κ+1 intervals. There are κ−3 wrap separators; at κ = 4 this is run 13 alone, which still suffices. So f0 = 2f0, giving f0 = 0.
- (F6) Q0 and Q0^c are both in F.

**4. Top-κ sorting (Sec. 5).**
- The CLAIM's cases are exhaustive: two-signed; single-signed with ν0 ≥ 1; single-signed with ν0 = 0.
- When ν0 = 0: if J_S is all-positive, every run of J_S is empty, which forces θ_(κ) ≤ −2. If it is all-negative, every run outside J_S is empty.
- The both-exceptional case splits exhaustively into (α), (β), (γ):
  - (α) forces ν0 = 0, which is excluded.
  - (β) gives Π0 = 0, so L5 yields B*−2p ≥ 7, contradicting B* ≤ 2p.
  - (γ) gives J_S1 ⊆ J_S2^c, so every run outside J_ev∪J_od is empty. Applying CLAIM (ii) twice gives B* ≤ 4κ−2 < R.
- The resulting bounds are R−2, R−1 and 4κ−2, all < R ≤ B*, which is the contradiction.

**5. The cells (4,13) and (5,17).**
- **(4,13)**, with N = 14, R = 20, 2p = 26:
  - Windows: W₄ = [2,18] and W₅ = [0,16].
  - Labels: t ≤ 3, E ≤ 8, a_i ≤ 9, s_j ≤ 5, m1 ≥ 10.
  - Margin: exactly 7, so Δ ≥ 1 with no slack.
  - Window and θ bounds: \|I*\| ≤ 10, \|θ\| ≤ 10 < 13, candidates differ by ≤ 20 < 26, complement interval ≤ 20 < 26.
  - (F5) separators: 2, 5, 8, 11, 13.
  - Final bounds: 18 / 19 / 14, all < 20.
- **(5,17)**, with N = 18, R = 26, 2p = 34:
  - Windows: W₅ = [2,24] and W₆ = [0,22].
  - Labels: t ≤ 4, E ≤ 11, a_i ≤ 12, s_j ≤ 7, m1 ≥ 13.
  - Margin: 9.
  - Window and θ bounds: \|I*\| ≤ 12, \|θ\| ≤ 12 < 17, candidates differ by ≤ 24 < 34.
  - (F5) wrap separators: 16 and 17.
  - Final bounds: 24 / 25 / 18, all < 26.

## Hidden-premise audit: none found

- **Full window:** not assumed. L7 works with the truncated windows and records exactly which values are lost.
- **Nonempty runs:** not assumed. Empty runs enter only through θ_e being a nonzero even integer, used in Sec. 5.
- **o_F, rotation pairs, rigidity:** not used. The sorting argument replaces rigidity.
- **Unreviewed results:** FCW, P11R and the USK/K3 lemmas are not used.
- **PL items:** S1(a), FB-E, the Setting fact and PL Lemmas D/U/A/C/THETA are not used. L2(b) is direct, L3 supplies its own bounds, and L4(a) supplies its own density.
- **Governing errata:** all complied with.
  - LOWER erratum: m(P) as half the sign transitions; θ only through explicit pairs.
  - USK erratum v1: step-two Q_i.
  - USK erratum v2: SS routed through the proof's own density lemma; light side chosen, then normalised.
  - K3 erratum: frame quantifier; direct zero-sum bound.

## Finding

**MINOR-1: input provenance, not load-bearing.** Proof LF26 and LF375, and scope LF31–36.
- **Step:** these lines attribute (SR) and the other PL Sec. 2/4–6 items to "PL Secs. 2–7 accepted relative to their inputs" via the K1 verdict.
- **Gap:** the literal K1 verdict (LF5) accepts Theorem K1, Theorem R as a range only, "Theorem S structure", and Lemma CR as a conditional. It does not state that the general-κ (SR) of PL LF47 is accepted.
- **Consequence:** none for the mathematics.
  - Every other PL item used is re-proved in the text: IF(a) is L2(a), the normalisation is at LF84–87, SS is L4(c), and the light-side argument is at LF88–94.
  - (SR) follows directly from the GRX if-direction and NF, as shown in the table.
- **Minimal repair:** cite (SR) as "GRX if-direction + NF, instantiated as in PL LF48–50, with m(P) per LOWER erratum LF7". No statement changes.

**Editorial notes (not counted, no mathematical effect):**
- Several symbols are overloaded: H (pair count) vs H(P); F (reflection count) vs F (family); W (label sum) vs W_m; σ(Y′) vs σ(P).
- "Exact m = κ sub-windows" at LF21 means containments, not sharp windows.
- (M3) at LF344–345 says the argument "does not reach the top R−2e". The direction is reversed: the bound R−2 lies above the window top R−2e. This is in a non-claim remark.
- Remarks (M1), (M2), (R1), (R2) and (R4) are accurate.

## Process, completeness, priority, computation

- **Process (parent qualification applied):** proof LF4–6 says "frozen … before derivation"; it must be read as "before *written* derivation".
  - Scope LF74–81 discloses unwritten preliminary route checks before the freeze. These include the κ = 4 additive-pair obstruction (now R1/F5) and the minority-sign loss (now L7(d)/(e)).
  - This is a preregistration-order deviation. **Strict pre-derivation preregistration is not certified.**
  - The target text is unchanged across transition LF6, scope LF16–25 and proof LF13–17.
  - Python string drafting, exactly-once checks and hashing were text/metadata operations, not scientific assertions or enumeration.
- **Completeness:** the full frozen target is covered, including the whole existential antecedent. The optional δ item is a declared non-claim (LF343–348), which scope LF24–25 permits.
- **Priority:** none claimed, none assessed.
- **Computation:** none is a premise of the proof, and none was used in this review.

**Not approved:** the ordered-Olson research target, any runtime or HOLD change, and any novelty, "first", human-review or Lean claim. The acceptance above covers Theorem SCW only, relative to its accepted inputs.
