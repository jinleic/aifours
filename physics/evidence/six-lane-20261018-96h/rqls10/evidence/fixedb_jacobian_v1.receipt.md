# Receipt: fixedb_jacobian_v1 (initial-scope stdlib probe, pure-Python float complex; validation, not a search)

Recorded 2026-10-19T04:52:41-0700 for the launch; receipt written after the run (clock read 04:53:12 at END). Owner
ContinueRQLS10b. Source code/fixedb_jacobian_v1.py 10c466ddf9afb9f1b9376a5bdca29783ecf97ffd7c57ed2adc1f5463268fed8c (0444
before launch); launch record evidence/fixedb_jacobian_v1.launch.json
218f628b1d523d8c13711e5c22579c78bb5fbb8d27f9965f846a84687182402d (0444; path + sha sent to the parent before the run);
input evidence/fixedb_anchors_v1.result.json 13d6ed64d8aafde833ce7981d7ed10044b2b06975d425a5778328ea610e22b92. Command (cwd
lane, tool timeout 0): /bin/bash -c 'echo START ... PID $$ ...; exec /usr/bin/env -i TMPDIR=<lane>/tmp
/opt/homebrew/bin/python3.14 -I -B code/fixedb_jacobian_v1.py evidence/fixedb_anchors_v1.result.json
evidence/fixedb_jacobian_v1.result.json'. START 2026-10-19T04:53:02-0700, PID 86952 = PGID 86952, EXIT 0, END 04:53:12 (in-run
10.27 s); single process; lane tmp/ empty. Output evidence/fixedb_jacobian_v1.result.json (2,621 bytes, born 04:53:12, 0444
within the same minute) 598282a44aa53bc9a9f8cb44a115f51dc88a095187a42451fbb055387b754bfa. One implementation, double precision.

Results (all five gates true):
- Analytic Jacobian of the fixed-B unitary model vs central differences along U_k (I + eps A_k) (exact for the bilinear
  M = U_i^* U_i'): max relative error 3.2e-13 .. 4.9e-13 at random unitaries (cyclic v = 4, 5, 7; XOR v = 8) and at both
  anchors.
- Anchors in float: residual <= 1.8e-16, full Gram deviation (all rows, columns, classes) <= 2.3e-16, U_0 = I, rays 49
  (minsep 5/7) and 64 (minsep 1/2).
- Tangent counts (real Jacobian rank by two-pass modified Gram-Schmidt, gap: accepted relative norms >= 0.079, rejected
  <= 3.3e-14; same rank at 1e-9 and 1e-6):
  - v = 7 Huang-Li anchor (cyclic B): 252 parameters, rank 246, kernel 6 = left-phase gauge rank 6 -> excess 0
    (first-order isolated modulo gauge).
  - v = 8 Zhang-Cao anchor (XOR B): 392 parameters, rank 380, kernel 12, gauge rank 6 (not 7: one left-phase direction,
    +1 on span{e_0..e_3} and -1 on span{e_4..e_7}, is absorbed by right phases because every U_k maps the computational
    basis into the two halves) -> first-order excess 6 (not known to integrate to a family).
  - classical v = 7 point (A(i,j) = j + 3i mod 7, cyclic B): rank 252 = parameters, kernel 0 (rigid).
Scope: validation of formulas and local counts at known points; no statement about v = 10.
