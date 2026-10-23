# Hostile written review: Olson LOWER packet v1 (k = p+1, lower half)

**Basis.** I used only the pasted blocks, with no tools, computation or enumeration.

**Abbreviations.**
- **PKG**: review-package-LOWER-v1
- **PRF**: proof-LOWER-v1
- **RES**: residual-LOWER-v1
- **ERR**: erratum-1-residual
- **SCP**: LOWER-scope-v1
- **ADD**: LOWER-scope-addendum-1
- **TP**: proof-theoremP

**Errata applied.**
- ERR, at RES LF25.
- FB erratum-1. It changes no statement of Lemma FB, FB-E or ZSTRUCT as used here; R1 concerns only the ROT-FB(b) caller.

## Counts

**FATAL 0 · MAJOR 0 · MINOR 5.** MINOR-1 needs an erratum; MINOR-2 to MINOR-5 are recommended. Process observations are listed separately and not counted.

## Claim-wise verdicts

| Claim | Verdict |
|---|---|
| **Theorem K1** (PRF LF20–21, LF131–161) | **CORRECT** for every prime p ≥ 11 under the full existential-NF/word antecedent: arbitrary extra-pair placement, the empty-run rule, and no o_F or rotation-pair hypothesis. Its load-bearing inputs are all accepted interfaces used at literal scope: NF (LF28–43), the "if" direction of GRX (LF7–20), Theorem P (I re-checked it), SC0, and B0S-CJ''' (used only when W = p+1). S1(a) is not needed at κ = 1. There is no circularity: K1 uses neither Lemma C, THETA, CR nor the residual. **Not conditional.** |
| **Theorem R** (PRF LF15–17, LF26–38) | **Range clause CORRECT as a necessary range.** H ≥ 0 gives κ̂ ≤ p−1. GRX all-plus (Φ = 0, C_max = 2H, target 0, n = 0 admissible if H ≥ p) gives κ̂ ≥ 0. F ≡ k (mod 2) makes κ̂ an integer. **CJ''' sub-case clause CORRECT.** At k = p+1: Δ = −κ ≤ 0, R = p−1+2κ ≥ 4κ−4, 2κ ≤ p−3, κ ≥ 1, and the S_i are exactly the maximal constant blocks. **ρ₀ sub-case CORRECT**: (SR) at P0 with 2κ zero letters. The universal "no accepted result" clause is a search outcome, not mathematics (MINOR-5). |
| **Theorem S** (PRF LF18–19, §§2–7) | **CORRECT** relative to NF, GRX, Theorem P, S1(a), SC0, and ZSTRUCT/FB/FB-E/Setting fact. The (S′) match was checked: (k′,κ′) = (p−1,κ−1), 1 ≤ k′ ≤ p−1, 1 ≤ κ′ < p exactly when t ≥ 1, \|Y\| = 2p+2κ′−k′ = R, L ≥ 2p−k′ = p+1, t ≤ κ′, and (S1) at κ′. Subject to MINOR-2/3/4, none of which changes anything K1 uses. |
| **Lemma CR** (PRF LF163–179) | **CORRECT AS A CONDITIONAL** at the antecedent of PRF LF168 and PKG LF21: κ ≤ (p−3)/4, (H-ALT), and 2Π₀+3+ν₀ > 2p. It is **not established** at the shorter antecedent printed at PRF LF22–23 and RES LF15 (MINOR-1). (H-ALT) is unproved, so no rotation rigidity follows. |
| **RES + ERR** | After ERR, items (i)–(vi) (LF20–26) agree with the proof. The open regime is stated exactly: 2 ≤ κ̂ ≤ (p−3)/2 with rotations not all equal ({2,3,4} at p = 11). No avoider or counterexample is claimed, and MC-L1/MC-L2 are labelled as route targets. Remaining defects: LF15 overstates Lemma CR, and MC-L1 is incomplete (both MINOR-1). |

## K1 re-derivation (load-bearing steps)

1. **(SR), LF47–50.**
   - All l_i are odd, so δ_GRX = N−Φ, C_max = 2H+Φ, and 2p−2H = 2κ+2.
   - Hence the admissible n are the even n in [max(0, 2κ+2−2m), min(R, 2p−2m)].
   - The target is Σ_{i∉P} θ_i = −Σ_{i∈P} θ_i = T(P). This holds for P ≠ all runs (MINOR-3).
2. **Shapes, LF54–59.**
   - Gaps inside a block are empty, so Theorem P reads F + Σ⌊r_i/2⌋ ≥ 3p−1. With F = 3p−1−2κ this gives Σ⌊r_i/2⌋ ≤ 2κ−1.
   - At κ = 1, R = N, so u has shape (a), (b) or (c). Hence E ≤ 2 and at most one run has length 2.
   - I re-derived TP Steps 1–6: injectivity, even size, the sign c_t = (−1)^{u_t}, summation by parts with u₁ = u_{F+1} = 0, deg Q ≤ 3(p−1) < M (M ≥ 3p−2), and the box lemma. All correct.
3. **Integer form at κ = 1, LF133–135.**
   - The m = 1 window [2, p+1] covers every positive length, so Y is zero-sum-free of length p+1.
   - SC0 then gives odd a_l with W ≤ 2p−1. W is even, so W ≤ 2p−2.
   - a_max ≤ W−p ≤ p−2, so no ρ₀ letter occurs, and m1 ≥ (p+5)/2.
4. **Lemma LT, LF102–106.** Correct, using 2κ+2 ≤ R. Swapping sides is the automorphism (e,x) ↦ (e,−x) of C_2p and keeps the same b_l.
5. **K1.1, LF136–139.**
   - The other p letters include at least (p+2+a)/2 ones. At most one of them lies in P0, so C0 holds at least (p+a)/2 ≥ a ones.
   - These give a zero-sum of length a+1 in [4, p−1] at m = 0 unless a = 1. So a = 1.
   - Consequently ν₀ = δ, Π₀ = W−δ, and 2Π₀+3+ν₀ = 2W+3−δ ≥ 2p+4.
6. **K1.2, LF142–146.**
   - For m in [2, (p−1)/2] the window is [0, R], so every such pattern is full.
   - For arcs the window is [2, R]. Any even v ≠ 0 forces \|J\| ≥ 2.
   - v = 0 is realised by {+1, −1}, or by {−w} plus w ones, since (p+2+w)/2 ≥ w for w ≤ p−2.
7. **K1.3, LF147–154.**
   - The complement of G′ has at most E+2 ≤ 4 runs, so G′ has at most 4 maximal arcs. The condition 4 ≤ (p−1)/2 needs only p ≥ 9.
   - The Lemma A chain is valid: prefixes of each A_j are arcs inside G′, and partial unions have m = 2, 3 or 4.
   - Lemma U (LF112–117) re-checked: the same-parity integers of [−ν₀, 2p−1−ν₀] form a complete residue system mod p.
   - Lemma A (LF118–121) re-checked: D ∈ 2pℤ ∩ (0, 4p).
   - Inequality (K1) follows.
8. **Case δ = 0, LF155–157.**
   - \|G′\| = p−E gives W ≤ p−1+E.
   - If W = p+1, all letters equal ρ_γ, and CJ''' applies at (k,κ) = (p+1,1): R = p+1 ≥ 0, 2κ = 2 ≤ p−1, Δ = −1 ≤ 0.
   - Otherwise W ≥ p+3 > p−1+E, a contradiction.
9. **Case δ = 1, LF158–160.**
   - P0 contains only the −1 letter, so z ∉ G and \|G′\| = p−1−E ≥ p−3.
   - Each −U′ ≥ 2, and −U′ ≥ 3 on odd-length runs; at most one run has even length.
   - So the left side of (K1) is at least 3p−10, while the right side 2p−W ≤ p−1. Contradiction.

## Findings

**MINOR-1. Lemma CR's lift hypothesis is missing from two consumer-visible statements; ERR is incomplete.**
- **Where:** PRF LF22–23 (the §0 statement), RES LF15, and RES LF29–32 (MC-L1).
- **Missing premise:** 2Π₀+3+ν₀ > 2p.
  - Lemma A (LF118) needs it at the step f = 2f (LF172–173).
  - Without it, f is only constant, and the bound Σ_{J\*} θ ≤ −1−ν₀ (LF174) is unavailable.
- **What ERR does:** its replacement at RES LF25 is literal and the old span occurs once. Its remark is correct: 2Π₀+3+ν₀ ≥ 2R+3−ν₀ = 2p+1+4κ−ν₀, so the hypothesis holds when ν₀ ≤ 4κ.
- **What ERR misses:** RES LF15 and MC-L1 are untouched, and no erratum covers PRF LF22.
- **Consequence:** someone citing §0 or RES §1 would assert "(H-ALT) and κ ≤ (p−3)/4 imply one rotation pair". That is unproved. MC-L1 also understates what a rigidity route still needs.
- **Repair (erratum-2, no claim added):**
  - Add "and 2Π₀+3+ν₀ > 2p" at PRF LF22.
  - Add the same at RES LF15.
  - Append to MC-L1: "prove 2Π₀+3+ν₀ > 2p (e.g. ν₀ ≤ 4κ) or avoid Lemma A".

**MINOR-2. The definition of θ_i can be empty (PRF LF126, LF129).**
- **Step:** if h_i ≡ 0 (mod p) and r_i is odd, no integer in (−p, p) has both required congruences. The claim that "the two integers have different parities" is false when h_i ≡ 0.
- **Consequence:** none for K1. Lemma THETA itself is correct: under its hypothesis |d| < p, so h_i ≡ 0 forces d = 0, hence σ({i}) is even and θ_i = d exists.
- **For Lemma CR:** θ_i is needed for every i ∈ S, and it exists. Since \|S\|−1 ≥ 2κ+1, there is a J ⊆ S∖{i} of size κ+1, and J and J∪{i} are both full under (H-ALT).
- **Repair:** define θ_i only where it exists, and add that one sentence.

**MINOR-3. m(P) is ambiguous for P = all runs (PRF LF45–47).**
- **Step:**
  - For P = all runs, z ≡ −1 has Φ = 0, so GRX gives the window [2κ+2, min(R, 2p)].
  - If m(all) = 1, the stated (SR) would also forbid 0 ∈ Σ_{2κ}(−X), which GRX does not imply.
- **Consequence:** none. This case is never used; every use has P = ∅, a proper arc, G′, unions of at most 4 arcs inside a proper G′, or S_ev/S_od.
- **Repair:** set m(all) := 0, or restrict (SR) to P ≠ all runs (P = all is equivalent to P = ∅).

**MINOR-4. Two one-line justifications are omitted.**
- **(a) Lemma IF bounds at t = 0 (LF66 with LF75).** For t = 0 and κ ≥ 2, the bounds a_i ≤ p−2 and m1 ≥ 2p+2−W are stated but derived only for t ≥ 1. Both are elementary:
  - a_max ≤ W−(L−1) ≤ p−1, and a_max is odd, so a_max ≤ p−2.
  - m1 − (2p−1−W) ≥ 2L−2p+1+h ≥ 3, using W ≥ m1+3h.
- **(b) Lemma C uniqueness (LF124–125).** "No other number of that class" needs the interval length 4p−4−2B\* to be below 2p. That holds because B\* ≥ R ≥ p+1.
- **Consequence:** none.
- **Repair:** insert the lines.

**MINOR-5. Theorem R wording and coverage (PRF LF15–17, LF28–33; compare LF7, LF185, PKG LF6, and the import table LF188–197).**
- **(a) Range wording.** "Admissible values 0..p−1" is a necessary range, not an attainment claim. For example, κ̂ = 0 at k = p+1 gives F = 3p−1, which Theorem P rules out.
- **(b) Unqualified negative.** "No accepted result excludes a whole lower-half cell" is labelled "[from pins]" but is a search outcome. PKG LF16 and RES LF9–10 qualify it correctly.
- **(c) KP3/KP4 status.** They are cited as accepted, via verdict hashes not in the import table, SCP or ADD. PRF LF7, LF185 and PKG LF6 call the same texts unreviewed non-premises. PP1 and KP2 are not pinned either.
- **Consequence:** none for K1, S or CR, since all of these concern κ̂ ≥ (p−1)/2. However, Theorem R's coverage clause cannot be accepted as mathematics.
- **Repair:** rephrase (b) as in RES LF9–10; read (a) as a range of possible values; pin or drop KP3/KP4 and reconcile LF7/LF185.

## Process, completeness, priority, computation

**Addendum timing (verified).** Timestamps run in order:

| File | Time (after /bin/date) |
|---|---|
| SCP | 21:17:19 |
| ADD | 22:05:02 |
| PRF | 22:07:01 |
| RES | 22:08:56 |
| ERR | 22:09:10 |
| PKG | 22:10:16 |

- "Added before first frozen use" holds, and the target and antecedent are unchanged (ADD LF4–7 against SCP LF12–19).
- **Deviation:** ADD LF6–7 discloses that Theorem P and ZSTRUCT/FB/FB-E/Setting fact were consulted during the post-freeze derivation before being listed. So the input list was amended mid-derivation rather than frozen beforehand.
- SC0 was already covered by "Savchev-Chen" (SCP LF32).
- This has no mathematical consequence. The parent should log the deviation.
- Checkpoints 001–004 are not in this excerpt set, so their ≤1800 s spacing is unverifiable here.

**Dependency checks.**
- **Theorem P.** TP LF3–5 says "NOT yet independently reviewed". The only acceptance record is the import list in the K0\* verdict, LF7. I re-derived the pasted proof and found it correct (the brute-force remark plays no role), so this load-bearing K1 dependency is discharged.
- **SC0.** Its literal statement is consistent with the recorded primary statement. Append −σ(Y′) to get a minimal zero-sum of length ≥ p+2. Its basis element must have order 2p, and dropping the appended term leaves a coefficient sum ≤ 2p−1.
- **S1(a).** The excerpt does not name its sequence class, but no premise is missing. The implication holds for any sequence of odd elements when κ′ ≤ (p−1)/2:
  - Split a zero-sum into minimal zero-sums; each has length ≤ 2κ′ by (ZP) and D(C_2p) = 2p.
  - The first cumulative length ≥ 2κ′+2 is then ≤ 4κ′ ≤ 2p−2, contradicting (ZP).
  - S1(a) is not used at κ = 1.

**Not counted (optional fixes).**
- RES F5: "n(S)" is undefined.
- RES F6: taken literally, "no zero alternating sum at all" is false for arcs, because y₀ ≡ y_p gives T({0}) = 0. The intended reading is presumably patterns with m ≥ 2. The failed-route notes are not claims.
- Notation reuse: u (the word, the count of ones, and a shifted value), H (number of extra pairs and H(P)), k (terminal block count and number of arcs), r, w, E.

**Completeness.** The packet is a correctly labelled partial: only the κ̂ = 1 cell is closed, and 2 ≤ κ̂ ≤ (p−3)/2 remains open.

**Computation.** None is used as a premise.

**Priority/novelty.** Not assessed; the "[NEW]" tags are provenance labels only.

## Not approved

This review approves only Theorem K1, the exclusion of the single cell κ̂ = 1 at k = p+1. It does not cover:
- any other lower-half cell;
- rotation rigidity without (H-ALT) and the lift hypothesis;
- UH, bottom or KP cells;
- INV\*, REFL, or lower-half or full ordered Olson;
- the research target or runtime.

All repairs are errata only; K1 needs no re-proof.
