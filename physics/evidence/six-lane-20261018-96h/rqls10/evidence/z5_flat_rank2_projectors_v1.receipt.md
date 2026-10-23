# Receipt: z5_flat_rank2_projectors_v1 and w8_flat_planes_couples_v2 (initial-scope stdlib FLOAT explorations)

Recorded 2026-10-19T02:26:00-0700 (from /bin/date at 02:25:07 plus writing time). Owner ContinueRQLS10b. Evidence only:
float, one implementation, never a premise of any impossibility claim.

## 1. z5_flat_rank2_projectors_v1
Source code/z5_flat_rank2_projectors_v1.py sha256 be9dd7625544a12e8bae3e915ba08640d72b75ebf8f79e0e1cc63e82907ba190 (0444, frozen
before run); launch record evidence/z5_flat_rank2_projectors_v1.launch.json sha256
19527d8177b4ea15244c1d84ebe216dde57c3e4f6d45d01cad3da9381ea03add. Command (cwd lane, tool timeout 0):
/bin/bash -c 'echo START ... PID $$ PGID ...; exec /usr/bin/env -i TMPDIR=<lane>/tmp /opt/homebrew/bin/python3.14 -I -B
code/z5_flat_rank2_projectors_v1.py evidence/z5_flat_rank2_projectors_v1.result.json'.
START 2026-10-19T02:10:30-0700, PID 47741 = PGID 47741; EXIT 0; END 2026-10-19T02:14:40-0700 (wall 250.3 s). Single process;
output closed; lane tmp/ empty afterwards. Output (0444) evidence/z5_flat_rank2_projectors_v1.result.json sha256
193bbc47f4ca5bb7580a047ed028fa3536635f2c3c6a1d4e1d648b30c8b3f335 (39,706 B).

Actual results:
- Controls: the six WH bases orthonormal (max dev 2.2e-16) and mutually unbiased (8.3e-17); all 30 MUB-pair projectors
  are exact zeros of P^2 - P (max 2.0e-16) and flat (1.7e-16).
- First-order kernel at the 30 MUB-pair points: the two smallest eigenvalues of J^T J are <= 6e-18 and the third is
  >= 5.7e-3 at every point, i.e. kernel dimension 2 at all 30 points (agrees with the written count). The recorded field
  "kernel_dim_real" (values 0, 1, 2) is WRONG: its cut-off 1e-18 * max(1, lambda_max) sits inside the round-off band.
- Search: 21,481 LM starts, all converged (residual < 1e-12); the printed classification "805 distinct, all
  NON_MUB_PAIR" is an ARTEFACT: the block-norm threshold 1e-6 is below the displacement (~6e-6) at which LM stops near
  the degenerate MUB-pair zeros (residual quadratic in the kernel displacement). Re-reading the stored 40 examples: 21 are
  MUB-pair points within ~6e-6; 19 are genuinely different (all three blocks of norm sqrt(10), residuals 1e-16..9e-13).
  Their blocks a_k are permutations of one multiset {1.912648879, 1.522874379, -0.904840390, -1.236067978 (= 1 - sqrt5),
  -1.294614890} (elementary symmetric data of the other four in Q(sqrt5): e1 = sqrt5 - 1, e2 = 1 - 2 sqrt5, numerically).
- Kernel-direction stage: only 2 of the 10 intended points ran (because of the wrong kernel count); all 16 starts
  (eps 0.05, 0.2) returned to the starting MUB-pair point (distance 6.1e-6..7.0e-6, the degenerate stopping distance).
Deviation D-1 (recorded in review/deviations-ContinueRQLS10b-v1.md): two threshold defects in the probe's bookkeeping
(classification and kernel count); the raw data are intact and re-read as above; the classification is redone in v3.

## 2. w8_flat_planes_couples_v2
Source code/w8_flat_planes_couples_v2.py sha256 7e5b5fd29b1da7c77dab2470ba2b75ed8fb55e3a757d4abc1edef9badb09626b (0444); launch
record evidence/w8_flat_planes_couples_v2.launch.json sha256 8b75b1bb9b436fd1491677da9de336d3f3fd5989da82cbf483c31894002a1571.
START 2026-10-19T02:20:41-0700, PID 50910 = PGID 50910; EXIT 1 at 2026-10-19T02:22:32-0700 (wall 111.0 s): ZeroDivisionError
in frame() right after the 110 s search stage; NO output file was created (checked: evidence/w8_flat_planes_couples_v2.result.json
absent); lane tmp/ empty. Deviation D-2: crash, no result; superseded by v3 (frame() fix only).
