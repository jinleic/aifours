# Deviations record, worker ContinueRQLS10b (v5; supersedes v4 10d7ca5f449ab44b3c25c13acc4eba1397c92092b837d3209e54341d1b8353be)

Recorded 2026-10-19T05:54:09-0700 (from /bin/date). D-1 to D-10 unchanged (see v2, v3, v4). D-9 concerns the lane's own
tmp/ directory (the probes' TMPDIR), not /tmp.

- D-11 (pre-freeze same-path draft rewrites; recorded at the parent's instruction 05:5x). Several of this worker's own
  files were edited in place at the same path while still unfrozen drafts, before they were frozen (0444), hashed and
  cited. None of them had been executed or sent to the parent before the final freeze. Instances:
  - code/fourier_co_enum_v1.py: first draft written ~05:38, never run, then rewritten at the same path to the parent's
    requirements (~05:46) plus one signature edit, frozen 05:48:49 as 2b72ec879f44239ba441160b2174baad0b107021be2e2475e7de42dde96e83a6
    (the version the parent pinned and ran);
  - code/fixedb_anchors_v1.py (normalisation fix and block repair before the 04:37 freeze), code/fixedb_jacobian_v1.py
    (rank/time-guard edits before 04:52), code/fixedb_candidate_verify_v1.py (refinement-loop fixes before 05:06),
    code/rqls_fixedb_lm_v1.py (MODE / plan edits before 05:02), code/fixedb_q1_check_v2.py (latency guard before 05:41);
  - documents: evidence/fixedb-unitary-model-proposal-v1.md (verification-boundary wording before 05:10),
    review/rqls10-fixedb-GO-request-v1.md (pins repointed v1 -> v3 before 05:14), review/rqls10-fixedb-GO-request-v2.md
    (Q1 config repointed before 05:26), README-addendum-3.md (one hash prefix corrected before 05:17).
  Rule adopted from 05:54: every correction, including to an unfrozen draft, is written to a NEW versioned file; the
  superseded draft is frozen as it stands. Applied first to code/fco_candidate_verify_v1.py (frozen unchanged,
  6b7b9ccdba9a36118c42eadc32e8681d33f570dbbf0d8102e5ff4f93d19d68ca).
