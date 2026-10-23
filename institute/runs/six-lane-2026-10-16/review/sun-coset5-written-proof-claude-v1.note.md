# Hostile audit: Sun 2006 Conjecture 1.2 at k = 5, written mathematics (S00–S07)

Citations use `Sxx:n` for SOURCExx line n. This is not a novelty or priority verdict.

## DISPOSITION: **ACCEPT-WITH-FIXES**

- **FATAL:** none found.
- **MAJOR:** none found.
- **MINOR:** three are load-bearing (F-1, F-2, F-3), each with a short repair supplied below. The rest are citation, wording or specification fixes.
- **Conditions:**
  - (i) Zhu Theorem 1.1 is imported as a statement.
  - (ii) The separate bridge replay must check the certificate semantics in §3. Under those semantics every certificate type does imply that no configuration with that pattern exists.

## 1. Essential path, re-derived independently

**R0 (S02:27–31). ✓**
- core_G(G_i) is the kernel of G acting on G/G_i, so its index is at most [G:G_i]!.
- N = ∩ core_G(G_i) is normal of finite index and lies in every G_i ∩ G_j.
- Each coset is the full preimage of its image in G/N. So indices, intersection indices and disjointness all transfer to G/N.

**R1 (S02:37–46). ✓, case analysis complete.**
- No pair of indices is coprime (L0.2 + L0.6).
- If some n_i is odd, each gcd with it is odd and lies in {2,3,4}, so equals 3. Hence 3 divides every index.
- **All-3 case:** all gcds are 3 < 4. Any four indices contradict Zhu Thm 1.1 at k = 4 directly.
- **All-even case:** the odd parts m_i are pairwise coprime, min(e_i,e_j) ∈ {1,2}, and at most one e_i ≥ 3.
  - Two indices with e = 1: a triple with all gcds 2 < 3 contradicts Zhu at k = 3.
  - Exactly one with e = 1: we get (2r_1, 4r_2, 4r_3, 4r_4) with r_1 odd and pairwise coprime r's. This is M-S Prop 4.5.
  - Otherwise: a Core(5) configuration.

**M-S Prop 4.5 (S03:465–521), audited line by line rather than imported blind.**
- Lemma 3.1 ✓.
- Lemma 3.5 / Cor 3.6 ✓. The claim, union and g_v step are all correct.
- Prop 3.8 ✓. The lcm computations hold, and VU_j ⊆ U_iU_j holds for every ordered pair, which covers the "j > i" hypothesis of 3.5.
- Lemma 4.1 ✓. Lemma 4.4 bullet 1 ✓.
- Lemma 4.4 bullet 2 ✓, except one citation (F-2).
- Prop 4.5 body:
  - α(1,i) = 1 and α(i,j) ∈ {1,3}.
  - A vertex of {2,3,4} whose two inner α's are both 1 is killed by Prop 3.8 (a = 4, a_1 = 2, Σ1/a_i = 1, gcd(2,r_1) = 1).
  - The case α(3,4) = 1: here 3 | τ, so |U_3(U_2∩U_4)| ∈ (|G|/4)ℤ. That forces U_3U_4 ⊆ U_3U_2, and Cor 3.6 applies with |U_3U_4| + |U_2U_4| = |G|. ✓
  - Final Lemma 3.1 count: 1/2 − 1/4 − 1/4 = 0, while the intersection contains U_2. ✓

**Minimal counterexample (S00:18, S01:30). ✓ (wording: F-3)**
- R1's argument works inside one group with the same subgroups. So for each finite G, "G has a full-target counterexample" ⟺ "G has a Core(5) configuration".
- Therefore the minimal-order G for the full target carries a Core(5) configuration, and every proper subgroup satisfies full Sun k = 5.
- k = 5 is applied only inside proper H (F2 with s = 5). There is no circularity.

**Pattern space.**
- α_ij ∈ {1,2,3} (L0.3), and E2, E3 ∈ {none} ∪ V with E2 = E3 allowed.
- I recomputed the orbit counts by Burnside over S5. On edges the cycle counts are 10/7/4/6/3/2/3, with class sizes 1/10/20/15/30/24/20.
  - 95,040/120 = 792 α-classes.
  - 2,538,000/120 = 21,150 (α, E2, E3) orbits, matching S06:7–8.
- This agreement is consistency only, not proof.
- Every rule is S5-equivariant, so one certificate per orbit suffices.

**L0 (S01:34–57). ✓**
- L0.2 is an iff, proved inline.
- L0.4 follows from |AxB| = |A||B|/|A∩xBx⁻¹|.
- L0.5 (the mirror of M-S 3.4(2)) ✓.

**L1, triangle rule T (S01:70–98). ✓**
- (T1)–(T3) are pure subgroup facts and need no harmonicity.
- Core(5) forms:
  - L = 4r_ar_br_c.
  - (T1) ⟺ α_xy | r_zτ.
  - (T3): |U_y(U_x∩U_z)| = τ|G|/(4α_xz).
  - (T2) at apex y: τ ≤ α_xzα_xy and τ ≤ α_xzα_yz. So τ_max is the minimum of the three vertex products.
- The admissible τ are exactly the multiples of τ_min. τ_min depends only on E2/E3.

**L2 and Lemma K (S01:100–132). ✓, orientation checked.**
- **K step 1:** both alternatives reduce to L0.2. The second goes via inversion: g_i⁻¹g_j ∈ U_iU_vU_j ⊆ U_iU_j.
- **K step 2:** g_iU_iU_v is right-U_v-invariant. If it met g_vU_v it would contain g_v, which forces g_vU_v to meet g_iU_i.
- **Bound:** the sets are disjoint inside G∖g_vU_v, so the inequality is strict.
- **K1:** L2 with (y,x,z) = (i,v,j) gives U_vU_i ⊆ U_jU_i, and (j,v,i) gives U_vU_j ⊆ U_iU_j. These are exactly K's two alternatives, and both have Core(5) condition τ = α_viα_vj.
- **K2:** the inverse of U_vU_j ⊆ U_vU_k is K's first alternative at vertex j with S = {v,k}.

**L4, P-pair and P-Bonferroni (S01:142–165). ✓**
- (P2) follows from L0.5 + L0.4, with gcd(4r_v, 4r_jr_kα_jk) = 4·gcd(r_v, α_jk).
- |X_j| = α_vj|G|/4 is always a multiple of u ∈ {|G|/4, |G|/8, |G|/12}. So the one-unit K2 lowering of hi is valid. The equal-size case yields the same condition.
- (P5): Bonferroni gives a lower bound on |∪Y_j|, and ∪Y_j ⊆ G∖U_v, so the inequality is strict.
- The left side of (P5) decreases in each |X_j∩X_k|, and the true value is ≤ hi. So LHS(hi) ≥ |G| refutes the pattern. hi does not depend on τ.

**N2 (S01:167–185). ✓ for every E2/E3, i.e. all 5 orbits.**
- Each triangle has at least two odd vertices, so τ is even; also τ ≤ 4.
- τ = 4 gives a link at every vertex, and L3 then requires 2 + 2 ≤ 3. So τ = 2.
- Take v with r_v odd. Then |Z_jk| = |G|/4 and u = |G|/4. X_j = X_k is forbidden by K2. Hence X_j∩X_k = Z_jk.
- Q is divisible by lcm(8r_vr_jr_k, 8r_vr_jr_l, 8r_vr_kr_l) = 8r_vr_jr_kr_l. So |U_vW| ≥ |G|/4, which forces the three Z's of a triple to coincide.
- Any two pairs among the four other vertices are linked through triples, so all six Z's are equal. Then |∪X_j| = 5|G|/4 > |G|.

**F (S01:187–201). ✓**
- (F1): g_lU_lH contains t_l left H-cosets.
- (F2): the piece in C is y(U_l∩H); the z⁻¹ left-translate lies in H. Sun applies in H for s ≤ 4 (L0.6 / Zhu) and for s = 5 by minimality, since H is proper.
- (F3) ✓. Also t_i = 1 ⟺ U_i ⊆ H, so applying F3 at enumerated t = 1 vertices is valid.

**H2 (S01:207–219). ✓**
- τ ≤ min(4,2,2), and 2 | r_aτ, 2 | r_bτ, so τ = 2.
- U_vU_a = U_v(U_a∩U_b) = U_vU_b, all of size |G|/2.
- The right stabiliser of X is a subgroup containing U_a and U_b. So X = U_vW and W ≠ G. Also [G:W] divides 4.
- Index 4: W = U_aU_b is proved by cardinality, not assumed. Then t_v = 2.
- Index 2: U_v ⊆ W.
- W does not depend on v.
- No subgroup product is assumed to be a subgroup anywhere on the path. X_j, Z_jk and D_j are handled purely as sets.

**L8, evaluation points (S01:221–241). ✓**
- **M1:**
  - A K-link at τ_min pins τ = τ_min, because τ is bounded above by the same vertex product.
  - The P lower bounds are monotone in τ.
  - T-kill concerns τ_min itself.
  - No other rule reads τ.
- **M2:**
  - T, K and P see r only through E2/E3 status.
  - In F, no prime ≥ 5 divides gcd(λ_l, λ_l'), since t ≤ 4 and the r's are coprime.
  - The 2-adic minimum is maximised once v₂(r_E2) ≥ 2 (m = 4) or ≥ 1 (m = 2). The 3-adic minimum is maximised once v₃(r_E3) ≥ 1. So 16 and 81 dominate every allowed case.
  - The kill condition is monotone in the gcds. There is no hidden exponent restriction.

**Lemma R (S00:31–55). ✓, except the (R5) derivation (F-1).**
- **(R1):** g_j ∉ U_vU_j, so D_j and U_vU_j are distinct, hence disjoint, double cosets.
- **(R2):** L0.4.
- **(R3):**
  - U_vy = U_vg_ju contains g_ju.
  - wU_j ∩ U_vw = (U_v∩wU_jw⁻¹)w.
  - The index is |U_vwU_j|/|U_j| = d_j, since wU_j = g_jU_j.
  - Count check: (|D_j|/|U_v|)·(|U_v|/d_j) = |U_j|.
  - The left/right orientation and conjugate are correct.
- **(R4):**
  - c_j = w_jw₀⁻¹ ∈ U_v.
  - The pieces become disjoint right cosets of A_j in U_v, then left cosets after inversion.
  - s ≤ 4.
- **Core(5) form:** d_j = s_jr_j with s_j ≤ 4 − α_vj.

**S-D refutation (S00:57–89). ✓, given R5′.**
- **Step 1:** |Y_j| = |G|/4 and |D_j| ≥ |G|/4, so D_j = Y_j and d_j = r_j.
- **Step 2:** by R5′, Y_1, Y_3, Y_4 are pairwise disjoint.
- **Step 3:**
  - τ₀₁₂ ≤ α01·α02 = 1.
  - τ₀₂₃: 2 | r₂τ with r₂ odd, and τ ≤ α02·α03 = 2, so τ₀₂₃ = 2. Likewise τ₀₂₄ = 2.
  - The apex-2 sets have size |G|/4 = |X_0|, so X_0 ⊆ X_j for j = 1, 3, 4.
- **Step 4:** cardinality gives G∖X_0 = Y_1 ⊔ Y_3 ⊔ Y_4.
- **Step 5:**
  - D_0 ⊆ G∖X_0 = ⊔Y_j.
  - Meeting Y_3 or Y_4 needs gcd(s_0, r_j) ≥ 2 with s_0 ≤ 3 and r_j coprime to 6. That is impossible.
  - So D_0 ⊆ Y_1, and size forces s_0 = 1. Then gcd(1, r_1) = 1, a contradiction.
  - The worker's s_0 = 2 route at S00:86–87 is also valid.
- The argument uses only α01, α02, α03, α04, α12, α23, α24, with r₂ odd and r₃, r₄ coprime to 6.

## 2. Findings

**F-1 MINOR, load-bearing (S00:40, S00:53; used at S00:64 and S00:82).**
- **Problem:** "Apply (R4) with s ≥ 2" only gives gcd ≥ s for *some* pair in S_C. If C also lies in a third D_l, that pair need not be {j,k}. This is a non-sequitur, though the conclusion is true.
- **Repair (R5′):**
  - Take C = U_vy ⊆ D_j∩D_k. By (R3), C meets g_jU_j and g_kU_k in pieces whose subgroups have index d_j and d_k in U_v.
  - The two pieces are disjoint. Right-translate by w₀⁻¹ and invert to get two disjoint left cosets in U_v.
  - L0.6 (Sun k = 2) then gives gcd(d_j, d_k) ≥ 2.
- **Effect:** after the repair, Lemma R's essential use needs only k = 2, and (R4) for s ≥ 3 becomes unused.

**F-2 MINOR, load-bearing import (S03:485, inside Lemma 4.4, used by Prop 4.5 at S03:501, :507, :518).**
- **Problem:** "Lemma 3.10a) implies 3 | r1" applies 3.10 outside its hypotheses (S03:359–360 needs a common a with pairwise coprime cofactors). The indices (2r₁, 4r₂, 4r₃) do not fit: a = 2 leaves 2r₂ and 2r₃ non-coprime, and 4 does not divide 2r₁.
- **Patch:**
  - T := [G:U₁∩U₂∩U₃] = 4r₁r₂r₃τ.
  - 12r₂r₃ | T gives 3 | r₁τ.
  - |U₂(U₁∩U₃)| = |G|·T/(4r₂·4r₁r₃) = τ|G|/4 ≤ |U₂U₁| = |G|/2, so τ ≤ 2.
  - Hence 3 | r₁.
- The lane missed this defect. I recommend writing the patched Prop 4.5 into R1 instead of resting on control C1, which is not evidence.

**F-3 MINOR, load-bearing wording (S00:18, S01:30).** Add the sentence: "R1(⇒) holds per group, so the minimal G over the full target carries a Core(5) configuration."

**F-4 MINOR, bridge specification (S01:207–219, :245–260; S00:22).**
- H2 only gives a disjunction. A valid FH2 certificate must exhaust **both** alternatives for the **same** (a,b).
- If any of the 22 certificates refutes only one case, that certificate is invalid, which would be FATAL for its pattern.
- Further semantics are in §3.

**F-5 MINOR (S01:140, S02:50).**
- The claimed misprint in M-S Lemma 4.4 is not supported by the extract.
- S03:468 reads "α(U2,U3) 6= 2", and "6=" is pdftotext's rendering of ≠ (compare S03:395, "U1U2 6= G").
- arXiv v1 already prints "≠ 2". Delete the claim or cite the journal page. The real defect is F-2.

**F-6 MINOR (S02:38–39).**
- The direction labels are swapped. "(⇐)" actually proves Sun ⟹ Core(5).
- "(⇒)" proves the load-bearing direction, Core(5) ⟹ Sun.

**F-7 MINOR (S00:17, S02:42, S02:44).**
- Zhu Thms 2.2 and 3.1 are not in the excerpt.
- Cite Zhu Thm 1.1 (S04:41–43) instead: Props 4.2 and 4.3 are immediate from it, since the gcds are 2 < 3 and 3 < 4.
- Only Prop 4.5 genuinely goes beyond Zhu, as S02:49 correctly notes.

**F-8 MINOR, imported (S03:508).**
- "Multiple of |G|α/4" is unjustified, since non-identity double cosets can be smaller.
- Only "multiple of |G|/4" follows (gcd(4r₂, 12r₃r₄) = 4 because 3 ∤ r₂), and only that is used.

**F-9 MINOR, source gap.**
- M-S §2 (definition of "harmonic" / "G-harmonic", Lemma 2.2, Thm B) is not excerpted.
- It is closed for this use because Prop 4.5's own proof fixes the meaning (S03:497–499: there exist g_i with pairwise disjoint left cosets, and no distinctness is used). I audited that proof rather than the bare statement.
- M-S's standing convention that groups are finite (S03:252) requires R0 first, which the lane provides.

**F-10 MINOR, cosmetic.**
- S00:55 uses s_j, which clashes with s = |S_C| at S00:39. Rename.
- S01:98: "gcd(α, r_z) = α exactly when…" is false for α = 1, but harmless because α/gcd = 1 either way.
- S02:28: justify why the cores have finite index.

**Counterexamples to invalid general lemmas:** none. No lane lemma on the essential path is false. F-1, F-2 and F-8 are faulty justifications of true conclusions, so there is nothing to refute.

## 3. Certificate semantics the replay must check

With these semantics, a passing certificate implies that no configuration with that pattern exists. Sizes are in units of |G|. All data are recomputed from (α, E2, E3) only.

- **Enumeration:** every S5-orbit of {1,2,3}^10 × ({∅}∪V)², for example by canonicalising all 2,125,764 labelled triples. The single uncertified orbit must be the orbit of the labelled S-D pattern at S00:25–28.
- **T(a,b,c):**
  - τ_min = lcm over the three edges of α_e/γ_e, where γ_e = α_e if (α_e = 2 and the opposite vertex is E2) or (α_e = 3 and the opposite vertex is E3), and γ_e = 1 otherwise.
  - τ_max = the minimum vertex product.
  - Require τ_min > τ_max.
- **K(v,S):**
  - For every pair {i,j} ⊆ S, require τ_min(v,i,j) = α_viα_vj.
  - Require Σ_{i∈S} α_iv ≥ 4.
  - Pair conditions may come **only** from K1.
- **PB or P-pair(v,·):**
  - x_j = α_vj/4.
  - u = 1/(4γ) with γ = gcd(r_v, α_jk) ∈ {1,2,3}, read off E2/E3.
  - hi = min(x_j, x_k) − u·[α_vs + α_jk ≥ 4], where s is the smaller side; equal sizes give the same test.
  - PB: Σ(1 − x_j) − Σ_{j<k}(1 − x_j − x_k + hi_jk) ≥ 1.
  - P-pair: ⌈max(τ_min(v,j,k)/(4α_jk), x_j + x_k − 1)⌉_u > hi.
  - S06 reports only "PB". The replay should state which rule actually fires; both are sound.
- **N2:** all ten α equal 2.
- **FH2(a,b):**
  - Require α_ab = 1 and V2 ≠ ∅.
  - Case (i): m = 4, t_a = t_b = 1, and t_v = 2 for every v ∈ V2.
  - Case (ii): m = 2 and t = 1 on {a,b} ∪ V2.
  - All other t_l range over 1..m, and every met-coset set M_l with |M_l| = t_l is enumerated.
  - λ_l = 4r_lt_l/m, with the 2-adic and 3-adic valuations taken at dominating representatives.
  - Reject an assignment iff (F3) fails for some vertex with t = 1, or some coset with s ≥ 2 has all pairwise gcds < s.
  - Coset-relabelling symmetry may be used. Placing a and b in distinct cosets is justified in case (i) only.
  - No coverage or balance constraint may be imposed.
  - All assignments must be rejected in **both** cases.

## 4. Audited versus imported

**Audited here:**
- R0 and R1.
- From M-S: Lemmas 3.1, 3.2, 3.4(1) and the mirror of 3.4(2), Lemma 3.5, Cor 3.6, Prop 3.8, Lemma 4.1, Lemma 4.4 (with the F-2 patch), and Prop 4.5.
- The minimality framing.
- L0.1–L0.6 and L1–L8, including the engine's use of P, M1 and M2.
- Lemma R (with the F-1 patch) and the S-D refutation.
- The orbit counts, as consistency only.

**Imported as statement only:**
- Zhu Theorem 1.1, used in R1 and in F2 for s ∈ {3,4}.
- Standard facts: the product formula, Lagrange, and cores of finite-index subgroups.

**Effectively re-proved:** Sun k = 2 (S05:604–616 = L0.2 + L0.6).

**Separately replayed, not reviewed here:** the 21,150 certificates.

**Unavailable but unneeded after F-7 and F-9:** M-S §2, Lemma 2.2 and Thm B; Zhu Thms 2.2 and 3.1; Menon §2; the journal versions.

## 5. Optional or unused (not on the essential path)

- **README R2 and R3 (S02:53–61):** spot-checked and correct, but unused.
- **H1 / M-S 3.7:** FH1 count is 0.
- **Cor 3.11 correction (S01:135–139):**
  - I agree the printed 3.10a step is vacuous when α(U,W) = α(V,W).
  - The fix is valid for α ∈ {1, prime}.
  - It is irrelevant here because Prop 4.3 goes through Zhu.
- **Lemma 4.4 misprint remark:** incorrect (F-5).
- **(R4) for s ≥ 3:** unused once F-1 is applied.
- **Controls C1–C4, the exploratory record, the priority search and the in-run re-checks:** not evidence.
