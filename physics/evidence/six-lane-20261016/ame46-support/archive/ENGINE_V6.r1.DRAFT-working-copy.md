# Engine v6 for the AME(4,6) support lane: v5 plus the Codex v5 delta fixes (r1)

Lane `physics/evidence/six-lane-20261016/ame46-support/`. Host clock PDT, 2026-10-17. Written once.
- No proof run has used v6. The parent decided at 16:2x that there will be no further proof runs in this target.
- v6 is frozen so that the engine state is documented.

## Files
- `code/large_t_joint6.py`: 37925573b9f2d167341df981b6fb9d7417235bf16f074e9c87fc922021d54a5d.
- `code/lratcheck_py2.py`: f2fdf57895686e6737c8487587e9a648464e240e7408eee7658fff285a215f8e.
- The CNF is identical to v5's, as specified exactly by `review/V4_PROOF_SCHEMA.r2.md`
  (ef692d9df4303b77a09b919abdd3e6bfb5f73661bbb03ccc92db73ac3f7c9309).

## Fixes (`review/ame46-v5-codex-delta-review-v1.note.md`)
| item | fix in v6 |
|---|---|
| M1 (schema pair order) | `review/V4_PROOF_SCHEMA.r2.md`; validated by `code/schema_regen_check.py`, 34/34 SHA matches |
| M2 (late guard trip) | `Guard6.settle()` stops and joins the watchdog thread before guard_tripped and the outcome are evaluated |
| m1 (W shape) | asserts six negative point literals and one common value pair {a, a′} for all three doubled pairs |
| m2 (recorded cardinality) | asserts \|Y\| = 2h + e with distinct points before blocking; otherwise UNKNOWN |
| m3 (exceptions) | build, solve, proof, checker and per-solution analysis failures are caught and give UNKNOWN |
| m4 (assert in checker) | `lratcheck_py2.py` raises explicitly; it is used by v6's `check_stream6` |

## Controls
`code/guard_smoke6.py` (a781f7e82e963ef2eb991198604b7be54e448ac70d3e9526b8c62df9e64a6aa4) →
`evidence/guard_smoke6.json` (94b7daad2fc80a58841491a41622ddfaa4f8dec282ac1e2ca18be365a4a31365), run 16:24:01–16:24:39,
all_required_true:
- **L1:** Pandya's state is SAT under base + J + W with the v6 assertions; the mutated N is UNSAT.
- **L2:** settle() joins the thread, and an early trip is reported.
- **L3:** Codex's mixed-pair replacement clause is rejected by v6 and accepted by v5.
- **L4:** an injected empty model gives UNKNOWN ("recorded Y has 0 points").
- **L5:** an injected checker startup failure gives UNKNOWN; a four-literal W clause is rejected.
- **L6:** checker-2 rejects a missing hint terminator, also with PYTHONOPTIMIZE=2.
- **L7:** v6 proof mode on the certified (30,0) gives EXCLUDED, with guard null and both streams verified.
