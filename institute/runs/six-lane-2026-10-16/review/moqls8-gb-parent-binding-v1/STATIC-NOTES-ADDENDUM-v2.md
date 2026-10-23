# Addendum v2 to STATIC-NOTES.md

Written 2026-10-18 07:40 PDT, before any v2 execution. `STATIC-NOTES.md` (sha256 `8c490600…75cf`) is unchanged
and still describes the GB reliance, the conventions and the controls. This addendum records only what changed in
v2, and why.

## Why v2 exists

The v1 pre-flight `receipts/SELFTEST.v1.json` (sha256 `157d7f5cf094f944513232fea2bade20ccfc737332512172c1c9c52b1c868b4e`)
ran at 07:36 PDT and failed.

- **What passed:** the pins, the GB source line and AST checks, and the flag-to-call mapping. The n=5 storage
  control also passed: 374912 clauses, 86301 vars and 6104417 B, byte-identical at segment sizes 64 KiB and
  16 MiB, with an identical name table, and the sorted-literal mutant was detected.
- **What failed:** gate (a) in the synthetic composition exercise. v1 required that no single-unit flip equal any
  of the 22 genuine hashes. That requirement is wrong. Some templates differ from another template in exactly one
  unit, for example:
  - P0-B1 and P1-B1 at row 6, coordinate 1;
  - P2-C3 and P2-C4 at row 2, coordinate 5.

  So such a flip correctly reproduces the other genuine formula.

The v1 scripts never ran a generation: `bind_gb_v1.py` is `7818a04f…33f0` and `launch_gb_v1.py` is `dcda4f42…0b2a`.
Both are kept unchanged.

## v2 changes

Only these change in v2 (the full diff is `v1 → v2` in `scripts/`):

- **Gate (a)** requires three things:
  - each of the 42 flips differs from its own formula;
  - the 42 flips are distinct;
  - the set of genuine formulas that a flip equals is exactly the set predicted from the composed pieces (same
    header and tail, identical unit list).

  Every observed equality is listed per formula.
- **The file and directory names** are now v2: `tmp/selftest-v2`, `tmp/gen-v2`, `tmp/launch-v2`,
  `GB-PRIMARY-MAP.v2.txt`, `receipts/SELFTEST.v2.json`, `receipts/CHILD-ABORT.v2.json`,
  `receipts/PRE-EXEC.v2.json`, `receipts/POST-EXEC.v2.json` and `receipts/bind_gb_v2.std{out,err}.log`.
- **The supersession record** is now part of the manifest, the selftest receipt and PRE-EXEC.
- **The selftest** also records the synthetic one-unit-neighbour equalities.

## Frozen v2 hashes (recorded before execution)

- `scripts/bind_gb_v2.py`: `188c88de64fa994ca7e212f8d1618da9a0eb3433e2e162a835139bbfa4985f51` (58883 B)
- `scripts/launch_gb_v2.py`: `93f3671791305ef4b5c171f0d78cd36f115e525e04aa8865f26fd9f166f3535d` (12295 B)
