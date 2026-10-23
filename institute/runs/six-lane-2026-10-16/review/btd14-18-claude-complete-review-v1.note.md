VERDICT: ACCEPT

Scope: I judged only the mathematics at L13–L110. I have not seen or run `code/proof_check.py` (L10) or checked the SHA. The proof does not depend on either, and I re-derived every number below by hand. L14–L15 match the stated target. The BTD label at L1 and L105 is not assessed.

**Fatal:** none.

**Major:** none.

**Minor (editorial; none affects validity):**
1. **L27:** `g_jk` is never defined; it must mean G_jk.
2. **L57:** `M = [N | P]` holds only after a column permutation. This is harmless, because the proof only uses MM^T = NN^T + PP^T, which does not depend on column order.
3. **L16, L22, L58, L62:** J and **1** silently change size (18, 14, 4). For example, in L62 the J inside P^TJP is 14×14 and the J in 49J is 4×4. Context makes each one unambiguous.
4. **L56:** the heading is loose. What L65 actually proves is 729·det(N)² = 7¹⁰·det H[S]. This forces 7⁵ | det N and det H[S] = (27·det N/7⁵)², an exact square.
5. **L64:** two things should be stated explicitly here:
   - the lemma used is the rank-4 (Sylvester) form det(A − PP^T) = det A · det(I₄ − P^TA⁻¹P), valid because A is invertible;
   - det(NN^T) = det(N)² because N is square, which currently appears only at L109.

**Independent derivation**

1. **Identities.**
   - MM^T = 11I + 4(J − I) = 7I + 4J =: A.
   - Row sums 9 and column sums 7 give GJ = JG = 63J and G² = M^TAM = 7G + 196J.
   - Expanding (63I − 9G + 28J)² with J² = 18J gives coefficients 3969 on I, 81·7 − 2·63·9 = −567 on G, and 15876 + 14112 + 3528 − 31752 = 1764 = 63·28 on J. So H² = 63H.
   - H**1** = (63 − 567 + 504)**1** = 0, and G_jj = (7 − 2c_j) + 4c_j.
   - Mod 9, H ≡ J entrywise, so every entry of H, including the diagonal, is ≡ 1 (mod 9).

2. **Positivity.** For all real x, y, 63·x^THy = (Hx)·(Hy) because H is symmetric. Taking y = x gives P1 and P2; Cauchy–Schwarz divided by 63² gives P3. Restricting to integer vectors (L30) is valid but unnecessary.

3. **Column types.** 28 − 18c_j ≥ 0 gives c_j ≤ 1, and Σc_j = 14 gives the 14/4 split.

4. **Entries next to a type-1 column a.**
   - For k ≠ a, H_ak² ≤ 280, so |H_ak| ≤ 16, which leaves H_ak ∈ {−8, 1, 10}.
   - Over k ≠ a the counts satisfy n₁₀ + n₁ + n₋₈ = 17, 10n₁₀ + n₁ − 8n₋₈ = −10, and 100n₁₀ + n₁ + 64n₋₈ = 530. This is a Vandermonde system with unique solution (2, 10, 5).
   - Check in G terms (g = 2, 3, 4): Σg = 54 = 63 − 9 and Σg² = 178 = 259 − 81.
   - If columns j ≠ k of M were identical, H_jk = −35 − 18c_j would violate P3. The proof never assumes distinct columns; every argument is index-based.

5. **(E) and (F).**
   - (E): the quadratic form of e_a − e_k is 10 + 10 − 20 = 0, so He_a = He_k.
   - (F): the form of 2e_a + e_k + e_l is 40 + 10 + 10 − 64 + 2H_kl = 2H_kl − 4 ≥ 0. Since H_kl ∈ {−8, 1, 10}, H_kl = 10.

6. **Lemma D4.**
   - (7I + 4J)(I − 4J/63) = 7I + (4 − 28/63 − 224/63)J = 7I, so the stated inverse is correct.
   - The eigenvalues are 7 (13 times) and 63, so det A = 7¹⁴·3².
   - P^TJP = 49J₄ gives I₄ − P^TA⁻¹P = I₄ − P^TP/7 + (4/9)J₄ = H[S]/63.
   - Hence det(N)² = 7¹⁴·3²·det H[S]/(7⁴·3⁸) = 7¹⁰·det H[S]/729. The coefficient is correct.
   - Second route: the same algebra on all 18 columns gives H/63 = I − M^TA⁻¹M, the projector complementary to Q = M^TA⁻¹M. Jacobi's complementary-minor theorem, applied to an orthogonal matrix built from bases of the two ranges, gives det(H[S]/63) = det Q[S^c] = det(N)²/det A. This is the same identity.

7. **Closure.**
   - **Choice of b.** Row a has five entries −8, and at most four of them can be in type-0 columns, so some type-1 b has H_ab = −8.
   - **(i)** Take type-1 c ∉ {a, b}.
     - If H_ca = 10, (E) on (a, c) read at row b gives H_cb = −8. The case H_cb = 10 is symmetric.
     - Otherwise both entries lie in {−8, 1}. H_ca = −8 lets (F) at a, with the distinct type-1 columns b and c, force H_bc = 10, a contradiction. H_cb = −8 is handled by (F) at b.
     - All 9 pairs are covered, and the survivors (10, −8), (−8, 10), (1, 1) all sum to 2. The cases c = a and c = b also sum to 2.
   - **(ii)** Each of {k : H_ak = 10} and {k : H_bk = 10} has exactly 3 elements, so at least 8 type-1 columns u avoid both. Such a u differs from a and b, and a sum of 2 with both entries in {−8, 1} forces (1, 1).
   - **(iii)** The form of e_a + e_b is 4, so (H_ca + H_cb)² ≤ 4·28 = 112. The possible sums −16, −7, 2, 11, 20 have squares 256, 49, 4, 121, 400, leaving only −7 and 2.
   - **(iv)** A sum of −7 means x + y = −7 and xy = −8.
     - Let B = H[{a, b, u}]. Then det B = 324 and adj B = [[99, 81, −18], [81, 99, −18], [−18, −18, 36]]; I checked B·adj B = 324I.
     - The bordered determinant is det H[S] = 9072 − (99·65 − 1296 + 252w + 36w²) = 3933 − 36w(w + 7).
     - This gives 3645 for w = −8 and w = 1 (both have w(w + 7) = 8) and −2187 for w = 10.
     - Row reduction, pivoting on the u-row, independently confirms the three (−8, 1, w) cases. The (1, −8, w) cases follow because swapping a and b leaves the rest of H[S] fixed. All six table entries are correct.
     - For 3645 = 3⁶·5, cancelling 729 ≠ 0 leaves d² = 5·7¹⁰ ≡ 2 (mod 3), which is impossible.
     - −2187 = −3⁷ < 0 is impossible as well, already by positive semidefiniteness. The integrality of det N is genuinely needed only for 3645.
   - **(v)** Σ_c H_ca = (H**1**)_a = 0, but 18 sums of 2 give 36. As a check, m type-0 columns with sum −7 would give a total of 36 − 9m, which requires m = 4, and (iv) excludes that.

**Assumptions:** the proof uses no column simplicity, rank, geometry or symmetry of M. It uses only H^T = H and the a ↔ b role swap. The swap is legitimate because a and b are both type-1, H_ab = H_ba, and H_ua = H_ub = 1.
