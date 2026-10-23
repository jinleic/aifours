# FQW v1 hostile written review (worker erratum 1 and parent erratum v1 applied)

**Counts: FATAL 0 · MAJOR 0 · MINOR 1** (wording only, not load-bearing).

**Verdict.** With the governing errata applied, every load-bearing step of Theorem FQW (proof LF14-19) re-derives from the literal pasted interfaces. I found no missing premise, scope violation or circularity.

The theorem remains conditional on its accepted imports. These were checked for literal-interface use only, not re-proved:
- NF, LF28-43
- GRX, LF7-20
- SC0, LF1-11
- ZSTRUCT/FB in (S′): FB LF11-19, balfull LF33

This review does not approve the research target, full ordered Olson, or runtime.

## Governing errata, confirmed independently

- **m1 (Lemma 8(b), proof LF158).**
  - With v even and all labels odd, |J0| ∈ {0,2}. Every branch at LF166-179 then closes, with sizes in [4, 3κ−4] ⊂ [4, R−4].
  - The narrowing is necessary. For odd v the unrestricted text is false: with q(P)=0, v=1 is reachable only by a single unit letter.
  - The only consumer is Lemma 9(c) (LF194), and its v is even (LF181). Lemma 9(b) uses only 8(a). Nothing downstream changes.
- **m2 (proof LF402).** At t=4, (41−5t)/2 = 21/2, so m1 ≥ 11 holds only by integrality. The consumer at LF95 (u1 ≥ s_j + m1) needs only m1 > 10. Nothing downstream changes.
- **Parent-check wording.** Proof LF95 already uses the non-strict form m1 ≥ (5κ−4)/2 > 10. Confirmed.
- **Worker erratum 1.**
  - Item 1: the bound 9.5 gives |A^c| ≥ 10 by integrality. The consumers need only |A^c| > 4 (LF370) and |A^c| − 2 > 2 (LF382).
  - Items 2 and 3 are correct clarifications.

## Claim-wise verdicts (all CORRECT)

1. **Import uses.**
   - **Lemma 1 (LF46-54).** Take z_i = −1 on P. Since every l_i is odd, δ = N−2m and C_max = 2H+2m. Also T(z) = −Σ_{i∉P}τ_i = T(P), and 2p−2H = 2κ+2.
   - **SC0 (LF67-74).** The length is L+1 ≥ p+2 = ⌊2p/2⌋+2. Since L+1 > p positive coefficients sum to ord g, ord g = 2p.
   - **(S′) at (k′,κ′) = (p−1, κ−1) (LF75-81).** R = 2p+2κ′−k′; (S1) at κ′ comes from LF64-66; t ≤ κ′; L ≥ 2p−k′ = p+1; g is odd with W ≤ 2p−1.
   - **Balance.** S(N) ≡ n+ (mod 2p) and both lie in [0, 2p−1], so S(N) = n+.
   - **Empty-run rule.** It enters only through Lemma 12(f).

2. **Label margin u1 ≥ |b|+9 (LF86-96).**
   - a-label b: u1 − b ≥ (7κ−9−b)/2 ≥ 2κ−1, using b ≤ 3κ−7. This is 9 at κ=5.
   - Label −s_j: u1 − s_j ≥ m1 ≥ 11.
   - Unit letter: u1 ≥ (7κ−6)/2, so u1 ≥ 15 at κ=5.
   - Lemmas 7 and 8 actually need only u1 ≥ |b|+6.

3. **Minimal representations missing ≤ 6 letters (Lemma 7, LF142-154).** The replacements need only u1−6 ≥ b and u1−5 ≥ x.

4. **Exception lists and (λ,μ) tables (Lemmas 9-11, LF181-231).**
   - I re-derived all three tables exactly.
   - The parities of x and y equal the parity of q, as Lemma 10 requires.
   - λ+μ ≤ 6 holds in every table.
   - Symmetry (ii) and the per-set bounds (iii) are correct, including the [q=R] terms.
   - The self-dual window [4, R−4] loses at most 3 per side, and only when min(q,q′) ≤ 2.

5. **θ pair-independence (Lemma 12(c)-(f), LF243-276).**
   - Per-type X maxima are max(14−c,7), max(12−c,8), max(10−c,6) and 8.
   - c_X + c_Y = 2R − r_i ≥ R, so the generic bound is Xmax+Ymax ≤ 21.
   - In the one-run branch c_Y = 0, X = −2, 0, 2, 4 and Y = 14, 12, 10, 8, so the sum is ≤ 18.
   - The c_X = 0 branch is vacuous because |A^c| ≥ 10, but it is harmless.
   - At κ=5: 2D0+21 ≤ 25 < 26, which needs B* ≥ R = 22.
   - Lemma 12(f): |θ_e| ≤ D0+14 < 2p.

6. **Additive constant (Lemma 12(a), (F4)-(F5); LF250-253, LF304-313).**
   - Δ ∈ [M0−6, 4p+6−B*] ⊂ [3, 4p), using M0 ≥ 2κ−1+E/2 ≥ 9 (LF131-135).
   - At N=14, P1∪P2 has intervals {0,1}, {3,4}, {6,7}, {9,10}.
   - x=12 has both neighbours (11 and 13) outside P1∪P2, so m = 5.

7. **Connectivity and total ((F1)-(F3), (F6); LF278-316).**
   - The separator counts are 2κ−7 ≥ 3 and 2κ−8 ≥ 2.
   - The gap normal form is (1,…,1,2κ−7).
   - (F3)(c) handles exactly κ ∈ {5,6}, with gaps (2,2,2,2,1) and (2,2,2,2,2,2).
   - Θ(all) = −(2κ−6) + e* − 2ν0.

8. **Final count (Sec. 5, LF320-392).**
   - (BI) holds, and ε_ev + ε_od = 2 + e*.
   - The case split by type G/P/Q and value of t_S is exhaustive:
     - Type G forces t ≤ −1.
     - Type Q forces t ≤ −1 (13(c)).
     - Type P with t = 0 is case H.
   - Lemma 15(a)-(c) are correct; in 15(b) the assumptions reduce to κ ≤ 4, a contradiction.
   - **Lemma 14 (LF354-362).** First w_κ ≤ −2; then w_{κ−1} ≥ e* ≥ 0, so w_{κ−1} ≥ 2. Its premise ν0 ≤ 2 is supplied by case H.
   - **Lemma 15(d) at κ=5.** It sends exactly the sub-case n_{B1} = 2 to Lemma 14. No sub-case is dropped.

9. **(5,13) and (6,17) (LF397-425).** All numbers check, with m2 applied, except MINOR-1 below.

10. **All-equal and degenerate configurations.** No step assumes two distinct rotation values, a second nonempty run, o_F, or rotation pairs. The one-run extreme is exactly the c_Y = 0 branch. The statement at LF395 is accurate.

## MINOR-1 (wording; Sec. 6, proof LF404)

- **Text:** "(u1 >= 7+9 > 7+6)".
- **Issue:** Lemma 4(v) proves u1 ≥ |b_l|+9 for each letter. The unconditional bound u1 ≥ 16 follows only if some |b_l| = 7. Otherwise LF96 gives only u1 ≥ (7κ−6)/2, which is 14.5 at t = κ−1 = 4, i.e. u1 ≥ 15.
- **Consequence:** none. Lemmas 7(b), 7(c) and 8(b) use only u1−6 ≥ |b| and u1−5 ≥ x per letter, and these hold with margin 3.
- **Repair:** read "(u1 ≥ |b_l|+9 ≥ |b_l|+6 for every letter, Lemma 4(v))".

## Distinctions

- **Correctness:** as above.
- **Completeness:** the whole frozen target is covered: every κ ≥ 5 with p = 4κ−7 prime, any admissible NF, arbitrary placement of the extra pairs, and the genuine empty-run rule. There is no failing lemma. (5,13) is covered, including both tight points: 25 < 26, and the 15(d) sub-case handled by Lemma 14.
- **Process:** not adjudicated. I only checked that no TCW, P7L, FCW, SCW or USK lemma is used as a premise.
  - Sec. 7 (R2)/(M3) are remarks, and the TCW reference in erratum-1 item 3 is provenance only.
  - PL is allowed by the scope but not used.
- **Priority/novelty:** none claimed and none assessed.
- **Computation:** the proof uses none. This review is written by hand only, with no tools and no enumeration.
