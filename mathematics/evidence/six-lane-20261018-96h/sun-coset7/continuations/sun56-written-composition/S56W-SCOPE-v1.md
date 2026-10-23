# S56W-SCOPE-v1 — written Sun(5)/Sun(6) import-replacement composition [target only; no claim]

- **Written:** `/bin/date` read at 2026-10-19T17:52:11-0700, immediately before this exclusive create (directory created empty just before).
  Owner SunM13MixedFibres, slot math-1. First `/bin/date` of this slice: 2026-10-19T17:51:04-0700.
- **Authority:** `RUN/control/written-sun56-import-cutover-and-E2-closure-v1.json`, sha256
  e1317e565a1c6218dbd594ec6530f76080a41d9fefab559e8639b60578990193, key "math1" (RUN = /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h).
  Pins: H5 = C5W (`../core5-written-bridge/C5W-v1.md`, 2e4b42b2ce88cad9f13b56b027fb10ea1082fb3d20df8acbbdff5667d4db5c69) and
  H6 = C56W (`../core6-written-bridge/C56W-v1.md`, 63cbcdb1cc3b8620a9f16207a1a6a7ed99b898568c59af549c6a73592263f8b1), both UNREVIEWED.

## 1. Frozen target
A composition S56W containing, in full written form: (a) R0 (finite-core reduction); (b) the Sun(5) reduction R1 of
O16/sun-coset5/proof-v4.md section 2 with every step of Prop 4.5 and every rules-v1 lemma it uses (L0.x, L1-L3), read with
every mandatory item of rules-v1-erratum-v3; (c) the Sun(6) reduction R1(6) at its accepted literal scope (with any
mandatory k6 errata); (d) two theorems with statements IDENTICAL to the accepted Sun(5) and Sun(6) statements (all groups,
possibly equal subgroups, no cover assumption), proved CONDITIONALLY on the explicit unreviewed hypotheses H5 (Core(5)) and
H6 (Core5(6)); (e) a full DAG: (classical Sun(2)/(3)/(4) + H5) -> Sun(5); (classical + written Prop 4.5 + H5 + H6) -> Sun(6);
(f) an audit of every load-bearing statement and import for old computational dependency or circularity; (g) exact rules
for how future Sun(7) texts may substitute these identical statements without re-labelling the old computer-assisted
proofs. No minimal-counterexample frame unless explicitly justified; all index cofactors and equal-subgroup cases carried.

## 2. Premise discipline
Allowed: elementary group facts; Sun(2) (re-proved); Zhu Thm 1.1 (k = 3, 4) as a classical external import; the written
reductions and Prop 4.5 with their written lemmas (re-derived here); H5, H6 ONLY as labelled hypotheses. Not premises: the
accepted Sun(5)/Sun(6) theorems or verdicts as mathematical inputs; any engine, checker, certificate, orbit/leaf count;
the minimal frames of proof-v4 section 3 or the k6 README; Gong; M-S Lemma 4.6; Menon. No claim that H5/H6 are accepted,
no claim that the old proofs became computation-free, no novelty (k5 claimed by Gong; k6 remains as locally accepted).

## 3. Outcome
Complete conditional composition with DAG/audit, or the exact gap (statement, line, missing authority).

## 4. Prior exposure (disclosed)
Already read in this session: proof-v4.md (all 278 lines); rules-v1-erratum-v3.md (all 18 lines); Sun(5) verdict
(2cf02436…5301) lines 1-35; Sun(6) verdict (efe1d849…1e29) lines 1-30; sun-coset6/README.md (10fc493e…e2bf) lines 20-60
(R0, R1(6) marked "[NEW; ... not yet hostile-reviewed]", minimal frame, pattern definitions); my own C5W, C56W, KII-W,
K52-W; the K7-lane LFC/INV record. NOT yet read: sun-coset5/rules-v1.md (L0.x, L1-L3 statements and proofs);
rules-v1-erratum v1/v2; the remaining README lines; proof-k6-v3.md; rules-k6 files; rules-k6-erratum-v3.md;
proof-k6-lemmas-v1.md. These will be read after this freeze, only for the literal statements/proofs and mandatory errata.
**Pre-freeze sketch:** none beyond the DAG shape stated in the authority.

## 5. Deliverables and governance
`S56W-v1.md`, `review-package-S56W-v1.md`, `review-excerpts-S56W-v1.json` ({path, sha256, start, end}), checkpoints
<= 1800 s apart (target 1200 s), IRC with paths/SHA256s, park. All files exclusive-create; old files immutable. Written-only:
no scientific scripts, assertions, enumeration, CLI or nested agents; metadata only. CANDIDATE_UNVERIFIED and CONDITIONAL.
