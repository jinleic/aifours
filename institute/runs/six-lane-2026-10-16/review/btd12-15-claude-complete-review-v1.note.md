VERDICT: ACCEPT

## Fatal findings
None.

## Major findings
None.

## Minor findings
These are editorial. None of them affects validity.

1. **Step 8(iii), parenthetical.** "The 2×2 conditions … alone would not suffice" is true only for a symmetric matrix not known to be PSD.
   - The same bullet has already shown Y ⪰ 0.
   - For a PSD matrix, vanishing 2×2 principal minors do force rank ≤ 1: the Gram vectors are pairwise parallel by Cauchy–Schwarz equality.
   - Reword it or drop it.
2. **Step 8(i).** Add "for k ∉ {a,b}". For k ∈ {a,b}, Y_kk = 0 follows from 8(iii).
3. **Step 9, size-4 bullet.** Where the extra t=1 and the two t=−1 values sit is asserted, not argued. It is correct, but add one line:
   - A type-2 column l ≠ j has t_l ∈ {0,1}.
   - t_l = 1 means H_jl = 4, which by Step 5 means l is a classmate of j.
   - All three classmates are already counted, so the extra 1 and both −1s lie on non-type-2 columns.
   - Also say explicitly that Step 4 is applied at j = a and j = b. This is harmless, since H-columns are constant on classes.
4. **Step 11.**
   - The bilinear form F_kl = (4p_k1p_l1 + p_k1p_l2 + p_k2p_l1 + 4p_k2p_l2)/15 is used but never displayed; only the quadratic form appears, in Step 10.
   - The finitary variant should display det H[{a,b,k,l}] = 15(Y_kk·Y_ll − Y_kl²).
   - For l ∈ {a,b}, Y_kl = 0 comes from 8(iii), not from a 4×4 minor.
5. **Header.** The SHA-256, `code/proof_check.py` and its "exhaustive enumeration" claim were not checked (no tools). The verdict does not rely on them. The bibliographic and open-status context was also not checked, and novelty was not assessed.

## Recommended simplification (also an independent cross-check of Steps 8–11)
After Step 7, take a ∈ A, b ∈ B and any type-1 column k. One exists because n₁ = 24 − 2n₂ ∈ {4, 6}.

- Step 2(b) gives x = H_ka with x² ≤ 56, and x ≡ −1 (mod 5), so x ∈ {−6, −1, 4}. The same holds for y = H_kb.
- Direct expansion gives det H[{a,b,k}] = 210 − (4x² + 2xy + 4y²).
- Over these x, y the value is −150, 50, 150 or 200, and none of these is a nonnegative square. This contradicts Lemma D.
- So Steps 8–11, including the Step 9 pattern analysis, can be replaced by three lines. This route reaches the same conclusion as Steps 10–11 independently.

## What I verified by hand

- **Setting.** VR = BK = 120. Also λ(V−1) = 66 = ρ₁(K−1) + 2ρ₂(K−2) = 42 + 24.

- **Step 1.**
  - Row norm² is 14 and off-diagonal inner products are 6, so MM^T = 8I + 6J.
  - G**1** = 80·**1**.
  - G² = 8G + 6(8·**1**)(8·**1**)^T = 8G + 384J.
  - Expanding H² gives 1600I − 200G + (9600 + 8640 + 1920 − 19200)J = 40H.
  - H**1** = (40 − 400 + 360)**1** = 0.
  - G_jj = (8 − 2c_j) + 4c_j, so H_jj = 24 − 10c_j.
  - H_jk ≡ −1 (mod 5).
  - trace H = 360 − 240 = 120.
  - Spectral cross-check: G has eigenvalues 80 (on **1**), 8 (×11) and 0 (×3). So H = 40·Π_{ker M}, giving rank 3 and trace 120.

- **Step 2.** PSD via x^T H x = |Hx|²/40. H/40 is idempotent, so rank = trace = 3. c_j ≤ 2. The 2×2 bounds hold, and all 4×4 minors vanish.

- **Step 3.** (n₀, n₁, n₂) ∈ {(0,6,9), (1,4,10), (2,2,11), (3,0,12)}. The cases 11 and 12 are later killed by Step 7.

- **Step 4.**
  - Σt = 2 and Σt² = 6, using 5Σt − 14 = −4 and 25Σt² − 20 + 14 = 144.
  - Write a for the number of ±2 entries and b for the number of ±1 entries. Then 4a + b = 6, and the only solutions are {1⁴, (−1)²} and {2, 1, −1}.
  - Hence at most four t = 1, and every class has at most 5 columns.

- **Step 5.**
  - H_jk ∈ {−1, 4}.
  - H_jk = 4 gives (e_j − e_k)^T H (e_j − e_k) = 0, so columns j and k of H are equal.
  - Transitivity holds, and H = −1 across classes.

- **Step 6.**
  - (8I + 6J)(I − 3J/40) = 8I + (6 − 0.6 − 5.4)J = 8I, which confirms A⁻¹.
  - det A = 80·8¹¹ = 2³⁷·5.
  - P^T A⁻¹ P = (P^T P − (24/5)J)/8, so I − P^T A⁻¹ P = H[S]/40.
  - Hence det(N)² = 5·2³⁷·det H[S]/(2⁹·5³) = 2²⁸·det H[S]/25.
  - This agrees with the complementary-minor identity det Π[S] = det(M_{S^c})²/det(MM^T).

- **Step 7.** det(5I − J₃) = 5²·2 = 50, which would force det(N)² = 2²⁹, impossible. So there are exactly two classes, with sizes in {4, 5} and n₂ ∈ {9, 10}.

- **Step 8.**
  - Γ⁻¹ is correct, and det H[{a,b,k}] = 15·Y_kk.
  - Σ_k p_k p_kᵀ = 40Γ, so ΣF = tr(40·I₂) = 80 and ΣY = 40.
  - Y ⪰ 0 via z: the cross terms reduce using E^T H E = Γ and HE = P.
  - Guttman rank additivity gives rank Y = 1.
  - P^T **1** = 0, so Y**1** = 0.
  - For type-2 columns, F = (64 − 8 + 4)/15 = 4.

- **Step 9.**
  - Row a, with n₂ = 9: entries sum to 4 + 16 − 4 − 16 = 0, and squares sum to 16 + 64 + 4 + 76 = 160.
  - Row b: entries sum to 4 + 12 − 5 + (4 − 12 − 3) = 0, and squares sum to 16 + 48 + 5 + 91 = 160.
  - The patterns are forced as stated. In particular, the extra t=1 cannot lie on a type-2 column (see minor finding 3).

- **Step 10.**
  - F values are 10/15, 160/15 and 360/15.
  - Let m be the number of (−6,−6) columns, m ∈ {0, 1, 2}. The F-sums are 130/3, 140/3 and 150/3, all different from 120/3.
  - The type-0 column is irrelevant: the test depends only on the p_k and on Σ H_kk = 56 + 24 = 80. The (−6,−6) patterns are included.
  - Cross-check via the off-diagonal entry of (ii): Σ_k H_ka H_kb = −40. The type-2 columns contribute −40, so Σ p_A p_B over the non-type-2 columns would have to be 0. Every term is positive, so this is impossible.

- **Step 11.**
  - F values: (−1,4) gives 60/15 = 4 and (−6,4) gives 160/15. (−6,−6) is excluded because n₀ = 0 and Y ≥ 0.
  - Case I gives F-sum 142/3. Case II gives 132/3.
  - Cross-check: the type-2 part of (ii) is −36, so Σ p_A p_B over type-1 columns must be −4. Case I gives 21; Case II gives −4.
  - Case II values: Y = 10/3 (four columns) and 40/3 (two columns).
  - H₅₆ = 2/3 ± 40/3, which forces s₅ = s₆.
  - The sign sum then forces s₁ = s₂ = s₃ = s₄ = −s₅.
  - F₁₂ = 110/15 = 22/3, so H₁₂ = 32/3, which is not an integer.
  - Finitary variant: F₁₅ = 10/15, giving H₁₅ = −6. F₂₅ = F₃₅ = F₄₅ = 35/15, giving H = 9 in each case. F₅₆ = 2/3, giving H₅₆ = 14. Row k₅ of Y then sums to 120/3 = 40 ≠ 0.

- **Hidden assumptions.**
  - Simplicity, distinct columns and cyclicity are never used.
  - Column order matters only in M = [N | P], and det² is permutation-invariant.
  - "Names chosen" in Step 11 is valid because Γ and F are symmetric under swapping coordinates.
  - The choice of representatives a, b is immaterial, because H-columns are constant on each class.
