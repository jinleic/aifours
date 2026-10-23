# Receipt: redei_p5_exhaustive_v1 (W3, initial-scope stdlib probe)

Recorded 2026-10-18T23:30:27-0700. Launch record evidence/redei_p5_exhaustive_v1.launch.json sha256
9b30702d1592cd099661101006e76b86f1d7c4fd2a57b6a2fdedc8644147ecac.

- Source code/redei_p5_exhaustive_v1.py sha256 73bb7b535f5ac87f8434d2c6739c9fcfbbf074672f06287a4dba2f12b602b20b (frozen 0444 before run).
- Command (cwd = lane): /bin/sh wrapper printing PID/PGID, then
  `env TMPDIR=<lane>/tmp PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /opt/homebrew/bin/python3.14
  code/redei_p5_exhaustive_v1.py evidence/redei_p5_exhaustive_v1.result.json`; tool timeout 0.
- Host times: START 2026-10-18T23:30:15-0700, END 2026-10-18T23:30:15-0700; PID 96668, PGID 96668; EXIT=0;
  in-script elapsed 0.165 s. Fresh free before launch 197,384,982,528 B. Lane tmp/ empty afterwards.
- Settlement: direct child exited (EXIT=0, reaped by the shell); single process, no descendants; output closed.
- Output evidence/redei_p5_exhaustive_v1.result.json sha256 708c82d992d27f1b1589302edf614507b1e9a89e97dc6df003a42a5fac57ecab.

Result (exact, finite): all 53,130 five-subsets of AG(2,5) enumerated; the 30 lines determine 1 direction; every other
subset determines at least 4 (distribution 4: 1500, 5: 15600, 6: 36000). Of the 120 permutation graphs, 20 are lines and
100 determine exactly the 4 non-axis directions. The bound is attained (1500 subsets with exactly 4), so a threshold of
5 would have been reported violated: the check discriminates at the intended value.

Consequence: Redei's bound for p = 5, the only external input of R3 Step 6, is now a checked finite fact (single
kernel: CPython 3.14.3). R3 is a complete elementary restricted result (still restricted: the flat Fourier-
permutation family only).
