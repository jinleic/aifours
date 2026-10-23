**DISPOSITION: GO-WITH-FIXES — nonblocking.** No BLOCKER or MAJOR found in the narrow delta.

**MINOR — generated reports name the wrong script directory.** [SOURCE03:404](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/m7-launch-v12-review-v1/snapshot/03-assemble_B_v12.py:404) and SOURCE03:489 still print `scripts/...`, although v12 executes and hashes `scripts-v12/`. **Repair:** derive the generator path and script prefix from `__file__` and `K.SCRIPTS`, relative to `K.DESK`.

The requested changes otherwise check out:

| Change | Static result |
|---|---|
| Unrounded age | SOURCE02:930–937 compares the unrounded value; rounding is only for recording. |
| Slots | SOURCE02:513–527, 651–664 and 704–715 implement ancestry attribution, legacy label mappings, target-slot exclusion and the unknown veto. Lane reservations, limits and the single-admitter rule remain intact. |
| Admission lock | SOURCE02:909–949 acquires before the final census and releases on refusal. SOURCE02:978–987 retains it through spawn and receipt creation, then schedules release after 90 seconds. |
| Route A | SOURCE06:88–124 matches SOURCE16’s composition: base → C311/G6 → lex generators in order → cuts. Counts progress **627398 → 627556 → 659168 → 897308**; output pins enforce `18583aab…2e5e`, header **107513/897308**. SOURCE04:369–417 checks the actual producer fields, including driver/delta, source cube and lex counts. Replay uses pinned kissat and parent drat-trim. |
| Script isolation | SOURCE04:82 selects bklib_v4’s own directory; the v12 execution paths use it. |

**Additional executable delta:** SOURCE04:339 and 372–374 also add an r6-delta dependency and driver/delta checks to existing **B_C311cuts**. This safely tightens provenance preflight; include it explicitly in the intended delta, or restrict those additions to route A.

**Replay proof acceptance is unchanged:** exact singleton statuses, required return codes, complete measured feeds, pinned CNF/binaries, and clean supervision remain required at SOURCE04:651–675, SOURCE05:340–351 and SOURCE03:257–287.

All **23 hashes and byte counts match**. Review used snapshot-only static reads and hashes; no code or tests were executed.