# proof-v4: a locally written candidate proof of Sun's disjoint-coset conjecture for k = 5, a case already claimed by Z. Gong (supersedes proof-v3)

- **Lane:** `mathematics/evidence/six-lane-20261016/sun-coset5`.
- **Freeze record:** the host-clock time and sha256 are in `evidence/proof-v4.sha256`.
- **Status:** LOCALLY WRITTEN CANDIDATE PROOF.
  - It is computer-assisted and not Lean-checked.
  - The gate is not claimed.
  - This run has published nothing.
- **Priority.** Z.-W. Sun reports that **Z. Gong** confirmed the case k = 5 for general groups, in 2009/2010.
  - Sources: MathOverflow Q316709 (2018-12-02); the slides Cover-Z+G.pdf (2024), slide 38. The parent record is S/math-1-sun-coset5-post-candidate-priority-v1.md (1d7043ae…7b84).
  - No public proof of that work was located. That is a search miss. It is no evidence about whether the work was refereed, and no novelty claim is made.
- **Meaning of [NEW].** "[NEW]" means only "written in this lane". It is not a novelty claim.
- **Predecessors:** proof-v1 (e35bfa0e…c698), proof-v2 (8eeb7976…c5ab) and proof-v3 (0e279a76…7781) remain frozen and unchanged. The code and the certificates are unchanged.

## Fix map from proof-v3 to proof-v4

Sources:
- Claude delta review `R/sun-coset5-proof-v3-delta-claude-v1.note.md`, findings m1–m10;
- Codex delta review `R/sun-coset5-proof-v3-delta-codex-v1.note.md` (db3aacf9…a1e9);
- the parent's instruction of 2026-10-18.

The mathematics of proof-v3 §2 passed both reviews. proof-v4 restores text that v3 had abbreviated, and corrects labels and wording. No mathematical step changes.

| item | change |
|---|---|
| m1 | §2(b), §2(d) and every Lemma K step now write out the inversion that yields L3's pair condition, and give the K2 tuple (v, j, k) where K2 applies. |
| m2 | §5 again contains the full proofs of (R1)–(R3) from proof-v1, and the repaired (R5′): two named pieces, right-translated into U_v, then inverted, then k = 2. (R4) is deleted, since it is unused. The phrase "as in proof-v2" is gone. |
| m3 | §5's setting states explicitly that g_1U_1, …, g_5U_5 are pairwise disjoint. |
| m4 | §4 again explains how a certificate implies impossibility (L8, M1, M2). §7 again contains the theorem closure. §6 restores the S-D derivations: R1/R2 forcing D_j = Y_j, (T1)/(T2) giving τ_023 = 2, the (T3) sizes, and gcd(q_0r_0, r_j) = gcd(q_0, r_j). The rename q_j and the valid q_0 = 1 route are kept. |
| m5 | The label "R1(⇒)" becomes "the Core(5) ⇒ Sun(5) direction". The sentence fixed under F-3 sits at the end of §2, not in §3. |
| m6 | The check-v2 statements are labelled lane SELF-REPORT. §4 states exactly how check v2 classifies the 60 labelled S-D triples (killed by its rule RSD), and how this matches the parent bridge's "SURVIVE 60". |
| m7 | §4 cites the parent bridge replay PASS: verifier 2d7fff78…7659, RESULT d741396c…7278. "Gate not claimed" is kept. |
| m8 | The text now says "locally written candidate proof of a previously claimed case", glosses [NEW], writes "Z. Gong", and adds "search miss, not a novelty claim". |
| m9 | Citations: L0.3 for α ≤ 3, (b) for α ≠ 2, L0.5 + L0.4 for double-coset counts. The sets in the Lemma 3.1 step are renamed 𝒜, ℬ, 𝒞. The q_0 = 2 route is attributed to proof-v1. "Self-contained" becomes "self-contained modulo rules-v1 L0.3–L0.5 and L1–L3". The dependency list no longer contradicts itself. |
| m10 | The cumulative `rules-v1-erratum-v3.md` carries the Cor 3.11 link correction explicitly: the links are at U and V, not at W. The correction is unused. |

## Theorem

Let G be any group. Let a_1G_1, …, a_5G_5 be pairwise disjoint left cosets of subgroups of finite index. Then gcd([G:G_i], [G:G_j]) ≥ 5 for some i < j.

## 1. R0: reduction to finite groups

core_G(G_i) is the kernel of the action of G on G/G_i, so its index is at most [G:G_i]!. Hence N = ∩_i core_G(G_i) is a normal subgroup of finite index contained in every G_i.

Each coset a_iG_i is the full preimage of its image in G/N. So indices, intersection indices and disjointness all pass to the finite group G/N.

## 2. R1: reduction to Core(5), and a proof of M-S Prop 4.5

**Core(5).** No finite group G has subgroups U_1, …, U_5 with [G:U_i] = 4r_i, the r_i pairwise coprime, and pairwise disjoint cosets g_iU_i.

**The Sun(5) ⇒ Core(5) direction.** A Core(5) configuration has every pairwise gcd equal to 4 < 5.

**The Core(5) ⇒ Sun(5) direction, group by group.** Let n_i = [G:G_i], and assume five disjoint cosets in G have all pairwise gcds ≤ 4.

1. **Each gcd is 2, 3 or 4.** By L0.2 and L0.6 no gcd equals 1, so each lies in {2, 3, 4}.
2. **All divisible by 3, or all even.** If some n_i is odd, every gcd with it is odd and so equals 3. Then 3 divides all five indices.
3. **All divisible by 3.** Every gcd is then 3 < 4. Any four of the cosets contradict Zhu Theorem 1.1 at k = 4.
4. **All even.** Write n_i = 2^{e_i}m_i with m_i odd. Then the m_i are pairwise coprime, every e_i ≥ 1, and at most one e_i ≥ 3.
   - **Two indices with e = 1.** With any third index they have all pairwise gcds equal to 2 < 3, contradicting Zhu Theorem 1.1 at k = 3.
   - **Exactly one index with e = 1.** We get (2r_1, 4r_2, 4r_3, 4r_4) with r_1 odd and the r's pairwise coprime. This is excluded by Proposition 4.5 below.
   - **Otherwise.** n_i = 4r_i with r_i = 2^{e_i−2}m_i pairwise coprime: a Core(5) configuration in the same group G, with the same subgroups.

**Proposition 4.5 (M-S, Beitr. Algebra Geom. 60 (2019); proof patched per F-2 and F-8).**

*Status of this proof.* It is self-contained modulo rules-v1 L0.3–L0.5 and L1–L3. "Harmonic" means: there exist g_i such that the cosets g_iU_i are pairwise disjoint (F-9).

*Statement.* Let r_1, …, r_4 be pairwise coprime with r_1 odd. Then no group has subgroups with indices [G:U_1] = 2r_1 and [G:U_i] = 4r_i (i = 2, 3, 4) and pairwise disjoint cosets g_iU_i.

*Proof.* By R0 we may take G finite. Sizes are in units of |G|, and α(i,j) := [G:U_i∩U_j] / lcm(n_i, n_j). Lemma K (rules-v1 L3) at a vertex v with set S requires: for each pair {i, j} ⊆ S, either U_vU_i ⊆ U_jU_i or U_vU_j ⊆ U_iU_j. Its conclusion is Σ_{i∈S} |U_iU_v| < 1.

- **(a) α(1,i) = 1 and |U_1U_i| = 1/2 for i ≥ 2.** gcd(2r_1, 4r_i) = 2, since r_1 is odd and coprime to r_i. So α ≤ 1 by L0.3.
- **(b) α(i,j) ≠ 2 for i, j ≥ 2.** Suppose α(2,3) = 2, so [G:U_2∩U_3] = 8r_2r_3.
  - T = [G:U_1∩U_2∩U_3] is divisible by 2r_1 and by 8r_2r_3, hence by 8r_1r_2r_3.
  - So |U_1(U_2∩U_3)| = T/(2r_1·8r_2r_3) ≥ 1/2 = |U_1U_2| = |U_1U_3|. Hence U_1U_2 = U_1(U_2∩U_3) = U_1U_3.
  - **Inverting** gives U_2U_1 = U_3U_1. In particular U_2U_1 ⊆ U_3U_1, which is L3's first alternative at v = 2 for the pair {1, 3}. This is K2 with (v, j, k) = (1, 2, 3).
  - Lemma K at v = 2 with S = {1, 3} then requires |U_1U_2| + |U_3U_2| < 1, but the sum is 1/2 + 1/2 = 1. Contradiction.
- **(c) If α(2,3) = 3, then 3 | r_1 and |U_2U_1 ∩ U_2U_3| = 1/4.** (F-2 patch.)
  - T = [G:U_1∩U_2∩U_3] is divisible by lcm(2r_1, 4r_2, 4r_3) = 4r_1r_2r_3. Write T = 4r_1r_2r_3τ.
  - [G:U_2∩U_3] = 12r_2r_3 divides T, so 3 | r_1τ.
  - [G:U_1∩U_3] = 4r_1r_3 by (a). So |U_2(U_1∩U_3)| = T/(4r_2·4r_1r_3) = τ/4 ≤ |U_2U_1| = 1/2. Hence τ ≤ 2, so 3 ∤ τ, and therefore 3 | r_1.
  - U_2U_1 ∩ U_2U_3 contains U_2(U_1∩U_3), so its size is ≥ τ/4 ≥ 1/4. By L0.5 and L0.4 it is a union of (U_2, U_1∩U_3)-double cosets, each of size a multiple of 1/gcd(4r_2, 4r_1r_3) = 1/4.
  - Its size is not 1/2. Otherwise U_2U_1 ⊆ U_2U_3. **Inverting** gives U_1U_2 ⊆ U_3U_2, which is L3's first alternative at v = 1 for the pair {2, 3} (K2 with (v, j, k) = (2, 1, 3)). Lemma K at v = 1 with S = {2, 3} would then give |U_2U_1| + |U_3U_1| = 1, a contradiction. Hence the size is exactly 1/4.
- **(d) Not all of α(2,3), α(2,4), α(3,4) equal 1.** Suppose they all do.
  - In the triangle {2, 3, 4}, (T2) gives τ ≤ 1, so τ = 1. Then |U_2(U_4∩U_3)| = 1/4 = |U_2U_4| (T3), so U_2U_4 ⊆ U_2U_3. **Inverting** gives U_4U_2 ⊆ U_3U_2. Likewise U_4U_3 ⊆ U_2U_3.
  - In the triangle {1, 2, 4}, T is a multiple of lcm(2r_1, 4r_2, 4r_4) = 4r_1r_2r_4. So |U_1(U_4∩U_2)| = T/(2r_1·4r_2r_4) ≥ 1/2 = |U_1U_4|, giving U_1U_4 ⊆ U_1U_2. **Inverting** gives U_4U_1 ⊆ U_2U_1. Likewise U_4U_1 ⊆ U_3U_1.
  - So for every pair {i, j} ⊆ S = {1, 2, 3}, the inclusion U_4U_i ⊆ U_jU_i holds for at least one ordering of the pair. That is L3's pair condition at v = 4.
  - Lemma K requires 1/2 + 1/4 + 1/4 < 1, which fails.
- **(e) Choosing labels.** By (b) and (d), together with α ≤ 3 from L0.3, some α(i,j) with i, j ≥ 2 equals 3. Relabel so that α(2,3) = 3. By (c), 3 | r_1.
  - α(2,4) and α(3,4) cannot both be 1. Otherwise the triangle {2, 3, 4} has τ ≤ α(2,4)α(3,4) = 1, and then 12r_2r_3 | T = 4r_2r_3r_4 gives 3 | r_4. That contradicts 3 | r_1.
  - By (b) neither of them equals 2. So, after swapping 2 and 3 if necessary, α(2,4) = 3.
- **(f) α(3,4) = 3.** By (b), α(3,4) ≠ 2. Suppose α(3,4) = 1.
  - In the triangle {2, 3, 4}, write T = 4r_2r_3r_4τ. Then 12r_2r_3 | T and 12r_2r_4 | T. Since 3 ∤ r_3r_4 (because 3 | r_1), we get 3 | τ.
  - So |U_3(U_2∩U_4)| = τ/(4·3) ≥ 1/4 = |U_3U_4|, giving U_3U_4 ⊆ U_3U_2. **Inverting** gives U_4U_3 ⊆ U_2U_3, which is L3's second alternative at v = 4 for the pair {2, 3} (K2 with (v, j, k) = (3, 4, 2)).
  - Lemma K at v = 4 with S = {2, 3} requires 3/4 + 1/4 < 1, which fails.
- **(g) Final count.** Now α(1,i) = 1 and α(i,j) = 3 for all i, j ∈ {2, 3, 4}, and 3 | r_1.
  - By (c), applied to the pairs (2,3) and (2,4): |U_2U_1 ∪ U_2U_j| = 1/2 + 3/4 − 1/4 = 1 for j = 3, 4.
  - |U_2U_3 ∩ U_2U_4| is a multiple of 1/gcd(4r_2, 12r_3r_4) = 1/4 (by L0.5 + L0.4, using 3 ∤ r_2). This is F-8.
  - That size is at least 3/4 + 3/4 − 1 = 1/2. It is not 3/4: otherwise U_2U_3 = U_2U_4, and K2 with (v, j, k) = (2, 3, 4) — that is, Lemma K at v = 3 with S = {2, 4}, using the inverse U_3U_2 ⊆ U_4U_2 — would give 3/4 + 3/4 < 1. So the size is 1/2, and U_2U_3 ∪ U_2U_4 = G.
  - Put 𝒜 = U_2U_1, ℬ = U_2U_3, 𝒞 = U_2U_4. All three pairwise unions are G. So G∖ℬ and G∖𝒞 are disjoint subsets of 𝒜, and 𝒜 ∩ ℬ ∩ 𝒞 = 𝒜 ∖ ((G∖ℬ) ⊔ (G∖𝒞)) (M-S Lemma 3.1, re-proved here). Hence
    |𝒜 ∩ ℬ ∩ 𝒞| = 1/2 − 1/4 − 1/4 = 0.
  - But U_2 ⊆ 𝒜 ∩ ℬ ∩ 𝒞, a contradiction. ∎

**F-3.** The Core(5) ⇒ Sun(5) direction holds group by group. So the minimal-order G over the full target carries a Core(5) configuration.

## 3. Minimal counterexample

Suppose Sun(5) fails. Let G have minimal order among finite groups containing five pairwise disjoint cosets with all pairwise index-gcds ≤ 4. By §2, G carries a Core(5) configuration (U_i, g_i).

Every proper subgroup of G satisfies Sun(5). Every group satisfies Sun(k) for k ≤ 4: Sun 2006 Lemma 2.1 / L0.6 for k = 2, and Zhu Theorem 1.1 for k = 3, 4.

## 4. Patterns, certificates, and why a certificate implies impossibility

**Patterns.** Put α_ij = [G:U_i∩U_j]/(4r_ir_j) ∈ {1, 2, 3} (L0.3). Let E2 be the vertex whose r is even and E3 the vertex whose r is divisible by 3, if they exist. Up to relabelling, (α, E2, E3) is one of 21,150 orbits. Burnside's lemma (Claude review v1 §1) confirms the count. Every rule is S5-equivariant, so one certificate per orbit suffices.

**Certificates.** The frozen program `code/core5_engine_v1.py` (65ce5a00…2eb1) gives, in `evidence/engine-v1-run1/certificates.tsv.gz` (1c7e8008…be85), one certificate for every orbit except S-D:

| rule | orbits |
|---|---|
| T | 20,465 |
| K | 637 |
| P-Bonferroni | 20 |
| N2 | 5 |
| FH2 | 22 |

**From certificate to impossibility.** Each certificate names a lemma of `rules-v1.md` together with its witness, and that lemma shows that no Core(5) configuration with that pattern exists. The program evaluates each triangle at τ = τ_min and uses representative r's. That suffices because of rules-v1 L8:

- **(M1)** Every admissible τ is a multiple of τ_min. Every rule is upward closed in τ:
  - a T-kill means τ_min > τ_max;
  - a K1 link at τ_min forces τ = τ_min;
  - the lower bounds in (P3) increase with τ, while hi and the K2 conditions do not depend on τ;
  - F, H2 and N2 do not read the program's τ.

  So a kill at τ_min is a kill for every admissible τ.
- **(M2)** All quantities depend on r only through the E2/E3 status, except the fibre gcds. Those are maximised by the representatives 16 and 81. So a kill at the representative is a kill for every instance.

**Certificate semantics** (Claude review v1 §3; sizes in units of |G|, everything recomputed from (α, E2, E3)):

- **T(a,b,c).**
  - τ_min is the lcm over the edges of α_e/γ_e, where γ_e = α_e if (α_e = 2 and the opposite vertex is E2) or (α_e = 3 and the opposite vertex is E3), and γ_e = 1 otherwise.
  - τ_max is the minimum, over the three vertices, of the product of the two α's at that vertex.
  - The certificate requires τ_min > τ_max.
- **K(v,S).** For every pair {i,j} ⊆ S, τ_min(v,i,j) = α_viα_vj; and Σ_{i∈S} α_iv ≥ 4.
- **PB / P-pair(v, ·).**
  - x_j = α_vj/4, and u = 1/(4γ) with γ = gcd(r_v, α_jk).
  - hi is the largest multiple of u that is ≤ min(x_j, x_k). It is lowered by u when the containment that equality would force is barred by K2.
  - PB: Σ_S(1 − x_j) − Σ_{pairs}(1 − x_j − x_k + hi_jk) ≥ 1.
  - P-pair: ⌈max(τ_min(v,j,k)/(4α_jk), x_j + x_k − 1)⌉_u > hi.
  - In run1 every P certificate is PB.
- **N2.** All ten α equal 2 (rules-v1 L5).
- **FH2(a,b).** Requires α_ab = 1 and V2 = {v : α_va = α_vb = 2} ≠ ∅. Both alternatives of rules-v1 L7-H2 are refuted for the same (a,b):
  - **case (i):** m = 4, t_a = t_b = 1, and t_v = 2 for v ∈ V2;
  - **case (ii):** m = 2, and t = 1 on {a, b} ∪ V2.

  In each case:
  - all other t_l range over 1..m;
  - every met-coset set M_l with |M_l| = t_l is enumerated;
  - the only symmetry used is fixing a's coset to label 0;
  - λ_l = 4r_lt_l/m;
  - an assignment is rejected iff (F3) fails at some vertex with t = 1, or some coset with s ≥ 2 has all pairwise gcds < s;
  - no coverage or balance constraint is imposed.

  The certificate requires every assignment to be rejected in both cases. Each of the 22 records lists the counts examined in both cases, [864, 16]. The Codex engine audit and the parent bridge confirm the engine implements exactly this.

**Verification status.**
- **Parent bridge replay: PASS.** This is a parent-independent replay of the 21,150 orbits and their certificates (R/sun-core5-parent-rule-audit-v1/), with verifier 2d7fff78…7659 and RESULT d741396c…7278.
- **C4** in engine-v1-run1 is a shared-code witness recheck. It is not independent verification.
- **check v2, lane SELF-REPORT.** `code/core5_check_v2.py` (9e4aac2a…48ae2) classifies all 2,125,764 labelled (α, E2, E3) triples. It reports 0 survivors, because it also encodes rule RSD, the Lemma R argument of §6. The 60 labelled triples it kills by RSD are exactly the labelled S-D triples: the S5-orbit of S-D, whose stabiliser is {id, (3 4)}. The parent bridge has no RSD rule, so it reports these same 60 as SURVIVE 60, and all its other labelled counts equal check v2's. The two classifications therefore agree. In both, the 60 S-D triples are disposed of by the written Lemma R argument in §6.
- **Controls** record observations only; they do not gate anything.

## 5. Lemma R: right-coset fibres over a vertex subgroup [NEW]

**Setting.** G is finite. U_1, …, U_5 ≤ G have indices n_i. **Assume the cosets g_1U_1, …, g_5U_5 are pairwise disjoint (F-9).** Fix a vertex v and left-translate the whole configuration so that g_v = 1; disjointness is preserved. For j ≠ v put D_j := U_v g_j U_j, a (U_v, U_j)-double coset, and d_j := |D_j|/|U_j|.

**Statement.**
- **(R1)** D_j ∩ U_vU_j = ∅.
- **(R2)** |D_j| is a positive multiple of |G|/gcd(n_v, n_j).
- **(R3)** Every right coset U_vy contained in D_j meets g_jU_j. If w ∈ g_jU_j ∩ U_vy, then g_jU_j ∩ U_vy = (U_v ∩ wU_jw⁻¹)w, and [U_v : U_v ∩ wU_jw⁻¹] = d_j.
- **(R5′)** If j ≠ k and D_j ∩ D_k ≠ ∅, then gcd(d_j, d_k) ≥ 2.
- (R4) from earlier versions is deleted, since it is unused.

**Proof of (R1).** Since g_vU_v = U_v and g_jU_j are disjoint, L0.2 gives g_j ∉ U_vU_j. Now U_vU_j = U_v·1·U_j is the double coset of 1, and D_j is the double coset of g_j. Distinct double cosets are disjoint, so D_j ∩ U_vU_j = ∅.

**Proof of (R2).** By L0.4, |U_v g_j U_j| is a multiple of |G|/gcd([G:U_v], [G:U_j]). It is positive because g_j ∈ D_j.

**Proof of (R3).**
- Let U_vy ⊆ D_j. Then y = c g_j u with c ∈ U_v and u ∈ U_j. So U_vy = U_v g_j u contains g_ju, which lies in g_jU_j.
- For w ∈ g_jU_j ∩ U_vy we have g_jU_j = wU_j and U_vy = U_vw. Then x ∈ wU_j ∩ U_vw ⟺ xw⁻¹ ∈ wU_jw⁻¹ and xw⁻¹ ∈ U_v. So g_jU_j ∩ U_vy = (U_v ∩ wU_jw⁻¹)w.
- For the index: [U_v : U_v ∩ wU_jw⁻¹] = |U_v · wU_jw⁻¹| / |wU_jw⁻¹|. Right multiplication by w preserves size, so |U_v · wU_jw⁻¹| = |U_vwU_j|. Since w ∈ D_j, U_vwU_j = D_j. Hence the index is |D_j|/|U_j| = d_j.

**Proof of (R5′).**
- D_j and D_k are both left U_v-invariant, so D_j ∩ D_k is too. Being non-empty, it contains a whole right coset C = U_vy.
- By (R3), choose w_j ∈ g_jU_j ∩ C and w_k ∈ g_kU_k ∩ C. The two pieces are P_j = g_jU_j ∩ C = A w_j and P_k = g_kU_k ∩ C = B w_k, where A = U_v ∩ w_jU_jw_j⁻¹ and B = U_v ∩ w_kU_kw_k⁻¹. Their indices in U_v are d_j and d_k.
- P_j ∩ P_k = ∅, because g_jU_j ∩ g_kU_k = ∅.
- **Right-translate into U_v.** Multiply both pieces on the right by w_j⁻¹. This gives A and Bc, where c = w_kw_j⁻¹ lies in U_v because w_j and w_k lie in the same right coset C. So A and Bc are disjoint subsets of U_v.
- **Invert.** A⁻¹ = A and (Bc)⁻¹ = c⁻¹B. These are disjoint left cosets in U_v of subgroups of indices d_j and d_k.
- **Apply k = 2 (L0.6) in U_v.** If gcd(d_j, d_k) = 1, then AB = U_v, so c⁻¹ ∈ AB, i.e. c⁻¹ = ab with a ∈ A and b ∈ B. Then a = c⁻¹b⁻¹ ∈ A ∩ c⁻¹B, a contradiction.
- Hence gcd(d_j, d_k) ≥ 2. ∎

**Core(5) form.** In Core(5), gcd(n_v, n_j) = 4. So |D_j| = q_j |G|/4 with q_j a positive integer. By (R1), D_j ⊆ G ∖ U_vU_j, which has size (4 − α_vj)|G|/4, so 1 ≤ q_j ≤ 4 − α_vj. Then d_j = q_j|G|/4 ÷ (|G|/(4r_j)) = q_jr_j.

## 6. Refutation of the pattern S-D

**S-D:**
- α01 = α02 = 1, α03 = α04 = 2, and α12 = α13 = α14 = α23 = α24 = α34 = 3;
- E2 = 1, so r_1 is even and 3 ∤ r_1;
- E3 = 0, so 3 | r_0 and r_0 is odd;
- r_2, r_3, r_4 are coprime to 6.

Assume a Core(5) configuration with this pattern. Take v = 2, translate so that g_2 = 1, and put X_j = U_2U_j for j ∈ {0, 1, 3, 4}.

**Step 1: sizes, and D_j = Y_j for j ∈ {1, 3, 4}.**
- By L0.3, |X_0| = α_20|G|/4 = |G|/4 and |X_1| = |X_3| = |X_4| = 3|G|/4.
- For j ∈ {1, 3, 4} put Y_j = G ∖ X_j, so |Y_j| = |G|/4.
- By (R1), D_j ⊆ Y_j. By (R2), |D_j| is a positive multiple of |G|/4.
- Hence D_j = Y_j, q_j = 1 and d_j = r_j.

**Step 2: Y_1, Y_3, Y_4 are pairwise disjoint.** If Y_j ∩ Y_k ≠ ∅ for distinct j, k ∈ {1, 3, 4}, then D_j ∩ D_k ≠ ∅. By (R5′), gcd(r_j, r_k) ≥ 2, contradicting coprimality.

**Step 3: X_0 ⊆ X_1 ∩ X_3 ∩ X_4.** Use rules-v1 L1 in the triangles {0, 1, 2}, {0, 2, 3} and {0, 2, 4}.
- In {0, 1, 2}: by (T2), τ ≤ α01·α02 = 1, so τ_012 = 1.
- In {0, 2, 3}: (T1) gives α03 = 2 | r_2 τ, and r_2 is odd, so τ is even. (T2) gives τ ≤ α02·α03 = 2. Hence τ_023 = 2. The same argument gives τ_024 = 2.
- By (T3) with apex 2:
  - |U_2(U_0∩U_1)| = τ_012|G|/(4α01) = |G|/4;
  - |U_2(U_0∩U_3)| = τ_023|G|/(4α03) = 2|G|/8 = |G|/4;
  - |U_2(U_0∩U_4)| = |G|/4.
- Each of these sets lies inside X_0 = U_2U_0, which has size |G|/4. So X_0 = U_2(U_0∩U_j) ⊆ U_2U_j = X_j for j = 1, 3, 4.

**Step 4: G ∖ X_0 = Y_1 ⊔ Y_3 ⊔ Y_4.**
- By Step 3, X_0 ∩ Y_j = ∅ for j = 1, 3, 4.
- By Step 2, |Y_1 ⊔ Y_3 ⊔ Y_4| = 3|G|/4 = |G ∖ X_0|.

**Step 5: the coset g_0U_0.**
- **Location.** By (R1), D_0 ⊆ G ∖ X_0. By (R2), |D_0| = q_0|G|/4 with q_0 ∈ {1, 2, 3}, and d_0 = q_0r_0.
- **D_0 meets some Y_j.** D_0 is non-empty, so by Step 4 it meets some Y_j = D_j with j ∈ {1, 3, 4}.
- **Gcd condition.** (R5′) gives gcd(q_0r_0, r_j) ≥ 2. Since gcd(r_0, r_j) = 1, gcd(q_0r_0, r_j) = gcd(q_0, r_j).
  - For j = 3, 4 the number r_j is coprime to 6, so gcd(q_0, r_j) = 1 for q_0 ∈ {1, 2, 3}. This is impossible.
  - So D_0 does not meet Y_3 or Y_4, and therefore D_0 ⊆ Y_1.
- **Contradiction (q_0 = 1 route).** Because |Y_1| = |G|/4, D_0 ⊆ Y_1 forces q_0 = 1. Then gcd(q_0, r_1) = gcd(1, r_1) = 1, which contradicts (R5′) for the pair {0, 1}.
- **Equivalent route (proof-v1).** gcd(q_0, r_1) ≥ 2 with r_1 even and 3 ∤ r_1 forces q_0 = 2, and then |D_0| = |G|/2 > |Y_1|.

So no configuration has the pattern S-D. ∎

## 7. Closure of the proof

Suppose Sun(5) fails. By §3, a minimal-order group G carries a Core(5) configuration. Its pattern (α, E2, E3) lies, up to relabelling, in one of the 21,150 orbits.

- If the orbit is not S-D, its certificate (§4) shows that no Core(5) configuration with that pattern exists. This holds for all admissible τ (M1) and for all pairwise coprime r with the given E2/E3 status (M2).
- If the orbit is S-D, §6 refutes it.

So no counterexample exists. Sun's conjecture holds at k = 5 for every group, subject to the verification status recorded in §4. ∎

## 8. Dependencies and boundary

**Imported as statements:**
- Zhu Theorem 1.1 (k = 3, 4).
- Standard facts: the product formula, Lagrange's theorem, and that cores of finite-index subgroups have finite index.

**Re-proved in this lane:**
- the k = 2 case (L0.2 + L0.6);
- M-S Lemma 3.1, inline in §2(g);
- the M-S Lemma 3.4 facts (L0.4, L0.5);
- M-S Prop 4.5 (§2).

**[NEW] (written in this lane):**
- rules-v1 L1–L8, with the cumulative errata in `rules-v1-erratum-v3.md`;
- N2;
- F together with H2;
- Lemma R.

**Finite exact:**
- engine-v1-run1 (canonical orbits);
- the parent bridge PASS (2d7fff78…7659 / d741396c…7278);
- check-v2-run1 (lane self-report).

**Not done:**
- No Lean.
- The gate is not claimed.
- Nothing has been published.
