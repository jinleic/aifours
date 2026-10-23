# proof-k6-lemmas-v1: written proofs of the k = 6 lemmas added after rules-k6-v1

This file covers rules-k6-v2 L9 and rules-k6-v3 L10, L11 and L12.

- **Freeze record.** The host-clock time and sha256 are in `evidence/proofs-v1.sha256`.
- **Status.** [NEW] means only "written in this lane"; it is not a novelty claim. Nothing here is a theorem claim about k = 6. The proofs are unreviewed. The parent will run hostile reviews of the v2 and v3 changes.

## 0. Standing setting and imports

**Setting.** These hypotheses hold throughout.
- G is a finite group with subgroups U_0, …, U_5.
- [G:U_i] = 5r_i, where r_i ≥ 1 and the r_i are pairwise coprime. The case r_i = 1 is allowed, and so are arbitrary prime powers.
- The cosets g_0U_0, …, g_5U_5 are pairwise disjoint.
- The subgroups need not be distinct. In Core5(6), two equal subgroups force both cofactors to equal 1.

**Markers.** E2 is the vertex with r even, together with its class c2 (v₂(r) = 1, or v₂(r) ≥ 2). E3 is the vertex with 3 | r. E5 is the vertex with 5 | r. Each marker may be absent. Any two of them, or all three, may coincide.

**Measures.** All sizes are normalised: for X ⊆ G, write μ(X) = |X|/|G|. Then:
- μ(U_iU_j) = α_ij/5, where α_ij = [G:U_i∩U_j]/(5r_ir_j) ∈ {1, 2, 3, 4};
- μ(U_i) = 1/(5r_i).

**Imports** (rules-k6-v1 §0), with H a subgroup:
- **Sun(2):** L0.6, the Chinese remainder theorem for coprime indices.
- **Sun(3) and Sun(4):** Zhu Theorem 1.1.
- **Sun(5):** the accepted Core(5) result, `R/sun-coset5-parent-verdict-v1.md`, which binds sun-coset5 proof-v4 and its cumulative errata. Via R1, this gives Sun(5) in every group.
- **Sun(6):** used **only** inside a proper subgroup H < G of a minimal-order counterexample, and only in F2 when six vertices meet one H-coset (FH5). It is never used in R4′, RLP or RPLP, where at most five pieces lie in one right U_v-coset.

## 1. rules-k6-v2 L9: the hereditary Sun condition

**Statement.** Two settings are covered.
- **(a) Left cosets of H.** Let H ≤ G, and assume H < G if |S| = 6 is used. Let C be a left coset of H, and let S be the set of l whose coset g_lU_l meets C. Put λ_l = [H : H∩U_l].
- **(b) Right cosets of U_v.** Let v be a vertex and translate so that g_v = 1. Let C = U_vy be a right coset, and let S be the set of j ≠ v with C ⊆ D_j = U_vg_jU_j. Put d_j = [U_v : U_v ∩ wU_jw⁻¹], where w ∈ g_jU_j ∩ C; the value does not depend on the choice of w.

In both settings: for every T ⊆ S with |T| ≥ 2, some pair l ≠ l′ in T has gcd(λ_l, λ_l′) ≥ |T| (respectively gcd(d_l, d_l′) ≥ |T|).

**Proof of (a).**
1. **Pieces are cosets of H∩U_l.** Fix z ∈ C. For l ∈ S choose y_l ∈ g_lU_l ∩ C. Then g_lU_l = y_lU_l and C = y_lH, so g_lU_l ∩ C = y_l(U_l∩H).
2. **Move into H.** Left-multiplying by z⁻¹ gives z⁻¹y_l(U_l∩H). Here z⁻¹y_l ∈ H, so this is a left coset in H of the subgroup U_l∩H, which has index λ_l in H.
3. **Disjointness.** For l ≠ l′ the sets g_lU_l ∩ C and g_l′U_l′ ∩ C are disjoint, because g_lU_l ∩ g_l′U_l′ = ∅. Left translation preserves disjointness.
4. **Apply Sun.** For T ⊆ S, the cosets {z⁻¹y_l(U_l∩H) : l ∈ T} are |T| pairwise disjoint left cosets in H of finite-index subgroups. Apply Sun(|T|) in H:
   - |T| ≤ 5: by the imports;
   - |T| = 6: by minimality, since H < G.

   So some pair has gcd ≥ |T|.

**Proof of (b).**
1. **Pieces are right cosets.** For j ∈ S, the coset C lies in D_j, so it meets g_jU_j (rules-k6-v1 L7 R3). Choose w_j ∈ g_jU_j ∩ C. Then g_jU_j = w_jU_j and C = U_vw_j, so g_jU_j ∩ C = (U_v ∩ w_jU_jw_j⁻¹)w_j =: A_jw_j.
2. **Index of A_j.** [U_v : A_j] = |U_v·w_jU_jw_j⁻¹| / |U_j|. Right multiplication by w_j preserves size, so this equals |U_vw_jU_j| / |U_j| = |D_j|/|U_j| = d_j.
3. **Move into U_v.** Fix w_0 ∈ C. Right-multiplying by w_0⁻¹ gives A_jc_j with c_j = w_jw_0⁻¹ ∈ U_v.
4. **Invert.** Inversion turns A_jc_j into c_j⁻¹A_j. These are pairwise disjoint left cosets in U_v, of indices d_j, because the g_jU_j are pairwise disjoint and both operations are bijections.
5. **Apply Sun.** For T ⊆ S, |T| ≤ 5. Apply Sun(|T|) in U_v by the imports (Sun(6) is not needed). So some pair has gcd ≥ |T|. ∎

**Consequences for the rules.**

| Rule | Consequence |
|---|---|
| FH5 | In every coset, every subfamily T of the members passes the test. An assignment that fails it for some T is impossible. |
| RLP / RPLP | A support S carries positive mass only if it is **hereditary-allowed**: every T ⊆ S with \|T\| ≥ 2 has a pair with gcd ≥ \|T\|. |

The allowed family is therefore closed under taking subsets.

**Replacing gcd by maxgcd is safe.** The allowed test is monotone, i.e. upward closed, in each pairwise gcd. The true gcd(q_jr_j, q_kr_k) is at most maxgcd, which is computed from the markers:
- only the primes 2 and 3 can be common, since q ≤ 4 and the r's are coprime;
- v₂ of the pair is min(v₂(q_j) + ε_j, v₂(q_k) + ε_k), where ε = 1 for E2 of class 1, ε = SAT for E2 of class 2, and ε = 0 otherwise. Likewise for 3 with E3.

Each minimum **saturates at the partner's q-part**: v₂(q) ≤ 2 and v₃(q) ≤ 1. So maxgcd equals the true gcd for every instance with the given markers. No allowed support is lost.

## 2. rules-k6-v3 L10 (XE)

**Statement.** Let v, j, k be distinct, and suppose U_vU_j = U_vU_k. Then:
- α_jk = 1;
- W := U_jU_k is a subgroup of index 5;
- [U_v : U_v∩W] = α_vj.

**Proof.**
1. **X absorbs W.** X := U_vU_j satisfies XU_j = X, and since X = U_vU_k, also XU_k = X. Hence XW = X for W := ⟨U_j, U_k⟩.
2. **X = U_vW.** Because 1 ∈ X, we have U_v ⊆ X, so U_vW ⊆ XW = X. Conversely, X = U_vU_j ⊆ U_vW.
3. **W ≠ G.** μ(X) = α_vj/5 ≤ 4/5 < 1.
4. **Index 5.** U_j ≤ W and U_k ≤ W, so [G:W] divides [G:U_j] = 5r_j and [G:U_k] = 5r_k. Hence it divides gcd(5r_j, 5r_k) = 5, and since W ≠ G, [G:W] = 5.
5. **α_jk = 1.** U_jU_k ⊆ W, so α_jk/5 = μ(U_jU_k) ≤ μ(W) = 1/5. Hence α_jk = 1 and μ(U_jU_k) = μ(W), so U_jU_k = W.
6. **The index of U_v∩W.** μ(U_vW) = [U_v : U_v∩W]·μ(W), by the product formula. Since μ(U_vW) = μ(X) = α_vj/5, we get [U_v : U_v∩W] = α_vj. ∎

**Corollary.** If α_jk ≥ 2, then U_vU_j ≠ U_vU_k for every vertex v.

## 3. rules-k6-v3 L11 (N2-6)

**Hypotheses.** Let v be a vertex such that:
- (i) v ≠ E2, so r_v is odd;
- (ii) α_vj = 2 for all j ≠ v;
- (iii) α_jk ∈ {2, 4} for all distinct j, k ≠ v;
- (iv) for every triple {j,k,l} ⊆ V∖{v}, gcd(r_v, τ_jkl) = 1.

Condition (iv) holds automatically if v ≠ E3, because every prime factor of τ is 2 or 3. If v = E3, it holds when 3 ∤ τ_jkl for every triple. A sufficient test for that: for each triple, either 3 | τ_min(jkl) — impossible here, since τ_min is a product of 2-powers when all α ∈ {2,4} — or τ_max(jkl) < 3τ_min(jkl). The second suffices because τ is a multiple of τ_min that is at most τ_max.

**Conclusion.** No configuration with these data exists.

**Proof.** Translate so that g_v = 1, and put X_j = U_vU_j for j ≠ v. Then μ(X_j) = 2/5, and U_v ⊆ X_j.

**Step 1: μ(X_j∩X_k) = 1/5 for all j ≠ k.**
- (T1) for the edge jk, whose opposite vertex is v, gives α_jk | r_vτ_vjk. Since r_v is odd and α_jk ∈ {2, 4}, this gives α_jk | τ_vjk, so τ_vjk ≥ α_jk.
- By (T3) at apex v, Z_jk := U_v(U_j∩U_k) has μ(Z_jk) = τ_vjk/(5α_jk) ≥ 1/5. Also Z_jk ⊆ X_j∩X_k.
- By L0.5, X_j∩X_k is a union of (U_v, U_j∩U_k)-double cosets. By L0.4 each has μ a multiple of 1/gcd(5r_v, 5r_jr_kα_jk) = 1/(5·gcd(r_v, α_jk)) = 1/5, since r_v is odd and α_jk ∈ {2, 4}.
- By the XE corollary, X_j ≠ X_k. As both have measure 2/5, this gives μ(X_j∩X_k) < 2/5.
- Hence μ(X_j∩X_k) = 1/5, and so Z_jk = X_j∩X_k with μ(Z_jk) = 1/5.

**Step 2: the three Z's of a triple coincide.** Fix a triple j, k, l of vertices other than v, and put W := U_j∩U_k∩U_l.
- Index of W: [G:W] = 5r_jr_kr_lτ_jkl, using the definition of τ.
- Put Q := [G : U_v∩W]. Then Q is a multiple of [G:W] = 5r_jr_k·(r_lτ_jkl) and of T_vjk = 5r_jr_k·(r_vτ_vjk). So it is a multiple of 5r_jr_k·lcm(r_lτ_jkl, r_vτ_vjk).
- **The coprimality step.** The lcm is a multiple of lcm(r_lτ_jkl, r_v). This equals r_lτ_jkl·r_v, because gcd(r_v, r_lτ_jkl) = gcd(r_v, τ_jkl) = 1. Here gcd(r_v, r_l) = 1, and gcd(r_v, τ_jkl) = 1 by (iv).
- Hence Q ≥ 5r_jr_kr_lτ_jkl·r_v = r_v[G:W].
- By the product formula, μ(U_vW) = Q/(5r_v·[G:W]) ≥ 1/5.
- U_vW ⊆ Z_jk ∩ Z_jl ∩ Z_kl, and each Z has measure 1/5. Hence Z_jk = Z_jl = Z_kl = U_vW.

**Step 3: contradiction.**
- Take any two pairs of vertices from V∖{v}. Two pairs that share a vertex lie in a common triple, and two disjoint pairs {j,k}, {l,m} are linked through {j,l}. So all ten sets Z coincide; call the common set Z, with μ(Z) = 1/5.
- For j ≠ k, X_j∩X_k = Z. So the five sets X_j∖Z are pairwise disjoint, each of measure 1/5.
- Hence μ(∪_j X_j) = μ(Z) + 5·(1/5) = 6/5 > 1, a contradiction. ∎

The markers E3 (when v ≠ E3) and E5 play no role in this proof. If E2 is a neighbour j, nothing changes either: only r_v is involved in the granularity, and only gcd(r_v, ·) enters Step 2.

## 4. rules-k6-v3 L12 (RPLP)

**Setting.** Fix v and translate so that g_v = 1. Write N for the five vertices other than v. For j ∈ N put X_j = U_vU_j, Y_j = G∖X_j and D_j = U_vg_jU_j.

**Facts, by rules-k6-v1 L7 (R1–R3, proved in sun-coset5 proof-v4 §5, which uses only pairwise disjointness and holds verbatim for six cosets):**
- D_j ⊆ Y_j.
- μ(D_j) = q_j/5 with an integer q_j satisfying 1 ≤ q_j ≤ 5 − α_vj.
- d_j = q_jr_j.

Each admissible vector q ∈ ∏_j {1, …, 5 − α_vj} is treated separately. The true configuration has exactly one such q, and it is not known which. So the argument must hold for every q.

**Types.**
- Each of X_j, Y_j and D_j is left U_v-invariant, hence a union of right U_v-cosets.
- For a right coset C, its type is (A_C, S_C), where A_C = {j : C ⊆ Y_j} and S_C = {j : C ⊆ D_j}. Since D_j ⊆ Y_j, S_C ⊆ A_C. By L9(b), S_C is hereditary-allowed whenever |S_C| ≥ 2.
- For each type (A, S) with A ≠ ∅, let x(A,S) be the total measure of right cosets of that type, so x(A,S) ≥ 0.
- The cosets with A_C = ∅ are exactly those in ∩_j X_j, and U_v is one of them.

**Forced containments.** Suppose τ_min(v,w,j) ≥ α_vwα_wj.
- (T2) at apex w gives τ ≤ α_vwα_wj, so τ = α_vwα_wj.
- (T3) at apex v gives μ(U_v(U_w∩U_j)) = τ/(5α_wj) = α_vw/5 = μ(X_w).
- Hence X_w = U_v(U_w∩U_j) ⊆ X_j, that is, Y_j ⊆ Y_w.
- So every type with j ∈ A and w ∉ A has x = 0. The engine omits those columns, which is valid.

**Constraints satisfied by x.**
- **(E1_j)** Σ_{(A,S): j∈S} x(A,S) = μ(D_j) = q_j/5.
- **(E2_j)** Σ_{(A,S): j∈A} x(A,S) = μ(Y_j) = (5 − α_vj)/5.
- **(B_jk)** ylo_jk ≤ Σ_{(A,S): j,k∈A} x(A,S) = μ(Y_j∩Y_k) ≤ yhi_jk.
  - μ(Y_j∩Y_k) = 1 − μ(X_j) − μ(X_k) + μ(X_j∩X_k).
  - lo_jk ≤ μ(X_j∩X_k) ≤ hi_jk, by rules-k6-v1 L4. Those bounds hold for every admissible τ (M1) and every instance (M2).
- **(TOT)** Σ x(A,S) = μ(∪_j Y_j) ≤ 1 − μ(U_v) < 1.

**The LP and its dual.** Let OPT(q) be the minimum of Σ x over all x ≥ 0 on allowed columns that satisfy E1, E2 and B. The true x is feasible, so OPT(q) ≤ μ(∪_j Y_j) < 1. If the system is infeasible, there is a contradiction straight away.

Let a_j, b_j be free rationals and u_jk, l_jk ≥ 0. Suppose that for every allowed column (A,S),
- Σ_{j∈S} a_j + Σ_{j∈A} b_j − Σ_{j<k, j,k∈A} u_jk + Σ_{j<k, j,k∈A} l_jk ≤ 1. ……(★)

**Weak duality.** For any feasible x:
- Σ x ≥ Σ_{(A,S)} x(A,S)·[Σ_{j∈S} a_j + Σ_{j∈A} b_j − Σ_{j,k∈A} u_jk + Σ_{j,k∈A} l_jk], using (★) and x ≥ 0.
- Regrouping the right side by constraint gives Σ_j a_j·(q_j/5) + Σ_j b_j·(5 − α_vj)/5 − Σ u_jk·μ(Y_j∩Y_k) + Σ l_jk·μ(Y_j∩Y_k).
- Since u_jk ≥ 0 and l_jk ≥ 0, this is ≥ Σ_j a_jq_j/5 + Σ_j b_j(5 − α_vj)/5 − Σ u_jk·yhi_jk + Σ l_jk·ylo_jk =: Obj.

So if Obj ≥ 1, then Σ x ≥ 1 for every feasible x, contradicting (TOT).

**Farkas case.** If the primal system has no solution, a dual direction exists with (★) holding with right-hand side 0 and positive objective. Scaling it so that Obj = 1 satisfies (★) with right-hand side 0 ≤ 1. So the same check (★) together with Obj ≥ 1 certifies this case as well.

**Exactness.** All entries are rationals: q_j/5, (5 − α_vj)/5, lo, hi, and the dual entries. The certificate is checked in exact rational arithmetic.

**Conclusion.** If, for **every** admissible q at v, there is either
- an RLP certificate (rules-k6-v1 L7 dual y with value ≥ 1), or
- a vector (a, b, u, l) satisfying (★) on all allowed columns with Obj ≥ 1,

then vertex v admits no configuration, so the pattern is impossible. ∎

The hereditary-allowed test is applied with maxgcd. That is exact, or at least safe, as shown in §1.
