# Hostile audit: Lemma S1(g) v2, Corollary S1(g)+ and Section 2

## Verdicts

| Item | Verdict |
|---|---|
| Lemma S1(g) v2 | **ACCEPT-WITH-FIXES**: 0 FATAL, 0 MAJOR, MINOR m1–m7 |
| Corollary S1(g)+ | **ACCEPT-WITH-FIXES**: m8–m10. S1(e) is not needed |
| Uniform INV* | **ACCEPT-WITH-FIXES**: m10, statement wording only. Conditional on acceptance of S1(g) |
| Uniform ordered Olson | **ACCEPT-WITH-FIXES**: m10 only |
| Tables (δ*, coverage, residual) | **ACCEPT-WITH-FIXES**: every value is correct; m11–m13 |

## Scope

**Audited**
- SOURCE00:1–157, line by line.
- SOURCE00:160–256, only for consistency with the body. It matches.
- Context read: SOURCE01 (notation and the Sec. 2 template), SOURCE02 overlay, SOURCE03, SOURCE04 items 3–5 and overlay items 1–3 and 8.
- SOURCE05:15–17: the Davenport pigeonhole proof, re-checked.

**Imported, not re-proved**
- D(Z_2p) = 2p.
- EGZ for Z_p.
- The Savchev–Chen / Yuan theorem, in the general form recorded at SOURCE03:9,11.
- The terminal criterion (SOURCE04:20), with GRX, DAV, K1, κ̂ ≥ 0 for k ≥ 2 (SOURCE04:53), SHgen-E, restricted REFL, RGR-LONG and the ordered deletion ledger (SOURCE04:58).

**Not used**
- S1(e), S1(g) v1, the residual notes, the t-search, and the "short script". Every table entry below was recomputed by hand.
- SHA256 values were not checked, because I had no tools.

## Lemma S1(g): independent re-derivation

**(1) Lengths.**
- All terms are odd, so N is even.
- N lies outside [p+δ+2, 2p], so N ≥ 2p+2.
- T minus one occurrence still has ≥ 2p+1 terms, so (D) gives a proper zero-sum.
- Minimality applied to a proper zero-sum and its complement, with p+δ even, puts every proper zero-sum length in [l, p+δ]. Here l is even and l ≥ p+2−δ. ✓

**(2) Claims A and B.**
- Claim A uses only |T₁| = p and x(T₁) = 0, so it holds for every such T₁ (as in SOURCE02:56).
- Claim B: two disjoint odd x-zero sets give a proper zero-sum of length ≤ 2δ. Then 2δ < p+2−δ ⇔ p ≥ 3δ−1. This is the binding use of P1. ✓

**(3) N ≤ 2p+δ−1.**
- If l > p, every Davenport V inside M is odd, of size ≤ δ.
- M−V₁ then has ≥ l ≥ p+1 occurrences, which gives a second disjoint V₂, contrary to Claim B.
- l is even and p is odd, so l ≤ p−1. ✓

**(4) No term (1,0).**
- EGZ on 2p−1 of the N−1 ≥ 2p+1 other occurrences puts u in M.
- An odd V contradicts Claim B together with {u}.
- An even V has |V| ≥ l. The leftover W is x-zero and even, with |W| ≥ μ−1−p = N−2p−1 ≥ 1, so |W| ≥ 2. Also |W| ≤ δ−1 < l. ✓ (m1)

**(5) M = C·V and index one.**
- Both sub-cases give an odd x-zero C ≠ M with 3 ≤ |C| ≤ δ. In the case C = M−V₀: Claim A bounds |C| ≤ δ, and |C| ≥ N−2p ≥ 2 with |C| odd.
- V is an even zero-sum with |V| ≥ l.
- A proper even V'' would force |V| ≥ 2l > μ. This holds because l > δ, which follows from p ≥ 2δ−1.
- A proper odd V'' gives V'' and V−V'', which violate Claim B.
- So x(V) is a minimal zero-sum over Z_p. Hence β ≤ p by Davenport, and β even gives β ≤ p−1 (m2).
- The index theorem applies: p+2−δ ≥ ⌊p/2⌋+2 ⇔ p ≥ 2δ−1.
- The basis element a is nonzero, so ord a = p, and the least positive coefficients lie in [1, p−1].
- Σ(c−1) = p−β ≤ δ−2, so m_V ≥ 2β−p ≥ p+4−2δ.
- Parity: ĥ = (1,h) has order 2p. A term (1,ch) equals c·ĥ if c is odd and (c−p)·ĥ if c is even. The weights sum to p(1−#even) ≡ 0 (mod 2p), so #even is odd.
- 2 ≤ e ≤ δ−1, and t ≥ m_V. ✓

**(6a) Even c.**
- ĥ^(p−c)z uses z ≠ ĥ and has even length p−c+1 ≤ p−1.
- This gives c ≤ δ−1, or else c ≤ p−t−1 ≤ 2δ−5. ✓

**(6b) Odd c ≤ p−e.**
- ĥ^(p−e−c)yz: y ≠ z because their coefficients have different parity, and neither equals ĥ.
- The length is even and ≤ p−3.
- This gives c ≤ δ−e, or else c ≤ 2δ−7. ✓

**(6c) Near-p terms.**
- s is even, with 2 ≤ s ≤ e−2 ≤ δ−3 ≤ p+4−2δ ≤ m_V (needs p ≥ 3δ−7).
- If z ∉ C, take the ĥ's from V; z itself may lie in V or T₁. Then ĥ^s z is a half-sum disjoint from C, and the union has length ≤ 2δ−2 < l (needs p ≥ 3δ−3).
- Two near-p occurrences (possibly of equal value): the weight is 2p and the length is ≤ 2δ−4 < l. Availability needs s+s' ≤ 2δ−6 ≤ p+4−2δ ≤ t, which is exactly P2. ✓
- K ≤ 2δ−5 for δ ≥ 5.
- For δ = 3: K_e = 2 and K_o ≤ 1. Moreover s ≤ e−2 = 0, so no near-p term exists at all.

**(7) The x-sum congruence.**
- The congruence is correct, and 2 ≤ N−2p ≤ δ−1 by step (3).
- u_q = 0 gives X ≥ p+1−δ.
- u_q = 1: since s_q ≥ 2, r ∈ [4−δ, e−3]; the stated 3−δ is valid but loose. X = r < e−1 ≤ X is impossible, so X ≥ p+r. ✓

**(8) S-condition and contradiction.**
- S-condition: the weight is p(1−#even S) ≡ 0, and the length is ≤ p−σ/2 < N (m4).
- Every maximal greedy run ends with σ ≥ Σ_U c − K_e ≥ X+|U|−K. The start is σ = e < 2δ−2, so the run crosses the threshold.
- Reachability needs p ≥ 5δ−8. P3 already gives this at δ = 5 (17 ≥ 17).
- The overshoot is ≤ 2K, so σ ≤ 6δ−13 ≤ p.
- σ ≥ 2δ−2 > 2δ−4 ≥ p−t.
- mass ≥ σ/2 ≥ δ−1 > δ−2. ✓

**Hypothesis map**
- (ZP) is used only in step (1).
- P1 enters only as p ≥ 3δ−1 (binding), p ≥ 3δ−3 and p ≥ 2δ−1.
- P2 is used only in (6c). P3 is used only in (8).
- Note: P1 ⇔ κ ≤ (2p−2)/3. So P1 coincides with the terminal range κ̂ ≤ k−1 ≤ ⌊(2p+1)/3⌋−1.

**Boundary cases** (worst-case values)

| δ, p | l ≥ | 2δ | t ≥ | K ≤ | X ≥ | σ_full ≥ / 2δ−2 | σ ≤ / p | mass ≥ / δ−2 |
|---|---|---|---|---|---|---|---|---|
| 3, 13 | 12 | 6 | 11 | 2 | 11 | 9 / 4 | 7 / 13 | 2 / 1 |
| 5, 19 | 16 | 10 | 13 | 5 | 15 | 10 / 8 | 17 / 19 | 4 / 3 |
| 7, 29 | 24 | 14 | 19 | 9 | 23 | 14 / 12 | 29 / 29 | 6 / 5 |
| 9, 41 | 34 | 18 | 27 | 13 | 33 | 20 / 16 | 41 / 41 | 8 / 7 |
| 11, 53 | 44 | 22 | 35 | 17 | 43 | 26 / 20 | 53 / 53 | 10 / 9 |

- P3 is exactly tight in σ ≤ p for δ ≥ 7, and it still closes there.
- P2 has ample slack.

**Counterexample attempt**
- Take p ≥ 7 prime and T = g^(p+3)(3g)^(p−1), with g an odd generator, so N = 2p+2.
- Its nonempty zero-sums are g^i(3g)^j with i+3j ∈ {2p, 4p}. The 4p case is only T itself.
- The 2p case has ⌈(p−3)/3⌉ ≤ j ≤ ⌊2p/3⌋ and length 2p−2j. The maximum is (4p+2)/3 when p ≡ 1 (mod 3) and (4p+4)/3 when p ≡ 2.
- Hence (ZP) holds and (S1) fails at every integer κ with ⌈(2p+1)/3⌉ ≤ κ ≤ p.
- Instances: (p, κ) = (7,5) via g¹⁰(3g)⁶, (13,9), (19,13) and (31,21).
- At p = 3δ−2 the proof breaks exactly at Claim B, since l = 2δ.
- Consequences:
  - P1 cannot be dropped.
  - For p ≡ 1 (mod 3), P1 is best possible for any implication of the form (ZP) ⇒ (S1).
  - Every instance violates P1, so none satisfies P1–P3.
- At p = 31, κ = 20, (ZP) fails for this family, because 42 is a zero-sum length. So the residual pair (21,20) is untouched.
- I found no counterexample, and claim none, in the gap 3δ+4 ≤ p < 6δ−13.

## Corollary and Section 2

**Corollary S1(g)+**
- S1(g) at δ = 5 has thresholds 19 (P1), 10 (P2) and 17 (P3), so it holds exactly for p ≥ 19.
- So SOURCE00:125 alone covers κ = (p+5)/2 for p ≥ 19. S1(e) is not a premise anywhere.
- P1–P3 all weaken as δ decreases. Together with S1+ (0 ≤ κ ≤ (p+1)/2) and S1(d), the covered set is the integer segment 0 ≤ κ ≤ (p+δ*)/2.
- P2 is implied by P3, so omitting it at SOURCE00:125,127 is harmless.

**Uniform INV***
- Any normal form has k ≤ o, so 3k ≤ 2p+1. The case k = 1 is K1.
- Low branch: κ̂ ≤ o−1 ≤ (p+δ*)/2.
- High branch: κ̂ ≤ p−1−(p−δ*−2)/2 = (p+δ*)/2.
- κ̂ is an integer and ≥ 0, so (S1) holds and the rotations lie in one pair.
- o ≤ (2p+1)/3 ≤ p, so restricted REFL applies. ✓

**Uniform ordered Olson**
- Case 1 needs o ≤ 2p−3, which holds.
- Cases 2 and 3 give o' ≤ o and F'−o' ≥ F−o. So both branches and 3o' ≤ 2p+1 are preserved.
- δ* depends on p only. ✓

**δ* table**
- The thresholds are 13, 19, 29, 41, 53 and 65 for δ = 3, 5, 7, 9, 11 and 13.
- SOURCE00:138–142 is correct for all primes from 13 to 61.

**Full coverage claim**
- Full coverage needs ⌊(2p+1)/3⌋ ≤ (p+δ*+2)/2. This holds as equality at p = 13 (9 = 9), 17 (11), 19 (13), 23 (15) and 29 (19).
- It fails at p = 31 (21 > 20).
- Since δ* ≤ (p+13)/6, the inequality forces p ≤ 29. So the full list is {5, 7, 11, 13, 17, 19, 23, 29}; the source omits p = 5.

**Residual**
- A residual pair needs (p+δ*+2)/2 ≤ κ̂ ≤ k−1 with 3k ≤ 2p+1.
- There are none for p ≤ 29. At p = 31 the only pair is (21, 20). ✓
- This is sufficiency only; nothing is refuted.

## Findings

**FATAL:** none. **MAJOR:** none.

**MINOR**

- **m1 (SOURCE00:52–53).** "At least 2" is unjustified.
  - Fix: |W| ≥ N−2p−1 ≥ 1 and |W| is even.
- **m2 (SOURCE00:62).** The bound β ≤ p is unjustified when C = V₀.
  - Fix: a minimal zero-sum over Z_p has length ≤ p (SOURCE05:15–17), and β is even, so β ≤ p−1.
- **m3 (SOURCE00:14–16, 63).** Two problems with the import.
  - The import is cited through SOURCE01's list, which still carries "V. Savchev" and the IRC pointer (corrected at SOURCE02:53).
  - The import is used at lengths [p+2−δ, p−1], while SOURCE02:66 records acceptance only at length p−1.
  - Fix: cite SOURCE03:9–11 and state the widened scope. SOURCE03:9 is the general statement, so nothing new needs to be read.
- **m4 (SOURCE00:103).** The parity and properness of ĥ^(p−σ)S are asserted, not shown.
  - Fix: the length is ≡ 1+#even(S) (mod 2), and the length is ≤ p−σ/2 < N.
- **m5 (SOURCE00:107–108).** "Raised to any value" is false as stated.
  - Fix: "every maximal run ends with σ ≥ Σ_U c − K_e, so the run crosses 2δ−2."
- **m6 (SOURCE00:79–82, 96).** "z lies in C" is never used afterwards. Also r ≥ 4−δ.
  - Fix: delete the C sentence or mark it as a remark, and sharpen the bound on r.
- **m7 (SOURCE00:22, 110–111).** Hypotheses are misattributed. P3 also covers δ = 5 in step (8), and P1 is used only as p ≥ 3δ−1.
  - Fix: add the hypothesis map and the remark P1 ⇔ κ ≤ (2p−2)/3.
- **m8 (SOURCE00:124, 137).** S1(e) is cited, but it is unsupplied, unreviewed and redundant.
  - Fix: write "S1(g), δ = 5" and delete S1(e) at line 137.
- **m9 (SOURCE00:120).** The accepted S1+ scope is integer κ ≥ 0 (SOURCE04:51).
  - Fix: write "integer κ ≥ 0".
- **m10 (SOURCE00:127, 131–135).** δ* is defined only for p ≥ 19, and Section 2 has no p-range.
  - Fix: set δ* = 1 for p = 5, 7, δ* = 3 for p = 11, and use the formula for p ≥ 13.
  - State the results "for every prime p ≥ 5, every avoider of length 4p−2" (INV*) and "every word of length 4p−1" (ordered Olson).
  - Cite restricted REFL and the overlay-8 ledger.
- **m11 (SOURCE00:8–10).** The status is stale: S1(d) is accepted (SOURCE02:5). "Sharper at small p" is false for S1(e) as described at line 124.
  - Fix: reword.
- **m12 (SOURCE00:137, 143).** The script is not a premise.
  - Fix: list the thresholds instead, add p = 5 (accepted S1(c), o ≤ 3), and note that the list is complete.
- **m13 (SOURCE00:146–147).** The residual statement lacks the required quantifier.
  - Fix: add SOURCE02:60's quantifier: every admissible normal form is uncovered and (S1) fails, and for INV* also o_F > p.
  - State that (21,20) is the only pair at p = 31, and give the general form (p+δ*+2)/2 ≤ κ̂ ≤ k−1 ≤ ⌊(2p+1)/3⌋−1.
