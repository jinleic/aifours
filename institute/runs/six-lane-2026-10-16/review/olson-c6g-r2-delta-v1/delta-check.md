# olson-c6g-r2 delta check v1: delegated parent delta check (subagent SeedGReviewDesk)

Written 2026-10-17T18:41:40.300314-07:00 (host clock, PDT). Scope: the change c6/proof-SEEDG-r1.md -> c6/proof-SEEDG-r2.md only. Lane root
`/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-run-count/mixdef-high/c6`. The two new files
proof-SEEDGstar.md and proof-SEEDG-cls.md go to the separate star reviews (`olson-c6g-r2-star-{codex,claude}-review-v1`).
Only correctness is checked here. Novelty and significance are not assessed.

## Outcome: DELTA-ACCEPT-WITH-NOTES

- r2 is r1 plus the replacements declared in r2 lines 3-22, plus three undeclared edits. None of the three is mathematical (N2).
- Every FATAL, MAJOR and MINOR finding of both r1 review notes is addressed in r2 text (map below). Both notes had zero FATAL findings. Codex had one MAJOR and two MINOR; Claude had M1-M3 MINOR.
- Every replacement claim I could test recomputes with my own arithmetic (own code, no lane code), sections A-G.
- The residual notes N1-N4 concern wording and accounting only; none changes a statement's truth.

## Inputs (sha256 verified before use; no mismatch)

| file | sha256 | bytes | LF-split lines |
|---|---|---|---|
| c6/proof-SEEDG-r1.md | fb3f8b9d2174ad1131e1e66cf7640429ef6fe8993b82ec19c4f60f0748d31e80 | 32166 | 311 |
| c6/proof-SEEDG-r2.md | 353b0e95c4e58d874038a11b5864514f4049753853d355015e27ebf7330130b7 | 36693 | 348 |
| review/olson-c6g-codex-review-v1.note.md | b1dcd57ba51213640f263ca4915436f7b447ebf44b5d256eaf476cea21453c99 | | |
| review/olson-c6g-claude-review-v1.note.md | 8c03644ddd4b7328994cbdf5c7ff6fbb5f787a99c2c92ee69c77bf2910a3d3cc | | |

The artifacts in this directory are `diff.txt` (exact difflib unified diff, n=0), `receipt.json` (hashes and opcodes), `delta_arith_check.py` (my code) and `arith-check.json` (its output).
Their hashes are in the final report and in receipt.json; this file cannot contain its own hash.

## Delta structure (diff.txt: 15 hunks; 286 r1 lines unchanged; 25 r1 lines replaced by 62 r2 lines)

| r1 lines | r2 lines | content | declared? |
|---|---|---|---|
| (insert) | 3-22 | r2 version header listing fixes (1)-(5) | header itself |
| 6 | 26-27 | status line: "r1: Codex and Claude ACCEPT-WITH-FIXES; the r2 changes not yet re-reviewed" | no (metadata, N2) |
| 8 | 29-30 | Lemma H cited "with its 07:39 correction; only its necessary direction for proper patterns is used" | (5) |
| 55 | 77-79 | Definition: an empty intersection of GS(a) seeds from actual configurations excludes w; an empty (QS) window alone is not an exclusion | (4) |
| 126 | 150 | 2-run split: "d_u > 2kB + B (for both parities of d_u + B)" (r1: "> 2kB + B - 1") | (3) |
| 143-145 | 167-171 | Theorem SEED-G: p >= 5 explicit; per run a quality seed OR GS(a) seeds with empty intersection; proof handles the empty case | (4) |
| 148-151 | 174-179 | Remark (1): RA2 and RA3 (b) generic and inside PA, only RA3 (a) non-generic, empty (QS) window is not an exclusion. Remark (2): SCW-G also uses a_t >= lambda({t}) | (4), (5) |
| 158 | 186-187 | Lemma CF: "(k >= 12)" replaced by "cyclic distance min(4, k - 4) >= 2, as k >= 2kappa + 3 >= 7" | (2) |
| 173 | 202-203 | Corollary SA conclusion: "quality seed (or seeds from actual configurations with empty intersection, which exclude w)" | (5) |
| 191 | 221-222 | Corollary PA conclusion: same | (5) |
| 207-208 | 238-241 | Sec. 5 "exactly" now "For p >= 11"; p = 7 classes (B, kB) = (2, 2), (3, 1) recorded as a coverage gap | (1) |
| 237-239 | 270-276 | Corollary (large B): "Let p >= 11"; six Claim E' classes placed in SA/PA; bad IND*/Sec. 6 cross-reference removed; (11; 5, 3) outside both regions | (1) |
| 267 | 304 | (R-a'') gains "(p >= 11)" | no (scope tag, N2) |
| 272-274 | 309-311 | [I] kernel note: "(no receipt; not evidence)" plus pointer to the unreviewed proof-SEEDG-cls.md | no (responsive to Claude's scope item, N2) |
| 285-286 | 322-323 | Sec. 7 Part B: an empty (QS)-window weight is "NOT an exclusion" (r1: "excluded outright") | (4) |

## Finding map (r1 notes -> r2)

All line numbers below are r1 (`G:`/`:`) as cited by the notes and r2 as split on LF.

| note | finding (verbatim summary) | r2 text | status |
|---|---|---|---|
| Codex | MAJOR: G:237-239 the large-B corollary needs p >= 11; p = 7 permits (kB, B) = (2, 2), (1, 3), not covered by SEED-B/RA2/RA3 | 7-11, 238-241, 270-276 | addressed; adequate (A, B, C) |
| Codex | MINOR: G:156-158 "k >= 12" false; setting gives k >= 7 | 186-187 | addressed; adequate (E). Codex's aside "ends nonadjacent already for k >= 5" is itself wrong (k = 5 gives distance 1); r2 uses the correct min(4, k - 4) |
| Codex | MINOR: G:126 the equivalence is d_u > 2kB + B, not > 2kB + B - 1 | 150 | addressed; adequate (D) |
| Claude | M1: :237-239 (and "exactly" at :207-208) false without a prime range; restrict to p >= 11 | 238, 270 | addressed (A, B, C) |
| Claude | M1: record p = 7 separately; "the packet's only p = 7 coverage is c3's computer-assisted run under Theorem C" | 239-241 | gap recorded as "coverage gap, not a counterexample"; c3 pointer not added (N3) |
| Claude | M1: (3, p - 7) is not a class at p = 7 (kB = 0) | 239-240 | addressed |
| Claude | M1 sharpening: the six Claim E' classes lie inside SA or PA (table) | 270-273 | addressed; recomputed (A) |
| Claude | M1 corrected statement: uncovered classes lie in {B >= 4, 2B + kB >= p - 1} u {(11; 5, 3)} | 273-276 (adds "outside SA and PA") | addressed; containment recomputed for primes 11-199 (C) |
| Claude | M1: cross-reference "(both IND* [W+F]; see Sec. 6)" points to nothing | 270-276 | removed (no IND*/Sec. 6 reference remains in the corollary) |
| Claude | M2: :158 "(k >= 12)" wrong; ends t + 2, t - 2 at cyclic distance min(4, k - 4) >= 2 for k >= 6 | 186-187 | addressed; adequate (E) |
| Claude | M3: :52-55, :147-149, :285-286 treat "a_t > b_t" as an exclusion; Theorem hypothesis must allow "quality seed or GS(a)-empty"; Part B "excluded outright" wrong | 77-79, 167-171, 174-176, 322-323 (and SA/PA conclusions 202-203, 221-222) | addressed; logic adequate (see N1 for residual wording) |
| Claude | INFO: RA2, RA3 (b) generic (inside PA); only RA3 (a) non-generic | 174-175 | addressed; recomputed (G) |
| Claude | INFO: :150 Remark (2) should say SCW-G also uses a_t >= lambda({t}) (2-run split, pin lower end) | 177-179 | addressed; the uses are at r2:146 and r2:153 |
| Claude | INFO: :8 omits the 07:39 Lemma H correction | 29-30 | addressed |
| Claude | INFO: :99, :106 U2+T2 and V2+S2 are >= stated bound + 1 (m + m' >= 2) | unchanged (r2:123, r2:130) | not changed; no change needed (slack is harmless) |
| Claude | scope: kernel computation at :272-274 has no receipt and is not evidence | 309-311 | addressed (undeclared in the header list) |

No r1 finding is unaddressed. The only items not acted on are the INFO slack remark, which needs no fix, and the optional c3 pointer for p = 7 (N3).

## Own arithmetic (delta_arith_check.py -> arith-check.json; formulas transcribed from r2 Secs. 0, 4, 5 and c6/proof-SEEDB-r3.md lines 35, 203-204)

- **A. Claim E' classes, (11; 5, 3) and p = 7.** All have E = 0, b* = 1 and notation (p; kB, B).
  - With the stated m, every one of the six classes is in its region: SA [4,4] for (11;4,2); PA [4,4] for (11;5,2); PA [4,5] for (13;6,2); PA [5,5] for (13;7,2); SA [5,5] for (13;5,3); SA [7,7] for (17;7,4). Delta0 = 5, 4, 5, 4, 5, 6.
  - For aligned t (d = 1) and anti t (d = -1), all four arcs are generic and (QS) and no-wrap hold. CF availability holds, and the GS(a) seeds are nonempty.
  - Example (17;7,4): lambda(Q) = 6 and lambda(Q^c) = 9. Aligned t gives 7, 9; anti t gives 6, 10. This matches the Claude table.
  - (11;4,2), (13;5,3) and (17;7,4) also lie in PA (regions [3,3], [4,4], [5,6]).
  - (11;5,3): SA region [5,3] is empty (lower end 5 > upper end 3), and PA is inapplicable (Delta0 = 3 < B + 1 = 4). Both match r2:276.
  - (7;2,2): SA [3,2] and PA [2,1] are both empty. (7;1,3): SA [3,2] is empty and PA is inapplicable (Delta0 = 3 < 4). Both are outside SA and PA, as r2:241 says.
- **B. Enumeration (E = 0, B in {2, 3}, kB >= 1, kB + B <= p - 3, 2B + kB >= p - 1).**
  - For every prime 11 <= p < 200 the classes are exactly (B, kB) = (2, p-5), (3, p-6), (3, p-7).
  - p = 7 gives exactly (2, 2), (3, 1); p = 5 gives none.
- **C. Corollary (large B) containment, primes 11-199, E = 0, B >= 2.**
  - Every class is in RB with (E) (SEED-B), in SA or PA (with b* = 1 and the stated inequalities), or RA2/RA3 at their prime bounds. Otherwise it lies in {B >= 4, 2B + kB >= p - 1} or is (11; 5, 3). Violations: 0.
  - The RB classes failing (E) are exactly the six Claim E' classes, each in SA or PA.
  - Category counts: {"SB": 130976, "SA/PA": 66704, "rest": 66243, "RA": 41}.
- **D. Off-by-one.** I tested kB, B in [1, 30] and d in [-40, 119], 144000 cases.
  - [floor((d + B)/2) + 1 < d + 1 - kB] <=> [d > 2kB + B] has 0 failures.
  - In that branch lambda >= kB + B + 1 has 0 failures.
  - The r1 form "> 2kB + B - 1" fails, e.g. at (kB, B, d) = (1, 1, 3) and (1, 2, 4); the latter is Codex's example.
- **E. Lemma CF.** For 5 <= k <= 200 the cyclic distance of t + 2 and t - 2 is min(4, k - 4): 1 at k = 5, 2 at k = 6, 3 at k = 7.
  - It is >= 2 exactly when k >= 6, and the setting gives k >= 2kappa + 3 >= 7 (kappa >= B + 1 >= 2).
- **F. Region inequalities: brute force, every class for primes 5-31.** 7274 classes; 3055 have a nonempty SA region and 3602 a nonempty PA region.
  - Checked: every m in each region, every weight d in [-b*, E + 1] (d = 0 only when E >= 2), and every y of Lemma CF's range (m <= y <= m + E - e_t, resp. 2m <= y <= 2m + E - e_t).
  - Conditions: all four arcs generic, (QS) for s_lo and s_hi, no-wrap, 2m + 2 <= k, and the CF count.
  - Result: 1380480 instances, 0 failures.
  - Mutation controls: m = (region low end) - 1 makes 5594 of 6640 class/region cases fail. Widening the y range by one makes 391 of 6657 fail. So the check is not vacuous.
- **G. Remark (1).** The Sec. 5 PA configurations were tested at each class's own m:
  - RA2 (B = 2, kB = p - 5, m = (p - 3)/2) and RA3 (b) (B = 3, kB = p - 7, m = (p - 5)/2) are generic and inside the PA region. Seeds are [0,0]/[-1,-1] and [0,1]/[-1,0], with (QS), no-wrap and availability. This holds for all 42 primes 11-199.
  - RA3 (a) (B = 3, kB = p - 6, m = (p - 3)/2) is non-generic: lambda(Q^c) = p - m - 3, while the third term is p - m - 2. It is outside SA and PA, and its seeds are [0,1]/[-1,0]. This holds for all 41 primes 13-199.

The lane receipt c6/out/seedG2_E.txt (read only, unchanged since r1) contains no `OPEN0:SA` key. So the r2 Sec. 6 wording "(R-a'') ... outside PA" agrees with the corollary's "outside the regions SA and PA" for the counted OPEN0 classes.

## Residual notes (no fix required for acceptance; wording/accounting)

- **N1 (wording).** Lemma GS (a)/(b) at r2:91-95 is unchanged. It still says its interval "is a seed" (resp. "a quality seed"), although the r2 Definition (r2:74-79) requires a_t <= b_t.
  - The empty case is carried correctly by the Definition parenthetical, the Theorem hypothesis and proof (r2:168-171), and the SA/PA conclusions. Read literally, though, "seeds of t obtained by Lemma GS (a) ... have empty intersection" calls a possibly empty GS(a) interval a "seed".
  - Cleaner wording would be: "if w avoids, x_t lies in [max(lambda({t}), s_lo), min(U({t}), s_hi)]; if nonempty, this is a seed". The logic is sound as is.
- **N2 (undeclared edits).** The header says "No other statement or proof step changed". That holds for statements and proofs. Three further edits are not in the (1)-(5) list:
  - the status line (r2:26-27);
  - "(p >= 11)" in (R-a'') (r2:304), which narrows scope consistently with (1);
  - the [I] note at r2:309-311, which answers Claude's scope item and adds a forward pointer to the unreviewed c6/proof-SEEDG-cls.md, labelled "[W+F], unreviewed, not part of this file".
  - All three are benign.
- **N3 (optional).** Claude M1 suggested recording that the packet's only p = 7 coverage is c3's computer-assisted run under Theorem C. r2 records only the gap. This is acceptable, but p = 7 remains uncovered by any written uniform argument here.
- **N4.** Claude's INFO slack remark (r2:123, r2:130) is unchanged, which is harmless. Header item (2) asks readers to read Lemma CF' of proof-SEEDG-cls.md with the corrected parenthetical. That file still prints "(k >= 12)" (cls line 41) and cites r1, not r2. This is for the cls review.

## Not checked / UNKNOWN

- I did not re-audit the 286 unchanged r1 lines. Both r1 reviews accepted them with fixes. My brute force F re-exercises only the SA/PA region inequalities.
- I did not recompute the Sec. 6 and Sec. 7 [F] counts.
- c6/proof-SEEDB-r3.md is imported by the large-B corollary. By its own status line, its r3 changes are not yet re-reviewed. I did not re-check it beyond Claim E'/RB transcription (C).
- Claims in r2 about the content of the unreviewed proof-SEEDG-cls.md (r2:13-14, r2:311) are pointers only. They are not checked here.
