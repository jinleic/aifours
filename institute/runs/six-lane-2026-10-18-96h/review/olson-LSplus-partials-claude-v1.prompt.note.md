# Referee report: LS+ partials v2 (`eedfa0f1…`) and MAX addendum v2 (`4b0be3e3…`)

**Basis.** This review relies only on the following accepted texts:
- S1-sharp v1 `992ab63f…`, its erratum 1 `bf504cdf…`, and the parent verdict `bd4a0a60…`.
- SLZ3 v1 `0cfe637f…`, its erratum 1 `483d9d1b…`, and the parent verdict `2b7b08a3…`.
- The index-one record `e4615144…`.

LS-scope-v1 (`80ae8041…`) is not embedded. I therefore read LS(p,κ) as "(ZP_κ) and |Y| ≥ p+2κ+1 ⟹ (S1_κ)". This matches SLZ3 §4 and erratum M11.

This is a written review only. It does not assess novelty and nothing was checked in Lean.

## Verdicts

| Item | Verdict |
|---|---|
| TV bound | **ACCEPT** |
| TV extremal classification E2/E3 | **ACCEPT** |
| RED+(a) | **ACCEPT-WITH-MINOR-FIX**. It needs only the accepted SLZ3, not H. |
| RED+(b) | **ACCEPT**. It is conditional on H(κ), and unconditional at κ = κ0+1. |
| SHIFT | **ACCEPT-WITH-MINOR-FIX** |
| SHIFT-C (LS+ form) | **ACCEPT-WITH-MINOR-FIX** (the σ(Y) ≠ 0 step) |
| SHIFT-C, LS version | **ACCEPT-WITH-MINOR-FIX**, relative to the exact LS text |
| MAX | **ACCEPT-WITH-MINOR-FIX** (integer overlap) |
| STAB ⟹ LS+ | **ACCEPT**, as a conditional reduction only |
| Side observation | **HOLD**. It is a separate, stronger candidate and is not granted. |

**Totals: 0 FATAL / 0 MAJOR / 9 MINOR.** Nothing here proves LS+, STAB, LS, INV* or ordered Olson.

## Derivation notes

### TV bound
- **Odd non-generator.** gcd(h,2p) = gcd(h,p), so the only odd non-generator is h = p. Then Y = p^(a+b). Since κ ≤ p−1, p^(2κ+2) has length ≤ 2p, so ZP forces a+b ≤ 2κ+1. Hence Y has no κ-long zero-sum.
- **Generator h.** Zero-sums correspond to i+3j = 2pk, with length 2pk−2j. ZP gives a, b ≤ 2p−1, hence k ≤ 3. Level 1 is never long, so k* ∈ {2,3}. The window and "long" conditions translate into j-intervals with exact integer endpoints.
- **k* = 2.**
  - If b ≥ p, then p ∈ J_2, giving a zero-sum of length 2p. So b ≤ p−1.
  - J_1 is nonempty. Its lower end ⌈(2p−a)/3⌉ is ≥ 1.
  - That lower end is ≤ b, because (2p−a)/3 < j0 ≤ b.
  - It is also ≤ ⌊2p/3⌋: from a ≥ 4p−3j0 ≥ p+3 we get (2p−a)/3 ≤ (p−3)/3 < ⌊2p/3⌋.
  - Every one of these comparisons is against an integer, so the integer conclusion is valid.
  - Finally, min J_1 ≥ p−κ ⟺ a ≤ 3κ−p+2.
- **k* = 3.**
  - J_2 is nonempty, because (4p−a)/3 ≤ j0−2p/3 < b, (4p−a)/3 ≥ (2p+1)/3 > 0, and (4p−a)/3 ≤ (4p−3)/3 < ⌊4p/3⌋.
  - Minimality of k* together with ZP excludes J_2 ∩ [0, 2p−κ−1].
  - Hence a ≤ 3κ−2p+2.

### TV classification
- **Equality cases.** Equality holds only at E2 (when k* = 2) and at E3 (when k* = 3).
- **Converse, for every generator h.**
  - E2:
    - At level 1, (2p−a)/3 = p−κ−2/3, so every level-1 length is ≤ 2κ.
    - At level 2, j ranges over [⌈(5p−3κ−2)/3⌉, p−1]. This interval is nonempty ⟺ 3κ ≥ 2p+1, and its lengths are ≥ 2p+2.
    - a+3b = 3κ+2p−1 < 6p, so there is no level 3.
  - E3:
    - At level 1, j ≥ p−κ+⌈(p−2)/3⌉. The text's "≥ p−κ" is true but weaker.
    - At level 2, min j = 2p−κ exactly.
    - At level 3, j ranges over a nonempty interval with upper end 2p−1.
    - a+3b = 3κ+4p−1 < 8p, so there is no level 4.
  - In both families a ≤ 2p−1, because κ ≤ p−1.
- **Representation is unambiguous.** If {h,3h} = {h′,3h′} with h′ ≠ h, then 8h ≡ 0 (mod 2p), which forces h = p.
- **Examples check out.**
  - 3·15 ≡ 1 (mod 22). So 1^21 15^7 = 15^7 (3·15)^21 is E3 at (11,9), and 1^21 15^4 is E3 at (11,8).
  - 1^18 3^10 and 1^15 3^10 are E2.
  - Direct check of 1^21 15^7: its zero-sum lengths are {8,10,12,16,18,24,26}.
  - p = 7: 6 odd generators × 2 families gives 12 distinct multisets.
- **Consistency check (not in the text).** At p ≡ 1 (mod 3) and κ = (2p+1)/3, E2 = F1 and E3 = F2 (take h = ((2p+1)/3)g). So F2 is not an obstruction to STAB.
- **§4 claim is correct.** The shortest zero-sum of E2 and of E3 has length 2⌈p/3⌉, which is > 2e.

### RED+
- **(a)** The cut preserves T. Take Y′ = T plus any 3κ+2−|T| ≥ 1 terms of Y−T.
  - ZP is hereditary.
  - Failure of S1 is witnessed by T ⊆ Y′; no heredity of "not S1" is assumed.
  - T remains a shortest long zero-sum of Y′.
  - No H is used.
- **(b)** Under ZP_κ and evenness of zero-sum lengths, "no 2κ-zero-sum" ⟺ ZP_(κ−1).
  - A long zero-sum has length ≥ 2p+2 > 2κ−2, so S1_(κ−1) fails.
  - If κ−1 = κ0, this contradicts Fact S.
  - Otherwise LS+(p,κ−1) ∈ H(κ) contradicts |V| ≥ 3(κ−1)+2.

### SHIFT
- **Window union is exact.** For a zero-sum W ⊆ Y−Z:
  - W∪Z excludes |W| ∈ [2κ′+2, 2p−z].
  - Heredity excludes |W| ∈ [2κ+2, 2p].
  - Any even L in (2p−z, 2p] satisfies L ≥ 2p−z+2 ≥ 2κ+2 ⟺ z ≤ 2e.
- **Ranges.**
  - κ′ ≥ κ−e = δ ≥ 3. This lower bound is needed for Fact S's range but is not stated.
  - κ′ ≤ p−3, so κ′ lies within the LS+ scope.
- **Endpoints.**
  - At κ = κ0+1, no such Z exists, unconditionally.
  - At κ = κ0+2, only z = 2 is possible, and it needs LS+(p,κ0+1).
  - H(κ) supplies exactly the κ′ ∈ (κ0, κ).

### SHIFT-C
- **Bullet 1** is correct.
- **Bullet 2.**
  - |X| ≤ 3κ−2p ≤ 2e+1, and the second inequality holds ⟺ 5κ ≤ 4p+1.
  - |X| ≡ κ (mod 2), and any zero-sum in X has even length, so it has length ≤ 2e.
  - If σ(Y) = 0, then T = Y is allowed, and X = ∅.
  - The parenthetical "X nonempty by SLZ3" therefore holds only for a *shortest* T, since |T| ≤ 3κ+1 < |Y|. With that choice the deduction is correct.
  - For odd κ, |Y| = 3κ+2 is odd, so σ(Y) ≠ 0 by parity alone.
- **LS version.**
  - |Y−Z| = p+2κ′+1 exactly.
  - |X| ≤ 2κ−p−1 = δ−1, which is always even, and δ−1 ≤ 2e+1 ⟺ 4κ ≤ 3p+2.
  - This is correct under the stated reading of LS.

### MAX
- **Formulas.** j1, j2, w1, w2 are as stated, and w1, w2 are integers because c is odd.
- **Valid integer comparisons.** w1 ≤ j2, j1 ≤ w2 and w1 ≤ w2 are each an integer compared with a floor or ceiling, so they are valid.
- **The gap: j1 ≤ j2 is not established.** The text proves only the real inequality x ≤ y, where:
  - E2: x = (2p+3e−2−c)/3 and y = (4p−c)/3;
  - E3: x = (5p+3e−2−c)/3 and y = (6p−c)/3.
- **Why it is nevertheless true.** In both cases y−x = a/3.
  - E2: a ≥ p+3.
  - E3: a ≥ 3. For E3 at a = 3 (p ≡ 1 mod 3, κ = κ0+1), the margin is exactly 1.
  - Also unstated: 0 ≤ j2 in both cases, and 0 ≤ w2 for E3.
- **c = 1 is a genuine exception.** The level argument fails: for E2, w1 = p > p−1; for E3, w1 = 2p > 2p−1. Lemma TV is load-bearing here.
- **Spot checks.**
  - c = 3 gives h^p (3h)^p for E2 and (3h)^(2p) for E3.
  - c = 2p−1 gives j = e (E2) or j = p+e (E3), with i = a−1 and length 2κ+2.
  - Only e ≥ 1 is needed for w1 ≤ w2.

### STAB ⟹ LS+
- **The proof is valid.**
  - Some y ∈ Y−T exists, since |T| ≤ 3κ+1 < |Y|.
  - Y−y ⊇ T, so it fails S1 without any heredity claim.
  - STAB then identifies Y−y as E2 or E3, and MAX gives the contradiction.
  - No H(κ) is needed.
- **What it does not show.** STAB itself is open. Its probe support is three cells, all with κ ≤ κ0+2.

### Side observation: HOLD
- **Status.** It is strictly stronger than the accepted SLZ3. The same strengthening was explicitly not adopted (SLZ3 erratum M6 and the parent verdict). The text's label "not a claim beyond the SLZ3 text" is false.
- **Re-derivation (not a grant).** Use the M4 step map at N = 3κ+1, with κ odd, l = κ+1, D = κ−1.
  - Steps 2 and 7 need N > 3κ.
  - Step 3 needs N > 3κ−2 and N > 2p. SLZ3 at κ−1 gives |T0| ≤ 3κ−2.
  - Steps 1, 4 and 6 need N ≥ 2p+2 and κ ≤ p−1.
  - All of these hold.
- **Step 9.** This is the only replaced input: "l ≥ κ+2 (base ≥ 4)". S1-sharp erratum A-m3/A-m6 needs only base ≥ 3 and l ≥ p−δ+2 ⟺ 3κ ≥ 2p+1. For odd κ ≥ κ0+2:
  - 3κ−2p ∈ {7, 13, …} when p ≡ 1 (mod 6);
  - 3κ−2p ∈ {5, 11, …} when p ≡ 5 (mod 6);
  - so base ≥ 4 in every case. v1's "≥ 4" was in fact true, and v2's "≥ 3" suffices.
- **Remaining cases.**
  - Even κ, including κ = p−1: parity alone suffices.
  - κ = κ0+1: N = 2p+2.
- **Conclusion.** The bound appears true for κ0+1 ≤ κ ≤ p−1. It must not be stated beyond p−1, because of the g^(4p) example at κ = p (SLZ3 erratum M5).

## Findings

**FATAL:** none. **MAJOR:** none. **MINOR:**

- **m1 (MAX).** The integer conclusion j1 ≤ j2 is drawn from a real inequality. Also unstated: 0 ≤ j2, and 0 ≤ w2 for E3.
- **m2 (SHIFT-C).** The σ(Y) ≠ 0 step must choose T shortest. "X nonempty" is false for T = Y. The odd-κ parity shortcut is missing.
- **m3 (SHIFT / Fact S).** Unstated:
  - Fact S's range 0 ≤ κ′ ≤ κ0, and κ′ ≥ δ ≥ 3;
  - z even;
  - "meets", "misses" and Y−Z are occurrence (index) notions.
- **m4 (RED+).** The construction in (a) is too terse. The heading places all of RED+ under H(κ), although (a) uses none of it.
- **m5 (citations).** "Candidate SLZ3" is stale. Cite SLZ3 with erratum `483d9d1b…` and parent `2b7b08a3…`. Cite Fact S with `bf504cdf…` and `bd4a0a60…`.
- **m6 (LS version).** The LS statement and its κ-range are not quoted. H′(κ) must range over LS's actual scope.
- **m7 (side observation).** The status label is false, and there is no step map and no stated κ-range. HOLD.
- **m8 (TV wording).**
  - "long iff j ≤ p(k−1)−1" is the ZP-relative criterion.
  - In the h = p clause, the operative comparison is a+b < 2κ+2.
- **m9 (MAX wording).**
  - "e−1 ≥ 1" overstates what is needed; e ≥ 1 suffices.
  - The text should say that c = 1 needs TV.

**Out of review scope.**
- In the scope file, "LS+ implies … S1-sharp" is not meaningful.
- The LS+ scope is empty at p = 5; the first nonempty cell is (7,5).

## Minimal repair

1. **MAX.**
   - **E2:** replace the j1 ≤ j2 sentence with: "(4p−c)/3 − (2p+3e−2−c)/3 = a/3 ≥ (p+3)/3 > 1, so ⌈x⌉ ≤ ⌊y⌋; 0 ≤ j2 since 4p−c ≥ 2p+1."
   - **E3:** "y − x = a/3 ≥ 1 since a = 3κ−2p+2 ≥ 3; 0 ≤ j2; w2 ≥ p+e > 0."
2. **SHIFT-C.** Replace the σ(Y) ≠ 0 sentence with:
   > "For κ odd, |Y| is odd. For κ even, if σ(Y) = 0, take T to be a *shortest* long zero-sum; SLZ3 gives |T| < |Y|, so X ≠ ∅ and σ(X) = 0, a contradiction. For T = Y the claim is vacuous."
3. **SHIFT.** Add: "z is even; κ′ ≥ δ ≥ 3, so Fact S (0 ≤ κ′ ≤ κ0) applies; complements are taken by occurrence."
4. **RED+(a).** Spell out Y′ = T ∪ (3κ+2−|T| terms of Y−T): ZP is hereditary, and not-S1 is witnessed by T. Relabel H(κ) as applying to (b) only.
5. **Citations.** Add the overlays and parents listed in m5, and state Fact S's range as 0 ≤ κ′ ≤ κ0.
6. **LS version.** Quote LS(p,κ) and its range from `80ae8041…`.
7. **Side observation.** Either delete its last two sentences, or relabel it as a separate unreviewed candidate. In the second case, state κ0+1 ≤ κ ≤ p−1 and include the M4-based step map given above.
8. **TV wording.** Write "(under ZP_κ) long iff …" and "a+b ≤ 2κ+1, so no zero-sum of length ≥ 2κ+2".

None of these repairs changes a statement. After repairs 1–8, TV, RED+, SHIFT/SHIFT-C and MAX are acceptable as scoped partials, with RED+(b) and SHIFT-C conditional on H(κ). STAB ⟹ LS+ is acceptable as a conditional reduction only; it shows only what a counterexample must look like. LS+, STAB, LS, INV* and ordered Olson remain open.
