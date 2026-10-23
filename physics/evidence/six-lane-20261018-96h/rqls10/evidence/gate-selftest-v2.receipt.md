# Receipt: stability gate v2 self-test (initial scope, stdlib, no science)

Recorded 2026-10-19T00:40:30-0700. Gate code/stability_gate_v2.py sha256 1f62874aff9b22657a90f180b81c678117fd703afe2345f7576454e0faae008a; self-test
code/stability_gate_v2_selftest_v2.py sha256 0d881038655c4d1e32ce45b88c97257be990b69166e793cf828a0e3d32eadc76 (selftest v1 sha256
f10826fa7c379576fd169b45095b361e1af7da6259d33ebb23f28f9bf0d40a68 never ran: its F09 fixture could not trip the drop rule).
Superseded and never run: code/stability_gate_v1.py (would refuse the real stream: its first line is the
observer_start event; parent finding).
Observer source pinned: institute/runs/six-lane-2026-10-18-96h/control/resource_observer_v3.py sha256
fe311f28d122310da004d0968272ae294a99757756b4898f0d9db4cb13f04196 (re-hashed by the gate).

Command: env -i TMPDIR=<lane>/tmp /opt/homebrew/bin/python3.14 -I -B code/stability_gate_v2_selftest_v2.py code/stability_gate_v2.py
evidence/gate-fixtures-v2 <lane> <RUN>/control/resource-observer-live-v3.jsonl <observer source> fe311f28... evidence/gate-selftest-v2.summary.json;
tool timeout 0; START/END 2026-10-19T00:40:18-0700; PID/PGID 25352 (+ one gate subprocess per fixture, each exited);
EXIT=0; 0.453 s. Settled; lane tmp/ empty. Fixtures and per-fixture gate receipts retained (0444) in
evidence/gate-fixtures-v2/ (25 files). Summary evidence/gate-selftest-v2.summary.json sha256
9bb5e8d95bd3c2aabbffd41cedea610111d9493188d3183d0fc53a279125d822.

Result: all 12 fixtures matched their expectations (positive synthetic PASS; unterminated final line ignored -> PASS;
malformed line, future sample, stale stream, observer_end, missing start event, wrong source sha, drop too large,
non-increasing timestamps, too few samples, low free -> REFUSE with the intended reason). Real stream at
1792395618 (epoch): PASS (30 samples in window, span
291.0 s, last age 7.0 s, last free
195555938304, max drop 24055808).
This PASS is a smoke of the gate, not a launch admission; every launch re-runs the gate in the same && chain.
