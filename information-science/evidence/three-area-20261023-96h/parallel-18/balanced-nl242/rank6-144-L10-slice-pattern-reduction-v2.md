# Balanced NL242 (3,144) at L = 10 — slice-pattern reduction to (8,1), (9,0) and (10,0)

Owner **InfoBalancedNL242-2**, slot info-6. Actual `/bin/date` observation BEFORE this write: **Tue Oct 27 08:04:12 PDT 2026**.

**NEW WRITTEN AUTHOR CANDIDATE.** It is unreviewed, with no machine check and no formal or novelty claim. No program was run; all arithmetic was done by hand.

This packet extends `rank6-144-L10-partial-reduction-v1.md` (SHA `f576731b…f69f`), which stays immutable. **L = 10 at (3,144) is still NOT excluded.**

## 0. Tools

All tools are taken from `rank6-lifted-floors-consolidated-proof-v1.md` (SHA `6c5ce361…b929`): Lemmas O, Φ and SV, Theorem M, and the census c_ā s_ā = 4 − 1.5G(ā) + c_ā ĥ_0(ā)/2, where G := c_ā·Walsh(σ1_Z) and Σ_ā (G − N_0/8)² = 64N_0 − N_0².

**Slice-pattern rule (from Lemma SV).** For a pure coset, the triple (υ_η)_{η≠0} must be one of:

- all zero;
- exactly one entry ±12 and the others zero;
- all three entries ±6.

In particular, **two nonzero entries together with one zero is forbidden, and a single ±6 is forbidden.**

**Activity of a coset in slice η.**

- A single-value Σ-coset is active in every slice.
- A balanced (1,1) coset with positions β^λ, β^μ is active iff (β^λ + β^μ)·η = 1, i.e. in 2 of the 3 slices.
- A same-sign 2-value Σ-coset is active iff (β_1 + β_2)·η = 0, i.e. in 1 slice.
- A (2,1) or (1,2) coset is active iff (β_3 + β_4)·η = 1, i.e. in 2 slices.
- A (3,0) or (0,3) balanced coset is active in all 3 slices.

## 1. Newly excluded configurations

**(6,2)-b.** Σ is a zero-sum 6-set with G = −1, p_1 and p_2 are balanced, and P = Σ ∪ {p_1, p_2} has the single relation Σ.

The pure cosets of class [p_1] are p_1 + x + y (x, y ∈ Σ). In a slice where p_1 is inactive, their value is 0. In a slice where both p_j are active (8 points), their value is −(1/2)(3 − 9G_η)g. To avoid ±3 this needs G_η = −1, and then the value is −6g ≠ 0. In a slice with p_1 active and p_2 inactive (7 points), the value is (3 − 9G_η)g ≠ 0.

- If d_1 = d_2: two slices have both active and one has neither, giving the pattern (±6, ±6, 0). Forbidden.
- If d_1 ≠ d_2: the slices have J = {1}, {2} and {1, 2}, giving the pattern (nonzero, 0, ±6). Forbidden.

**(7,1).** Σ = Σ′ ∪ {p}, where Σ′ is zero-sum with g = +1 and p = ΣΣ, plus one balanced p′. The tenth small value lies in exactly one of three places.

- *A same-sign 2-value coset y ∈ Σ′.* In a slice where y is inactive, the active set is affinely independent, because the only relation of P is Σ′. Its size is 6 or 7, and a 5-subset not equal to Σ′∖{y} sums to a pure coset with |υ| = 18 or 9. Forbidden.
- *y = p.* For the cosets p′ + x + z, p′ is inactive in exactly one slice. In each slice where p′ is active, the value is nonzero (one of ±3, ±6, −6g or 12g), so the pattern has two nonzero entries and one zero. Forbidden.
- *p′ of type (3,0) or (0,3).* p′ is active in all slices. Then class [p′] needs G′_η = −1 for all three η ≠ 0, i.e. B′·η = 1 for all of them, which is impossible on F_2^2.

**(8,0)-C1′, remaining sub-cases.**

- *{y_1, y_2} = {q_1, q_2} with η_{q_1} ≠ η_{q_2}.*
  1. The type-(a) cosets x + y + q_i are active only at η_{q_i}, so they need value ±12. That forces G6_{η_{q_i}} = −1 for both i, hence B6 = 0, hence G6_η = −1 for all η.
  2. Then the 10 type-(b) cosets (triples in Σ_6) and the 10 type-(d) cosets (5-sets {a, b, c, q_1, q_2}) have υ ≡ 0 in every slice, so they are monochromatic. Also ĥ_0 = 0 at all of them, because (1 + G6_0) = 0.
  3. So G ∈ {−4, 12} on these 20 cosets. With N_0 = 26: Σ (G − 3.25)² ≥ 20·52.56 > 988 = 64·26 − 26². Contradiction.
- *{y_1, y_2} = {q_1, q_2} with η_{q_1} = η_{q_2} =: η*.* The type-(a) cosets are active only at η*, where all 8 points are active. Their value is −(1/2)(3 − 9G6)g ∈ {3g, −6g}, so the pattern is a single ±3 or ±6. Forbidden.
- *One 3-value coset y = q_1.* In its 2 active slices all 8 points are active, so the type-(a) cosets x + y + q_1 need G6 = −1 and take value −6g. In the inactive slice they are 0. That gives (±6, ±6, 0). Forbidden.

Together with the C2′ exclusion in the earlier partial packet, **(8,0) is fully excluded at L = 10.**

## 2. Remaining at (3,144), L = 10 (NOT excluded)

- **(8,1):** 8 single-value Σ-cosets plus one balanced coset. Here dim R(Σ) ≤ 2, and 3A_4 − 9A_6 + 27A_8 ≥ 9 is needed. The inactive-slice argument does not apply directly, because OddSums(Σ) may already cover all of F_2^6.
- **(9,0):** one same-sign 2-value coset, with dim R(Σ) = 2.
- **(10,0):** all single-value, dim R = 3, and P_η = Σ in every slice. The two-value condition "M_γ = A + 24c_ā ε(γ)" was not resolved.

## Status

**WRITTEN:** the §1 exclusions. The (3,144) floor stays L ≥ 10; L = 10 is now reduced to three configurations.

The type, the (24,24,2) gap and the original problem remain OPEN. Novelty is UNCLEARED. All findings are retained. Same 18 owners, OWN root and HOLD. Science cutoff 11:05:38 PDT.
