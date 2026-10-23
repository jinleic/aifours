# s1sharp_support_probe_v2 run1: receipt (aid only; never a premise)

Written after /bin/date 2026-10-19T00:14:53-0700.  Owner ContinueOlson.  Launch plan sent to parent before launch (IRC 00:1x).
- Launcher code/lane_launcher_v2.py c10c28555bb6829206e2b6778948085155662844061b195c609950f48780aef4 (stdin-gated child);
  probe code/s1sharp_support_probe_v2.py 316a92a298a3812a83fb92384bae7474289b675dda3f374cabe0dffdbb9f4694 (frozen 00:13:39).
- Shell reads START 2026-10-19T00:14:21-0700, END 00:14:23.  Pre-compute record evidence/probe-v2/run1.pre.json (PID 20282,
  PGID 20282, launcher PID 20281, abs end bound 00:19:21, free 195,877,392,384 B) written before the gate byte; settlement
  run1.post.json: returncode 0, wall 1.891 s, reaped.  run1.jsonl sha256
  92ae8d704261209b9d89d21ccaaf3c876d9c6b8a14ee806b409768cc3f043d6c; child stdout empty.
- Results (exact, all T with support <= 3 values containing a generator, N even in [2p+2, 4kappa], sum 0):
  POS (13, 9): 12,045 T checked, 4 survivors = F1 and F2 each in two unit normalisations
  (1^16 3^12, 1^12 9^16 ~ F1; 1^25 9^3, 1^3 3^25 ~ F2).  TARGET (13, 8): 6,284 checked, 0 survivors.
  POS (31, 21): 409,486 checked, 4 survivors = F1 (1^34 3^30, 1^30 21^34) and F2 (1^61 21^3, 1^3 3^61).
  TARGET (31, 20): 316,122 checked, 0 survivors.
- Scope: shortest long zero-sums with support size <= 3 only; not a proof; independent of Lemma S1-sharp Steps 3-9.
