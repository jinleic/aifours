# Receipt: w8_flat_planes_couples_v3 (initial-scope stdlib FLOAT exploration; evidence only)

Recorded 2026-10-19T02:29:30-0700 (from /bin/date 02:27:18 + writing). Owner ContinueRQLS10b.
Source code/w8_flat_planes_couples_v3.py sha256 232b202f85793bb0b2b9f5bae025c8e1d26af7e7ce0fb8fe19620c8c316c1c16 (0444; v2 plus the
frame() fix only). Launch record evidence/w8_flat_planes_couples_v3.launch.json sha256
0364c585c5e2d3fbcf3c7ef5d24bff3039435f1ea0a35235a7e0442237e784d2. Command (cwd lane, tool timeout 0): /bin/bash -c '...; exec
/usr/bin/env -i TMPDIR=<lane>/tmp /opt/homebrew/bin/python3.14 -I -B code/w8_flat_planes_couples_v3.py
evidence/w8_flat_planes_couples_v3.result.json'. START 2026-10-19T02:23:46-0700; PID 51395 = PGID 51395; EXIT 0; END
2026-10-19T02:25:40-0700 (wall 114.4 s); single process; lane tmp/ empty. Output (0444) sha256
241219fd01acd82bc8f0530367891ea385b7b122326afd2acac8989c65054e5e (31,895 B).

Actual results (float, one implementation; NOT a proof and NOT a premise of any impossibility claim):
- S: 9,628 LM starts, all converged; 4,581 endpoints within 1e-3 of one of the 30 MUB-pair projectors, 5,047 at
  "exotic" flat rank-2 projectors (polished to ||P^2 - P|| < 1e-12, trace 2); 100 distinct exotic projectors
  (multiplicities 16..138), each at Frobenius distance >= 1.0128 from every MUB-pair projector.
- O: the 130 planes (30 + 100) are closed under conjugation by the 25 operators X^a Z^c (0 missing images);
  10 orbit representatives (6 MUB-pair orbits, 4 exotic orbits of size 25).
- C: 3,900 couple tests (orbit representative x plane x basis), 271 compatible (all with a 1-dimensional kernel
  proportional to a unitary; 0 with kernel >= 2): MUB-MUB in Z/X/T 83/67/75, exotic-exotic in Z/X/T 13/18/15,
  MUB-exotic 0 in every basis.
- K: 867 assignments of listed planes to 00, 01, 10, 11 (00 an orbit representative) pass all six pairwise couple
  tests; all 867 frame-checked (U_00 = I, U_s from the unique kernels at 00), 0 with a 2-dimensional kernel, and every
  one FAILS at least one of the remaining three couples: minimum over all 867 of the maximal remaining couple residual
  |(e^* F_r) U_r U_s^* (e^* F_s)^*| = 0.12360679774997903 = (sqrt5 - 1)/10 (scale: |row| |row| = 2/5); the first 50
  (all four planes MUB-pair) take the values (2/5)|cos(k pi/5)|, k = 0, 1, 2, i.e. 0.4, 0.3236, 0.1236 - the numerical
  shadow of the K4-triangle parity. 0 solutions; nothing to verify on the full 10 x 10 configuration.
Limits: completeness of the 130-plane list and the exotic computations are numerical; the type breakdown of the 867
assignments beyond the first 50 was not recorded.
