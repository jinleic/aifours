# K7-pair-lemma-v1: twin pairs, the subgroup ⟨U_j, U_k⟩, and the unmarked consequences

- **Freeze record:** host-clock time and sha256 in `evidence/k7-pair-lemma-v1.sha256`.
- **Labels:** [NEW] means written in this lane; it is not a novelty claim.
- **Status:** unreviewed. No computation was run. K7 stays OPEN.
- **Builds on:**
  - `K7-structure-v1.md` (f4534c07…9fc1): K7-TWIN(b)–(d) and the families Q23/Q24;
  - `K7-block-lemma-v1.md` (93c3cd1f…29db3), used only in Corollary P2.
- **Imports (frozen written rules only):**
  - L6 (XE);
  - L5 (F), with 2 ≤ |T| ≤ 4 per erratum W1, using Sun(2), Sun(3) and Sun(4) inside a subgroup (imports);
  - L0.3.
- **No least-order frame.** No minimal-counterexample frame or Sun(7) is used. FH (the certificate rule) stays UNUSED: this file proves fixed lemmas, it does not enumerate fibres.

## Lemma K7-PAIR [NEW]

Let B = {j, k} ⊆ U be a twin block of size 2. Put W := ⟨U_j, U_k⟩ and m := [G:W].

- **(i)** m ∈ {3, 6}.
- **(ii)** If m = 3, then α_vB ∈ {2, 4} for every v ∉ B.
- **(iii)** If m = 6:
  - U_jU_k = W, a subgroup of index 6;
  - g_jW ≠ g_kW;
  - no g_vU_v with v ∉ B meets g_jW or g_kW;
  - each v ∉ B meets exactly α_vB of the other 4 cosets of W, with the F-packing of K7-BLOCK(c) and λ_v = n_v α_vB/6.

### Proof

**Step 1: what L6 gives.** For any v ∉ B, K7-TWIN(d) gives U_vU_j = U_vU_k. L6 applied to (v; j, k) gives:
- W ≠ G;
- m divides 6;
- t_v := [U_v : U_v ∩ W] = m·α_vB/6 ∈ ℤ.

Also t_j = t_k = 1, because U_j, U_k ⊆ W. By K7-TWIN(c), α_vB ≤ 4. In L5 (F) with H = W, each g_lU_l meets exactly t_l cosets of W. Inside a coset, the pieces are pairwise disjoint and are translates of cosets in W of subgroups of index λ_l = n_l t_l/m.

**Step 2: m = 2 is impossible.** If m = 2:
- α_vB/3 ∈ ℤ forces α_vB = 3, so t_v = 1 for all five v ∉ B. All seven vertices then have t = 1.
- W has only 2 cosets, so one coset contains the pieces of at least 4 vertices.
- λ_l = n_l/2 for every l, and gcd(n_x/2, n_y/2) = gcd(n_x, n_y)/2 = 3 for every pair, since all n are even.
- Sun(4) in W needs a pair with gcd ≥ 4. Contradiction.

So m ∈ {3, 6}, because m = 1 would mean W = G. This proves (i).

**Step 3: (ii).** If m = 3, then α_vB/2 ∈ ℤ for every v ∉ B.

**Step 4: (iii).** If m = 6:
- U_jU_k ⊆ W, and μ(U_jU_k) = 1/6 = μ(W), so U_jU_k = W.
- Disjointness gives g_j⁻¹g_k ∉ U_jU_k = W.
- For v ∉ B, λ_v = n_v α_vB/6, while λ_j = n_j/6 = w_j. Since gcd(w_j, λ_v) = 1, Sun(2) in W forbids v from meeting g_jW or g_kW.
- The rest is K7-BLOCK's argument with s = 2. ∎

## Corollary P1 (Q23, any marking) [NEW]

In the family Q23 (at least two 2-classes), every twin pair B has m = 6.

*Proof.*
- B lies in some 2-class, and some block of another class has β = 3 to B. So some v ∉ B has α_vB = 3, which rules out m = 3 by (ii).
- m = 2 is excluded by (i). ∎

## Corollary P2 (Q23 with M = ∅) [NEW]

If M = ∅, a K7 configuration of type Q23 has only singleton twin blocks.

*Proof.*
- Blocks of size ≥ 3 are excluded by K7-BLOCK(d), since M = ∅.
- Let B be a twin pair. By P1, m = 6. By (iii), the five outside vertices, all unmarked, lie in the 4 remaining cosets of W, each meeting t_v = α_vB ∈ {2, 3} of them, with λ_v = t_v w_v.
- The gcds are 2 for (2,2), 3 for (3,3) and 1 for (2,3). So inside a coset no mixed pair occurs; at most 2 vertices with t = 2 occur together, because a triple needs a pair with gcd ≥ 3; and at most 3 with t = 3 occur together, because a 4-set needs a pair with gcd ≥ 4.
- Let k_2 and k_3 be the numbers of outside vertices with t = 2 and t = 3, and c_2, c_3 the numbers of cosets used by each kind. No coset is shared, so c_2 + c_3 ≤ 4.
- Counting incidences: 2k_2 ≤ 2c_2 and 3k_3 ≤ 3c_3. Hence 5 = k_2 + k_3 ≤ c_2 + c_3 ≤ 4. Contradiction. ∎

## Corollary P3 (Q24 with M = ∅) [NEW]

If M = ∅, then in a K7 configuration of type Q24, every twin pair B has **at least three** outside vertices v with α_vB = 4.

*Proof.* All five outside vertices are unmarked, with α_vB ∈ {2, 4}. Let k_4 be the number with α_vB = 4. By (i), m ∈ {3, 6}.

**Case m = 3.** W has 3 cosets.
- For v ∉ B: α_vB = 2 gives t_v = 1 and λ_v = 2w_v ("light"); α_vB = 4 gives t_v = 2 and λ_v = 4w_v ("heavy").
- j and k are light, with t = 1 and λ = 2w.
- The gcds are 2 for light–light, 2 for light–heavy and 4 for heavy–heavy.
- So an allowed set in a coset has at most 4 vertices. If it has at least 3 vertices, it has at most one light vertex, because every triple needs a pair with gcd ≥ 3.
- Hence a coset holding 2 light vertices holds nothing else, and at most 6 light incidences fit in total.
- The light incidences number 2 + (5 − k_4) = 7 − k_4.

| k_4 | light incidences | contradiction |
|---|---|---|
| 0 | 7 | more than 6 |
| 1 | 6 | all three cosets hold exactly 2 light vertices, leaving no coset for the heavy vertex |
| 2 | 5 | two cosets hold 2 light vertices and nothing else, so both heavy vertices must use 2 distinct cosets among the single remaining one |

So k_4 ≥ 3.

**Case m = 6.** By (iii), the five outside vertices lie in the 4 remaining cosets.
- Heavy vertices (α_vB = 4) meet all 4 cosets; light vertices (α_vB = 2) meet 2. λ_v = α_vB·w_v, with the same gcd pattern as above.
- An allowed coset set has at most 4 vertices, and at most one light vertex once it has at least 3.

| k_4 | contradiction |
|---|---|
| 0 | at most 2 light vertices per coset: 10 incidences against a capacity of 8 |
| 1, 2 | at most one light vertex per coset: 2(5 − k_4) > 4 light incidences needed |
| 4 | every coset already holds 4 vertices, so the light vertex cannot be placed |
| 5 | 5 vertices per coset |

So k_4 = 3.

In both cases k_4 ≥ 3. ∎

## What this changes, and what it does not

When M = ∅ (all seven vertices unmarked), the earlier lemmas leave:
- K7-Q5: Q5 is removed;
- K7-BLOCK: blocks have size ≤ 2;
- P2: Q23 has singleton blocks only;
- P3: in Q24, every twin pair B has at least three outside vertices with β(B, ·) = 4.

**Remaining cases for M = ∅:**
- Q23 on seven singletons: a partition into at least two 2-classes, with α = 2 inside a class and α = 3 across;
- Q24 with blocks of size ≤ 2, subject to P3.

**Not covered:** the marked cases (M ≠ ∅) beyond P1, and size-3 blocks with M ≠ ∅.

**Use in a future enumeration.** These consequences may be added only as a recorded **conditional layer**, as in K7-enumeration-spec-v1 §5, and only after review. A run that uses them has K7-PAIR as an extra premise. No class is removed here.
