# Second-family (Claude) written review: Theorem K2 v1

**Counts: 0 FATAL / 0 MAJOR / 1 MINOR.** The MINOR is presentation only. I found no mathematical flaw.

**Errata applied:**
- Author erratum 1: E1 replaces the K2 LF124 conclusion; E2 changes Sec. 0 wording.
- Parent erratum v1: corrects the remark at K2 LF125–127.

**Basis and status:**
- I used only the pasted text: no tools, files, computation or enumeration.
- I did not re-check hash or range metadata.
- I did not treat the first-family review as authority; I re-derived the parent-erratum remark myself.
- This is a review input, not a parent verdict.

## Claim-wise verdicts

**1. (SR) windows, K2 LF23–24: CORRECT.** Re-derived from GRX LF18–19 via PL LF47–50:
- All l_i are odd, so δ = N − 2m and C ∈ [2m, 2m+2H].
- With 2p − 2H = 6, this gives n ∈ [max(0, 6−2m), min(p+3, 2p−2m)].
- The windows follow:
  - ∅: [6, p+3].
  - m=1: [4, p+3].
  - m=2: [2, p+3], using p ≥ 7.
  - 3 ≤ m ≤ (p−3)/2: [0, p+3].
- The target is T(P) because Στ = 0.
- The m-convention is the one in parent erratum 087ab3ae, LF7.

**2. Integer frame and Lemma IF at κ=2, K2 LF25–34: CORRECT.**
- **(S′) instance.** Take (k′, κ′) = (p−1, 1). Then R = p+3 and L = p+3−2t ≥ p+1 = 2p−k′.
- **(ZP).** (SR) at P0 (m=1) excludes zero-sums of every length 4 through p+3 = |Y|.
- **t=0:**
  - There are p+3 odd labels, so W is even and W ≤ 2p−2.
  - m1 ≥ (p+11)/2.
  - b ≤ W − (L−1) ≤ p−4.
- **t=1:**
  - n− ≥ 1 (FB LF17) and Σs_j = n+ ≥ n− rule out (n+, n−) = (0, 2). Hence n+ = n− = s₁ = 1.
  - W ≤ 2p−2, and a_i ≤ p−2 by FB-E.
  - m1 ≥ (p+5)/2; adding z+ gives #(b=1) ≥ (p+7)/2.
- **Light side.** LT at κ=2 uses 3+3 = 6 ∈ [6, p+3]. A swap negates the c-labels and leaves b unchanged.
- **Positions of z±.** If z+ ∈ P0 it is counted in o(P0). If z− ∈ C0 it is the only negative letter outside P0. Both cases are covered by u+ ≥ #(b=1) − o(P0).

**3. Imported D/SS/U/A/C at κ=2, K2 LF35–42: instantiations CORRECT.**
- Lemma D's max-element step needs W ≤ 2L + r − 2. This holds because W ≤ 2p−2 < 2L.
- Lemma A's positivity comes from Lemma N.
- Lemma C needs p−2 < B* ≤ 2p−2.

**4. CJ''', K2 LF43–44 and LF110: CORRECT at literal scope (cj-cjx LF8, LF12–13).**
- The setting: length 4p−2, all R = p+3 rotations equal to ρ_γ with γ ≠ 0, and F = 3p−5.
- Each S_i is a maximal block, separated by a nonempty run or by the empty-run rule (NF LF38). So there are k = p+1 odd blocks.
- The parameters: H = p−3, κ = 2, Δ = −2, R ≥ 4κ−4, and 2κ = 4 ≤ p−1.

**5. Lemma N, K2 LF46–61: CORRECT.**
- u+ ≥ (p+3)/2.
- **(a) c = −B with B ≥ 5.** Such a letter must be an a-label in P0.
  - For t=1, the remaining excess is at most p−2−B (even), so #(b=1) ≥ (p+4+B)/2.
  - For t=0, the remaining excess is at most p−4−B, so #(b=1) ≥ (p+8+B)/2.
  - In both cases u+ ≥ (p+B)/2 ≥ B, giving a forbidden zero-sum of size B+1 ∈ [6, p−1].
- **(b)** The partial sums x_j increase by 2 or 4 each step. So the first x_j ≥ 6 is 6 or 8, and w_j ≤ 7 ≤ (p+3)/2 ≤ u+. This is tight at p = 11.
- **Lift inequality.** 2Π0 + 3 + ν0 = 2B* + 3 − ν0 ≥ 2p+6.

**6. Lemma F, K2 LF63–89: CORRECT.**
- **(F1)** Every |J| ≤ R lies in [0, p+3], and the parity condition is automatic by SS. Since F ≠ ∅, B* ≤ 2p−2.
- **(F2) θ_i is well defined.**
  - |d| ≤ 2p−2−B* ≤ p−5.
  - Two values d, d′ agree mod p and mod 2, and |d − d′| ≤ 2p−10, so d = d′.
  - The cyclic distance from i to i+6 is min(6, N−6) ≥ 6. So m(Q∪{i}) = 4 ≤ M, with M = 4 at p = 11.
  - θ_i ∈ (−p, p) is defined through a full pair, as erratum 087ab3ae LF6 requires.
- **(F3) The family is connected.**
  - (a) Removing an endpoint of a non-singleton interval keeps m unchanged.
  - (b) Shrinking an independent set stays within 3 ≤ m ≤ M.
  - (c) Advancing or retreating a, b or c gives all six donor→receiver transfers, provided the donor gap is ≥ 2. The intermediate {a, a+1, b, c} has m = 3.
  - Each transfer lowers Σ|g − target| by 2.
  - The target is (3, 3, N−9), where N−9 ≥ 3.
  - The cycle (3,3,N−9) → (3,4,N−10) → (4,3,N−10) → (3,3,N−9) shifts the triple by one. At p = 11 the intermediate steps are (3,4,2) and (4,3,2).
- **(F4)** {0,2,4} and {1,6,8} are independent. Their union has intervals {0,1,2}, {4}, {6}, {8}, and 8 is not adjacent to 0, so m = 4. Lemma A with Lemma N gives f0 = 0.
- **(F5)** m(Q0) = m(Q0ᶜ) = 3. Lemma C then gives Σθ = B* − 2ν0 − 2p.

**7. Lemma RIG, K2 LF91–102: CORRECT.**
- From 3θ₍₃₎ ≤ −1 − ν0 we get θ₍₃₎ ≤ −1. Summing with (F5) gives B* ≤ p+3.
- Equality forces:
  - every |c| = 1;
  - θ₍ⱼ₎ = −1 for j ≥ 3 (this uses (p+1)/2 ≥ 4);
  - θ₍₁₎ + θ₍₂₎ = −ν0;
  - ν0 ∈ {0, 1, 2}.
- There is no circularity: the dependency order is N → F → RIG → §5.

**8. §5 with E1, K2 LF104–124: CORRECT.**
- **ν0 = 2:**
  - Every θ = −1, so every r_i is odd. Since Σ(r_i − 1) = 2, there is one 3-run and p singletons.
  - At least p−2 singletons carry +1.
  - For such a singleton, X^({i}) contains three −1's and p letters +1. Taking n = 4 gives sum −2 ≡ τ_i.
- **ν0 = 1:**
  - (θ₍₁₎, θ₍₂₎) = (0, −1).
  - A run with θ = 0 has r_e even. It is nonempty: otherwise θ_e ≡ τ_e = y_e − y_{e−1} ≢ 0.
  - One such run avoids the single −1, so r_e ≤ p+1.
  - Taking n = r_e + 2 ∈ [4, p+3] gives sum −r_e ≡ τ_e.
- **ν0 = 0:** handled by item 4.
- **Antecedent fully respected:**
  - Block lengths enter only through oddness.
  - The empty-run rule is used at LF117–118 and in item 4.
  - The rotation pair is derived, not assumed.
- **Theorem P genuinely unused.** The run shapes come from θ-parity and Σr = R; no step uses PL §3. Lemma CR is also unused.

**9. Remark, K2 LF125–129 as corrected by parent erratum LF5: CORRECT** (re-derived), and not used by the proof.

**10. Scope and package, K2 LF131–149 and package LF1–43: accurate.** Claims are confined to κ̂ = 2 and p ≥ 11.

## Finding

**MINOR-1 (presentation): overloaded symbols.**
- **F** means the reflection count (K2 LF22), the family (LF65; "inside F" at LF68; "on F" at LF84), and the lemma name.
- **u** means the NF word (LF22) and u+ (LF50); PL also uses u inside Lemmas D and U.
- **H** means the extra-pair count (LF13) and H(P) (LF36).

**Consequence:** no mathematical effect, but LF68 is easy to misread.

**Repair:** rename the family (for example 𝓕) and u+ in any later version or wording erratum. No statement changes.

## Notes (not counted)

- **S1(a) is not load-bearing at κ=2.** Because |Y| = p+3 < 2p, (ZP) at κ′ = 1 already bounds every zero-sum length by 2.
- **The unstrengthened B0S-CJ suffices.** R = p+3 ≥ 4κ+1 = 9.
- **Where p ≥ 11 is actually used:** LF59, LF65, LF71 and LF86 (M ≥ 4, N ≥ 12). The "p ≥ 9" at LF137 concerns only the family being nonempty.

## Status and boundary

**Correctness.** Theorem K2 and Lemmas N, F and RIG hold at κ̂ = 2, for every prime p ≥ 11, under the full antecedent. This is relative to the accepted imports at their literal scopes:
- PL SR/IF/D/SS/LT/U/A/C, per K1 verdict 93ea601c… and erratum 087ab3ae…;
- through IF: NF, GRX (if direction), SC0, and ZSTRUCT/FB/FB-E in (S′);
- CJ''' for the ν0 = 0 case only.

No other unresolved load-bearing dependency remains.

**Other dimensions:**
- **Completeness:** the full antecedent is covered.
- **Process:** not assessed beyond this review's own compliance.
- **Priority and computation:** none is claimed by the proof, and none was used here.

**Not approved:**
- other lower-half cells, κ̂ = 0, or p < 11;
- (H-ALT) or the lift inequality for κ ≥ 3;
- rigidity, INV*, o_F assembly, or full ordered Olson;
- the research target or runtime.

No novelty, first, Lean or human claim is made.
