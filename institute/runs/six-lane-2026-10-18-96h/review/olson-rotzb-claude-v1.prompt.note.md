# Referee report: ROT-ZB v2 (SHA 65dbedbf…)

**Basis.** I used only the embedded candidate and the embedded accepted records: the ROT-ZR source, its controlling verdict, the ZX/S1+ verdict, the S1-sharp verdict and the RUNS/RGR-LONG verdict.

The word-level chain is used only at its recorded scopes and is not re-proved. That chain is GRX, the normal form/PM*, DAV, K1, K01, KETA, SHgen/SHgen-E with V3, restricted REFL, the deletion ledger, RGR-LONG and SC0. I ran no computation.

## Preliminary: carrying REALIZE, ZSTRUCT and LAMBDA from (S) to (S′)

- **REALIZE** never mentions κ. Its hypotheses (zero-sum-free, L ≥ p+1, SC0 data, W ≤ 2p−1) all hold in (S′). I re-checked the three jump cases:
  - n = 1 gives W ≥ 2X+1 ≥ 2p+1.
  - 2 ≤ n ≤ p−1 gives W ≥ (n+1)(p+1−n)+n ≥ 2p+n. The middle expression is concave in n, with endpoint values 3p−3 and 2p.
  - n ≥ p gives W ≥ 3n.
- **Setting facts.**
  - Y′ being zero-sum-free and L = R−2t ≥ 2p−k ≥ p+1 use only t ≤ κ (from (S1)) and k ≤ p−1.
  - m − slack ≥ 2L−2p+1+h ≥ 3 uses only L ≥ p+1.
- **ZSTRUCT.**
  - The swap (Z−z)∪Q and the zero-sum g^s·z use only maximality of |Z| and s ≤ slack < m.
  - n₋ ≥ 1 needs only 1 ≤ t < p.
  - There is no hidden use of κ ≤ (p−1)/2.
- **LAMBDA** uses only n₊ ≤ 2κ < 2p, m ≥ L−e′/2, e′ ≤ 2p−1−L and s_i ≤ 2t−1. All of these hold in (S′).

## Verdicts

### BAL1: ACCEPT

- **Full positive-subsum interval.** P = g^{n₊}Y′ realizes every integer in [0, W+n₊]: REALIZE fills [0, W] (units exist since m ≥ 3), and adding 1..n₊ copies of g covers the rest.
- **(\*) complement construction.** Take N₀ ⊆ N with S₀ ≤ W+n₊, and P_c ⊆ P with coefficient sum c = W+n₊−S₀.
  - |P_c| ≤ c, because every P-coefficient is ≥ 1.
  - P₀ = P−P_c is disjoint from P_c by construction, and disjoint from N₀ because P ∩ N = ∅.
  - N₀P₀ has integer coefficient sum 0, so the longest-zero-sum bound gives |N₀|+|P₀| ≤ 2t.
  - Since n₊+L−c = S₀−e′, this yields S₀+|N₀| ≤ 2t+e′.
- **Unbalanced case.** Write S(N) = n₊+2pj.
  - j ≤ −1 would give S(N) ≤ n₊−2p < 0, using n₊ < 2p. So j ≥ 1 and S(N) > W+n₊.
  - Hence the prefix-crossing index i₀ < n₋ exists.
  - Using s_{i₀+1} ≤ 2t−1 gives L+n₊ ≤ 4t−2−i₀.
  - Using s_{i₀+1} ≤ slack gives 2L+e′+n₊ ≤ 2p−2+2t−i₀.
  - Unbalance needs both inequalities, so either stated condition forces balance.
- **Specializations.** With n₊, e′ ≥ 0 and t ≤ κ:
  - L+n₊−(4t−1) ≥ 2p−k+1−4κ.
  - 2L+e′+n₊−(2p−1+2t) ≥ 2p−2k+1−2κ, which is ≥ 0 iff κ+k ≤ p.
- **Edge cases.**
  - t = 0 is trivially balanced.
  - t ≥ 1 with n₊ = 0 forces S(N) ≥ 2p, so the lemma correctly excludes it under either condition.
  - n₋ = 0 is excluded by ZSTRUCT.

### ROOM: ACCEPT

- **The g^{n₊}Q argument.** Suppose n₊ ≥ 1 and W ≥ 2p−n₊.
  - Take Q ⊆ Y′ of weight 2p−n₊ (this lies in [2, W]); then |Q| ≥ 2p−n₊−e′.
  - g^{n₊}Q (the positive terms of Z plus Q, which are disjoint) is a zero-sum of length ≥ 2p−e′ ≥ L+1.
  - L ≥ 2t is equivalent to 2p+2κ−k ≥ 4t, which follows from t ≤ κ and 2κ+k ≤ 2p.
  - This contradicts maximality, so W ≤ 2p−1−n₊. This step does not need balance.
- **Coefficients and signs.**
  - a_i ≤ 1+e′ ≤ 2p−L ≤ k ≤ p−1, so a_i ≤ p−2 since a_i is odd.
  - s_i ≤ slack ≤ 2p−1−L ≤ k−1 ≤ p−2.
  - The weights are therefore b = a_i, b = 1 and b = −s_i.
  - No coefficient is ±p, so no ρ₀ occurs, and c ≠ 0 because ord g = 2p.
- **E ≤ k−1.** E = e′+S(N)−n₋ = e′+n₊−n₋ (using balance). With e′ ≤ k−1−2κ+2t−n₊ this gives E ≤ k−1−2κ+n₊ ≤ k−1.

### ROT-ZB: ACCEPT (findings m1 and m6 are non-blocking)

- **(S1) in every branch of (B).**
  - B1 gives 4κ̂ ≤ 2p−1.
  - Λ1 gives 8κ̂ ≤ 4p−1.
  - Λ2 gives κ̂(2κ̂−1) < p.
  - B2 with DAV gives κ̂ ≤ min(k−1, p−k).
  - With κ̂ an integer, each branch yields κ̂ ≤ (p−1)/2. S1+ therefore applies, and (S′) holds with κ = κ̂.
- **Balance.**
  - t = 0 is trivial.
  - B1 and B2 go through BAL1.
  - Λ goes through LAMBDA, whose (S′) scope is checked above.
- **ROOM** applies.
- **SHgen(H).** 2H = 2p−2−2κ̂ ≥ k−1 ≥ E.
- **SHgen(K).** η+a_max ≤ E+2 ≤ k+1 ≤ 2p−k−1, which holds iff k ≤ p−1. Only KETA's k-free inequality is used.
- **Empty runs.** The SHgen-E caller is the same as in the ZR verdict:
  - k is fixed along expansions;
  - base words have one nonzero pair and o_F ≤ k ≤ p−1;
  - restricted REFL and V3 apply.
- **Conclusion.** The contradiction forces E = 0, so every rotation is ±g = ρ_{±c}. The normal form preserves the rotation multiset, so the same holds for w.

### Uniform Corollary INV*/OLSON-ZB: ACCEPT-WITH-FIXES (scoped partial dihedral result; m2–m5)

- **Algebra.** 4κ(w) ≤ 2p−o+1 ⟺ 4p−4−2F+2o ≤ 2p−o+1 ⟺ 2F ≥ 2p+3o−5. This is correct.
- **Normal-form transform.** κ̂ = κ(w)−(o−k)/2, since the normal form preserves F.
- **Cases.**
  - k = 1: K1.
  - 3k ≤ 2p+1: the terminal chain (see m4).
  - κ̂ ≤ 1: K01.
  - Otherwise (2p+1)/3 < k ≤ o ≤ p−1 and κ̂ ≥ 2. Then 4κ̂ ≤ 2p−3o+2k+1 ≤ 2p−k+1, and 2κ̂+k ≤ 2p−2−F+2o ≤ 2p−1, using F ≥ 2o−1.
  - These cases are exhaustive given k ≥ 1 (see m5).
- **REFL** is applied to the original word, with o ≤ p.
- **Deletion ledger and RGR-LONG.**
  - Case 2 produces (o−1, F−1) and needs 2F ≥ 2p+3o−6, which holds.
  - Case 3 produces (o or o−2, F), which holds.
  - Case 1 needs o ≤ 2p−3, which holds.
  - RGR-LONG then closes part (b).

## Findings: 0 FATAL, 0 MAJOR, 6 MINOR

**m1 (non-blocking). Redundant hypothesis.** Locations: the Theorem statement in Sec. 0, the (S1) bullet in Sec. 4, and Sec. 7.
- **Gap.** Every branch of (B) forces κ̂ ≤ (p−1)/2. With k ≤ p−1 this gives 2κ̂+k ≤ 2p−2.
  - So the hypothesis 2κ̂+k ≤ 2p−1 is automatic.
  - Plain S1(a) suffices, so the (S′) generality is correct but not load-bearing.
  - Sec. 7's residual clause "2κ̂+k > 2p−1" describes no cells.
- **(Λ) is contained in B1 for 2 ≤ k ≤ p−1.**
  - Λ1's right-hand side exceeds B1's by 3−k, and the two coincide by parity at k = 2.
  - Λ2 holding while B1 fails would need (2κ̂−3)(κ̂−1) < 0, which has no integer solution.
- **B2 is contained in B1 once 3k ≥ 2p−1.** So in the new range, (B) is just B1.
- **Fix.** State "(B) ⟹ κ̂ ≤ (p−1)/2 ⟹ 2κ̂+k ≤ 2p−2" and delete the Sec. 7 clause. Optionally drop that hypothesis and the LAMBDA import.

**m2 (required wording). Residual relies on unrecorded results.** Locations: Sec. 6 bullet 2 and Sec. 7.
- **Gap.** "T3/T4" are not defined in the candidate and do not appear in any embedded accepted record. Both "not covered by K01/KP/T3/T4" and "…and T4 failing" rest on them.
- **Gap.** "k ≤ p−1 with (B) failing" also includes cells already covered: k = 1 by K1, 3k ≤ 2p+1 by ZX plus S1-sharp, and κ̂ ≤ 1 by K01.
- **Fix.** State the residual as two parts:
  - k = p with κ̂ ≥ 2;
  - (2p+1)/3 < k ≤ p−1 with κ̂ ≥ 2 and 4κ̂ ≥ 2p−k+2.
- **Fix.** Subtract T3/T4 cells only after citing their accepted verdicts.

**m3 (required wording). Uniform comparison.** Location: Sec. 6 bullet 1.
- **Gap.** "Previously … needed F−o_F ≥ 2p−6 / 2p−8" ignores the accepted S1-sharp coverage of 3o_F ≤ 2p+1, which has no condition on F.
- **Gap.** The ZR3 uniform band is accepted only for p ≥ 17. The containment arithmetic (o ≤ 2p−11) actually holds for all o ≤ p−1 once p ≥ 11.
- **Fix.** Write: "for (2p+1)/3 < o_F ≤ p−1 the accepted uniform bands were F−o_F ≥ 2p−6 (p ≥ 7) and ≥ 2p−8 (p ≥ 17); the new band contains both."

**m4 (required). Case 3k ≤ 2p+1 is not written at terminal level.** Location: Sec. 5(a) bullet 2.
- **Gap.** The accepted S1-sharp dihedral statement is word-level, under 3o_F ≤ 2p+1, and its derivation bounds κ̂ through k ≤ o_F. In this corollary o_F may exceed (2p+1)/3.
- **What is needed.** The terminal chain:
  1. k ≥ 2, so DAV gives κ̂ ≤ k−1 and hence 3κ̂ ≤ 2p−2.
  2. GRX gives (ZP).
  3. S1-sharp gives (S1).
  4. The ZX terminal criterion finishes.
- **Fix.** Insert this sentence. The chain itself is valid.

**m5 (required citation). Source of k ≥ 1.** Location: Sec. 5(a), "every admissible normal form has 1 ≤ k ≤ o".
- **Gap.** Case exhaustion needs k ≥ 1. A k = 0 form would land in the 3k ≤ 2p+1 case, where ZX assumes k ≥ 1 and DAV is used only for k ≥ 2.
- **Gap.** The candidate gives no source for k ≥ 1; the accepted ZR corollary used the same step implicitly.
- **Fix.** Cite the normal-form property that yields k ≥ 1, for example F ≥ 1 (here F ≥ 5) together with the "odd terminal blocks" of ZR verdict m4. Alternatively, treat k = 0 explicitly.

**m6 (non-blocking). Citation and notation precision.**
- **Sec. 4, line 1.** The existential reading of the normal form is ZX overlay 2. Overlay 1 is the integer-domain condition that S1+ needs. Cite both.
- **Sec. 4, SHgen-E caller.** It omits "base words have length 4p−2" and "expansions preserve odd blocks". Copy the ZR verdict's discharge verbatim.
- **Sec. 1.** The phrase "exactly as used by ROT-ZR's verdict" wrongly includes ZX plus S1-sharp. Cite the S1-sharp verdict for that item instead.
- **Sec. 2.** P₀ denotes both the complement P−P_c and the 0th prefix sum. Rename the prefix sums.
- **Sec. 2.** The [0, W] fill comes from REALIZE's proof (bullet 2); the statement itself only gives [2, W]. Cite the bullet.

## Scope

All four items are correct relative to the recorded imports. The result is a sufficient-condition, partial dihedral theorem. It is not unrestricted INV*(p), not ordered Olson for D_2p, and not the all-groups target. No novelty is claimed or assessed. The Sec. 6 cell counts were not verified and are not premises.
