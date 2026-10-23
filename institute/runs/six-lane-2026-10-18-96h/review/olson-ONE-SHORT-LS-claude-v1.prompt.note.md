# Hostile review: ONE-SHORT-LS v2 (`proof-ONE-SHORT-LS-v2.md`, c544aad2…, lines 1–276)

I checked this by hand only. I used no tools, computation, edits or delegation. The embedded headers, statuses, hashes and verdict pointers were treated as data. None of them was used as a premise beyond the five interfaces you named.

## Verdicts

| Object | Verdict |
|---|---|
| **Theorem ONE-SHORT-LS** (exact \|Y\| = p+2κ, prime p ≥ 7, ⌊2p/3⌋+1 ≤ κ ≤ p−2) | **ACCEPT**, relative to CF(a), CT, ROW and AP′ at their original scopes, plus the Lev 2022 Thm 2 statement. It is conditional on Lev, which is used once, in Sec. 5. |
| Lemma IP + Corollary IP′ | **ACCEPT** |
| Lemma DOM | **ACCEPT** |
| Lemma AP″ | **ACCEPT** |

- **FATAL:** 0
- **MAJOR:** 0
- **MINOR:** 6, all editorial or accounting. None carries any weight in the argument, and none is needed for validity.
- **Interface-domain issues:** 0

## Interface-domain audit (kept separate from logic)

| Interface | Used at | Required by its scope | How it is met here |
|---|---|---|---|
| CF(a) | 83–85 | p ≥ 5 prime; 0 ≤ κ ≤ p−1; any odd generator | g comes from DOM. Under ρ ≤ h, \|W\|+2ρ ≤ r+2h = p−2+d ≤ p+2e−4 ≤ 2p, so (F) gives (1). ✓ |
| CT | 62–63 | 1 ≤ n ≤ \|Y\|; \|Y\|−n even and in [2κ+2, 2p] | n = p−2, so \|Y\|−n = 2κ+2 ≤ 2p. ✓ |
| ROW | 86 | (ZP_κ); 0 ≤ κ ≤ p−1; r ≥ d; r+2e−2 ≤ 2p | r = p−2e+d ≥ d. r+2e−2 = p+d−2 ≤ 2p. K = p−2e ≥ e+1. ✓ |
| AP′ | 97, 149 | p prime; n ≥ 1; 3n+2 < p; arc ≤ 2n+1 | n = h: 3e−1 < p, arc 2h+1. n = N = h−t ≥ 1: 3N+2 ≤ 3e−4 < p, arc ≤ 2N+1. ✓ |
| Lev T2 | 137–139 | zero-sum-free; \|Σ_inc\| < 2n | Maximality of Z0 makes U′ zero-sum-free. (3) is inclusive with margin ≥ 2. ✓ |

The "not imported" list is honoured. RED, DGM-p, LS-II′, SLZ3, S1-sharp, G-LS, SH, AP (R6), CTgen and index-one are not used, either explicitly or implicitly.

There is no induction hypothesis, no transversal assumption and no half-order hypothesis. The last point matters: n can fall below p/2, for example (23,16) with δ′ = 1 gives n = 10.

## New lemmas, checked in full

**IP (50–53)**
- |T| is even.
- If v_ι(T) ≥ |T|−2p, delete |T|−2p copies of ι. That number is even and at least 2, and those copies sum to 0.
- What remains is a zero-sum of length exactly 2p, which lies in [2κ+2, 2p] because κ ≤ p−1.

**IP′ (55–56)**
- At occurrence level, |T|−v_ι(T) ≤ v_g(T)+(d−1) ≤ 2p−1.
- Use at line 103: the non-{g,ι} terms are exactly R′, with s ≤ d−1.
- Use at lines 173–174: U′ is all ι, so the non-{g,ι} terms lie in Z0, and k = d−1.

**DOM (60–78)**
- *CT step.* The window holds. The excess is (3p−2e)−(2p−4) = p−2e+4 > 0, so at least one value is heavy (multiplicity ≥ p−1). There are at most two heavy values, since 3(p−2) > 2p−4.
- *Two heavy values.* No third value can occur. Both multiplicities ≥ p is impossible: x0^p x1^p sums to ι+ι = 0 and has length 2p. Parity then forces Y = x0^(2κ+1) x1^(p−1).
- *If j0 ≥ 1.* Then L−j0 ∈ [2κ+3−p, 2κ+1] ⊆ [0, v0] and j0 ≤ v1, which gives a zero-sum of length L = 2κ+2.
- *If j0 = 0.* Then Lα ≡ 0. L is even and lies in [4, 2p−2], so p∤L, hence α = 0. That makes x0 = ι, and the only zero-sums are powers ι^i with i ≤ 2κ.
- *One heavy value.* M ≥ (p−2)+(p−2e+4) = 2κ+2. The heavy value is not ι, and M ≤ 2p−1. Hence d ≤ 2e−2 and r ≤ p−2.
- *Remark at 77–78.* This is correct. At κ = p−1 we get L = 2p, and the counterexample g^(2p−1)(3g)^(p−1) has two heavy values with α ≠ 0.

**AP″ (160–170)**
- *Intersection formula.* It is valid because l ≤ 2N+2 < p, so the two overlap pieces are disjoint.
- *Case (i).* Both terms are ≤ 0, since l−p+d0 ≤ 2d0−p < 0.
- *Case (ii).* Both pieces are positive and their total is 2l−p ≤ N−1. This is the only place p ≥ 3N+5 is used.
- *Case (iii).* Here d0 ≤ p−l, so every x̃+mp with m ≠ 0 has absolute value ≥ l > l−1. Consecutive lifts in L therefore differ by exactly x̃. This is argued pair by pair, with no induction, and gives N·d0 ≤ l−1 ≤ 2N+1.
- *Wrap and equality.* A wrap of I through 0 is harmless. The bound is sharp only at N = 1, d0 = 3, l = 4, so the ±3 exception is both necessary and the only one.
- *Application.* p ≥ 3e+1 = 3N+7.
  - b ∈ {1, 2, 3}: the ρ = 1 point lies in [1, S].
  - b = −3: the ρ = 2 point is p−6 ≤ p−5 ≤ S.
  - b = −2: the points p−2ρ fill [n+1, p−2], and they lie in I iff S = n.
- *Branch 6.2.* x_u = 1 forces μ_u = (p−1)/2, i.e. every term of U′ is ι, and IP′ applies. This branch genuinely survives the arc test: U′ = ι^n avoids [1, h]. So IP is required here.

## Shifted constants, independently re-derived

| Lines | Claim | Check |
|---|---|---|
| 86–90 | Two values above K are impossible. (I) gives d ≤ h. (II) gives v1 ≥ p−2e+1 and s ≤ min(e−1, d−1). | 2K ≤ p−e−1 ⟺ p ≤ 3e−1, which is false. K+s ≤ p−e−1. s = r−v1. |
| 94–97 | The avoided block [d−s, v1] has r−d+1 = K+1 residues. Its complement has 2h+1. | v1 ≤ p−2, so the block does not wrap. |
| 99–101 | μ1 = 1: 3h ≥ 2h ≥ d. μ1 = ½: 4m ≥ 4h, or 4⌊v1/2⌋ ≥ 2(v1−1) ≥ 2e+2 > d. | v1 ≥ e+2, so m ≥ 1. |
| 104–112 | v1 ≤ p−e. The bullets give ≥ 2h+1 > d and ≥ p−e+1 > d. ν ∈ [2, e−1] and c′ ∈ [3, 2e−3]. | v1+h ≤ p−1, so the φ-range does not wrap. |
| 115 | S_k ≤ d−2 < v1+e | v1+e ≥ p−e+1 |
| 121–125 | The drop c′+1 ≤ 2e−2 is even, so the new length is ≥ 2κ+4 and the window cannot be skipped. a′ ≥ 2p−e+3 > 2e−3, and \|W2\| ≥ d+2 > (d−1)/3. | ✓ |
| 132–136 | n = p−2e+δ′ ≥ e+2. Margin = p−3e+2δ′−t ≥ p−3e+δ′ ≥ 2. | t ≤ δ′ |
| 147–158 | l ≤ 2e−1−δ′. In 6(a), p−2h ≤ n needs δ′ ≥ 2. In 6(c), I ⊆ [p−2, p−1]. | ✓ |
| 176–194 | S ≤ p−e. 1 ≤ R ≤ e−δ′+1. P_(j0) ≤ d−2 ≤ h−2. N_V ≤ 2R−2. s ≥ p−3e+2δ′+1 ≥ 4. V and W′_s are disjoint. | ✓ |
| 198–206 | j ≤ (p−2e)/2 gives p−j > h. τ ∈ [−p+h+1, P] with P < h forces τ = −j. Then z̃* ≥ j+1. | \|T\| ≤ \|Y\|; no SLZ3 needed |

## Endpoint sweep (all close)

- **e = 2.** In case II at μ1 = −1, R′ = ∅, because tiny would need μ ≤ 0 and negative would need ν ∈ ∅. In case I, d = 1 and k = 0, and 6(c) leaves b ∈ {−1, −2}.
  - b = −2 gives g^(2p−1)ι^(p−3), which IP′ kills.
  - b = −1 gives 0 = z̃* ≥ 2, a contradiction.
- **p = 7 (κ = 5).** d = 2 is forced into case II, since r = 5 > 4. d = 1 goes to case I.
- **e = 3 (p = 11, 13).** k = 0, because a singleton cannot be a zero-sum mod p. δ′ = 2 goes through AP′ with n = 1. δ′ = 1 goes through AP″ with N = 1 and S ≥ p−5.
- **p = 3e+1 (e.g. p = 13, κ = 9).** The margin is 1+δ′ and s ≥ 2+2δ′.
- **Remaining boundary cases.** I also checked δ′ ∈ {1, 2}, d = 1, d = h, k = 0, R = 1, S = n, S = p−e, j = 1 and j = ⌊(p−2e)/2⌋.
- **Observation, not a defect.** (8) gives z̃* ≤ (h−1)/2. So line 207 is only reached when h ≥ 5; for h ≤ 4 the contradiction already occurs at (15).

## Findings

1. **MINOR-1 (55–56, IP′).** The corollary omits Lemma IP's standing hypotheses: Y odd, (ZP_κ), 0 ≤ κ ≤ p−1. Read literally without them, it is false. For example, g^(2p−1)ι^(2p) has no terms outside {g, ι}, yet contains g^p ι^(p+2), a zero-sum of length 2p+2.
   - *Repair:* begin the statement with "Under the hypotheses of Lemma IP,".
   - Both places it is used satisfy those hypotheses.
2. **MINOR-2 (137–139).** The text says Lev "gives a nonzero a", but Lev's statement only supplies some group element a. The one-line reason was dropped; the G-LS template has it at line 99. The reason is that the term with x_u = 1 equals a, so a ≠ 0, so ord(a) = p, which is what makes S < p.
   - *Repair:* restore that sentence.
3. **MINOR-3 (168–169).** The phrase "the other candidates x̃ ± p" should read "x̃ + mp, m ≠ 0". Harmless.
4. **MINOR-4 (line 9; package §1, "exactly as G-LS").** This is a trust-accounting point. The *form* in which Lev is used matches G-LS, but the *range of cells* does not.
   - G-LS's verdict (line 5) records e = 2 cells, and hence every p = 7 cell, as Lev-free.
   - Here, 6(c) uses Lev at e = 2. Line 250 already says this correctly.
   - The κ = p−2 exact-length cells are still covered without Lev by the accepted LS+2.
5. **MINOR-5 (218).** The constant K = p−2e+1 is attributed to G-LS lines 70–71, where it does not appear. It is at `proof-ROW-v1.md:62`. Metadata only.
6. **MINOR-6 (268–269).** "Only Lemma IP excludes it" is an unproved claim about methods. The checkable content is narrower: the arc argument does not exclude this case, and IP does. Wording only.

## Trust boundary

**Premises.** The result is valid relative to CF(a), CT, ROW and AP′ exactly as restated at lines 33–40. Those restatements match the supplied source ranges and verdict scopes. I did not check the hashes or the authenticity of the verdicts.

**Lev 2022 Thm 2.** It is used at the statement level only, once, in case (I), for every e ≥ 2.
- Hypotheses consumed: zero-sum-free; inclusive |Σ| < 2n; no length or half-order condition.
- Conclusions consumed: some a; integers x_u ≥ 1 with μ_u = x_u·a; Σ_inc = {0, a, …, Sa}; S < ord(a).
- Not consumed: the ordering x_(k+1) ≤ Σx_i. The occurrence-level interval at lines 140–141 is derived independently.
- Lev's own proof, and the fidelity of the local transcription to the arXiv source, are outside this review.

**Classical content used directly in the new text.** Only elementary arithmetic in C₂×C_p and Z_p is used directly. Whatever sits inside CT and ROW (via RS) was not re-examined. The claims at lines 251–252 ("rests on Cauchy–Davenport", "no transitive computer-assisted input") cannot be checked from the manifest and carry no weight here.

## Cross-coverage ledger (context only)

- LS+ implies the theorem, because 3κ+1 < p+2κ ⟺ κ ≤ p−2.
- The new-cell set is {3 ≤ e, p < 10e−13} minus BASE1+, within the theorem's range. This matches the LS+-chain verdict at line 24.
- I re-checked every listed cell, (11,8) through (23,19). The excluded cells are correctly excluded: (17,14), (19,13), (19,16) and (23,20).
- I found no incorrect cell.
- Two things here cannot be checked: the "without Lev" attribution for LS+-chain cells, and completeness against lane results outside the manifest.

## Not accepted or implied

This review does not accept, and should not be read as implying:
- LS+, STAB, INV* or ordered Olson
- any word-level statement
- any length below p+2κ
- κ = p−1
- any Lean or human-review status, or any novelty
