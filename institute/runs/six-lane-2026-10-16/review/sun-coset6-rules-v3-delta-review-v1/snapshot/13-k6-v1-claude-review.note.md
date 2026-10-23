# Hostile mathematics audit: k6 reduction (SOURCE01) and rules-k6-v1 (SOURCE00)

**Scope.** I re-derived everything by hand from the inlined texts only. No code, enumeration, certificates, counts or survivor lists were supplied, so nothing here says any pattern dies. **No k6 theorem, no survivor claim and no novelty is asserted.** This is one hostile review (Claude family); SOURCE02:46 also requires a Codex-family review.

**Bottom line.** I found no FATAL or MAJOR mathematical defect. As written, each rule is a necessary condition for every genuine Core5(6) configuration in the minimal frame. That holds for all admissible τ, for all pairwise-coprime r with the stated markers (including r_i = 1 and arbitrary prime powers), for all q, all fibre assignments and all seven E5 placements. The findings are MINOR text or specification fixes, plus code and certificate obligations.

| Component | Verdict |
|---|---|
| Reduction R0/R1(6) and minimal frame | ACCEPT-WITH-FIXES (MINOR) |
| T/K/P specialisation | ACCEPT |
| H5 | ACCEPT |
| RLP | ACCEPT-WITH-FIXES (MINOR) |
| F/FH5 with M1/M2/E5 | ACCEPT-WITH-FIXES (MINOR) |
| Enumeration and certificates | not supplied; obligations only |

## 1. Reduction (SOURCE01:21–50)

**Verified:**
- **R0 (SOURCE01:23).** The intersection N of the cores is normal of finite index and lies inside every G_i. Each coset is a union of N-cosets, so indices and disjointness pass to G/N.
- **Each pair has one common prime.** gcd = 1 is excluded by L0.2 + L0.6. Every gcd in {2,3,4,5} is a prime power, so each pair shares exactly one prime, and it lies in {2,3,5}.
- **The A_p cover.**
  - If A_p ∩ A_q contained a pair {i,j}, then pq would divide its gcd, so the gcd would be ≥ 6.
  - With every |A_p| ≤ 5, the binomials lie in {0,1,3,6,10}. 10 + x + y = 15 has no solution, so the only option is 6+6+3, i.e. sizes {4,4,3}, which needs ≥ 7 points.
  - Hence one prime divides all six indices.
- **p = 2 sub-branches (SOURCE01:39–42).** The constructed r's are pairwise coprime, since at most one is even.
- **p = 5.** The r_i are pairwise coprime, and 5 may divide one of them (E5).
- **Repeated subgroups.** U_i = U_j forces r_i = r_j = 1 and α_ij = 1. No lemma assumes the subgroups are distinct.
- **Frame (SOURCE01:47–50).** Minimality is used only in F2 at s = 6, inside a proper H. R4′ has s ≤ 5. The argument is never circular.

**Findings:**
- **MINOR SOURCE01:38.** "All six gcds" should read "all fifteen pairwise gcds".
- **MINOR SOURCE01:45; SOURCE02:33, 46–47.** These lines are stale. They say Core(5) "still awaits" its verdict, and they bind proof-v3. SOURCE06:5,11 accepts Sun(5) on proof-v4 with erratum v3. Rebind to that text.
- **MINOR (simplification).** For p ∈ {2,3}, all fifteen gcds are ≤ 4. So any five of the six cosets contradict the accepted Sun(5) (SOURCE06:7–8) directly.
  - Replacing SOURCE01:38–42 with that argument removes Prop 4.5, Core(5) and Zhu from R1(6).
  - Zhu then remains only for F2 and R4′ at s = 3, 4.

## 2. T/K/P (SOURCE00:41–101)

Verified with L = 5r_ar_br_c and I_xy = 5r_xr_yα_xy:
- **(T1)–(T3) and the table.**
  - (T1) ⇔ α_xy | r_zτ.
  - (T3) = τ/(5α_xz), where xz is the edge not at the apex.
  - (T2) ⇔ τ ≤ the product of the two α's at each vertex.
  - τ_min = lcm of α_e/gcd(α_e, r_opp).
  - The table at SOURCE00:57–62 is correct, including α = 4 giving 4, 2 or 1 by E2 class. No prime ≥ 5 divides α.
- **Links and K.**
  - The L2 hypothesis holds exactly when τ equals the product at x.
  - Both K1 alternatives reduce to τ_ivj = α_ivα_vj. L2's second conclusion, U_vU_i ⊆ U_jU_i, has exactly the orientation L3 needs.
  - K: Σα_iv/5 ≤ 1 − 1/(5r_v) ⇔ Σα_iv ≤ 4.
  - K2 is L3 at j, via the inverse: α_vj + α_kj ≤ 4.
- **P.**
  - P2: gcd(5r_v, 5r_jr_kα_jk) = 5·gcd(r_v, α_jk).
  - min(|X_j|, |X_k|) is a multiple of u. When the sizes are equal, the two K2 conditions coincide.
  - PB uses only hi. The Bonferroni left side is non-increasing in the intersections, and ∪Y_j ⊆ G∖U_v.
- **Markers.** E2 = E3 coincidence is safe because the 2-part and 3-part are read independently. r_i = 1 and high prime powers enter only through gcd(α, r) with α ≤ 4.

No defect found. One note: "admissible" at SOURCE00:64 means "consistent with (T1)/(T2)", not "realised".

## 3. H5 (SOURCE00:116–137)

1. τ_max = min(c, c, c²) = c.
2. (T1) on edges va and vb gives c | r_bτ and c | r_aτ.
   - For c ∈ {2,3}, one of r_a, r_b is prime to c. For c = 4, one of them is odd.
   - So τ = c; the case c = 1 is immediate.
3. (T3) at apex v gives |U_v(U_a∩U_b)| = c/5 = |U_vU_a| = |U_vU_b|, so all three sets equal one set X.
4. X is right-invariant under W = ⟨U_a, U_b⟩ and contains U_v, so X = U_vW.
5. c ≤ 4 gives |X| < 1, so W ≠ G. [G:W] divides gcd(5r_a, 5r_b) = 5, which is prime. So W has index 5 and is proper.
6. U_aU_b ⊆ W and |U_aU_b| = 1/5 = |W|. The subgroup property is proved, not assumed.
7. |U_vW| = t_v/5 = c/5 holds for each v ∈ V separately, and W does not depend on v.

Also τ_min({v,a,b}) = c, so these triangles are never T-killed.

**ACCEPT, no findings.**

## 4. RLP (SOURCE00:139–173)

Verified (I re-checked R1–R3 and R5′ at SOURCE03:181–197):
- **Fibres.** D_j is left U_v-invariant, so it is a union of right U_v-cosets. S_C = {j : C ∩ g_jU_j ≠ ∅}.
- **R4′.**
  - The pieces A_jw_j are pairwise disjoint, where A_j = U_v ∩ w_jU_jw_j⁻¹ has index d_j.
  - Right-multiplying by w_0⁻¹ (with w_0 ∈ C) gives A_jc_j with c_j ∈ U_v.
  - Inverting gives disjoint left cosets c_j⁻¹A_j in U_v.
  - Sun(s) with s ≤ 5 then applies inside U_v (L0.6, Zhu, k5). Sun(6) is never used.
- **Sizes and mass.**
  - d_j = q_jr_j with 1 ≤ q_j ≤ 5 − α_vj, and common primes lie in {2,3}.
  - The total mass is ≤ 1 − |U_v| < 1, because U_v itself has S_C = ∅ by R1.
- **Duality.** Weak duality is enough.
  - If y ≥ 0 and Σ_{j∈S} y_j ≤ 1 on every allowed S, then Σμ ≥ Σ_j y_jq_j/5.
  - Constraints on maximal sets imply all the others (because y ≥ 0), even though "allowed" is not downward-closed.
- **Support.** The support predicate is upward-closed in each pairwise gcd, so a pointwise over-approximation is safe and simultaneous realisability is not needed.
  - In fact maxgcd is exact, because the minimum saturates at the partner's q-part. For class 2, v₂(r) ≥ 2 ≥ v₂(q). For E3, v₃(r) ≥ 1 ≥ v₃(q). Class 1 is exact.
  - No genuine support is dropped, provided all 31 non-empty S are tested.
- **All q are needed.** LPmin is not monotone in q: moving q_j from 2 to 3 can lose a common factor 2. So every q is required, as SOURCE00:166 says.

**Findings:**
- **MINOR SOURCE00:143.** R1–R5′ were proved for five cosets (SOURCE03:172). State that the proofs use only pairwise disjointness and hold verbatim for six.
- **MINOR SOURCE00:153.** Write out the s-piece translation and inversion, as SOURCE03:192–196 does for two pieces.
- **MINOR (certificate specification) SOURCE00:171, 194–210.** The content of an RLP witness is not specified. Require the following:
  - For each killing v and every q in ∏[1, 5−α_vj], an exact rational y(q) ≥ 0 with Σq_jy_j ≥ 5.
  - The verifier recomputes allowed-ness itself and checks all ≤ 31 subsets, so no maximal-set generator has to be trusted. A clique-style generator can silently drop allowed sets.
  - Simplex or Bland's-rule output is not evidence.

## 5. F/FH5 with M1/M2/E5 (SOURCE00:103–114, 175–192, 202–208)

Verified:
- **F1–F3.** These match SOURCE04:189–201, with λ_l = r_lt_l. F2 uses imports for s ≤ 5 and minimality for s = 6 (H is proper).
- **FH5.**
  - Inside H: a, b and the members of V with α = 1. Forced: t_v = α_va. Free: t ∈ 1..5.
  - F3 is applied at every vertex with t = 1. A free vertex given t = 1 would need α = 1 to both a and b, so it would lie in V; such assignments are rejected anyway.
  - F2 is applied in all five cosets. Fixing a's label is a pure relabelling.
  - The rejection test is downward-closed in the gcds, so using maximal gcds is safe.
- **E5.** No α or q is divisible by 5, and P2 adds no factor 5. So E5 matters only in F, where all seven placements are required.
- **M1.** A link at τ_min forces τ = τ_min, and lo increases with τ. hi, K2, PB, RLP and F do not read τ.

**Findings:**
- **MINOR SOURCE00:189.** "Exponents larger than any t-part" is false for genuine small cofactors: v₂(r) = 2 against t = 4, v₃ = 1 against t = 3, v₅ = 1 against t = 5. The correct justification is saturation:
  - Let e₂ = 2, e₃ = 1, e₅ = 1, the largest v_p(t) for t ≤ 5.
  - Then v_p(r) ≥ e_p gives min(v_p(t_l) + v_p(r_l), v_p(t_l′)) = v_p(t_l′), which does not depend on the instance.
  - So every instance, from r = 4·…, 3·…, 5·… up to arbitrary powers, has the same gcd vector as the 2⁴/3⁴/5⁴ representative. Class 1 is exact.
  - Fix: replace "larger than" with "at least e_p (the minimum saturates)".
- **MINOR SOURCE00:206.** The M_l-enumeration clause sits under "Free vertices". State that every vertex except a ranges over all t_l-subsets:
  - b and the inside V-vertices over all five labels;
  - forced vertices over all C(5,c) sets.
  - Fixing any of them would be unsound; this is a code obligation.
- **MINOR SOURCE00:24.** "Any two" should read "any, including all three".

## 6. Enumeration and controls

Code obligations (I have not checked these):
1. **Coverage.** For each type, all 4^15 labellings are visited. Pruning happens only at a completed triangle with τ_min > τ_max from the table.
2. **Canonical forms.**
   - The 8 types (none, E3, E2c1, E2c2, E2=E3 ×2, E2≠E3 ×2) have stabilisers S6 (once), S5 (five times) and S4 (twice).
   - The canonical form must be a complete invariant: one that merges orbits is unsound, one that splits them is only redundant.
   - The rules must run on the stored representative.
3. **Representatives.**
   - Non-special bases must be prime to 30 and pairwise coprime.
   - E2c1 needs v₂ = 1 exactly, E2c2 needs v₂ ≥ 2, E3 needs v₃ ≥ 1, and E5 needs v₅ ≥ 1 at each of the 7 placements.
4. **Search ranges.** K, P, RLP and FH5 must range over all v, S, pairs, 1-edges, q and E5 placements.

**MINOR SOURCE00:215 (controls wording).** "Any other orbit would mean a rule is unsound" inverts the logic.
- An extra Core(5) survivor means the k6 code kills less than engine-v1's T/K/PB did. That is a reproduction mismatch, not a false elimination.
- Every Core(5) and Core_3(4) pattern is impossible by accepted theorems, so these reruns cannot detect unsoundness at all.
- Better: evaluate each rule independently per orbit, and flag two cases:
  - engine-v1 T/K/PB kills that are not reproduced (a mismatch);
  - N2, FH2 or S-D orbits killed by the rerun's T/K/P (an over-strength warning; only RLP may legitimately do this).
- Soundness evidence remains the written proofs, survival of realisable configurations (SOURCE02:41), and mutation demonstrations.

## 7. Audited, imported, and required certificates

**Independently audited here, by hand:**
- R0 and R1(6);
- L0.3–L0.6 (elementary);
- the specialisation of L1–L4;
- H5;
- R1–R3, R5′ and R4′, with the LP and its duality;
- F1–F3 and the FH5 logic;
- M1, M2 and E5.

**Imported:**
- Zhu Thm 1.1 (k = 3, 4);
- Sun(5) for every group, per SOURCE06, including its engine and bridge;
- the product formula, Lagrange's theorem and cores.

The Gong thesis was not used.

**Not audited:** any code, run, count or survivor list, and the exploratory figures at SOURCE01:71–85.

**Exact certificates required.** These are per canonical orbit, in exact integers and rationals, and replayed independently per SOURCE02:46:
- **T:** the triangle, its α's, the markers, and τ_min > τ_max.
- **K:** v, S, τ_min = α_viα_vj for each pair, and Σα_iv ≥ 5.
- **P-pair:** v, j, k, u, and lo > hi.
- **PB:** v, S, every hi, and left side ≥ 1.
- **RLP:** v, and y(q) for every q.
- **FH5:** (a,b), V, the inside and forced sets, and for each of the 7 E5 placements the exhaustive all-rejected count.
- **Universe:** coverage over the 8 types (or a proved-complete canonical set), plus the exact survivor list (α matrix, E2 class, E3), with no leaf dropped.

The rules are sound subject to the MINOR fixes above. Any k6 conclusion stays conditional on SOURCE06 and on replayed certificates; none is drawn here.
