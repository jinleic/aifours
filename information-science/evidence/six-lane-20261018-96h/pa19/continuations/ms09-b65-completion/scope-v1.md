# PA19 ms09 b65 full joint completion: frozen scope v1

Frozen after host clock 2026-10-19T16:54:08-0700 by ContinuePA19d (info-1 slot), before any written derivation in this directory.

## Authority and target
Slot record: /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/control/six-slot-written-resumption-20261019-1603-v1.json (SHA256 ac09b46532a233c6d9ce1b227c3dffecee9655bd83413d96d3a403065a0ef0f8). Target, verbatim: "Resolve exact current b65 full joint P0/P1/empty-row completion obligation, or prove a necessary reduction plus exact surviving obligation. Re-derive any unreviewed e7 premise; no projection counted as full array; b63/b66/b68 and e2 expansion outside this slice."

## Exact case binding
- S = /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19/cycle2/skel-b/skeletons-b-ms09.json, SHA256 7c46ebbad3389476407e99807593287a8b3bb6c6a80f34574f0e9c00134293d0. b65 = zero-based half-open bytes [4421,4503), entry SHA256 010b2b819f60b937e449a6af5ab88b711709fcae840ff226bb14af0895b28818, verbatim: {"types": [[0, 1, 2], [0, 3], [0, 4], [1, 3], [1, 4], [2, 3], [2, 4]], "empty": 7}. Header bytes [0,433) give P0 profiles (4,3,3,3,3,3) x5, P1 profiles (4,4,3,3,3,2) x3, c0=5, L=0.
- Current parent frontier v10 /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/pa19-parent-frontier-v10.json, SHA256 29c7cbe8e22cdad3bb1d196f9df12d9336652cb4942dc9538ac6d22225ebd90a: b_index 65 at line 4789; current counts lines 4958-4961 (total 129). Binding is b_index + exact skeleton bytes + whole-file SHA, never the s-tag alias.
- Encoder E (read only) /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/pa19/code/vendor/encode_skel_b.py, SHA256 d0002e60d11ef5cba568309fde5b15e29280ca127bc0e6bb1f4d22929a5628e5, lines 3-8 and 77-99: membership semantics only.

## Quantifiers retained
Every 19x8 array over six symbols in which any two rows agree in at most one column, whose five P0 columns each have symbol-0 class exactly Q_c = {rows whose type contains c} and profile (4,3,3,3,3,3), and whose three P1 columns have profile (4,4,3,3,3,2); rows are the seven listed types, one private row p_c of type {c} for each c=0..4, and seven distinct empty rows. No placement list, interval, solver/DRAT status, GPS coverage, model review or frontier status is a premise.

## Premises and symmetries
Only the definitions above. Every needed e7 statement (exact pair cover, row patterns, single-excess categories, incidence/rescue lemmas, the four-vertex Petersen bound, b65 normal form, high/low quads, actual-empty graph) is re-derived inside the new proof; the e7 Codex PASS and parent erratum fc48075b are context, not premises. Accepted Theorems A/B are not needed. Permitted symmetries, each to be stated with its induced row map: S3 on indices {0,1,2}; simultaneous index 3<->4 with P1 A<->B; any permutation of the seven empty rows.

## Disclosure of prior sketches
1. My e7 dossier (manifest 8773ac590e8456b132fcbcf70c7b9558142328891f74d02d8af13111286d88ba) already contains b65 partial reductions (Q1 normal form, high/low quads, zero-triple relation, one displayed P0-incompatible branch).
2. Between reading this assignment (host clock 16:42:44) and this freeze, unrecorded in-session reasoning already sketched a CANDIDATE COMPLETE CONTRADICTION: forced actual-empty quad graph, P0 eps-1 empty bookkeeping for p3,p4,p1,p2, then a P0 column-3/column-4 empty-pair conflict. It is unreviewed. The written proof must re-verify every step; any gap found is reported as an exact surviving obligation, never silently closed.

## Admissible outcomes and bounds
(i) whole-case written exclusion of the b65 class; (ii) an explicit full array (would need independent checking); (iii) a necessary reduction plus exact surviving obligation. Written only: no computation, enumeration, solver, encoder, probe, test or model CLI; metadata reads/hashes only. Exclusive-create files only in this directory; review packet <=100000 bytes; checkpoints target 1200 s, max 1800 s. No frontier or count mutation (parent only), no b63/b66/b68 or e2 work. Global PA(19,8,6) stays UNDECIDED regardless of outcome.
