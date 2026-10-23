# M7 launcher v6–v8 and route A r9 watcher — Codex HOLD and parent admission addendum (2026-10-18T07:27:41-07:00)

## Codex review (static source)
- Review: `review/m7-launch-v6-r9-codex-v1.note.md`, sha256 `b9db41b60ade5623f7651fa55f60815d8e0cfc0798f9f40a1a09d4a99c344f93`; prompt `58876e07…946d`.
- **Part 1, parent B launcher v6 (inherited by v7/v8): HOLD.**
  - BLOCKER: `lsof` failure or incomplete output is not fail-closed (SOURCE01:190–211).
  - MAJOR: the three-observation census is joined only by PID; missing rows/argv/cwd default to empty; argv is truncated before the slot veto searches it (SOURCE01:196–241, 261–276).
  - BLOCKER: after the second reading, hashing, receipt writes and output opening precede the spawn, and the final refusal omits `deadline_ok()` (SOURCE01:366–394).
  - MAJOR: `_run_text` (helper bounds, process group) was not in the snapshot, so bounded helper execution is unverified.
  - MAJOR: the v5→v6 diff also changes assembler output names and makes attempt-1 history optional (SOURCE00:486–551); no acceptance-condition or measured-feed change is in those hunks.
  - MINOR: a tagged regen precheck is not bound to the gate's `regen_receipt_sha256` at assembly.
- **Part 2, route A r9 watcher: HOLD.** The r9 driver diff is path/text-only (confirmed). Watcher BLOCKERs: admission is evaluated before the 16:10 deadline check; a negative sample age (future-dated sample) passes; no chronological validation of the window. MAJOR: incomplete-tail parsing and stale/ended handling.

## Why the two running attempts continue
Both GOs were given before this review returned (07:19–07:24). The defects concern admission robustness under failure modes; none touches the scientific acceptance predicate (Codex confirms the driver diff is path/text-only and that no acceptance-condition or measured-feed change appears). The parent verified post hoc that each actual admission met the rule with real observations:
- **Route A attempt 5 (r9, started 07:20:35):** from the parent monitor `review/disk-monitor-v1-20261018T0700.jsonl`, the last sample before admission (07:20:08) was 07:20:04 (age 4.0 s, non-negative), free 189,510,246,400 B; the [t−300 s, t] window holds 31 strictly increasing timestamps spanning 300.0 s; max peak-to-later drop 30,453,760 B. Rule met as confirmed (last free ≥ 13.5e9; drop ≤ 300 MB; ≥ 25 samples; age ≤ 30 s). The deadline defect is moot (admission at 07:20).
- **B_C321-a3 (launcher v8, started 07:24:32):** gate receipt `receipts/B_C321-a3.gate.json` sha256 `363af65fc6d3d324d00ac79ac780eb1248e03dc9c0b79fa205fe8ebaa0690bbe`: readings 189,508,395,008 B (07:19:29) and 189,282,471,936 B (07:24:30), gap 300.4 s; the ancestry scan found route A's drat-trim 74330 and cadical 74331 by cwd (so lsof returned cwd data), reserved 4,048,388,096 B, ancestry headroom 3,758,096,384 B ≥ cap 2,797,076,480 B; launch long before 17:30. The parent monitor over 07:19:29–07:24:32 has 30 samples, minimum 189,282,488,320 B, max drop 230,064,128 B.

## Required before any further M7 launch (B/C411, B/C311+cuts, parent A replay)
A repaired launcher (v9) and, if a watcher is reused, a repaired watcher (r2), each with an exact diff and a Codex re-review GO:
1. fail-closed enumeration (ps and lsof return codes, complete rows, unresolved live identity = unknown, refuse);
2. consistent census (one snapshot or a re-validated join; no argv truncation before the slot veto);
3. prepare hashes and output files before the final scan; final fresh free/capacity/deadline recheck immediately before spawn;
4. include the exact `_run_text` helper source in the review;
5. split the assembler output-name/history changes into a separately identified change, or restore the baseline;
6. bind the tagged regen receipt hash to the gate's `regen_receipt_sha256` at assembly;
7. watcher: deadline before success, `0 ≤ age ≤ 30 s`, timezone-aware strictly ordered timestamps, bounded window, tolerant tail parsing, exit on a stale or dead monitor without end metadata.
