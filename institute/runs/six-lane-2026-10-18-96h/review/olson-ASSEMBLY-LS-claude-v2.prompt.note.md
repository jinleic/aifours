# Hostile review: ASSEMBLY-LS v2 (`ac854c31…`), with parent erratum v1 applied afterwards

I read proof lines 1–263, the scope, and every supplied verdict and source range. Erratum v1 was applied last. Shorthand: `proof:N` means `proof-ASSEMBLY-LS-v2.md:N`.

I compared the table's hashes against the excerpt headers as strings only, and all match. I did not recompute any hash. I inferred no acceptance from the author's table, the package, the erratum, or prior reviews.

## Verdicts (prime p ≥ 7)

| Item | Verdict | FATAL / MAJOR / required MINOR |
|---|---|---|
| Proposition ROT-LS | **ACCEPT-WITH-FIXES** | 0 / 0 / 1 (N1, trust label) |
| Theorem (A) | **ACCEPT** | 0 / 0 / 0 |
| Theorem (B) | **ACCEPT** | 0 / 0 / 0 |
| Erratum v1 (E1, E2) | Correct, residual-only, no effect on the rows above | n/a |

- **Basis:** all three hold relative to the cited parent-accepted interfaces at their original scopes and overlays.
- **Lev condition:** as universal statements they are conditional on Lev for p ≥ 11. `proof:8-10` declares this for the theorem; N1 asks that the same tag be attached to ROT-LS.

## 1. Normal form (row NF)

- **Existence and termination.** The source asserts a terminal w^ (fewE-v4:37). The block-count measure at `proof:52-53` is the author's addition and is harmless (O3).
- **Invariants.** PM* preserves avoidance from original to reduced (lowodd:8). Length and rotation multiset are preserved (fewE-v4:37), so F is preserved. Fusion only re-reads the representation; the word does not change.
- **Bounds on k.** 1 ≤ k ≤ o_F and k ≡ o_F (mod 2):
  - A PM* step keeps the odd count. A fusion step lowers it by 0 or 2.
  - A terminal form with at least two blocks has all blocks odd, since otherwise PM* still applies.
  - A single even block is impossible: K1 forces F = 2p−1, which is odd (lowodd:9, M4 at :32).
  - Hence **no avoider has o_F = 0.**
- **Quantifiers.** ROT-LS is existential. (A) covers every normal form, because every normal form has k ≤ o_F ≤ p−1 (`proof:149-150`). This matches ZX overlay 2 (zx:52).
- **Empty runs.** Empty runs are allowed in every row that sees w^: GRX (lowodd:7), PM* and K1 (M1, :29), DAV, and K01/FB via SHgen-E.
- **Arithmetic in 1.4.** R = 2p+2κ̂−k and κ̂ = κ(w) − (o_F−k)/2 both check.

## 2. GRX and DAV

**GRX, all-plus pattern.**
- f ≡ 0 and Φ = 0. δ = k because every block is odd. C_max = 2Ĥ. T = Σθ = 0 by telescoping.
- If Ĥ ≥ p, then C = 2p with the empty rotation selection qualifies, so an avoider has κ̂ ≥ 0.
- For even m in [2κ̂+2, 2p], C = 2p−m lies in [0, 2Ĥ] automatically. Lengths m > R are vacuous.
- This is exactly the sequence condition (ZP_κ̂).

**DAV, re-derived independently.**
- Take Ĥ disjoint pairs from alternate interior gaps. Pairs in different blocks stay disjoint even across empty runs.
- A boundary-gap frame exists in every cyclic representation, empty runs included.
- D(C_p ⊕ C_2p) = 3p−1, and a zero-sum item set has size in 2pℤ ∩ [1, 4p−2], so its size is exactly 2p.
- R + Ĥ = 3p−1+κ̂−k ≤ 3p−2 gives κ̂ ≤ k−1.
- N = 4p−2 lies inside RUNS m4's stated N ≤ 4p−1 (runs:57). The phrase there "load-bearing N = 4p−1" is an observation, not a restriction.

**DAV authority path: adequate.**
- The decisive in-scope instance is fewE-v4:42–43: the empty-run normal form with a boundary-gap frame. It is accepted through fewodd addendum:12.
- It is backed by ZX overlay 3 (zx:53) and the import lists at zx:55, rotkp:59 and k01:63.
- o3-v4 is correctly demoted to a written instance.
- SHgen-v3:34–36 says the frame "exists because runs are nonempty", which would not cover an empty-run w^. The GRX row correctly cites only lines 28–33 and 37.

## 3. LS step

- **Threshold.** |Y| − (p+2κ̂+1) = p−1−k, which is ≥ 0 iff k ≤ p−1. Equality holds at k = p−1.
- **Domain.** The LS definition (LS-scope:10–12) and LS-ALL (G-LS verdict item 2, :10) agree: prime p ≥ 5, integer 0 ≤ κ ≤ p−2, odd Y in C_2p. Here κ̂ is integral with 0 ≤ κ̂ ≤ k−1 ≤ p−2.
- **Blocks used:**
  - κ̂ ≤ ⌊2p/3⌋: S1-sharp, with no length hypothesis.
  - ⌊2p/3⌋+1 ≤ κ̂ ≤ p−3: G-LS with e ≥ 3, conditional on Lev. This range is nonempty iff p ≥ 11.
  - κ̂ = p−2: forces k = p−1, so e = 2 and no Lev input.
  - At p = 7: ⌊14/3⌋+1 = 5 = p−2, so no Lev cell exists.
- **Lev enters nowhere else.**
  - K01 gets (S1) from S1+.
  - FB(a) takes (S1) as a hypothesis.
  - NF, REFL and RGR predate G-LS.

## 4. Routing and ROT-FB(a) hidden hypotheses

**Routing.**
- k = 1 goes to K1: c ≠ 0 and F = R = 2p−1.
- κ̂ = 0 with 2 ≤ k ≤ p−1 goes to K01 (k01:18).
- κ̂ ≥ 1 goes to FB(a) (fb:11–12).
- The cases are exhaustive because κ̂ ≥ 0.

**Constraints found in the ROT-FB proof body (fb-proof:86–106):**
- (S′) needs L = R−2t ≥ 2p−k ≥ p+1. This uses t ≤ κ̂ from (S1) and needs k ≤ p−1.
- (H) needs E ≤ 2k−2−2κ̂ ≤ 2Ĥ, which needs k ≤ p.
- (K) needs η+a_max ≤ k ≤ 2p−1−k, which needs k ≤ p−1.
- The SHgen-E caller condition o_F(u°) ≤ k ≤ p is discharged inside the accepted FB. This is the caller obligation in refl:16, which FB's own verdict judges.

**Absent constraints.**
- There is no 3k ≤ 2p+1 condition.
- There is no 2κ̂+k ≤ 2p condition; that was ZB+'s (fb-proof:129).
- There is no condition on F or on o_F(w).
- (S′)'s requirement 1 ≤ κ < p is met by 1 ≤ κ̂ ≤ k−1.

## 5. Theorem (A)

REFL (refl:6) is applied to the original w:
- (i) the rotation pair comes from ROT-LS through the rotation multiset;
- (ii) w avoids;
- (iii) o_F(w) ≤ p−1 ≤ p, computed on w's maximal decomposition, not on w^.

Condition (i) is never vacuous: R ≥ p+1 when k ≥ 2, and R = 2p−1 when k = 1.

## 6. Theorem (B): ledger re-derived independently

**Domain.**
- B = p−1 ≤ 2p−3.
- The caller obligations are met: o ≤ 2p−3, no even-block deletion, and the shorter-word class is preserved (zx:58; k01:59, m10).
- The bound B = p−1 is already an accepted instance (k01:38, FB Corollary (b)). Those instances carry F side conditions that the ledger's mechanics never use. So the ledger is used **in domain**.

**Case 1 (R ≤ 2).**
- F − o_F ≥ 3p−2 ≥ 2p.
- Σ⌊l_i/2⌋ = (F−o_F)/2 ≥ p disjoint adjacent equal pairs.
- The frame starts at a rotation (R ≥ 1) or at a change of reflection value (R = 0). The R = 0 constant word is handled separately by σ_y^{2p} = 1.
- Pulling back from the cyclic frame: AB = 1 iff BA = 1.

**Case 2 (an odd block of length ≥ 3).**
- After deleting one letter the block has length l−1 ≥ 2, so it stays nonempty and nothing fuses.
- o_F drops by exactly 1.
- Reconstructing w from w' is valid.

**Case 3 (R ≥ 3).**
- o_F(w_i) is either o_F or o_F−2. A rotation run empties only if it held exactly one rotation. In that case another run is nonempty, so two distinct maximal runs merge linearly, and their meeting blocks fuse only if their values are equal.
- The third rotation x3 lies in both deletions, so its value is t = ±c1 ≠ 0. This forces {±c1} = {±t} = {±c2}.
- Every rotation is covered: x1 lies in w_2 and x2 lies in w_1.
- Cyclic adjacency, including the wrap-around pair, survives deleting a rotation.

**Ordering.**
- RGR-LONG's conclusion is already stated in increasing original index order (runs:7).
- Only Case 1 needs the conjugation step.
- If F = 0 at length 4p−1, the Case 3 deletions cannot be avoiders by 1.3, which is consistent.

## 7. Endpoints

| Endpoint | Outcome |
|---|---|
| o_F = 0 | No avoider (terminal even block, K1 parity) |
| F = 0 | Not an avoider at length 4p−2 (EGZ twice, since 4p−2 ≥ 3p−1) |
| R ≤ 2 / R = 0 | Case 1 |
| k = 1 | K1, rotations c^{2p−1}, c ≠ 0 |
| k = 2 | κ̂ ∈ {0, 1}: K01, or FB(a) with S1-sharp |
| k = p−1 | Length meets the threshold with equality; κ̂ ≤ p−2 |
| κ̂ = ⌊2p/3⌋ | S1-sharp |
| κ̂ = ⌊2p/3⌋+1 | G-LS: e = 2 at p = 7, e = 3 (Lev) at p = 11 |
| κ̂ = p−2 | Forces k = p−1; e = 2, Lev-free |
| p = 7, cell (o_F, F) = (6, 8) | Every normal form has k = 6, κ̂ = 5 (k = 4 would give κ̂ = 4 > 3; k = 2 would give 3 > 1). Lev-free |
| p = 11, cell (9, 13) | Only k = 9, κ̂ = 8: Lev |
| p = 11, cell (10, 14) | k = 10, κ̂ = 8 (Lev), or k = 8, κ̂ = 7 (S1-sharp) |
| p = 11, cell (10, 12) | Only k = 10, κ̂ = 9: Lev-free |

The p = 11 cells show that the Lev dependence of the universal statement is real.

## 8. Findings

### N1 (MINOR, required): trust labelling of ROT-LS

- **Where:** `proof:24-26` states ROT-LS with no Lev qualifier. `proof:8-10` attaches the condition only to "the theorem".
- **Why it matters:** ROT-LS is Lev's only entry point (`proof:121-123`). It has no o_F hypothesis by design, and it is reused outside (A)'s scope at `proof:215-217` and `proof:240`.
- **Instance:**
  - Take p = 11, o_F = 11, and a normal form with k = 9, κ̂ = 8 (so F = 13, R = 29 ≥ 28).
  - The 7.1 bullet's INV* conclusion for such a word rests on Lev with e = 3.
  - Yet `proof:216-217` records only "CANDIDATE_UNVERIFIED".
- **Minimal fix:**
  - Append to `proof:26`: "For p ≥ 11, relative to Lev 2022 Thm 2 (statement level), used only when the invoked normal form has ⌊2p/3⌋+1 ≤ κ̂ ≤ p−3; p = 7 is Lev-free."
  - Tag `proof:217` and `proof:240` the same way.
  - Recommended: add the same tag at `proof:20-22` and to the completeness sentences at `proof:150` and `proof:258-259`.

### Optional items (no verdict impact)

- **O1.** The DAV row (`proof:79`) should list fewodd addendum:12 in its verdict column, as the acceptance of the empty-run instance fewE-v4:42–43.
- **O2.** "RUNS verdict m6" at `proof:164` is not in the manifest; OLSON-few-v3:36 cites runs L49 instead. The inline conjugation argument is enough, so cite L49 or drop the reference.
- **O3.** The termination measure at `proof:52-53` should be labelled as the author's own; the source (fewE-v4:37) only asserts that a terminal form exists.
- **O4.** At `proof:198`, "normalization preserve o_F ≤ p−1" should read "normalization gives k ≤ o_F ≤ p−1".
- **O5.** The quantifier at `proof:241-242` is ambiguous. Suggested wording: "every admissible normal form has k ≥ p+1, or has k = p with (S1) failing at its κ̂ (necessarily κ̂ ≥ ⌊2p/3⌋+1)".
- **O6.** At `proof:242` (wording kept by E2), "below every LS threshold" can be misread as saying (S1) is unavailable.
  - S1-sharp still gives (S1) for κ̂ ≤ ⌊2p/3⌋ with no length hypothesis; for example k = p+1, κ̂ = 1, |Y| = p+1.
  - The binding obstruction is the caller side that E2 names.
- **O7.** The trust summary (`proof:33-37` and `proof:203-209`) should do two things:
  - Name the transitive imports that were not re-audited: SHgen's KB, KBH, B′(b) and C1 (rotkp:59), and G-LS's RED, SLZ, EXT and PROP (G-LS verdict:50). Note that the G-LS verdict at :5 records Lev as G-LS's only external premise.
  - Say that explicit no-computation records exist at RUNS:3, FB:5, K01:63 and G-LS:50, and that the other supplied verdict lines are silent (none of them records a computation).
- **O8.** Two wording changes:
  - At `proof:28`, "verbatim items 1-2" should be "items 1-2 specialized to p = 5".
  - At `proof:138-139`, "the scope's sentence ... is used as written" should name the actual premise, fb:11–12. The LS-scope lead at :16–17 is literally false at κ̂ = 0 and must not be read as a premise.

## 9. Interface domain (kept separate from proof gaps)

- **No interface is used outside its original domain.**
- **p5-lift citations.** The LED row's citation of p5-lift:37 is a written overlay reproduced at `proof:172-173`, with no dependence on C5. The p5-lift:34 citation is pin metadata only.
- **Ranges cited but not in the supplied text:**
  - lowodd-v1:48–61
  - FB erratum:9–27
  - G-LS proof:15–28 and its m3 overlay at :184 and :187
  - runs-v4:204–205
  - REFL r4:13–14
- These do not matter: every statement used is fixed by a supplied verdict line.
- **Proof gaps: none.**

## 10. Erratum v1, assessed independently

- **E1 is correct.**
  - (S1) at κ̂ is ROT-KP+'s hypothesis (kps-slz:10).
  - FB(b) (fb-proof:29) additionally excludes zero-sums of length exactly 2κ̂.
  - Example: any Y with (S1) that contains g^{κ̂}(−g)^{κ̂} satisfies ROT-KP+'s input but not FB(b)'s.
- **E2 is correct.**
  - At k ≥ p+1 with t = 0, L = R = p−1+2κ̂ ≥ p+1 once κ̂ ≥ 1. So the old "SC0/index-one is unavailable" overstated the case.
  - Likewise, o_F(u°) ≤ k is only a bound, not a value.
- **Scope of the erratum.**
  - Each Old span occurs exactly once, at `proof:225-226` and `proof:242-245`.
  - The main statements and Sections 3–5 are untouched.
  - The erratum grants no acceptance, and I inferred none.
- **Residual wording still open after E1/E2:** N1 at :216–217, O5 and O6.

## 11. Trust boundary

**p = 7 (written, Lev-free).** The result rests on:
- NF, PM*, K1 and GRX;
- DAV (Davenport-alpha with m4, using the classical D(C_p ⊕ C_2p) = 3p−1);
- EGZ;
- S1-sharp (Savchev–Chen/Yuan index-one);
- G-LS with e = 2 (Cauchy–Davenport);
- K01 and FB(a), with SC0, KETA, SHgen and SHgen-E;
- REFL-few-odd, the ordered deletion ledger, and RGR-LONG.

**p ≥ 11.** The same inputs, plus Lev 2022 Theorem 2 at statement level (proof not replayed).
- Lev is confined exactly to the cells ⌊2p/3⌋+1 ≤ κ̂ ≤ p−3 of the normal form invoked.
- (A), (B) and ROT-LS are Lev-conditional as universal statements.

**Computer-assisted input.**
- None is recorded as a premise for any p ≥ 7 interface used.
- C5 enters only at p = 5, through Remark P5's citation union with p5-lift items 1–2 (o_F = 4 piece; separate trust class).
- p5-lift contributes nothing beyond a written overlay and metadata to p ≥ 7.

**S(p).** ROT-KP+'s S(p) trust class is confined to Section 7.

**Not re-audited here:** the transitive proof bodies.

## 12. Open targets (descriptive only)

**o_F = p.**
- The rotation half remains open for avoiders whose every normal form has k = p, with κ(w) ∈ [⌊2p/3⌋+1, p−1] and (S1) failing.
- **The one-short-LS boundary is correct.**
  - For κ ≤ p−2, the stated missing lemma covers the cell.
  - At κ = p−1 the sequence statement is false. The family Y = g^{2p−1}(3g)^{p−1} has no zero-sum of length 2p: that would need b ≡ 0 (mod p), forcing b = 0 and then a = 2p > 2p−1. But it does contain the zero-sum g^{p+3}(3g)^{p−1} of length 2p+2, with coefficient sum 4p.
  - So the cell (k, κ̂) = (p, p−1) needs word-level input.

**o_F ≥ p+1.**
- Rotation cells with k ≥ p+1.
- REFL beyond o_F ≤ p, i.e. RES_<(p) with k ≥ p+1 (both B = 0 and 1 ≤ B < κ).

**Global targets.**
- Unrestricted INV*(p).
- Ordered Olson for D_2p and for all finite groups.
- LS+ and STAB.
