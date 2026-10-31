# Balanced NL242 (3,112) at L = 16 — partial reduction (s ∈ {0,…,7, 9, 11, 13} excluded; s = 8, 10, 12 structured; s = 14, 15, 16 open)

Owner **InfoBalancedNL242-2**, slot info-6. Actual `/bin/date` observation BEFORE this write: **Tue Oct 27 09:07:44 PDT 2026**.

**NEW WRITTEN AUTHOR CANDIDATE.** It is unreviewed, with no machine check and no formal, kernel or novelty claim. No program was run; all arithmetic was done by hand.

**Scope.** This file builds on `rank6-112-L14-e7sq-exclusion-L16-v5.md` (97fc01ef…ce74d), whose floor is L ≥ 16. It covers (3,112) at L = 16 only. **L = 16 is NOT excluded.**

## 0. Setting at L = 16

- α + 2ν = 14 − u/2 with u ≡ 4 (mod 8). So wt(h_0) ≤ 12 and **N_0 ≥ 52**.
- (★) reads 3wt + Ξ = 28 − u.
- s + 2|P∖Σ| + (extra values) ≤ 16, and dim aff(P) = 6.

**Lemma H at L = 16.** For every ω whose hyperplane meets Σ on both sides, q ≥ 20, so N(Σ_0) ≥ 40 and N(Σ_1) ≥ 40. By (3.1):

- **no side has size 1, 2, 3 or 5**;
- a side of size 4 is a positive 2-flat.

**W-moments** inside aff(Σ) ≅ F_2^d: Σ W² = 2^d s and Σ W⁴ = 2^d(3s² − 2s + 24n_4).

## 1. Exclusions

- **s = 0.**
  1. P consists of eight balanced (1,1) cosets. We have wt = Ξ = 0, so u = 28, and N_0 = 64.
  2. Then G ≡ c·Walsh(σ)·c = 8, so c s = 4 − 12 = −8 at every coset. At pure cosets this forces k = 3 at all 56 of them, so Lemma SV gives all three slices nonzero, and every pure coset lies in OddSums(P_η) for every η.
  3. That needs 2^{|P_η|−1} ≥ 56, i.e. |P_η| ≥ 7 in each slice. But Σ_η |P_η| = 2·8 = 16 < 21. ✗
- **s = 1.** |Ψ| = 1, so N_0 = 0. ✗
- **s = 2, …, 7.** Some hyperplane splits Σ into two nonempty sides, both of size ≥ 4. That needs s ≥ 8. ✗
- **s = 9.** Every split (4,5), (6,3), (7,2), (8,1) contains a forbidden size. ✗
- **s = 11.** Only (4,7) splits are allowed, so W = ±3. Then 121 + 9(2^d − 1) = 11·2^d gives 2^d = 56. ✗
- **s = 13.** Splits are 4|9 or 6|7, so W ∈ {±5, ±1}, and n_5 = (2^d − 14)/2.
  - d = 6: n_4 = 8.75. ✗
  - d = 5: Σ W⁴ = 28561 + 9·625 + 22 = 34208 = 32(481 + 24n_4), so n_4 = 24.5. ✗
  - d = 4: n_4 = 56. But 13 points of AG(4,2) contain exactly 140 − 105 + 21 − 1 = 55 planes. ✗

## 2. Structure of the surviving small cases (partial)

**s = 8.** Every split is 4|4, so W ≡ 0 off ω = 0 and 2^d = 8: **Σ is a 3-flat F**, and all 14 of its planes are positive. Then g = ±(affine character), h_0 is supported on one W_3^0-coset K′ (wt = 8, N_0 = 56), and ĥ_0 vanishes off F.

1. For pure ā: c s = −8 + (3/2)G′, with G′ = c·Walsh(σ1_{K′}), so G′ = 12 − 4k ∈ {8, 4, 0, −4}.
2. |Walsh(σ1_{K′})| is constant on the 8 W_3-classes, and Σ_classes |W|² = 512/8 = 64.
3. So at most 4 pure classes have |G′| = 4, and at least 3 pure classes have odd k. Those classes must be reachable in all three slices.
4. With |P∖Σ| = 3 (including the variants where Σ-cosets carry extra values, and where one coset is a (2,2) balanced coset active in a single slice), no nonzero offset is reachable in all three slices (spans of pairs of a basis meet only in 0). ✗
5. With four balanced (1,1) cosets of offsets c_1…c_4: only the inactivity partition (2,1,1) survives, with span(J_{η_1}) = S of dimension 2 contained in the other two spans. Example: c = (e_3, e_1 + e_2 + e_3, e_1, e_2). Then exactly 3 classes (S ∖ 0) have k = 3, 4 classes have |G′| = 4, and Walsh(σ1_{K′}) vanishes on F's class.

**This sub-case is OPEN.** It needs the explicit ±6 slice values on the 24 cosets with k = 3.

**s = 10.** Every split is 4|6, so W = ±2, d = 4 and n_4 = 15. Σ is 10 points of a 4-flat in which every hyperplane cuts off a positive plane. **OPEN.**

**s = 12.** Splits are 4|8 or 6|6, so W ∈ {±4, 0}. The cases are d = 4 (n_4 = 39, so the complement of Σ in AG(4,2) is a 2-flat), d = 5 (n_4 = 15) and d = 6 (n_4 = 3). **OPEN.**

**s = 14, 15, 16.** **OPEN.**

## Status

**WRITTEN:** the exclusions in §1 and the reductions in §2. **(3,112) floor: L ≥ 16** (T112, v5). At L = 16 the surviving s are {8 (one sub-case), 10, 12, 14, 15, 16}.

The (24,24,2) gap and the original problem remain OPEN. Novelty is UNCLEARED. All findings are retained. Same 18 owners, OWN root and HOLD. Science cutoff 11:05:38 PDT.
