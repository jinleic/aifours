# PA19 structural route (plan item 2): frozen scope note v1

written_after_host_clock: 2026-10-19T13:13:39-0700 · author: ContinuePA19d (info-1 slot) · status: SCOPE FROZEN BEFORE DERIVATION

## Authority and boundary
- Parent IRC 2026-10-19 12:59:44 (Main): all six v8/v36 reviews HOLD; no P9/D37/test10; do not touch any runner/test file. NEW ASSIGNMENT: plan item 2 structural route, written only. Parent join file `RUN/review/pa19-v8-v36-six-review-parent-HOLD-v1.json` (e306dcc2255f8a8a6d61dcba2b34ab08186861e068279c1fbc8415d3330bc89b).
- README plan item 2 (README.md line 43, sha 75c02890…): "look for definition-level counting lemmas beyond GPS that cut whole ms09/ms06 skeleton cases, as b3/b30/b44 did". Its "frozen <=300 s stdlib probes" clause is SUPERSEDED by the parent: NO probes, scripts, solvers, encoders or any execution.

## Frozen target
A definition-level counting lemma, beyond GPS-1/GPS-2 and the accepted ms09 b3/b30/b44 exclusions, that excludes WHOLE named skeleton cases of the frozen frontier `evidence/probes/frontier-v1.json` (0e7e4370961ea8713f8549576a3973c661c1b6499f8a345c74be97d0b4216a46): ms09 b in {4..29, 31..43, 45..70} (65 cases, entries at lines 3223..5708) and the 86 ms06 cases listed there. Primary family: ms09 (five P0 columns (4,3,3,3,3,3), three P1 columns (4,4,3,3,3,2), L = 0), because 5*21 + 3*22 = 171 = C(19,2) makes every counting identity exact. ms06 only if a lemma transfers; no ms06 claim otherwise.

Candidate families (from README item 2 and the parent): (F1) P0-triple empty-partner demand; (F2) P1-quad T-disjoint capacity; (F3) pair-block demand; (F4) pair counting inside row classes with T contained in a fixed column set (in particular the empty rows), with per-row incidence identities. Lemmas may combine these. Every lemma is stated for all ms09 skeletons and proved from definitions only; it is then applied to explicitly named cases.

## Premises allowed
1. Problem definition: a 19x8 array over 6 symbols in which any two rows agree in at most one column.
2. Skeleton bytes: `OLD/cycle2/skel-b/skeletons-b-ms09.json` (7c46ebbad3389476407e99807593287a8b3bb6c6a80f34574f0e9c00134293d0; one physical line, cited by byte offsets) and the identical per-case copies in frontier-v1.json (cited by line ranges).
3. Skeleton semantics (explicit bridge premise, stated in the proof note and checked against the bytes, not inferred by running code): profile list as in the file header; for each P0 column c the skeleton fixes the 4-row quad Q_c; "types" lists T(r) = {c : r in Q_c} for the rows with t(r) >= 2; the other rows with t(r) = 1 are private rows and "empty" counts the rows with t(r) = 0; consistency: sum of t = 20 and the row total is 19. This is the semantics used by the accepted b3/b30/b44 proofs.
4. GPS-1/GPS-2 and b3/b30/b44 may be CITED only at their accepted scope (written necessity; the exact named cases). No GPS applied count, list coverage, solver or probe result is a premise.

## Method and deliverables
Written reasoning only. Tools are used only to read files, compute whole-file SHA-256, locate quoted byte/line ranges, and exclusive-create lane files. Deliverables: (1) this note; (2) proof note: statements, complete proofs, and the exact list of named frontier-v1 cases excluded, each with its quoted skeleton bytes, or, if none, the exact obstruction and the smallest missing lemma; (3) excerpt manifest {path, sha256, start, end}; (4) review package <= 100 KB; (5) checkpoints <= 1800 s apart.

## Claim boundary
No claim beyond the explicitly named cases. Level: written proof, not solver-checked, not Lean. Acceptance needs parent mathematical check and hostile review. No effect on any interval, list, queue or frontier count before parent disposition. PA(19,8,6) stays UNDECIDED unless every frontier case is closed.

## Pre-freeze sketch disclosure
Before this freeze I read README.md, notes/ms06-block-relaxation-lemmas-v2.md, cycle2 structural-ms09-b00003-proof.json, ms09-b30-b44-structural-candidate-v1.json, gps-proof-addendum-v1.md, the ms09 skeleton file, and the frontier-v1 ms09 b_index list. While reading I sketched mentally, without writing anything down: (a) for a row r the rows sharing no quad with r number 18 - 3t(r); for t(r) = 4 they are exactly the rows with T contained in the missing column, which forces e >= 3; for t(r) = 3 they number 9 and force e >= 2. These exclude ms09 b1 and b2, which are NOT in frontier-v1 (already closed), and they do not exclude the frontier cases b6, b7, b8, b14. (b) Counting pairs of empty rows over all non-quad blocks: C(e,2) must equal sum C(eps,2) over P0 triples, P1 quads and P1 triples; a convexity lower bound appeared to fail for e >= 8, that is for b67, b69 and b70, with slack 1 at e = 7. No exclusion is claimed by this note. Item (b) is derived and checked in the proof note.
