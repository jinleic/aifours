# Parent-carried deviation and correction list (as of 2026-10-18 ~14:45 PDT)

Every item must appear in the final report's deviation section (grouped), unless already listed verbatim in outcomes.md's deviation sections (then cite it once). Do not add causes that are not stated here or in the records.

## Session and interruptions
- Parent eval kernel lost four times (helpers re-created each time; no state inferred).
- External SIGTERM at 09:25:51 PDT (2026-10-18): CFR lanes E–H and GA P1-B2.M2 are UNKNOWN.

## Hashes and timestamps
- An invented hash in lift-v1 was caught before sending; a placeholder hash was sent, then corrected.
- Estimated timestamps: ZS v2 verdict "after 11:50" (actual 11:45:17); retry 543 phrasing; parent IRC labels at 13:08–13:35 (withdrawn; see review/parent-irc-timestamp-clarifications-v2.md); worker label "13:37:3x"; the M7 worker's 15:04 cutoff claim (retracted).

## Checker and verification defects
- NumPy auxiliary checker route.
- Malformed checker draft, repaired before its first run.
- Ill-posed exploratory mutations.
- Same-author k6 selfcheck stopped, UNKNOWN.
- Checker v1 latent false PASS (reproduced, fixed in v2).
- First B-cut audit schema mismatch.
- An A-side log labelled 466 B (CR-normalized; raw is 475).
- False "empty log" templates.
- Sun k7 Stage B independent checker v1 returned INVALID on a float in producer metadata run.json (checker fault); v2 changed only that.

## Process-safety violations
- ulimit backstops in the Olson lanes, including a SIGXCPU kill on reflection cell (6,19).
- t-search admitted with the wrong stability rule: drop 6.49e9 > allowed 2.44e9.
- GB r6 worker deleted FIFOs.
- Earlier P1-B3.M2 disk-floor UNKNOWN.
- Math1 lane deleted evidence intermediates (historical).
- Early MOQLS7 moved about 17.6 GB of DRAT files to Trash (historical).
- Old AME engine reached about 35 GiB RSS (historical).

## Cadence and wording
- Checkpoint gap 12:17:33 → 12:56:14 (2026-10-18).
- 10:26 "not reachable" claim reclassified as a forecast.
- zs-check draft edited before freeze.
- k6 calibration not counted; Sun controls_v2 UNKNOWN; exploratory LP timeout.
- PA19 v5 retry versions; M7 interrupted attempts UNKNOWN or NOT_STARTED.

## New on 2026-10-18 afternoon
- Failed S1(d) and EDGE verdict write attempts (Python syntax error, undefined path variable, quoting) before the successful exclusive writes.
- M7 verdict v1 typographic defects (fixed in readable v2; v1 retained).
- GB v5 plan swallowed shell status (Codex NO-GO; fixed in plan v5b); GB P1-B4 relative-path launch failure (recorded in review/moqls8-gb-gbs5-P1-B4-launch-path-failure-v1.json).
- t-search-v2 wrapper exits 0 unconditionally and skips missing RSS reads; ended DONE_PARTIAL; a floor breach fell between guard samples; not a premise.
- Sun k7: CERT-FORMAT frozen 13:38:43, after Stage A started 13:35:02 and Stage B 13:37:15; RPLP addendum frozen 14:00:41 after the runs; FINITE-COVERAGE's "transcribed" claim was false at freeze (process MAJOR F-1, permanent).
- k7 launcher v2 would have run 3 processes (NOT_STARTED).
- PA19 split-pilot stop_reason misstated (corrected to null).
- Workers' attributions of the disk writer withdrawn; disk-floor breaches recorded without causal attribution (monitor 14:07:50 11,985,104,896 B; df 14:19:49 11,960,438,784 B; probe guard ~14:19:49 11,999,363,072 B; CFR lane N 14:20:01 11,900,555,264 B; statvfs 14:20:05 11,771,092,992 B).
- PhysRqls10 numeric probe stopped by floor guard (UNKNOWN); CFR lane N chunk floor stop (1/5 done, 4 UNKNOWN).
- Duplicate MCPQLS inquiry stopped.
- gcDCQS20 "40 classes of 1027 triples" wording corrected (review/gcdcqs20-class-count-clarification-v1.md: 1,027 triples partitioned into 40 classes).
- transitions.json edit raised an auto-repair warning; content verified correct.
- GA P1-B3.M2 UNKNOWN: CaDiCaL hit its 3600 s limit; drat-trim reported no conflict, NOT VERIFIED.

## Inventory corrections to carry
- Historical statuses in old headlines are superseded by current-status rows.
- ME3 scope: no uniform D2 gap; D1 needs complete test-centre coverage.
- PH scope is a>c>0, b>0.
- chi8/chi12 count only under the new-theorem clause.
- T7 credits Nicoară/Geng.
- Depolarizing result does not exceed Ahmed's claimed 0.2029161.
- Matrix-weight result is moment feasibility only.
- Olson naming: PAIR1 (sequence lemma) vs the accepted one-block Proposition K1; the rotation K0 draft is unreviewed; RUNS/INV_Res apply only to inherited avoiders; S1(e), K0 draft and S1(g) v1 are unreviewed non-premises.
- Empty QS windows are not exclusions.
- The DOB universal lifting-obstruction claim was rejected.
- Every Lean result used one kernel implementation.
- 466,560 unsound clauses voided an exploratory COMPLETE.
- Detailed lists: review/final-report-inventories-v1/.
