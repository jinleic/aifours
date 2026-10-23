# PAR/MIX_low closure repair (Rstar r4, R4-closure r1, PAR-assembly r2): delegated parent delta check

Recorded 2026-10-17T23:24:35-07:00 (host clock, America/Los_Angeles) by OlsonPar2DeltaDesk for Main.  **Label: delegated parent
delta check.**  It is a static reading by the delegated desk plus one static Codex delta review (pinned snapshot,
read-only sandbox).  It is not a fresh review of the previously reviewed proofs: it checks that the 14 closure-review
MINOR findings and the priority-scout wording request are repaired, that nothing else changed, and that the one new
statement (Corollary R4-av) is correct.  Scope is correctness only; novelty and significance are separate questions
(review/olson-par-priority-scout-v1.md) and are not assessed here.  Census and replay outputs are aids, never premises;
no census, replay or claimant code was run, imported or compiled.

Lane directory L = /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-parity/mixdef-low/c2
(read-only).  Line numbers are LF line numbers of the pinned files.  r4 = proof-Rstar-r4.md, r1 = proof-R4-closure-r1.md,
r2 = proof-PAR-assembly-r2.md; "Codex-closure" / "Claude-closure" = the two closure review notes.

## 0. Verdicts

| New file | Delegated parent delta check | Codex delta review (olson-par2-delta-codex-v1) |
|---|---|---|
| proof-Rstar-r4.md | **DELTA-ACCEPT-WITH-NOTES** | DELTA-ACCEPT-WITH-NOTES |
| proof-R4-closure-r1.md | **DELTA-ACCEPT-WITH-NOTES** | DELTA-ACCEPT-WITH-NOTES |
| proof-PAR-assembly-r2.md | **DELTA-ACCEPT-WITH-NOTES** | DELTA-ACCEPT-WITH-NOTES |

Codex disposition: **DISPOSITION: ACCEPT-WITH-FIXES**.  There is no FATAL or MAJOR finding.  There are 4 MINOR and 2 NOTE
findings; all concern change declarations, status wording or path references.  Codex: "No FATAL or MAJOR mathematical
defect found.  The avoider-based closure is valid from the stated imports."

Summary:
* All 15 repair requests are handled.
  * 13 are repaired by edits in the new files.  Codex-closure MINOR-3 and Claude-closure MINOR-10 are also corrected
    by the dated README note.
  * Claude-closure MINOR-6 is repaired in r2.  Its second part (proof-PAR-Kplus-partial-r2.md:133) is only recorded,
    at r2:107-112.
  * Claude-closure MINOR-11 (proof-PAR-K0.md:4) is only recorded, at r2:94 and r2:105-106.
  * The two import files are outside the worker's write scope and are unchanged.  Their lines are still literally
    stale, but no proof uses the stale status text.
* Theorem M (r1:61-80) now runs from avoider data only:
  * Step 0: trivial cut.
  * Step 1: Lemma M0.
  * Step 2: if B' = 0, Proposition S1' applies, with R' = 2p-k+2g <= 2p-2.
  * Step 3: otherwise Lemma S, the new Corollary R4-av and Lemma R4.
  * It no longer uses Corollary', Theorem PA or any census.
* Theorem P (r1:84-95) states F, R >= 1 and the five inherited conditions, copied exactly from
  proof-INV-reduction.md:14-16.  The chain P <= K0, (K1, K1'), S1'/A1', KB, Lemma OR, Theorem M is complete, and every
  hypothesis matches (Sec. 4.3).
* Corollary R4-av (r4:215-221) is correct.  It restates, with the required avoider qualifiers and an explicit proof
  list, the implication r3 already asserted at r3:192.
* The only mathematics beyond the declared fixes is correct supporting annotation.  No theorem scope, hypothesis or kill
  construction changed (Sec. 6).
* The notes do not block acceptance.  An optional cleanup list is in Sec. 9.
* Nothing here proves RUNS(p), INV*(p), unrestricted INV, unrestricted MIX_DEF, or ordered Olson for D_(2p).

## 1. Pins (all SHA-256 verified at 23:21:30 PT, just before writing)

| Role | File | SHA-256 |
|---|---|---|
| pair 1 old | L/proof-Rstar-r3.md | acdde81fd4bdc46b0739082c0cc4c08be2ca5fd7b78b18b5a3d81cf71f054e2b |
| pair 1 new | L/proof-Rstar-r4.md | 3b27db3f16341b2493bab1ef259e7cec8a1ce4d6d523b74518909bac541d3fa9 |
| pair 2 old | L/proof-R4-closure.md | 74929e9c40ebe893ab7466e4960be739b701c3739e2236b4ada79490690333f6 |
| pair 2 new | L/proof-R4-closure-r1.md | 4432a2d840a2651540e38d4c2b2ad102d3ba7ad21fc25f74606b1d5c9f9f8837 |
| pair 3 old | L/proof-PAR-assembly-r1.md | b1b320bf1498e1db33c294f733a555b1dfdafe6760a4dcb568e138b9789bc601 |
| pair 3 new | L/proof-PAR-assembly-r2.md | 0bb78d1f948e4646665ec89fbfe8048f81aa138bbd4d66af1328acbf82276648 |
| unchanged import | inverse-parity/proof-PAR-K0.md | 4b107fffb766855d82a1c421707d426dc7fdc0a0ece77864a73d8db1ad5f9a38 |
| unchanged import | inverse-parity/proof-PAR-Kplus-partial-r2.md | 8a13d98291a4514cd982a2059a9b9fd05653d190166b70c22e7f7558b8fefd04 |
| import | L/proof-MIX-low-partial-r2.md | adf8cb7014c91e6c7c19bef894f2e5d2f75e36a34291c7cad4993a1f85716a22 |
| import | inverse-run-count/proof-RUNS.md (M0 only) | e3682f4d02ab0062cddfda8d4199f4307860936581cf75b843a93e91dec40661 |
| definitions | proof-INV-reduction.md | f11c9de18974993b1a291f7f0cb5029299d88a3902cffb531d5f59e31bd01c29 |
| import | proof-DR.md | dbaa48bbd96e6d0e9c21e2a01cb5f1dbb78e5cdead550157113bd2a7cb84308d |
| import | repr-WAS.md | 87d7cade40e69c11e11200ae4034c0265c98d0618f715c67fccb43b43c1f6806 |
| import | proof-GR.md | 33621e9e51e2f4f38ad68cff2a3a467c5277a2c6dc5317e591e35600f945fc08 |
| definition | inverse-parity/mixdef-low/README.md (MIX_low frozen target) | 00be84d95ccedcb7f63f2982e5f68bfe9b475799265abc97dddca658fbdf2a56 |
| worker log | L/README.md (note appended at L105-116) | 850588c62a85b325a6e6544ba4ffd2b8dec6cb0850fd7d213523998bb178fcc7 |
| worker freeze log | L/out/freeze.txt (L21-23 freeze the three new files) | bd7949fb8359f43c54bed7f9fbe7170be50362801abf68f6124b4df360bb94f8 |
| review note | review/olson-par2-closure-codex-review-v1.note.md | 2ee09b8efa1de3e0f3f176484bda27edc633fcb207fb4de9c457ca09592f38a1 |
| review note | review/olson-par2-closure-claude-review-v1.note.md | bfd7038b2eee400c87eb68ea18be5ef9966ee879f9e6415fc764fe3508f9f314 |
| wording request | review/olson-par-priority-scout-v1.md | 1798e9368b81913fb01924909c6bd1c0e38040146ef5656e0528b806b5b8f707 |
| context | review/olson-par-math-parent-spot-v1.md | 4de8b4aff60a2e4f52ed5581165e2b02d1266b22070c21124c0df2ea3907a5ed |

Every hash prefix that the new files cite for these inputs matches.  This covers acdde81f...4e2b, 74929e9c...33f6,
b1b320bf...c601, adf8cb70...6a22, 0df17ff8...4a40, 4b107fff...9a38, 8a13d982...fd04, f11c9de1, e3682f4d, 33621e9e,
87d7cade, 2ac68aa5, 1c6e9c18 and 4e1b6d0b...6c6a.  It also covers the two closure notes, 2ee09b8e...a1 and
bfd7038b...14.  The three originals are unchanged, as the worker stated.

## 2. Exact diffs (saved in this directory)

| Diff file | SHA-256 | Hunks | +/- lines |
|---|---|---|---|
| diff-Rstar-r3-to-r4.diff | fedf9d9527fab5a198a260d26d98f549b75616616271b8fa5b5268e3d5ed2f2c | 5 | +58 / -15 |
| diff-R4-closure-r0-to-r1.diff | d1938a787cef87d00d1c261a2904744daa43e30a73befbc5ea58c479bf8699c9 | 1 (whole file) | +117 / -50 |
| diff-PAR-assembly-r1-to-r2.diff | 6ecae2e772eef8d8043e2a08b6853ffb9dfc298cd31b4a9f7292d48cf0cc0762 | 2 | +108 / -41 |

Method:
* Python difflib.unified_diff on text.split('\n'), with n = 3 and lineterm = ''.  The headers carry the file names
  and full SHA-256 values.
* The parent applied each diff in memory to the old file and rebuilt the new file exactly.
* Codex regenerated all three diffs independently and got exact matches.  Its in-memory reconstructions also matched.

Hunk classes (parent reading; this agrees with the Codex table in its note, Sec. 1):
* r3 -> r4:
  * Header and status (L3-22).
  * R*** paragraph (Claude-closure MINOR-4 wording; Codex-closure MINOR-2 realisability, L185-192).
  * R4 consequences (MINOR-4 wording; MINOR-3 line, L205-210).
  * Corollary R4-av (new, L215-221).
  * Remark scope (MINOR-5 support, L223-226).
  * Sec. 7 pointer (L235-238) and the r4 change log (L289-301).
  * Sections 1-5 are untouched.  In Sec. 6, the lemma statements of KS, AC, ZP and C are untouched.
* r0 -> r1: the whole file was rewritten.  The construction of Lemma R4 and its dichotomy are unchanged (Sec. 4.2).
  The undeclared items are listed in Sec. 6.
* r1 -> r2:
  * Header, Sec. 1 statements and Sec. 2 (a)-(c) with P5.
  * Sec. 3 heading and note, Sec. 4 table, new Sec. 5 and Sec. 6, and the change log.
  * The Statement PF text (r1:45-58 = r2:75-86) is verbatim.

## 3. Finding map (15 items -> r-text)

"Rec." means recorded in the new chain without editing the import itself.

| # | Finding (source) | Requested repair | Implementing r-text | Parent | Codex |
|---|---|---|---|---|---|
| 1 | Codex-closure MINOR-1 (note L3; assembly-r1:72) | replace stale "p >= 19 open" with the reviewer's sentence | r2:119-123 (sentence verbatim at L122-123); Theorems M, P in r2:36-37 | ADEQUATE | ADEQUATE |
| 2 | Codex-closure MINOR-2 (L5; r3:178) | realisability is not avoidance | r4:187-192 (proof; "Membership does not establish ... avoider ..., and it provides no ordered-product counterexample") | ADEQUATE | ADEQUATE |
| 3 | Codex-closure MINOR-3 (L7; c2/README:99) | historical "Theorem PF" is superseded and conditional | README:109-112 (dated note, append-only; reviewer's wording); r2:42-44, r2:71-73, r2:113-115 | ADEQUATE | ADEQUATE |
| 4 | Claude-closure MINOR-1 (R4-closure:40) | Theorem M must use avoider data, not Corollary' or Theorem PA | r1:65-80 (Steps 0-3; L79-80 "Neither ... nor any census output is used"); r4:215-221 (Corollary R4-av) | ADEQUATE | ADEQUATE |
| 5 | Claude-closure MINOR-2 (R4-closure:33) | BH(S) <= 2s - delta+ <= s-g-1 <= B-g-3 < B; S != [k] since BH(S) < BH([k]) | r1:52-54 (verbatim chain; properness before m(S) >= 1) | ADEQUATE | ADEQUATE |
| 6 | Claude-closure MINOR-3 (r3:194-195) | prove Z0+ nonempty before s <= alpha - 2 | r4:209-210 (verbatim insert); r1:31-34 (fact (iii)) | ADEQUATE | ADEQUATE |
| 7 | Claude-closure MINOR-4 (r3:192, :176) | "every normalized MIX_low avoider (after Lemma M0, with B >= 1 and A <= 2p-1)" | r4:185-186, r4:205-206 (also r4:215-216) | ADEQUATE | ADEQUATE |
| 8 | Claude-closure MINOR-5 (assembly-r1:39; r3:200-203) | P5 = Sec. 2(b) (trivial cut; M0; B' = 0 by S1'), then Remark, then (a) | r2:67-68; r4:223-226 (Remark scoped to normalized words, pointer to r2 Sec. 2(b)) | ADEQUATE | ADEQUATE |
| 9 | Claude-closure MINOR-6 (assembly-r1:70-73; Kplus-r2:133) | supersede the open status, keeping the exact scope (avoider data, not interval-feasible emptiness) | r2:119-122 (assembly part); r2:95 and r2:107-112 (Kplus part, with the MIX_DEF k <= p caveat) | ADEQUATE for r2; Kplus part Rec. only, Kplus-r2:133 still says "OPEN" | ADEQUATE (chain); import unchanged |
| 10 | Claude-closure MINOR-7 (R4-closure:47-48) | Theorem P states F, R >= 1 | r1:84-85 (also r2:25, r2:31, r2:37) | ADEQUATE | ADEQUATE |
| 11 | Claude-closure MINOR-8 (R4-closure:53-54) | ordered Olson <= INV*(p) + PAR(p) + RUNS(p) by DR-Res + DR' | r1:96-99; r2:16-17, r2:124-125 | ADEQUATE | ADEQUATE |
| 12 | Claude-closure MINOR-9 (R4-closure:11-12, :64-65) | X and delta+ "defined here"; replay is "a weakening of the facts used (evidence only)" | r1:21-22; r1:107-112 | ADEQUATE | ADEQUATE |
| 13 | Claude-closure MINOR-10 (c2/README:98-99) | mark the PF log entry superseded and conditional | README:109-112; r2:42-44, r2:113-115 | ADEQUATE | ADEQUATE |
| 14 | Claude-closure MINOR-11 (proof-PAR-K0.md:4) | update the stale "not yet hostile-reviewed" | Rec. only: r2:94, r2:105-106; r4:28-30 (note present since r3) | ADEQUATE for the chain; K0:4 still stale | ADEQUATE (chain); import unchanged |
| 15 | Scout wording request (scout L61, L75) | "inherited" = (E), (P), (V), (Pairs), (D0) of proof-INV-reduction.md:14-16 | r1:86-91 (five conditions copied exactly, plus "does not assume ... one-letter deletion"); r2:22-32; rigid-family gloss r1:63-64 | ADEQUATE | ADEQUATE |

Unaddressed: none.  Partial: items 9 (second part) and 14, as above.  This is an adequate repair for the chain,
because no proof step uses the stale status text; the import files themselves remain literally stale.

## 4. The specific checks requested (parent reading; each item was re-derived, not copied from Codex)

### 4.1 Theorem M (r1:61-80): avoider data only

* The statement (r1:61-64) equals MIX_low(p) of inverse-parity/mixdef-low/README.md:9-12.
  * kappa := p - 1 - H is defined there and at proof-PAR-K0.md:12.  It is imported through notation, not restated.
  * Oddness is required of the reflection runs only.
* Step 0: A >= 2p gives rho_1^(2p).  Otherwise A = 2p - k + 2g + B <= 2p - 1, which is equivalent to 2g + B <= k - 1.
* Step 1: the invariants checked against Lemma M0, proof-RUNS.md:402-414.
  * Length, k, d_t, the reflection-run parities and theta (y unchanged) are preserved.
  * (A, B, R, H, kappa) -> (A-1, B-1, R-2, H+1, kappa-1), so g is unchanged.
  * r_t >= 3 keeps every run nonempty, and F, R >= 1.
  * Every half window shrinks, so avoidance transfers.
  * Termination: B decreases.  The end state has only pure runs or (1,1)-pairs.
  * No inherited inequality is reused.
* Step 2 (B' = 0): all letters are rho_1, the reflection runs are odd, k <= p and kappa' = g >= 1.
  * R' = A - B = 2p - k + 2g <= 2p - 2, because k >= 2g + B + 1 >= 2g + 2 with the original B >= 1.
  * These are exactly the hypotheses of Proposition S1' (Kplus-r2:164-166).
  * A1' and the trivial cut are indeed unreachable here.
* Step 3 (B' >= 1): every normalized MIX_low hypothesis persists.
  * odd reflection runs; k <= p
  * A' - B' = A - B = 2p - k + 2g > 0
  * kappa' - B' = g >= 1 and kappa' <= kappa <= k - 1
  * A' <= 2p - 1; pure or (1,1) runs
  * Then Lemma S (r2-import) -> Corollary R4-av -> Lemma R4 -> contradiction.
* Neither Corollary' (r4:214) nor Theorem PA nor any census output is used (r1:79-80).  Verified.

### 4.2 Lemma R4 (r1:26-57) against r0 (proof-R4-closure.md:16-35)

Statement, construction (the independent set N, the complement S' and S = Z0+ u N) and dichotomy are unchanged.  The
justifications are filled in.

* (iii) Z0+ is nonempty.  Otherwise X = alpha = 0 and 2X + alpha = 0 < 2g + s + S_Z, which contradicts R***.
  * Hence m(Z0+) >= 1 and X <= g - 1.
  * Also alpha >= 2m(Z0+) + s + S_Z >= s + 2, and B >= alpha (free antis carry anti mass <= B).
  * So s <= B - 2 <= g - 2.  Verified.
* (iv) D(Z0+) = S_Z + n_d - (free anti mass).  Aligned Z0 runs have phi >= 1, and Z0 pairs are free.
  * Hence delta+ >= 2X + alpha - S_Z - n_d >= 2g + s - n_d >= g + s + 1, using n_d <= X <= g - 1.  Verified.
* Step 1: Y is nonempty, since the bh sum is B + s + 1 > 0.  Y != [k], since Z0+ is nonempty.
  * BH(Y) = s + 1 + B + delta >= 3s + g + 4.
  * The heavier parity class of each path is independent in the cycle.  k = 2g + B + s + 1 >= 11, because s >= 1 and
    B, g >= 3.
  * Greedy selection gives s + 1 <= BH(N) <= 2s and |N| >= 2.  Verified.
* Step 2(a): S' is nonempty (it contains Z0) and proper; m(S') = |N| by independence.
  * c(S') = TOT - phi(N) + |N| >= g + 1 and BH(S') <= B.  KL applies.  Verified.
* Step 2(b): the order of the argument is now correct.
  * First the BH chain: BH(S) = BH(N) - delta+ <= 2s - delta+ <= s - g - 1 <= B - g - 3 < B.
  * Next S != [k], because BH(S) < s + 1 + B = BH([k]).
  * Only then are m(S) >= 1 and c(S) >= X + phi(N) + 1 >= g + 3 derived.  KL applies.  Verified.
* Remark r1:56-57 (not used) is correct.
  * delta+ >= 2s - B suffices for BH(S) <= B < BH([k]).
  * With |N| = 1, branch (b) still gives c(S) >= g + 2.  The displayed g + 3 uses |N| >= 2.
* One ordering detail.  m(Z0+) >= 1 in (iii) also needs Z0+ to be proper.  That is available before use from the
  import r2-import:86 (Z0 is proper since the bh sum lies in [B+1, k-1]), and r1:39-40 restates it.  No gap.

### 4.3 Theorem P (r1:84-95) and the chain (r2:48-54)

The statement is PAR(p) of proof-INV-reduction.md:41-42, with F, R >= 1 (INV-reduction:12) and inherited =
(E), (P), (V), (Pairs), (D0).  These are copied exactly from INV-reduction:14-16 at r1:88-89 and r2:27-28.

| Step / lemma | Hypotheses needed | Supplied by |
|---|---|---|
| normalisation B <= A | automorphism preserves avoidance, RGR, runs, inherited conditions | K0:48-50 |
| A, B <= 2p-1; zero condition B <= kappa | avoidance; Lemma H with A, B <= 2p-1 | K0:23-31 (r2:50) |
| kappa >= 0 | (Pairs), or directly 0 <= B <= kappa | Theorem P hypothesis |
| kappa = 0: Theorem K0 | F, R >= 1, k <= p, (P), (V), kappa = 0, an even run | K0:94-96 and K0:145-147; all in Theorem P's statement |
| kappa >= 1: Lemma OR | o_F >= 1 (from (V): kappa <= o_F - 1) | Kplus-r2:24-42; k(w~) = o_F <= k <= p; R, F, A, B, H, kappa unchanged |
| B = 0: S1' / A1' / trivial cut on w~ | odd reflection runs, all rho_1, k(w~) <= p, kappa >= 1; R <= 2p-2 / R = 2p-1 / R >= 2p | OR; Kplus-r2:164-166, 207-208 |
| B = kappa >= 1: Theorem KB | F, R >= 1, A >= B, (V), o_F <= p; (D0) in the capped case | Kplus-r2:238-241; (D0) from the original word |
| kappa = 1 (K1, K1') | (V), k <= p; K1' also needs (D0) | Kplus-r2:46-48, 65-67; redundant given the two rows above (r2:54) |
| 1 <= B < kappa: Theorem M on w~ | odd reflection runs, k(w~) = o_F <= p, A >= B >= 1, B < kappa <= o_F - 1 | OR and (V); Theorem M needs no (P) or (D0) |

* The cases kappa = 0, then (kappa >= 1, B = 0), then B = kappa >= 1, then 1 <= B < kappa are exhaustive, because
  0 <= B <= kappa.
* (E) is not used.
* In the B = 0 route, R = A <= 2p - 1 already holds, so the trivial cut is unreachable there (Codex Sec. 6).
  This is harmless; A1' (R = 2p - 1) remains needed.
* Verified: Theorem P <= K0, K1, K1', S1'/A1', KB, Lemma OR, Theorem M, with every hypothesis stated in Theorem P or
  derived from it.

### 4.4 Consequence wording (r1:96-99; r2:16-17, r2:124-125)

* Corollary DR' (proof-DR.md:42-58) proves RGR membership from INV* and then uses only Theorem DR's conclusion
  (L57-58).
* DR-Res (INV-reduction:19-20) gives the same conclusion from INV_Res = PAR + RUNS (INV-reduction:44).
* Hence "ordered Olson for D_(2p) <= INV*(p) + PAR(p) + RUNS(p)" is correct.
* The three files state that RUNS(p) and INV*(p) are open and that ordered Olson is not claimed.  Verified.

### 4.5 Census labelling

* Statement PF is "[W+F, conditional on unreviewed census code; historical]" and superseded (r2:42-44).  The Sec. 3
  heading and note (r2:71-73) say the same, and the census row "used only by Statement PF" is at r2:101.
* r4:235-238 and the README note at L109-112 agree.
* r4:237-238 says only "conditional evidence".  The surrounding text already qualifies it (Codex Sec. 9).
* Census-dependent sentences:
  * r4:243-275 (Sec. 7 bullets)
  * r1:101-115 (its own Sec. 4; r1:115 says so)
  * r2:75-86, r2:101
* No theorem (M, P, PA or P5) uses them.  Verified.

### 4.6 Realisability remark (r4:187-192)

* x_t = d_t - phi_t and sum_t x_t = D - (p - k + 2g) = p, so u_t := x_t mod p has sum 0.
* theta_t := 2u_t then has zero sum.  By repr-WAS.md:11-12 (theta_i = y_(i-1) - y_i) it is realised by reflection
  values.  This is consistent with u_Q = 2^(-1) sum_Q theta_t (K0:13-14).
* The rotation runs come from d: pure aligned, pure anti, or a (1,1)-pair.
* The k odd reflection lengths have total F = k + 2H with H = p - 1 - kappa >= 0, since kappa = g + B <= k-1 <= p-1.
  Then R = 2p - k + 2kappa and R + F = 4p - 2.
* The remark now makes no claim of avoidance or of an ordered-product counterexample.  Verified.  This is a remark
  only; no proof uses it.

## 5. Corollary R4-av (new in r4; r4:215-221)

**Statement.**  Every normalized MIX_low avoider (after Lemma M0, with B >= 1 and A <= 2p-1) has lift data
(r2-import Lemma S) in R4, where R4 := R*** n {c(Z0+) <= g} n {every bh_t <= s} (r4:207).

**Proof check.**  Let v be such an avoider.  Its interval-chain lifts exist (Lemma S), and each lemma below gives
an identity 2p-subword under its condition.  Every condition therefore fails, in this order:
1. MIX-R: data outside R* (r2-import:129-130).
2. W: B >= g + 1 (no R* needed).
3. B1: some d_t >= 2p - B (no R* needed).
4. A: in R*, some bh_t >= B + 1.
   * What remains is R** (r4:149).
   * By Fact F(d) and F(c), every phi_t <= g - 1 there.
5. AC: every run cheap (inside R*).
6. KS: not every run cheap and 2 phi(Z0+) + alpha <= 2g + s - 1 + S_Z (inside R*).
   * What remains is exactly R*** (r4:184).
7. ZP: c(Z0+) >= g + 1 (full setting).
8. C: some bh_t0 >= s + 1.  All other runs have phi <= g - 1, and the exceptional-run bound phi_t0 <= g - 1 <= p - k + g
   holds because k <= p.

What survives is exactly R4.

Further points:
* Lemma G1 is not listed.  This is harmless: none of these steps or Lemma R4 needs g >= 2, and R4 itself forces
  g >= B >= s + 2 >= 3.  G1 is used only on the P5 route (r2:69).
* The conclusion is exactly the hypothesis of Lemma R4 ("v is a normalized MIX_low avoider whose lift data lie in R4",
  r1:26-27).
* R4-av is not new mathematics.  It names and gives a proof list for the implication already asserted at r3:192
  ("every MIX_low avoider has lift data in R4"), with the Claude-closure MINOR-4 qualifiers.
* Corollary' (interval-feasible emptiness, r4:214) is kept and labelled as unused (r4:220-221).
* Codex re-derived the same chain and agrees (its Sec. 3).

## 6. Content beyond the declared fixes

All items below are correct.  None changes a theorem target, hypothesis or kill construction.

* r4:
  * Header L8-9 says "no other statement changed", and change log L300-301 says "No mathematical statement of
    Sec. 1-6 changed".  Both are inaccurate, because Sec. 6 gains Corollary R4-av, the realisability proof and the
    scope of the Remark.  The change log does list these (items 1, 4, 5).
  * No other new mathematics.
* r1, undeclared but correct annotations:
  * BH(Y) >= 3s + g + 4 (L41; Claude-closure's own observation).
  * k >= 11 (L43; Codex-closure's observation).
  * The Remark at L56-57.
  * "p >= 5 throughout" (L11) and "(Census-dependent sentences: this section only.)" (L115).
  * Expanded justifications in (i), (iv) and Step 2.  These partly fall under change-log item 8, "Main (22:4x):
    explicit nonemptiness ...".
* r1, undeclared deletion: the r0:62 sentence "(R4 itself is empty in every census computed, so Lemma R4 has no census
  instance.)" was removed.  It was evidence-only text, so the deletion removes a claim and adds none.
* r2:
  * Change log L140 says "No mathematical step of r1 is changed", but Sec. 2(b) is sharpened (at B' = 0 only S1'
    applies; declared as item 7).
  * The bookkeeping tuple (A, B, R, H, kappa) -> (A-1, ..., kappa-1) (L57) is added.
  * The zero-condition sentence (L49-50) is added.
  * Two labelled review observations are added: K1/K1' are redundant (L54), and G1 is needed only for P5 (L69).
    Both are correct.

## 7. Codex delta review: disposition and every finding

Run: olson-par2-delta-codex-v1.  The runner is run_codex_note_coop.py with sha256
196fc7f10ba0bcb55d7c813adbd36eed2094670fd1167daf9711b1bc492fea69.  Model gpt-6.1-sol (provider openai), reasoning effort max, read-only sandbox,
2026-10-17T23:07:32-07:00 to 23:18:23-07:00 (651 s), status NOTE_RETURNED_UNVERIFIED, return code 0.

Scope check (parent):
* All 14 exec commands recorded in its stderr read only from review/olson-par2-delta-v1/inputs.
* Codex reports 25 SHA-256 checks, 3 exact diff regenerations and 3 in-memory reconstructions.
* It ran no enumeration, solver, network, delegation or writes.

**DISPOSITION: ACCEPT-WITH-FIXES.**  All three files: DELTA-ACCEPT-WITH-NOTES.

| Codex finding (note line) | Location | Content | Parent adjudication |
|---|---|---|---|
| MINOR (L12) inaccurate change declaration | r4:301, r4:8 | "No mathematical statement of Sec. 1-6 changed" is inaccurate: Sec. 6 gains R4-av, realisability and the scope of the Remark | AGREE; bookkeeping only |
| MINOR (L14) stale status wording | r4:31; r4:231 | the import line still calls M0 "not independently reviewed", although both closure reviews re-derived it; the Sec. 7 heading still says "The residual (open)" | AGREE; status wording only |
| MINOR (L16) relative references that do not resolve | r1:14, :15, :17; r2:61, :97, :99, :100; r4:189 | "c2/..." prefixes in files that live in c2/; bare "repr-WAS.md" should be ../../../repr-WAS.md | AGREE; cosmetic, an older convention (r0:8 and assembly-r1 already used "c2/") |
| MINOR (L18) overbroad unchanged-step claim | r2:140 | should read "theorem targets and kill constructions unchanged; normalization, dependency and scope arguments made explicit" | AGREE; bookkeeping |
| NOTE (L20-24) correct but un-itemized annotations | r1:41, :43, :56 | BH(Y) >= 3s+g+4, k >= 11 and the Remark (precise form: with \|N\| >= 1, c(S) >= g+2 suffices; the displayed g+3 uses \|N\| >= 2) | AGREE (Sec. 4.2, Sec. 6) |
| NOTE (L26) unchanged imports still literally stale | K0:4; Kplus-r2:133 | recording them in r2 repairs the chain; the source lines are unchanged | AGREE (items 9 and 14) |
| Table (L43) undeclared deletion | r0:62 | evidence-only census sentence removed | AGREE (Sec. 6) |
| Table (L44) un-itemized observation | r2:54 | K1/K1' redundancy, correct | AGREE |
| Sec. 6 (L202) | PAR B = 0 route | the trivial cut is unreachable there (R = A <= 2p-1); A1' remains relevant | AGREE; harmless |
| Sec. 9 (L242) | r4:237-238 | the PF labels are not repeated at every cross-reference ("conditional evidence") | AGREE; context suffices |
| Sec. 10 (L268) | r2:98 | should read "v2 portions within r3/r4 Sec. 1-6" | AGREE; cosmetic |
| Sec. 10 (L269-271) | r2:17, :22, :50, :81, :84-85, :113; r1:97, :103-104; r4:243 | bare root-document names and extra "c2/" prefixes | AGREE; cosmetic |
| Sec. 10 (L272) | r2:123 | the active conclusion cites r0's file name (the reviewer's verbatim sentence); it should cite proof-R4-closure-r1.md | AGREE; cosmetic (L121 already says "revised as proof-R4-closure-r1.md") |
| Sec. 10 (L273-274) | r4:15, :234, :287; r2:81 | historical references, correctly historical | AGREE; no action |
| Sec. 10 (L276) | K0:157-162; Kplus-r2:10, :122, :138-141, :313-314 | historical open-status text in the unchanged imports, superseded only for the PAR/MIX_low application; MIX_DEF in its broader scope is not closed | AGREE |

Codex also wrote "Established" (L292-294), "Open" (L296-298) and "UNKNOWN" (L300-302) sections:
* Established, from the stated imports:
  * Lemma R4 excludes normalized avoider data in R4.
  * R4-av supplies exactly those data.
  * M proves MIX_low(p), and P proves PAR(p), for every prime p >= 5.
  * PA remains a valid conditional, and P5 has a written-proof route.
  * M0 monotonicity and the realisability arithmetic were re-derived.
* Open: RUNS(p), unrestricted INV(p), INV*(p), ordered Olson, unrestricted MIX_DEF, and emptiness of interval-feasible
  R4 data (not needed); p = 3 is out of scope.
* UNKNOWN: fidelity of the census/replay code, counts, runtimes and mutations.

## 8. Parent-only notes (not raised by Codex)

* P-1 (NOTE) r1:61-62: "R >= A + B >= 2" should read "R = A + B >= 2", since R = A + B by definition.  Cosmetic.
* P-2 (NOTE, reporting): the scout's recommended wording at L75 says "... k nonempty constant reflection runs, all of
  odd length".  That is ambiguous.  Theorem M (r1:61-62) requires odd length of the reflection runs only.  Reports
  should quote r1's statement.  This is not a defect of the delta.
* P-3 (NOTE): the ordering detail in Sec. 4.2 (Z0 is proper by import r2-import:86 before (iii) uses m(Z0+) >= 1).
  No gap.

## 9. Optional cleanup for a later revision (non-blocking; none affects Theorems M, P)

1. r4:8-9 and r4:300-301: reword the change declarations (Codex L12).
2. r4:31: update the status of M0.
3. r4:231: retitle the heading.
4. r2:140 and r2:98: reword.
5. r2:123: cite proof-R4-closure-r1.md.
6. r1 change log: itemize L41, L43, L56-57 and the deletion of r0:62.
7. Paths: drop the "c2/" prefixes in c2 files, use ../../../ for root documents, and ../../ for proof-PAR-K0.md at r2:50.
8. r1:61-62: R = A + B.
9. When the owners of the import files next revise them: update proof-PAR-K0.md:4 to "reviewed: Codex ACCEPT".
   Qualify proof-PAR-Kplus-partial-r2.md:133 with the Codex L26 wording: "For the PAR application with original
   k <= p, the remaining range is covered by OR and Theorem M; this does not settle unrestricted MIX_DEF."

## 10. Limits

* Status after this check:
  * Theorems M and P are written proofs [W].
  * The r0 mathematics was reviewed by Codex and Claude (ACCEPT-WITH-FIXES).
  * The fixes now pass this delegated parent delta check, with notes.
  * Model reviews of the delta: Codex only (static).  No second-vendor review of the delta was run.
* The chain relies on these reviewed imports as reviewed: proof-MIX-low-partial-r2.md, the v2 parts of r4 Sec. 1-6,
  proof-PAR-K0.md, proof-PAR-Kplus-partial-r2.md, Lemma M0, proof-INV-reduction.md, proof-DR.md, repr-WAS.md and
  proof-GR.md.  Their internals were not re-reviewed here.
* Not established: RUNS(p), INV*(p), unrestricted INV(p), unrestricted MIX_DEF(p), ordered Olson for D_(2p), and p = 3.
  Emptiness of interval-feasible R4 data is neither established nor needed.
* Compute by this desk:
  * In-memory hashing and difflib only: three diffs, each rebuilt in memory.
  * No census, replay, enumeration, solver or claimant code.
* Compute by Codex: hashing and diff regeneration only.
* Disk:
  * This directory: three diffs, a text-only Codex input snapshot (inputs/, 26 files including manifest.json,
    ~320 KB), this file and delta-result.json.
  * Runner outputs in review/: olson-par2-delta-codex-v1.* (~312 KB, stderr included).
  * Launched at 23:07 PT, before Main's 23:17 disk notice; no stage was launched after it.

## 11. Artefact hashes (this check)

| File | SHA-256 | Bytes |
|---|---|---|
| inputs/manifest.json | 4a6393ff56d550fedce21d63dc1eca644a1af6d7c9f1d55edae76244ebaf70e9 | 11638 |
| diff-Rstar-r3-to-r4.diff | fedf9d9527fab5a198a260d26d98f549b75616616271b8fa5b5268e3d5ed2f2c | 9503 |
| diff-R4-closure-r0-to-r1.diff | d1938a787cef87d00d1c261a2904744daa43e30a73befbc5ea58c479bf8699c9 | 16397 |
| diff-PAR-assembly-r1-to-r2.diff | 6ecae2e772eef8d8043e2a08b6853ffb9dfc298cd31b4a9f7292d48cf0cc0762 | 15928 |
| ../olson-par2-delta-codex-v1.prompt.txt | ad00a944b263824618a7cfe3844685fd788564762a10313a78a6f124658360c1 | 11339 |
| ../olson-par2-delta-codex-v1.note.md | 7d3d0c7832a12a2918253e5149e7ec4355636d5e1ce7126ee1d7a9db74710b1c | 24274 |
| ../olson-par2-delta-codex-v1.stdout.txt | b706589632d8ad91b779f2ba0b8868ed3e6e5fec9fb84954e97b0085cfc26b3f | 24275 |
| ../olson-par2-delta-codex-v1.stderr.txt | 1f61609178434925d5edf762e06dd3c95c98fd788a7f912bb8e65660b0555a85 | 251831 |
| ../olson-par2-delta-codex-v1.receipt.json | 615a5c63542ca5ec0b37554a21d34532bb09d45a8c5374ce966c410385194e13 | 790 |

The stdout copy equals the note plus one trailing LF.  Hashes of this file and of delta-result.json are reported in the
desk's final message to Main.
