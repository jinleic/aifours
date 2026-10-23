# Class extension: source bindings, premise map and review interface v1

Written after host clock 2026-10-19T17:50:45-0700 by ContinuePA19d. Slot authority: /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/control/written-slot-transition-pa19-20261019-1718-v1.json (SHA256 76f00a6908c2f1e0599a75ce38179ffb1ef4633eb1094d4f4c32a7eb1033ebaa). Scope frozen first: scope-v1.md (SHA256 27b13a5c19b9bc7dc885d7fc52030796dcacc53bff8dcf707c1f1d232fa7b269, 17:25:56).

## 1. Deliverables and claims
| file | claim | status |
|---|---|---|
| class-theorem-v1.md | Every ms09 type list with e=7 and a 3-type whose complementary pair is unlisted has no array (H1,H2) | CANDIDATE complete written proof; unreviewed |
| case-table-v1.md | H holds for exactly one of the 59 v10-undecided ms09 cases (b65); H covers no further case | by-hand decision with exact byte bindings |
| b63-reduction-v1.md (+ erratum v1) | Proven reductions B1-B9 for the rule-selected nearest case b63 and its exact surviving obligation | PARTIAL; b63 NOT excluded |
| entry-range-hash-metadata-v1.txt; v10-binding-lines-v1.txt | exact S byte-range bytes/SHA256 and exact V lines | metadata only |

## 2. Sources
- S = /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19/cycle2/skel-b/skeletons-b-ms09.json, SHA256 7c46ebbad3389476407e99807593287a8b3bb6c6a80f34574f0e9c00134293d0, 4977 bytes, one physical line. The packet embeds S in FULL, so every zero-based half-open range in case-table-v1.md can be checked by hand (header [0,433); entry k starts after entry k-1 plus the 2-byte separator ", ").
- V = /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/pa19-parent-frontier-v10.json, SHA256 29c7cbe8e22cdad3bb1d196f9df12d9336652cb4942dc9538ac6d22225ebd90a. ms09_undecided spans lines 2662-4938; the 59 b_index lines are embedded verbatim via v10-binding-lines-v1.txt. V is a status binding only; current counts ms06=70, ms09=59, total=129 are untouched.
- E = /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/pa19/code/vendor/encode_skel_b.py, SHA256 d0002e60d11ef5cba568309fde5b15e29280ca127bc0e6bb1f4d22929a5628e5. Lines 3-8 (bytes [114,507), SHA256 d2badacac8e8224914d82ed27f64ee212b0ec1d9d99ed4c3d4ed8488e28f9790) and 77-99 (bytes [3404,4286), SHA256 92f988ec1c8e36fbf50616e84c94847ca6ffd439c642bbaaba7bd891b7e94fe7) fix the row model (types, then 4-deg(c) private rows per index, then empty rows; symbol-0 class of P0 column c = rows whose type contains c). Embedded raw from the earlier exact excerpt files of ms09-b65-completion. No encoder execution, CNF, list, interval or solver output is a premise.

## 3. Premise map
- class-theorem-v1.md uses only its Section 0 setting (the row model above) and elementary counting. Section 1 (pair cover, row patterns for t=0..5, five categories, I(r)=7, L1 rescue, L2/L3 three-type lemmas) is proved there. Section 2 Steps A-G reduce H1-H2 to the b65 list (or an immediate contradiction). Sections 3-4 re-derive the b65 empty-row table, the M-graph matching (G), f(w)=5-deg_M(w), the O-to-E bijection and the column-4 contradiction. The pending b65 candidate (ms09-b65-completion/proof-v1.md, SHA256 80241121fe3e97e46e446e96cd7ca83c90fd80001f67fd444749718e107b43f0) is NOT a premise; the e7 dossier and accepted Theorems A/B are not used.
- case-table-v1.md uses S bytes and V lines only; decisions are read by hand: H1 fails for 55 cases (e from 1 to 6); b63 fails H2 because {3,4} is listed; b66 and b68 have no 3-type; b65 satisfies H.
- b63-reduction-v1.md uses class-theorem-v1.md Section 1 (same packet) and the b63 row model. B8 (spread lemma) and B9 (normal form of one subcase) are new; nothing is imported from the e7 dossier.

## 4. Selection-rule interface
The scope froze, before derivation, the lexicographic rule (|e-7|, minimal P0-relabelled type symmetric difference Delta, b_index) and its application: b63 (Delta=2) over b66,b68 (Delta=3). The scope also disclosed that the unweighted metric Delta+|e-7| ties b58 (e=6) with b63. The rule was applied unchanged.

## 5. Verification boundary and deviations
Metadata-only operations: file reads, SHA256 via shasum, dd byte-range extraction, sed line extraction at explicitly listed line numbers, byte/line counts. No scientific script, assertion, enumeration, solver, encoder, model CLI, import, compile, test or Lean check. All files exclusive-created in this directory. Deviations: (1) scope discloses pre-freeze in-session sketches (class reduction, byte ranges, selection metrics); (2) b63-reduction-v1.md has an unverified header clock (18:03:00), corrected by b63-reduction-v1-erratum-v1.md (actual creation between 17:43:22 and 17:49:11); (3) the frozen rule's target b63 was NOT completely excluded: the deliverable is an honest partial reduction plus exact surviving obligation. Independent parent checking and both-family hostile review are required for the class theorem. No ledger mutation; PA(19,8,6) remains UNDECIDED; runtime HOLDs unchanged.
