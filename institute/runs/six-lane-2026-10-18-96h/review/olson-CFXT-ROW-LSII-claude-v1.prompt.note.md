## Basis

I read the frozen texts as hashed, through erratum-1, with E1–E5 governing, and LS-caseII-v2 alongside them. The only black boxes used are CD, S1-sharp and RED. I re-derived every cross-file use below, so nothing else is imported.

## Verdict summary

| Item | Verdict | FATAL / MAJOR / MINOR |
|---|---|---|
| CF(a) | ACCEPT (with E1) | 0/0/0 |
| CF(b) | ACCEPT | 0/0/1 editorial |
| CF(c) and instances | ACCEPT | 0/0/0 |
| XT(i) | ACCEPT | 0/0/0 |
| XT(ii) | ACCEPT | 0/0/0 |
| XT "In particular" sentence and Remark | ACCEPT-WITH-FIXES | 0/0/2 |
| TR Proposition (conditional) | ACCEPT-WITH-FIXES | 0/0/2 |
| RS(a), RS(b) | ACCEPT | 0/0/1 editorial |
| DGM-p | ACCEPT | 0/0/1 informational |
| Theorem U and its sharpness | ACCEPT-WITH-FIXES (E3 mandatory) | 0/0/2 |
| Lemma ROW | ACCEPT (with E3) | 0/0/0 |
| LS-threshold dichotomy | ACCEPT | 0/0/1 informational |
| Length-(3κ+2) dichotomy | ACCEPT-WITH-FIXES | 0/**1**/1 |
| Endpoint note and E5 | ACCEPT-WITH-FIXES | 0/0/4 |
| SH(a,b) | ACCEPT-WITH-FIXES | 0/0/2 |
| AP | ACCEPT-WITH-FIXES | 0/0/2 |
| LS-II (and §4) | ACCEPT-WITH-FIXES | 0/0/3 |

There is no FATAL finding. There is one MAJOR finding: a scope error in a statement that nothing downstream uses, fixable in one line.

---

## CF

**Scope.**
- p ≥ 5 prime.
- κ an integer with 0 ≤ κ ≤ p−1 (E1).
- Y any odd sequence.
- g any odd generator. g is never the involution p, and g need not occur in Y.
- (b) needs only M ≤ 2p−1 and is independent of κ.
- (c) is pure arithmetic for any M.

**What I checked.**
- Since 0 ≤ i ≤ M < 2p, each W gives at most one i. So zero-sums correspond exactly to pairs (W,k) with 2pk−M ≤ A_W ≤ 2pk, of length 2pk−2σ(W).
- The window forces k ≥ 1, because κ ≥ 0.
- ρ = σ mod p, because e ≤ p.
- The converse gives i ∈ [0,M].
- Empty W is harmless, since δ0 ≥ 1.
- M ≥ 2p puts g^{2p} inside the window, because κ ≤ p−1.
- The map x ↦ μ_x is injective, so occurrence sub-multisets of R correspond exactly to sub-multisets of U.
- In (b), set j := p(k−1)−σ. Then k ≥ 2 is automatic.

**MINOR (editorial).**
- (L) characterises "zero-sum of length ≥ 2p+2". That equals "long" (length ≥ 2κ+2) only under (ZP_κ).
- I found no downstream misuse: ROW §5, TR and LS-II all work under ZP.
- Still, ROW §5's phrase "the long zero-sum condition (L)" should add "under (ZP_κ)".
- The clause "σ(W)+j ≥ p" is redundant.

## XT and the TR reduction

**Scope of (i).**
- p ≥ 7 and κ0+1 ≤ κ ≤ p−2, so e ≥ 2 and 3e ≤ p−1.
- h any generator.
- Z any odd sequence of at most three terms, including the involution and 3h.

**Scope of (ii).** As (i), plus κ ≥ κ0+2, so n = p−3e−1 ≥ 3. This range is empty at p = 7, so (ii) has content only for p ≥ 11.

**What I checked in (i).**
- Base: δ0 = 3e+1 and U = 1^{p−1}. ρ = w ≤ e−1 forces 3w ≤ 3e−3. The E2 re-derivation suffices; neither TV nor (ZP_{κ−1}) is used.
- One-term extensions: there is exactly one W per residue. x is forbidden iff p+1+3ρ−μ ≥ 3e+1 for some ρ ≤ min(e−1, μ−1).
  - This holds for every μ ≤ p−3, including 3h (μ = 1) and the involution (μ = (p−1)/2).
  - It fails for μ ∈ {p−2, p−1}.
- All six two-term cases and both three-term cases were recomputed. The witnesses are 1^{e+1}{p−2}, 1^{e+1}{p−1}², 1^{e+2}{p−1,p−2}, 1^{e+3}{p−2}² and 1^e{p−1}.
  - Each has w ≤ e+3 ≤ p−1.
  - Each has |W|+2ρ ∈ [δ0, 2p].

**What I checked in (ii).**
- δ0 = 1 and |W| ≤ n+3, so (F) is equivalent to "no nonempty W has σ mod p ∈ [0,e−1]".
- The union of the intervals [−3ρ−n, −3ρ] is [−(p−4), 0]; this needs n ≥ 2.
- ν ∈ {1,2,3} corresponds to h, −h, −3h. I checked 3(2c*−1) ≡ −1 (mod 2p).
- The subset sums of 1^{n+a}2^b3^c fill [1,N]. The least forbidden integer is n+4.
- The base E3(κ−1) is the case a = b = c = 0.

**MINOR 1 (statement broadening).** The E3 half of "In particular … E3(κ−1)h³ = E3(κ)" is proved only for κ ≥ κ0+2.
- At κ = κ0+1 we have n ∈ {0,1}, and the one-term covering argument fails.
- For example, n = 0 admits every ν ∉ Φ.
- **Repair:** add "(for κ ≥ κ0+2)".

**MINOR 2 (Remark).** The Remark is not used anywhere, but two parts are unsupported as written.
- "Similarly E2(κ0) has no long zero-sum" is asserted without proof. It is true: with g = h, δ0 ∈ {p−1, p}, only k = 1 occurs, and every length 2p−2w with 3w ≥ δ0 is ≤ 2κ0.
- The route "by S1-sharp" would also need (ZP_{κ0}) for E3(κ0), which is not shown.
- **Repair:** keep only "directly" and add the one-line computations.

**TR Proposition: ACCEPT-WITH-FIXES, as a conditional implication.** Scope is κ0+2 ≤ κ ≤ p−2, so it has content only for p ≥ 11. TR is OPEN and the base κ0+1 is not covered.

**MINOR 3 (STAB wording).** STAB's text is not in the packet. I accepted the Proposition relative to the reading its proof uses:
- STAB(p,k): every odd Y with |Y| = 3k+1, satisfying (ZP_k) and having a zero-sum of length > 2k, equals E2(k) or E3(k) for some generator h.
- **Repair:** pin this wording to STAB2-scope. If the source says "up to automorphism" or similar, the last line needs rechecking.

**MINOR 4 (meaning of "long" in TR).** Under (ZP_κ), and with V having no zero-sum of length 2κ, both readings of "long" (≥ 2κ+2 or ≥ 2κ) force length ≥ 2p+2. State this.

## RS

**Scope.** p any prime. (a) any S over Z_p with 1 ≤ n ≤ |S|. (b) all terms nonzero, K ≥ 0. The only import is CD.

**What I checked.**
- Each listed occurrence goes to exactly one row.
- At most n consecutive occurrences of one value land in distinct rows. So each row is a set, and picking one element per row picks n distinct occurrences. A value may recur across rows, but always via different occurrences, so nothing is reused.
- T ≥ n, so every row is nonempty.
- (b) needs 0 ∉ A_i. Empty rows are fine as B_i = {0}.
- Every downstream application uses μ-multisets with terms in [1,p−1], which are nonzero mod p.

**MINOR (editorial).** Fix the indexing as k = 0,…,T−1.

## DGM-p

**Scope.** p ≥ 5; κ an integer with (p−3)/2 ≤ κ ≤ p−1; Y odd with (ZP_κ) and |Y| ≥ p+2κ+1. Imports: RS(a), CD.

**What I checked.**
- 2κ+2 ≤ min(2p, |Y|).
- A subsequence of exactly 2κ+2 terms has even length, so it is a zero-sum iff its C_p-sum is 0.
- T ≤ p+2κ < |Y|.
- The step p−2 < 2κ+2 needs exactly κ ≥ (p−3)/2.
- The involution is excluded because x0^{2κ+2} would be a zero-sum in the window.

**MINOR (informational).**
- At κ = p−1 the hypotheses are inconsistent: multiplicity ≥ 2p+1 contradicts ZP. So the lemma is vacuous there, and its real content is κ ≤ p−2 with 2κ+3 ≤ M ≤ 2p−1.
- The DeVos–Goddyn–Mohar attribution is unverified context, not a premise.

## Theorem U

**Scope.** p ≥ 5; κ an integer with (p−3)/2 ≤ κ ≤ p−1. It applies to **every** odd Y with (ZP_κ), with no length or long-zero-sum hypothesis.

**What I checked (with E3).**
- r ≤ p−2 and e ≤ (p+3)/2 give r+2e−2 ≤ 2p−1.
- The v1 sentence assumed ρ ≤ e−1 in order to bound |W|+2ρ. E3's contrapositive form is valid and necessary.
- The case V' = ∅ is included.
- RS(b) with K = |V| gives |V|+1 ≤ p−e.
- In the branch r < δ0, |Y| ≤ 2p−1.
- At κ = p−1 the DGM branch is empty.

**Sharpness.** Take g^{2p−1}(−g)^κ.
- A zero-sum needs i ≡ j (mod 2p) with i ≤ 2p−1 and j ≤ κ < 2p, so i = j.
- Every zero-sum is therefore g^j(−g)^j, of length 2j ≤ 2κ.
- So the sequence satisfies (S1_κ), hence (ZP_κ), and has no zero-sum longer than 2κ. Its length is exactly 2p+κ−1.

**MINOR 1 (statement broadening).** "At κ = 0 it is D(C_{2p})−1" lies outside the proven range, since (p−3)/2 ≥ 1, and it cites Davenport.
- **Repair:** delete it, or mark it "outside scope, not claimed".

**MINOR 2.** The s_{2p}(C_p) remark is a comparison only. In fact U at κ = p−1 re-proves the bound 3p−2 for odd sequences from CD. The "Use for LS" paragraph is heuristic, not a claim.

## ROW and the two dichotomies

**Lemma ROW: ACCEPT.** Scope is as in E4: κ an integer with 0 ≤ κ ≤ p−1, (ZP_κ), any odd generator, r ≥ δ0 and r+2e−2 ≤ 2p. The E3 wording is necessary and sufficient.

**LS-threshold dichotomy: ACCEPT.**
- Scope: κ0+1 ≤ κ ≤ p−2 (nonempty only for p ≥ 7), |Y| = p+2κ+1, (ZP_κ), g = g0.
- Checked:
  - δ0 ≤ 2e−3.
  - r = p−2e+1+δ0 ≤ p−2.
  - K = p−2e+1 ≥ 0, and ROW's hypotheses hold.
  - Case (I) is equivalent to δ0 ≤ e−2.
  - Two values with multiplicity > K would force p ≤ 3e−3, which is false.
  - In case (II), the remaining terms number at most e−2.
- MINOR (informational): the long zero-sum is never used. The dichotomy holds for every (ZP_κ) odd Y of length thr, and RED is context only.

**Length-(3κ+2) dichotomy: ACCEPT-WITH-FIXES.**

**MAJOR (scope).** Neither v1 nor E4 states a κ range. E4 gives ROW the range 0 ≤ κ ≤ p−1, but the proof needs K = 3κ+2−2p ≥ 0 (ROW's hypothesis r ≥ δ0). As literally scoped, the statement is **false at κ = 0**:
- Take Y = g² with g an odd generator.
- Y satisfies (ZP_0), and v_g = 2 ≥ p−e = 0.
- U = ∅ and δ0 = 2p−2 > 2e−3 = 2p−3.
- So neither (I+) nor (II+) holds.

**Repair:** add "κ0 ≤ κ ≤ p−1 (equivalently 3κ+2 ≥ 2p)", or use the LS+ range κ0+1 ≤ κ ≤ p−2. Under that range the proof checks:
- K = p−3e+2 ≥ 0.
- M ≥ p−e gives r ≤ 2p−2e+2.
- (I+) implies δ0 ≤ 2e−3.

**MINOR.**
- The dichotomy remains conditional on a generator with v_g ≥ p−e. DGM-p does not supply one, since 3κ+2 < p+2κ+1 for κ ≤ p−2.
- Its relevance to LS+ (cutting a counterexample to length exactly 3κ+2) rests on SLZ3. SLZ3 is a pending candidate and not an allowed import. Do not cite this dichotomy as an LS+ reduction step.

## Endpoint counterexamples (range note and E5)

**Scope after E5.**
- **(A)** For every prime p ≥ 5 and distinct a, b ∈ C_p, Y_{a,b} has length 3p−2 and satisfies (ZP_{p−1}). It fails (S1_{p−1}) iff it has a zero-sum of length ≥ 2p+2.
- **(B)** At p = 11: 1^21 5^10 over Z_22. 1^19 5^5 is a long zero-sum, and the sequence is not E2(10) or E3(10).
- **(C)** For every prime p ≥ 7 and b ∉ {0, ±1, 3, 3^{−1}}: (1,1)^{2p−1}(1,b)^{p−1} satisfies (ZP_{p−1}), has a zero-sum of length exactly 2p+2, and is neither E2(p−1) nor E3(p−1) for any generator h. So extending STAB to κ = p−1 fails for **every p ≥ 7**.
- **p = 5 is not decided.** The excluded set {0, ±1, 3, 3^{−1}} is all of Z_5, so the family is empty there and nothing more is claimed.

**What I checked.**
- A 2p-term subsequence has j ∈ [1,p−1] and C_p-sum j(b−a) ≠ 0.
- j0 = −2/(b−1) is defined since b ≠ 1.
  - j0 ≠ 0.
  - j0 ≠ 1, since b ≠ −1.
  - j0 ≠ 2, since b ≠ 0.
  - Hence j0 ∈ [3, p−1] and i0 ∈ [p+3, 2p−1], within the available multiplicities.
- The C_p-sum is ≡ 2 + j0(b−1) = 0, and the length is even.
- The exclusions b ≠ 0 and b ≠ −1 are genuinely needed: they would give j0 = 2 or 1, which needs i0 ≥ 2p.
- Since 2p−1 ≠ p−1, the multiplicities fix which value is h.
  - 3(1,c) = (1,3c), so Y = E2 forces b = 3, and Y = E3 forces 3b = 1.

**MINOR 1.** Erratum-1's header "(no statement strengthened)" is false for E5. E5 replaces a p = 11 claim with a new, proved claim for all p ≥ 7. Relabel it.

**MINOR 2 (import leakage).** "LS+ at κ = p−1 is classical (s_{2p}(C_p) = 3p−1)" is outside the allowed imports.
- **Repair:** cite Theorem U at κ = p−1 instead, accepted above.

**MINOR 3.** These are not checkable here, because STAB's text is not embedded:
- "STAB is stated (and only ever used) for …";
- the citations of MAX v2 and STAB2-scope.
- **Repair:** downgrade to "intended scope".

**MINOR 4.** The closing remark about "the much larger classical family of s_{2p}(C_p)-extremal sequences" is unproved.
- **Repair:** restrict it to the Y_{a,b} family. Also fix the j-range wording to j ∈ [1, p−1].

## SH(a,b)

**Scope.**
- p ≥ 7 and κ0 < κ ≤ p−2.
- H'(κ).
- Y odd with (ZP_κ) and |Y| = p+2κ+1, having a long zero-sum.
- Imports: S1-sharp for κ' ≤ κ0, and H' for κ0 < κ' < κ. Only smaller κ is used.

**What I checked in (a).**
- W and WZ are both zero-sums of Y.
- So the excluded lengths |W| are [2κ+2−z, 2p−z] ∪ [2κ+2, 2p]. These are contiguous on even lengths because 2p−z ≥ 2κ.
- |Y−Z| = p+2κ'+1.
- T ⊆ Y−Z has length ≥ 2p+2 > 2κ', contradicting S1-sharp or H'.
- κ' ∈ [p−2e, κ−1], and p−2e ≥ (p+2)/3 > 0.

**What I checked in (b).** |T| ≥ 2p+2 by ZP, so |T−Z| ≥ 2κ+2.

**MINOR 1.** State that z is even (Z is a nonempty zero-sum of odd elements), so κ' is an integer. State κ' ≥ p−2e > 0, not merely κ' ≥ 0.

**MINOR 2.** Say explicitly that "meets" and "disjoint" are occurrence-level. Note that the union of windows relies on parity: 2κ+1 is odd.

## AP

**Scope.** p an odd prime; integer n ≥ 1 with 3n < p; x ≠ 0; any a; I an arc of l ≤ 2n consecutive residues.

**What I checked.**
- The intersection formula holds: |I∩(I+x)| = max(0, l−|x|) + max(0, l−p+|x|), with the signed representative 1 ≤ |x| ≤ (p−1)/2.
  - It needs l < p.
  - It needs |I∩(I+x)| = |I∩(I−x)|.
- The three cases force |x| ≤ n.
- No-wrap lifting: [α−n, α+3n−1] meets L+mp only for m = 0.
  - m = 1 is excluded because p > 3n−1.
  - m = −1 is excluded because l+n−1 < p.

**MINOR 1.** In the cases |x| ≥ 2n and p−2n < |x| < 2n, the bounds should read max(0, 2n−(p+1)/2) and max(0, 4n−p). As written, "≤ a negative number" is false when that number is negative. The conclusion "< n" still stands.

**MINOR 2.** Write the lifting as an induction on ρ:
- If y_ρ ∈ L, then y_ρ+x̃ ∈ [α−n, α+3n−1] and its residue lies in I, so y_{ρ+1} ∈ L.
- Hence n|x̃| ≤ l−1 ≤ 2n−1, so |x̃| = 1.
- Also state the m = −1 exclusion explicitly.

## LS-II

**Scope.**
- p ≥ 7 and κ0 < κ ≤ p−2.
- H'(κ), which is vacuous at κ = κ0+1.
- Y odd, |Y| = p+2κ+1, (ZP_κ), with a long zero-sum.
- g = g0 from DGM-p.

**Conclusion.** No μ-value has multiplicity ≥ p−2e+2.

**§4 consequence.** Such Y lies in case (I):
- δ0 ≤ e−2, i.e. M ≥ p+κ+2;
- every U-multiplicity is ≤ p−2e+1;
- r ≤ p−e−1.

**What I checked.**
- **Step 1.**
  - t ∈ [δ0−s, v1] runs over K+1 = p−2e+2 ≤ p consecutive integers, so their residues form an arc.
  - The e-point progression x1(ρ−σ(R')) lies in the complementary arc, of size exactly 2e−2 = 2n.
  - AP applies with n = e−1 ≥ 1 and 3n < p.
- **Step 2.** v1 ≥ p−2e+2 ≥ e−1, and 3e−3 ≥ δ0.
- **Step 3.**
  - v1 ≤ p−e, via t = p−e+1 ≤ p−2.
  - The three φ-ranges cover [0, p−1], and in each one t ∈ [0, v1]. The second range uses v1 ≥ e.
  - The allowed set lies in [0, (δ0−1−k)/2] ∪ [v1+e, p−1].
  - For k = 1, a negative term has ν ∈ [2, e−2] and c' ∈ [3, 2e−5].
  - The involution (μ = (p−1)/2) is neither tiny nor negative, so it cannot occur in R'.
- **Step 4.** At the first violating prefix, 0 < S_k ≤ δ0−(k+2)/2 < δ0 ≤ 2e−3 < v1+e ≤ p. So there is no wrap.
- **Step 5, structure of T.**
  - Apply SH(a) to every pair (occurrence of g, occurrence of −g). Hence T contains all copies of g, or all copies of −g.
  - T cannot contain both:
    - if |T| = 2p+2, removing one pair leaves a 2p-term zero-sum in the window;
    - if |T| ≥ 2p+4, removing one pair leaves a long zero-sum disjoint from that pair.
  - A T with no g has length ≤ r ≤ p−2, so it is not long.
- **Step 5, the term c'.**
  - c' ≤ 2e−5 < 2p−2e+3 ≤ M, since 4e < 2p+8.
  - The c' copies of g are taken from T.
  - c'+1 is even and lies in [4, 2e−4].
  - So SH(b) applies.
- **No stronger issue found.** I also checked every other place that needs "enough copies": t ≤ v1 in Steps 1 and 3, and v1 ≥ e−1 in Step 2.

**MINOR 1.** Add the c' ≤ M sentence.

**MINOR 2.** Write out the occurrence-level pair argument in Step 5. Also note that W' ⊆ R' as a sub-multiset, which is what lets Step 4 apply.

**MINOR 3.** Neither "s ≤ e−2" nor the uniqueness of μ1 is used. Case (II) needs only "some value with multiplicity ≥ K+1", and ROW enters only in §4. State this; it narrows the dependency.

---

## Import closure

**Accepted dependency graph.**
- CD → RS → DGM-p → U (with E3).
- CF (with E1) and RS(b) → ROW (with E3) → LS-threshold dichotomy, also using DGM-p → LS-II §4.
- CF → XT (with E2) → TR Proposition, with hypotheses STAB(p,κ−1) and TR(p,κ).
- Elementary arithmetic → range note and E5.
- S1-sharp and H'(κ) → SH. AP is elementary.
- CF, DGM-p, SH and AP → LS-II. RED is used only to translate "no counterexample of length thr" into LS(p,κ).

There are no other premises, and no finite probe is a premise.

**Mentions that are not premises (strip or label).**
- Lemma TV: removed by E2, and nothing else uses it.
- DeVos–Goddyn–Mohar: attribution only.
- D(C_{2p}) and s_{2p}(C_p): remarks only.
- SLZ3: sits behind the motivation for length 3κ+2, and is pending.
- STAB2-scope and MAX v2: STAB's text is not embedded.
- SHIFT: expressly unused.
- ROT-FB: appears only in the LS scope document.

**Statement-broadening flags.**
1. The length-(3κ+2) dichotomy has no κ range (the MAJOR finding).
2. The E3 half of XT's "In particular" sentence.
3. Theorem U's κ = 0 remark.
4. The v1 range note's "STAB(p,p−1) is false", now superseded by E5.
5. Erratum-1's "no statement strengthened" header.
6. The "only ever used" claim and the classical-family remark.

## What is not concluded

- No LS, LS+ or STAB result follows, and no ordered-Olson statement.
- LS-II excludes only case (II), under H'(κ).
- Case (I) is untreated, so LS(p,κ) for κ0 < κ ≤ p−2 stays open. For κ ≤ κ0, LS is just S1-sharp.
- The TR reduction is conditional on the open TR and on STAB(p,κ−1). It does not reach the base κ0+1.
- STAB at κ = p−1 is refuted for p ≥ 7 only; p = 5 is undecided.
- The LS+ dichotomy is conditional on a generator with v_g ≥ p−e.
