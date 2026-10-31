# Four-qubit depolarizing prefixes k=5,6,10,11

**Disposition: same-harness written support for the stated prefix comparisons.** Let `Φ_p(X)=(1−p)X+(p/2)Tr(X)I₂`. For every four-qubit density `ρ` and `p∈[0,4/3]`, the sum of the `k` largest output eigenvalues of `Φ_p^{⊗4}(ρ)` is at most the corresponding sum for `Φ_p^{⊗4}(|0000⟩⟨0000|)`, for `k∈{5,6,10,11}`. This does not establish k=3, the other prefixes, full majorization, or the original unrestricted claim.

Native clock observed before composing: **2026-10-28T21:13:10-0700 PDT**, not an asserted creation time. No novelty, human review, independent-model-family review, or formal/kernel proof is claimed. No historical held result is a premise.

## Dual lemma and reconstruction

For four-qubit operators define `H₁(X)=Σ_i I_(complement i)⊗Tr_(complement i)X` and full spin flip `X̃=Y^{⊗4}XᵀY^{⊗4}`. For every complex orthogonal projector `Q` of rank `r∈{5,6,10,11}`,

`H₁(Q)+Q̃ ≥ (2r−5)I₁₆`.

Rotate each local marginal to `(r/2)I+(m_i/2)Z`, `m_i≥0`; both maps are covariant under local unitaries, with the U(2) determinant phases cancelling in the full spin flip. Put `S=Σm_i`. Ky Fan bounds for `Σ_iZ_i` and for each three-site sum give `S≤12` and `Σ_{j≠i}m_j≤10` at these ranks. Thus `H₁(Q)−(2r−5)I=5I+(1/2)Σm_i Z_i` is positive if `S≤10`. Otherwise let `c=(S−10)/2∈(0,1]` and `E=|1111⟩⟨1111|`; every computational eigenvalue except at E is at least c, while E has eigenvalue −c. Hence the operator is at least `c(I−2E)`.

For `N=Σ(I−Z_i)/2`, `Π₁` the rank-four weight-one projector and `E₀=|0000⟩⟨0000|`, `N≥2I−2E₀−Π₁` and `Tr(QΠ₁)≤4` imply `S≤8+4q`, where `q=⟨1111|Q̃|1111⟩=⟨0000|Q|0000⟩`. Thus `q≥(1+c)/2`. For any projection R with this overlap, the only nontrivial block of `R+c(I−2E)` has nonnegative diagonal and determinant `c(2q−1−c)≥0`; the complement is `R+cI≥0`. Taking `R=Q̃` proves the lemma. The three-site spectral cut exceeds 10 at ranks 7,8,9; the proof is not extended to them.

For a density define `H₂(ρ)=Σ_{i<j}I_(complement ij)⊗ρ_ij` and `F(ρ)=Σ_{i,a∈{X,Y,Z}}σ_i^aρσ_i^a`. One-qubit spin flip and Pauli twirl give the exact identity

`H₂(ρ)−H₁(ρ)+I = ρ+ρ̃+F(ρ)/2`.

Self-adjointness in the trace pairing and the dual lemma yield `Tr(QH₂(ρ))≥r−5` for the **same** Q. The sum of actual one-qubit marginals is a convex combination of local-unitary conjugates of the four-site occupancy operator; its bottom-r sum gives `Tr(QH₁(ρ))≥2r−6`.

For `0≤p≤1`, put `t=1−p`, `b=p/2`, `a=t+b`. The erasure expansion has positive remainder and implies

`Φ_p^{⊗4}(ρ) ≥ b⁴I+t b³H₁(ρ)+t²b²H₂(ρ)`.

Therefore each rank-r trace is at least `rb⁴+(2r−6)tb³+(r−5)t²b² = b⁴+4ab³+(r−5)a²b²`, exactly the bottom-r product-reference sum. Minimizing over Q and using unit trace gives prefixes `k=16−r`. At `p=1` the output is uniform. For `1≤p≤4/3`, full transpose spin flip identifies the output spectrum with that at `2−p∈[2/3,1]` and preserves the reference multiset; the positive-erasure bound itself is **not** used with negative t. Ties and p=0 are covered.

## Evidence and qualifications

Parent read the complete [rank-six candidate](../../../../physics/evidence/three-area-20261027-96h/parallel-18/depolarizing-majorization4/frontier-20261028-98-rank6-global-k10.md), 131 LF, SHA-256 `05c04b8b093835c2a0fe63e849e2552c012ef1d33a7b35e78a9738ebce0799f2`, complete [other-ranks candidate](../../../../physics/evidence/three-area-20261027-96h/parallel-18/depolarizing-majorization4/frontier-20261028-100-rank10-11-global-k5-k6.md), 108 LF, `108322fa2469cb6a374b9b8cca633e78e8810169f6cdb7b7183cef26cdb188db`, and complete [f130 review](../review-waves/f130-depolarizing-global-k10-k5-k6/review-v1.md), `a0d968c23ce32998ec92fbeaff02ce487a330031ac48d09efc43daa64bad59be`. The reviewer reconstructed the entire argument without executing author code, with no FATAL/MAJOR and six presentation/reproducibility MINORs. The candidate's unnamed finite-example weight-two vectors and cited out-of-manifest packet 94 are not imported; no k12–15 coverage is inferred here.

The reviewer independently ran exact non-diagonal complex/projector/local-rotation/erasure controls, documented in [its exact receipt](../review-waves/f130-depolarizing-global-k10-k5-k6/reviewer-exact-controls-v1.result.json), `2e7910c83dfd10994f14404b2575eb1c700ae692a3fc289d0dde848488c50d27`, plus separate floating searches. Only the written proof carries universal quantifiers; neither a floating search nor finitely many exact projectors proves them.

Parent wrote and ran a separate rational [control program](../review-waves/f130-depolarizing-global-k10-k5-k6/parent-dual-prefix-controls-v1.py), SHA-256 `e6079c5737eea4ef9212bb7358d2bbd4f4d0e98a7df540fbb5f88c3b3a64f6f8`; [result](../review-waves/f130-depolarizing-global-k10-k5-k6/parent-dual-prefix-result-v1.json), `f1962ba26a0131c94b3907a206a9df357243f797e55d9b01a35b07c4e5530b06`. It checks the four rank-specific spectral cuts, four actual non-diagonal rational projectors and exact PSD pivots, 20 scalar determinant identities, 16 reference-polynomial identities and negative controls for an increased threshold and the excluded-rank cut. These are exact instance checks, not full proof-assistant verification.

The open k3 and other uncovered prefix cases remain separate; no claim about operational distillability, worldwide priority or an unrelated theorem follows.
