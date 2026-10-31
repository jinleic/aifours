# Rank-6 lifted types — the pure-coset slice lemma; (3,112) at L = 12 reduced to s ∈ {10, 11, 12}; (3,144) at L = 8 reduced to three configurations

Owner **InfoBalancedNL242-2**, slot info-6. Actual `/bin/date` observation BEFORE this write: **Tue Oct 27 07:33:09 PDT 2026**.

**NEW WRITTEN AUTHOR CANDIDATE.** It is unreviewed, with no machine check and no formal or novelty claim. No program was run; all arithmetic was done by hand.

This packet excludes **no whole residue type and no whole L-value**. It records strict reductions only.

## 0. Inputs

- The admitted S0017 cut, as in `rank6-112-coset-projection-L8-exclusion-v1.md`.
- Own WRITTEN premises, all unreviewed:
  - Theorems A and O and Lemma B;
  - Theorem R′ and the formulas N_0, φ and Ξ, together with (★), in `rank6-112-erratum-and-L10-exclusion-addendum-v1.md` (SHA `520f1484…41d4`).
- At d = 144 the analogue of (★) is **3wt(h_0) + Ξ = 100 − 2L − u**, from S0017 (11): α + 2ν = 50 − L − u/2.

## 1. Lemma PC (pure-coset slice lemma, rank-6 lifted)

Here |V| = 4, so there are 3 slices η ≠ 0. Let ā ∉ P be a coset with no small value, and let k be its number of entries T = −28.

- If **k is odd**, then υ_η(ā) = 3c_ā ε̂_ā(η) = ±6 for **all three** η ≠ 0, so ā ∈ OddSums(P_η) ∖ P_η for every η ≠ 0.
- If **k = 2**, the same holds for exactly one η ≠ 0.
- If **k ∈ {0, 4}**, the coset is monochromatic.

Here P_η := supp(g_η) ⊆ P.

*Proof.* Write T = −4 + 24ε with ε = ±1 on the 4 points of the coset. For η ≠ 0, Σ_β T(β)(−1)^{β·η} = 24ε̂(η). On F_2^2:

- an ε of odd weight has ε̂ = ±2 at every η;
- a balanced ε is ± a character, so ε̂ = ±4 at exactly one η ≠ 0.

Then apply Lemma O. ∎

## 2. (3,112) at L = 12

Here wt(h_0) ≤ 16 and (★) gives 3wt + Ξ = 36 − u ≤ 32. Running the case list of Theorem R′:

- **s ∈ {1, 2, 3, 5, 6, 7}** fails the bound N_0 ≥ 48.
- **s = 4** (flat with G = +1): (★) needs Ξ ≤ −16, but |Ξ| ≤ 8.
- **s = 9** (|P∖Σ| ≤ 1, so dim aff(Σ) ≥ 4 and the dependency code R has dimension ≤ 4) needs −A_4 + 3A_6 − 9A_8 ≥ 36. In a binary linear code every active coordinate is 1 in exactly half of the codewords, so Σ wt ≤ 8·9 = 72 with exactly 15 nonzero codewords. Hence:
  - n_8 = 1 gives n_6 ≤ 4 and a value ≤ 31;
  - n_8 = 0 gives n_6 ≤ 6 and a value ≤ 27;
  - a smaller code gives ≤ 19.
- **s = 8**:
  - dim aff ≥ 4 is excluded as in Theorem R′.
  - dim aff = 3 means Σ is an affine 3-flat a + W_3. Its h_0 is constant up to sign on W_3^0-cosets, so wt(h_0) ∈ 8Z. The only value allowed by N_0 ≥ 48 is A_4 = 14, wt = 8, g = γ·character on the flat.
- **s = 0** (Σ = ∅, P = six balanced cosets, u = 36).

The last two configurations, s = 0 and the 3-flat, were the survivors listed in the addendum. **Both are now excluded:**

**(I) s = 0.**

1. h_0 ≡ 0, so u_0 = −σ and every s_ā = −8c_ā.
2. Every pure coset therefore has ΣT = −64, so k = 3, which is odd.
3. By Lemma PC, all 58 pure cosets must lie in OddSums(P_η) ∖ P_η for each η ≠ 0.
4. But a 6-set has at most C(6,3) + C(6,5) = 26 odd sums of size ≥ 3. Contradiction.

**(II) Σ a 3-flat, g = γ·character, wt = 8.**

1. aff(P) is a 5-flat. The 32 cosets outside it, which form 4 classes mod W_3, are monochromatic by Lemma O, so c_ā s_ā ∈ {−14, 10}.
2. Write u_0 = −σ + e, with e supported on the single W_3^0-coset K′ and |e| ≤ 2. Then |ê| ≤ 16, so ê(ā) = −6c_ā on every outside coset.
3. Since ê(ā + w) = (−1)^{w·ξ_0} ê(ā), we get D̄(w) + B̄(ā, w) = w·ξ_0 for all w ∈ W_3.
4. This forces B̄|_{W_3} = 0. So W_3 is Lagrangian, and B̄(ā_1 + ā_2, ·)|_{W_3} = 0 forces ā_1 + ā_2 ∈ W_3.
5. Hence at most ONE outside class satisfies the equation, whereas 4 must. Contradiction.

**Conclusion (WRITTEN).** Every (3,112) target with L = 12 has |Σ| ∈ {10, 11, 12}: at least ten cosets are imbalanced mod 3, and at most one other small-value coset exists. Those cases were not resolved. Crude weight-sum bounds do not close s = 10 or s = 11, and s = 12 was not analysed. **L = 12 is NOT excluded**, and the proven floor remains L ≥ 12.

## 3. (3,144) at L = 8

Here wt(h_0) ≤ 42 − u/2 ≤ 40, 3wt + Ξ = 84 − u, |Ξ| ≤ wt and α = (wt − Ξ)/2 is even. The options for (s, |P∖Σ|) are those of Theorem R.

- **(4,2):**
  - Non-flat: wt = 40, so Ξ ≤ −40, but |Ξ| ≤ 16 for s = 4.
  - Flat with G = +1: dim aff(P) ≤ 4.
  - Flat with G = −1: wt = 64.
- **(5,1) and (6,0):** P is 6 affinely independent points, so A_k = 0 and wt = 44 or 42, both > 40.
- **(6,1), wt = 36:** the only relation is one 2-flat with g = +1. (★) forces Ξ = −28 and u = 4. The extremal-deficit equation 2a + 6b + 18c = 8 gives (a, b, c) ∈ {(4,0,0), (1,1,0)}.
  - Put κ := G(−1)^{D̄(s)} with s = ΣΣ, and ℓ := B̄(s, ·). The five-subset conditions give g_x = G c_{s+x}. Then single value = κ(−1)^{ℓ(x)} and triple value = κ(−1)^{ℓ(T) + β(T)}, where β(x,y,z) = B̄(x,y) + B̄(x,z) + B̄(y,z).
  - **Case (4,0):** swapping one triple point gives B̄(x + y + s, z + w) = 0. Then B̄(y + y′, z + w) = 0, β is constant, ℓ is constant, and all singles are equal. That contradicts a = 4.
  - **Case (1,1):** the four-point identity Σβ = 0 makes every placement of the single exceptional triple fail.
- **(7,0), wt = 40 (one 2-flat with g = −1):** (★) forces Ξ = −40 and u = 4. The deficit equation gives a + 3b + 9c + 27d = 4.
  - The 7-set condition gives G = c_s. The pair (5-subset) conditions give B̄(x,y) = 1 + ℓ′(x) + ℓ′(y) with ℓ′ = ℓ + η, where η marks exceptional singles. Hence β ≡ 1.
  - The triple conditions then force η(T) = [T exceptional] for every triple, which is impossible for a = 4 and for a = 1.

**Remaining at (3,144), L = 8 (NOT excluded):**

- (6,1) with Σ a zero-sum 6-set, G = −1 and wt = 24. Here Ξ = 2Σ_x g_x c_x ∈ {8, 0, −8}.
- (7,0) with wt = 34 (one zero-sum 6-subset Σ∖{p}, where p = ΣΣ).
- (8,0).

So the (3,144) floor is NOT raised here.

## 4. Status

**WRITTEN:** Lemma PC; the exclusion of configurations (I) and (II) at (3,112), L = 12; and the (3,144) L = 8 reductions listed above.

**Proven floors** (own WRITTEN, unreviewed):

- (3,112): L ≥ 12 (Theorem R′).
- (3,144): the admitted L ≥ 8 only.

The (24,24,2) gap and the original problem remain OPEN. Novelty and priority are UNCLEARED. All earlier findings are retained, including the permanent v167 reviewer read-order PROCESS MAJOR, the cadence MAJORs, the checkpoint-054 attribution MINOR and the s = 6 erratum MINOR. Same 18 owners, OWN root and HOLD. Science cutoff 11:05:38 PDT; no early park.
