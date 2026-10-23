# Olson rotation: Lemma S1(d) and its consequences, parent verdict v1

Recorded at 2026-10-18T13:11:08-07:00.

**CORRECTNESS-ACCEPTED relative to the declared classical imports, with the overlay below.** For every prime p ≥ 11 and every integer κ with 0 ≤ κ ≤ (p+3)/2, (ZP) implies (S1). The terminal, uniform INV* and uniform ordered-Olson consequences hold at the hypotheses stated below. This is a partial result. It is not ROT(p), INV*(p), ordered Olson for D_2p in general, or the all-groups target. No novelty claim, no Lean check, no human peer review.

## Text of record

- [S1(d) addendum v1](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation/proof-ROT-ZX-addendum-S1d-v1.md), SHA256 `aefcfc58edfd878b8417d96f278406aedac99bd453c0553fb6979f838d3ac61b`, read through this verdict's overlay.
- Classical import record: [index-one primary statement record](olson-index-one-primary-statement-parent-v1.md), SHA256 `e461514461d23287beeecf04fa26334efd91d3de51caa33312f6c5b10b4d35c6`.
- Upstream accepted scope: [ZX + S1(c) parent verdict](olson-zx-s1c-parent-verdict-v1.md), SHA256 `2f8d376b524bdbac7e0a3ff5fa588744bd26a49b2858c9d0f0bb1db6dbeee6af`, including its mandatory overlay (integer κ, existential normal form, k = 1 by K1, SHgen-E discharge, ordered deletion ledger).

## Exact accepted statements

Notation: elements of Z_2p = Z_2 × Z_p; an odd element is (1, x). For a sequence of odd elements, (ZP) at integer κ excludes zero-sum subsequences of length in [2κ+2, 2p], and (S1) bounds every zero-sum subsequence length by 2κ.

1. **Lemma S1(d).** Let p ≥ 11 be prime and κ = (p+3)/2. Every sequence of odd elements of Z_2p satisfying (ZP) satisfies (S1): every zero-sum subsequence has length ≤ p+3.
2. **Corollary S1++.** For every prime p ≥ 11 and every integer 0 ≤ κ ≤ (p+3)/2, (ZP) implies (S1). This combines the accepted S1+ (κ ≤ (p+1)/2) with item 1.
3. **ROT-ZX++ (terminal).** Let p ≥ 11 and w an avoider of length 4p−2. If some normal form produced by the accepted process has k = 1, or has 3k ≤ 2p+1 and κ̂ ≤ (p+3)/2, then all rotations of w lie in one nonzero pair {ρ_c, ρ_−c}. If moreover o_F(w) ≤ p, then w satisfies INV*.
4. **ROT/INV*-ZX++ (uniform).** Let p ≥ 11. Every avoider of length 4p−2 with o = o_F(w), F = F(w) satisfying **3o ≤ 2p+1 and [o ≤ (p+5)/2 or F ≥ o+p−5]** satisfies INV*.
5. **OLSON-ZX++ (uniform).** Let p ≥ 11. Every word of length 4p−1 over D_2p satisfying the same condition has an identity 2p-subword in increasing index order.

Coverage without an extra F condition (with 3o_F ≤ 2p+1): p = 13: every o_F ≤ 9; p = 17: every o_F ≤ 11; p = 19: o_F ≤ 12, and o_F = 13 when F ≥ 27; p = 23: o_F ≤ 14, and o_F = 15 when F ≥ 33; p = 11: unchanged (o_F ≤ 7). These are sufficient classes; no claim is made that avoiders with these parameters exist.

**Not claimed at p = 5 or p = 7.** At p = 7, κ = 5 the lemma is false: g^13 (5g)^3 in Z_14 has nonempty zero-sum lengths exactly 6, 10 and 16, so it satisfies (ZP) and violates (S1). Both reviewers recomputed this control; the parent recomputed it as well (solutions of a + 5b ≡ 0 mod 14 with 0 ≤ a ≤ 13, 0 ≤ b ≤ 3 are (0,0), (4,2), (9,1), (13,3)).

## Hostile reviews

| Reviewer | Note | Result |
|---|---|---|
| Codex gpt-6.1-sol | [note](olson-rotation-zx-s1d-v1-codex-v1.note.md), SHA256 `60d2ca2767471b4fa90a1daaed6911cc178a1f9edc3a92f1f349a72e9878b488` | S1(d) ACCEPT-WITH-FIXES (bibliographic only); S1++, terminal, uniform INV*, ordered Olson ACCEPT. 0 FATAL/MAJOR, 1 MINOR. All 7 snapshot hashes matched. |
| Claude claude-opus-5-5 | [note](olson-rotation-zx-s1d-v1-claude-v1.note.md), SHA256 `0d84ff8e28f534b09ac4925af35ff516f7c1309a0e515586e1822d51fd84c637` | S1(d) ACCEPT-WITH-FIXES; S1++, terminal, uniform ACCEPT; ordered Olson ACCEPT (1 optional MINOR); tables ACCEPT-WITH-FIXES. 0 FATAL/MAJOR, 10 MINOR (m1–m10). |

Codex read the hash-checked snapshot statically; Claude had no tools and audited the inlined text. Both re-derived Steps (1)–(8) independently. Their agreement is not formal verification.

## Independent parent derivation

The parent read the complete addendum and re-derived every step.

- **(1)** Zero-sums of odd elements have even length. A shortest zero-sum T with |T| ≥ p+5 has N ≥ 2p+2 by (ZP). D(Z_2p) = 2p applied to T minus one term gives a nonempty proper zero-sum. For any such T′, both T′ and T−T′ are shorter zero-sums, hence of length ≤ p+3. So N ≤ 2p+6 and every nonempty proper zero-sum of T has length in [N−p−3, p+3].
- **(2)** EGZ on 2p−1 terms gives T_1 with |T_1| = p and x(T_1) = 0. For M = T−T_1 (odd length N−p, x(M) = 0): an even x-zero V ⊆ M with |V| ≤ p is a proper zero-sum, so |V| ≥ N−p−3; an odd one makes T_1V a proper zero-sum, so |V| ≤ 3. Two disjoint odd x-zero subsets of size ≤ 3 form a proper zero-sum of length ≤ 6 < p−1 ≤ N−p−3. These claims use only |T_1| = p and x(T_1) = 0, so they hold for every such T_1 (Claude m4).
- **(3)** If N ≥ 2p+4, no even V with |V| ≤ p is allowed, so two Davenport applications (|M| ≥ p+4) give two disjoint odd V of size ≤ 3, contradicting Claim B. Hence N = 2p+2 and proper zero-sum lengths are p−1, p+1 or p+3.
- **(4)** With u = (1,0) in M (EGZ chosen among the other 2p+1 occurrences), Davenport in M−{u} gives V. Odd V contradicts Claim B with {u}. Even V has |V| = p−1, and the two leftover occurrences form an x-zero, hence zero-sum, pair of length 2 < p−1.
- **(5)** Davenport in M gives V_0; either |V_0| = 3 (not 1, by (4)) or |V_0| = p−1. In both cases M = C·V with |C| = 3 and V an even zero-sum of length p−1. A proper even x-zero subset of V would be a proper zero-sum shorter than p−1; a proper odd one gives two disjoint odd x-zero subsets of M, both of size ≤ 3 by Claim A, forcing p−1 ≤ 6. So V's x-values form a minimal zero-sum sequence **over Z_p**, as the import requires.
- **(6)** The index-one theorem applies (C_p, length p−1 ≥ ⌊p/2⌋+2 for p ≥ 5). Its generator a is nonzero because the terms are nonzero, so ord(a) = p (Claude m3). p−1 positive integers with sum p are p−2 ones and one two: V = ĥ^(p−2)y with ĥ = (1,h), y = (1,2h), and t ≥ p−2.
- **(7)** A term z ≠ ĥ with coefficient c ∈ [2, p−1]: if c is even, ĥ^(p−c)z is a proper even zero-sum of length p−c+1 ≤ p−1, forcing c = 2; if c ≥ 3 is odd, ĥ^(p−2−c)yz is a proper zero-sum of even length p−c ≤ p−3, impossible. So T = ĥ^t y^u with t+u = 2p+2.
- **(8)** x(T) = 0 gives u ≡ −2 (mod p), so u ∈ {p−2, 2p−2}; u = 2p−2 gives t = 4 < p−2. Hence u = p−2, t = p+4, and ĥ^(p−6)y^3 is a proper zero-sum of even length p−3 < p−1. Contradiction.

The p ≥ 11 hypothesis is used exactly where the addendum says: Claim B and Step (5) need 6 < p−1. The consequences were re-derived: κ̂ = κ(w) − (o−k)/2 ≤ κ(w); the low branch gives κ̂ ≤ k−1 ≤ o−1 ≤ (p+3)/2, the high branch gives κ̂ ≤ p−1−(p−5)/2 = (p+3)/2; o ≤ (2p+1)/3 ≤ p gives restricted REFL on the original word; the ordered deletion ledger (accepted overlay 8) gives o′ ≤ o and F′−o′ ≥ F−o, preserving both branches. The table entries and the residual threshold (κ̂ ≥ (p+5)/2 needs k ≥ (p+7)/2, compatible with 3k ≤ 2p+1 iff p ≥ 19) were recomputed.

## Mandatory overlay (disposition of all findings)

1. **Citation** (Codex MINOR; Claude m1): read "V. Savchev" as **S. Savchev**. Replace the IRC pointer by the parent record [olson-index-one-primary-statement-parent-v1.md](olson-index-one-primary-statement-parent-v1.md).
2. **Davenport citation** (m2): the C_p Davenport proof is the S1(c) addendum's Imports block, lines 15–17; there is no "Sec. 0".
3. **Order of a** (m3): a ≠ 0 because the terms of V are nonzero; hence ord(a) = p.
4. **Claims for every half-sum** (m4): Claims A and B hold for every T_1 ≤ T with |T_1| = p and x(T_1) = 0. Step (1)'s parity remark: lengths are even and p+4 is odd.
5. **Notation** (m5): the generic odd element in the notation paragraph is unrelated to the specific term y = (1, 2h).
6. **Residual notes** (m6): the cross-reference to the (R1)–(R2) results of notes-ZX-residual is informational and unaudited.
7. **Ordered Olson inequalities** (m7, optional): 3o′ ≤ 3o ≤ 2p+1 and o ≤ (2p+1)/3 ≤ 2p−3 are used explicitly.
8. **Residual quantifier** (m8): an avoider is outside this route only if **every** admissible normal form has k ≥ 2 and either 3k > 2p+1, or 3k ≤ 2p+1, κ̂ ≥ (p+5)/2 and (S1) fails. For INV*, also the case o_F(w) > p. Outside 3k ≤ 2p+1 nothing is covered.
9. **Pair list** (m9): the listed residual pairs are examples. The general form is (p+7)/2 ≤ k ≤ ⌊(2p+1)/3⌋ with (p+5)/2 ≤ κ̂ ≤ k−1.
10. **UNKNOWN run** (m10): t-search-v1 run1 is ruled UNKNOWN. Its records are not evidence either way and are not premises.

## Imports and boundary

Classical imports, not re-proved here: D(C_n) = n, EGZ for Z_p, and the Savchev–Chen / Yuan index-one theorem at C_p, length p−1. The parent read the author's statement and definition (Chen, CANT 2016 slides, p. 4, Theorem 1) and the bibliography, not the 2007 proofs. Claude notes that a narrower import suffices (every zero-sum-free sequence of length p−2 over C_p is g^(p−2) or g^(p−3)(2g)); that import is not used here. The accepted ZX/S1+ results and their GRX, PM*, K1, DAV, MULT, SHgen/SHgen-E, restricted REFL and RGR-LONG dependencies enter at the scopes of the ZX + S1(c) verdict.

This is written mathematics relative to explicit imports. No Lean, Comparator or independent kernel; no human peer review; no priority or novelty assessment. No finite search is a premise.
