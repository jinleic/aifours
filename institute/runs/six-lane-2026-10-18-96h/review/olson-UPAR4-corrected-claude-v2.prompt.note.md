# UPAR4: second-family full mathematical review (Claude, claude-opus-5-5, hand only)

**What was reviewed:**
- `proof-UPAR4-v1.md` LF1–190, as pasted (pin `bd4f51d4…`), read through parent erratum v1 (`066122…`).
- `UPAR4-scope-v1.md` LF1–79.
- Every governing body and excerpt supplied in the packet.

**How:**
- I re-derived every identity and inequality listed below by hand from the pasted text.
- The Codex review's content was not in the packet. I inferred nothing from the overlay's report of its outcome.
- No tools, code, machine computation, enumeration, network or delegation were used.

**Outcome: 0 FATAL / 0 MAJOR / 7 MINOR.** UPAR4-P and UPAR4-R (literal R4) pass at their stated scope. Every MINOR concerns wording, notation, an unstated justification or a citation. None changes an inequality, branch, cell or residual test.

## Per-claim verdicts

**Overlay s_J (LF58–61): PASS.**
- For a near-A r-top J, q ≤ ℓ_r−2 gives M_r−q′ ≤ δ−R < 0. So x = ℓ_r−q, and Θ(J) ≤ 2κ−2r−ν−q(J) = A0−ν−q(J).
- Hence s_J ≥ 0. It is even, because Θ(J) ≡ l(J) ≡ a+q(J) ≡ ν+q(J) mod 2.
- s_Q equals sQ of LF47. Count and Order are unchanged, and no premise is added.

**§1 common data: PASS.**
- **Endpoints.** Θ(Q) = A0−ν−z−sQ and Θ(K) = P0−ν−zP−sP. For P_{r+1}, x = M−q′ because ℓ−q ≤ ℓ+M−2−R < 0.
- **Letter partition.** α′(K)+α(Q) = β(Q)+β′(K)+l(X)+l(Y). Hence zP+z = 2W+l(X)+l(Y), and zP = W+β(X)+β(Y).
- **(Defect).**
  - Use Θ(X∪Y) = l(X)+l(Y)−2(2κ+2d−2r−1)−D_X−D_Y.
  - Adding the two endpoints and using ID gives F−e = 2W+sP+sQ+D_X+D_Y exactly.
  - sP, sQ and D_i are even (parity) and ≥ 0 (Lemma 1).
  - B0 ≥ 2 is the imported UPAR3-Z gap.
- **Tail bounds and (Strong-count).** θ ≤ −1 gives |L_i| ≤ D_i+1. θ ≤ −2 gives |L_i| ≤ D_i, so every nonempty strong run has D_i ≥ 2.
- **(Order).**
  - Exactly, zP+sP = 2b−2d+z0+s_I−θ_u.
  - θ_u ≤ −1 always.
  - θ_u ≤ t_r(S) ≤ −2 when I is strong.
- **(Count).**
  - Start from 2r−3l(J) ≤ A0−ν−q(J)−s_J, and use 2r−A0 = 2b, l = a−q+2β and ν = a+η. This gives 2a ≥ 2b+4q(J)−6β(J)+η+s_J.
  - For I, β(I) = z0−a+β′(I) gives z0 ≥ 2a+b−3β′(I)+(η+s_I)/2 ≥ 2a+b−3wA.
- **(Pred).**
  - QQ-1 with ID gives e+ν+E ≤ 4κ−6r = κ−3b.
  - QQ-mixed gives e ≤ (κ−b−2d)/2−z0−z.
  - Lemma 3(a)/(b) are imported as accepted.
- **(Cap).** ⌈(a+1)/2⌉−1 = ⌈(a−1)/2⌉ ≤ a/2.

**§2 weak-I/strong-Q, unconditional: PASS.**
- (M1) is exact algebra.
- wA ≤ B0/2 and b ≤ (κ−2d−2e)/3 give a ≤ κ/2−4d+3/2−7e/4−z/2 < δ+1. So the Cap domain is proved before Cap is used.
- Strong Y gives E(Y) ≥ y0−B0/2+W.
- Cap and 2y0 = κ+2d−b then give a ≥ κ−3b+4d−2+e+2W.
- The gap is 3τ/4+6d−2+3e/2+2w+wA/2+z/2 ≥ 10. There is no restriction on Γ, κ or e.

**§3 aggregate charge when Γ>0: PASS.**
- Γ>0 is equivalent to 2·qstar > Λ.
- 2·tmax−Λ = κ−3b+4d+e+2W > 0 under either form of (Pred).
- Q∪V is an independent subset of S′ with central size r+t in [d, κ+1].
- The entry the window needs is at least qstar−t+2 ≥ 2, using sQ+D_V ≤ Λ.
- The P entry is ≤ −A0/2−8d+7−e < 0 (see m1).
- So only the ℓ entry can supply it. Because Θ(V) = l(V)−2t−D_V exactly, this is equivalent to (Charge): 2β(V) ≤ sQ+D_V.

**§4 both weak, when Γ>0: PASS.**
- (W1) and (W2) are exact.
- a ≤ (κ+b)/4−5d/2+1−e < δ+1, so the Cap domain is proved first.
- n(Y) ≤ β′(Y)+β(Y) ≤ α+β(Y). This counts letters, not weights.
- Hence a+2α ≥ κ−b−sQ−D_Y. With the Q-Count, κ ≤ 2a+w−η/2+sQ/2+D_Y.
- Chaining: κ ≤ x0+B0−3b+2d−1+2wA+D_Y/2−η/2 ≤ x0+2B0−3b+2d−1−η/2.
- That equals (κ+b)/2−5d+2−2e−η/2, which is ≤ κ−6d+1−2e−η/2 < κ. Contradiction.

**§5 strong-I/weak-Q, when Γ>0: PASS.**
- β(X) ≤ D_X, so zP+sP ≤ W+D_X+sP+(sQ+D_Y)/2 ≤ B0−W.
- Strong Order gives zP+sP ≥ 2b−2d+2. The gap is 2d+e > 0.
- Only Aggregate, Order and the strong tail are used.

**§6 Γ bounds, T4 and branch completeness: PASS.**
- Γ = 2κ−8b−2z+12d−6+3e+6W.
- **(G-WW)** is reproduced exactly: the term (−κ+44d−22+18e)/3, plus 3w+6wA+3η/2+sQ/2.
- **(G-SW)** is reproduced exactly: 3Γ ≥ 5κ−21b+38d−18+11e+12w+16wA+η+sQ, using z0 ≥ α(I) = a−β′(I) ≥ a−wA.
- When κ ≤ 26d−10, these give Γ ≥ 6d−4 and Γ ≥ 2/3 respectively.
- Every branch is covered:
  - both strong is excluded by inheritance (UPAR LF271);
  - weak-I/strong-Q is excluded by §2;
  - the two Q-weak orientations are excluded by §§3–6.
- κ ≤ 26d−10 is equivalent to 27κ ≤ 13p+3 by substitution.
- T3 ⊊ T4 because 18d−16 > 0, and (25,53) witnesses strictness.

**Diagnostics: PASS for each.** Each cell has d=2 and κ=(p−3)/2. Each is in T (p prime, ⌊(p+7)/4⌋ < κ), outside T3 (κ > 22) and inside T4 (κ ≤ 42):

| Cell | 27κ | 13p+3 |
|---|---:|---:|
| (25,53) | 675 | 692 |
| (28,59) | 756 | 770 |
| (29,61) | 783 | 796 |

All three are excluded by the uniform theorem, not by any per-cell computation.

**UPAR4-P: PASS (scoped candidate).**
- T3 is excluded by accepted UPAR3-P.
- On T4∖T3, every frame induces R3 (accepted UPAR3-R), and §§2–6 contradict every branch.
- Frames always exist (UMR), so no such NF exists.

**UPAR4-R and literal R4: PASS.**
- R3^lit is a literal intersection.
- Each new conjunct is proved necessary:
  - κ > 26d−10 follows from UPAR4-P;
  - Q weak follows from §2 together with R2's exclusion of both-strong;
  - Γ ≤ 0 follows from §§3–5.
- No R2 or R_PAR test is deleted.
- R2(4)'s F=0 branch is vacuous because F ≥ e+2 ≥ 2.
- (G-WW) and (G-SW) are implied tests and therefore redundant.
- Finiteness is claimed only for each fixed (κ,p).

**CHARGE-FAILURE-COVER and the scope statements (LF156–176): PASS.**
- It is correctly stated as unproved.
- It is equivalent to nonexistence on T∖T4 at terminal k = p+1.
- I found no overclaim.

## Requested focus items

- **Quantified branches: covered.**
  - Orientations: four pairs, of which one is excluded by inheritance, one unconditionally (§2) and two under Γ>0.
  - The sign of Γ, and the κ cutoff.
  - The number of positive-containing runs in Y: at least tstar, between 1 and tstar−1, or none.
  - The Cap domain at both places it is used.
  - No split on e, η, the parity of κ, p mod 4 or tie-breaking is needed, and none is made.
- **Nonunit labels and e>0: retained.** e and η stay arbitrary even, nonnegative data, and every e-term enters with the favorable sign:
  - +e in §2's gap;
  - −2e in §4;
  - +e in §5's gap;
  - +6e and +25e/3 in the Γ bounds.

  Cap uses only e ≥ ν−a. Nothing anywhere assumes |c_l| = 1, ν = a or e = 0.
- **Aggregate slack paid once: confirmed.**
  - The window is applied once, to the single set Q ∪ (all positive-containing runs of Y). It is never summed run by run, so sQ and D_Y each carry coefficient 1.
  - The "fewer than tstar runs" step also applies (Charge) once, to a single tstar-subset.
  - Summing per run would have charged sQ t times; the proof does not do that.
- **Γ bound:** both lower bounds were re-derived term by term, and their positivity at the cutoff was checked.
- **Literal R4:** as above, subject to the binding precision in m6 and m7.

## Findings

**FATAL:** none.

**MAJOR:** none.

**MINOR**

- **m1 (LF91–93): unstated steps in the P-entry display.**
  - The first "≤" uses q(Q∪V) = z+β(V)−β′(V) ≤ z+l(V) ≤ z+t+D_V (via LF48), together with M_{r+t} = κ+b+2t−2d and R = 4κ+2d−2.
  - "z ≤ A0" holds because Q is a Q_r top: z ≤ ℓ_r−2 = 2κ−2r = A0 (UPAR LF75).
  - **Fix:** insert both clauses. The display itself is correct.
- **m2 (LF86–88): range of t.**
  - Read "any 1 ≤ t ≤ tstar runs". The case t = 0 is the trivial β(Y) = 0, already covered at LF101.
  - Read "central: d ≤ r < r+t ≤ κ+1 ≤ h−1". The lower end comes from LF46.
- **m3 (LF57, LF78): strong-orientation wording.**
  - LF57's "replace 1 by 2" relies on θ_u ≤ t_r(S) ≤ −2, because u is the (r+1)-st sorted run of S. **Fix:** state this.
  - LF78 should read: "the strong-Q hypothesis t_r(S′) ≤ −2 is used only through θ ≤ −2 on Y; no value inside Q is constrained beyond sorted order." As written it can be misread as a weakened hypothesis.
- **m4: notation collisions.**
  - (a) The scalar W = wA+w (LF41) collides with the window label (W) (LF36, 88, 95) and with the labels (W1)/(W2) (LF108, 110).
  - (b) The counts t, tmax, tstar (LF82–101) collide with the thresholds t_r and with ENV's t/ρ(t), which remain in the literal R4 (UPAR LF223–226).
  - (c) D_i, D_X, D_Y, D_V (LF47) collide with ENV's D(S) and D_r(S) inside R4. The text should also state that D_X+D_Y is exactly UPAR2's tail slack C. That is UPAR2 LF104, called C* in UPAR2 erratum v2 item 2 and D in UPAR3. It is not R_PAR's C(S).
  - (d) τ (LF71) collides with UMR's τ_i (UMR LF52).
  - (e) x0, y0 (LF42) collide with the window entries x, y. This is the same class as UPAR3 erratum v2 m6.
  - **Fix:** add one disambiguation sentence after LF43, or rename. There is no mathematical effect.
- **m5: per-step citations.** LF20 promises precise LF citations for each use, but LF181–187 give only file-level ranges. This is the same class as UPAR3 erratum v2 m2. **Fix:** bind the following.

  | Statement used | Source | Cite at |
  |---|---|---|
  | Θ ≥ 2r−3n and n ≤ l | UPAR LF71–72 | LF58 |
  | Types, endpoints, Q_r thresholds negative | UPAR LF73–78 | LF44, 47, 56 |
  | Lemma 1 | UPAR LF66–69 | LF48 |
  | Cap | UPAR LF102–107 | LF66 |
  | QQ-1 / QQ-mixed | UPAR LF146–155 | LF62–64 |
  | Lemma 3 | UPAR2 LF112–123 | LF62–64 |
  | r-interval, θ_u ≤ −1, at least one exactly −1, both-strong exclusion | UPAR LF266–273; UPAR2 LF204–208 | LF44–46, 145 |
  | F−e ≥ 2 | UPAR3 verdict LF9 | LF54 |
  | m = size | UMR LF252–253 | LF37, 88 |
- **m6 (LF160): bind R4's new conjuncts to R3^lit's own symbols.**
  - Write {Γ ≤ 0} as 2(κ−b*)−2zQ−3(sP+sQ+C*) ≤ 0, using the definitions in UPAR2 LF98–104.
  - Write {Q predecessor weak} as t_r(S′) = −1, where S′ is the set without the P exit.
- **m7 (LF158–159): source-coverage qualification.**
  - "These FULL bodies are actually pasted" is true for UPAR LF216–275 and UPAR2 LF194–218.
  - R2's literal text, however, cites bodies outside the pasted UPAR2 ranges (LF95–123 and LF194–224):
    - UPAR2 Lemma 1, used in R2(2) for the P+ removal;
    - UPAR2 Lemma 5 and "(Z)", used in R2(4).
  - These enter only as accepted justification or under the impossible F=0 premise (LF165–166). R2(4)'s F>0 clause is itself pasted and is implied by κ > 8d+6.
  - **Fix:** append this qualification. No unreviewed premise is used.

## Observations (not promoted; no new claim)

- **O1.** The displayed (G-SW) bound is exactly 0 at κ = 26d−9 when e = w = wA = η = sQ = 0, and Γ is even. So 26d−10 is the last value that bound certifies. I do not claim such data occur in any actual frame.
- **O2.** Combining Γ ≤ 0 with the Γ bounds gives the following. Both are already the redundant tests retained at LF169, and neither replaces literal R4.
  - Both-weak R4 frames need κ ≥ 44d−22+18e+9w+18wA+9η/2+3sQ/2, by (G-WW).
  - Strong-I/weak-Q R4 frames need 2κ ≥ 52d−18+25e+12w+16wA+η+sQ, by (G-SW).

## Process and limits

- **Pre-freeze departure.** The departure recorded at scope LF56–64 is permanent and uncured, and this PASS does not cure it.
  - The route actually delivered, a charge-based uniform coefficient, belongs to the route family named in the disclosed speculation (LF60–61). This bears on provenance, not on correctness.
  - Re-derived-after-exposure governs. There is no independent-corroboration, strict-preregistration or priority claim.
- **Pins not machine-checked.** SHA256 and byte pins, and LF-numbering fidelity, were checked only by reading. The count of "16 governing bodies" (3+4+3+3+3) matches.
- **Imports not transitively re-verified.** Imports are used at their accepted literal scope. A spot-check of UPAR2 Lemma 3(b) (LF117–123) is consistent.
- **Not claimed:**
  - CHARGE-FAILURE or POSITIVE-BUDGET cover;
  - full T, another terminal k, or full ordered Olson;
  - nonemptiness of R4, or finiteness of the unbounded union;
  - novelty or priority;
  - human peer review, Lean/kernel verification, or runtime.
