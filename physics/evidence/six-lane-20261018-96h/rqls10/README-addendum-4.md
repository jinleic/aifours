# rqls10 lane README, addendum 4 (navigation; successor worker ContinueRQLS10b)

Recorded 2026-10-19T07:31:24-0700 (from /bin/date). Extends README-addendum-3.md. Target 1-RQLS(10) OPEN / UNKNOWN;
no candidate; no run since 05:07. All files below are 0444 unless marked DRAFT (unfrozen, uncited, never run).

## Owned supervisor lineage (all written only, never run; parent HOLD on launches)
- code/owned_supervisor_v7.py a45f8538d86cf021a04d816fad9c5ac2392cac016b286bedb9dcb64ad8f8d2fa - Codex HOLD
  RUN/review/rqls10-owned-supervisor-v7-source-codex-v1.prompt.stdout.txt (bf682151...3a62); disposition of the v5
  review: review/rqls10-owned-supervisor-v7-disposition-v1.json 8ea83d33...4f8a; diff v5->v7 d56d32f8...e7ee.
- review/owned_supervisor_v8-pending-items-v1.md 3b982c6f...71b4 (folded into v8).
- code/owned_supervisor_v8.py 472fddf9...27a3 - superseded (removed /bin/date; parent objection, D-17); disposition
  review/rqls10-owned-supervisor-v8-disposition-v1.json f5e08a87...26b1; diffs v7->v8 bd1e366e...4158, v5->v8 7fd79331...095.
- code/owned_supervisor_v9.py c7674b907a37297cc35758ce994983b5b6878c07f994b387225e422a3283a1cd - CURRENT, routed to
  Codex by the parent (freeze RUN/review/rqls10-owned-supervisor-v9-source-review-freeze-v1.json); disposition
  review/rqls10-owned-supervisor-v9-disposition-v1.json 7d1037b0...25cb1; diffs v8->v9 0fda417e...a80e, v7->v9
  b8733488...8680, v5->v9 6992227779...4d48.

## Guard qualification
- plan v3 a6f2e0a5... and plan v4 1de3fce1...9ebca (with child v4/v5, configs v3/v4, checker v3/v4): superseded, never
  used (busy3 over the lane limit; Codex HOLD on v4: RUN/review/rqls10-guard-qualification-v4-codex-v1.prompt.stdout.txt).
- Package v5 DRAFTS against v9 (unfrozen until the v9 source findings return; snapshot sha256 at 07:31):
  code/guard_qual_child_v6.py 81421448...d7ea, code/guard_qual_configs_v5.py e6396db6...0c63,
  code/guard_qual_check_v5.py cbab55c5...984d, evidence/owned_supervisor_v9-guard-qualification-plan-v5.md
  4982587f...f784, review/rqls10-guard-qualification-v5-disposition-v1.json 8ffa93da...9491.

## Fixed-B assay and Q1 checker (review on hold until the supervisor API is pinned)
- code/rqls_fixedb_lm_v7.py 4a78a7a0...df07 and code/fixedb_q1_check_v5.py 4cb5495a...62f9 (Codex v6 findings;
  disposition review/rqls10-fixedB-v7-disposition-v1.json 76fe4fb0...d9bc; diffs v6->v7 6cad2206...927e,
  checker v4->v5 4e29cba1...6b66). The checker v5 latency criterion must be re-based on the parent-captured
  post_publish_mono (v9 summary) before any Q1 (review/owned_supervisor_v8-pending-items-v1.md, P1).

## FCO
- evidence/fourier-co-ansatz-v1-addendum-4.md 40c9b2b4...05fa cites the parent-accepted Proposition FCO-2p (no FCO
  solution for n = 2p); no further FCO enumeration planned (parent, 07:1x); code/fco_candidate_verify_v1.py frozen/unrun.

## Records
Checkpoints 023 (6d47cf4d...8e4e), 024 (1ff66500...f368), 025 (29f4e26e...6d1); deviations v6 (a8c34dff...1aa3),
v7 (28bf2aeb...f871), v8 (2601b1a8...f331); public XNU sources for citations in lane tmp/ (0444, sha256 in the v7
disposition).
