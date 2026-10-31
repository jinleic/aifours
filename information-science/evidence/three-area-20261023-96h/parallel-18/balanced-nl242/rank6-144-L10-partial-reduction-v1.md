# Balanced NL242 (3,144) at L = 10 — partial reduction (L = 10 NOT excluded)

Owner **InfoBalancedNL242-2**, slot info-6. Actual `/bin/date` observation BEFORE this write: **Tue Oct 27 07:56:04 PDT 2026**.

**NEW WRITTEN AUTHOR CANDIDATE.** It is unreviewed, with no machine check and no formal or novelty claim. No program was run; all arithmetic was done by hand.

The proven floor stays **L ≥ 10**, from `rank6-144-slice-value-lemma-L8-exclusion-v1.md` (SHA `3f9e20f6…2de2`).

## 0. Inputs and constraints at L = 10

The chain is: S0017, Theorems A and M(a), Lemmas O and SV, the N_0, φ and Ξ formulas, and (★) at d = 144, which reads 3wt + Ξ = 80 − u.

At L = 10:

- wt(h_0) ≤ 40 − u/2 ≤ 38, so N_0 ≥ 26;
- |P| ≥ 7 and dim aff(P) = 6;
- |Σ| + 2|P∖Σ| ≤ 10.

## 1. Excluded configurations, written as (|Σ|, |P∖Σ|)

- **(4,3), (5,2), (6,1), (7,0):** |P| = 7 with dim aff(P) = 6 makes P affinely independent, so Σ has no relations. Then N_0 = 24, 20, 22, 21 respectively, all < 26.
- **(6,2) with a 2-flat of g-product +1 in Σ:** N_0 = 28, wt = 36. (★) gives Ξ ≤ −32, but |Ξ| ≤ 30 for s = 6. All other (6,2) relation patterns give N_0 < 26, except (6,2)-b below.
- **(8,0)-C2′:** Σ is zero-sum with G = +1, and two extra small values lie inside Σ-cosets.
  - *Two cosets, each with 2 same-sign values.* Such a coset is active only in the single slice η ⊥ (β_1 + β_2). Hence some slice η has both inactive, and there P_η is 6 affinely independent points. A 5-subset of P_η sums to a pure coset; otherwise there would be a relation of size ≤ 6, but the only relation is Σ. There υ_η = 2·(−3)^2·g = ±18, contradicting |υ| ≤ 12 (Lemma SV).
  - *One coset y with a (2,1) or (1,2) pattern.* y is active iff (β_3 + β_4)·η = 1. That fails for exactly one η ≠ 0, where β_3 is the minority position and β_4 the fourth point. In that slice P_η = Σ∖{y} is 7 affinely independent points, with coefficients b_k = 2^{−6}(−3)^{(k−1)/2}. Its 5-subsets sum to the pure cosets y + x_1 + x_2, which carry υ_η = −64·b_5·g = −9g. The value |υ| = 9 ∉ {0, 6, 12} contradicts Lemma SV. (Its triples similarly give |υ| = 3.)

## 2. Open configurations at L = 10

- **(6,2)-b:** Σ is a zero-sum 6-set with G = −1, wt = 24, Ξ = 2Σ_x g_x c_x ∈ {4, −4, −12}, and there are two balanced cosets. A coset-class second-moment test is numerically consistent here (for example m_9 = 1, m_1 = 12, m_7 = 3 on a pure W_4-coset).
- **(7,1):** Σ∖{p} is zero-sum with g = +1 and p = ΣΣ ∈ Σ; wt = 34 and Ξ ∈ {−26, −34}.
- **(8,0)-C1′:** a zero-sum 6-subset with g = −1, wt = 38, Ξ = −38, u = 4, ν = 0.
  - The extremal-sign analysis forces g_x = −c_x on Σ_6 and g_q = c_q, together with β(x, y, q) = 1 and β(x, q_1, q_2) = 1.
  - **Excluded C1′ sub-cases (WRITTEN, same inactive-slice argument):**
    - two same-sign 2-value cosets with {y_1, y_2} ≠ {q_1, q_2}: in a slice where both are inactive, P_η is 6 affinely independent points, and its 5-subsets give |υ| = 18;
    - one 3-value coset y ∈ Σ_6: in its inactive slice, P_η = (Σ_6∖{y}) ∪ {q_1, q_2} is 7 affinely independent points, giving |υ| ∈ {3, 9}.
  - **Open C1′ sub-cases:**
    - {y_1, y_2} = {q_1, q_2}, where the inactive slice gives P_η = Σ_6 and every value lies in {0, ±12};
    - one 3-value coset y ∈ {q_1, q_2}, where P_η = Σ_6 ∪ {q_other} and the values lie in {−6g, 12g, 6g, 0}.
    - Both pass every slice test tried.
- **(8,1), (9,0), (10,0):** these pass the N_0 and dim-aff tests. They were not analysed further.

## Status

**WRITTEN:** the exclusions of §1. The (3,144) floor stays L ≥ 10.

The type, the (24,24,2) gap and the original problem remain OPEN. Novelty is UNCLEARED. All findings are retained. Same 18 owners, OWN root and HOLD. Science cutoff 11:05:38 PDT.
