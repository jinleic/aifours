# PA19 ms09 class extension of the b65 mechanism: frozen scope and exposure v1

Frozen after host clock 2026-10-19T17:25:56-0700 by ContinuePA19d (info-1), BEFORE any written derivation in this directory.

## Authority and inputs
- Transition: /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/control/written-slot-transition-pa19-20261019-1718-v1.json, SHA256 76f00a6908c2f1e0599a75ce38179ffb1ef4633eb1094d4f4c32a7eb1033ebaa (rules: written only; NO scripts, assertions, enumeration or CLI over scientific data; hash/byte-range metadata only; all files x; checkpoints <=1800 s, target 1200; <=100 KB packet; no frontier/ledger mutation; park).
- S = /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19/cycle2/skel-b/skeletons-b-ms09.json, SHA256 7c46ebbad3389476407e99807593287a8b3bb6c6a80f34574f0e9c00134293d0 (4977 bytes, one physical line).
- V = /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/pa19-parent-frontier-v10.json, SHA256 29c7cbe8e22cdad3bb1d196f9df12d9336652cb4942dc9538ac6d22225ebd90a. Its ms09_undecided list (lines 2662-4938) has exactly 59 b_index values: 4,6,7,8,10-29,31-43,45-58,60-66,68 (line numbers of each b_index recorded later).
- Previous candidate (NOT a premise): ms09-b65-completion/proof-v1.md, SHA256 80241121fe3e97e46e446e96cd7ca83c90fd80001f67fd444749718e107b43f0 (Codex PASS 0F/0M/1m per parent IRC; Claude pending).

## Class hypotheses H (frozen)
Setting: the ms09 row model of S/encoder bridge: profiles P0 (4,3,3,3,3,3) x5, P1 (4,4,3,3,3,2) x3; each listed type is one row; for each P0 index c there are 4-deg(c) private rows of type {c}; e empty rows; 19 rows; Q_c = rows whose type contains c.
- H1: e = 7.
- H2: some listed type g has exactly three indices, and the two-element complement of g is NOT a listed type.
Claimed class theorem (to be proved in full, re-deriving every b65 step used): no array exists for any type data satisfying the ms09 setting and H1-H2. Per-case decision order: H1, then H2. The class statement does not use S, V, solver or list facts.

## Selection rule for the nearest-case exclusion (frozen BEFORE derivation)
Candidates: the 58 v10-undecided ms09 cases other than b65. Order lexicographically by (1) |e-7| (the excess regime driving every b65 step); (2) Delta = minimum over the 120 permutations of P0 indices of the symmetric difference between the case's type set and b65's type set; (3) smallest b_index. The selected case gets a complete written exclusion attempt; if not completed, the exact surviving obligation is reported, never a closure.

Application (by hand, recorded now): e=7 candidates are b63, b66, b68. b63 = b65 with {0,3} replaced by {3,4}: Delta=2 (Delta=0 impossible: degree sequences differ). b66 and b68 have no 3-type and eight 2-types: Delta=3. Selected case: **b63** (S bytes [4256,4338)).

## Exposure disclosure (before this freeze)
1. In this session I read all of S raw (as context for the b65 slot) and the V b65 entry; I wrote the e7 dossier (manifest 8773ac59...6d88ba) containing b63 partial reductions (G1/T2 with two unmatched-type orbits; G2 with C0/Q1); those are context only and must be re-derived if used.
2. Between the parent IRC (about 17:18) and this freeze, unrecorded in-session reasoning already: (a) sketched that H1-H2 force either an immediate contradiction or exactly the b65 type list up to P0 relabelling (unreviewed; to be written in full); (b) computed by hand all 71 entry byte ranges from text lengths (entry length = 23 + 3*(total type size) + 2*(number of types); separator 2 bytes; first entry at 433), matching all eight previously hashed anchors b59,b63,b65-b70; (c) read by hand the e values and 3-types of the 59 cases: only b63,b65,b66,b68 have e=7; only b65 satisfies H (b63 fails H2 because {3,4} is listed; b66,b68 have no 3-type; all others fail H1); (d) computed alternative-metric facts: under the UNWEIGHTED metric Delta+|e-7|, b58 (e=6; b65 minus one 2-type up to relabelling) ties b63 at 2, and b61,b64 score 3. The frozen lexicographic rule selects b63; b58 is disclosed as the nearest e=6 case.
3. No derivation of the b63 exclusion beyond the e7 dossier statements has been made yet.

## Deliverables and bounds
Class theorem + proof; per-case table for all 59 cases (b_index, V line, S byte range, entry SHA256 via hash metadata, e, H decision/first failing hypothesis); complete written b63 exclusion or exact surviving obligation; interface map; manifest; <=100 KB packet; SHA256 receipt; checkpoints. No scientific computation, enumeration, script, assertion or model CLI; byte extraction and SHA256 only as metadata. Exclusive-create in this directory only. No frontier/count mutation; PA(19,8,6) stays UNDECIDED.
