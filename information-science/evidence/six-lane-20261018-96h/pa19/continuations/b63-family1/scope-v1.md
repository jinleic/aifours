# PA19 ms09 b63 residual family 1: frozen scope and exposure v1

Frozen after host clock 2026-10-19T21:45:18-0700 by ContinuePA19d (info-1), BEFORE any written derivation in this directory.

## Authority
RUN/control/written-PA19-b63-family1-transition-v1.json, SHA256 a6addf8f869e4bf6f1ed6d37bb9a15f383e47f2a37a034ddf87e1b46d6c12851 (RUN=/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h). Target: resolve residual b63 family 1 under its exact frozen-case identity and every eligible empty-row/identity placement; keep earlier class/b63/families-4/5 candidates unaccepted; prove needed ingredients or state conditional hypotheses; full exclusion or exact remaining obstructions; no count gain, no PA19 solution; no scripts/assertions over scientific data.

## Exact binding (read first)
- Case: S=/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19/cycle2/skel-b/skeletons-b-ms09.json, SHA256 7c46ebbad3389476407e99807593287a8b3bb6c6a80f34574f0e9c00134293d0; b_index 63 = zero-based half-open bytes [4256,4338), entry SHA256 6b03eb8ad5a5d05c6486cd04656e444f051a2a6677a136759c9cbf2e22149a6a: {"types": [[0, 1, 2], [0, 4], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], "empty": 7}.
- Current status snapshot: RUN/review/pa19-parent-frontier-v11.json SHA256 f4fe5001153ed75507c136a7d65b3346b654dec998f1ce00aa15799a3c917a27 (b_index 63 at line 4694; current counts total 128 at lines 4958-4961). Status binding only.
- Frozen family partition: /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/pa19/continuations/ms09-class-extension/b63-reduction-v1.md, SHA256 6be58b9a82078ac9ed8df4fa4dc80d86ea91038b65885416087b05ef3a5c2aa9, line 38 item 1: "G1 with B/C pairs {13-24,14-23}", where G1 (line 15) means: g={0,1,2} has P1 pattern (n2,n3,n4)=(1,2,0). Interpretation frozen here: family 1 = every b63-class array in which g lies in exactly one P1 pair block and two P1 triples, and the two P1 pair blocks NOT containing g are {13,24} and {14,23} (row 04 in no pair). Both column orders of those two pairs are included. Labels 04,13,14,23,24,34 denote the listed two-type ROWS; p0,p0' the two distinct type-{0} private rows; p1,p2,p3 the other private rows; seven distinct empty rows.

## Premises and non-imports
Only the b63 row model (S entry + encoder membership semantics: listed types, then 4-deg(c) private rows per index, then empty rows; P0 column c has size-4 class Q_c = rows whose type contains c; P0 profile (4,3,3,3,3,3), P1 profile (4,4,3,3,3,2)) and elementary counting. NOT imported as facts: class-theorem-v1, b63-reduction-v1 (B1-B9), families 4/5 proofs, e7 dossier. Every ingredient (exact pair cover, row patterns, occupancy categories, I(r)=7, rescue lemmas, G1 consequences) will be re-proved in this directory. The parent-accepted b65 verdict (RUN/review/pa19-b65-parent-verdict-v1.md SHA256 46bc640ca77c75ea7afa65a6d6f289e2054f0878b055a8f5b2fea621791fc9fd) concerns a different case and is not used.
Planned normalization: the symmetry 1<->2 (13<->23, 14<->24, p1<->p2; fixes g,04,34,p0,p0',p3) swaps the two pairs, so the column order of the pairs may be fixed once the columns are named by g's blocks; this will be stated explicitly.

## Exposure disclosure
I authored b63-reduction-v1.md (B1-B3 contain the G1 split, the matching list and a p3 incidence fact), families 4/5 and the class theorem, so the G1 facts are known to me; they will be re-derived, not cited. A prior in-session attempt at this slot (after reading the transition at 21:08) exceeded the output limit and was discarded unseen; nothing from it is recorded or relied on. No family-1 derivation has been written.

## Outcomes and bounds
(i) whole-family written exclusion; (ii) exact remaining obstruction list. Written only; metadata hashes/ranges only; exclusive-create in this directory; checkpoints <=1800 s (target 1200); packet <=100 KB. No frontier/count change; b63 and PA(19,8,6) remain UNDECIDED regardless.
