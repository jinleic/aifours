# Receipt: classical_tangent_count_v2 (W3, initial-scope stdlib probe)

Recorded 2026-10-18T23:54:32-0700. Launch record evidence/classical_tangent_count_v2.launch.json sha256
32ae20e0bb1a3f6df1f4467d21fc492d72bf734aec2b5036a8de99f57d69cfe4. (evidence/classical_tangent_count_v1.launch.json was written
for code v1, which lacked the 300 s self budget check; v1 was never launched.)
- Source code/classical_tangent_count_v2.py sha256 a919796172182194ee700a643586ec19f47bf74d020820ac353ea1554085d4bf (frozen before run).
- Command: /bin/sh wrapper, then `env -i TMPDIR=<lane>/tmp /opt/homebrew/bin/python3.14 -I -B code/classical_tangent_count_v2.py
  evidence/parker_z7p3_classical_v1.result.json evidence/classical_tangent_count_v2.result.json`; tool timeout 0.
- START/END 2026-10-18T23:51:43-0700; PID/PGID 16037; EXIT=0; in-script 0.017 s. Settled: single process exited, no
  descendants, output closed; lane tmp/ empty.
- Output evidence/classical_tangent_count_v2.result.json sha256 724884347837943eb1a568c67b403de4e3db73dfb836eabd882b0bed96c1348f
  (frozen 0444 after run).
Result: see evidence/classical-tangent-theory-v1.md (sha256 733e454838a352094405e17036dfc1b854d23d09104d7124f0c3d6301cda75a3): all ten cases unsym excess 6, N7 = 6, N1 = 6,
forced-U excess 0, classical-U excess 6. Exact combinatorics, single kernel (CPython 3.14.3).
