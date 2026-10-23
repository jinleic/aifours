VERDICT: ACCEPT

I found no flaw in Claim B or in the distribution/guessing-number equivalence. The guard-replacement wording you asked for is at the end; it is a scope statement, not a correction to the proof.

**Checks I did myself, beyond what you allowed me to assume**
- All ten triples are cliques of the listed edge set. Each vertex lies in exactly three of them, so both the rows and the columns of B sum to 3.
- B is nonsingular over Q, checked without the inverse witness. Suppose z_a+z_b+z_c=0 on every triangle.
  - The pairs (123, 239), (145, 4·5·10) and (167, 678) force z9 = z10 = z8 = z1 = a.
  - The remaining triangles then force z = a(1,1,−2,−2,1,1,−2,1,1,1).
  - Triangle 569 then gives 3a = 0.
  - So B is singular only mod 3, which does not matter here. Hence B⁻¹1 = (1/3)1 > 0, and 1 lies in the interior of the cone B·R¹⁰₊.

**Claim B, point by point**
1. **Arbitrary finite alphabets: correct.** Only sizes enter.
   - Define S(C) = 3log|C| − 2Σ log|proj_v C|. S is additive under products, because the projection of a product is the product of the projections.
   - S(K_T(q)) = 6log q − 6log q = 0, so S(P) = kg exactly.
   - Injective relabelling into [s] keeps every FD and every row.
2. **Non-vertex-transitivity: correct.** Vertices 1 and 8 have degree 6, the rest degree 5. No automorphism is used; only B invertible with B⁻¹1 > 0 is needed.
3. **Exact products and floor rounding: correct.**
   - log₂M_v = kα_v + (Be)_v = L − (Br)_v.
   - (Br)_v ∈ [0,3) because B is 0/1 with three ones per row.
   - The identity 3log|P| − 20log s = kg − 2Σδ_v also uses Σ_v (Be)_v = 3Σ e_T, i.e. column sums of 3, which hold.
   - e_T = 0 gives the one-word code K_T(1), which is harmless.
4. **Integer common alphabet: correct.** s = max M_v is an integer with log₂s ∈ (L−3, L], so δ_v ∈ [0,3). Also s ≥ 2 automatically, since |P| ≥ 2.
5. **Sup versus limit: harmless.** If s^m ≤ t < s^{m+1}, then C^m ⊆ [s^m]¹⁰ ⊆ [t]¹⁰ gives gn(G,t) ≥ (m/(m+1))·log_s|C|. So lim_t gn(G,t) exists and equals sup_s gn(G,s), and the conclusion holds under either convention.

**Type-class bridge: valid**
- A finite law obeys the FDs exactly when its support is FD-consistent. Perturbing to positive rationals on the same support keeps the FDs, and Φ < 0 survives by continuity.
- The type-class code C_n ⊆ ∏_v A_vⁿ is FD-consistent coordinatewise. Its sizes satisfy:
  - log|C_n| ≥ nH(X_V) − |S|·log(n+1);
  - proj_v C_n is exactly the marginal type class (by permutation), of size ≤ 2^{nH(X_v)}.
- Therefore 3log|C_n| − 2Σ log|proj_v C_n| ≥ −nΦ − 3|S|·log(n+1) > 0 for large n. Claim B applies because it is stated for arbitrary finite alphabets, which this step needs.
- The converse (uniform law on a common-alphabet code) is correct, and so is the 20/3 lower anchor.

**Edge cases: none break the argument**
- Equality |C|³ = ∏|A_v|² (g = 0) certifies nothing. The triangle product itself is an equality case (Φ = 0), so the test must be strict.
- Constant coordinates (α_v = 0), q_T = 1, and |C| ≤ 1 are all harmless; |C| ≤ 1 cannot satisfy the hypothesis.
- No hidden hypotheses are used beyond the three verified ones: cliques, 3-regular incidence, and nonsingular B. The result is conditional on the edge transcription, which is out of scope.

**Required wording before replacing the max-alphabet guard with the aggregate test**

> For this transcribed graph only (the ten listed triangles are cliques, each vertex lies in exactly three, and the incidence matrix is nonsingular): let C ⊆ ∏_v A_v be a finite code satisfying every FD N(v)→v, with A_v its exact column projections. If the exact integer inequality |C|³ > ∏_{v=1}^{10} |A_v|² holds strictly, then gn(G) > 20/3 by Claim B.
>
> Acceptance certifies strict exceedance of 20/3 only. It does not assert that C, or C padded to max_v|A_v|, is a strategy beating 20/3. The guaranteed witness is C^k × ∏_T K_T(2^{e_T}) on the alphabet s = max_v |A_v|^k·2^{(Be)_v}. Taking k > 60/g suffices, so s may be astronomically large.
>
> An explicitly built witness counts only after |P|³ > s²⁰ is checked in exact integers. Only log_s|P| of such a witness may be reported as an achieved rate. The aggregate ratio 10·log|C| / Σ log|A_v| is not certified as an achieved guessing number.

Notes on the replacement:
- The old guard implies the new test, since ∏|A_v|² ≤ (max|A_v|)²⁰. No previously accepted candidate is lost; the extra acceptances rest entirely on Claim B.
- Using declared alphabets instead of exact projections remains sound, only more conservative.
- The test does not transfer to other graphs without their own balancing lemma.
