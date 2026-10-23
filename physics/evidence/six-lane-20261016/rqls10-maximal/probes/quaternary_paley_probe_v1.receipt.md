# Receipt: quaternary_paley_probe_v1 (the single exact probe under hadamard-probe-go-v1)

## Authority and frozen inputs

- Authority: review/phys-2-rqls10-hadamard-probe-go-v1.json, sha256
  7d8d298bd41c8ee8e4b35a6af4df7c6f0144eba817f72c8b95179672ed138e4b (2026-10-18T14:44:59-07:00).
- Pre-registration: quaternary_paley_probe_v1.prereg.json, sha256
  6f33e0c47d4e1590400efa9b6428bf51cfd4c0a4702b8bbbf764051ae8d58210. Frozen before launch.
- Script: quaternary_paley_probe_v1.py, sha256 eff3718539da43e20f2b20485da0994d9d13a5c042b4d2c8187b786df96c81f2.
  Frozen 14:46:53 PDT.
- Checker, imported in-process and used only on hits: exact_rqls_checker_v1.py, sha256
  90aaf3beefd049087b7b3d5f00644884a7a99bebcdfdbf90d26c2985cbe89a5d. It was not invoked, because there were no hits.

## Pre-launch actions (no probe execution)

- A static AST syntax check (`python3.14 -c ast.parse`, PYTHONDONTWRITEBYTECODE=1). Result: AST_OK.
- A statvfs one-liner (python3.14) at 14:47:13 PDT: 14,512,357,376 B.
- `df -k` immediately before START: 14,511,280,128 B. This is at least 12.2e9.

## Execution

Command:

```
cd <lane>/probes && /usr/bin/env TMPDIR=<lane>/tmp PYTHONDONTWRITEBYTECODE=1 /opt/homebrew/bin/python3.14 quaternary_paley_probe_v1.py quaternary_paley_probe_v1.result.json
```

- Process discipline: one process; no tool or subprocess timeout; no SIGKILL; no ulimit.
- Host times: START 2026-10-18T14:47:25-0700, END 2026-10-18T14:47:38-0700. EXIT=0.
- In-script elapsed: 13.1 s.
- stop_reason: MAX_SAMPLES. All 2000 pre-registered samples completed; there was no truncation and no guard stop.
- free_bytes_start 14,511,280,128 and free_bytes_end 14,510,112,768, both above the 12e9 floor.

## Output

- quaternary_paley_probe_v1.result.json, sha256 4eda225a09443e3f72894092ca1d4422ae8c13b07edb249146b037d0fd899bd8.
  4986 bytes. Frozen read-only 14:48:46 PDT.

## Result (exact Z4 decisions)

- paley_ok: C is symmetric with zero diagonal and CC^T = 9I, and the rows of H are pairwise balanced.
- Cases: 2000, all with rows and columns orthonormal.
- 824 of 2000 cases have 100 pairwise non-parallel rays.
- No case contains any orthonormal transversal: cases_with_cliques = 0 and max_cliques = 0.
- Partitions: 0. Hits: 0. No enumeration or cover caps were reached.

## Interpretation

- Per the GO: this is a sampled restricted-family **UNKNOWN**, not nonexistence.
- Separately, a written lane derivation (restricted-results-addendum-4.md, R9, unreviewed) explains the outcome for
  every pi. The Paley product family admits no orthonormal transversal at all, because of a mod-4 parity of quaternary
  ONBs that is specific to n = 2 (mod 4).
- That derivation is not part of this probe's evidentiary status.
