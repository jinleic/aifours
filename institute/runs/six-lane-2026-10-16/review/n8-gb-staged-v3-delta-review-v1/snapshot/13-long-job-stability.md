# Parent rule amendment — long-job disk stability (2026-10-18T07:31:51-07:00)

- **Previous rule (07:16–07:17 parent messages):** a native job expected to run ≥ 60 min needs free ≥ 13.5e9 B and no drop > 300 MB within the last 5 min, read from the parent monitor.
- **Observation:** free space jumped to ~189.5e9 B at 07:17:14. A single step of about 2.26e9 B occurred between 07:25:01 and 07:26:01 (`disk-monitor-v1-20261018T0722-to-1810.jsonl`), then free was flat at ~186.65e9 B. Under the fixed 300 MB limit such a step blocks every long launch for 5 min although the floor is ~174e9 B away.
- **Amended rule (broadcast 07:32):** last free ≥ 13.5e9 B AND max peak-to-later drop within the last 300 s ≤ max(300,000,000 B, (free_last − 13.5e9 B)/12), i.e. one hour of runway to 13.5e9 B at the worst observed 5-min rate. Sample-quality conditions are unchanged: tz-aware strictly increasing timestamps, 0 ≤ age ≤ 30 s, ≥ 25 samples spanning ≥ 290 s, a stale monitor refuses.
- **Unchanged:** in-flight floor 12e9 B; per-launch fresh gate ≥ 12.2e9 B + projected growth; lane caps.
- **Transition:** frozen code that implements the stricter old rule stays valid; the amendment is adopted only in each lane's next frozen version, which must cite this file.
- **Why this is safe:** the rule's purpose is to avoid launching long jobs that the floor will stop. The amended limit still refuses any launch whose observed worst 5-min rate, sustained for an hour, would cross 13.5e9 B.
