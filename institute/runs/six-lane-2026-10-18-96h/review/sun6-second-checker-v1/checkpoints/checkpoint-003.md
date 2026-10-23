# Sun6 second checker v1 - checkpoint 003

- Clock (/bin/date immediately before writing): 2026-10-19T17:32:42-0700
- Previous: checkpoints/checkpoint-002.md (abb2e8278aa077532c5ca481657f25f0581277567de0820f2d6f69dbf5792c0e).

## Claim
None (source authoring only; nothing executed, compiled or tested).

## Actual result since checkpoint 002
- Wrote complete checker `code/sun6_second_checker_v1.py` (sha256 1a092d0c1eca40f1939e83ebf1ddaac02cf7888c1d83601ae20450efd7bd704f); ast.parse only.
- Froze `CONTROLS-PLAN-v1.json` (sha256 42cd627528121b3a26ce886514b4cc24b0ec33ac83ee8f75fe11768b4563b01b): 124 controls (7 T-table, 6 leaf-membership, 4 stabiliser, 4 orbit, 1 placement, 12 dual/maxgcd/hereditary, 7 P-bound, 3 forced-pair/column, 6 fgcd, 30 synthetic records, 17 pinned-line mutations, 7 coverage, 16 pipeline/lifecycle, 4 publication). All expectations hand-derived from the written rules except the three real-data positives C01/DR1/DP1 (inherited from the accepted replay, labelled as such).
- Wrote harness `code/sun6_second_checker_controls_v1.py` (sha256 ef47979132296fd5a4bfc45fe2c1d130e1b2fefd5d033b72404c71af2a0869d3) that pins checker+plan hashes and executes exactly the hashed checker bytes; mutations in memory only.
- Notable derivation: with t_a = t_b = 1 in distinct cosets, no vertex can take t = 5 in FH5, so the E5 placement can never change an FH5 outcome here; all 7 placements are still searched as the format requires, and SAT5 is exercised by unit control G01.

## Blocker
None.

## Next bounded action
Write MATH-BRIDGE-v1.md (every-rule source map + saturation/marker bounds + least-order frame + literal Sun5 dependency), INPUT-PINS-v1.json, RESOURCE-LIFECYCLE-PLAN-v1.json, READLOG-v1.json, SOURCE-REVIEW-PACKET-v1.md and SHA256SUMS-v1.txt.
