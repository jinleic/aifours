# Hostile audit of SOURCE00: Lemma SC0, Lemma ZX-SC, Theorem ROT-ZX-SC, Corollaries INV*-ZX-SC and OLSON-ZX-SC

## What was audited and what is imported

- **Audited line by line:** SOURCE00:20–116. I checked it against:
  - ZX Steps A–G, Remark (3) and Secs. 4–5 (SOURCE01:81–266);
  - the mandatory overlay (SOURCE02:49–61);
  - the index-one record (SOURCE03:7–11);
  - S1+ (SOURCE05:50–51);
  - the normal form and SHgen-E (SOURCE06:28–70, 83–85);
  - OLSON-few Cases 1–3 (SOURCE07:28–47), read through overlay 8 (SOURCE02:58).
- **Imported, not re-proved:**
  - D(Z_2p) = 2p;
  - the Savchev–Chen/Yuan statement exactly as recorded at SOURCE03:9–11, instantiated here at n = 2p;
  - GRX, PM*, K1, DAV/(V), the normal form, SHgen, SHgen-E, REFL-few-odd, RGR-LONG, the OLSON-few case structure, and S1(a)/S1+, each at its accepted scope.
- **Not supplied:** proof-SHgen-v3.md. SHgen's hypotheses are read from SOURCE06:48, 83–84 and SOURCE01:226–233.
- **No execution.** The hand controls below are sanity checks, not premises.

## Verdicts

| Claim | Verdict |
|---|---|
| Lemma SC0 | **ACCEPT** (relative to the import) |
| Lemma ZX-SC | **ACCEPT-WITH-FIXES** |
| Theorem ROT-ZX-SC | **ACCEPT-WITH-FIXES** |
| Corollary INV*-ZX-SC | **ACCEPT-WITH-FIXES** |
| Corollary OLSON-ZX-SC | **ACCEPT-WITH-FIXES** |

There are 0 FATAL, 0 MAJOR and 8 MINOR findings. I found no counterexample, and no hypothesis is missing for anything the file actually claims.

## Independent derivation

**(1) SC0.**
- S is nonempty and zero-sum-free, so s ≠ 0. Hence S⁺ = S(−s) is a zero-sum of length t+1 ≥ p+2 = ⌊2p/2⌋+2, and n = 2p ≥ 10 ≥ 3.
- Minimality (SOURCE00:26–27):
  - A nonempty proper zero-sum V cannot lie in S, so V = U(−s) with σ(U) = s.
  - Then σ(S−U) = 0, so S−U must be empty, and V = S⁺.
  - This also covers U = ∅, which would force s = 0.
- The import gives coefficients x_i ≥ 1 with Σx_i = ord(a) ≥ t+1 ≥ p+2.
- The only divisor of 2p above p is 2p, so a generates. This step does not even need p prime.
- Dropping x_{t+1} ≥ 1 leaves a sum ≤ 2p−1.
- The generators of Z₂×Z_p are exactly the (1,c) with c ≠ 0, so g is odd. An odd a_i·g then forces a_i odd.

All correct.

**(2) Step A'.**
- |Z| ≤ 2κ, and Y' is zero-sum-free by maximality (SOURCE01:83).
- L ≥ 2p−k ≥ p+1 by integrality (see m1).
- e = 2p−1−L = k−1−2κ+|Z| lies in [0, k−1]. The lower bound uses L ≤ W' ≤ 2p−1.
- Each a_i ≥ 3 adds at least 2 to e'. So q := #{a_i ≥ 3} ≤ e'/2, m = L−q ≥ L−e'/2, and every a_i ≤ e'+1.
- (A2'): e'+1 ≤ L−e'/2 follows from 3e' ≤ 3e ≤ 2L−2. That is 3(2p−1−L) ≤ 2L−2, i.e. 5L ≥ 6p−1. Since 5L ≥ 10p−5k, it suffices that 5k ≤ 4p+1. The estimate is tight at k = (4p+1)/5, L = 2p−k.
- Multiplicity: every value other than g occurs at most q ≤ e'/2 < L−e'/2 ≤ m times, using e' ≤ k−1 < L. So g is the *unique* most frequent value and coincides with ZX's choice. Steps B–G use only the resulting decomposition, not maximality itself.
- MULT's m ≥ e+1 is recovered as well (m ≥ L−e/2 ≥ e+1), though nothing needs it.
- a_i ≤ e+1 ≤ k ≤ p−1 and a_i is odd, so a_i ≤ p−2 and b_g(a_i·g) = a_i.
- COMP holds: (a) by filling, since every d_j ≤ m (SOURCE01:99–101); (b) directly from SC0; (c) trivially.
- Uses of "p+2" in SOURCE01:
  - L106 (A3) is consumed only at L116, as "b ≤ p < W'". So W' ≥ p+1 suffices.
  - L124, "2p−β ≥ p+2", comes from β ≤ p−2 (negative odd b in (−p, 0)) and is unaffected.
  - Step D uses no lower bound on W' at all.

**(3) Steps B–D.**
- They use: (EX) for a longest Z; s(Z) ≡ 0 mod 2p (g has order 2p by SC0); COMP(a); (A4); W' > p (Step C only); and the definitions W' = L+e', e = 2p−1−L.
- They do not use MULT's m ≥ max(2, e+1), nor 3k ≤ 2p+1.
- Every hypothesis is supplied by A'.

**(4) Step E.**
- Definitions (SOURCE01:120–121, 130–131): r = #(g in Z); T = the negative terms; β = −b_g ∈ [1, p−2]; σ = Σβ.
- 0 ≤ r ≤ 2κ < 2p gives σ = r+2pt with t ≥ 0.
- The window chain at SOURCE01:134 is 2m−2p+1 ≥ 2p−1−2e−e' ≥ e−e'. Its last step holds **exactly** when 3e ≤ 2p−1.
- Second alternative of (R2): 3e ≤ 3(k−1) ≤ 2p−1. The final step 2p ≤ |Z| ≤ 2κ < 2p needs κ < p, which (R1) gives.
- First alternative of (R2): β ≤ e−e' ≤ k−1 (Step D) and |T| = |Z|−r ≤ 2κ. So σ ≤ 2κ(k−1) < 2p, forcing t = 0.

**(5) Steps F and G.**
- Step F: the completion Q has |Q| ≥ 2p−r−e', and exchanging with U = T gives 2p ≤ |Z|+e' ≤ 2κ+k−1 ≤ 2p−2. Even 2κ+k ≤ 2p would suffice.
- Step G: cost = e'+r ≤ e, and |b| ≤ k on Y', on g^r and on T.

**(6) Theorem ROT-ZX-SC.**
- For k ≥ 2, κ̂ ≤ 1 ≤ k−1 holds automatically.
- 2κ̂+k ≤ k+2 ≤ 2p−1.
- κ̂(k−1) < p.
- (S1) at integer κ̂ ≤ 1 already follows from S1(a); (ZP) comes from GRX (SOURCE06:43).
- |b| ≤ k ≤ p−2 (see m1).
- (H): 2H ≥ 2p−4 ≥ k−1 ≥ E.
- (K): (4p−3k−1)/2 ≥ k is equivalent to 5k ≤ 4p−1.
- REFL is called only on u°(h), with o_F = k ≤ (4p−1)/5 < p (SOURCE06:69).
- Every use of 3k ≤ 2p+1 in SOURCE01:208–234 has been replaced: (G'), k ≤ p−2, (H) and (K).

**(7) Corollaries.**
- κ(w) ≤ 1 iff F ≥ o+2p−4.
- κ̂ = κ(w)−(o−k)/2 ≤ κ(w), and 5k ≤ 5o ≤ 4p−1.
- REFL applies to w with o ≤ p.
- Deletion ledger:
  - Case 1 needs o ≤ 2p−3, which follows from (4p−1)/5 ≤ 2p−3.
  - Case 2 gives (o−1, F−1).
  - Case 3 gives (o or o−2, F).
  - Both 5o ≤ 4p−1 and F−o ≥ 2p−4 are preserved.

**(8) Section 3.**
- If k > (2p+2)/3, then κ < 3p/(2p−1) ≤ 5/3, so κ ≤ 1.
- The integers in ((2p+1)/3, (4p−1)/5]:

| p | New o_F | F condition |
|---|---|---|
| 5 | none | — |
| 7 | none | — |
| 11 | 8 | F ≥ 26 |
| 13 | 10 | F ≥ 32 |
| 19 | 14, 15 | F ≥ o_F + 34 |
| 29 | 20, …, 23 | F ≥ o_F + 54 |

- The file's examples are correct.

## Findings

**FATAL:** none. **MAJOR:** none.

**m1. SOURCE00:48, 83 — integrality.**
- Line 48 claims (4p+1)/5 ≤ p−1 for p ≥ 5. This is false at p = 5, where (4p+1)/5 = 4.2 > 4.
- Line 83 uses k ≤ p−2 without justification. The real inequality (4p−1)/5 ≤ p−2 needs p ≥ 9.
- Both conclusions hold for integer k: at p = 5, k ≤ 4 (lemma) and k ≤ 3 (theorem); at p = 7, k ≤ 5.
- **Fix:** write ⌊(4p+1)/5⌋ ≤ p−1 and ⌊(4p−1)/5⌋ ≤ p−2, with the p = 5, 7 cases stated.

**m2. SOURCE00:60–62 — Step E is not literally "unchanged".**
- SOURCE01:133 justifies the window inequality by "3e ≤ 3k−3 ≤ 2p−2", which uses 3k ≤ 2p+1. SOURCE01:130's "2κ ≤ 2k−2 < 2p" likewise depends on the old hypotheses.
- **Fix:** substitute "3e ≤ 3(k−1) ≤ 2p−1 by (R2)" and "2κ < 2p by (R1)". Note in the text that the chain needs exactly 3e ≤ 2p−1.

**m3. SOURCE00:41, 49 — statement and lower bound.**
- The statement omits two of ZX's conclusions: "positive terms of Z equal g" and "E+N = cost_g(Y)". SOURCE00:83 uses the second. Both are proved by Steps C and G (SOURCE01:115–119, 160).
- Line 49 asserts e ≥ 0 before SC0 is applied.
- **Fix:** add both conclusions to the statement, and cite (D) for e ≥ 0, or L ≤ W' ≤ 2p−1.

**m4. SOURCE00:73, 92 — missing κ̂ ≥ 0 in the corollary.**
- The theorem needs κ̂ ∈ {0, 1}, but the corollary proves only κ̂ ≤ 1.
- For k ≥ 2, κ̂ ≥ 0 comes from GRX (SOURCE02:53 overlay 3; SOURCE01:214–215). Without this citation the theorem's hypothesis is not discharged.
- The k = 1 case should cite the accepted terminal branch, including c ≠ 0 (SOURCE02:20, 53).
- **Fix:** add both citations, or restate the theorem with "κ̂ ≤ 1" and derive κ̂ ≥ 0 inside it.

**m5. SOURCE00:87 — SHgen-E caller discharge.**
- Overlay 4 (SOURCE02:54) requires the discharge to be explicit.
- **Fix:** state that base words u°(h) have length 4p−2, rotations in one nonzero pair, and o_F = k ≤ (4p−1)/5 ≤ p; that expansions preserve k (SOURCE06:52–59); and cite the generalized ZS v2 overlay V3.

**m6. SOURCE00:13–18 — imports.**
- The Imports block does not list RGR-LONG(p), the OLSON-few case structure with overlay 8, or the S1 result used at line 82. S1(a) at integer κ̂ ≤ 1 suffices there, with overlay 1.
- The index theorem is now used at n = 2p (composite), with length ≥ p+2. The S1(d) verdict records only "C_p, length p−1" (SOURCE04:66).
- The recorded statement (SOURCE03:9) covers every n ≥ 3, so no new import is needed. The parent record should still list this instance.

**m7. SOURCE00:99–102 — ledger inequalities.**
- "Case 1 needs o ≤ 2p−3" is asserted but not shown.
- **Fix:** add "o ≤ (4p−1)/5 ≤ 2p−3" and "5o' ≤ 5o ≤ 4p−1", as overlay 7 of SOURCE04:59 required for the analogous corollary.

**m8. SOURCE00:9–10, 111–115 — scope wording.**
- **(a) The 3k = 2p+2 slice.**
  - At 3k = 2p+2 (p ≡ 2 mod 3; (p, k) = (5,4), (11,8), (17,12), (29,20)), 3(k−1) = 2p−1. (R2)'s second alternative then holds for **every** κ, so Lemma ZX-SC covers every κ allowed by (R1) and (S1).
  - Line 113 ("the theorem states only that case") and line 114 ("Not covered by this route … κ̂ ≥ 2") are therefore inaccurate at k = (2p+2)/3.
  - **Fix:** write "not claimed here". Any extension to that slice needs its own (H), (K) and (S1) discharge and its own review.
- **(b) Residual quantifier.** The residual must quantify over all admissible normal forms (SOURCE02:52; SOURCE04:60).
- **(c) "No earlier file covers."** The terminal ROT-ZX/ROT-ZX++ results already cover avoiders with 3o_F > 2p+1 whenever some normal form has 3k ≤ 2p+1 (SOURCE01:242–243; SOURCE02:20). **Fix:** write "outside every earlier uniform range".
- **(d) Small primes.** At p = 5 and p = 7 the new range is empty. Say so.

## Counterexample search and controls

**p = 5, k = 4, κ = 2.** This is in the lemma only, at 3k = 2p+2.
- Take Y = 1⁹·7 in Z₁₀. Its only nonempty zero-sum is 1³·7, of length 4 = 2κ, so (S1) holds.
- With g = 1: Z = 1³·7, Y' = 1⁶, e = 3, e' = 0, r = σ = β = 3 = e−e'.
- cost = 3 = k−1, so the bound is attained.
- The variant 1⁷·3·9² fails (S1) through 1⁷·3 (length 8), exactly as Step C predicts.

**p = 7.** The lemma allows k ≤ 5, which is already within 3k ≤ 15. Nothing is new here.

**p = 11, k = 9 = (4p+1)/5, κ = 0.**
- Take Y = g¹²·(9g). All its subset sums are at most 21, so it is zero-sum-free.
- e = e' = 8 = k−1, |b| = 9 = k = p−2, and m = 12 ≥ 9.
- (A2') is tight in the worst-case estimate (5L = 6p−1) but valid.

**Lemma at κ ≥ 2 with 3k ≤ 2p+1.** Here ZX-SC reduces to ZX, because 2(k−1)+k ≤ 2p−1. Consistent.

## Observation (not a finding; unreviewed; do not adopt without review)

The theorem's bound 5k ≤ 4p−1 comes only from the *separate* estimates η ≤ (k−1)/2 and a_max ≤ k (SOURCE01:228–229). A sharper bound is available:
- Every heavy has |b| ≥ 3, so E ≥ (a_max−1) + 2(η−1).
- Hence η + a_max ≤ E+2 ≤ k+1.
- Then 2p−η−a_max−1 ≥ 2p−k−2 ≥ k for every k ≤ p−1.

The only slice excluded by the current bound is 5k ∈ {4p, 4p+1}: that is (5, 4), and k = (4p+1)/5 for p ≡ 1 (mod 5) (11, 31, 41, …). At (11, 9) the separate estimates give 8 < 9, while the example above has η = 1, a_max = 9 and 2p−η−a_max−1 = 11.

This is an under-claim, not a defect. It assumes SHgen's η and a_max mean what they mean at SOURCE01:228–229.
