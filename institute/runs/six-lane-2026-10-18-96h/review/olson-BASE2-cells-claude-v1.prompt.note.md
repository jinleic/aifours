# Hostile review: `proof-LS-BASE2-cells-v2.md` (`fd6e64e5…`): L1, B2-1, (S1), (S2)

This review is written derivation only, with no tools and no machine computation. Line numbers refer to the frozen candidate. I used the package only to locate steps, and re-derived every step below from the candidate and the verbatim import excerpts.

Accepted imports are taken at their recorded scopes. I re-derived the two short ones, AP′ (proof D1) and the greedy step (C). The index-one theorem is a statement-level external import, and I did not re-prove it.

## 1. Verdicts

| Claim | Verdict | FATAL | MAJOR | MINOR |
|---|---|---|---|---|
| Lemma L1 | **ACCEPT** | 0 | 0 | 1 (optional) |
| Lemma B2-1 | **ACCEPT-WITH-FIXES** (editorial) | 0 | 0 | 3 |
| (S1) LS(17,12) | **ACCEPT** | 0 | 0 | 2 (shared, non-blocking) |
| (S2) LS(23,16) | **ACCEPT-WITH-FIXES** (editorial) | 0 | 0 | 5 (2 shared) |

I found no mathematical gap. No fix changes a statement or adds an import.

## 2. Findings and minimal fixes

**Shared setting (apply to S1 and S2)**
- **G1 MINOR, line 23.** The bound "1 ≤ delta0" is presented as part of case (I), but the dichotomy only gives delta0 ≤ e−2. The lower bound comes from CF(a): (ZP_kappa) forces M ≤ 2p−1.
  - Fix: append "(delta0 ≥ 1 by CF(a))".
- **G2 MINOR, Sec. 0 (lines 12–15).** Two pins are missing:
  - the RED verdict `23d1a488…`;
  - the authority for the general-r greedy step, i.e. the LS+-chain verdict `4005007f…` and its C4 overlay `f1573d6c…` lines 63–65, with hypothesis S′ ≤ p−1 < p+1 ≤ 2|U′|.
  - Fix: add the pins. Both greedy uses meet C4 literally (see §3).

**L1**
- **L1-1 MINOR (optional), lines 31–32.** The step "≡ 0 (mod 2p)" silently uses ord(g0) = 2p (DGM-p) and c = 2mu+1 (CF §0–1).
  - Fix: add a half-sentence, or note "equivalently CF(b)/(L) with j = 1, read through R4".

**B2-1**
- **B-1 MINOR, lines 51–52, step (e).** The pair window {4m} ∪ [8m−1, 8m] and the triple window [8m−1, 10m−1] are asserted without the wrap check.
  - Fix, one sentence: an integer sum S of terms in J = [2m, 4m] has residue S if S < p; 0 if S = p or 2p; S−p if p < S < 2p; and 1 or 2 if S = 2p+1 or 2p+2. Since 1, 2 < 2m, a residue in J forces S = 4m or S−p ∈ [2m, 4m].
- **B-2 MINOR, line 48, step (d).** The triple lower bound 18m−1−2B uses the fact that one pair of the triple lifts to p+y with y ∈ J, so y ≥ 6m−B.
  - Fix: state this.
- **B-3 MINOR, line 34 (also line 112).** The heading reads as a bare statement about BASE2 cells.
  - Fix: "for a threshold LS counterexample at a BASE2 cell, CF data w.r.t. g0 (Sec. 1 setting), delta0 = 1 is impossible."

**S2**
- **S2-1 MINOR, lines 101–102.** "Lemma B2-1 (a) applied to U′ (same argument…)" reuses an internal step of a proof whose hypotheses were delta0 = 1 and the sequence U.
  - Fix: isolate the step as **Sublemma (a)**. If V is zero-sum-free over Z_p, p = 6m−1, |V| = 2m+3, and no nonempty subset sum lies in [1, 2m−2], then sigma(V) ∈ [2m−1, 4m−4] and all subset sums lie in {0} ∪ [sigma(V), p−1].
  - Its hypotheses hold for U′: U′ is zero-sum-free by maximality of Z0, |U′| = 11, and (F′) at delta′ = 1 excludes [0, 6]. I re-derived sigma′ ∈ [7, 12] directly.
- **S2-2 MINOR, line 86.** The bound |W′_s| ≥ s−E′ is never used in Sec. 4.
  - Fix: delete it or mark it unused.
- **S2-3 MINOR (optional), lines 98–99.** "the negative part of Z0 has total |sum| ≤ 1" is imprecise.
  - Fix: "the negative z~ of Z0 sum to −q ≥ −1, so sigma~(Z*) ≥ −1".

## 3. Check 1: every import application

| Lines | Import | Literal hypothesis and check |
|---|---|---|
| 21, 79, 109 | RED and its erratum (M-8, E-2) | Requires 1 ≤ kappa ≤ p−2. Here kappa = 12 and 16. |
| 21–22 | DGM-p | Requires (p−3)/2 ≤ kappa ≤ p−1 and \|Y\| ≥ thr. Here 4m ≥ 3m−2. |
| 23 | Dichotomy (E4) and LS-II′ (D-1 wording) | Requires p ≥ 7, kappa0+1 ≤ kappa ≤ p−2, \|Y\| = thr, g = g0. Here kappa = kappa0+1. |
| 24–28 | CF(a) via E1, giving (F*) and (F′) | r+2e−2 = p−1+delta0 ≤ 2p. (F′) applies (F*) to W′ ∪ Z0, which is occurrence-disjoint and has the same residue. |
| 30 | SLZ3 | Requires ⌊2p/3⌋+1 ≤ kappa ≤ p−1. Gives 3kappa+1 = 12m+1 = 2p+3; parity then gives \|T\| = 2p+2. It bounds T only, never \|Y\|. |
| 64–65, 84 | I-small | Requires delta0 ≤ 2 and 4e ≤ p+1+2·delta0. Here 20 ≤ 20, 20 ≤ 22, and 28 ≤ 28. Only its literal scope is used. |
| none | CF(b)/R4 | Used only inside I-small (E). L1 uses the coefficient identity directly, which is (L) with j = 1. |
| 68–70 | Index one, n = 17 | The minimality argument is correct. Length \|U′\|+1 ∈ {10, 12} ≥ 10. Least coefficients sum to ord(a) = 17 and the appended one is ≥ 1, so S′ ≤ 16. |
| 85 | Index one, n = 23 | \|U′\|+1 = 11+delta′ ≥ 13 iff delta′ ≥ 2. It is correctly **not** invoked at delta′ = 1, where the length is 12. |
| 71, 86 | Greedy (C) via C4 | Requires S′ ≤ p−1 < p+1 ≤ 2\|U′\|. Here 18 ≤ 2\|U′\| (p = 17) and 24 ≤ 2\|U′\| (p = 23). |
| 73 | AP′ (D1), n = 3 | 11 < 17. s_1..s_4 lie in [S′+1, 16], size ≤ 7 = 2n+1. |
| 88–89 | AP′, n = 5 | 17 < 23. s_1..s_6 lie in an arc of size ≤ 12−delta′ ≤ 10 ≤ 11, for delta′ ∈ {2, 3}. |
| 89 | AP′, n = 4 | 14 < 23. s_2..s_6 form a 5-term AP with difference a⁻¹ in an arc of size ≤ 8 ≤ 9, for delta′ ∈ {4, 5}. |

**D1, re-derived.**
- Case (i), d ≥ l: the intersection is empty.
- Case (ii), p−l < d < l: there are fewer than 2l−p ≤ 4n+2−p < n points, which holds iff 3n+2 < p.
- Case (iii) gives d ≤ n+1.
- In the lifting step, the window [α−n−1, α+3n+1] needs p > 3n+1 and l+n < p.
- All of these hold at (n, p) = (3, 17), (5, 23) and (4, 23).

**Greedy, re-derived.** A first failure at index k forces S ≥ −k² + (r+1)k + r. This expression is concave in k and equals 2r at k = 1 and k = r, so S ≥ 2r.

**After AP′.**
- p = 17: a⁻¹ ∈ {1, 2} puts s_1 ≤ 2 ≤ S′. a⁻¹ = −2 puts s_4 = 9 ≤ S′, since S′ ≥ |U′| ≥ 9.
- p = 23: a⁻¹ ∈ {1, 2} puts s_2 ∈ {2, 4} ≤ S′. a⁻¹ = −2 puts s_6 = 11 ≤ S′. With a = −1, s_6 = 17 > S′ gives S′ ≤ 16.
- Using s_2 rather than s_1 is necessary when delta′ ∈ {4, 5}, and the candidate does this.

## 4. Check 2: exhaustiveness of the case split

The reduction chain is: RED (LS fails ⇒ a counterexample of length exactly thr) → DGM-p → dichotomy → LS-II′ removes case (II) → 1 ≤ delta0 ≤ e−2.

**p = 17, delta0 ∈ {1, 2, 3}.**
- delta0 ∈ {1, 2}: I-small.
- delta0 = 3: (F*) caps mod-p zero-sums of U at size 2, and nonzero terms force size ≥ 2, so |Z0| ∈ {0, 2}.
  - |Z0| = 2: some z has residue nu ∈ [1, 8]. Take W = {z} or W = {z} ∪ W′_(nu−1); this needs S′ ≥ 7, and S′ ≥ 9.
  - |Z0| = 0: L1 gives s* = 1, so |W*| ≤ 1 < 5.

**p = 23, delta0 ∈ [1, 5].**
- delta0 = 1: B2-1.
- delta0 = 2: I-small.
- delta0 ∈ {3, 4, 5}: |Z0| ∈ {0} ∪ [2, delta0−1], so delta′ ∈ [1, delta0].
  - delta′ = 1 and delta′ ≥ 2 partition this range.
  - delta′ ≥ 2 gives |Z0| ≤ 3, as used.
  - delta′ ∈ {4, 5} forces Z0 = ∅, which the uniform argument covers.

No residue class or sub-case is left open.

## 5. Check 3: Lemma B2-1

**(a) Complement symmetry and interval trapping.**
- |A| ≥ 2m+4: the element 0 plus 2m+3 distinct nonzero prefix sums.
- A = sigma − A, with the pairing ∅ ↔ U included.
- sigma ∈ [2m−1, p−1].
- If sigma ≥ 4m−3, the arcs [1, 2m−2] and [sigma−2m+2, sigma−1] ⊆ [2m−1, p−2] are disjoint, so |A| ≤ p−4m+4 = 2m+3. Contradiction.
- If sigma ≤ 4m−4, then sigma−2m+2 ≤ 2m−1, so the union is exactly [1, sigma−1].
- B ∈ [2m+3, 4m], with exact endpoints p−(4m−4) and p−(2m−1).
- No rectification is used. Terms enter only as representatives in [1, B], and every later integer sum is placed against explicit multiples of p.

**(c)** J = [6m−B, B], which is empty iff B ≤ 3m−1. The quantifiers are correct: V and Z*−V are both proper and nonempty, and singletons are proper since t ≥ 3.

**(d) B ∈ [3m, 4m−1].**
- Pair sums lie in [12m−2B, 2B] ⊆ (B, 2p), so they lift.
- If t ≥ 4, a triple sum lies in [10m+1, 12m−3]. Its residue is in [4m+2, 6m−2], which is disjoint from J ⊆ [2m+1, 4m−1].
- If t = 3, the sum lies in [6m+3, 12m−3] and misses both p+1 and 2p+1.

**(e) B = 4m.**
- The pair and triple windows are as in B-1, and t ≥ 4 is impossible.
- If the sum is 6m, then Z* = (2m)³.
- If the sum is 12m−1, then each 12m−1−z_k ∈ [8m−1, 8m], giving Z* = (4m−1, 4m, 4m).
- Spot checks: (6,6,6) and (11,12,12) mod 17, and (8,8,8) and (15,16,16) mod 23, all have sum ≡ 1.

**(f) Non-extension.**
- (2m)³:
  - The conditions y+1 ≤ 4m, y+4m ≥ p+1 and y+2m ≤ 4m force y = 2m.
  - Then Y′ = (2m)^(2m+3). Five copies are available since 2m+3 ≥ 9, and 10m ≡ 4m+1 > B.
- (4m−1, 4m, 4m):
  - y ∈ [2m+1, 4m−1], because y = 2m makes y+4m−1 = p.
  - Then y+8m−1 ∈ [10m, 12m−2] has residue y+2m ∈ [4m+1, 6m−2], or residue 0 when y = 4m−1.
- In both cases a term outside Z* exists, because t = 3 < 2m+3.

**Uniformity.** Only m ≥ 2 is used: delta0 = 1 ≤ 2m−3; 1, 2 < 2m; 4m+1 < p; 10m < 2p. The proof therefore holds verbatim at every BASE2 cell (m ≥ 3, 6m−1 prime). Its inputs are only (F*), r = 2m+3 and L1. It uses no index one, AP′, I-small or greedy step.

## 6. Check 4: the p = 23 arguments

**Pinning Z0 when delta′ ≥ 2.** After a = −1, we have 12 ≤ |U′| ≤ S′ ≤ 16.
- ζ ∈ [2, S′]: {z} ∪ W′_(ζ−min(ζ,6)) has residue in [2, 6], which is forbidden.
- ζ ∈ [S′+1, S′+6]: {z} ∪ U′ has residue in [1, 6] and size ≥ 13, which is forbidden.
- The remaining residues are ζ = 1 or ζ ∈ [19, 22].
- q ≤ 1, from 3q ≤ delta0−1 ≤ 4.
- The signed total lies in [−12, 1], whose only multiple of 23 is 0. So the congruence forces equality, and the negative terms sum to −q ≥ −1.
- L1 gives sigma~(Z*) − s* ∈ [−28, 1]. The only values ≡ −1 in that range are −1 and −24.
  - −24 would need sigma~(Z*) ≤ −8, impossible since sigma~(Z*) ≥ −1.
  - −1 gives s* ≤ 2, so |W*| ≤ 2 + delta0 − delta′ ≤ delta0.
- Every congruence-to-equality step is forced by an explicit integer range.

**delta′ = 1.**
- Arc (i): W = {z} ∪ W′ has |W|+2·rho ≥ 5 > delta0−1, using delta0 ≤ 5. So A′ avoids [2−ζ, 6−ζ].
- Arc (ii): W = (Z0−{z}) ∪ W′ has |W| ≥ delta0−2, so |W|+2·rho ≥ delta0. So A′ avoids [ζ+1, ζ+6].
- The pieces in both arcs are occurrence-disjoint.
- Since 0 ∈ A′, ζ ∉ [2, 6] ∪ [17, 22].
- For ζ ∈ [7, 16], both arcs lie inside [7, 22]:

| ζ | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|---|---|---|---|---|---|---|---|---|---|---|
| (i) [25−ζ, 29−ζ] | 18–22 | 17–21 | 16–20 | 15–19 | 14–18 | 13–17 | 12–16 | 11–15 | 10–14 | 9–13 |
| (ii) [ζ+1, ζ+6] | 8–13 | 9–14 | 10–15 | 11–16 | 12–17 | 13–18 | 14–19 | 15–20 | 16–21 | 17–22 |
| overlap | 0 | 0 | 0 | 2 | 4 | 5 | 3 | 1 | 0 | 0 |
| removed | 11 | 11 | 11 | 9 | 7 | 6 | 8 | 10 | 11 | 11 |

- This matches line 108 and the package table.
- The minimum is 6, so |A′| ≤ 1+10 = 11 < 12.
- Hence every z has ζ = 1, and sigma(Z0) ≡ |Z0| ∈ {2, 3, 4} ≢ 0 mod 23.
- This branch uses neither index one nor AP′.

## 7. Exact conclusions supported

These conclusions hold relative to the imports at the scopes in §3: RED with erratum, DGM-p, the threshold dichotomy, LS-II′, CF(a) via E1, CF(b) via R4 inside I-small, I-small, index one at n = p, greedy via C4, AP′ via D1, and SLZ3 as a |T| bound only.

1. **L1.** In the Sec. 1 setting at every BASE2 cell (threshold LS counterexample, CF data w.r.t. g0), a shortest long zero-sum has length exactly 2p+2. Some W* ⊆ U has sigma(W*) ≡ −1 (mod p) and |W*| ≥ delta0+2.
2. **B2-1.** Let p = 6m−1 be prime with m ≥ 3, and kappa = 4m. Then no odd Y over C_2p with |Y| = 14m, (ZP_4m) and a zero-sum of length ≥ 2p+2 has delta0 = 1 with respect to g0. This is a restricted lemma: it yields no LS(p, 4m) for p ≥ 29, and S3 remains unproved.
3. **(S1) LS(17,12)** holds exactly as stated in scope line 9, at sequence level.
4. **(S2) LS(23,16)** holds exactly as stated in scope line 10, at sequence level.

**Not supported:**
- LS+ or STAB at any cell, or any extremizer classification.
- INV*, ordered Olson, or word-level or dihedral-avoider statements.

Sec. 5 is planning context, not a classification of the remaining cases. I checked only that its two thresholds are arithmetically correct:
- index one needs |U′|+1 ≥ 3m+1, i.e. delta′ ≥ m−2;
- I-small at delta0 = 2 needs m ≤ 4.

## 8. Range statement

- (17,12): e = 5, and 6e−10 = 20 > 17.
- (23,16): e = 7, and 6e−10 = 32 > 23.

Both cells lie outside the accepted LS-lin range p ≥ 6e−10. They are also outside the accepted e ≤ 4 band and are not BASE1 cells (p ≡ 2 mod 3). This is consistent with line 33 of the delta verdict, which lists both as not decided by that package. This is a statement about recorded acceptance ranges only, with no novelty or priority claim.
