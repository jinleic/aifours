# Addendum 2 — the least CS congruence settles any R/L pair it separates; row bands

Owner **MathSemigroup-2 / original math-4**. Clock before writing (`/bin/date`): **Tue Oct 27 06:40:02 PDT 2026**.

**Status.** This is an additive **AUTHOR-WRITTEN / UNREVIEWED** successor to `semigroup-SEP-comparable-fibre-separation-and-RL-reduction-v1.md` (d7e9a9a2…9d5a), addendum 1 (68782978…fc63) and erratum 1 (cb09f3a0…19b5). None of those files is edited.

**Inputs.** Authority, sources, exclusions and limits are the same as there. The proofs are WRITTEN by hand.

Additional inputs used here, both inside the already named sources:

- the lemmas U1 (FACTOR) and U3 (PUSH) of U205, with that file's named Rees-homomorphism cut;
- the corollary in SQ-E §7 that the least completely simple congruence ξ is pure. That corollary keeps SQ-E's named ordinary existence fact for ξ.

## 1. Products of hosts

Let j_1 and j_2 be hosts over q, with bands B_1 and B_2.

Then s ↦ ((b¹_s, b²_s), q(s)) is a host into P(B_1 × B_2, C), where G acts diagonally. B_1 × B_2 ∈ V because V is a variety. The same holds for arbitrary products.

**Consequence.** SEP holds as soon as every individual R-pair and every individual L-pair in every fibre is separated by *some* host. No uniform construction is needed.

## 2. Corollary F (separation by ξ)

**Statement.** Let ρ ⊆ τ be any congruence with S/ρ completely simple and q_ρ idempotent pure. If q_ρ(e) ≠ q_ρ(f) for idempotents e, f with q(e) = q(f), then β(e) ≠ β(f).

In particular, the least completely simple congruence ξ is pure (SQ-E §7) and lies inside τ. Hence every fibre pair that ξ separates is separated by β.

**Corollary.** Suppose ξ separates every R-pair and every L-pair of every syntactic fibre. Then SEP holds, and S embeds into an allowed host.

*Proof.*

1. **A host over q_ρ.** Put D = S/ρ. Take the one-point band {b0}, which lies in V, and the trivial action. Then j_ρ(s) = (b0, q_ρ(s)) is a host over q_ρ, and it separates e from f.
2. **The factor map is pure.** By U205 Lemma U1, ker q_ρ ⊆ τ. So the induced map φ : D → C with φ∘q_ρ = q is a well-defined onto homomorphism. It is idempotent pure, by the FACTOR argument of U1.
3. **Push forward.** U205 Lemma U3 gives an injective homomorphism Ψ : P({b0}, D) → P(D_band, C) over φ, with D_band ∈ V.
4. **Conclusion.** Ψ∘j_ρ is a host over q, and it separates e from f because Ψ is injective. The universal property then gives β(e) ≠ β(f). ∎

**Example.** Take S = (I × Λ) × T, where T is an E-unitary orthodox monoid whose idempotent band lies in V. Here τ merges the columns, while ξ keeps them. So ξ separates the R-pairs (i, x, λ1) and (i, x, λ2).

**Limits of Corollary F.** In the band {g, e, f} (g an identity, {e, f} right zero), both ξ and τ are universal. So Corollary F does not apply there, although S embeds. Corollary F is sufficient only.

## 3. Row bands and the position-1 vertex class

For a row j of C, put

`E_j = { s ∈ E(S) : the row of q(s) is j }`.

**Lemma 3.1.** E_j is a subband of S, and it lies in V.

*Proof.* For s, t ∈ E_j, the product q(s)q(t) is the idempotent (j, p_(λ_t, j)⁻¹, λ_t). Purity then gives st ∈ E_j. The local corners of E_j lie inside E(kSk), which are regular bands, so E_j ∈ V. ∎

**Lemma 3.2.** Let e be an idempotent in row i, and let Vert(1, i) be the vertex class of R_e at position 1 for row i. Then:

1. Vert(1, i) = E(R_e).
2. E(R_e) is a right-zero subband, and it is an R-class of E_i.
3. If s ∈ E_i keeps one element of E(R_e) inside R_e, then s maps all of E(R_e) into E(R_e). The action a ↦ a·s is idempotent.

*Proof.*

- *Part 1.* a ∈ Vert(1, i) means g_a·p_(λ_a, i) = 1, which says that q(a) is idempotent. By purity, a is idempotent.
- *Part 3, all of E(R_e) stays.* This follows from VERT.
- *Part 3, images are idempotent.* The q-images of the images are idempotents, so purity makes the images idempotent.
- *Part 2.* R-related idempotents a and a' satisfy a·a' = a', so E(R_e) is right zero, and it is the R-class of e inside E_i. ∎

**Meaning.** At the base position, an R-pair (e, f) of a fibre is an R-pair of the band E_i ∈ V, acted on by right multiplication. Separating it by a host over q is therefore a "positioned" version of separating an R-pair inside a single band of V. Any construction for (R) must extend the right regular structure of these row bands across positions consistently.

Erratum 1 records why one-layer right-zero colourings are too weak. No such extension is proved here.

## 4. Status

**New WRITTEN author-level results:**

- §1 (products of hosts);
- Corollary F, together with its corollary for ξ;
- Lemmas 3.1 and 3.2.

**Still open.** (R)/(L) remain open in general. The original problem is not solved, and no counterexample is claimed. The same review requirements, quarantines and limits as in the main packet apply.
