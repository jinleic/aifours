# Receipt: parker_z7p3_classical_v1 (W3, initial-scope stdlib probe)

Recorded 2026-10-18T23:32:46-0700. Launch record evidence/parker_z7p3_classical_v1.launch.json sha256
f47dc46a963c07ffbe6594b81289852d9e92476a24691f0b719bd1daa642ecdd. Source code/parker_z7p3_classical_v1.py sha256
420ac8c8ff41dee907584e2106baac1a8a5d9e08841fb4c240c4d5554a144d57 (frozen before run).

- Command (cwd lane): /bin/sh wrapper, then `env TMPDIR=<lane>/tmp PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1
  OMP_NUM_THREADS=1 /opt/homebrew/bin/python3.14 code/parker_z7p3_classical_v1.py evidence/parker_z7p3_classical_v1.result.json`,
  tool timeout 0. START 2026-10-18T23:32:31-0700, END 2026-10-18T23:32:32-0700, PID/PGID 97585, EXIT=0, stop MAX_HITS
  after 16 beta pairs (0.001 s in loop). Settled: direct child exited, no descendants, output closed, lane tmp/ empty.
- Output evidence/parker_z7p3_classical_v1.result.json (13,244 B, frozen 0444 after run) sha256
  00e991d692e669411a49d45aa1623c52189346dc32acb6fb1feea1858b841c30.

Result (exact): five pairs (A,B) of orthogonal Latin squares of order 10, each square invariant under the Z_7 action
with three fixed rows/columns/symbols (Parker-type Z_7 + 3). The first pair was re-checked in the parent kernel
(Latin rows/columns; 100 distinct ordered pairs). These are classical 1-RQLS(10) (cardinality 10) in the Z_7 + 3
ansatz with U = shift (+) I_3, i.e. eigen-multiplicities (4,1,1,1,1,1,1). Role: exact positive control for the
Z_7 + 3 bookkeeping of the proposed numerical assay; no bearing on maximal cardinality (Lemma 5 of the W2 note shows
such configurations are never maximal).
