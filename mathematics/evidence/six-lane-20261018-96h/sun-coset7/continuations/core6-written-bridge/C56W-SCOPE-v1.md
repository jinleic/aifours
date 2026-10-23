# C56W-SCOPE-v1 — direct written Core5(6) proof [target only; no claim]

- **Written:** `/bin/date` read at 2026-10-19T17:44:45-0700, immediately before this exclusive create (directory created empty just before).
  Owner SunM13MixedFibres, slot math-1. First `/bin/date` of this slice: 2026-10-19T17:44:16-0700.
- **Authority:** `RUN/control/written-slot-transitions-core6-corner-sigma-v1.json`, sha256
  7ff16d5b5b312bb3ca65206cb84f73331ccf3cd7b71cc7f0753687f1e2da26ec, key "math1" (RUN = /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h).
  Definition source named there: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset6/README.md
  (sha256 10fc493e5bf79f98fb805dc9e4b48becbf51fc7d7648848fa8874542dda5e2bf) lines 23-57 — NOT yet read; it will be read and
  quoted after this freeze, and the target below is adjusted only to match its literal wording.

## 1. Frozen target
**Theorem target C56W (Core5(6)).** No finite group admits six pairwise disjoint left cosets g_iU_i with [G:U_i] = 5 r_i and
the r_i pairwise coprime (equivalently: six disjoint cosets all of whose pairwise index gcds equal 5). Every independent
placement of the markers E2 (even r), E3 (3 | r), E5 (5 | r), every higher power of 2, r_i = 1 and unbounded cofactors are
included; no minimal-order frame unless explicitly stated and justified.

## 2. Premise discipline
- Allowed: elementary index/coset facts; R0; Sun(2) (re-proved); Zhu's Sun(3), Sun(4) at literal classical scope; the
  left-fibre count and actual inversion RE-PROVED inside the new file without assuming they suffice.
- Sun(5): only if needed, explicitly; C5W (2e4b42b2…5c69) is UNREVIEWED and may not be cited as accepted. If a Sun(5)
  instance is needed, either re-prove the needed lower-core step inline or disclose the computational import (accepted
  Sun(5) verdict 2cf02436…5301 is computer-assisted).
- NOT premises: any accepted Core5(6)/Sun(6) conclusion; any engine, checker, certificate, orbit/leaf count or survivor
  list of the k6 lane; Sun(6), Sun(7); pending candidates (C5W, KII-W, K52-W, K7-NF, A2X, SUN7-COMP).

## 3. Outcomes
(A) complete written proof with import DAG; or (B) exact surviving marker/multiplier regime plus every attempted argument;
never a restated computer bridge.

## 4. Prior exposure (disclosed; none is a premise)
- `R16/sun-coset6-parent-gate-verdict-v1.md` (efe1d849…1e29) lines 1-30, read earlier this session: exact Sun(6) theorem;
  proof composition v3 and cumulative erratum v3 names/hashes; CERT-FORMAT-k6-v3; parent derivation record; primary
  verifier checker_v2; the k6 contract's k5 dependency; certificate input files (run.json, orbits.jsonl.gz, rlp_duals.json,
  survivors.json) with byte sizes and hashes. No certificate, orbit, dual, code or proof text of the k6 lane was read.
- sun-coset7 README (R1(7) step 1 uses Sun(6) on six cosets with all pairwise gcd 5 — an instance of Core5(6));
  rules-k7-v1 (cites sun-coset6 proof-k6-lemmas-v1 section 1(b) for VFC (V3)); sun-coset5 proof-v4 and erratum v3 and the
  Sun(5) verdict (read for the C5W task); the K7-lane LFC/INV record; my own C5W, KII-W, K52-W candidates.
**Pre-freeze sketch:** none. Planned route only: at an apex v the five neighbours have labels r_j alpha_vj and masses
alpha_vj/5 with alpha in (1, 2, 3, 4); derive which rows survive a fibre count using Sun(2)-Sun(4) only (at most five pieces
per fibre, so a Sun(5) clause would be needed to constrain 5-sets), then use alpha + alpha* <= 5 and marker placement;
record every surviving regime exactly if the argument does not close.

## 5. Deliverables and governance
`C56W-v1.md`, `review-package-C56W-v1.md`, `review-excerpts-C56W-v1.json` ({path, sha256, start, end}), checkpoints
<= 1800 s apart (target 1200 s), IRC with paths/SHA256s, park. All files exclusive-create; old files immutable. Written-only:
no scientific scripts, assertions, enumeration, numerical checking, CLI, tests or nested agents. New claims
CANDIDATE_UNVERIFIED; no novelty, acceptance, Lean or human-review claim.
