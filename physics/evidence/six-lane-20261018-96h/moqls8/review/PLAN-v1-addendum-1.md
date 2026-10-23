# PLAN v1 — addendum 1 (no overwrite of PLAN-v1.md)

Recorded 2026-10-18T23:26:44-0700. Supersedes only the items below of `review/PLAN-v1.md` (sha256 3a67a280…3ccd).

1. **Wording correction (parent nit).** In PLAN v1 §Attack 1, "UNKNOWN by budget: B3 is not closable directly within one chunk" is withdrawn. Correct statement: an UNKNOWN at the self-budget means only that **this attempt** did not close within its allocated chunk. It says nothing about whether B3 is intrinsically closable, and B3 remains open.

2. **New-round controls adopted.** The launch rules now come from three parent records, each re-hashed by the runner or cited in each GO:
   - `control/moqls8-pipeline-resource-amendment-v1.json` (dc1eaed0…b2a8): at most 4 busy processes including driver, feeders and helpers; one scientific pipeline; lane RSS 11 GiB.
   - `control/launch-contract-tightening-v1.json` (8ac55669…aa20).
   - Observer v3 with stability addenda v1 (9aff1085…) and v2 (6ddac862…).

3. **GA runner identity is now `code/replay_v6b.py`** (sha256 de93413c2f110472a3f12f877ab3f440e0dfecd423756d592a4221c5829d8df7), with diff `code/DIFF-replay_v5e-to-v6b.txt` (33df80c7…1585).
   - `code/replay_v6.py` (43751f4f…0ad3f) is an unreviewed draft. It was never run and its docstring numbers are stale; it is kept unchanged.
   - Final v6b limits:

| Limit | Value |
|---|---|
| Gate wait budget | 300 s (then DEFERRED; no native start) |
| CaDiCaL | `-t 6300` |
| drat-trim | `-t 10020` (wall time from its own start) |
| Backstop | 10260 s from native spawn |
| Chunk fit | driver start + 300 + 60 + 10260 + 120 reap + 60 margin ≤ +10800 s |
| No native spawn | at or after 2026-10-22T19:01:33-07:00 |
| In-flight SIGTERM | 2026-10-22T21:50:00-07:00 |
| Busy accounting | MINE = 3 (cadical, drat-trim, driver) against cap 4 |
| Formula reservation | 9 GiB (desk stop 9.5 GiB) |
| Retained output | solver+checker logs > 64 MiB → SIGTERM; 80 MiB per-run reservation in the launch floor (12.2e9 + 80 MiB) and the stability floor (13.5e9 + 80 MiB) |

4. **Ownership.** Each run gets an exclusive parent-readable launch record under `evidence/ga-replay-v6b/launch/` before the native spawn decision. It records the owner, the parent GO hash, the driver PID/PGID and start identity, the argv/source/binary/input pins, cwd, the absolute worst-case child end, output paths, and the 80 MiB reservation. The path is sent to the parent immediately.

5. **Review.** A Codex delta review of v6b is running (`review/ga-v6b-delta-review-v1/`). No native process runs until that review returns, the parent's independent constants inspection is done, and an item GO is issued.
