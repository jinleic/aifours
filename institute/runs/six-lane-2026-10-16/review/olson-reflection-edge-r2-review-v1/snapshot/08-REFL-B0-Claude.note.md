# Hostile review: Corollary REFL-B0 r2

Citations are `SS:LL`, meaning SOURCE SS at LF line LL.

**Verdict: ACCEPT-WITH-FIXES. 0 FATAL / 0 MAJOR / 7 MINOR.**

The composition is correct under its stated hypotheses. Every fix concerns scope or wording.

## A. What is new, and what is imported

**New content.** This is unreviewed and checked independently below.
- **N1.** Under B = 0, only the moves P1 and P2 ever fire.
- **N2.** P1 and P2 keep R, B = 0, the length and every rotation letter, and κ never increases.
- **N3.** The hypotheses transfer from κ to κ′, and the Δ′ arithmetic holds.

**Imported at accepted scopes.** I checked how each is applied, not its proof.
- The correctness of RED's process: avoidance preservation, termination, Exit P1 and the terminal class (01:136–164; accepted at 07:8). This includes K0*, K1*, (I2), (I3), FUS and PM0 (02:84–114).
- The small-k verdict through B0S (06:3, 06:11).
- B0S-CJ''' and the first two sentences of Corollary 2, read through the overlay (03:14–17, 05:13, 05:15).

## B. Independent checks

1. **Normalisation and word order.**
   - c = x⁻¹ exists because p is prime. The automorphism ρ_v→ρ_{cv}, σ_v→σ_{cv} sends ρ_x to ρ_1 (02:15–16).
   - It preserves avoidance, the block partition, block lengths and neighbour inequality (08:79–81). So R, H, κ, k and g are unchanged.
   - After it, A = R and B = 0, so A ≥ B needs no swap.
   - Avoidance is invariant under cyclic rotation (ab = 1 ⇒ ba = 1), so reading runs cyclically is valid.
   - SPEC concatenates the pieces T_U, T_X, T_V in order, so increasing-index order is kept (02:80–83). ✓
2. **B = 0 is invariant.**
   - P3 needs a run with a, b ≥ 1, and P4 needs a (1,1)-run (01:142–144). Neither exists when B = 0.
   - P1 and P2 never change a rotation letter; PM0 only concatenates runs (02:108–109).
   - By induction B stays 0 and R stays constant. ✓
3. **P1 parity cases.**
   - Single fusion X·E with E even: ⌊(a+b)/2⌋ = ⌊a/2⌋ + b/2, so ΔH = 0.
   - Double fusion X·E·Y (Y has value u, across a second empty run): ΔH = [a and c both odd].
   - Both neighbours even, whichever block is recoloured: ΔH = 0, because any triple fusion has an even outer block.
   - Maximal-block reread: only E changes value, and blocks fuse only across empty runs, so these are all the fusions.
   - If the far run is empty and Y ≠ u, it stays genuine.
   - A double fusion with k = 2 would need R = 0, which is excluded.
   - **P2:** the merged run is nonempty, so nothing fuses. Empty runs and their neighbouring values are unchanged (02:113–114), and ΔH = 0.
   - No move creates an empty run. ✓
   - **Cross-check:** with R fixed, (0.1) (02:30) gives o_F = 2p − R + 2κ, so Δo_F = 2Δκ. This agrees independently with MON (08:86–112).
4. **Exits and terminal state.**
   - Exit P3 cannot be reached.
   - **Exit P1:**
     - (I2) forces κ(w_end) = 0 (01:27–31).
     - K0* gives κ(w′) ≥ 1.
     - So the last step is C2 with a and c both odd. The resulting even block σ_u^{a+b+c} contradicts (I3) (01:155–156).
     - The κ(w_end) ≥ 1 branch (TII, SING, QQ) and the imports (I1), (I4) are never reached.
   - **Terminal state:**
     - There is no even block. An even block next to an empty run allows P1; otherwise P2 applies, and g ≥ 1 forces k ≥ 3.
     - κ′ ≥ 1 by K0*, and κ′ = 1 is excluded by K1* (01:91). B = κ is vacuous because B = 0 < κ′.
   - **Conclusion:** w_T ∈ RES_<(p) with B = 0, all blocks odd, R(w_T) = R, 2 ≤ κ′ ≤ κ, and k′ = 2p − R + 2κ′.
   - **No o_F or RGR hypothesis on w0:** w0 is not assumed to satisfy o_F ≤ p or to be RGR. The only o_F ≤ p in the chain, inside (I3), is derived for RGR outputs (01:33–34). ✓
5. **The two branches.**
   - **k′ ≤ p:** B0S excludes w_T (06:11).
   - **k′ ≥ p+1:**
     - R ≥ 4κ−4 ≥ 4κ′−4 and 2κ′ ≤ p−1, so (H''') holds.
     - Δ′ = p + κ′ − 1 − R.
     - Corollary 2 would force both Δ′ ≥ 2 (that is, R ≤ p+κ′−3) and 5R < 4p + 6κ′ − 10.
     - Both bounds increase in κ′, so each alternative of 00:15 contradicts one of them. ✓
6. **Edge cases.**
   - κ(w0) < 0: not an avoider, by (Pairs) (02:69).
   - κ = 0: K0* applies directly.
   - κ(w0) = 1: no terminal state can exist (2 ≤ κ′ ≤ 1), so the R conditions are not needed.
   - R = 0: Lemma AR (02:66–67, inherited at 01:138–139). The hypotheses alone would also force κ < 0.
   - F = 0: vacuous, and excluded by 2κ ≤ p−1.
   - R ≥ 2p: ρ_1^{2p} is an identity subword.
   - The proof states none of these explicitly (m3).
7. **Examples.**
   - **p = 31, κ = 7:**
     - The three thresholds are 24, 36, and 156/5, which gives R ≥ 32.
     - Avoiders have 31 ≤ R ≤ 61, so the covered range is [32, 61] ✓.
     - For κ′ ∈ [2, 7], k′ = 30 + 2κ′ ∈ [34, 44], so the CJ''' branch is always the one used.
   - **p = 7:** κ = 2 needs R ≥ 6 ✓; κ = 3 needs R ≥ 8 ✓; κ ≥ 4 is excluded ✓.

## C. Coverage beyond REFL-fewodd, and existence

**Containment.**
- By (0.1), fewodd's hypothesis o_F ≤ p is equivalent to R ≥ p + 2κ.
- For an avoider (R ≤ 2p−1) this implies 2κ ≤ p−1, R ≥ 4κ+1 and 5R ≥ 4p + 6κ − 10.
- So on the equal-rotation slice, REFL-B0 contains fewodd.

**The added band.** REFL-B0 adds exactly

  max(p, 4κ−4, ⌈(4p+6κ−10)/5⌉) ≤ R ≤ p + 2κ − 1.

This band is nonempty for every 1 ≤ κ ≤ (p−1)/2. For example:
- (p, κ) = (31, 7): R ∈ [32, 44], so o_F ∈ [32, 44].
- (p, κ) = (7, 2): R ∈ [7, 10].

Fewodd still covers mixed ρ_{±x} words, which REFL-B0 does not.

**Existence.**
- No avoider is assumed to exist. The result is a non-existence statement proved by contradiction.
- "The terminal word" at 00:53 is hypothetical.
- When R < p + κ, every word in the cell has g ≥ o_F − R ≥ 1. So the result says no equal-rotation avoider with those parameters exists at all.
- The band is not vacuous as a set of words:
  - Example at (p, κ, R) = (7, 2, 7): blocks of lengths 2, 3, 3, 3 and eight 1s; seven runs ρ_1 and five genuine empty runs.
  - Then o_F = 11 > 7, and (Z0), (V) and (P0) all hold, with (P0) tight (5 ≤ 1 + 4).
  - I do not decide whether this word avoids; the corollary does.

## D. Findings (all MINOR)

**m1 (00:1, 00:7). The title and scope line overstate the result.**
- "REFL(p) for avoiders with all rotation letters equal, without a bound on o_F" omits the R/κ range. It reads like REFL for the whole equal-rotation slice.
- o_F(w0) = 2p − R + 2κ is fixed by (R, κ). In scope it is at most min(2p−2κ+4, (6p+4κ+10)/5) ≤ (10p+18)/7, which is 46 at p = 31 and 12 at p = 7.
- 00:17 ("no hypothesis on o_F") is accurate.
- **Fix:** retitle to "…in the range R ≥ 4κ−4, 2κ ≤ p−1, 5R ≥ 4p+6κ−10 (no hypothesis o_F ≤ p)", and state the o_F identity.

**m2 (00:15). The first alternative is redundant.**
- R ≥ p+κ−2 gives 5R ≥ 5p+5κ−10 ≥ 4p+6κ−10, because κ < p. In the same way, Δ ≤ 1 implies p ≥ κ+5Δ−5.
- **Fix:** keep only 5R ≥ 4p+6κ−10, and mark the bullet at 00:45 as subsumed.
- Optional: add that every R is covered when κ ≤ ⌊(p+10)/6⌋. This includes κ ≤ 2 for all p.

**m3 (00:12–16, 00:33). R ≥ 1 and F ≥ 1 are never stated.**
- **Fix:** add, as fewodd does at 08:37–38, "words without reflections are vacuous; R = 0 is excluded by Lemma AR (02:66–67)". Also state that κ(w0) ≤ 1 is immediate.

**m4 (00:40). "The exits … are contradictory there" is too terse.**
- **Fix:** cite 01:152–156 for the κ(w_end) = 0 branch, via (I2), (I3) and K0*.
- Cite 01:162–164 for the terminal state, via K0* and K1*.
- Record these as unused: (I1), (I4), TII, SING, QQ, KB*, CAP, KBH*, P3 and P4. This also documents the smaller dependency set.

**m5 (00:38–39). Reread completeness and PM0's no-fusion are asserted only by citation.**
- **Fix:** add the reread argument from B.3: only E changes value, and the merged PM0 run is nonempty (02:113–114). Add the (0.1)/MON cross-check.

**m6 (00:53–54). Remark (1) does not show what it intends.**
- "k′ ≤ 44 and o_F(w0) ≥ k′ by MON" does not show o_F(w0) > p.
- MON is not in the import list.
- **Fix:** write "o_F(w0) = 2p − R + 2κ = 44 > 31 by (0.1) (02:30), so fewodd does not apply. A hypothetical w_T would have k′ = 30 + 2κ′ ∈ [34, 44]."

**m7 (00:60–61, 00:28–29). Remark (3) is wrong for P3, and the CJ''' import paraphrase is imprecise.**
- Remark (3): TR keeps R, B and κ (02:104–106).
- P4 lowers R by 2, A and B by 1 each, and κ by 1. κ drops by 2 when two odd neighbouring blocks fuse (08:104–111).
- Import paraphrase:
  - Add the setting: length 4p−2, F, R ≥ 1, maximal decomposition, genuine empty runs.
  - k ≥ p+1 is not a hypothesis of CJ'''.
  - Under (H'''), the k′ ≤ p branch has Δ′ ≤ −κ′−1 ≤ 0, so CJ''' alone covers it (05:33).
  - State whether the small-k import is kept as a redundant second route.

## Scope

This is a partial result on the equal-rotation slice only. It makes no claim about full REFL(p), INV*(p) or ordered Olson, and no novelty claim. The open cells remain untouched, for example (31, 7, 31) and κ ≥ (p+1)/2.
