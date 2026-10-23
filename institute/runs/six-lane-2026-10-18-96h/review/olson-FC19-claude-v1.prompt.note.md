# Independent written review: FC19 v1, cells (7,19) and (8,19)

**Basis.** I used only the pasted selected text: package LF1-102, proof LF1-261, scope LF1-78, process erratum LF1-18, authority LF1-49, UMR verdict LF1-38, UMR proof LF1-258 and LF344-355, UMR errata v1 and v2, and FQW LF9. I used no tools, files, computation or enumeration. Every step was re-derived by hand from the literal UMR statements. All errata are applied. The parent checked the hashes and ranges; I did not treat them as mathematical evidence.

## Counts: FATAL 0 · MAJOR 0 · MINOR 1

The single MINOR is interface wording with no mathematical effect.

| Cell | Correctness | Completeness | First failing step |
|---|---|---|---|
| (7,19), k=20, κ̂=7 | No error found in WC719 or Theorem FC19(a) | Complete: every frame and every type pair, with no residual | None |
| (8,19), k=20, κ̂=8 | No error found in WC819 or Theorem FC19(b) | Complete: every class pair, including both C6 branches, with no residual | None |

- Each cell depends only on UMR-F (Lemmas 0–13) and Lemma 14, at the literal scope of verdict LF7-11.
- Both of those are parent-accepted, so no load-bearing dependency is left unresolved.
- Neither part cites the other: Part (a) uses Secs 1–2 and Lemmas 3.x; Part (b) uses Secs 1–2 and Lemmas 4.x.

## 1. Interface audit: the data (D1)–(D4) against UMR

| Item (proof LF) | Re-derivation from UMR | Verdict |
|---|---|---|
| (D1)(1) e ≥ ν−a ≥ 0 (LF39-42) | Labels are odd (UMR LF88, LF101). e* = B*−R (LF108) = (ν₀−a)+(Π₀−a'), and each bracket is ≥ 0 because every \|c_l\| ≥ 1. | ✓ |
| (D1)(2) ν ≡ a (mod 2) | ν is a sum of a odd numbers. | ✓ |
| (D1)(3) a' ≥ 14 | Lemma 5(d) (LF118) gives a' ≥ (p+κ+1)/2, which is 13.5 at (7,19) and 14 at (8,19); a' is an integer. | ✓ |
| (D2) | UMR-F LF27 and Lemma 10 LF203/208-209: an empty run has a nonzero even θ. | ✓ |
| (D3) (U_j) and (L_j) | Lemma 8 (LF162-165) gives U' ∈ [Π₀+2−y−2p, −2−ν₀+x]. With Π₀ = R+e*−ν₀ and R−2p = −g, the lower end is e−g+2−ν−y. Lemma 13 (LF238-239) gives U' = Θ on Cl. A j-subset of S_ev or S_od with j ≤ 9 has m = j (LF55-56, LF252-254). j=5 lies in 3..8, and j=5,6 lie in 2..9. (ℓ_j, M_j) is (6,4) at (7,19) level 5, and (8,6) and (6,8) at (8,19) levels 5 and 6. These match LF345 and LF351. x and y are exactly as in Lemma 7 (LF137-138), with ε = q mod 2. | ✓ |
| Erratum v1 | It restricts only Lemma 13's level-addition link to g/2 ≤ m ≤ κ, and Cl stays connected. The levels used here (5 and 6) are ≤ κ in both cells, so the restriction is never touched. Erratum v2 is wording only. | ✓ |
| (D4) | Lemma 14 (LF256-258) with h−κ = g/2 (LF19) gives Ξ = Θ+ν+3 at (7,19) and Θ+ν+2 at (8,19). It is used only at LF128 and LF230, after the count. | ✓ |
| ε (offset) weakening | Every replacement of ε by 1 enlarges x (upper window) or y (lower window), so it only weakens the bound. The one place ε is not weakened (Lemma 4.6 Step 2) is closed by contradiction: the ε-branch would give Θ(Q_v) ≤ −2−ν+1 < 0. | ✓ |

**Common facts F1–F4 (LF67-83).**
- F2: a letter cannot lie in both of two disjoint letter sets. The count of letters outside both sets is ≤ α'(Q₁)+α(Q₂).
- F3(a)–(f) follow from (D2): an empty run with θ ≥ −1 has θ ≥ 2, and one with θ ≤ 0 has θ ≤ −2.
- F4: if q ≤ ℓ−2, then ℓ−q ≥ 2 > ε and q' ≥ R−ℓ+2 > M. The symmetric case is the same.
- Verdict: all ✓.

## 2. Cell (7,19): claim-wise

| Claim | Key re-derived step | Verdict |
|---|---|---|
| Types G/Q/P (LF87-92) | F4 at (6,4): G holds iff q ≥ 5 and q' ≥ 3, which gives x ≤ 1. Q is q ≤ 4 with x = 6−q. P is q' ≤ 2 with x = 4−q'. Q and P cannot both hold because q+q' = 32. | ✓ |
| 3.1(a) | Θ(J) ≤ −1−ν, so t ≤ −1, so Θ(B) ≤ −5−e(B), so Ξ ≤ −3−e(B). | ✓ |
| 3.1(b) | If t ≥ 0: ν+k ≤ 4 and 10−2a−2k ≤ 4−k−ν. Using a ≤ ν, this gives 6 ≤ a+k ≤ 4, impossible. So Ξ ≤ 2−k−e(B), and Ξ ≤ −3−k when t ≤ −2. | ✓ |
| 3.1(c) | Θ(J) ≤ 2−k−ν ≤ 4, so t ≤ 0. If t ≤ −1, Ξ ≤ −k−e(B). | ✓ |
| 3.1(d) | ν+k ≤ 2. At most a+k ≤ 2 letters lie outside L(J). Then Ξ ≤ −5−k+2n(B) ≤ −1−k. | ✓ |
| 3.2(a) | 14 ≤ a' ≤ 2+2, a contradiction. | ✓ |
| 3.2(b) | The 10 runs of B¹∪B² have ≤ k₁+k₂ letters, so the sum is ≤ (−k₁−e)+(2−k₂−e) ≤ −8. | ✓ |
| 3.2(c) | If some t_i ≤ −2, the sum is ≤ −1. If both t_i = −1, each set gives 6+ν+α_i ≤ 3α_j+2β_i. Summing gives k₁+k₂ ≥ 6+ν, so the sum is ≤ −2−ν. | ✓ |
| 3.2(d) | λ+l(B¹) ≤ 2, and q'(J²) ≥ a'−λ ≥ 12, so J² is G or Q. e(B²) ≥ 3+n(B¹). The sum is ≤ −9 if J² is G and ≤ −4 if J² is Q. | ✓ |
| Completion (LF125-129) | Per-set maxima: G −3, Q 2, P with t ≤ −1: 0, H −1. Pairs: G with anything ≤ −1; P with P impossible; P(t≤−1) with Q ≤ −8; H with Q ≤ −2; Q with Q ≤ −1. This covers every pair. | ✓ |

## 3. Cell (8,19): claim-wise

| Claim | Key re-derived step | Verdict |
|---|---|---|
| Types and C1–C6 (LF133-141) | F4 at (8,6) and (6,8). The classes are exhaustive once P5 forces t5 ≤ 0. | ✓ |
| 4.1(a)–(d) | Ξ ≤ −4−e(B5) for C1; t5 ≤ 0 for P5 and Ξ ≤ 1−k−e(B5) for C2; C3 leaves ≤ 4 outside letters and gives Ξ ≤ −4−k+2n(B5); Ξ ≤ −3−e(B6) for C4. | ✓ |
| 4.1(e) | If t6 ≥ 0, then 8 ≤ a+k ≤ 4, impossible. So Ξ ≤ 2−k−e(B6), and Ξ ≤ −2−k when t6 ≤ −2. If t6 = −1, then 3n(J6) ≥ 8+k+ν, so n(J6) ≥ 3. | ✓ |
| 4.1(f) | k6 = 34−k5−β(u)+β'(u), so β(u) ≥ 22 and a ≤ k5+k6 ≤ 12. For Q ⊆ S', β(Q) ≤ α'(J6) ≤ 6, so q'(Q) ≥ 16. If t6 ≤ −1, Ξ ≤ 4−k6−e(B6). | ✓ |
| 4.2 | (L5) with g = 4. y5 ≤ max(1, 6−q) because 8−q' ≤ 1. q ≥ a−β'. e−ν ≥ −a, using (D1)(1) and not just e ≥ 0. So Θ(K) ≥ −2−max(a+1, 6+β') ≥ −9 > −10. | ✓ |
| 4.3(a)–(c) | (a): 14 ≤ 4+4, a contradiction. (b): the 9 runs give a sum ≤ −6. (c), mixed case: a sum ≥ 0 forces L(J6¹) = A = L(J6²), so all six runs of J6² are empty and t² is even, not −1. (c), both t = −1: k₁+k₂ ≥ 8+ν. | ✓ |
| 4.4 (C3) | m+λ ≤ 4 and a ≤ 4. q'(Q ⊆ S₂) ≥ 10, so S₂ is C1, C4 or C5. Bounds: C1 ≤ −5; C4 ≤ −3; C5 with t6 = −1 ≤ −3. C5 with t6 ≤ −2: B5(S₂) contains the sixth run, whose θ is t6 ≤ −2; Lemma 4.2 gives λ ≥ 2, so the sum is ≤ 0−2. | ✓ |
| 4.5 (C6, t6 ≤ −1) | S' is C1, C4 or C5. The sums are ≤ k5−9 ≤ −3, ≤ k5−7 ≤ −1, and ≤ −2. | ✓ |
| 4.6 Step 1 | ν+2α(J5) ≤ a+1, so α(J5) = 0 and, by parity, ν = a. Hence A ⊆ L(J5), β'(u) = 0, k6 = o+a and β(J5) ≥ 4−a. | ✓ |
| 4.6 Step 2 | Q_v is a central 5-set with θ ≥ 0 throughout. Because u is nonempty, Θ(Q_v) ≥ 2e(J5∖{v}). q(Q_v) ≥ 22 kills the 8−q term. q'(Q_v) = o+β(v)+a−β'(v). This gives (*) for every v. | ✓ |
| 4.6 Step 3 | Summing over all five v: Σβ(v) ≥ 4−a; Σβ'(v) = a (this needs Step 1); each empty run is counted 4 times. So 5o+8a+8e(J5) ≤ 16 and o+a ≤ 3. | ✓ |
| 4.6 Steps 4–5 | S' contains no letter of A, and J6(S') is Q6. t6(S') ≤ −2 contradicts Lemma 4.2. With t6(S') = −1: a = 0 and o = 3; then Ξ(S) ≤ −3 and Ξ(S') ≤ −5. | ✓ (see O1) |
| Completion (LF226-231) | Any C3 is handled by 4.4. Otherwise any C6 is handled by 4.5 or 4.6. Otherwise the per-class maxima are −4, 1, −3, 2. The pairs C2·C2, C2·C5 and C5·C5 are excluded or bounded by 4.3. | ✓ |

## 4. Premise hygiene

- **No forbidden premises.** No step uses UB, RES, Lemmas 15–20, saturation, a converse, or any FC717 lemma or constant.
- **Every frame.** (D1)–(D3) hold in every frame (UMR LF111-112), and no frame is selected.
- **Full antecedent.** Arbitrary reflection pairs and the empty-run rule enter only through the UMR scope (verdict LF7) and Lemma 10.
- **Identity used once, at the end.** (D4) enters only for the final contradiction.

## 5. Finding

**MINOR-1 (interface wording).**
- **Step.** Proof LF257-258 lists the primitive inputs "(NF, GRX, SC0, ZSTRUCT/FB, (S1), LOWER and FCW errata)" as entering through accepted UMR, citing UMR LF393-399. Scope LF38 also adds "balfull".
- **Conflict.** Verdict LF24 accepts only NF, GRX if-direction, SC0 applied to Y′z, ZSTRUCT/FB at the exact (S′) parameters, the S1 definition and the stated LOWER conventions. It promotes no FCW lemma. LF393-399 is outside the review excerpt.
- **Consequence.** None for either theorem: no FC19 step invokes a primitive input directly. A reader could, however, take FCW errata or balfull to be accepted inputs.
- **Repair.** A wording erratum: "only the inputs listed at UMR verdict LF24."

**Observations (not counted, no repair needed):**
- **O1.** The final branch of Lemma 4.6 is in fact vacuous. q(J6(S′)) = a+l ≥ n, and the Lemma 4.1(e) inequality gives 3n ≥ 8+q+ν, so n ≥ 4 > o. The stated −8 bound is still valid.
- **O2.** In 4.1(f), the clause "q(J6) ≥ 22" is redundant: F4 alone gives x6 = 8−k6.
- **O3.** The symbols k (4.1) and m (4.4) are overloaded, but every use rebinds them explicitly.

## 6. Distinctions

- **Correctness and completeness:** as in the table at the top; no error found and no residual in either cell.
- **Process:** the freeze time, checkpoint gaps (420/783/630/84 s) and prior exposure are self-reported, and I do not certify them. The disclosed exposure is UMR authorship, full knowledge of the FC717 method, and unwritten pre-freeze attempts on these cells. Correctness does not depend on any of this, because every step is re-derivable from accepted statements. Process erratum 1 is wording only. The inherited UMR process qualifications remain.
- **Priority and novelty:** not assessed.
- **Computation:** none was used in this review, and correctness does not depend on any machine step.

This review does not approve the research target, runtime, a full p=19 or ordered-Olson statement, or any other cell. Acceptance and any composed claim belong to the parent.
