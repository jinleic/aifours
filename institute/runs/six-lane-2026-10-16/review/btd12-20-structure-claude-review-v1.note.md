VERDICT (STRUCTURAL REDUCTION ONLY): ACCEPT-WITH-FIXES

Scope: this review covers the text of Parts A–D only. I did not verify code, nauty or orbit output, hashes, CP-SAT runs, or nonexistence. A model review is not a proof.

**Fatal:** none. **Major:** none. Parts A–C and the Part D predicate are mathematically correct. The fixes below are editorial or documentation.

**Minor findings**
1. **L58–60.** "The seven L + {y}" reads as one fixed line L. It should be the seven L′+{y}, with L′ ranging over all Fano lines. That is true because L + e7 = {lines} ∪ {X} (D2).
2. **L51–52, L63.**
   - State that T, T1, T2 are independent: all seven listed sums are nonzero.
   - Include the Fano check (D2).
   - State that X = T∪T1∪T2, and that y lies in the member that introduced it.
3. **L65–66 vs L101–102.** L65–66 says the code facts "are re-checked"; L101–102 says Part E has not run. Fix the tense. D2 settles these facts by hand anyway.
4. **L69–74, L88–90.**
   - State that for |F| ≥ 2, (d) holds exactly when all splits are consistent. So e-type components are exactly the Step-3 ones, and their span is exactly e7 or e8. That is what makes the reduction modulo Aut(e7)/Aut(e8) lossless.
   - State that the e8 list over-includes full-support multisets that are not genuine e-components. Example: {P, Pᶜ, Q, Qᶜ}, two non-parallel planes and their complements, is d-type (a 4-cycle).
   - So E0 and E1 overlap. This is harmless, but 3073 is not a count of A-classes.
5. **L80–81.** Say that e-components are column-disjoint from each other and from the multigraph, and that two same-type components form an unordered pair. How `e_combos.py` handles this is undocumented.
6. **L83–84.** `lo` is never given. Completeness needs:
   - lo ≤ ⌈n/2⌉; for n = 10 a perfect matching with multiplicities 4,2,2,2,2 is admissible;
   - no multiplicity cap below 6; for n = 4 a matching with multiplicities 6,6 is admissible.

   Record the values actually used. The reported counts 7 and 173 (D5) are consistent with both conditions.
7. **L90.** Break the 204 down by type (e7/e8) and by r.
8. **L76.** "Free" columns are not free: Part D forces d_j = 3 there.
9. **L98, L104.** The predicate is invariant only under Aut(A). Any symmetry breaking in `restricted_batch.py` or the CNFs (lex order, swaps within a column pair, zero-column order) must be justified by Aut(A). Part E should state that none is used, or justify each instance.

**Independent derivations**

**D1 (Part A).**
- M_i·M_k = |A_i∩A_k| + 2(|A_i∩D_k| + |D_i∩A_k|) + 4|D_i∩D_k|. So |A_i∩A_k| is even, i.e. in {0,2,4}.
- a_j = 6 − 2d_j ∈ {0,2,4,6}.
- L21–25 is correct.

**D2 (code facts, from scratch, length 7 and 8 only).**
- **Seed.** Over (1,2,3,4,a,b,d) the generators are T = 1111000, T1 = 1100110, T2 = 1010101. The columns are the 7 distinct nonzero vectors of F₂³, so e7 is the simplex code. For u ≠ 0, wt(uG) = #{v ≠ 0 : u·v = 1} = 4.
- **Hamming dual.** Distinct words meet in (4+4−4)/2 = 2 points, so e7 ⊆ e7^⊥ =: H, which has dimension 4. All e7 weights are even, so 1_X ∈ H. Counting 16 words gives H = e7 ∪ (1+e7).
  - Weights of H: 0, 4 (×7), 7, 3 (×7).
  - So H's weight-4 words are exactly the seven e7 tetrads.
  - The weight-3 words pairwise share at most 1 point (minimum distance 3) and cover 7·3 = 21 = C(7,2) pairs, so they are the lines of a Fano plane.
- **Extension to e8.** A weight-3 L lies in 1+e7, so L + e7 = {7 lines, X}.
  - e7 ⊕ ⟨L+y⟩ = {0, the 7 e7 tetrads, the 7 L′+y, X+y}, with weights 0, 4 (×14), 8. This does not depend on which L is used.
  - All weights are ≡ 0 mod 4, so all intersections are even and the code is self-orthogonal. Dimension 4 = 8/2, so it is self-dual.
- **Duals are local.** Duals are taken in F₂^X or F₂^{X+y}. This is legitimate because ⟨T′,w⟩ = ⟨T′∩X, w⟩ for w supported on X.
- **No outside assumptions.** No self-duality of the 20-column row code and no length-24 theorem is used. The orders 168 and 1344 equal |GL(3,2)| and |AGL(3,2)|.

**D3 (Lemma T).**
- **Step 2.** With consistent splits, adjacent T, T′ have parts {T∩T′, T∖T′} and {T∩T′, T′∖T}; these are pairwise equal or disjoint. Non-adjacent members are disjoint. So the parts partition S. Conversely, (d) forces consistent splits, because T∩T′ must be a shared pair. Hence Step 3 excludes (d).
- **Step 3.**
  - Parts of different splits meet in one point, and T1 ≠ T2.
  - 2 ∉ T2, 3 ∉ T1, 4 ∉ T1∪T2, and |T1∩T2| = 2.
  - So T1 = {1,2,a,b}, T2 = {1,3,a,d} with b ≠ d: seven distinct points.
  - All seven sums in L50–51 are correct.
- **Step 4.** The BFS order is valid because {T,T1,T2} is connected. T′ is orthogonal to span(G).
  - **e7 case:** |T′∩X| ∈ {0,3,4,7} ∩ [2,4] = {3,4}. So T′ is an e7 tetrad, or T′ = L+y and the span becomes e8.
  - **e8 case:** |T′∩(X+y)| ∈ {0,4,8} ∩ [2,4] = {4}. So T′ ⊆ X+y is an e8 tetrad, and a second new point is impossible.

  Lemma T is correct as stated.

**D4 (Part C completeness).**
- **Components.** Non-adjacent distinct tetrads meet in 0 points, so components have disjoint supports.
- **d-type.** Each vertex is a pair and each row is an edge. The graph is loopless (two distinct pairs per edge) and repeated rows become parallel edges. Both columns of a vertex have a_j equal to the degree, which lies in {2,4,6}.
- **e-type.** Support is full (7 or 8 columns) and degrees lie in {2,4,6}. A full-support e7 multiset spans e7, since any family of dimension ≤ 2 covers at most 6 points. Three e-components would need ≥ 21 columns.
- **Zero columns.** The remaining columns are zero columns of A (d_j = 3).
- **Invariants.** Up to row/column permutation, A is determined by:
  - the multigraph's isomorphism class;
  - the multiset of e-orbits;
  - the number of zero columns.

  Each such datum lies in E0 (with 6n ≥ 24 and 2n ≤ 20, so n = 4..10) or in E1.
- **Conclusion:** E0 ∪ E1 is complete as a mathematical description. Whether the files realise it is unverified.

**D5 (spot counts by hand; not file verification).**
- **Sums.** 7+59+312+550+616+352+173 = 2069, and 2069 + 1004 = 3073.
- **n = 4.** All degrees must be 6, forcing m12 = m34 = x, m13 = m24 = y, m14 = m23 = z with x+y+z = 6. S4 acts as S3 on the three matchings. The count is the number of partitions of 6 into ≤ 3 parts, which is 7. This matches.
- **n = 10.** The degree types are (6,2⁹) and (4,4,2⁸). Let q(N) be the number of partitions of N into parts ≥ 2 (cycles, digons included). The cases are:
  - a 3-petal flower plus cycles: Σ p₃(K)·q(9−K) = 24;
  - a theta with 4 threads: Σ p≤4(S)·q(8−S) = 65;
  - 2 threads plus one petal at each end: 70;
  - two 2-petal flowers: 14.

  The total, 173, matches.
- **Not checked:** 59, 312, 550, 616, 352, 204, 1004.

**D6 (Part D is exact).**
- **Row and column conditions.** With D supported off A, M = A + 2D has entries in {0,1,2} and its 1-pattern is exactly A.
  - Row sums 3 give exactly three 2s per row.
  - (6 − a_j)/2 is equivalent to a_j + 2d_j = 6, and it is integral because a_j is even.
- **Pair equation.** It is the expanded inner product; i < k suffices by symmetry. With x = |A_i∩D_k| + |D_i∩A_k| and y = |D_i∩D_k|, the solutions are:
  - |A_i∩A_k| = 4: (x,y) = (0,0);
  - |A_i∩A_k| = 2: (1,0);
  - |A_i∩A_k| = 0: (2,0) or (0,1).
- **No hidden conditions.** No distinct-column, simplicity, orbit or ordering condition appears in the text. Repeated M-rows are impossible anyway, since M_i·M_i = 16.
- L96–97 is exactly the BTD constraint. The implementation is unverified.
