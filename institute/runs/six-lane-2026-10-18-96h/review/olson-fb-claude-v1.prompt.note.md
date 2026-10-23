# Referee report: proof-FB-v1 (`339dcadc…cc6b`)

This is a text-only audit against the embedded accepted sources. I ran no computation. The two p = 7 examples below were checked by hand and illustrate the argument; they are not premises.

## Verdicts

| Item | Verdict |
|---|---|
| (1) Lemma FB | **ACCEPT** (0 FATAL / 0 MAJOR) |
| (2) Corollary FB-E | **ACCEPT** (0 FATAL / 0 MAJOR) |
| (3) Theorem ROT-FB | **ACCEPT-WITH-FIXES**. Clause (a) is accepted as written. Clause (b), k = p, is arithmetically correct but needs its k = p caller discharge made explicit (R1). The Sec. 4 T-MAX Remark cannot be accepted under its name (R2). |
| (4) Corollary INV*/OLSON-FB | **ACCEPT**. It uses only clause (a), so R1 and R2 do not affect it. |

I attacked Lemma FB hardest and could not break it. BAL-forall's L ≥ 2t+1 came from its prefix-window witness, not from the mathematics.

## (1) Lemma FB

**What ZSTRUCT actually needs.** Write z = rg with r odd in [1, 2p−1]. There are three cases:
- r = 1, so z = g.
- 3 ≤ r ≤ W is impossible: REALIZE gives Q ⊆ Y′ of weight r with |Q| ≥ 2, so (Z−z)Q would be a longer zero-sum.
- r ≥ W+1 gives s = 2p−r ≤ 2p−1−W = slack.

So s_i ≤ slack needs only that Z is longest, plus REALIZE. REALIZE needs only L ≥ p+1 and W ≤ 2p−1; its n = 1 case uses X_i ≥ L−1 ≥ p. The unit count is needed only for the separate bound s ≤ 2t−1, because g^s·z must exist.

**Setting fact.** slack ≤ 2p−1−L−2h and m = L−h, so m − slack ≥ 2L−2p+1+h ≥ 3+h. This uses only L ≥ p+1. No step relates L to t, and every step holds verbatim for any index-<1 generator (BAL-full overlay 5).

**First crossing.** Each s_i ≤ δ−1, so if S(N) ≥ δ then δ ≥ 2 and r ≥ 2. Put x = r−1 ≥ 1. Then x ≤ S_{r−1} ≤ δ−1, and x·s_(r) ≤ S_{r−1} because the order is decreasing.

**y + r ≤ δ, rederived in integers.**
- y + r = S_{r−1} + s_(r) − δ + x + 1 ≤ x + s_(r).
- (x−1)(s_(r)−1) ≥ 0 gives x + s_(r) ≤ x·s_(r) + 1 ≤ δ.
- The candidate's convexity form is equivalent and correct: f(u) = (δ−1)/u + u has f(1) = f(δ−1) = δ.
- Also 0 ≤ y ≤ s_(r)−1 ≤ slack−1 ≤ m−4, so the y units exist in Y′.

**Z\*.**
- Z* is Y with y units of Y′ and the r largest negatives of N removed. Its three pieces are occurrence-disjoint parts of Y′ and Z, so it is a genuine subsequence of Y.
- Integer coefficient sum: (W−y) + n₊ − (S(N)−S_r) = W + δ + n₊ − S(N) = 2p + n₊ − S(N).
- That sum is ≡ 0 mod 2p because σ(Z) = 0 gives S(N) ≡ n₊. It may be 0 or negative, which does not matter.
- Length: R − (y+r) ≥ L + 2t − (2p−W) ≥ 2t + 2, since W ≥ L ≥ p+1.

**Degenerate cases.**
- t = 0, or n₋ = 0: n₋ = 0 forces t = 0, because 2tg ≠ 0 for 0 < t < p. Then S(N) = 0 and there is nothing to prove.
- slack = 0: then N = ∅.
- y = 0: all of Y′ is used.
- r = n₋: the computation is unchanged. With n₊ = 0 this case is vacuous, since S_r ≤ 2δ−2 < 2p.

**Balance.** 0 ≤ S(N) ≤ slack ≤ 2p−1 and 0 ≤ n₊ ≤ 2κ ≤ 2p−2. Since S(N) ≡ n₊ mod 2p, S(N) = n₊ and W + n₊ ≤ 2p−1. Remark (i) is accurate.

**Why it escapes L ≥ 2t+1.** The witness deletes at most δ = 2p−W occurrences from all of Y. The length gain comes from L + W ≥ 2p+2, which follows from L ≥ p+1 alone. BAL-forall compared two prefix-exchange bounds, f ≤ 2t and f ≥ 2p−e′, and that comparison is what consumed L ≥ 2t+1.

**Attack attempts (p = 7, Z₁₄, g = 1, hand-checked).**
- *Unbalanced shape attempt.* Take Y = 1⁸·9·11·13⁶ and Z₀ = 9·11·13⁶, so S(N) = 14 and n₊ = 0. The ZSTRUCT shape constraints hold. FB's witness gives δ = 6, r = 2, y = 2 and Z* = 1⁶·13⁶ of length 12, so Z₀ is not longest. The attack fails exactly where the proof says it must.
- *Sharp instance outside every older lemma.* Take k = 6, κ = 4, Y = 1¹³·11·13² (R = 16).
  - The zero-sums are 1^(3b+c)·11^b·13^c, of length 4b+2c ≤ 8, so (S1) and (ZP) hold.
  - Z = 1⁵·11·13² is longest, with L = 8 = 2t. BAL-forall does not apply, 2κ+k = 2p, and κ > (p−1)/2.
  - Here S(N) = n₊ = slack = 5, W+n₊ = 13 = 2p−1, m−slack = 3, and E = 2 = k−1−2κ+n₊.
  - So FB, the Setting fact and FB-E all hold with equality.

## (2) Corollary FB-E

Every step checks:
- n₊ ≤ 2p−1−W ≤ 2p−1−L = k−1−2κ+2t ≤ k−1, using t ≤ κ.
- a_i ≤ 1+e′ ≤ 2p−L ≤ k ≤ p−1, so a_i ≤ p−2 since a_i is odd.
- s_i ≤ slack ≤ k−1 ≤ p−2.
- E = e′+n₊−n₋ ≤ 2p−1−L−n₋ = k−1−2κ+n₊, using L+n₋ = R−n₊.

Since every |b| ≤ p−2, these coefficients are the canonical K01 representatives. So this E is exactly SHgen's E_c, and no ρ₀ occurs (Y(0) = pg would need a_i = p or s_i = p).

Byproduct: n₋ ≤ S(N) = n₊ gives t ≤ n₊ ≤ k−1, a sequence-level analogue of DAV. It is consistent with κ̂ ≤ k−1 in the t = κ̂ cells.

## (3) Theorem ROT-FB

- **(S1).** For κ̂ ≤ ⌊2p/3⌋, S1-sharp gives (S1) from GRX's (ZP); otherwise (S1) is a hypothesis. Since κ̂ ≤ k−1 ≤ p−2 < p, setting (S′) holds in clause (a).
- **(H) as needed: E ≤ 2H = 2p−2−2κ̂.** The bound n₊ ≤ k−1 gives E ≤ 2k−2−2κ̂, which is ≤ 2H exactly when k ≤ p. This uses the k−1 bound on n₊, not the 2t−1 bound.
- **(K) as needed: η + a_max ≤ 2p−1−k.** KETA's k-free inequality gives η + a_max ≤ E+2 ≤ k+1−2κ̂+n₊.
  - t ≥ 1: n₊ ≤ 2κ̂−1, so η + a_max ≤ k, which is ≤ 2p−1−k exactly when k ≤ p−1.
  - t = 0: η + a_max ≤ k−1.
- **k = p clause.**
  - The worry is real: if t = κ̂ then L = p, and neither SC0 (needs length > p) nor REALIZE's n = 1 case (needs X_i ≥ p) applies.
  - Hypothesis (b) forces t ≤ κ̂−1, so L = p+2κ̂−2t ≥ p+2.
  - Every use of k ≤ p−1 in (S′), FB and FB-E is then only through L ≥ p+1, 2p−1−L ≤ p−2 and t < p.
  - (H) holds with E ≤ 2H.
  - (K): for t ≥ 1, η + a_max ≤ p−2; for t = 0, η + a_max ≤ p+1−2κ̂ ≤ p−1 = 2p−1−k.
  - The arithmetic is correct. The open item is R1.

## (4) Corollary INV*/OLSON-FB

- κ(w) ≤ ⌊2p/3⌋ is exactly equivalent to F−o_F ≥ 2(p−1−⌊2p/3⌋).
- For every admissible normal form, k ≤ o_F ≤ p−1 and κ̂ = κ(w)−(o_F−k)/2 ≤ min(k−1, ⌊2p/3⌋). So S1-sharp always applies, and only clause (a) is used.
- k = 1 goes to K1; κ̂ ≤ 1 goes to K01.
- Restricted REFL applies at o_F ≤ p−1 ≤ p.
- Deletion ledger:
  - Case 1 uses o ≤ 2p−3.
  - Case 2 gives (o−1, F−1), so F−o is unchanged.
  - Case 3 gives (o or o−2, F), so F−o does not decrease.
  - Both side conditions persist, every relevant deletion lands in (a), and RGR-LONG closes.
- Spot check, p = 7, (o_F, F) = (6, 10), the only p = 7 cell not already covered by S1-sharp or ZB+. DAV excludes k = 2, leaving k ∈ {4, 6} with κ̂ ∈ {3, 4} ≤ 4.

## Findings

**FATAL:** none. **MAJOR:** none. I found no counterexample to any of the four statements.

### MINOR, required

- **R1 (ROT-FB (b), Sec. 4, SHgen/SHgen-E step).**
  - **Issue:** the caller discharge is copied from the ROT-ZR verdict, where it was recorded for o_F(u°) ≤ k ≤ p−1. At k = p, restricted REFL (o_F ≤ p) still applies. But the packet does not show that SHgen's accepted statement imposes nothing beyond (H) and (K) at k = p, or that the V3 caller covers o_F(u°) = p. ZX overlay 4 ("≤ p, cite generalized V3") suggests it does.
  - **Repair:** add one sentence citing that scope, for example ZX overlay 4, or the ROT-KP verdict if it used SHgen at k = p.
  - **If it cannot be cited:** clause (b) is unsupported, which would be MAJOR for (b) only. Clause (a) and item (4) are unaffected.
- **R2 (header and Sec. 4 Remark).**
  - **Issue:** "ROUTE-ALL(T)" and "obstruction family of the kind (ii)" are defined only in the frozen scope file, not in the packet, so they should not be accepted by name. Also, if (T) fixes the longest zero-sum length at 2κ, then (S1) is automatic and "(S1) assumed when κ > ⌊2p/3⌋" is redundant.
  - **What is acceptable:** in (S′) with 2 ≤ k ≤ p−1, any longest Z and any index-<1 generator give E_c ≤ 2H, and either E_c = 0 or η_c + a_max,c ≤ 2p−1−k.
  - **Repair:** inline the definition, or restate the header sentence as that content.

### MINOR, optional

- **O1 (FB, the y + r step).** Replace the convexity line with the integer inequality (x−1)(s_(r)−1) ≥ 0. It also exposes the equality cases.
- **O2 (ROT-FB (b) statement).** "(S1) at κ̂" is implied by "every zero-sum has length ≤ 2κ̂−2". Restate (b) as: k = p and every zero-sum has length ≤ 2κ̂−2. For κ̂ ≤ ⌊2p/3⌋ this is equivalent to having no zero-sum of length exactly 2κ̂.
- **O3 (Sec. 2 Remark (ii)).** The BAL-full parent derivation records ROOM's W-bound as using only longestness. "Without ROOM's hypothesis L ≥ 2t" may therefore misdescribe ROOM. Say "recovers ROOM's W-bound" instead.
- **O4 (Sec. 6).** Residual (ii) at k = p should exclude κ̂ ≤ 1, which accepted ROT-KP covers. "Contains the ZX terminal criterion" holds only for k ≥ 2 and κ̂ ≥ 1; κ̂ = 0 goes to K01. Neither point is load-bearing.
- **O5 (FB-E).** State in FB-E itself, not only in Sec. 4, that the canonical representatives make this E equal to SHgen's E_c. Optionally also record t ≤ n₊ ≤ k−1.
