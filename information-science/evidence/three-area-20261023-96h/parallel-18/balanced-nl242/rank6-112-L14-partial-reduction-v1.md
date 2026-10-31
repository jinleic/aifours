# Balanced NL242 (3,112) at L = 14 — partial reduction (the 3-flat survivor and every s ≤ 9 or s = 11 are excluded)

Owner **InfoBalancedNL242-2**, slot info-6. Actual `/bin/date` observation BEFORE this write: **Tue Oct 27 07:52:04 PDT 2026**.

**NEW WRITTEN AUTHOR CANDIDATE.** It is unreviewed, with no machine check and no formal or novelty claim. No program was run; all arithmetic was done by hand.

**L = 14 is NOT excluded.** The proven floor stays L ≥ 14, from `rank6-112-L12-exclusion-L14-v1.md` (SHA `18613ab3…b6fd`).

## 0. Inputs

The same chain as that file: S0017; Theorems A, M and O; Lemmas B, PC and SV; the N_0 formulas and (★).

At L = 14, wt(h_0) ≤ 14 so N_0 ≥ 50, and (★) reads 3wt + Ξ = 32 − u with u ≡ 4 (mod 8).

## 1. Excluded at L = 14

- **s = 0** (seven balanced cosets): wt = Ξ = 0 forces u = 32 ≢ 4 (mod 8).
- **s ∈ {1, 2, 3, 5, 6, 7}:** N_0 ≤ 42 < 50.
- **s = 4:** a flat with G = +1 has N_0 = 48 < 50.
- **s = 8 with dim aff(Σ) ≥ 4:** the value is ≤ 45 < 57.
- **s = 8 with Σ an affine 3-flat F = a + W_3.** Then h_0 is constant up to sign on W_3^0-cosets, so wt ∈ 8Z. This forces A_4 = 14, i.e. g = γ·character on F, wt = 8 and supp(h_0) = K′, a single W_3^0-coset. Also P = F ∪ {p_1, p_2, p_3}, three balanced (1,1) cosets with [a], [p_j] affinely independent in Q := F_2^6/W_3.
  1. **Even k.** Each p_j is active in slice η iff d_j·η = 1, where d_j = β_j^λ + β_j^μ ≠ 0. That happens for exactly 2 of the 3 slices η ≠ 0. A coset whose class has offset c from [a] lies in OddSums(P_η) only if c ∈ {Σ_{j∈J′} e_j : J′ ⊆ J_η}. Checking the three patterns of (d_1, d_2, d_3) (all distinct, all equal, two equal) shows that every nonzero offset is active for at most 2 of the 3 slices. So Lemma SV forbids odd k, and every one of the 53 pure cosets has k ∈ {0, 2, 4}.
  2. **The value G′.** For a pure ā, ĥ_0(ā) = 0 because ĥ_0 is supported on F. So c_ā s_ā = −8 + (3/2)G′(ā) with G′ := c_ā·Walsh(σ1_{K′})(ā) and |G′| ≤ 8. The census c_ā s_ā = 10 − 6k gives G′ = 12 − 4k, so k ∈ {2, 4} and |G′| = 4.
  3. **Parseval contradiction.** Walsh(σ1_{K′})(ā_0 + w) = ±Walsh(σ1_{K′})(ā_0) for w ∈ W_3, so |Walsh| = 4 on all 8 cosets of each of the 7 classes with nonzero offset. That gives Σ Walsh² ≥ 7·8·16 = 896, but Parseval gives Σ_ā Walsh(σ1_{K′})² = 64·8 = 512. Contradiction.
- **s = 9** (|P∖Σ| ≤ 2, so dim aff(Σ) ≥ 4 and dim R ≤ 4): this needs −A_4 + 3A_6 − 9A_8 ≥ 39, but the code-weight bound gives ≤ 31.
- **s = 11** (|P∖Σ| ≤ 1, so dim aff(Σ) ≥ 5, dim R ≤ 5 and Σwt ≤ 176): this needs −9A_4 + 27A_6 − 81A_8 + 243A_10 ≥ 1377. Since n_10 ≤ 1 and 2n_6 + 4n_8 ≤ 46, the value is ≤ 270 + 810 + 243 = 1323.

## 2. Open at L = 14

- **s = 10:** e.g. Σ in a 4-flat with ΣΣ = 0, G = −1, at most one negative 2-flat among 15, and |P∖Σ| = 2. Crude code bounds allow this (value ≤ 87 against the 77 needed).
- **s = 12 with dim aff(Σ) = 5** (dim R = 6). The case dim aff(Σ) = 6 gives ≤ 2080 < 2752 and is excluded.
- **s = 13 and s = 14:** the crude weight bounds are insufficient.

## Status

**WRITTEN:** the exclusions in §1.

The (3,112) floor remains L ≥ 14. The type, the (24,24,2) gap and the original problem remain OPEN. Novelty is UNCLEARED. All findings are retained. Same 18 owners, OWN root and HOLD. Science cutoff 11:05:38 PDT.
