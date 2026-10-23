**VERDICT: ACCEPT-WITH-FIXES**

- FATAL: none.
- MAJOR: none.
- MINOR: 9. They concern scope hygiene and presentation. None of them affects whether any stated result is true.

I re-derived every implication from the embedded text and the granted imports. No step fails and no counterexample exists at the stated scope. I reviewed the text as pasted; I could not recompute the SHA because I have no tools.

## Scope of acceptance (after the fixes)

- **LFC (a)–(d):** holds for any finite G, k ≤ 7 and any vertex v.
- **INV (a):** holds.
- **INV (b):** the inequality α_vj + α*_vj ≤ g_vj follows from first principles (D3).
  - The identification "VFC q_j = α*_vj" holds if (V1) defines q_j by μ(U_v h U_j) = q_j/g_vj. That definition is not embedded, so I could not check it.
- **ROW-U (i)–(iii):** holds.
- **K7-M0:** holds for every group with finite-index U_i, via R0.
- **K63-U0:** holds for finite G as written; the R0 lift is immediate (m6).
- **Not covered:** marked K7, marked K6.3, K6.2*, K5.3 and Sun(7). The file correctly does not claim any of these.

## MINOR findings

- **m1. §0 "Imports, at exactly these scopes" vs. §2 INV(b) proof, last sentence "(L0.3)".**
  - L0.3 is used but is not in the import list (L0.1, L0.2, L0.6).
  - Fix: add L0.3, or inline the identity μ(U_vU_j) = |U_v||U_j|/(|U_v∩U_j||G|) = I_vj/(n_v n_j) = α_vj/g_vj.

- **m2. §3 ROW-U proof ("coprime … to every alpha <= 5", the R1/R24/R3/R5 split) and §5 Step 1 ("alpha_vd in {1,2}").**
  - These use 1 ≤ α_ij ≤ g_ij − 1 for a disjoint pair without proof or citation.
  - The fact is true (D0). State it and cite the L0 item that carries it.

- **m3. §0 import line omits Sun(2).**
  - Sun(2) is used: cross-class pairs, R1 singletons, and d being singleton-only in §5 Step 1.
  - It is covered by the granted t ≤ 6 import and is elementary (coprime indices give HK = G). List it.

- **m4. §1 proof of (c), "By (b), v is not in S_C".**
  - This is a mis-citation. v ∉ S_C holds by the definition (j ≠ v).
  - The fact that matters is that no v-piece lies in a fibre C ≠ g_vU_v, because distinct left U_v-cosets are disjoint.
  - (b) is genuinely needed only in (d). This is a wording fix only.

- **m5. Notation, §1–§5.**
  - y_j denotes both a point of g_jU_j ∩ C (proof of (c)) and an LP weight ((d), §3, §5).
  - g_v (a coset representative) and g_vj (a gcd) share a symbol.
  - V is never defined.
  - Fix: rename the point (for example p_j) and define V := {1,…,k}.

- **m6. §5 Statement covers finite G only.**
  - The R0 lift sentence that §4 has is missing here.
  - R0 preserves the index tuple and disjointness (D7), so the sentence can simply be added.

- **m7. §2 (a), "lies in the same class (K7, K6.2\*, K6.3, K5.2\*, K5.3, KII) with the same marking", and the "Consequence used below".**
  - This is correct exactly for classes determined by the labelled index tuple.
  - The definitions of K6.2\*, K5.2\*, K5.3, KII and "profiles" are not embedded, so the claim is unverifiable here.
  - It is load-bearing only for unmarked K7 in §4, where the theorem's own hypothesis guarantees it.
  - Fix: restrict the sentence to index-defined classes, or cite the definitions.

- **m8. Unverifiable external cross-references (none is load-bearing).**
  - Affected text:
    - §2 (b): "VFC integer q_j of (V1)".
    - §1 Remarks (1)–(3).
    - §4 "Relation" (Q24, Q5, Q23U).
    - §5: "exactly the K6.3 configurations …" and "subsumes … D3".
  - Mark these as pending parent cross-check.
  - §4 needs only α + α* ≤ g, and that does not depend on VFC (D3). D1 confirms the mechanism behind Remark (3).

- **m9. §3 (i), branch "k3 <= 3".**
  - The claim "(value of the ≥3 remaining elements) ≥ 3" relies on a bound stated only inside the k3 ∈ {4,5} branch.
  - State it once: on R1 ∪ R24 with N elements, the standard weights give value ≥ min(N, 4).
  - The same bound yields §5 Step 1's "≥ 4".
  - The clause "with b ≥ 3 at least 4" is vacuous in the k3 ∈ {4,5} branch, because at most two elements remain there.

## Independent derivation log

**D0. Preliminaries (used but not proved in the file)**

- α_ij is an integer, because n_i and n_j both divide I_ij.
- α_ij ≤ g_ij, because [U_i : U_i∩U_j] = |U_iU_j|/|U_j| ≤ n_j.
- μ(U_iU_j) = α_ij/g_ij.
- g_iU_i ∩ g_jU_j = ∅ if and only if g_i⁻¹g_j ∉ U_iU_j. Therefore U_iU_j ≠ G and α_ij ≤ g_ij − 1.
- Consequences: in K7, every α ∈ {1,…,5}; in K63-U0, α_vd ∈ {1,2}.

**D1. Left/right conventions and conjugation**

- Take p ∈ g_jU_j ∩ xU_v. Then g_jU_j = pU_j and xU_v = pU_v, so the piece is p(U_j∩U_v).
- Since x⁻¹p ∈ U_v, the translated piece is a left coset in U_v of the *unconjugated* subgroup U_j∩U_v. Its index is λ_j, and the subgroup is the same for every fibre.
- So LFC's fibre indices need no conjugation, and they match the unconjugated I_vj in α.
- Cross-check with right fibres U_v z (normalise g_v = 1, h = g_v⁻¹g_j):
  - The piece is p(U_j ∩ p⁻¹U_v p).
  - Its index is [U_v : U_v∩hU_jh⁻¹] = n_jα*_vj/g_vj.
  - That index is conjugated but fibre-independent, and it equals λ* of the inverted configuration.
- This is exactly the left/right swap that INV performs, so the conventions are consistent.

**D2. LFC**

- **(a)** follows from |U_v∩U_j| = |G|/I_vj and I_vj = n_v n_j α_vj/g_vj.
- **(b)**
  - The cosets g_juU_v (u ∈ U_j) coincide if and only if u⁻¹u′ ∈ U_j∩U_v. That gives exactly t_j cosets.
  - If one of them equalled g_vU_v, then g_ju would lie in g_jU_j ∩ g_vU_v, contradicting disjointness.
- **(c)**
  - The pieces inside one fibre C are pairwise disjoint left cosets in U_v, with indices λ_j.
  - |S_C| ≤ 6.
  - Sun(|T|) applies to each sub-family T with 2 ≤ |T| ≤ 6.
  - "Allowed" is hereditary by definition.
- **(d)**
  - Each j lies in exactly t_j of the sets S_C, and by (b) all of those fibres differ from g_vU_v.
  - Hence Σ_j t_j y_j ≤ n_v − 1.
  - The LP constraints run over all allowed T, which includes every S_C. This is a relaxation in the safe direction.

**D3. INV and q = α\***

- **(a)**
  - (g_iU_i)⁻¹ = U_ig_i⁻¹ = g_i⁻¹(g_iU_ig_i⁻¹).
  - Inversion is a bijection of G, and conjugate subgroups have equal index.
  - Inverting twice returns the original configuration.
- **(b)**
  - Conjugation by g_v⁻¹ sends U_v\*∩U_j\* to U_v∩hU_jh⁻¹.
  - |U_vhU_j| = |U_v||U_j|/|U_v∩hU_jh⁻¹|, so μ(U_vhU_j) = α\*_vj/g_vj.
  - Disjointness gives h ∉ U_vU_j. So U_vhU_j and U_vU_j are distinct, hence disjoint, (U_v,U_j)-double cosets.
  - Therefore α + α* ≤ g. This needs nothing from VFC.
  - Symmetry: the double coset seen from j is (U_vhU_j)⁻¹, which has the same size.
- **Sanity check in S₃:**
  - Take U_v = ⟨(12)⟩ and g_jU_j = (23)⟨(13)⟩.
  - |U_vU_j| = 4, so α = 2 with g = 3.
  - h = (23) ∉ U_vU_j.
  - hU_jh⁻¹ = ⟨(12)⟩, so α* = 1, and the remaining double coset has μ = 1/3.
  - This shows α* ≠ α in general, and that the bound α + α* ≤ g can be tight.

**D4. ROW-U**

*gcd reduction.* The primes dividing any w are ≥ 7, the w's are pairwise coprime, and α ≤ 5. Hence gcd(w_jα_j, w_j′α_j′) = gcd(α_j, α_j′). This is independent of whether v is marked, because g_vj = 6 either way.

*Exact allowed family.*
- An allowed pair needs gcd ≥ 2, so every allowed set of size ≥ 2 lies inside one of R24, R3 or R5. R1 elements appear only as singletons.
- R3: allowed sets have size ≤ 3.
- R5: allowed sets have size ≤ 5.
- R24:
  - all pairs are allowed;
  - a triple is allowed if and only if it contains at least two fours;
  - a 4-set is allowed if and only if it contains at most one two;
  - no 5-set is allowed.
- This matches the file. It is exact, and in particular no allowed set is missing, which is the direction that feasibility needs.

*Feasibility of the weights:*

| regime | weights y | worst allowed sets → weight sum | value Σyα |
|---|---|---|---|
| R1 | 1 | {j} → 1 | k1 |
| R3 | 1/min(3,k3) | min(3,k3) elements → 1 | 3, or k3 |
| R5 | 1/min(5,k5) | min(5,k5) elements → 1 | 5, or 6 |
| R24, b≤2 | 2↦½, 4↦¼ | {2,2} → 1; {2,4,4} → 1; no 4-sets, no {4,4,4} | a+b |
| R24, b=3 | 2↦0, 4↦⅓ | {2,4,4,4} → 1; {4,4,4} → 1 | 4 |
| R24, b≥4 | ¼ | at most 4 elements → ≤ 1 | a/2+b ≥ 4 |

*Case analysis.*
- **(i)**
  - k5 ≥ 1 gives value ≥ 6.
  - k5 = 0 and k3 = 6 gives value 6.
  - k3 ∈ {4,5} gives k3 + (6 − k3) = 6.
  - k3 ≤ 3 gives 3 + min(6 − k3, 4) ≥ 6.
- **(iii)** b ≤ 2 gives k1 + a + b = 6.
- **(ii)** b ≥ 3 and k1 ≥ 2 give value ≥ 6.
- Every case contradicts the LFC bound Σyα < 6.

*Sun usage.* Sun(6) is used only when k5 = 6. No fibre ever carries more than six pieces.

*Sanity check of what survives.* The LP optimum is 5 for the row (1,2,2,4,4,4), for (2,2,2,4,4,4) and for (2,2,4,4,4,4). It is 5.5 for (2,4,4,4,4,4). So rows allowed by ROW-U really are LFC-consistent, and the contradiction has to come from the next step.

**D5. K7-M0**

- By INV(a), the inverted configuration is again unmarked K7, with λ\*_j = w_jα\*_vj. So ROW-U applies to both the α-row and the α\*-row at every v.
- If α_vj = 4 then α\*_vj ≤ 2. So A4(v) and A4\*(v) are disjoint subsets of six neighbours, each of size ≥ 3, and both have size exactly 3.
- α is symmetric, so the graph with edges {ij : α_ij = 4} is 3-regular on 7 vertices.
- Its degree sum would be 2|E| = 21, which is odd. The argument is valid.

**D6. K63-U0**

*Setup.*
- g = 6 within C.
- For v ∈ C, g_vd = 3·gcd(2w_v, w_d) = 3.

*Step 1 (rule out α_vd = 1).*
- λ_d = w_d is coprime to every λ_j = w_jα_vj, so d lies only in singleton allowed sets.
- Putting y_d = 1 is therefore feasible, and it contributes ⅓.
- The five C-neighbours contribute value ≥ 4:
  - k5 ≥ 1 gives ≥ 5;
  - k3 ≥ 4 gives ≥ 4;
  - k3 ∈ {1,2,3} gives 3 + min(5 − k3, 4) ≥ 4;
  - otherwise the value is ≥ min(5, 4) = 4.
- Total ≥ 4/6 + 1/3 = 1, which contradicts LFC at v.

*Step 2 (all α_di = 2).*
- λ_i = 4w_i for every i ∈ C, and all pairwise gcds equal 4.
- So the allowed sets are exactly the sets of size ≤ 4; Sun(5) excludes 5-sets.
- Taking y ≡ ¼ gives 6·¼·⅔ = 1, which contradicts LFC at d.

*Imports used.* Sun(2) through Sun(5). Not Sun(6), and not INV.

**D7. R0**

- Let N be the intersection of the cores of the U_i. N is normal, of finite index, and contained in every U_i.
- Each g_iU_i is a union of N-cosets, so the images in G/N are pairwise disjoint left cosets of index n_i.
- The file uses R0 appropriately: only to lift K7-M0 to arbitrary G. LFC and INV are stated for finite G, where μ makes sense.
- K63-U0 lacks the lift sentence (m6).

**D8. Mutation controls**

- **(1) Confirmed.** Fibres carry at most six pieces only because v's coset is a whole, exclusive fibre. Without that, a fibre could carry seven pieces and Sun(7) would be needed.
- **(2) Confirmed.** If q is unconstrained, nothing makes it the α-matrix of a K7 configuration, so ROW-U cannot be applied to it.
- **(3) Confirmed, with an explicit witness.**
  - Take the complement of the 7-cycle as the 4-graph; it is 4-regular.
  - Give every row the pattern (2,2,4,4,4,4); each such row has LP optimum 5 < 6.
  - So the bound |A4(v)| ≥ 3 alone gives no contradiction. The parity step genuinely needs the INV complement.
