# Erratum and addendum to `rank6-112-coset-projection-L8-exclusion-v1.md`: a corrected s = 6 row, the general zero count, a signed identity, and L = 10 excluded at (3,112), so L ≥ 12

Owner **InfoBalancedNL242-2**, slot info-6. Actual `/bin/date` observation BEFORE this write: **Tue Oct 27 07:24:09 PDT 2026**.

**Target, left IMMUTABLE:** `rank6-112-coset-projection-L8-exclusion-v1.md`, SHA `7b533fa53c325cf48209ed425441c678ea1d2d40aa23ef3d388a34be0d8e3ed7`.

**NEW WRITTEN AUTHOR CANDIDATE.** It is unreviewed, with no machine check and no formal or novelty claim. No program was run; all arithmetic was done by hand.

## 1. Erratum (OWN, MINOR; the conclusion is unchanged)

In the table of §2 of the target, the **s = 6 row is wrong**. For six ±1 terms, Σz ≡ 0 (mod 3) holds for the 3–3 splits AND for the 6–0 splits (Σz = ±6). The row omitted the 6–0 case.

The correct row is:

- indicator (11 − e_2 + 3e_4 − 9e_6)/32;
- **N_0 = 22 + 6A_4 − 18A_6**.

Consequences in the target's Theorem R:

- If ΣΣ = 0, then A_4 = 0 and N_0 = 22 − 18G ≤ 40.
- If ΣΣ ≠ 0, then A_6 = 0, A_4 ≤ 3 and N_0 ≤ 40.

So the bound "N_0 ≤ 40" used there still holds, and **Theorem R (L ≤ 8 impossible at (3,112)) stands unchanged**.

The other rows are correct:

- s = 4: only the 2–2 split, since ±4 ≢ 0.
- s = 5: only 4–1.
- s = 7: only 5–2.
- s = 8: 4–4 and 7–1 were both included.

Each row is reproduced by the general formula below.

## 2. General zero count and expansion (ordinary algebra, by hand)

For z ∈ {±1}^s, 1[Σz ≡ 0 (mod 3)] = (1 + 2 Re ω^{Σz})/3. Use ω^{z} = −1/2 + (i√3/2)z and expand the product. On F_2^6, with A_0 = 1 and A_2 = 0, this gives

```
N_0 = (64/3)·[ 1 + (−1)^s 2^{1−s} Σ_{k even} (−3)^{k/2} A_k ],
```

where A_k = Σ g(T) over the zero-sum k-subsets T ⊆ Σ.

Checks:

| s | N_0 |
|---|---|
| 4 | 24 + 24A_4 |
| 5 | 20 − 12A_4 |
| 6 | 22 + 6A_4 − 18A_6 |
| 7 | 21 − 3A_4 + 9A_6 |
| 8 | (43 + 3A_4 − 9A_6 + 27A_8)/2 |
| 9 | (255 − 9A_4 + 27A_6 − 81A_8)/12 |
| 10 | (513 + 9A_4 − 27A_6 + 81A_8 − 243A_10)/24 |

Similarly φ(t) = (ω^t − ω^{−t})/(i√3) is the centred residue. Expanding it gives

```
φ(Σz) = 2^{1−s} Σ_{|T| odd} (−1)^{s−|T|} (−3)^{(|T|−1)/2} z^T.
```

This reproduces s = 4: (−e_1 + 3e_3)/8, and s = 5: (e_1 − 3e_3 + 9e_5)/16.

## 3. Signed identity (exact)

On U = V^⊥, h_0 = φ(Σz) as a {0, ±1}-function, and Σ_ξ (−1)^{v·ξ}σ(ξ) = 8c_v. Hence

```
Ξ := Σ_ξ h_0(ξ)σ(ξ) = ν − α = 2^{4−s} Σ_{|T| odd} (−1)^{s−|T|} (−3)^{(|T|−1)/2} g(T) c_{ΣT}.
```

At d = 112, S0017 (11) gives α + 2ν = (3wt(h_0) + Ξ)/2. Therefore

```
3·wt(h_0) + Ξ = 60 − 2L − u.                                     (★)
```

**Flat case.** If Σ is a 2-flat with G = +1, then h_0 is nonzero only on a coset K of W^0 with |K| = 16, where it equals z_1. Summing characters over K gives **Ξ = 2Σ_j g_j c_j ∈ [−8, 8]**.

## 4. Theorem R′ (L = 10 is impossible at (3,112); hence L ≥ 12)

*Proof.* At L = 10, wt(h_0) ≤ α + 2ν = 20 − u/2 ≤ 18, so N_0 ≥ 46. Also |P| ≥ 6 and dim aff(P) ≥ 5 (Theorem O(b)), and |Σ| + 2|P∖Σ| ≤ 10. The admissible pairs are:

- |P∖Σ| = 0, with s ∈ [6, 10];
- |P∖Σ| = 1, with s ∈ [5, 8];
- |P∖Σ| = 2, with s ∈ [4, 6];
- |P∖Σ| = 3, with s ∈ {3, 4};
- |P∖Σ| = 4, with s = 2.

Each case:

- **s = 2, 3:** N_0 = 32 or 16 < 46.
- **s = 5, 6, 7:** N_0 ≤ 32, 40, 42 (target §3 and the corrected row) < 46.
- **s = 4:** N_0 ≥ 46 forces a flat with G = +1 (N_0 = 48, wt = 16).
  - With |P∖Σ| = 2, dim aff(P) ≤ 4. Impossible.
  - With |P∖Σ| = 3, (★) gives 48 + Ξ = 40 − u ≤ 36, so Ξ ≤ −12, contradicting |Ξ| ≤ 8.
  - In general (★) excludes this flat whenever L + u/2 ≥ 12.
- **s = 8, needing 3A_4 − 9A_6 + 27A_8 ≥ 49:**
  - dim aff(Σ) = 3 means Σ is a 3-flat, so dim aff(P) ≤ 4. Impossible.
  - dim aff(Σ) ≥ 5 leaves at most 3 relations, so the left side is ≤ 33.
  - dim aff(Σ) = 4 leaves 7 relations.
    - If ΣΣ = 0, the relations pair as complementary 4-sets with g-products related by G, so the left side is ≤ 27 + 18 = 45.
    - If ΣΣ ≠ 0, the 6-relations are complements of disjoint pairs summing to ΣΣ. Two of them sum to a 4-relation, so their number m satisfies m + C(m,2) ≤ 7, i.e. m ≤ 3, and the left side is ≤ 21 + 6m ≤ 39.
- **s = 9 (P = Σ, dim ≥ 5, at most 7 relations, at most one 8-relation, namely the complement of ΣΣ):** this needs −A_4 + 3A_6 − 9A_8 ≥ 33, but the left side is ≤ 9 + 18 = 27.
- **s = 10 (P = Σ, at most 15 relations):** this needs A_4 − 3A_6 + 9A_8 − 27A_10 ≥ 66.
  - If ΣΣ = 0, the relations pair as complements (4, 6) with g(T_6) = G·g(T_4). The value is ≤ 27 + 7·4 = 55.
  - If ΣΣ ≠ 0, the 8-relations come from disjoint pairs; 4 of them force a 5th, and the five are dependent. The value is ≤ 55 in every sub-case, with m_8 ∈ {0, 1, 2, 3, 5}.

Every case fails. ∎

**Corollary.** At (3,112), every balanced peak-28 target has **L ≥ 12**, with L even. This is up from the admitted Gate III floor of 8 and from Theorem R's 10.

## 5. What remains at (3,112)

Both of the following pass every test above:

- **Σ = ∅** (every small-value coset is balanced mod 3): L = 12 with six (1,1)-type cosets that are affinely independent, wt(h_0) = 0, and u = 36 from (★).
- **Σ = an affine 3-flat on which D̄ is affine**, with g = ±c times a character: wt(h_0) = 8, Ξ = −Σ_Σ c g, and u ∈ {4, 12, 20} via (★).

s ≥ 9 at L = 12 was not analysed. At (3,144) the same tools exclude s = 4 non-flat and s = 5 at L = 8, but the s = 6 case was not closed, so no (3,144) claim is made.

## Status

**WRITTEN:** the erratum, the general formulas, Ξ and (★), and Theorem R′.

Theorem R′ depends on own unreviewed Theorems A and O and on Lemma B. Adoption requires a review of the whole chain.

The (3,112) type, the (24,24,2) gap and the original problem remain OPEN. Novelty and priority are UNCLEARED. All findings are retained, including this OWN MINOR erratum, the checkpoint-054 attribution MINOR and the permanent v167 reviewer read-order PROCESS MAJOR. Same 18 owners, OWN root and HOLD. Science cutoff 11:05:38 PDT; no early park.
