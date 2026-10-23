# proof-v3: a public written proof of Sun's disjoint-coset conjecture for k = 5 (supersedes proof-v2)

- **Lane:** `mathematics/evidence/six-lane-20261016/sun-coset5`.
- **Freeze record:** the host-clock time and sha256 are in `evidence/proof-v3.sha256`.
- **Status:** CANDIDATE. The proof is computer-assisted and not Lean-checked. It is not claimed as correct, and the gate is not claimed.
- **Priority:** Sun reports an **unpublished** confirmation of k = 5 by Zhu Gong (2009/2010). The sources are MathOverflow Q316709 (2018-12-02) and the slides Cover-Z+G.pdf (2024), slide 38; the parent record is S/math-1-sun-coset5-post-candidate-priority-v1.md (1d7043ae…7b84). No public text of that work was found.
  - This file is therefore a public written proof of a case for which there is a prior unpublished claim.
  - It is not a "first" proof, and novelty is not claimed.
- **Predecessors:** proof-v1 (e35bfa0e…c698) and proof-v2 (8eeb7976…c5ab) remain frozen and unchanged.

## Fix map from proof-v2 to proof-v3

Sources:
- Claude written-math review `R/sun-coset5-written-proof-claude-v1.note.md`, with findings F-1 to F-10;
- Codex engine/bridge audit `R/sun-core5-engine-codex-v1.note.md` (d87212a9…b3d1).

F-1 (the (R5) repair), F-5 (the M-S Lemma 4.4 "misprint" was a text-extraction artefact) and F-6 (the R1 direction labels) were already fixed in proof-v2, erratum-v1 E3/E4 and README-addendum-v2 §1. They are carried over unchanged.

| item | change in proof-v3 |
|---|---|
| F-2 (load-bearing) | R1 no longer imports M-S Prop 4.5. §2 gives a complete written proof of Prop 4.5 that patches M-S Lemma 4.4's use of Lemma 3.10a outside its hypotheses. It now reads: T = 4r_1r_2r_3τ, 12r_2r_3 \| T so 3 \| r_1τ, and τ ≤ 2 from \|U_2(U_1∩U_3)\| = τ\|G\|/4 ≤ \|G\|/2, hence 3 \| r_1. |
| F-3 | Added in §3: "R1(⇒) holds group by group, so the minimal G over the full target carries a Core(5) configuration." |
| F-4 | §4 states the FH2 certificate semantics exactly. It records that engine v1 and check v2 implement exactly these semantics, and that every FH2 certificate exhausts **both** H2 alternatives for the **same** (a,b); none covers only one case. |
| F-7 | Zhu is cited as Theorem 1.1 (k = 3, 4). Props 4.2 and 4.3 are immediate from it. |
| F-8 | In the Prop 4.5 proof, only "multiple of \|G\|/4" is used for \|U_2U_3 ∩ U_2U_4\|, since gcd(4r_2, 12r_3r_4) = 4 when 3 ∤ r_2. |
| F-9 | "Harmonic" means: there exist g_i such that the cosets g_iU_i are pairwise disjoint. The subgroups need not be distinct. This is the meaning fixed by the Prop 4.5 proof below, which is self-contained here. |
| F-10 | The double-coset multiplicity in Lemma R is renamed q_j, avoiding a clash with s = \|S_C\|. The remark on gcd(α, r_z) is restricted to α ∈ {2,3}. R0 now justifies that the cores have finite index. |
| Codex MAJOR (wording) | C4 is a **shared-code witness recheck**: it reuses the engine helpers and does not reopen the certificate file. It is not independent verification. `core5_check_v2.py` is **lane evidence**, not a replay independent of the parent. |
| Codex MINOR | Controls record observations only; they **do not gate** the run. The C4 mutations are restated as *selected* intended-reason demonstrations (controls-v2/v3 part A). The targeted demos named "K_star_1111" and "P_star_3333" in engine-v1-run1 actually fired T and K respectively; that is their correct label. |

## Theorem

Let G be any group. Let a_1G_1, …, a_5G_5 be pairwise disjoint left cosets of subgroups of finite index. Then gcd([G:G_i], [G:G_j]) ≥ 5 for some i < j.

## 1. R0: reduction to finite groups

core_G(G_i) is the kernel of the action of G on G/G_i, so its index is at most [G:G_i]!. Hence N = ∩_i core_G(G_i) is a normal subgroup of finite index contained in every G_i.

Each coset a_iG_i is the full preimage of its image in G/N. So indices, intersection indices and disjointness all pass to the finite group G/N.

## 2. R1: reduction to Core(5), with a self-contained proof of M-S Prop 4.5

**Core(5)** says: no finite group G has subgroups U_1, …, U_5 with [G:U_i] = 4r_i, the r_i pairwise coprime, and pairwise disjoint cosets g_iU_i.

**(Sun(5) ⇒ Core(5)).** A Core(5) configuration has every pairwise gcd equal to 4 < 5.

**(Core(5) ⇒ Sun(5)), group by group.** Let n_i = [G:G_i], and assume five disjoint cosets in G have all pairwise gcds ≤ 4.

1. **Each gcd is 2, 3 or 4.** By L0.2 and L0.6 no gcd equals 1, so each lies in {2, 3, 4}.
2. **All divisible by 3, or all even.** If some n_i is odd, every gcd with it is odd and so equals 3. Then 3 divides all five indices.
3. **All divisible by 3.** Every gcd is then 3 < 4. Any four of the cosets contradict Zhu Theorem 1.1 at k = 4.
4. **All even.** Write n_i = 2^{e_i}m_i with m_i odd. Then the m_i are pairwise coprime, every e_i ≥ 1, and at most one e_i ≥ 3.
   - **Two indices with e = 1.** With any third index they have all pairwise gcds equal to 2 < 3, contradicting Zhu Theorem 1.1 at k = 3.
   - **Exactly one index with e = 1.** We get (2r_1, 4r_2, 4r_3, 4r_4) with r_1 odd and the r's pairwise coprime. This is excluded by Proposition 4.5 below.
   - **Otherwise.** n_i = 4r_i with r_i = 2^{e_i−2}m_i pairwise coprime: a Core(5) configuration *in the same group G* with the same subgroups.

**Proposition 4.5 (M-S, Beitr. Algebra Geom. 60 (2019); proof patched per F-2 and F-8).**

*Statement.* Let r_1, …, r_4 be pairwise coprime with r_1 odd. Then no group has subgroups with indices [G:U_1] = 2r_1 and [G:U_i] = 4r_i (i = 2, 3, 4) and pairwise disjoint cosets g_iU_i.

*Proof.* By R0 we may take G finite. All sizes below are in units of |G|, and α(i,j) := [G:U_i∩U_j] / lcm(n_i, n_j).

- **(a) α(1,i) = 1 and |U_1U_i| = 1/2 for i ≥ 2.** gcd(2r_1, 4r_i) = 2, so α ≤ 1 by L0.3.
- **(b) α(i,j) ≠ 2 for i, j ≥ 2.** Suppose α(2,3) = 2, so [G:U_2∩U_3] = 8r_2r_3.
  - T = [G:U_1∩U_2∩U_3] is divisible by 2r_1 and by 8r_2r_3, hence by 8r_1r_2r_3.
  - So |U_1(U_2∩U_3)| = T/(2r_1·8r_2r_3) ≥ 1/2 = |U_1U_2| = |U_1U_3|. Hence U_1U_2 = U_1(U_2∩U_3) = U_1U_3.
  - Apply Lemma K (rules-v1 L3) at vertex 2 with S = {1, 3}. The pair condition U_1U_2 ⊆ U_1U_3 holds. So we would need |U_1U_2| + |U_3U_2| < 1, but the sum is 1/2 + 1/2 = 1. Contradiction.
- **(c) If α(2,3) = 3, then 3 | r_1 and |U_2U_1 ∩ U_2U_3| = 1/4. (F-2 patch.)**
  - T = [G:U_1∩U_2∩U_3] is divisible by lcm(2r_1, 4r_2, 4r_3) = 4r_1r_2r_3. Write T = 4r_1r_2r_3τ.
  - [G:U_2∩U_3] = 12r_2r_3 divides T, so 3 | r_1τ.
  - [G:U_1∩U_3] = 4r_1r_3 by (a). So |U_2(U_1∩U_3)| = T / (4r_2·4r_1r_3) = τ/4 ≤ |U_2U_1| = 1/2. Hence τ ≤ 2, so 3 ∤ τ, and therefore 3 | r_1.
  - U_2U_1 ∩ U_2U_3 contains U_2(U_1∩U_3), so its size is ≥ τ/4 ≥ 1/4. By L0.5 and L0.4 it is a union of (U_2, U_1∩U_3)-double cosets, each of size a multiple of 1/gcd(4r_2, 4r_1r_3) = 1/4.
  - Its size is not 1/2 = |U_2U_1|. Otherwise U_2U_1 ⊆ U_2U_3, and Lemma K at vertex 1 with S = {2, 3} would give |U_2U_1| + |U_3U_1| = 1, a contradiction. Hence the size is exactly 1/4.
- **(d) Not all of α(2,3), α(2,4), α(3,4) equal 1.** Suppose they all do.
  - The triangle {2, 3, 4} has τ ≤ 1 (rules-v1 T2), so τ = 1. Then |U_2(U_4∩U_3)| = 1/4 = |U_2U_4|, which gives U_2U_4 ⊆ U_2U_3.
  - In the triangle {1, 2, 4}, T is a multiple of 4r_1r_2r_4. So |U_1(U_4∩U_2)| = T/(2r_1·4r_2r_4) ≥ 1/2 = |U_1U_4|, which gives U_1U_4 ⊆ U_1U_2. Likewise U_1U_4 ⊆ U_1U_3.
  - So every pair in S = {1, 2, 3} satisfies the pair condition of Lemma K at vertex 4, in the form "U_iU_4 ⊆ U_iU_j".
  - Lemma K then requires 1/2 + 1/4 + 1/4 < 1, which fails.
- **(e) Choosing labels.** By (b) and (d), some α(i,j) with i, j ≥ 2 equals 3; relabel so that α(2,3) = 3. By (c), 3 | r_1.
  - α(2,4) and α(3,4) cannot both be 1. Otherwise the triangle {2, 3, 4} has τ ≤ α(2,4)α(3,4) = 1, and then 12r_2r_3 | 4r_2r_3r_4 gives 3 | r_4. That contradicts 3 | r_1.
  - So, after swapping 2 and 3 if necessary, α(2,4) = 3.
- **(f) α(3,4) = 3.** Suppose α(3,4) = 1.
  - In the triangle {2, 3, 4}, write T = 4r_2r_3r_4τ. Then 12r_2r_3 | T and 12r_2r_4 | T. Since 3 ∤ r_3r_4 (because 3 | r_1), we get 3 | τ.
  - So |U_3(U_2∩U_4)| = τ/(4·3) ≥ 1/4 = |U_3U_4|, which gives U_3U_4 ⊆ U_3U_2.
  - Lemma K at vertex 4 with S = {2, 3} then requires 3/4 + 1/4 < 1, which fails.
- **(g) Final count.** Now α(1,i) = 1, α(i,j) = 3 for all i, j ∈ {2, 3, 4}, and 3 | r_1.
  - By (c), applied to the pairs (2,3) and (2,4): |U_2U_1 ∪ U_2U_j| = 1/2 + 3/4 − 1/4 = 1 for j = 3, 4.
  - |U_2U_3 ∩ U_2U_4| is a multiple of 1/gcd(4r_2, 12r_3r_4) = 1/4, using 3 ∤ r_2. This is F-8: only the multiple of 1/4 is used.
  - That size is at least 3/4 + 3/4 − 1 = 1/2. It is not 3/4: otherwise U_2U_3 = U_2U_4, and Lemma K at vertex 3 with S = {2, 4} would give 3/4 + 3/4 < 1. So the size is 1/2, and U_2U_3 ∪ U_2U_4 = G.
  - By M-S Lemma 3.1, applied with R = U_2U_1, S = U_2U_3, T = U_2U_4 (all pairwise unions are G):
    |R ∩ S ∩ T| = |R| − |G∖S| − |G∖T| = 1/2 − 1/4 − 1/4 = 0.
  - But U_2 ⊆ R ∩ S ∩ T, a contradiction. ∎

  *Proof of M-S Lemma 3.1 as used.* G∖S and G∖T are disjoint subsets of R, so R ∩ S ∩ T = R ∖ ((G∖S) ⊔ (G∖T)).

**F-3.** R1(⇒) holds group by group. So the minimal-order G over the full target carries a Core(5) configuration.

## 3. Minimal counterexample

Suppose Sun(5) fails. Let G have minimal order among finite groups containing five pairwise disjoint cosets with all pairwise index-gcds ≤ 4. By §2 (F-3), G carries a Core(5) configuration.

Every proper subgroup of G satisfies Sun(5). Every group satisfies Sun(k) for k ≤ 4: Sun 2006 for k = 2, and Zhu Theorem 1.1 for k = 3, 4.

## 4. Patterns and certificates

**Patterns.** Put α_ij = [G:U_i∩U_j]/(4r_ir_j) ∈ {1, 2, 3}. Let E2 be the vertex whose r is even and E3 the vertex whose r is divisible by 3, if they exist. Up to relabelling, (α, E2, E3) is one of 21,150 orbits. The count is confirmed by Burnside's lemma in the Claude review §1.

**Certificates.** The frozen program `code/core5_engine_v1.py` (65ce5a00…2eb1) gives, in `evidence/engine-v1-run1/certificates.tsv.gz` (1c7e8008…be85), one certificate for every orbit except S-D. The meaning of each certificate type (Claude review §3) is as follows. Sizes are in units of |G|, and everything is recomputed from (α, E2, E3) alone.

- **T(a,b,c).**
  - τ_min = lcm over the edges of α_e/γ_e, where γ_e = α_e if (α_e = 2 and the opposite vertex is E2) or (α_e = 3 and the opposite vertex is E3), and γ_e = 1 otherwise.
  - τ_max is the minimum over the three vertices of the product of the two α's at that vertex.
  - The certificate requires τ_min > τ_max.
- **K(v,S).**
  - For every pair {i,j} ⊆ S, τ_min(v,i,j) = α_viα_vj.
  - Σ_{i∈S} α_iv ≥ 4.
- **PB / P-pair(v, ·).** Here x_j = α_vj/4 and u = 1/(4γ) with γ = gcd(r_v, α_jk), read off from E2/E3.
  - hi = the largest multiple of u that is ≤ min(x_j, x_k), lowered by u when the containment that equality would force is barred by K2.
  - PB: Σ_S(1 − x_j) − Σ_{pairs ⊆ S}(1 − x_j − x_k + hi_jk) ≥ 1.
  - P-pair: ⌈max(τ_min(v,j,k)/(4α_jk), x_j + x_k − 1)⌉_u > hi.
  - In run1 every P certificate is PB; the P-pair count is 0.
- **N2.** All ten α equal 2. The proof is rules-v1 L5.
- **FH2(a,b) (F-4).** Requires α_ab = 1 and V2 ≠ ∅, where V2 = {v : α_va = α_vb = 2}. Both cases below are examined for the same (a,b):
  - **case (i):** m = 4, t_a = t_b = 1, and t_v = 2 for v ∈ V2;
  - **case (ii):** m = 2, and t = 1 on {a, b} ∪ V2.

  In each case:
  - all other t_l range over 1..m;
  - every met-coset set M_l with |M_l| = t_l is enumerated;
  - the only symmetry used is fixing a's coset to label 0;
  - λ_l = 4r_lt_l/m, evaluated with dominating representatives (rules-v1 L8, M2);
  - an assignment is rejected iff (F3) fails at some vertex with t = 1, or some coset with s ≥ 2 met cosets has all pairwise gcds < s;
  - no coverage or balance constraint is imposed.

  The certificate requires every assignment to be rejected **in both cases**. `rule_FH2` in engine v1 and `r_FH2` in check v2 implement exactly this: each returns a kill only if `fibre_search(4, …)` and `fibre_search(2, …)` both find no admissible assignment for the same (x, y). A one-case FH2 certificate cannot arise from either program. Each of the 22 engine FH2 records lists the counts examined in both cases (the Codex audit reports 864 and 16 per record).

**Verification status of the certificates.**
- C4 in engine-v1-run1 is a shared-code witness recheck. It reuses the engine's τ/link/p_bounds/N2/fibre helpers and does not reopen the certificate file. It is not independent verification.
- `code/core5_check_v2.py` (9e4aac2a…48ae2) finds 0 survivors among all 2,125,764 labelled patterns. It is lane evidence, not a replay independent of the parent. It is written separately (symbolic, without symmetry reduction) but by the same author and from the same rules.
- Controls C1–C3 and controls-v2/v3 record observations only and do not gate anything.
- The parent's replay desk is the independent check of the finite part.

## 5. Lemma R and the refutation of S-D

S-D is the pattern:
- α01 = α02 = 1, α03 = α04 = 2, and the other six α equal 3;
- E2 = 1, E3 = 0, and r_2, r_3, r_4 coprime to 6.

**Lemma R (right-coset fibres over a vertex subgroup) [NEW].**

*Setting.* Fix a vertex v and normalise g_v = 1. For j ≠ v put D_j = U_vg_jU_j and d_j = |D_j|/|U_j|. In Core(5), |D_j| = q_j|G|/4 with q_j a positive integer, so d_j = q_jr_j.

*Statements.*
- **(R1)** D_j ∩ U_vU_j = ∅.
- **(R2)** |D_j| is a positive multiple of |G|/gcd(n_v, n_j). In Core(5), 1 ≤ q_j ≤ 4 − α_vj.
- **(R3)** Every right coset U_vy ⊆ D_j meets g_jU_j. The piece g_jU_j ∩ U_vy is a right coset of a subgroup of index d_j in U_v.
- **(R5)** If j ≠ k and D_j ∩ D_k ≠ ∅, then gcd(d_j, d_k) ≥ 2.

*Proofs.* As in proof-v2. (R5) applies the k = 2 case directly to the two pieces of j and k inside one right coset C ⊆ D_j ∩ D_k (F-1).

**Refutation of S-D.** Take v = 2 and the sets X_j = U_2U_j.

1. For j ∈ {1, 3, 4}, Y_j = G ∖ X_j has size |G|/4. Hence D_j = Y_j, q_j = 1 and d_j = r_j.
2. The sets Y_1, Y_3, Y_4 are pairwise disjoint, by (R5) and coprimality of the r_j.
3. τ_012 = 1 and τ_023 = τ_024 = 2. So by (T3), X_0 ⊆ X_1 ∩ X_3 ∩ X_4.
4. Therefore G ∖ X_0 = Y_1 ⊔ Y_3 ⊔ Y_4.
5. D_0 ⊆ G ∖ X_0, with d_0 = q_0r_0 and q_0 ∈ {1, 2, 3}. So D_0 meets some Y_j, and (R5) gives gcd(q_0, r_j) ≥ 2.
   - This is impossible for j = 3, 4.
   - So D_0 ⊆ Y_1, which forces q_0 = 1 by size. But then gcd(1, r_1) = 1, a contradiction. (proof-v2's route through q_0 = 2 is also valid.) ∎

## 6. Dependencies and boundary

**Published, imported as statements:**
- Zhu Theorem 1.1 (k = 3, 4).
- Sun's statement for k = 2, re-proved here as L0.2 + L0.6.
- M-S Lemma 3.1 (re-proved inline above) and M-S Lemma 3.4 (rules-v1 L0.4, L0.5).

M-S Prop 4.5 is no longer imported; it is proved in §2.

**New, written:**
- rules-v1 L1–L8, with errata v1 and v2.
- N2.
- F with H2.
- Lemma R.
- The proof of Prop 4.5 in §2.

**Finite exact:** engine-v1-run1 (canonical orbits) and check-v2-run1 (all labelled patterns, lane evidence).

**Pending:** the parent's independent replay of the 21,150 certificates. No Lean.

**Priority:** a prior unpublished claim exists (Zhu Gong, as reported by Sun). This work is a public written proof of that case.
