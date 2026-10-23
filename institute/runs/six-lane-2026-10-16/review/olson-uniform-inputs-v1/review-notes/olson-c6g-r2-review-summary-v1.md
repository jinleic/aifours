# SEED-G r2 delta and SEED-G* / X review closeout

Delegated parent review desk (subagent SeedGReviewDesk). Written 2026-10-17T19:14:47.080115-07:00. This is a correctness review, not a novelty or significance certificate. Lane files were read only. No lane fixes, commits, pushes, solver runs, network requests or external contacts were made.

## Result

- **Delta: DELTA-ACCEPT-WITH-NOTES.** The r1 MAJOR/MINOR findings are all addressed by r2; only benign metadata/scope-note edits were not in its declared list. Exact diff: 15 hunks; 286 r1 LF-split lines unchanged, 25 removed, 62 added.
- The finding map and mathematical assessment are in **/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6g-r2-delta-v1/delta-check-v2.md** (`sha256 0d8898242666018636704e8568e4ae91f0c37ef7951b3dc22f0eaceb4e389998`). v2 is authoritative. The required `delta-check.md` remains unchanged with one line-number typo (cls line 41 should be 35); v2 corrects it.
- **Codex (gpt-6.1-sol): ACCEPT-WITH-FIXES; FATAL 0, MAJOR 1, MINOR 4** (one MINOR is my prompt hash abbreviation typo, not a lane defect).
- **Claude (claude-opus-5-5): ACCEPT-WITH-FIXES; FATAL 0, MAJOR 0, MINOR 15.**
- Both runners returned exit 0 and `NOTE_RETURNED_UNVERIFIED`; I read the complete returned notes and checked their central evidence. No fixes have been applied and there has been no post-fix re-review.

## All FATAL / MAJOR findings (verbatim from the note)

Both reviewers: **FATAL none**. Claude: **MAJOR none**.

Codex note line 7:

- **M1 — The closing scope claim exceeds the receipt.** [c6/proof-SEEDGstar.md:82](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6g-r2-parent-inputs-v1/inverse-run-count/mixdef-high/c6/proof-SEEDGstar.md:82) identifies COUNT as the remaining obstacle, but [out/seedXstar2_mode0.txt:8](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6g-r2-parent-inputs-v1/inverse-run-count/mixdef-high/c6/out/seedXstar2_mode0.txt:8) records one OPENE class failing the seed test. Replace that sentence with: **“Among the 378 OPENE classes remaining in the reported range, 377 pass the seed/certification tests but fail C+’s stated class sufficient condition; one further class fails the seed/certification test.”** Failure of the class sufficient condition also does not establish failure of C+’s per-word condition.

Parent spot-check: the pinned star file at lines 79-83 explicitly reports 377 noC+ classes and one seed failure, then overstates the obstacle as COUNT only. The pinned mode0 receipt line 8 has `OPENE:fail: 1`. Independently summing its rows yields 3,114 = 1,793 SA/PA + 756 X + 187 additional X* + 377 noC+ + 1 seed failure. Thus the finding is supported. Failure of C+'s class sufficient condition does not establish failure of either per-word condition.

## MINOR finding map for the new files (reviewers' findings, not applied)

Paths c6/... are relative to `inverse-run-count/mixdef-high/` in the pinned snapshot.

### Codex: 4

| ID | file:line | finding / correction |
|---|---|---|
| m1 | c6/proof-SEEDGstar.md:42 | Certification sum is >= the MINIMUM of the nine displayed term bounds, not >= each. Correct min_i U_i + min_j T_j = min_(i,j)(U_i+T_j) >= min_(i,j) B_ij = L_A(d), then use integrality. Likewise L_B. |
| m2 | c6/proof-SEEDG-cls.md:35 | Replace false k >= 12 reason with cyclic distance min(4,k-4) >= 2, since k >= 7. |
| m3 | c6/seedXstar2.py:23 | Floating division + math.ceil exact at p <= 31, but not unrestrictedly. Use doubled integer expressions. The review gives legal arithmetic parameters p=2^61-1, Delta0=2^60+200, kappa=p-Delta0, k=p+kappa, B=d=1, E=0: float ceilings are 27 and 26 too large. Does not affect reported computations. |
| m4 | parent Codex prompt (T1 abbreviated hash), manifest.json:7 | My prompt wrote suffix `2b22`; actual hash ends `f5b22`. Full pin/task hashes are correct. |

I recomputed m1's arithmetic example independently: (p,k,kappa,B,E,Delta0)=(11,14,4,1,2,6), d=1, y'=2, m=m'=1 gives lam=0 and lamc=7, sum 7, but U1+T1's displayed bound is 10. The corrected min argument preserves the theorem.

### Claude: 15

| ID | file:line | finding / correction |
|---|---|---|
| m1 | c6/proof-SEEDGstar.md:50-52 | Per-run either/or followed by "these seeds satisfy P2/PIN" quantifies over missing seeds in the empty case. State globally: either some actual-configuration intersection is empty, OR every run has a QS* seed and these seeds satisfy P2 (PIN is redundant: m5). |
| m2 | c6/proof-SEEDGstar.md:42-43 | Same minimum-comparison wording defect as Codex m1. |
| m3 | c6/proof-SEEDGstar.md:20 | Bounds also use m-1 <= m' <= m, m' >= 1 and the floor inequality; (0.2') is used only in comparison with targets. Correct the facts-used list. |
| m4 | c6/proof-SEEDGstar.md:22-29 | LF closed forms are correct but proof skips a mirror comparison/zero-side and keeps redundant linear terms. On the stated domain, simplify to L_A=(Delta0+E+3-max(d,-1))/2 and L_B=(Delta0+E+3+min(d,1))/2. |
| m5 | c6/proof-SEEDGstar.md:40,46,63 | PIN is implied by seed b_a <= U(a) and P0: b_a-lambda(a) <= p-lambda(a^c)-lambda(a) <= p-1. Drop it (and its vacuous normal-mode code check) if desired. |
| m6 | c6/proof-SEEDG-cls.md:35 | Same wrap-reason defect as Codex m2. |
| m7 | c6/proof-SEEDG-cls.md:6,25,54,58 | Stale r1/"under review" references; update to r2. Nothing T2 uses changes substantively; r1's quality-seed theorem already suffices because T2 handles actual sigma emptiness itself. |
| m8 | c6/proof-SEEDG-cls.md:39-42; c6/seedX2.py:38-50 | Written "allowed" definition does not explicitly match extra necessary filters in the a*=1 branch. Code is sound; make definition explicit (review note lines 71-76). |
| m9 | c6/proof-SEEDGstar.md:84 | Receipt displays equal per-label/verdict counts, not per-class lines. Say reproduces per-label counts; classwise equality needs nesting/shared-code argument. |
| m10 | c6/proof-SEEDGstar.md:47-49,70-80 | Additional X* column needs X-pass => X*-pass even for code's non-co-occurring/equal weight pairs. Nesting holds; extend QQ to those weight pairs using the weaker y lower bound (review note lines 88-94). |
| m11 | c6/proof-SEEDGstar.md:81; c6/proof-SEEDG-cls.md:73-74 | Receipts alone identify one OPEN0:written:pass RA class per p at 29,31, not whether RA2 vs RA3(a)/(b). Give tuple or call it RA class. |
| m12 | c6/proof-SEEDGstar.md:84-86 | No sensitive X* control on OPENE; MODE 2 is insensitive, MODE 1 compares to X. Suggest tightened QS* control and per-class failing-test report, incl. p=31 failure. |
| m13 | c6/seedXstar2.py:13,64; c6/seedX2.py:111 | Receipts do not hash exec-ed source bytes (seedX2.py, map6.py, c4 sources) at runtime. Add hashes to future receipt headers; later freeze hashes do not recover old run provenance. |
| m14 | c6/proof-SEEDGstar.md:82-83 | Interpretive overreach: same issue Codex rates MAJOR. Scope as finite class-level [F]; class condition is only worst-case sufficient. |
| m15 | c6/proof-SEEDGstar.md:78-80,71-77; c6/seedXstar2.py:2,6; c6/seedX2.py:6,16; c6/proof-SEEDG-cls.md:30,78 | Presentation: mark totals X/X* [W+F]; OPEN0 column means all pass (not additional); filename and r2 references; docstring E>=2 vs E=0 processing; explicit CF' properness/S1 total; generic-seed-bound-attainment gloss unsupported. |

These are advisory findings; redundancy (m5), omitted routine comparisons (m4), and conservative enumeration do not invalidate the reported finite exclusions. The reviewer-proposed corrected overreach statement should still be read as conditional on the stated seed/count conditions, not as a claim that other exclusion routes fail.

## What the reviews support

- After correcting wording, [W]: LF, SCW-G*, QQ, conditional SEED-G*, PR, CF', and the implications underlying X/X*.
- L_A/L_B are the exact minima of the displayed term-sum lower bounds; LF's closed forms match. QS* relaxes QS by >= 3/2 REAL units on each side, and by >= 2 INTEGER endpoint units before canonical clipping/P2 restrictions.
- Corollary X and X* are correctly classified **computer-assisted [W+F]**, not uniform written exclusions of the reported class lists.
- Both reviews found the shared profile/seed/hull/no-wrap/class-pass implementation sound over the reported small-prime computations. No current implementation weakens the written hypothesis there. Many over-enumerated profiles, ranges and pairs are conservative.
- Code carrying the class criteria: seedX2.py cdiv/classes/profiles/exact_seed/class_pass; seedXstar2.py shared-source load/bounds/class_pass. Coverage/labels additionally need region_SA/region_PA/main and map6.py's c4 dependencies.
- Reported finite additional exclusions: 756 X + 187 additional X* beyond 1,793 SA/PA, at primes 11,13,17,19,23,29,31. Remaining 378 OPENE classes split as 377 seed-pass/noC+ and 1 seed failure. These are modest finite results, no full NMH/MIX_DEF_HIGH/RUNS/PAR/INV/ordered-Olson conclusion.

## Verification, separated by verifier

- **My delta arithmetic (own code, no lane imports):** 1,380,480 SA/PA region instances over every arithmetic class at primes 5-31, no failure; six Claim E' memberships all pass; 144,000 off-by-one cases no r2-equivalence failure. Mutating m to region-low-end minus one makes 5,594/6,640 class/region cases fail; widening y-range by one makes 391/6,657 fail. This is ONLY my delta check's mutation suite.
- **My star spot-check (own code, exact fractions, no lane imports):** LF 2,675,225 class/weight tuples at primes 5-61, no mismatch; min relaxation 3/2 real / 2 integer per side. SCW-G* s>=3: 2,102,384 domain tuples at primes 5-17, no failure. QQ: 14,919,412 admissible weight-pair/m cases at primes 5-43, no P2/PIN failure. No mutation suite was run for this star spot-check.
- **Codex:** self-reports 31,878 LF tuples and 386,412 term-bound domain tuples at p=5,7,11,13; no pinned claimant code imported/executed. I did not replay its transient checks.
- **Claude:** prompt-only, no tools. Hand derivations and receipt arithmetic only; no executable verifier or mutation controls. Its controls section describes claimant MODE receipts, not Claude-executed tests.

## Unknowns / limits

- No claimant code was run by me or either reviewer. Tables reconcile to pinned receipts, but the computer-assisted class enumerations were not independently replayed in this assignment.
- map6.py execs **unpinned** c4/ind_star3.py and c4/ind_star_ex.py. The label partition cannot be independently reproduced from this snapshot alone.
- Execution-time hashes for the claimant's exec-ed sources are absent. Pin/freeze consistency now does not close that provenance gap.
- No external novelty/priority search was performed. No firstness claim.
- No lane changes applied; all required fixes remain for the owner. Both dispositions are conditional ACCEPT-WITH-FIXES.

## Exact artifacts and hashes

Machine receipt: `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6g-r2-review-result-v1.json`
sha256 `0caed8e66cd69dd5a4238004bbf45f6f62cd6204048956603fc85884810f07a7`.

| artifact | sha256 |
|---|---|
| /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6g-r2-parent-inputs-v1/manifest.json | 165f4f0e21efa2e4fbd0794056a8fd80fc51c91a27251de1019dfa6207e0e48e |
| /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6g-r2-delta-v1/diff.txt | dd9803eb3b80432cf290b2332f600c286544c2823df451555f2650f5dde07b29 |
| /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6g-r2-delta-v1/receipt.json | 4c0140435382b4fee70e20114eb8c7aea93baf330b850e3eca01603e9cc2934a |
| /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6g-r2-delta-v1/delta-check-v2.md (authoritative) | 0d8898242666018636704e8568e4ae91f0c37ef7951b3dc22f0eaceb4e389998 |
| /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6g-r2-delta-v1/delta-check.md (superseded typo) | 26295f16632b58bf67e2bef3f99cf92711ffe139baaaeaf7e94193b25d556707 |
| /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6g-r2-delta-v1/delta_arith_check.py | 5b5db3274c0147d615cea4dfcfcc06d7c65f0623b5c2cd041b71087002e67dc8 |
| /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6g-r2-delta-v1/arith-check.json | 3d828ce3f398d41ac1aa53c30d143623b35c26318970b90a588781c977163432 |
| /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6g-r2-star-parent-arith-v1/star_arith_check.py | 8a98382adca1345c191d8f2eb5c6ad08a8751cc8a2f0ed5f1cb153ad456234e9 |
| /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6g-r2-star-parent-arith-v1/arith-check.json | 43278160b63c14595056dd220a46f68a9b42c923440cee0fc713ad0cca57bc2e |
| /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6g-r2-star-codex-review-v1.note.md | ae6d66828117fd81863ba1c99d36f9db2126cba4f826ac5a11f75be4921371d3 |
| /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-c6g-r2-star-claude-review-v1.note.md | 4e55c8cc34b53d2d995c6f28a7379417015a8beaecc7e5f43c967244dd023f41 |

Full inventory (including all pinned inputs, both prompts, reviewer logs/receipts) is `olson-c6g-r2-created-files-v1.json` in REVIEW. Empty tmp/ dir is inside olson-c6g-r2-delta-v1.

## Deviations / own errors (preserved, not hidden)

- Snapshot root was created with exist_ok=False and every file x/xb; nested parent directories used os.makedirs(..., exist_ok=True), contrary to the literal directory-creation rule. They are all inside the exclusively created snapshot. No pre-existing file was overwritten.
- Initial delta-check.md typo: cls line 41 instead of 35, preserved. delta-check-v2.md supersedes it.
- Codex prompt abbreviation suffix typo: 2b22 instead of f5b22. Full task/manifest hashes correct and Codex verified the named bytes (its m4).
- Some read-only inspection used shell ls/grep/awk/cut/cat instead of specialized file tools, and bash cd instead of cwd. No file mutation resulted from those inspections.
