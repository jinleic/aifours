# proof-v2: candidate proof of Sun's disjoint-coset conjecture for k = 5 (supersedes proof-v1)

- **Lane:** `mathematics/evidence/six-lane-20261016/sun-coset5`.
- **Written:** 2026-10-18; last edited at or before 09:57 PDT by the host clock. The freeze time and sha256 are in `evidence/proof-v2.sha256`.
- **Status:** CANDIDATE. Computer-assisted, not Lean-checked. Not claimed as correct or as passing the gate.
- **Predecessor:** `proof-v1.md` (e35bfa0e…c698) stays frozen and unchanged.

## Fix map from proof-v1 to proof-v2

The changes come from the Codex written-math review, `R/sun-coset5-written-proof-codex-v1` (84b3dadd…2002). It returned ACCEPT-WITH-FIXES with three MINOR findings and no FATAL or MAJOR ones.

| proof-v1 | proof-v2 | reason |
|---|---|---|
| (R5) derived from (R4) on the whole set S_C | (R5) applies the k = 2 statement (L0.6) **directly to the two pieces of j and k** in one right coset | (R4) on S_C gives only *some* pair, not the pair {j, k} (Codex MINOR 1) |
| (R4) listed as used | (R4) kept but marked "not used" | Steps 2 and 5 use only (R5) |
| "rules-v1 L0–L8" | rules-v1 together with `rules-v1-erratum-v1.md` | the Cor 3.11 commentary and the C4 wording are corrected there (Codex MINORs 2 and 3); the formal rules and the code are unchanged |

Nothing else changes. The engine, the certificates and the S-D refutation steps are identical to v1 apart from these citations.

## Theorem

Let G be any group. Let a_1G_1, …, a_5G_5 be pairwise disjoint left cosets of subgroups of finite index. Then gcd([G:G_i], [G:G_j]) ≥ 5 for some i < j.

## Proof structure

1. **R0** (README §2): G may be taken finite.
2. **R1** (README §2; the arrow labels are corrected in `README-addendum-v2.md`): it suffices to prove **Core(5)**.
   - Core(5) says no finite group has subgroups U_1, …, U_5 with [G:U_i] = 4r_i, the r_i pairwise coprime, and pairwise disjoint cosets g_iU_i.
   - R1 uses M-S Props 4.2, 4.3 and 4.5 (Beitr. Algebra Geom. 60 (2019)). Zhu Theorems 2.2 and 3.1 give Props 4.2 and 4.3 independently.
3. **Minimal counterexample.** Suppose Core(5) fails. Choose a counterexample with |G| minimal among finite groups that contain five pairwise disjoint cosets with all pairwise index-gcds ≤ 4.
   - Every proper subgroup then satisfies Sun's statement for k = 5.
   - Sun's statement for k ≤ 4 holds in every group (Sun 2006 for k = 2; Zhu Theorem 1.1 for k = 3, 4).
4. **The pattern.** Define α_ij = [G : U_i∩U_j]/(4r_ir_j) ∈ {1, 2, 3}. Let E2 be the vertex with r even and E3 the vertex with 3 | r, if they exist.
   - After relabelling, (α, E2, E3) is one of the 21,150 patterns enumerated by the frozen program `code/core5_engine_v1.py` (65ce5a00…2eb1).
5. **Frozen run** (`evidence/engine-v1-run1/`).
   - Every pattern except one has a certificate naming a lemma of `rules-v1.md` and its witness. Counts: T 20,465; K 637; P-Bonferroni 20; N2 5; F with H2 22.
   - Evaluating at τ_min and at representative r is justified by L8 (M1, M2).
   - **The survivor is S-D:**
     - α01 = α02 = 1, α03 = α04 = 2, and α12 = α13 = α14 = α23 = α24 = α34 = 3;
     - E2 = 1, so r_1 is even and 3 ∤ r_1;
     - E3 = 0, so 3 | r_0 and r_0 is odd;
     - r_2, r_3, r_4 are coprime to 6.
   - **Second implementation:** `code/core5_check_v2.py` (9e4aac2a…48ae2) is written independently with symbolic formulas and no symmetry reduction. It also implements the S-D argument as rule RSD. Over all 2,125,764 labelled patterns it finds **0 survivors** (`evidence/check-v2-run1/summary.json`). The 60 patterns killed by RSD form exactly the S5-orbit of S-D (stabiliser {id, (3 4)}).
6. S-D is refuted below by Lemma R, so no counterexample exists. ∎

## Lemma R: right-coset fibres over a vertex subgroup [NEW]

**Setting.** A harmonic configuration (rules-v1 §0). Fix a vertex v and translate so that g_v = 1. For j ≠ v put D_j = U_v g_j U_j, a (U_v, U_j)-double coset, and d_j = |D_j| / |U_j|.

- **(R1)** D_j ∩ U_vU_j = ∅.
- **(R2)** |D_j| is a positive multiple of |G| / gcd(n_v, n_j).
- **(R3)** Every right coset U_vy ⊆ D_j meets g_jU_j. For w ∈ g_jU_j ∩ U_vy:
  - g_jU_j ∩ U_vy = (U_v ∩ wU_jw⁻¹)w;
  - [U_v : U_v ∩ wU_jw⁻¹] = d_j.
- **(R4)** (Not used below.) Let C be a right U_v-coset and S_C = {j : C ⊆ D_j}. If |S_C| = s ≥ 2, then gcd(d_j, d_k) ≥ s for some j ≠ k in S_C.
- **(R5)** If j ≠ k and D_j ∩ D_k ≠ ∅, then gcd(d_j, d_k) ≥ 2.

**Proof.**
- **(R1)** By L0.2, g_j ∉ U_vU_j. The set U_vU_j is the double coset of 1, and distinct double coset classes are disjoint.
- **(R2)** This is L0.4.
- **(R3)**
  - Write y = c g_j u with c ∈ U_v and u ∈ U_j. Then U_vy = U_v g_j u contains g_ju ∈ g_jU_j.
  - For w ∈ g_jU_j ∩ U_vy we have g_jU_j = wU_j and U_vy = U_vw. So x ∈ wU_j ∩ U_vw ⟺ xw⁻¹ ∈ wU_jw⁻¹ ∩ U_v.
  - [U_v : U_v ∩ wU_jw⁻¹] = |U_v · wU_jw⁻¹| / |U_j| = |U_vwU_j| / |U_j| = d_j, because w ∈ D_j.
- **(R4)**
  - Fix w_0 ∈ C. Right-multiplying the pieces by w_0⁻¹ gives pairwise disjoint right cosets A_jc_j in U_v, with [U_v : A_j] = d_j and c_j ∈ U_v.
  - Inversion turns them into the disjoint left cosets c_j⁻¹A_j.
  - Apply Sun's statement for k = s in U_v: L0.6 for s = 2, Zhu for s = 3, 4. Note s ≤ 4.
- **(R5)**
  - D_j ∩ D_k is left U_v-invariant and non-empty, so it contains a whole right coset C = U_vy.
  - By (R3), the pieces P_j = g_jU_j ∩ C and P_k = g_kU_k ∩ C are non-empty. They are right cosets (U_v ∩ w_jU_jw_j⁻¹)w_j and (U_v ∩ w_kU_kw_k⁻¹)w_k, with indices d_j and d_k in U_v.
  - P_j and P_k are disjoint, because g_jU_j ∩ g_kU_k = ∅.
  - Right-multiply both by w_j⁻¹. This gives the subgroup A = U_v ∩ w_jU_jw_j⁻¹ and the right coset B c of B = U_v ∩ w_kU_kw_k⁻¹, where c = w_kw_j⁻¹ ∈ U_v. These are disjoint subsets of U_v.
  - If gcd(d_j, d_k) = 1, then by L0.6 in U_v, BA = U_v. So c ∈ BA, i.e. c = ba with b ∈ B and a ∈ A. Then b⁻¹c = a ∈ A ∩ Bc, contradicting disjointness. Hence gcd(d_j, d_k) ≥ 2. ∎

**Core(5) form.** By (R2), |D_j| = s_j |G|/4 with s_j a positive integer. By (R1), s_j ≤ 4 − α_vj. Then d_j = s_j r_j.

## Refutation of S-D

This is the same argument as proof-v1, with every overlap step citing the corrected (R5).

Take v = 2, translate so that g_2 = 1, and put X_j = U_2U_j for j ∈ {0, 1, 3, 4}.

**Step 1: the D_j for j ∈ {1, 3, 4}.**
- |X_0| = |G|/4 and |X_1| = |X_3| = |X_4| = 3|G|/4 (L0.3).
- For j ∈ {1, 3, 4} put Y_j = G ∖ X_j, so |Y_j| = |G|/4.
- By (R1) and (R2), D_j ⊆ Y_j and |D_j| is a positive multiple of |G|/4. Hence D_j = Y_j and d_j = r_j.

**Step 2: Y_1, Y_3, Y_4 are pairwise disjoint.** If Y_j ∩ Y_k ≠ ∅, then (R5) gives gcd(r_j, r_k) ≥ 2. That is impossible, since the r's are pairwise coprime.

**Step 3: X_0 ⊆ X_1 ∩ X_3 ∩ X_4.**
- τ_012 = 1, by (T2): τ ≤ α01α02 = 1.
- τ_023 = 2: (T1) gives 2 | r_2τ with r_2 odd, and (T2) gives τ ≤ α02α03 = 2. Likewise τ_024 = 2.
- By (T3) with apex 2: |U_2(U_0∩U_j)| = τ_02j |G| / (4α_0j) = |G|/4 = |X_0| for j = 1, 3, 4.
- Hence X_0 = U_2(U_0∩U_j) ⊆ X_j.

**Step 4: G ∖ X_0 = Y_1 ⊔ Y_3 ⊔ Y_4.** By Step 3, X_0 ∩ Y_j = ∅ for each j. By Step 2, |Y_1 ⊔ Y_3 ⊔ Y_4| = 3|G|/4 = |G ∖ X_0|.

**Step 5: the coset g_0U_0.**
- **Location.** D_0 ⊆ G ∖ X_0 by (R1). Also |D_0| = s_0 |G|/4 with s_0 ∈ {1, 2, 3}, and d_0 = s_0r_0.
- **D_0 meets some Y_j.** By Step 4, D_0 meets some Y_j = D_j with j ∈ {1, 3, 4}.
- **Gcd condition.** (R5) gives gcd(s_0r_0, r_j) ≥ 2, that is, gcd(s_0, r_j) ≥ 2.
  - For j = 3, 4 this is impossible, since r_j is coprime to 6 and s_0 ∈ {1, 2, 3}.
  - So D_0 ⊆ Y_1.
- **Contradiction.** For j = 1 the condition forces s_0 = 2, because r_1 is even and 3 ∤ r_1. Then |D_0| = |G|/2 > |Y_1| = |G|/4, contradicting D_0 ⊆ Y_1.

So pattern S-D cannot occur. ∎

## Dependencies

**[PUB]:**
- L0.2 and L0.4 (M-S Lemmas 3.2(3) and 3.4(1)).
- L0.5 (M-S Lemma 3.4(2), mirrored).
- L0.6 (Sun 2006 Lemma 2.1; M-S Lemma 2.2).
- L0.7 (Sun 2006 for k = 2; Zhu Theorem 1.1 for k = 3, 4).
- M-S Props 4.2, 4.3 and 4.5, used only in R1.

**[NEW]** (rules-v1 together with erratum-v1, and this file):
- L1 to L4 (the τ-calculus, links, Lemma K, the vertex count P).
- L5 (N2).
- L6 (F) and L7-H2.
- L8 (M1 and M2).
- Lemma R.

M-S Lemma 3.7 (H1) is implemented in the engine, but no certificate uses it.

**Verification boundary:**
- *Written:* R0, R1, L0–L8, N2 and Lemma R.
- *Finite exact:* `engine-v1-run1` (canonical patterns) and `check-v2-run1` (all labelled patterns, independent code).
- *Sanity only:* controls C1–C3 and controls-v2.
- *Pending:* parent finite audit, Claude written review, post-result priority audit. No Lean.
