# FC717: independent written review (second family, no tools)

**Abbreviations:** proof = proof-FC717-v1.md, pkg = review-package-FC717-v1.md, UMR = proof-UMR-v1.md, with LF prefixes as pasted.

**Governing material applied:** FC717 prerequisite update v1, UMR parent errata v1 and v2, and the UMR scoped-partial verdict. The packet's "UMR pending" wording (pkg LF14–18, proof LF19–20, scope LF31) is read as historical and is not a finding. I re-derived every step myself. Nothing here relies on UMR acceptance or on the first-family FC717 review.

**Counts: FATAL 0 · MAJOR 0 · MINOR 2.** Both minors are wording or citation issues in the Sec. 1 application. WC717 itself has no findings.

| Claim | Source | Verdict |
|---|---|---|
| WC717: (A1)–(A4) imply Ξ(S_ev)+Ξ(S_od) ≤ −1 | proof LF35–49, LF71–185 | **CORRECT** (0F/0M/0m). Every branch re-derived; the case split is exhaustive |
| FC717: no avoider has an admissible NF with k=18, κ̂=7 at (7,17) | proof LF13–17, LF51–63, LF187–192 | **CORRECT relative to the accepted UMR-F scope** (0F/0M/2m). Covers every frame, including RES. Uses nothing outside UMR-F, so no unaccepted dependency remains |
| First failing step | — | None |

## 1. WC717 from (A1)–(A4) only

**Excess bound (1), LF38–40.**
- There are exactly 30 letters and each |c_l| ≥ 1, so e = Σ(|c_l|−1).
- The A-part of that sum is ν−a ≥ 0 and the A^c-part is ≥ 0.
- This is purely definitional; it does not use (T). ✓

**Types, LF74–78.**
- Since q+q′ = 30: type G gives 6−q ≤ 1 and 6−q′ ≤ 1, so χ = 1.
- Type P (q′ = k ≤ 4) gives q ≥ 26 and 6−k ≥ 2, so χ = 6−k. Type Q is symmetric.
- Not-G means min(q,q′) ≤ 4. P and Q together would force q+q′ ≤ 8, so they are exclusive.
- For any tie-break, the top five are ≥ t and the bottom four are ≤ t. ✓

**Lemma 1, LF80–96.**
- **(a)** (W) gives Θ(J) ≤ −1−ν < 0, which rules out t ≥ 0. The bottom four are then ≤ −1, so Ξ ≤ −3. ✓
- **(b)** 5t ≤ Θ(J) ≤ 4−k−ν ≤ 4, so t ≤ 0.
  - If t ≤ −2, then Ξ ≤ −2−k.
  - For any t ≤ −1, an empty bottom run is even and ≤ −1, hence ≤ −2, so Ξ ≤ 2−k−e_B.
  - This extension to all t ≤ −1, used at LF107, is valid. ✓
- **(c)** t = 0 gives ν+k ≤ 4, and l ≤ a+k.
  - The empty top runs (at least 5−l of them) are ≥ 0, nonzero and even, hence ≥ 2. So Θ(J) ≥ 10−2l, which also holds trivially when l ≥ 5.
  - Combining: 6 ≤ 2a+k−ν ≤ ν+k ≤ 4, using a ≤ ν. Contradiction. ✓
- **(d)** |L(J)^c| ≤ |A∖L(J)| + |A^c∖L(J)| ≤ a+k ≤ 4.
  - Nonempty bottom runs are ≤ 0. Empty bottom runs are ≤ −2, which needs the nonzero property.
  - Hence Ξ ≤ −2−k+2n_B. ✓

**Lemma 2, LF98–117.** L(J_1) and L(J_2) are disjoint because S_1 and S_2 are disjoint run sets.
- **(a)** A^c ⊆ (A^c∖L(J_1)) ∪ (A^c∖L(J_2)), so 13 ≤ a′ ≤ 8. Contradiction, independent of t. ✓
- **(b)** At most k_1+k_2 letters lie outside L(J_1)∪L(J_2), and the eight bottom runs draw only on these letters.
  - So e_{B_1}+e_{B_2} ≥ 8−k_1−k_2.
  - The sum is then ≤ 4−k_1−k_2−(8−k_1−k_2) = −4. ✓
- **(c)** Disjointness gives a ≤ α_1+α_2, so |L(J_i)| ≤ α_{3−i}+β_i.
  - With E ≥ 5−α_{3−i}−β_i empty top runs (each ≥ 2) and the rest ≥ −1: Θ(J_i) ≥ 3E−5 ≥ 10−3α_{3−i}−3β_i. This holds even when the bound on E is vacuous.
  - The upper window gives Θ(J_i) ≤ 4−ν−k_i, so 6 ≤ 3α_{3−i}+2β_i−α_i−ν.
  - Summing over i: 2(k_1+k_2)−2ν ≥ 12. Hence the sum is ≤ 4−k_1−k_2 ≤ −2−ν. ✓
- **(d)** If both t_i ≤ −2, the sum is ≤ −4. Otherwise it is ≤ −k_1−k_2−e_{B_2}.
  - The proof refutes k_1 = k_2 = 0, which is a superset of the only bad corner.
  - In that case L(J_1) = A = L(J_2), and disjointness forces A = ∅.
  - Then every run of J_2 is empty, so t_2 is even and cannot be −1. ✓

**Lemma 3, LF121–137.** The hypothesis ν ≤ 4 gives a ≤ 4 and a′ ≥ 26.
- **(a)** l_J ≤ 2 gives q′ ≥ 24 and q ≥ l_J−a.
  - So Θ(J) ≤ max(−1−ν, 4−l_J−(ν−a)) ≤ 4−l_J.
  - If t ≥ −1, the top count gives Θ(J) ≥ 10−3l_J. Together these force l_J ≥ 3, a contradiction. ✓
- **(b)** Take K = the fifth run plus the bottom four. By (a), Θ(K) ≤ 5t ≤ −10.
  - q(K) ≥ a−l and q′(K) ≥ 25 give χ(K) ≤ 6−a+l. This is ≥ 2, so it absorbs the constant 1 in χ.
  - The LOWER half of (W) together with (1) gives Θ(K) ≥ e−(ν−a)−8−l ≥ −9. Contradiction.
  - Only the lower window and the definitional (1) are used, not (T). ✓

**Lemma 4, LF143–176** (J_1 of type P with t_1 = 0).

Setup checks:
- ν+k ≤ 4.
- L(B_1) ∪ L(S_2) = L(J_1)^c, which has at most a+k ≤ 4 letters.
- (3): Ξ(S_1) ≤ −2−k+2n.
- (4): |L(S_2)| ≤ a+k−n ≤ 4−n.
- q′(J_2) ≥ 22, so J_2 is type G or Q, and t_2 ≤ −1.
- Lemma 3's hypothesis ν ≤ 4 holds.

Branches:
- **n = 3, 4:** |L(S_2)| ≤ 1, which contradicts Lemma 3(b). ✓
- **n = 2:** Lemma 3(a) gives t_2 ≤ −2.
  - Type G: the sum is ≤ −5.
  - Type Q: the sum is ≤ −k−k_2. The case k = k_2 = 0 forces L(B_1) ⊆ A∖L(J_2) = ∅, contradicting n = 2. ✓
- **n = 1:** Ξ(S_1) ≤ −k.
  - Type G, or type Q with t_2 ≤ −2: the sum closes directly.
  - Type Q with t_2 = −1: the (2)-type bound and the top count force l_2 = 3 and Θ(J_2) = 1.
  - Then L(S_2) = L(J_2), so all four runs of B_2 are empty with θ ≤ −2.
  - So Ξ(S_2) ≤ ν−5 ≤ −1, and the sum is ≤ −1. ✓
- **n = 0:** Ξ(S_1) ≤ −2−k.
  - Type Q with t_2 = −1 gives a sum ≤ −k−k_2−e_{B_2}.
  - The case k = k_2 = 0 means L(J_1)∪L(J_2) covers all 30 letters, so e_{B_2} = 4.
  - The empty-run bonus is retained. ✓

**Assembly, LF180–185.**
- If some set has t = 0, it must be type P (Lemma 1(a),(c)). Lemma 4 then applies, with that set labelled S_1.
- Otherwise both sets have t ≤ −1:
  - A type-G set contributes ≤ −3, and the other set contributes ≤ 2. The ≤ 2 bound is valid because that set's t ≤ −1 in this branch.
  - P/P is impossible by 2(a), P/Q is covered by 2(b), and Q/Q by 2(c) or 2(d).
- The split is exhaustive.
- Several branches end at exactly ≤ −1. The unit margin against e ≥ 0 is all the argument needs.

**Count hygiene.**
- Secs. 2–5 use only (A1)–(A4) and the definitional (1). (T) is used only at LF189–190.
- None of the following enters the count:
  - UB or RES membership;
  - UMR Lemmas 15–20 or a converse of Lemma 20;
  - the withdrawn saturation or "A^c-saturated" glosses;
  - giant pairs;
  - FQW;
  - windows at any other level.

## 2. Word-level application

- **Scope.** ⌊24/4⌋ = 6 < 7 ≤ 7, with k = 18 and κ̂ = 7. The constants at LF32 are correct, the full existential antecedent is retained, and no premise is added.
- **(A1).** Comes from UMR LF49–56 and LF99–110. The bound a′ ≥ ⌈25/2⌉ = 13 comes from Lemma 5(d).
- **(A2).** Comes from UMR-F and Lemma 10.
- **(A3)–(A4).**
  - Every 5-subset of an alternating set is independent with m = 5, a central level.
  - Lemma 2 gives ℓ = M = 6, and Lemma 7 then gives x = y.
  - Lemma 8 gives U′ ∈ [Π0+2−y−2p, −2−ν0+x]. Using Π0 = `B*`−ν0 and 2p = R+4, the lower end equals e−2−ν−x.
  - UMR-F gives U′ = Θ.
  - Since ε ≤ 1, x ≤ χ, so widening both ends to χ yields (W). ✓
- **(T).** The UMR-F total is Θ(all) = e−4−2ν. With Ξ = Θ+ν+2, this gives Ξ_ev+Ξ_od = e, which is accepted Lemma 14. ✓
- **Quantifiers.**
  - UMR-F holds in EVERY frame (verdict LF9; UMR LF111–112), and a frame always exists. So the contradiction excludes the NF word u, and hence w (UMR LF49).
  - RES frames are covered because no UB condition is assumed.
- **Errata.**
  - v1 does not affect the conclusions used.
  - v2 changes only UMR's residual wording (LF8, 30–32, 309, 371, and "A^c-saturated"). FC717 uses none of that wording.
  - FC717's own phrase "no failing step remains" refers to its own argument.
- **Imports.** Only UMR-F (Lemmas 0–13) is used. Through it, FC717 inherits exactly UMR's accepted inputs (NF, GRX if-direction, SC0 via Y′z, ZSTRUCT/FB at (p−1,κ−1), the S1 definition, LOWER conventions). There are no new imports.

## 3. Findings

**MINOR-1: citation.**
- **Step:** proof LF13 and pkg LF9 list the premises as "UMR-F and Lemmas 3,5,7,8,10,13". The used-range column at LF221 omits UMR LF64–68 and LF133.
- **Why it matters:** LF55 takes ℓ_5 = M_5 = 6 from UMR Lemma 2, and Lemma 7's ℓ and M are fixed at UMR LF133.
- **Consequence:** none mathematically. Lemma 2 is within the accepted Lemmas 0–13, the values are pure arithmetic, and both loci lie inside the frozen manifest range LF1–258.
- **Repair:** add "Lemma 2 (LF64–68) and LF133" to the premise list and used ranges.

**MINOR-2: wording at proof LF54.**
- **Step:** LF54 says "Empty-run evenness is the only use of the genuine empty-run rule". This misattributes the source.
  - By UMR Lemma 10 (LF208–209), evenness comes from L_e = ∅.
  - The genuine empty-run rule supplies the NONZERO property.
- **Where nonzero is load-bearing:** Lemma 1(c), 1(d), 2(c) and 3(a), and therefore all of Lemma 4. Without it, case H fails because empty bottom runs at t = 0 could equal 0.
- **Consequence:** none for the proof. (A2) at LF41 correctly states NONZERO EVEN, and both properties come from accepted Lemma 10.
- **Repair:** reword LF54 to "the nonzero-even property of empty-run θ (evenness from L_e = ∅, nonzero from the empty-run rule) is the only special use of empty runs."

**Uncounted editorial notes:**
- k is overloaded: the terminal k = 18 versus the deficit q or q′ in Lemmas 1–4.
- B (the label sum) versus B_S (the bottom set).
- LF147 says "these four letters" where it means "these at most a+k ≤ 4 letters".

## 4. Axes

- **Correctness:** as given above.
- **Completeness:** complete for the single cell. It says nothing about the remaining-middle interval or about any union of cells.
- **Process:** the disclosed items are process qualifications only, and I could not verify any of them. They are:
  - the worker's authorship of UMR;
  - a freeze that is not certified as strict preregistration;
  - two pre-creation text replacements;
  - a JSON manifest checked by eye;
  - metadata-only use of Python.
- **Priority/novelty:** not assessed and not claimed.
- **Computation:** none in this review. This is a written model review, not a human or Lean/kernel verification.

## 5. Nonclaims preserved

This review does not claim any of the following:
- any other cell, including (7,19) and (8,19), any other k, or any other prime;
- a full p=17 union or any composed frontier statement;
- exclusion of the remaining-middle interval;
- full ordered Olson, `INV*`, rigidity or o_F assembly;
- universal UB, RES nonemptiness or saturation, or a Lemma 20 converse;
- that UMR itself excludes any cell;
- priority, novelty, Lean, human-referee or runtime status.

FC717 acceptance and any composition remain with the parent.
