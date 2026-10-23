# Receipt: rqls_assay_v3 FULL run under owned_supervisor_v2 (parent GO 3bcf3103...1b5d)

Recorded 2026-10-19T00:33:38-0700. Parent GO institute/runs/six-lane-2026-10-18-96h/review/rqls10-assay-v3-full-parent-GO-v1.json sha256
3bcf3103ceda20fa453127f8cf14705cfc7f1e99cbf4ca7569165138b3ab1b5d (exactly one run). Numerical only; NOT a certificate.
Recorded limitation (parent): the smoke's C1 runs were not polished (err > 1e-2), so the polisher had no negative
challenge there; the same holds in this run (C1: 4 runs, err >= 0.122, not polished).

Command (cwd lane, tool timeout 0, TMPDIR=lane/tmp): `/opt/homebrew/bin/python3.14 -I -B <lane>/code/owned_supervisor_v2.py
<lane>/evidence/rqls_assay_v3.full.supervisor-config-v2.json` (supervisor 1fece595..., config 0750bef7..., child 3168e2a3...).
Execution: supervisor PID 18497; child PID 18499 = PGID 18499; start 2026-10-19T00:05:03-0700 (epoch 1792393503.90);
supervisor end 2026-10-19T00:32:38-0700; wall 1654.41 s (< 1800 s). Supervisor: EXITED, returncode 0, no trips, no
SIGTERM, no cancel, no error; max RSS 529,891,328 B; min free 195,577,257,984 B; 822 samples at 2 s; group census empty;
SETTLED. Independent ps census after the run: no PID 18497/18499 or PGID 18499. stdout/stderr empty; no stop receipt;
end record mode full, terminated false, 826 records, 379,970 B. Outputs frozen 0444 (sha256):
- rqls_assay_v3.full.sv2.launch.json: 84704c31c4609e55c3c9b966a6bab3a8e2a1435357d12509bedb47d543de9ad3
- rqls_assay_v3.full.sv2.result.jsonl: b69d610920c2b9e896b7ff8a979009c8dc80b1de2d46d323c98247131c67c55c
- rqls_assay_v3.full.sv2.samples.jsonl: a8a51690abf3bd9e51fb0494fa269f8bc63cc2ca052015af78dc4be706c65005
- rqls_assay_v3.full.sv2.stderr.txt: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- rqls_assay_v3.full.sv2.stdout.txt: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- rqls_assay_v3.full.sv2.supervisor-receipt.json: 34d8f70d475188c7aa755c64caa2839df8e9f77959e3fb66aa1831a61c320a96

## Results (float, single run, seeds in the JSONL)

Gates: A 7/7 PASS; C1 PASS (4 runs x 15000, zero verified v=6); C2 PASS (6/6 polished to maxdev <= 1e-15, all 5 rays).

Stage L (numerical SVD rank estimates; exact prediction in evidence/classical-tangent-theory-v1.md):
- 300/300 classical forced-U Z_7+3 points (5 pairs x 2 roles x 30 label triples): kernel 34 = rank of gauge+phase
  tangents 34, **excess 0** everywhere; |J T| <= 1.2e-15; singular-value gap: smallest nonzero >= 0.356, largest
  "zero" <= 7.6e-15. Matches the exact combinatorial prediction 2*N7 - 12 = 0. No continuation was attempted.
- Unsymmetric kernel at classical pair 0: kernel 196, rank T 190, **excess 6** (gap 0.413 vs 8.8e-15) = exact
  prediction 2*sum(c-1) = 6.

Calibrations (maximal solutions known to exist for C3, C4):
- C3 v=7 Cay(Z_7): 5/6 verified after polish: 4 classical (7 rays), **1 maximal (49 rays, seed 33, minsep 0.714)**.
- C4 v=8 XOR: 6/6 verified: **2 maximal (64 rays, seeds 41, 44)**, 3 with 16 rays, 1 with 32.
- C5 symmetric Z_7+0: 10/10 verified, all classical (7 rays).
- C6 symmetric Z_7+1 (F_8, classical solutions exist): 1/10 verified (8 rays); 9 runs stalled at err 0.31-0.34.
- C7 symmetric Z_7+3, classical U, Parker B (classical solutions exist): **0/10** (err 0.29-0.35).

Targets (v = 10): no verified solution, no maximal candidate anywhere.
- T1 forced Z_7+3 random: 244 runs (122 configurations), best RRR err 0.299, median 0.344.
- T1t trine-fixed corners: 44 runs, best 0.295, median 0.312.
- T1c classical start + noise 0.15: 41/41 verified, all classical (10 rays) - consistent with local rigidity.
- T2 Z_9+1: 81 runs, best 0.272, median 0.292. T3 Z_5+5: 29 runs, best 0.385, median 0.404.
- T4 unsymmetric v=10 (Parker B, Cay(D_5), Cay(Z_10)), 2 x 20000 each: err 0.47-0.50, no convergence.

## Interpretation (scope)

- Unsymmetric RRR + polish finds maximal solutions at v = 7, 8 for the calibration squares, so the method can see
  maximal points where they are reachable.
- At v = 10 the method's sensitivity is NOT qualified: it failed to recover *known* classical solutions in C7
  (0/10) and T4-Parker (0/2), and C6 succeeded once in 10. All v = 10 misses are therefore uninformative
  (UNKNOWN), not evidence of nonexistence, not even within the sampled ansatze.
- The L stage confirms the exact first-order prediction (excess 0) numerically at all 300 points.
