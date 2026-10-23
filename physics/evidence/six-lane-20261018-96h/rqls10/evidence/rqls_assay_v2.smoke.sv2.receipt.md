# Receipt: rqls_assay_v2 control-only smoke under owned_supervisor_v2 (parent GO 47e7e70a...01a1)

Recorded 2026-10-18T23:59:15-0700. Parent GO: institute/runs/six-lane-2026-10-18-96h/review/rqls10-assay-v2-smoke-parent-GO-v1.json sha256
47e7e70a0c514adb92ec3c1315b01ea87c6baaecf4b7a1cecc3f6c4f557301a1 (smoke only). Not a scientific resolution.

Command (cwd lane, tool timeout 0, TMPDIR=lane/tmp in the launching shell): exactly the GO command array
`/opt/homebrew/bin/python3.14 -I -B <lane>/code/owned_supervisor_v2.py <lane>/evidence/rqls_assay_v2.smoke.supervisor-config-v2.json`.
Pins verified by the supervisor before launch (supervisor 1fece595..., config 644aecc8..., child 6042d573..., inputs).

Execution: supervisor PID 16933; child PID 16935 = PGID 16935 (own session); launch record written before the GO
handshake; start 2026-10-18T23:57:46-0700 (epoch 1792393066.85); end 2026-10-18T23:57:56-0700; wall 10.09 s.
Supervisor: status EXITED, child returncode 3, no trips, no SIGTERM, no cancel, no error, max RSS 40,779,776 B,
min free 196,284,993,536 B, 5 samples at 2 s; process-group census after exit empty; settlement SETTLED. Independent
census by `ps -A -o pid=,pgid=` after the run: no process with PID 16933/16935 or PGID 16935. stdout/stderr empty.
Outputs frozen 0444 after the run (sha256):
- rqls_assay_v2.smoke.sv2.launch.json: a6783618f2e492685c4fa3e7ffd40641a20eb80f269f91132763228e98eba13f
- rqls_assay_v2.smoke.sv2.result.jsonl: c9403fcbc1386f407ce5402f9b8c242ec967d8fb1c93118eed4e4433c4324553
- rqls_assay_v2.smoke.sv2.samples.jsonl: cd072c1c0c9405b431bf38b6a0e28cd8985bb5a4354b5626aae74b802f540fff
- rqls_assay_v2.smoke.sv2.stderr.txt: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- rqls_assay_v2.smoke.sv2.stdout.txt: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- rqls_assay_v2.smoke.sv2.stop-receipt.json: 03108d4f29a02ab6c9fb04aa2bf164ce5cbed2d0199715d0aab8508d79f430d3
- rqls_assay_v2.smoke.sv2.supervisor-receipt.json: 22286d52e4a19646d087a4bd6b4091a4a32c5e9a70c01cfadf60d1fc4d847441

Result:
- Gate A_anchors PASS (all seven): A1 Example 2.4 maxdev 3.1e-16, 64 rays, minsep 0.5; A2 mutation maxdev 0.383;
  A3 four classical Parker encodings maxdev 2.0e-15, 10 rays, F ~ 1.1e-14 to 1.3e-14; A4 unsymmetric maxdev 1.8e-15, 10 rays.
- Gate C1_negative_v6 PASS (non-vacuous): 2 runs x 4000 iterations, final err 0.19 / 0.14, no verified solution.
- Gate C2_v5_classical_only **FAIL (vacuous)**: 3 runs x 8000 iterations, final RRR err 1.1e-4, 1.5e-5, 1.8e-5,
  maxdev 1.4e-4, 8.2e-6, 1.7e-5 (all above the 1e-8 verification threshold), ray counts 5 at the 1e-7 merge threshold.
  No verified solution, so the non-vacuity rule failed. The child stopped with GATE_FAIL_STOP (stop receipt), exit 3,
  before any science stage.

Diagnosis: RRR approaches the (degenerate, classical) 1-RQLS(5) solutions sublinearly; 8000 iterations reach ~1e-5,
not 1e-10. The solver has no local refinement step, so "verified" (maxdev < 1e-8) is not reached on degenerate
solution sets. This latches STOP S-NEW-1 on the full v2 assay (review/stop-registry-v2.json); full v2 is not run.
