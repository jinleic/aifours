# t-search-v2 README (append-only)

* 13:13:58 Pre-launch record, as required by the parent's conditional GO (IRC 13:17 PDT, condition (c)):
  - code/t_search_v2.py ad22b19bf455e46d360dd74139a05388a72813b76cfcf08d144018d5bf59b119
  - code/admission_v1.py 661379066d0fa56f641e587b6aca373f137f3e8b4fdb6289074bc3bdf39d0364
  - gate_v1.sh (wrapper) ba112eca261da2e656f6429079454aca2dc56f6876fb72de82de2eb41e07bf81
  - PLAN-v1.md 2a7fd4628c7e0e541c95b2b8e1695625d8dc9fdbdf0043f3bfadeed754ba2b96
  - EXPECTED-v1.json 48419050a767de7f3441f32af9b364de67403d02fdde60385199e8fa5c5b47ef
  - The t-search-v1 run's peak RSS was NOT recorded (that run lasted 13.4 s and no RSS sampling was done).
  - Wrapper behaviour, matching condition (b):
    - admission_v1.py with PROJECTED_BYTES = 1300000000, so A4 enforces free >= 13.5e9;
    - launch only on admission exit 0;
    - one python3 -B code/t_search_v2.py, with TMPDIR = t-search-v2/tmp;
    - PID and start time logged;
    - watcher loop in the same shell: sleep 20 s, then /bin/df -k free and /bin/ps -o rss= for the PID;
    - if free < 12.0e9, RSS > 3 GiB, or the clock is >= 17:29 PDT: kill -TERM to that PID only, then a bounded wait of
      at most 120 s with kill -0 polling, then UNKNOWN with the reason recorded;
    - no SIGKILL, ulimit, timeout or gtimeout;
    - exit code and end time logged (out/wrapper-run1.log, created exclusively; noclobber on every output).
  - The plan's launch line (PLAN-v1 Sec. 4) is superseded by this wrapper, at the parent's instruction.
  - Pre-launch checks: bash -n on the wrapper; one read of the date -j / df expressions (df free 25,878,276 KB at
    13:13).  No admission check or search has run yet.

* 14:16:08 run ended: child exit 0 ("END exit=0" 14:14:19), DONE_PARTIAL at 14:14:14 (self-budget 3600 s).  Complete:
  (7,5) control found; (29,15) (31,16) 0; COVERED (29,18) (31,19) (37,22) 0; BEYOND (31,20) (37,23) (37,24) 0.
  ITEM_UNKNOWN: (41,25) (budget during item), (41,26) (43,27) (43,28) (not started).  Guard: 179 samples, none empty,
  no STOP; parent monitor shows one floor breach 11,985,104,896 at 14:07:50 during (41,25), unseen by the 20 s guard.
  Receipt END-RECEIPT-v1.md 9323e19733b31b4174ca4c67bc0b8d136715b97a46f8cb0637b91f3c9c34c0ac.  Aid only; no claim.
