# Hostile written review: Theorem FCW (`proof-FCW-v1.md`, `c23fd037…`)

This review uses only the frozen pasted text. I used no tools, files, code or numerical enumeration, and I checked every case by hand.

**Abbreviations.**
- FCW = proof-FCW-v1.md
- SCOPE = FCW-scope-v1.md
- PKG = review-package-FCW-v1.md
- TJ = transition JSON
- PL = proof-LOWER-v1.md (LF40–129)
- LE = LOWER parent erratum
- K1V = K1 verdict
- ROT = proof-ROT-few-E-v4.md (LF28–43)
- GRX = notes-GRX-v1.md (LF7–20)
- S1V = zx-s1c verdict LF19
- SC0 = index-one record
- FBV = FB verdict
- FBP = proof-FB-v1.md (LF9–24)
- BFV = balfull verdict (LF26–34)
- K3V / K3E = K3 verdict / K3 erratum

## Counts

| Severity | Count |
|---|---|
| FATAL | **0** |
| MAJOR | **0** |
| MINOR | **4**: 2 editorial, 1 import-instantiation completeness, 1 provenance |
| Process notes (not mathematical) | 2 |

**Correctness verdict.** I found no mathematical flaw. Every load-bearing step re-derives from these literal interfaces:
- NF (ROT LF37–42)
- GRX if-direction (GRX LF18–19)
- SC0 (SC0 LF9–11), through a one-line reduction that the proof does not write out (MINOR-3)
- ZSTRUCT/FB in (S′) (FBP LF16–19; FBV LF9; BFV LF33)

Theorem FCW is correct as written relative to those accepted imports. None of the following is a premise: any USK, K3 or P11R lemma, S1(a), the Setting fact, FB-E, Theorem P, CJ‴, K3-11, or PL D/U/A/C/THETA. No load-bearing dependency is left unresolved.

---

## Claim-wise verdicts

### Setup and (SR), FCW LF30–41: CORRECT

**Parameters.**
- N = 4κ, R = 6κ−2, F = 10κ−4, H = 3κ−2, 2p = 8κ−2.
- R + F = 16κ−6 = 4p−2.
- R ≤ 2p−2 holds iff κ ≥ 1.

**(SR), re-derived by me directly from GRX LF14–19 and ROT LF37–42, not from the K1 label.**
- Every l_i is odd, so δ = N − Φ and C_max = F − δ = 2H + 2m(P).
- Hence n = 2p − C ranges over [2κ+2−2m, 2p−2m] ∩ [0, R], because 2p − 2H = 2κ+2.
- The GRX target is Σ_{z_i=+1}(y_{i−1} − y_i) = −Σ_{i∉P} τ_i = T(P), using Στ_i = 0.
- GRX LF12–13 ("maximal or not") covers equal adjacent blocks separated by nonempty runs.
- The placement of extra pairs enters only through H.
- The LE item-3 convention, m = Φ/2, is exactly the GRX count.

### Lemma W, LF43–46: CORRECT

- W_κ = [max(0, 2), min(R, 6κ−2)] = [2, R].
- W_{κ+1} = [0, 6κ−4] = [0, R−2].
- Part (d) is monotonicity and is not load-bearing.

### Lemma IF*, LF48–68: CORRECT

**(a)** Pigeonhole on p+1 block values in Z_p gives an arc P0 with T(P0) = 0, so m(P0) = 1.

**(b)** This is direct and does not use S1(a).
- |Y| = R < 2p, so every zero-sum has even length ≤ R.
- W_1 = [2κ, R] removes every length ≥ 2κ, so the maximum is 2κ−2.
- This is the same move as K3E item 2.

**(c)** Y′ is zero-sum free, otherwise Z would extend. L ≥ 6κ−2−2(κ−1) = 4κ = p+1. For SC0, see MINOR-3.

**(d)** The (S′) hypotheses hold at (k′, κ′) = (p−1, κ−1):
- 2p + 2κ′ − k′ = p + 2κ − 1 = R
- 1 ≤ κ′ < p
- (S1) at κ′ is exactly (b)
- t ≤ κ′
- L ≥ 2p − k′ = p+1

The outputs used are: the shape of Z, odd s_j ≥ 1, n₊ + n₋ = 2t, n₋ ≥ 1, Σs_j = n₊, and W + n₊ ≤ 2p−1. From these:
- n₋ ≤ n₊ and n₋ ≤ t.
- s_j ≤ n₊ − (n₋ − 1) = 2t − 2n₋ + 1 ≤ 2κ−3.

**(f)**
- E = W − L ≤ (2p−1−n₊) − (R−n₊−n₋) = 2κ−1+n₋ ≤ 3κ−2.
- Hence a_i ≤ 3κ−1.
- m1 ≥ L − E/2 ≥ (10κ−3−5t)/2, which is at least (5κ+2)/2 at t = κ−1.

### Normalisation, light side and quantities, LF69–82: CORRECT

- Scaling by γ⁻¹ preserves the run/block structure, (SR) and the empty-run rule.
- **LT:** (SR) at ∅ with n = 2κ+2 ∈ W_0, since 2κ+2 ≤ 6κ−2.
- **Exchange of sides:**
  - The sequence of C0 is −Y, because −(1, x) = (1, −x).
  - −Z is a longest zero-sum of −Y, and −g is an index-<1 generator with the same coefficients.
  - Coefficients relative to a generator are unique, so n±, the s_j and every b_l are unchanged.
  - Re-normalising afterwards is correct.
- B* = W + 2n₊ = R + E + n₊ − n₋, and B* is even.

### Lemma D*, LF84–90: CORRECT

- s_j ≤ 2κ−3 ≤ m1+1.
- a_max − 1 ≤ E − 2(r−1) ≤ m1 is equivalent to E ≤ L + r − 2. This holds because E ≤ 3κ−2 ≤ 4κ−1 ≤ L + r − 2.
- The prefix sums step by at most m1+1 ≤ u1+1, so they cover [0, B*].
- B* − R = E + (n₊ − n₋) ≥ 0, with equality iff every |c_l| = 1.

### Lemma SS, LF91–95: CORRECT

- It is instantiated through D*, not PL Lemma D. This is the same routing as USK erratum v2.
- From Π(P) + ν(P) = B* and Π(P) − ν(P) = (Π0 − ν0) − 2σ(P), the stated formulas follow.

### Lemma N, LF99–108: CORRECT

**The type split is exhaustive.**
- In P0: b = 1 is type (i); an a-label ≥ 3 is type (ii); b = −s_j is positive.
- In C0: b > 0 is positive; b = −s_j is type (iii).

**The bounds.**
- B ≤ (3/2)(B−1) for B ≥ 3.
- Σ(B_k − 1) ≤ E, since the type-(ii) letters have distinct a-indices.
- Σ_(iii) s_j ≤ n₊.

**The margin.** 2Π0 + ν0 − 2p = 2B* − ν0 − 2p ≥ 4κ−2 + E/2 + n₊ − 2n₋ − q1. Using q1 ≤ κ, then n₊ ≥ n₋, then n₋ ≤ κ−1, this is at least 2κ−1 + E/2.

### Lemma Z, LF115–122: CORRECT

This is the case where O1 has only one sign. The opposite-sign letter has |c| = b ≥ 3.
- If b is an s-label: b ≤ 2κ−3 ≤ m1.
- If b is an a-label: m1 ≥ L − 1 − (E−b+1)/2 ≥ (10κ−6−5t+b)/2 ≥ (5κ−1+b)/2 ≥ b, because b ≤ 3κ−1.

For κ ≤ 4 the crude bound already suffices. The refined count is genuinely needed for κ ≥ 5, and it is supplied.

### Lemma U*, LF124–157: CORRECT, including single-signed patterns

**Step 1(i), two-signed patterns.**
- A minimal J contains no nonempty signed zero-subset. So J is not the set of all letters, which contains Z0.
- Hence |J| ≤ R−1, and by parity |J| ≤ R−2.
- If v ≠ 0, then |J| ≥ 2.
- If v = 0: use Z0 when m = κ, and J = ∅ when m = κ+1. The latter is legitimate because n = 0 gives C = 2p ≤ C_max = 2κ + 2 + 2H = 2p.

**Step 1(ii)/(iii), single-signed patterns.**
- v = 0 at (ii, m = κ) and v = B* at (ii, m = κ+1) are genuinely unrealisable: all values are positive, and only J = all letters sums to B*.
- So the one-unit shift is real, not an artefact.
- Every other even value is realised.

**Step 2.** σ(P) = −ν0 in case (ii) and Π0 in case (iii). The translated intervals are as stated, and b − a ≥ B* − 2.

**Step 3.**
- The complete residue system a, …, a+2p−2 forces b ≤ a+2p−4, so B* ≤ 2p−2.
- The representative lies in [b+2, a+2p−2], and the sub-interval containments are as stated.
- [Π0, 2p−ν0] contains 2p−B*+1 < 2p integers. Since p is odd, the residue mod 2p is unique.

**The "in particular" clause.** The case split is exhaustive, because every |c_l| ≥ 1. Cases (ii) and (iii) are mutually exclusive, because letters(P) and letters(P^c) are disjoint and R > 0.

### Lemma A*, LF158–161: CORRECT, and the margin absorbs the extra unit

- Δ ≡ 0 (mod 2p).
- Δ ≥ 2Π0 − (2p − ν0) ≥ 2κ−1 > 0.
- Δ ≤ 4p − 2ν0 − Π0 < 4p.
- Therefore Δ = 2p.

PL Lemma A (PL LF118–121) needed 2Π0 + 3 + ν0 > 2p for the window [Π0+1, 2p−1−ν0]. The wider common window costs exactly 3 in the lower bound for Δ. Lemma N leaves a margin of 2κ−1 ≥ 5, so the extra unit is absorbed with room to spare.

### Lemma C*, LF162–165: CORRECT

- [2Π0, 4p−2ν0] contains Π0 − ν0 + 2p, because B* ≤ 2p.
- It excludes Π0 − ν0 and Π0 − ν0 + 4p, because B* > 0.

### Lemma F, LF169–206: CORRECT

**(F1)**
- The separators are 2κ−1 and 2κ−2. Also i−1 ∉ Q_i, since 4κ−1 > 2κ+1.
- |d| ≤ 2p − B* ≤ 2κ, and |d − d′| ≤ 4κ < 8κ−2.
- So d = θ_i for every pair P, P∪{i} in C.
- θ_i is defined without fullness. This is compatible with LE item 2, which restricts PL's THETA; PL's THETA is not imported.

**(F2)**
- (a) Removing an endpoint of a maximal interval of length ≥ 2 preserves m.
- (b) The added run is non-adjacent to v_j, at distance g_j ≥ 2. After the deletion, the new run is at distance g_{j+1}+2 from v_{j+2}.
- (c) Each chain of moves lowers Σ_{j≤κ} g_j by one, and the process ends at gaps (1, …, 1, 2κ−1).
- (d) The gap ahead at each move is G, then 2, …, 2.

**(F3)** The wrap separators are κ−1 for P1, κ−1 for P2, and κ−2 ≥ 1 for P1∪P2. This is the only place where κ ≥ 3 is used.

**(F4)** 3κ runs lie in κ gaps, so some gap is ≥ 3, and x = j+2 is independent of J. The wording has a minor issue; see MINOR-2.

**(F5)** Q0^c has κ+1 maximal intervals.

### Section 5, LF210–230: CORRECT

**Set-up.** J_S ⊂ S is independent with m = κ, and Θ(J_S) = U′(J_S) by (F4).

**Case letters(J_S) ≠ A⁻.** U′ ≤ −1−ν0, so θ_(κ) ≤ −1, so Σ_S ≤ −1−ν0−κ.

**Case letters(J_S) = A⁻ and ν0 ≥ 1.** U′ ≤ −ν0, so Σ_S ≤ −ν0−κ.

**Case letters(J_S) = A⁻ and ν0 = 0.**
- A⁻ = ∅, so every run of J_S is empty.
- θ_e ≡ τ_e ≢ 0 (mod p) by the empty-run rule (ROT LF38).
- θ_e is even (σ_e = 0), and |θ_e| ≤ 2κ < p. So θ_e is a nonzero even integer.
- θ_(κ) is carried by a run of J_S. If θ_(κ) > 0, then Θ(J_S) ≥ 2κ > 0 = −ν0, which is impossible.
- So θ_(κ) ≤ −2, and Σ_S ≤ −2κ ≤ −1−κ.

**Exception in at most one set.** If both sets were exceptional, A⁻ would lie in letters(J_ev) ∩ letters(J_od) = ∅, forcing ν0 = 0. That contradicts the exception's requirement ν0 ≥ 1.

**Final contradiction.**
- Π0 − ν0 − 2p = Θ(all) ≤ −1 − 2ν0 − 2κ.
- Hence B* ≤ 6κ−3 = R−1.
- This contradicts B* ≥ R.

The "which inputs carry the weight" paragraph (LF231–233) is accurate.

### Section 6 instances, LF237–253: CORRECT

These are instantiations of the general proof, not independent checks.

**(3, 11)**
- Windows: [8,16], [6,16], [4,16], [2,16], [0,14], [0,12], [0,10].
- Frame bounds: t ≤ 2, L ≥ 12, s_j ≤ 3, E ≤ 7, a_i ≤ 8, m1 ≥ 9.
- Lift margin ≥ 5; B* ≤ 20; |θ| ≤ 6; |d−d′| ≤ 12 < 22.
- Explicit sets: Q_i, gaps (1,1,1,5), P1∪P2 separated by runs 2, 5, 8, 11, and Q0^c.
- Conclusion: B* ≤ 15 < 16 = R.

**(5, 19)**
- Windows: W₅ = [2,28], W₆ = [0,26], W₀ = [12,28].
- Frame bounds: t ≤ 4, E ≤ 9+n₋, a_i ≤ 14, m1 ≥ 14.
- Lift margin ≥ 9; the wrap separators 17, 18, 19 are κ−2 = 3 runs.
- Conclusion: B* ≤ 27 < 28 = R.

### The H11-failing branch of K3-11, LF249–250: COVERED

- Per K3V LF7 and K3E item 1, K3-11 needs (H11) in some admissible frame. The residual is an avoider that fails (H11) in every frame.
- FCW runs in an arbitrary admissible frame (P0, longest Z, index-<1 g, light side; LF81–82).
- It never inspects whether a run mixes signs or how many runs lack a positive label.
- So it excludes every avoider with a qualifying NF at p = 11, whatever (H11) does. K3-11 is not cited.

### Theorem FCW, LF14–19: CORRECT relative to the accepted imports

It is not conditional on any unaccepted lemma.

---

## Findings

**MINOR-1. Symbol overloading (editorial). FCW LF32, LF41–46, LF56, LF80, LF112, LF170, LF232.**
- **What:**
  - F means both the reflection count (LF32) and the family {m(P) = κ+1} (LF170, (F1)–(F5)).
  - H means both the extra-pair count (LF17, LF32, LF232) and H(P) (LF80).
  - W means both the windows W_m (LF41–46) and Σa_i (LF56).
  - C means both the family (LF112) and the C0 arc and C_max.
- **Consequence:** None mathematical. Each use resolves from context; for example, the H in LF232 is 3κ−2.
- **Repair:** In an erratum, rename the families (for example 𝒞, 𝓕) and the windows (for example Win_m). No statement changes.

**MINOR-2. Wording in (F4) (editorial). FCW LF200–201.**
- **What:** "x := j+2 is adjacent to neither end of the gap" is true only if "ends" means the two runs of J that bound the gap. x is adjacent to j+1, which is the first run inside the gap.
- **Consequence:** None.
- **Repair:** "x is at distance 2 from j and g−1 ≥ 2 from the next run of J; both its neighbours j+1 and j+3 lie in the gap, since g ≥ 3."

**MINOR-3. The SC0 instantiation is not written out (completeness). FCW LF55–57; table LF293.**
- **What:** The literal SC0 record (SC0 LF9–11) is a statement about minimal zero-sum sequences of length ≥ ⌊n/2⌋+2. IF*(c) asserts directly that an index-<1 g exists and that "g generates C_(2p)".
- **My re-derivation of the reduction:**
  1. σ(Y′) ≠ 0, so Y′·(−σ(Y′)) is a minimal zero-sum sequence of length L+1 ≥ p+2 = ⌊2p/2⌋+2 over C_{2p}, with 2p ≥ 3. So it has a 1-element basis {g}.
  2. Every term is odd and lies in ⟨g⟩, so ord g is 2 or 2p.
  3. If ord g = 2, every term is (1,0), and two of them (L ≥ 2) form a zero-sum in Y′. That is impossible, so ord g = 2p.
  4. The least coefficients then sum to 2p, and the appended term's coefficient is ≥ 1, so W ≤ 2p−1.
- **Consequence:** None. The import is used within its scope.
- **Repair:** Insert these lines in an erratum, or cite the recorded index-<1 interface explicitly as the derived form.

**MINOR-4. Provenance paraphrase. FCW LF28, LF287; SCOPE LF29–31.**
- **What:** FCW credits K1V with accepting "PL Secs. 2–7 relative to their inputs". The pasted K1V LF5 accepts Theorem K1, Theorem R (as a range), Theorem S structure and CR (conditionally), and lists imports. It does not enumerate PL sections.
- **Consequence:** None. Every PL item FCW uses is re-derived:
  - IF(a), the normalisation, the SS bijection and LT are re-derived in FCW.
  - (SR) is re-derived above from GRX and ROT.
- **Repair:** Cite (SR) as "GRX if-direction applied to the NF word (instantiation PL LF48–50)", and cite K1V as context only.

---

## Import and scope audit

| Import | Use in FCW | At scope? |
|---|---|---|
| NF (ROT LF37–42) | Avoider u; k = p+1 odd blocks; R formula; empty-run rule, used only in the Sec. 5 case ν0 = 0 | ✓ |
| GRX if-direction (LF18–19, LF12–13) | Only through (SR), as the contrapositive for u | ✓ |
| (S1) definition (S1V LF19) | Hypothesis of (S′) at κ′ = κ−1 | ✓ Definition only; S1(a) unused |
| SC0 | Existence of g in IF*(c) | ✓ n = 2p, length ≥ p+2 (MINOR-3) |
| ZSTRUCT and FB in (S′) (FBP LF16–19, FBV LF9, BFV LF33) | Shape of Z, n₋ ≥ 1, balance, W + n₊ ≤ 2p−1 | ✓ At (p−1, κ−1), only when t ≥ 1 |
| FB-E, Setting fact, Theorem P, CJ‴, K3-11 | Not used | ✓ The bounds a_i ≤ 3κ−1 and s_j ≤ 2κ−3 are derived locally; the all-equal case needs no split |
| PL D/U/A/C/THETA | Not used; replaced by D*, U*, A*, C*, (F1) | ✓ |
| USK, K3, P11R | Context only; no lemma is silently a premise | ✓ Q_i is the step-two form required by USK erratum v1 |

**Errata applied.**
- **LE:** the m-convention is used; the θ restriction does not bite because PL THETA is not imported; CR is not used.
- **K3E items 1–3:** FCW's argument holds in every frame, so it covers the frames K3-11 leaves open. IF*(b) uses the same direct zero-sum bound as item 2.
- **USK errata v1/v2:** these are context only, and FCW already matches them.
- **FB erratum 1:** no statement change.

None of these errata changes any verdict above.

---

## Process, computation and priority (separate from correctness)

- **P-1 (process). PKG LF6–7 against SCOPE LF9–12 and TJ LF32.**
  - The package discloses a "drafting helper [that] checked that each wording replacement matched exactly once".
  - The frozen rules allow only clock, hash, byte and LF metadata operations.
  - The parent should decide whether this helper counts as text drafting. The parent should also confirm it acted only on drafts before exclusive file creation (SCOPE LF9).
  - There is no mathematical consequence: every step above was hand-checked.
- **P-2 (process, disclosed and not a defect).**
  - SCOPE LF34–36 and LF72–77 planned to import PL's U/A/C and to use a fullness-based route.
  - FCW instead proves U*/A*/C* afresh and drops PL U/A/C/THETA (LF289, LF296), disclosing the change at LF266–271.
  - This narrows the imports and does not expand scope.
- **Computation.** I performed none, and FCW relies on none.
- **Priority.** I read the "[NEW]" tags only as "proved in this packet". I make and assess no novelty, priority, "first", Lean or human-referee claim.

## What this verdict does not conclude

- It does not approve the research target, any runtime, or full ordered Olson.
- It does not cover any other cell: p ≠ 4κ−1, κ_hat = 0, or p = 7.
- The route remarks (LF257–274) are not claims. I did check (R2) in passing: sorting the top κ+1 runs gives only B* ≤ R.
