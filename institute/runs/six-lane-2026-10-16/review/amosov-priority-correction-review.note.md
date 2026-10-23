VERDICT: ACCEPT-WITH-FIXES

**Scope.** I checked the quoted statements and your arguments by hand. I did not inspect the source, later arXiv versions, the parent receipt, Alhejji–Knill or Song–Chen. Everything below assumes the quotations are accurate.

## Claim A: correct and decisive

**Hypotheses, item by item:**
- **T is CPTP.** (1/4)Σ_{W∈{I,X,Z,XZ}} Ad_{W⊗I} is the Pauli twirl on A, since XZ = −iY. It equals (I_A/2)⊗tr_A. ✓
- **T ≺ (1/2,1/2).** spec T(ρ) = (b₁/2, b₁/2, b₂/2, b₂/2), where (b₁,b₂) = spec ρ_B. So Ky Fan₁ ≤ 1/2 and Ky Fan₂ = b₁ ≤ 1. Since Σ_{j≤k}⟨e_j,σe_j⟩ ≤ Ky Fan_k(σ), Definition 1 holds for every orthonormal tuple and every unit f. This is analytic, not sampled. ✓
- **Dimensions.** m = n = 2 ≤ dim H = 4 = mn. ✓
- **Conclusion fails.** T∘T = T, and T(|00⟩⟨00|) = (I/2)⊗|0⟩⟨0| has spectrum (1/2,1/2,0,0). With e₁ = f = |00⟩, the k = 1 inequality would require 1/2 ≤ 1/4, so it fails by 1/4. The k = 2 and k = 3 inequalities also fail. ✓

This is decisive against Proposition 1 as quoted, provided ∘ means composition. The receipt is not needed. Two likely rebuttals both fail:

1. **"Proposition 1 is meant only inside the paper's class."**
   - T is the uniform mixture over the real Pauli group {±I,±X,±Z,±XZ} on A.
   - Take 𝒯 = {±I,±Z}. The coset distribution is (1/2,1/2), and (8) holds even literally.
   - This works unless an unquoted condition, such as irreducibility, excludes it.
2. **"Proposition 1 is meant only for channels on distinct tensor factors."** That version is also false.
   - Let W(X) = (tr X·I − Xᵀ)/2 on C³ (Werner–Holevo). Every pure output has spectrum (1/2,1/2,0), so W ≺ (1/2,1/2).
   - Φ ≺ P always implies Φ⊗id ≺ P. Reason: (Φ⊗id)(ψ) and Φᶜ(tr₂ψ) share nonzero spectrum, Ky Fan sums are convex, and Φᶜ and Φ have equal pure-input spectra.
   - So W⊗id and id⊗W are both ≺ (1/2,1/2) on C⁹, and 9 ≥ 4.
   - Their composition W⊗W maps Φ⁺ to (I/3 + Φ⁺)/4, which has eigenvalue 1/3 > 1/4.

Claim A refutes the lemma. It does not refute the specific instance of it used in Theorem 2.

## Claim B: right about the literal text, but understates the amended reading and needs a 𝒯 scope

**Is the same-coset reading forced?** Yes, given non-strict ≤ and unrestricted U, V.
- Excluding U = V would not help: take V = UT₀.
- Only "[U] ≠ [V]" or a strict "<" avoids it.
- Literal (8) is exactly "π is constant on each coset"; the cross-coset part then holds automatically. That redundancy is good evidence the author meant distinct cosets. So present the literal failure as a drafting defect, not a substantive obstacle.

**The depolarizing computation is right:** the identity coset has weights 1−p+p/d² and p/d², which are equal only at p = 1.

**Problems:**
1. **"Might change" understates.** Under the distinct-coset or strict reading, D_p with the diagonal 𝒯 does satisfy (8) for every 0 ≤ p ≤ 1:
   - Each non-identity coset has constant weight p/d², which is ≤ every identity-coset weight.
   - The reverse premise p_[I] ≤ p/d holds only at p = 1, where all weights are equal.
   - Ties among non-identity cosets are harmless.

   So the scout was wrong under the literal text and right under that reading, as far as (8) goes.
2. **The phase-copy sentence needs a scope.** It holds when 𝒯 contains a non-scalar element. If 𝒯 is scalar-only (𝒯 = {I}, or the centre with weights split evenly), literal (8) holds. The coset distribution is then the d² mixture weights:
   - It has more than dim H positive entries, so it is not admissible under Definition 1 (m ≤ dim H).
   - Its top entry 1−p+p/d² is below the true top output eigenvalue 1−p+p/d.

   So nothing usable results, but the sentence as written is false for that choice.
3. **Optional: your "no alternative representation" caveat can be closed.** I checked this argument:
   - Literal (8) gives Φ = (Σ_[U] p_[U] Ad_U)∘𝒯_𝒯, where 𝒯_𝒯 is the 𝒯-twirl.
   - D_p is invertible for p ≠ 1, while an idempotent twirl other than id has a kernel. So every element of 𝒯 must act as a scalar.
   - The Choi matrix J(D_p) has rank d² for p > 0, so there are at least d² positive-weight cosets, which exceeds d.
   - Each p_[U] ≤ λ_max(J) = 1−p+p/d², which is less than 1−p+p/d.

   Hence for 0 < p < 1, no representation satisfying literal (8) gives an admissible, valid majorizer. If you prefer not to rely on this, the caveat as written is correctly calibrated.

## Claim C: well calibrated, but reorder the emphasis and scope the version

- **Lead with the proof gap.** Theorem 2's proof cites Proposition 1, which is false. If the lifted channels are Φ₁⊗id and id⊗Φ₂, their majorization is automatic (shown under Claim A), so Proposition 1 carries the whole tensor step. Listing "hypothesis not met" first invites a "technicality" rebuttal.
- **The limitation is correct.** Nothing here shows the conclusion is false or rules out a repair that uses the extra structure.
  - You may add that a generic distinct-factor repair is impossible, by the Werner–Holevo example.
  - That example is not mixed-unitary: its Kraus span is the 3×3 antisymmetric matrices, which are all singular. So it says nothing about Theorem 2's own instance.
- **Check the factor count before writing "would cover n = 3".** A two-factor theorem does not iterate through the product Weyl representation. For 0 < p < 1, D_p⊗D_p with the product diagonal subgroup violates even distinct-coset (8):
  - p_[(0,1)] < p_[(0,0)].
  - Yet I⊗X has weight (1−3p/4)(p/4), which exceeds (p/4)², the weight of Z⊗Z in the identity coset.
- **Scope to v1** as accessed 2026-10-16.
- **Alhejji–Knill dating.** Dating the conjecture to v2 when you read v3 is an inference unless v2 §III was itself checked. I have not verified the Alhejji–Knill or Song–Chen statements.
- **The printed "inf".** For convex F it is reversed, and false as printed. Example: F(x) = x², D_{1/2}^{⊗2}, input Φ⁺ gives Σλ² = 19/64, below 25/64. Call it a misprint at most and rest nothing on it.

## Exact minimal fixes

**(B)** Replace "If one silently amends (8)… different hypothesis." with:
> "If (8) compares only distinct cosets (or uses strict <), the standard representation with the diagonal subgroup satisfies it for all 0 ≤ p ≤ 1; under that reading the scout's claim is correct as far as (8) goes."

**(B)** Replace "With actual group phase copies… fails." with:
> "With phase weights split evenly, the same failure occurs whenever 𝒯 contains a non-scalar element. For scalar-only 𝒯, literal (8) holds, but the coset distribution then has d² > dim H positive entries (inadmissible in Definition 1) and top entry 1−p+p/d² < 1−p+p/d."

**(C)** Replace the first sentence with:
> "The source (v1, accessed 2026-10-16) cannot be imported as a valid proof of depolarizing-output majorization: Theorem 2's proof invokes Proposition 1, which is false as stated; this is decisive however (8) is read. Separately, the standard representation fails (8) as printed, though not its distinct-coset reading."

## Safe priority wording

> Amosov (arXiv:2401.05104v1, 10 Jan 2024) states a tensor-product extremality result (Theorem 2), proved via output majorization, for mixed-unitary channels satisfying a coset-weight condition (Eq. (8)). Read as comparing distinct cosets, (8) is satisfied by the standard Weyl representation of the depolarizing channel for 0 ≤ p ≤ 1. As printed, it also compares weights within a coset, forcing them to be equal, which that representation violates for p < 1. The proof of Theorem 2 relies on Proposition 1 (Φ ≺ P, Ψ ≺ Q ⇒ Φ∘Ψ ≺ P⋆Q), which is false as stated: T(X) = (I_A/2)⊗tr_A X on C²⊗C² satisfies T ≺ (1/2,1/2), yet T∘T = T maps |00⟩⟨00| to a state with eigenvalue 1/2 > 1/4. [It also fails for channels on distinct tensor factors.] We therefore do not regard it as an established prior proof of our three-qubit result. We do not claim its conclusion is false, nor that the argument cannot be repaired using the additional structure.
