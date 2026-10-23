# proof-v1: candidate proof of Sun's disjoint-coset conjecture for k = 5

- **Lane:** `mathematics/evidence/six-lane-20261016/sun-coset5`.
- **Written:** 2026-10-18 from 09:42 PDT (host clock). The freeze time and sha256 are recorded in `evidence/proof-v1.sha256`.
- **Status:** CANDIDATE. This is a computer-assisted proof, unreviewed and not Lean-checked.
  - It uses five new lemmas: T/L/K/P, N2, F+H2, M1/M2 and R. None has yet been re-derived by the parent or hostile-reviewed.
  - Novelty is not established. A search miss is not novelty.

## Theorem

Let G be any group. Let a_1G_1, …, a_5G_5 be pairwise disjoint left cosets of subgroups of finite index. Then gcd([G:G_i], [G:G_j]) ≥ 5 for some i < j.

## Proof structure

1. **R0** (README §2): we may assume G is finite.
2. **R1** (README §2): it suffices to prove **Core(5)**. Core(5) asserts that no finite group has subgroups U_1, …, U_5 with [G:U_i] = 4r_i, the r_i pairwise coprime, and pairwise disjoint cosets g_iU_i.
   - R1 uses M-S Props 4.2, 4.3 and 4.5 (Beitr. Algebra Geom. 60 (2019)). Zhu Theorems 2.2 and 3.1 supply Props 4.2 and 4.3 independently.
3. Suppose Core(5) fails. Choose a counterexample with |G| minimal among finite groups containing five pairwise disjoint cosets with all pairwise index-gcds ≤ 4. Then every proper subgroup satisfies Sun's statement for k = 5. Also, Sun's statement for k ≤ 4 holds in every group (Sun 2006 for k = 2; Zhu Theorem 1.1 for k = 3, 4).
4. **Pattern of the counterexample.** Define α_ij = [G : U_i∩U_j]/(4r_ir_j) ∈ {1, 2, 3} (rules-v1 L0.3). Let E2 be the vertex with r even and E3 the vertex with 3 | r, if they exist. After relabelling, (α, E2, E3) is one of the 21,150 patterns enumerated by the frozen program `code/core5_engine_v1.py` (sha256 65ce5a00…2eb1).
5. **The frozen run.**
   - Location: `evidence/engine-v1-run1/`, certificates in `certificates.tsv.gz`.
   - Every pattern but one has a certificate naming a lemma of `rules-v1.md` and its witness: T (20,465 patterns), K (637), P-Bonferroni (20), N2 (5) and F with H2 (22).
   - Each certificate shows that no Core(5) configuration with that pattern exists; L8 (M1, M2) justifies evaluating at τ_min and at representative r.
   - The one survivor is the pattern **S-D**:
     - α01 = α02 = 1, α03 = α04 = 2, α12 = α13 = α14 = α23 = α24 = α34 = 3;
     - E2 = 1 (r_1 even, 3 ∤ r_1);
     - E3 = 0 (3 | r_0, r_0 odd);
     - r_2, r_3, r_4 coprime to 6.
6. S-D is refuted below by the new Lemma R. Hence no counterexample exists. ∎

## Lemma R: right-coset fibres over a vertex subgroup [NEW, unreviewed]

**Setting.** Harmonic configuration (rules-v1 §0). Fix a vertex v, and translate so that g_v = 1. For j ≠ v put D_j = U_v g_j U_j, a (U_v, U_j)-double coset, and d_j = |D_j| / |U_j|.

**Statement.**
- **(R1)** D_j ∩ U_vU_j = ∅. So D_j ⊆ G ∖ U_vU_j.
- **(R2)** |D_j| is a positive multiple of |G| / gcd(n_v, n_j).
- **(R3)** Every right coset U_vy contained in D_j meets g_jU_j. If w ∈ g_jU_j ∩ U_vy, then g_jU_j ∩ U_vy = (U_v ∩ wU_jw⁻¹)w, and [U_v : U_v ∩ wU_jw⁻¹] = d_j.
- **(R4)** Let C = U_vy be a right coset, and let S_C = {j ≠ v : C ⊆ D_j}. If |S_C| = s ≥ 2, then gcd(d_j, d_k) ≥ s for some j ≠ k in S_C.
- **(R5)** If D_j ∩ D_k ≠ ∅ (j ≠ k), then D_j ∩ D_k contains a whole right coset U_vy. Hence gcd(d_j, d_k) ≥ 2.

**Proof.**
- **(R1)** By L0.2, disjointness of g_vU_v = U_v and g_jU_j gives g_j ∉ U_vU_j. Now U_vU_j = U_v·1·U_j is the double coset of 1. Distinct double cosets are disjoint, so D_j ∩ U_vU_j = ∅.
- **(R2)** This is L0.4.
- **(R3)** Take U_vy ⊆ D_j.
  - Write y = c g_j u with c ∈ U_v and u ∈ U_j. Then U_vy = U_v g_j u contains g_ju ∈ g_jU_j.
  - For w ∈ g_jU_j ∩ U_vy we have g_jU_j = wU_j and U_vy = U_vw. Then x ∈ wU_j ∩ U_vw ⟺ xw⁻¹ ∈ wU_jw⁻¹ ∩ U_v.
  - The index is [U_v : U_v ∩ wU_jw⁻¹] = |U_v · wU_jw⁻¹| / |wU_jw⁻¹| = |U_vwU_j| / |U_j| = |D_j| / |U_j|, since w ∈ D_j.
- **(R4)** Fix w_0 ∈ C. By (R3), for each j ∈ S_C the piece g_jU_j ∩ C is a right coset (U_v ∩ w_jU_jw_j⁻¹)w_j with w_j ∈ C.
  - Right-multiplying by w_0⁻¹ gives right cosets A_j c_j of subgroups A_j ≤ U_v with [U_v : A_j] = d_j, where c_j = w_jw_0⁻¹ ∈ U_v.
  - These cosets are pairwise disjoint, because the g_jU_j are. Inversion turns them into the pairwise disjoint left cosets c_j⁻¹A_j of U_v.
  - So (d_j)_{j∈S_C} is U_v-harmonic. Sun's statement for k = s holds in U_v: by L0.6 for s = 2, Zhu for s = 3, 4. Here s ≤ 4 automatically, since S_C ⊆ the other vertices.
- **(R5)** D_j and D_k are both left U_v-invariant, so their intersection is too. A non-empty left U_v-invariant set contains a full right coset U_vy. Apply (R4) with s ≥ 2. ∎

**Core(5) form.** By (R2), |D_j| = s_j |G|/4 with s_j a positive integer. By (R1), s_j ≤ 4 − α_vj. Then d_j = s_j |G|/4 ÷ (|G|/(4r_j)) = s_j r_j.

## Refutation of S-D

Assume a Core(5) configuration with pattern S-D. Take v = 2, translate so that g_2 = 1, and put X_j = U_2U_j for j ∈ {0, 1, 3, 4}.

**Step 1: sizes.** By L0.3, |X_0| = α_20 |G|/4 = |G|/4 and |X_1| = |X_3| = |X_4| = 3|G|/4. For j ∈ {1, 3, 4} put Y_j = G ∖ X_j, so |Y_j| = |G|/4.
- By (R1), D_j ⊆ Y_j. By (R2), |D_j| is a positive multiple of |G|/4. Hence D_j = Y_j, s_j = 1 and d_j = r_j.

**Step 2: Y_1, Y_3, Y_4 are pairwise disjoint.** Suppose not. By (R5), gcd(d_j, d_k) = gcd(r_j, r_k) ≥ 2 for some j ≠ k, contradicting coprimality.

**Step 3: X_0 ⊆ X_1 ∩ X_3 ∩ X_4.** Use rules-v1 L1 in the triangles {0, 1, 2}, {0, 2, 3} and {0, 2, 4}.
- In {0, 1, 2}: by (T2), τ ≤ α01·α02 = 1, so τ_012 = 1.
- In {0, 2, 3}: (T1) gives α03 = 2 | r_2 τ with r_2 odd, so τ is even. (T2) gives τ ≤ α02·α03 = 2. Hence τ_023 = 2. Likewise τ_024 = 2.
- By (T3) with apex 2:
  - |U_2(U_0∩U_1)| = τ_012 |G| / (4α01) = |G|/4;
  - |U_2(U_0∩U_3)| = τ_023 |G| / (4α03) = |G|/4;
  - and the same holds for U_4.
- Each of these sets lies inside X_0 = U_2U_0, which has size |G|/4. So X_0 = U_2(U_0∩U_j) ⊆ U_2U_j = X_j for j = 1, 3, 4.

**Step 4: G ∖ X_0 = Y_1 ⊔ Y_3 ⊔ Y_4.**
- By Step 3, X_0 ∩ Y_j = ∅ for each j.
- By Step 2, |Y_1 ⊔ Y_3 ⊔ Y_4| = 3|G|/4 = |G ∖ X_0|.

**Step 5: the coset g_0U_0.**
- **Location.** By (R1), D_0 = U_2g_0U_0 ⊆ G ∖ X_0. By (R2), |D_0| = s_0 |G|/4 with s_0 ∈ {1, 2, 3}, and d_0 = s_0 r_0.
- **D_0 meets some Y_j.** By Step 4, D_0 ⊆ Y_1 ⊔ Y_3 ⊔ Y_4, so D_0 meets some Y_j with j ∈ {1, 3, 4}.
- **Gcd condition.** By Step 1, Y_j = D_j. So (R5) gives gcd(s_0 r_0, r_j) ≥ 2. Since gcd(r_0, r_j) = 1, this says gcd(s_0, r_j) ≥ 2.
  - For j = 3, 4 the number r_j is coprime to 6, so gcd(s_0, r_j) = 1 for s_0 ∈ {1, 2, 3}. This is impossible.
  - Hence D_0 does not meet Y_3 or Y_4, and therefore D_0 ⊆ Y_1.
- **Contradiction.**
  - For j = 1 we need gcd(s_0, r_1) ≥ 2. As r_1 is even and 3 ∤ r_1, this forces s_0 = 2.
  - But then |D_0| = |G|/2 > |Y_1| = |G|/4, contradicting D_0 ⊆ Y_1.

So no configuration has pattern S-D. ∎

## Dependency list

**[PUB] (published):**
- L0.2 and L0.4 (M-S Lemmas 3.2(3) and 3.4(1)).
- L0.5 (mirror of M-S Lemma 3.4(2)).
- L0.6 (Sun 2006 Lemma 2.1; M-S Lemma 2.2).
- L0.7: Sun's statement for k ≤ 4 (Sun 2006 for k = 2; Zhu 2008 Theorem 1.1 for k = 3, 4).
- M-S Props 4.2, 4.3, 4.5, used in R1 only.

**[NEW] (written in rules-v1.md / this file, unreviewed):**
- L1 (T), L2 (links), L3 (K), L4 (P).
- L5 (N2): used by 5 certificates.
- L6 (F) with L7-H2: used by 22 certificates.
- L8 (M1, M2): evaluating at τ_min and at representative r values suffices.
- Lemma R, used for S-D.
- M-S Lemma 3.7 (H1) is implemented, but no certificate in run1 uses it (FH1 count 0).

**Computer part:**
- An exact, deterministic enumeration of the 21,150 patterns, with one certificate per pattern.
- Every certificate was re-verified by an independent re-check function in the same run (C4: 21,149 re-checks, 0 failures).
- The parent should re-implement the enumeration and the certificate checks independently.

## Verification boundary

- **Written:** R0, R1, L0–L8, N2 and Lemma R are hand proofs. All new parts are unreviewed.
- **Finite exact:** pattern enumeration and certificates in engine-v1-run1, Python 3.14.3, run on 2026-10-18 at 09:37 PDT.
- **Sanity controls (not evidence):** C1–C3 in `evidence/engine-v1-run1/controls.json`.
- **Not done:** parent re-derivation, hostile reviews by both CLI families, post-result priority audit, Lean.
