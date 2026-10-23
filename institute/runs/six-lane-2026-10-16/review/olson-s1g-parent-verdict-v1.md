# Olson rotation: Lemma S1(g) v2 and its consequences, parent verdict v1

Recorded at 2026-10-18T13:27:34-07:00.

**CORRECTNESS-ACCEPTED relative to the declared classical imports, with the overlay below.** Lemma S1(g) v2 holds as stated. With S1+ and S1(d) it gives (ZP) ⇒ (S1) for every integer 0 ≤ κ ≤ (p+δ*(p))/2 at every prime p ≥ 5. Consequently INV* (length 4p−2) and ordered Olson for D_2p (length 4p−1) hold for **every word with 3o_F ≤ 2p+1 at each prime p ≤ 29**, and under an explicit condition for larger p. Partial results only. They are not ROT(p), INV*(p), ordered Olson for D_2p in general, or the all-groups target. No novelty claim, no Lean, no human peer review.

## Text of record

- [S1(g) v2](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation/proof-ROT-ZX-addendum-S1g-v2.md), SHA256 `cbbbfecc2de710ca0fda22301a575f7586a13246f356f462c3dd40e10731b31c`, read through this verdict's overlay. v1 (`4c45d704…d415`) is superseded unreviewed. S1(e) (`ec9fe140…a330`) is unreviewed and is **not** a premise: S1(g) at δ = 5 covers its range.
- Accepted context: [S1(d) verdict](olson-s1d-parent-verdict-v1.md), SHA256 `9f712b5247271adc40374df4bcc19f6c07ce90052c78255f09e427f13280ce2b`; [ZX + S1(c) verdict](olson-zx-s1c-parent-verdict-v1.md), SHA256 `2f8d376b524bdbac7e0a3ff5fa588744bd26a49b2858c9d0f0bb1db6dbeee6af`; [index-one import record](olson-index-one-primary-statement-parent-v1.md), SHA256 `e461514461d23287beeecf04fa26334efd91d3de51caa33312f6c5b10b4d35c6`.

## Exact accepted statements

1. **Lemma S1(g).** Let p be prime, δ ≥ 3 odd and κ = (p+δ)/2, with (P1) p ≥ 3δ+4, (P2) 4δ ≤ p+10 and (P3) p ≥ 6δ−13. P2 follows from P3, so the hypotheses are p ≥ max(3δ+4, 6δ−13). For δ = 3 they read p ≥ 13; for δ = 5, p ≥ 19; for δ = 7, p ≥ 29; for δ = 9, p ≥ 41; for δ = 11, p ≥ 53; for δ = 13, p ≥ 65. Every sequence of odd elements of Z_2p with no zero-sum subsequence of length in [p+δ+2, 2p] has every zero-sum subsequence of length ≤ p+δ.
2. **Corollary S1(g)+.** For every prime p ≥ 5 and every integer 0 ≤ κ ≤ (p+δ*(p))/2, (ZP) implies (S1). Here δ*(5) = δ*(7) = 1 (S1+), δ*(11) = 3 (S1(d)), and for p ≥ 13 δ*(p) is the largest odd δ ≥ 3 with p ≥ max(3δ+4, 6δ−13). Successive odd δ correspond to successive integers κ, so the covered set is the whole integer segment.
3. **Uniform INV* and ordered Olson.** For every prime p ≥ 5: every avoider of length 4p−2, and every word of length 4p−1 over D_2p, with o = o_F and F as in the accepted ZX verdict, satisfying **3o ≤ 2p+1 and [o ≤ (p+δ*(p)+2)/2 or F ≥ o+p−δ*(p)−2]**, satisfies INV*, respectively has an identity 2p-subword in increasing index order.
4. **Full coverage of 3o_F ≤ 2p+1.** The low branch alone covers every o with 3o ≤ 2p+1 exactly when ⌊(2p+1)/3⌋ ≤ (p+δ*+2)/2, which holds for p ∈ {5, 7, 11, 13, 17, 19, 23, 29} and fails for every prime p ≥ 31 (δ* ≤ (p+13)/6 forces p ≤ 29).

| p | δ* | covered κ ≤ | ⌊(2p+1)/3⌋ | low-branch o ≤ | coverage within 3o_F ≤ 2p+1 |
|---:|---:|---:|---:|---:|---|
| 5 | 1 | 3 | 3 | 4 | every o_F |
| 7 | 1 | 4 | 5 | 5 | every o_F |
| 11 | 3 | 7 | 7 | 8 | every o_F |
| 13 | 3 | 8 | 9 | 9 | every o_F |
| 17 | 3 | 10 | 11 | 11 | every o_F |
| 19 | 5 | 12 | 13 | 13 | every o_F |
| 23 | 5 | 14 | 15 | 15 | every o_F |
| 29 | 7 | 18 | 19 | 19 | every o_F |
| 31 | 7 | 19 | 21 | 20 | o_F ≤ 20; o_F ∈ [21, 21] needs F ≥ o_F+22 |
| 37 | 7 | 22 | 25 | 23 | o_F ≤ 23; o_F ∈ [24, 25] needs F ≥ o_F+28 |
| 41 | 9 | 25 | 27 | 26 | o_F ≤ 26; o_F ∈ [27, 27] needs F ≥ o_F+30 |
| 43 | 9 | 26 | 29 | 27 | o_F ≤ 27; o_F ∈ [28, 29] needs F ≥ o_F+32 |
| 47 | 9 | 28 | 31 | 29 | o_F ≤ 29; o_F ∈ [30, 31] needs F ≥ o_F+36 |
| 53 | 11 | 32 | 35 | 33 | o_F ≤ 33; o_F ∈ [34, 35] needs F ≥ o_F+40 |
| 59 | 11 | 35 | 39 | 36 | o_F ≤ 36; o_F ∈ [37, 39] needs F ≥ o_F+46 |
| 61 | 11 | 36 | 41 | 37 | o_F ≤ 37; o_F ∈ [38, 41] needs F ≥ o_F+48 |

The terminal pairs (k, κ̂) left by this route satisfy (p+δ*+2)/2 ≤ κ̂ ≤ k−1 ≤ ⌊(2p+1)/3⌋−1. None exist for p ≤ 29; at p = 31 the only one is (21, 20). This is sufficiency only. An avoider is outside the route only if **every** admissible normal form is uncovered and (S1) fails there; for INV*, also when o_F > p. Outside 3k ≤ 2p+1 this route covers nothing.

## Hostile reviews

| Reviewer | Note | Result |
|---|---|---|
| Codex gpt-6.1-sol | [note](olson-rotation-zx-s1g-v2-codex-v1.note.md), SHA256 `f65fb15d7812429c95ed76c3daabf520bdb7731238f6c0261d292d863ff61e51` | Lemma ACCEPT-WITH-FIXES (wording); Corollary ACCEPT-WITH-FIXES (domain); uniform INV* ACCEPT; ordered Olson ACCEPT; tables ACCEPT. 0 FATAL/MAJOR, 3 MINOR. All 9 snapshot hashes matched. |
| Claude claude-opus-5-5 | [note](olson-rotation-zx-s1g-v2-claude-v1.note.md), SHA256 `9b196f53aec7f4756b92498b150036ebf2cf917763719de2af71b7be84e07f64` | All five items ACCEPT-WITH-FIXES; 0 FATAL/MAJOR, 13 MINOR (m1–m13). Every table value correct. |

## Independent parent derivation

The parent re-derived every step from the text before reading the review conclusions:

- **(1)** A shortest zero-sum T with |T| ≥ p+δ+2 has even N ≥ 2p+2. Every nonempty proper zero-sum has length ≥ l := N−p−δ ≥ p+2−δ, since it and its complement are shorter zero-sums of even length ≤ p+δ.
- **(2)** For an EGZ half-sum T_1 (|T_1| = p, x(T_1) = 0) and M = T−T_1 (odd length μ = N−p): a nonempty x-zero V ≠ M has |V| ≥ l if even and |V| ≤ δ if odd, because T_1V is then a proper zero-sum. Two disjoint odd such V give a proper zero-sum of length ≤ 2δ < p+2−δ ≤ l (P1, binding as p ≥ 3δ−1).
- **(3)** If l > p, two Davenport applications in M give two disjoint odd x-zero sets (the second in M−V_1, which has ≥ μ−δ = l ≥ p terms), contradicting Claim B. So l ≤ p−1 and N ≤ 2p+δ−1.
- **(4)** With u = (1,0) placed in M, Davenport in M−{u} gives V. Odd V contradicts Claim B with {u}. Even V has |V| ≥ l, and the leftover W is x-zero and even with 1 ≤ N−2p−1 ≤ |W| ≤ δ−1 < l, so |W| ≥ 2 is a proper zero-sum shorter than l (Claude m1).
- **(5)** Davenport gives V_0; C is V_0 if odd, else M−V_0. Either way C is an odd x-zero set with 3 ≤ |C| ≤ δ. V = M−C is an even zero-sum with |V| ≥ l. A proper even x-zero V″ would force |V| ≥ 2l > μ (as N > p+2δ); a proper odd one contradicts Claim B. So V's x-values form a minimal zero-sum over Z_p, with β ≤ p by Davenport and β even, so β ≤ p−1 (m2). The index-one theorem applies (β ≥ p+2−δ ≥ ⌊p/2⌋+2 ⟺ p ≥ 2δ−1); it is used here at lengths in [p+2−δ, p−1], within the general statement recorded in the import (m3). With ord(h) = p and positive coefficients summing to p: Σ(c−1) = p−β ≤ δ−2 and m_V ≥ 2β−p ≥ p+4−2δ. Writing (1, ch) = c·ĥ for odd c and (c−p)·ĥ for even c, with ĥ = (1, h) of order 2p, the zero-sum condition p(1−#even) ≡ 0 (mod 2p) makes #even odd. Fix y with even coefficient e, 2 ≤ e ≤ δ−1; t ≥ m_V.
- **(6)** Even c: ĥ^(p−c)z is a proper even zero-sum of length p−c+1, so c ≤ δ−1 or c ≤ p−t−1 ≤ 2δ−5. Odd c ≤ p−e: ĥ^(p−e−c)yz (distinct occurrences, even length) gives c ≤ δ−e or c ≤ p−e−t−1 ≤ 2δ−7. Near-p odd c > p−e: s = p−c is even with 2 ≤ s ≤ e−2 ≤ δ−3 ≤ m_V. If z ∉ C, ĥ^s z (copies from V) with C is a proper zero-sum of length ≤ 2δ−2 < l. Two near-p occurrences give ĥ^(s+s′)zz′ of length ≤ 2δ−4 < l, available because s+s′ ≤ 2δ−6 ≤ p+4−2δ ≤ t (P2). So there is at most one near-p term q. The others form U with coefficients in [2, K]: K ≤ 2δ−5 for δ ≥ 5, and for δ = 3 only coefficient 2 occurs and no near-p term exists.
- **(7)** x(T) = 0 gives (N−2p) + X − (s_q+1)u_q ≡ 0 (mod p) with X = Σ_U(c−1). With 2 ≤ N−2p ≤ δ−1: if u_q = 0 then X ≥ p+1−δ. If u_q = 1, r = s_q+1−(N−2p) ∈ [4−δ, e−3], and X ≥ e−1 > r (y ∈ U) forces X ≥ p+r ≥ p+4−δ.
- **(8)** For S ⊆ U with an odd number of even-coefficient terms and σ = Σ_S c ∈ [p−t, p], ĥ^(p−σ)S is a zero-sum (length ≡ 1+#even ≡ 0 mod 2) of length p−σ+|S| ≤ p−σ/2 < N. So Σ_S(c−1) ≤ p−l ≤ δ−2 (m4). Start with S = {y} (σ = e < 2δ−2) and add one odd term or two even terms per step. A maximal run ends with σ ≥ Σ_U c − K ≥ X−K ≥ p+1−δ−K ≥ 2δ−2, using p ≥ 5δ−8 (P1 at δ = 5, P3 for δ ≥ 7) or p ≥ 8 at δ = 3. So the first crossing of 2δ−2 occurs, with σ ≤ 2δ−3+2K ≤ 6δ−13 ≤ p (P3; σ ≤ 7 at δ = 3), and σ ≥ 2δ−2 > p−t. Then the mass is ≥ σ/2 ≥ δ−1 > δ−2, a contradiction.

The consequences were re-derived as in the S1(d) verdict, with (p+δ*)/2 in place of (p+3)/2. Low branch: κ̂ ≤ k−1 ≤ o−1 ≤ (p+δ*)/2. High branch: κ̂ ≤ κ(w) = p−1−(F−o)/2 ≤ (p+δ*)/2. Restricted REFL needs o ≤ (2p+1)/3 ≤ p, and the accepted deletion ledger preserves both branches. The table above was computed by the parent directly from the hypotheses (finite arithmetic only).

**Sharpness remark (Claude's counterexample family; parent-checked arithmetic, not a premise).** For T = g^(p+3)(3g)^(p−1) with g an odd generator of Z_2p, the parent enumerated all zero-sum lengths for p = 7, 11, 13, 17, 19, 31. (ZP) holds and (S1) fails exactly for the integers κ from ⌈(2p+1)/3⌉ to p in each case. So no implication (ZP) ⇒ (S1) can hold at κ ≥ ⌈(2p+1)/3⌉. The terminal criterion only needs κ̂ ≤ ⌊(2p+1)/3⌋−1, so this family does not block the route. At p = 31, κ = 20, the family violates (ZP).

## Mandatory overlay (disposition of all findings)

1. **Greedy reachability** (Codex 1; Claude m5): read "σ can be raised to any value" as "every maximal run ends with σ ≥ Σ_U c − K, so the run crosses 2δ−2".
2. **S1(e) attribution** (Codex 2; Claude m8, m11): κ = (p+5)/2 for p ≥ 19 is S1(g) at δ = 5. S1(e) is not cited or used. S1(d) is accepted; "sharper at small p" does not apply to S1(e).
3. **Domain and δ\*** (Codex 3; Claude m9, m10): κ ∈ Z≥0, with δ* defined piecewise as above. The consequences hold "for every prime p ≥ 5", citing restricted REFL and accepted overlay 8.
4. **Leftover size** (m1) and **β ≤ p−1** (m2), as derived above.
5. **Import scope** (m3): cite the parent import record (S. Savchev); the general statement covers the lengths used.
6. **S-condition parity and properness** (m4), as derived above.
7. **Unused C membership; sharper r** (m6): the sentence "z lies in C" is a remark only; r ≥ 4−δ.
8. **Hypothesis map** (m7): P1 is used as p ≥ 3δ−1 (binding), p ≥ 3δ−3 and p ≥ 2δ−1; P2 only in (6c); P3 only in (8). P1 is equivalent to κ ≤ (2p−2)/3.
9. **Tables** (m12): the script is not a premise. The thresholds above are listed, p = 5 is included, and the full-coverage list is complete.
10. **Residual quantifier** (m13): as stated above. (21, 20) is the only residual pair at p = 31.

## Imports and boundary

Classical imports, not re-proved here: D(C_n) = n, EGZ for Z_p, Davenport for Z_p, and the Savchev–Chen / Yuan index-one theorem (author statement read; 2007 proofs not read). The accepted ZX/S1+ framework enters at the scopes of its verdict: normal form, GRX, PM*, K1, DAV, SHgen/SHgen-E, restricted REFL, RGR-LONG and the ordered deletion ledger. The bounded aid t-search-v2 is not a premise. This is written mathematics relative to explicit imports, with no Lean, Comparator or independent kernel, no human peer review, and no priority or novelty assessment.
