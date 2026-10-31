# Parent disposition — physics-3-ppt-complement-cone-and-reconstruction-barrier-parent

Observed clock before writing: **2026-10-27T16:28:45-0700 PDT**. Same-harness written disposition; not formal/kernel, human, configured-family, executable or novelty acceptance. Independent-model CLI review not performed.

## Inputs read completely by Main (raw windows, through endings)

- Author [prerequisite-derivation-v1.md](/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/ppt-schmidt44/prerequisite-derivation-v1.md) SHA256 `7d00196376108da34c416b8e80f815adfc337d01cb24191f8ad40f6a47d8cdc4`, 208 LF (1–70, 71–140, 141–208).
- Author [prerequisite-derivation-v1-addendum-1.md](/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/ppt-schmidt44/prerequisite-derivation-v1-addendum-1.md) SHA256 `02beb05df29588703aa46ced25d103ea6ec1aefcbf042c61f6f3df1c1d2d29bf`, 111 LF (1–60, 61–111).
- w14 review by InfoResearch96h-2: [review](/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/review-w14-physics-3-v1-v1.md) SHA256 `6262274cd2627da65f6e8fcde01a90c2eab8feb1a8a9428ecc4e7e010b9c2a90`, 154 LF; verdict 0F/0M/0m.
- w50 review by MathResearch96h-2: [review](/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/phase-type/review-w50-ppt-all-pt-reconstruction-barrier-v1.md) SHA256 `30894deb794b9952dd50485c255f0ff532b1d2cf0ce6b6532e62d46803059e6b`, 169 LF; verdict 0F/0M/0m.

## Parent checks

Main re-derived: Ψ_d(X)=Σ_{i<j}A_ij X A_ij* = Tr(X)I − Xᵀ for A_ij=|i⟩⟨j|−|j⟩⟨i|, hence R_A(ρ)=(Ψ_a⊗id)(ρ^{Γ_A}) is a sum of positive terms with Alice support ≤2; the pairing inequalities Tr(W X_A)=b_A−a0 ≥ 0, Tr(W X_B)=b_B−a0 ≥ 0, Tr(W X_AB)=t−b_A−b_B+a0 ≥ 0; the sector eigenvalues (a−1)^p(b−1)^q on I⊗I and ±1 on the doubly traceless sector; Hilbert–Schmidt orthogonality of local-unitary and partial-transpose words on that sector; and the spanning of all Hermitian operators by positive product operators.

## Disposition

**ADOPTED at same-harness written-support scope (arbitrary a,b ≥ 2; barrier needs a,b ≥ 3, which includes 4×4):**

1. For every PPT ρ, the one-sided trace complements I_A⊗ρ_B−ρ and ρ_A⊗I_B−ρ are PPT and lie in the unnormalized Schmidt-number-≤2 cone C2, via explicit rank-two Kraus decompositions; the double complement sI−I⊗ρ_B−ρ_A⊗I+ρ lies in C2 for every positive ρ. Hence sI−ρ ∈ C2 for PPT ρ (a trace-complement statement, not ρ ∈ C2).
2. For every Hermitian W that is nonnegative on all Schmidt-rank-≤2 vectors, Tr(W)I−W has an explicit decomposable representation (not a decomposition of W).
3. For the same actual pair, b_A+b_B−t ≤ Tr(Wρ) ≤ min(b_A,b_B); a negative eligible PPT/witness pair therefore requires b_A+b_B < t.
4. **Barrier:** no nonnegative finite combination, or norm limit, of maps L∘R_A^pR_B^q∘T (p+q ≥ 1; T any finite word of local-unitary conjugations and partial transposes; L an output local-unitary conjugation) together with the noise maps L∘D∘T equals a positive multiple of the identity — even when equality is demanded only on PPT states. So that fixed positive-reconstruction mechanism cannot prove that all PPT states have Schmidt number ≤2.

## Not established

No PPT state with Schmidt number ≥3, no proof that all 4×4 PPT states have SN ≤2, no state-dependent or nonlinear reconstruction exclusion, no output partial-transpose claim, no source/book equivalence and no novelty (these classical-flavoured identities are not claimed new). The JL source-audit STOP and the author's stopped nonunitary/marginal-normalization branch remain. Original target OPEN.
