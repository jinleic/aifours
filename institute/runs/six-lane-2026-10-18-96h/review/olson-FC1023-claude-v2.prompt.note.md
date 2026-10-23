# FC1023 v1: independent written review (second family, no tools)

**Counts: FATAL 0 · MAJOR 0 · MINOR 0.** I found no flaw. I applied governing erratum v1. All three of its items are wording only, match the text, and change no bound.

This review uses only the pasted packet. I opened no files, ran no code and did no numerics; every constant and inequality below was re-derived by hand. Codex's count was not an input.

## Claim-wise verdicts

### Imports (proof LF11–52)

| Claim | LF | Verdict | Re-derivation |
|---|---|---|---|
| Cell lies in the UMR range | 19 | correct | ⌊30/4⌋ = 7 < 10 ≤ (23−3)/2 |
| Constants | 31 | correct | R = 42, g = 4, δ = 16, h = H = 12, central levels 2..11. Run letters: 90 − (24 + 2·12) = 42 |
| (A1) Labels and counts | 33–36 | correct | Labels are odd (UMR LF81–88). ν ≥ a and e ≥ 0. a′ ≥ (3κ+g)/2 = 17 (UMR LF118) |
| (A2) Parity for **all** runs | 37–41 | correct | UMR Lemma 10, LF202, gives θ_i ≡ σ_i for every run. This descends from Lemma 8 (U ≡ σ(P)) through Lemma 9. Odd c_l then gives σ_i ≡ \|L_i\|. An empty run has nonzero even θ (LF203, 208–209). All of this is inside verdict LF9 (Lemmas 0–13) |
| (A3) U6/U7 | 42–50 | correct | (ℓ6, M6) = (10, 8) and (ℓ7, M7) = (8, 10). up = −2 − ν + x (UMR LF164–165); replacing ε by 1 only weakens it. U′ = Θ on all of Cl (Lemma 13; UMR erratum v1 restricts the link but keeps the conclusion). m(Q) = \|Q\| (LF252–254) |
| (A4) Ξ and the total identity | 51–52 | correct | h − κ = 2. Θ(all) = B − 2ν − 46 = e − 2ν − 4, so Ξ_ev + Ξ_od = e |

### Local lemmas

- **Definitions, LF54–57: correct.** q = α + β, q′ = α′ + β′, l = a − α + β (= β′ + a′ − α′), and n ≤ l.
- **Lemma 1, LF58–62: correct.** All three cases hold:
  - |L| = 0: θ is nonzero even, so θ ≥ 2 or θ ≤ −2.
  - |L| = 1: θ is odd.
  - |L| ≥ 2: the length alone gives 2.
  - Summing is valid because occurrence sets are disjoint.
- **Lemma 2, LF63–68: correct.**
  - (a) Every letter lies outside at least one of two disjoint letter sets.
  - (b) A letter outside both lies in A^c∖L(Q1) or in A∖L(Q2), and α′ ≤ q′, α ≤ q. Bottoms of the opposite sets avoid both tops.
- **Sorted estimates, LF70–74: correct.**
  - If t ≤ −1, the bottom sum is ≤ −b − E.
  - If t ≤ −2, the bottom sum is ≤ −2b.
  - If t = −1, the top sum is ≥ 2r − 3n, because an empty top θ is nonzero even and ≥ −1, hence ≥ 2.
- **Types, LF78–82: correct, exhaustive and exclusive.** Use q + q′ = 42.
  - Q6 (q ≤ 8): 8 − q′ = q − 34 ≤ −26, so χ6 = 10 − q ≥ 2.
  - P6 (q′ ≤ 6): χ6 = 8 − q′.
  - Otherwise q ≥ 9 and q′ ≥ 7, so χ6 = 1 (G6).
  - P and Q are disjoint because q + q′ ≤ 14 < 42. Level 7 works the same way.
- **Lemma 3, LF83–86: correct.** Θ + l ≤ 8 − (ν−a) − 2α ≤ 8 < 12 for Q6, and Θ + l ≤ 6 < 14 for Q7.
- **Lemma 4, LF87–93, with erratum item 1: correct.**
  - 6 ≤ Θ(J6) ≤ 6 − ν − q′ forces ν = q′ = 0. So A = ∅, L(J6) holds all 42 letters, and the other 18 runs are empty.
  - Bottom θ ≤ 1 and nonzero even, so ≤ −2, giving Ξ(S) ≤ −4.
  - For S′, q(J6(S′)) = 0. Lemma 3 plus evenness gives t6 ≤ −2. The top is ≤ 8 (χ6 = 10) and the bottom ≤ −12, so Ξ(S′) ≤ −2.
  - Total ≤ −6. Positive weights stay arbitrary odd numbers; there is no unit-label or e = 0 premise.
- **Five classes, LF94–100: correct.**
  - G6 gives t6 ≤ −1, since Θ(J6) ≤ −1 − ν < 0. Q6 gives t6 ≤ −1 by Lemma 3.
  - P6 splits into t6 ≥ 1 (Lemma 4) or t6 ≤ 0 (C2). Q6 splits by the type of J7.
  - So each set is exactly one of: positive P6, C1, C2, C3, C4, C5.
  - In C5, t7 ≤ t6 ≤ −1. The nonnegative hybrid is therefore excluded by derivation, not by assumption.
- **Lemma 5, LF101–112: correct.**
  - (a) G6: (−1−ν) + (−6−E) + ν + 2 = −5 − E. G7: −4 − E.
  - (b) P6 with t6 ≤ 0: the top is ≤ 6 − ν − z, and the bottom mass is ≤ l(B6) − 12. If t6 = 0, then ν + z ≤ 6, the letters outside L(J6) number ≤ a + z ≤ 6, so l(B6) ≤ 6.
  - (c) Q7: the top is ≤ 6 − ν − z and t7 ≤ −1. This gives all three stated bounds (erratum item 2 is consistent).
  - (d) C5: (8 − ν − z₊) + (−5 − E) + ν + 2.
- **Lemma 6, LF116–131: correct.**
  - A G-class set with any of C1–C4 gives ≤ −4 + 3 = −1. This also holds under the broader reading "any set whose J7 is G7", since the G7 bound needs only Θ(J7) ≤ −1 − ν.
  - P6/P6: 17 ≤ a′ ≤ α′ + α′ ≤ 12, a contradiction.
  - P6/Q7: ≤ −6 − (z1+z2) + l(B6¹) + l(C7²) ≤ −6. This covers t6 = 0 and needs no spare-letter assumption.
  - Q7/Q7, case (−1, −1): each side gives 8 + ν ≤ 3α_{3−i} + 2β_i − α_i. The sum gives z1 + z2 ≥ 8 + ν.
  - Q7/Q7, case (≤−2, ≤−2): the sum is ≤ −4.
  - Q7/Q7, mixed case: n(K2) ≥ ⌈8/3⌉ = 3 and n(K2) ≤ α1 + β2 ≤ z1 + z2, so the sum is ≤ −2.
  - These threshold cases are exhaustive.
- **Lemma 7, LF135–155: correct.**
  - z₊ = 42 − z0 − β(u) + β′(u), so β(u) ≥ 26. This is derived, matching erratum item 3.
  - a ≤ β′(J7) + α(J6) ≤ 16. For any Q ⊆ S′, β(Q) ≤ α′(J7) ≤ 8, so q′(Q) ≥ 18.
  - Hence S′ is not P6 (including positive P6) and has no P7 top, so S′ is C1, C3 or C4. Hybrid/hybrid is impossible.
  - o ≤ z0 + z₊.
  - S′ in C1: ≤ z0 − 11 ≤ −3. S′ in C3: ≤ z0 − 9 ≤ −1. S′ in C4: Lemma 2(b) with (J7(S), J7(S′)) gives ≤ −2.
  - The empty-count inequalities stay valid when their right-hand sides are negative.
- **WC1023, LF159–163: correct and complete.**
  - Case tree: if either set is positive P6, apply Lemma 4. Otherwise both lie in C1–C5. Any C5 goes to Lemma 7; the rest go to Lemma 6.
  - This covers every pairing and every tie choice.
  - It uses only (A1)–(A3) and the definition of Ξ. The total identity does not appear.
- **FC1023, LF164–167: correct relative to accepted UMR.**
  - A frame exists (UMR LF111–112), and UMR-F holds in every frame, which supplies (A1)–(A3).
  - WC1023 then gives Ξ_ev + Ξ_od ≤ −1, while (A4) gives the sum = e ≥ 0. Contradiction.
  - The existential-NF antecedent is therefore excluded.
- **Package claims, LF17–34:** each matches the proof, and none adds a premise.

**Margins.** Two pairings close at exactly −1: G-class with C4 (−4 + 3), and Lemma 7's C3 case at z0 = 8. An off-by-one in (ℓ, M) or in h − κ would break the proof at these points. I re-derived those constants, and they are right.

## Editorial notes (not findings; nothing needs repair for correctness)

1. **Proof LF94–95 and LF106.** The text states that t7 ≤ −1 for a G7 top but does not argue it. The argument is the same as LF94 gives for G6: the top-7 sum is ≤ −1 − ν < 0. In C3 it also follows from t7 ≤ t6 ≤ −1.
2. **Proof LF25, "(A1)–(A3) alone".** The count also uses the definition of Ξ, which is shown inside (A4) at LF51. That is a definition, not the total identity, so the "identity only at the end" rule still holds.
3. **Proof LF174–175.** The summary list leaves out q + q′ = 42, which is part of (A1). It is used in the type split and at LF138–139.

## Scope of this verdict

- **Correctness:** I checked every load-bearing step and found no counterexample.
- **Completeness:** every frame, tie choice, threshold sign and pairing is covered. There is no residual, and R23 membership is never used.
- **Premise boundary:** the only premises are UMR Lemmas 2, 5(c)(d), 7–8, 10 and 13, plus frame existence, with the UMR-F total or Lemma 14 used only at the end. No UFC, E0, ENV, UB, RES, Lemma 15–20, saturation, giant-pair or FC717/FC19 internals are used. The exposure disclosures are not premises.
- **Process:** not certified. I did not check hashes, byte counts, timestamps, freeze cadence or checkpoint contents. "By hand" is the author's own report.
- **Computation:** none, for this review or required by the proof.
- **Priority, novelty, Lean, human review, runtime:** no claim.

**Status:** FC1023 (via WC1023) is correct and complete, conditional only on accepted UMR at its literal scopes. Acceptance is the parent's decision. This verdict makes no claim about other cells, the p23 union, full UFC, full ordered Olson, the whole research target or runtime.
