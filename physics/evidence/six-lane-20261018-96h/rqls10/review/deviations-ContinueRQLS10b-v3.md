# Deviations record, worker ContinueRQLS10b (v3; supersedes v2 b2c9e42c1b84e57a12c25aa4049843d938d5d31337ac2562444ddd23a7272ce2)

Recorded 2026-10-19T04:12:36-0700 (from /bin/date). D-1 to D-4 unchanged (see v2).

- D-5 (04:12, review/rqls10-wh10-GO-request-v1.md 0d6f91f1...93d7): the abbreviated hash of code/rqls_w8_lm_v2.py is
  written "d336e2e3...a9fd"; the correct sha256 is d336e2e3d3fdbc0afe9cc1e55232524466152e4369519e47a387cc9caf061ca2. The
  file is only cited there as the origin of the copied LM damping schedule; no pin depends on it. The frozen request is
  not edited; this record corrects it.
- D-6 (wording, found by the parent): the hand-off sentence that exact trades "stop at 13-14 rays" overstated the
  result. 13 is proved only for R-trades from the Parker points; 14 is the maximum FOUND in bounded general searches,
  not a ceiling. Recorded in checkpoints/015-checkpoint-v1.md (98d5bcc9...a1d2); frozen notes are accurate on this point
  (exact-trades-lemma-v1.md says "saturated at 14 in the bounded search").
