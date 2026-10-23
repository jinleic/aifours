# t-search-v2 END-RECEIPT-v1 (aid only; not a proof; no claim)

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T14:15:34-07:00 (first clock read after the run ended).
Run launched under the parent's CONDITIONAL GO for exactly one bounded launch.  No relaunch.  Nothing edited in place.

## 1. Process facts (from out/wrapper-run1.log and out/run1.jsonl)

- WRAPPER START, ADMISSION PASS, LAUNCH pid 7441: 2026-10-18T13:14:14-07:00 (host clock lines in the log).
- Admission (out/admission-run1.json): free 26,497,814,528 (monitor) / 26,496,626,688 (statvfs); 300 s peak-to-later
  drop 958,943,232 <= allowed 1,083,151,210; 31 window samples; age 6.8 s; need 13.5e9.  verdict PASS.
- Child self-budget 3600 s reached: record DONE_PARTIAL, clock 2026-10-18T14:14:14-07:00, elapsed 3600.0.
- Child exit code 0, recorded by the wrapper as "END exit=0" at 2026-10-18T14:14:19-07:00 (the wrapper's
  `wait "$PID"` status).  The wrapper itself always exits 0 (parent-noted limit); completion is established only by
  this child exit code together with the per-item records below.
- stderr empty (0 bytes); run1.stdout.txt is byte-identical to run1.jsonl (cmp exit 0).
- Retained output of this run: out/ = 33,140 bytes.  Peak RSS observed by the guard: 17,024 KB.

## 2. Per-item status (mechanically checked: every even N in [2p + 2, 4 kappa] has both passes "1-max" and "(1,0)-max")

| item (p, kappa) | role | status | found_total | N range |
|---|---|---|---|---|
| (7, 5) | CONTROL_POS | complete | 2 (control target found: true; examples g^10 (3g)^6 and g^13 (5g)^3 at N = 16) | 16..20 |
| (29, 15) | CONTROL_NEG | complete | 0 (as expected) | 60 |
| (31, 16) | CONTROL_NEG | complete | 0 (as expected) | 64 |
| (29, 18) | COVERED | complete | 0 (as expected) | 60..72 |
| (31, 19) | COVERED | complete | 0 (as expected) | 64..76 |
| (31, 20) | BEYOND | complete | 0 (no prediction) | 64..80 |
| (37, 22) | COVERED | complete | 0 (as expected) | 76..88 |
| (37, 23) | BEYOND | complete | 0 (no prediction) | 76..92 |
| (37, 24) | BEYOND | complete | 0 (no prediction) | 76..96 |
| (41, 25) | COVERED | ITEM_UNKNOWN (budget reached during item) | - | - |
| (41, 26) | BEYOND | ITEM_UNKNOWN (not started; budget) | - | - |
| (43, 27) | BEYOND | ITEM_UNKNOWN (not started; budget) | - | - |
| (43, 28) | BEYOND | ITEM_UNKNOWN (not started; budget) | - | - |

All nine complete item records were written before the 14:04:15 heartbeat, which already reports item (41, 25).

## 3. Guard samples and the floor

- 179 WATCH samples, 13:14:34 to 14:13:59, spacing 20-21 s, all preserved in out/wrapper-run1.log.  Every sample has a
  numeric free and a numeric rss_kb: 0 empty or unparseable readings, so no guard reading is UNKNOWN.
- Minimum free seen by the guard: 12,199,706,624 at 13:57:58 (below the 12.2e9 launch-gate level, above the 12.0e9
  stop threshold).  No sample < 12.0e9, no RSS > 3 GiB, clock never reached 17:29: no STOP fired.
- Parent monitor R/disk-monitor-v1-20261018T0722-to-1810.jsonl, read-only: 360 samples in [13:14:14, 14:14:19]; exactly
  one is below the continuous 12e9 floor: 11,985,104,896 at 14:07:50.  This breach fell inside item (41, 25), between
  guard samples 14:07:39 (12,724,191,232) and 14:07:59 (12,452,282,368); the 20 s guard did not observe it and did not
  stop the run.  No cause is established here (this run retained 33,140 bytes).  Item (41, 25) is ITEM_UNKNOWN anyway;
  the parent rules on any further consequence.

## 4. Meaning (aid only)

- Controls behaved as specified: detection on CONTROL_POS; 0 on CONTROL_NEG (accepted S1 (c)).
- COVERED (29, 18), (31, 19), (37, 22): 0, consistent with the accepted S1 (g) v2 (R/olson-s1g-parent-verdict-v1.md);
  the lemma rests on its written proof, not on this search.  (41, 25): UNKNOWN.
- BEYOND (31, 20), (37, 23), (37, 24): no T of the (R1) form was found by this enumerator with these two passes.
  This is NOT evidence that (ZP) => (S1) holds there: the (R1) reduction (notes-ZX-residual-v3.md, unreviewed), the
  normalization passes and the enumerator are unreviewed and not independently replayed.  No claim.
  (41, 26), (43, 27), (43, 28): UNKNOWN.
- No COVERED hit occurred, so nothing falsifies S1 (g) at the checked items.

## 5. Deviations and labels

- gate_v1.sh line 2 says "(parent conditional GO, 13:17 PDT)": an estimated time label copied from the parent message,
  not a host clock read.  The actual admission and launch clock reads are 13:14:14.
- Parent-noted wrapper limits: it always exits 0; an empty ps RSS reading would have been skipped rather than failing
  closed (none occurred); the 20 s cadence cannot see dips between samples (the 14:07:50 breach).

## 6. Hashes (sha256, computed when this receipt was written; README.md before this run's README append)

- PLAN-v1.md 2a7fd4628c7e0e541c95b2b8e1695625d8dc9fdbdf0043f3bfadeed754ba2b96
- EXPECTED-v1.json 48419050a767de7f3441f32af9b364de67403d02fdde60385199e8fa5c5b47ef
- code/t_search_v2.py ad22b19bf455e46d360dd74139a05388a72813b76cfcf08d144018d5bf59b119
- code/admission_v1.py 661379066d0fa56f641e587b6aca373f137f3e8b4fdb6289074bc3bdf39d0364
- gate_v1.sh ba112eca261da2e656f6429079454aca2dc56f6876fb72de82de2eb41e07bf81
- README.md 8b41bd4e7cf25b750ac57c0d7c094d9cb5016a5c29123b9e27d82097cb583e1e
- out/admission-run1.json 984fca26943dbd6b01ffa79be01f9cd00a8255ff26b0ad9268321c941fee553c
- out/run1.jsonl ae12553b43e7ca4a2e76fde90533030f4dd96db90ecff3f73ff6fc42d1d2100e
- out/run1.stdout.txt ae12553b43e7ca4a2e76fde90533030f4dd96db90ecff3f73ff6fc42d1d2100e
- out/run1.stderr.txt e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- out/wrapper-run1.log fa918f6100ba8af5e940f990ed05d044ac9d8d2eb675902e6473654d8f317be6
