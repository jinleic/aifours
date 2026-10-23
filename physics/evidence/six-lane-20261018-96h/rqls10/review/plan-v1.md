# rqls10 continuation: frozen target, baseline and initial plan (v1)

Recorded 2026-10-18T23:25:48-0700 (from /bin/date). Lane `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/rqls10`.
Owner: ContinueRQLS10, a Claude subagent of Main (worker model as declared by the harness: anthropic/claude-opus-5-5;
not a runtime receipt). Parent runtime as declared by parent: openai-codex/gpt-6-astra (parent correction v2).
Controls: run contract sha256 55baff0cf1ac1a4b0ab38b0eb1b1fa5a35a47c890f352b79dae4dfea919ffcaa; worker contract
sha256 ef76faefc90f6bdbe4544d3ccf4e7b29e6a2c172f2d8ea0bbb793af16b185f83; launch tightening sha256
8ac556699352a42f3d97f83861039e21f57db0646da2f38391ee1f11e330aa20. STOP registry: review/stop-registry-v1.json.

## Target (unchanged from the old contract, no quantifier change)

Decide whether a maximal-cardinality 1-RQLS(10) exists (Zhang-Cao arXiv:2608.29201v2, Def. 1.1, Thm 1.3; order 10
is a named exception). Concretely, MAX10(B,q):
1. q = (q_ij), i,j in [10], unit vectors in C^10; every row and every column is an orthonormal basis;
2. B is a Latin square of order 10; each class T_s = {(i,j): B(i,j) = s} is an orthonormal basis;
3. the 100 vectors are pairwise nonparallel (distinct modulo global phase).

Positive gate: an exact witness (B and all 100 vectors in a stated exact number field) passing a definition-level
exact checker, independent second checker, mutation controls, producer replay, hostile reviews, primary comparison.
Negative gate: nonexistence for arbitrary complex vectors and every Latin square B. Restricted-family exclusions,
failed searches and numerics are UNKNOWN for the target. Correctness, priority and significance stay separate.

Status at start: OPEN / UNKNOWN. No candidate.

## Baseline (inherited, read-only, hashes checked 2026-10-18)

- Old contract screening/phys-2-rqls10-contract.json sha256 0adc1f92552936f8dbbaa5dcdc82a92c9a8aac32bd40481d835ab0c180750f16;
  priority audit sha256 bdf48cd2a7e42ad6f915f719a879bfbc7e5eecd0602bbdbfc77a69f1af910dfd (NONE_FOUND_IN_SCOPE);
  pre-check sha256 4c62b2435ae08d8ce26b8554afceedf47b60891d41f561f69a6a18df4354aec5.
- Old lane summary sha256 1bb1596182f1be6d66de937b6974353a2dd0f3366ed5b5a7347d489137a9c73f (pinned in the run's
  prior-evidence manifest); README 05a30452...; representation-v1 de4b30b3...; restricted-results-v1 4ccf86cd...;
  addenda 1-7: 7ee05dd2..., 5bebfb32..., 61bee974..., 589a62a2..., 30326860..., b6022794..., 1aad0ee5...;
  exact_rqls_checker_v1.py 90aaf3be...
- Primary source re-fetched into sources/: zhang-cao-2608.29201v2.eprint.tar.gz sha256
  127bef1882685dcaa03927f9e64ac27a71c14a468d26fcb22368f138eb7d21b6 (identical to the old lane pin).
  Its constructions: Z_2 x Z_m complete mappings (v = 0 mod 4), Huang-Li odd orders, singular direct product
  v = mn + h needing maximal 1-RQLS(m) and 1-RQLS(m+1) with m >= 3 (no admissible (m,n,h) for 10), and v = 90.
- Old computation: one float probe (UNKNOWN, DISK_FLOOR, weak G8 control), one exact Paley sample (2000/2000, no
  orthonormal transversal; sampled UNKNOWN). Not repeated here.

## Initial plan (bounded obligations, in order)

W1 (written). Re-derive the load-bearing restricted results R1-R10 and addenda 3, 5, 7, record VALID/DEFECT per item.
W2 (written). New representation, materially different from the old Z_10 / Paley / half-split families:
   cyclic quasi-difference ansatze Z_n + h (n + h = 10): a cyclic group Z_n acting on rows, columns and symbols with
   h fixed points each, and a unitary U on C^10 with q_(g.p) = U q_p. Derive the eigen-multiplicity forcing lemmas
   (corner lemma), the reduced block equations, and exclude impossible (n,h) exactly.
W3 (exact anchors, <=300 s stdlib). Classical Parker-type Z_7 + 3 Latin square bookkeeping control; reduced-equation
   identities checked on exactly known configurations.
W4 (numerical assay, needs item GO). Frozen divide-and-concur (RRR) feasibility solver with controls v = 6
   (negative: no 1-RQLS(6)), v = 7 and v = 8 (maximal 1-RQLS known to exist); targets: Z_7 + 3 and Z_9 + 1 reduced
   systems over enumerated B-data, and unsymmetric fixed-B runs (Parker-type B, Cay(D_5), Cay(Z_10)). Any lead is
   polished at high precision and passed to exact recognition and the exact checker. A miss is UNKNOWN.
W5 (primary applicability). Huang-Li arXiv:2606.27758 odd-order construction, Ball-Simoens arXiv:2607.12933
   template, the maximal QLS(10) constructions, and the newly exposed listing, focused on order-10 resolvability.

Stopping rule for each obligation: deliver the written result or the frozen GO request; then continue with the next.
