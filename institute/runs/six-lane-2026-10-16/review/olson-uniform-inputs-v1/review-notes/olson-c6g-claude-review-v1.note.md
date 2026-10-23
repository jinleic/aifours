DISPOSITION: ACCEPT-WITH-FIXES

There are no FATAL or MAJOR findings. The core chain is correct for every NMH word with R ≤ 2p − 3 and any run structure:

- Lemma P0 → canonical lifts → NW / GS → SL / SCW-G (all term sums, the s = 2 split, the pin) → C0+ → Theorem SEED-G.
- Corollaries SA and PA, and Propositions RA2 and RA3, recompute correctly.

The fixes needed are one coverage corollary that is false as stated, plus some wording.

## FATAL
None.

## MAJOR
None.

## MINOR

**M1. Corollary (large B) is false without a prime range** (`c6/proof-SEEDG-r1.md:237-239`; also the "exactly" at `:207-208`)

The file states no range on p, and the setting at `:19` is p ≥ 5. At p = 7 there are two all-single-letter item-(iii) classes with B ≤ 3 that nothing in this file excludes:
- **The classes:** (kB, B) = (2, 2) = (2, p−5) and (1, 3) = (3, p−6), with kB + B = 4 = p − 3 and R = k = 11.
- **Not covered by SEED-B, RA2 or RA3:** these need p ≥ 11, p ≥ 11 and p ≥ 13 respectively. Also, at p = 7 the value m = 2 exceeds the CF(PA) count ⌈(n−B−4)/3⌉ = 1 for both classes.
- **(7; 2, 2) is outside SA and PA:**
  - SA: the lower bound is ⌈8/3⌉ = 3, but the upper bound is min(3, Δ0+B−b*−2 = 2, 3) = 2.
  - PA: the lower bound is 2, but the upper bound is ⌈(k−2B−4)/3⌉ = 1.
- **(7; 1, 3) is outside SA and PA:**
  - SA: the lower bound is 3, but the upper bound is ⌊8/3⌋ = 2.
  - PA: it needs Δ0 = 3 ≥ B+1 = 4, which fails.
- **Other p = 7 class:** (7; 1, 2) is covered by SA, with region m ∈ [2, 3].
- **Also at p = 7:** the listed class (3, p−7) is not a class at all, since kB = 0.

Fix: restrict the corollary to every prime p ≥ 11. Record p = 7 separately; the packet's only p = 7 coverage is c3's computer-assisted run under Theorem C.

**Sharpening.** All six Claim-E' classes already lie inside SA or PA. Here E = 0, b* = 1, and condition (i) holds. I re-derived all four arcs in each case as generic.

| (p; kB, B) | Δ0 | region | m |
|---|---|---|---|
| (11;4,2) | 5 | SA [4,4] | 4 |
| (11;5,2) | 4 | PA [4,4] | 4 |
| (13;6,2) | 5 | PA [4,5] | 4 |
| (13;7,2) | 4 | PA [5,5] | 5 |
| (13;5,3) | 5 | SA [5,5] | 5 |
| (17;7,4) | 6 | SA [7,7] | 7 |

For example, for (17;7,4):
- λ(Q) = 6 and λ(Qᶜ) = 9.
- For an aligned run: λ(Q+t) = 7 and λ((Q+t)ᶜ) = 9.
- For an anti run: λ(Q+t) = 6 and λ((Q+t)ᶜ) = 10.

The class (11; 5, 3) is outside both regions: for SA, 5 > 3; for PA, Δ0 = 3 < 4.

Corrected statement: for every prime p ≥ 11, the uncovered classes are contained in {B ≥ 4, 2B + kB ≥ p − 1} ∪ {(11; 5, 3)}. The cross-reference "(both IND* [W+F]; see Sec. 6)" also points to nothing: Sec. 6 does not treat these classes.

**M2. Wrong justification in Lemma CF** (`:158`)

"(k >= 12)" does not follow from the setting; p = 7 gives k ∈ {10, 11}. The needed fact holds for every k ≥ 6, because the path ends t+2 and t−2 are at cyclic distance min(4, k−4) ≥ 2. Replace the parenthetical with that.

**M3. Empty seeds** (`:52-55`, `:147-149`, `:285-286`)

The definition of a seed requires a_t ≤ b_t. Yet three places treat "a_t > b_t" as an exclusion: the parenthetical in the definition, Remark (1), and Part B. So Theorem SEED-G's hypothesis "every run has a quality seed" does not literally cover the empty case.

Fix: state "for every run, either a quality seed is established or GS(a) yields an empty interval (then w does not avoid)."

Part B's "such runs are excluded outright" is wrong as written:
- An empty extreme QS window only shows that no nonempty quality seed exists for that weight.
- The word is excluded only when some configuration actually puts s_lo and s_hi inside the QS bounds, as GS(b) does.
- Otherwise SEED-G simply does not apply to that word.

## INFO

- **RA2 and RA3(b) are generic.** Their configurations hit the third term (ties such as p−2−m = p−m−2, and p−3−m = p−m−3), so these classes are also inside PA (Δ0 = B+1).
  - Only RA3(a) is genuinely non-generic: λ(Qᶜ) = p−m−3 is strictly below the third term p−m−2. This is as Remark (1) says.
  - RA2's direct argument (Σx = −2) remains cleaner, since it does not need C0+.
- **Remark (2) at `:150`** says SCW-G "needs nothing but (QS)". In fact the s = 2 split (`:122-127`) and the pin's lower end (`:129`) also use a_t ≥ λ({t}). That fact is part of the seed definition, so nothing breaks, but the remark should say so.
- **`:8`** omits the 07:39 correction to Lemma H. This has no impact: only the necessary direction for proper patterns is used.
- **`:99`, `:106`:** U2+T2 and V2+S2 are actually ≥ (stated bound) + 1, because m + m′ ≥ 2. The slack is harmless.

## Requested checks (all pass)

- **Imports are used within their hypotheses.**
  - Lemma H, ARC and CLAIM (`:29-36`): used only in the necessary direction, for proper Q, with β = 0.
  - TS and SL: these use only ARC and CLAIM, so they hold for every NMH word.
  - C0+ (`:136-142`) needs only Σx = p and X_Q ≥ λ(Q) for all proper Q from x, as checked against C+ Sec. 2 and C Secs. 1-2:
    - The bound X_Q ≥ λ(Q) enters through the Kill lemma, and through the singleton bound in (A-ii).
    - Its other inputs come from the setting or (ii+): (0.1), E ≤ p−4, d_t ≤ p−3, 2kB ≤ p, and n_an(Z) ≤ B.
    - No upper bound X_Q ≤ U(Q), no congruence, and no Lemma-L structure is used.
  - SEED-G supplies exactly what (0.2) did:
    - singletons, from the lift window (`:44`, `:145`);
    - patterns with |Q| ≥ 2, from SCW-G together with SL;
    - Σx = p, from the pin.
- **Seeds come from real two-pattern arcs, for every run type.** GS(b) (`:73-75`) is exact for arbitrary d. SA and PA feed in d ∈ [−b*, E+1] and y ≤ m+E−e_t (resp. 2m+E−e_t). This covers multi-letter aligned runs, (1,1)-pairs (d = 0) and anti runs of length up to min(B, E+1).
- **Seeds lie inside the canonical lift range, and lifts are unique.**
  - Lemma P0: all nine sums are ≥ 1, so the lift window has ≤ p integers.
  - GS(a) intersects the seed with [λ({t}), U({t})].
  - Lemma NW: all six term bounds hold for E > 0.
- **Term sums hold for arbitrary weights.** The file displays 18 sums, 9 per condition; these replace SEED-B's 36 aligned/anti sums.
  - I re-derived each from (2.1), (F1), (0.1′) and (0.2′).
  - The m′ ≤ m versus m′ ≥ m−1 attribution at `:110` is correct.
  - Every sum is ≥ (Δ0 ∓ d)/2 throughout −(E+1) ≤ d ≤ E+1.
- **The s = 2 step (`:114-127`).** All six term checks hold.
  - In the branch 2Δ0 ≥ A+4, the case A + y + 3 < 4kB would force 2B + 2E + y + 7 < 0, which is impossible.
  - The other branch gives a sum ≥ (kB+B+1) + (1−B−kB) = 2.
- **The pin (`:128-132`) holds with E > 0.**
  - In the λ-branch, Δ0 + 2kB − d ≤ p + kB − E/2 ≤ 2p.
  - In the floor-branch, the bound is (Δ0−B−3)/2 < p−1.
- **Configuration existence (`:156-168`).** This holds apart from M2.
  - The counts ⌈(n_al−3)/2⌉ and ⌈(n_al−B−4)/3⌉ are correct, with n_al = k−B+e_an ≥ k−B.
  - Non-adjacency holds across intervals and across the deleted triple.
  - Q+t has m+1 blocks.
- **SA and PA regions (`:171-200`).** All eight conditions in each region are correct: worst cases, monotonicity, and the implications (a1)⇐(b1) and (c1)⇐(d1).
  - In PA, (c2) is exactly Δ0 ≥ B+1, and (d1) is exactly b* ≤ Δ0+B−1.
  - The regions are monotone in b* (`:202-203`).
- **RA2 and RA3 arithmetic.**
  - All λ and λᶜ values recompute correctly.
  - The seeds are [0,0] and [−1,−1] for RA2, and [0,1] and [−1,0] for RA3(a) and (b).
  - Availability holds, including the p = 11 and p = 13 rounding edge cases.
  - (QS) holds at Δ0 = 3 and Δ0 = 4.
  - In RA2, Σx = −2 ≢ 0 (mod p).
  - The seeds lie inside the canonical windows: for RA2, [7−p, 2] for aligned runs and [5−p, 1] for anti runs.

## Exact scope (after fixes)

- **Lemmas P0, NW, GS, SL, SCW-G and C0+:** every NMH word with R ≤ 2p−3 (p ≥ 5 prime), with any run lengths, (1,1)-pairs and any positions.
- **Theorem SEED-G:** per word. It needs (i) or (ii+), and for every run either a quality seed or a proven-empty seed.
- **Corollaries SA and PA:** every word of a class inside the region, provided that word satisfies (i) or (ii+). A sufficient class-level condition is E ≤ 4, or 2kB ≤ p together with E ≤ 2(k−kB−2B)−1.
- **RA2:** (B, kB) = (2, p−5) for p ≥ 11; this needs no C0+.
- **RA3:** (3, p−6) for p ≥ 13, and (3, p−7) for p ≥ 11.
- **Corollary (large B):** only for p ≥ 11, as corrected under M1.

## What remains open

- **All-single-letter classes:**
  - B ≥ 4 with 2B + kB ≥ p−1 outside PA (the [F] aid counts 64 such classes for p ≤ 43);
  - (11; 5, 3);
  - the p = 7 classes (2, 2) and (1, 3).
- **Excess classes outside SA/PA, or inside a region but failing C+'s class condition** (the [F] aid counts 5,530 for p ≤ 43). These have only word-level arguments: the word's own seeds, C/C+ with computed (H), or IND*.
- **Words violating both (i) and (ii+).**
- **The kernel computation at `:272-274`** has no receipt and is not evidence.
- **No headline result.** Nothing here proves NMH(p), MIX_DEF_HIGH(p), RUNS(p), PAR(p), INV, INV* or ordered Olson for D_2p. The class counts are aids only.
