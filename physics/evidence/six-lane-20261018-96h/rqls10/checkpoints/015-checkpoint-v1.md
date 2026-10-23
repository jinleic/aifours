# Checkpoint 015 (rqls10 continuation, successor worker)

Recorded 2026-10-19T03:52:50-0700 (from /bin/date). Owner ContinueRQLS10b. Target OPEN / UNKNOWN; no candidate. No
process running; lane tmp/ empty.

## New parent instruction (IRC, after checkpoint 014)
ONE frozen WH_10 single-orbit assay proposal: written phase/eigenbasis reduction first; exact Gauss anchors d = 5, 7, 9
and negative controls d = 2, 6; all 30 row/column/B-class ONB constraints and ray counts; recovery results kept separate
from target detection power; reuse the reviewed owned_supervisor_v2 / stability_gate_v2; source + config + pins + GO
request for a bounded <= 1700 s numerical assay, NOT launched. Exact cyclic-10-root candidates may be probed within the
<= 300 s initial stdlib scope (PID before compute). W8 E1-E4 only as a prerequisite.

## Clarification of earlier wording (parent correction, recorded here; frozen files not edited)
- Trades: 13 is a PROVED ceiling only for R-trades (rotation [[3/5,-4/5],[4/5,3/5]]) from the Parker classical points
  (evidence/exact-trades-lemma-v1.md, Proposition 3). For general unitary trades NO ceiling is proved: 14 is the maximum
  FOUND in the bounded exact searches (rqls_exact_trades_v2, rqls_trade_mates_v1). My hand-off sentence "they stop at
  13-14 rays" overstated this and is withdrawn in that form.
- All theorem-type claims of this worker (Theorem A of W8, Lemma T/T2, Proposition 3, local-rigidity readings) are
  single-author, unreviewed and NOT parent-accepted.

## Plan (this block)
1. evidence/wh10-reduction-v1.md: line conditions; CRT C^10 = C^2 (x) C^5; reduction to a C^5 flat-plane problem;
   automatic maximality; exact d = 2 and d = 6 exclusions; odd-d Gauss anchors.
2. Exact stdlib probe (Fractions/integer cyclotomics): CRT identities, anchors, exhaustive CAZAC enumeration over mu_20
   (d = 10) and mu_12 (d = 6) with the third-basis test, Chu completeness as positive control.
3. code/rqls_wh10_lm_v1.py + supervisor config + GO request (no launch).
