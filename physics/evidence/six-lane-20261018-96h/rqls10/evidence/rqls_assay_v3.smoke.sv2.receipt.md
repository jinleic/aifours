# Receipt: rqls_assay_v3 control-only smoke under owned_supervisor_v2 (parent GO 6fc27a15...64fe)

Recorded 2026-10-19T00:03:56-0700. Parent GO institute/runs/six-lane-2026-10-18-96h/review/rqls10-assay-v3-smoke-parent-GO-v1.json sha256
6fc27a159c258d4cfa999b647a17658158af3c093021090272f5941857e564fe (v3 smoke only; S-NEW-1 stays latched on v2).
Not a scientific resolution.

Command (cwd lane, tool timeout 0, TMPDIR=lane/tmp in the launching shell): `/opt/homebrew/bin/python3.14 -I -B
<lane>/code/owned_supervisor_v2.py <lane>/evidence/rqls_assay_v3.smoke.supervisor-config-v2.json`; pins re-verified
(supervisor 1fece595..., config eccccf9a..., child 3168e2a3...).

Execution: supervisor PID 18080; child PID 18082 = PGID 18082; launch record before GO handshake; start
2026-10-19T00:03:30-0700 (epoch 1792393410.75); end 2026-10-19T00:03:38-0700; wall 8.08 s. Supervisor: EXITED,
returncode 0, trips none, SIGTERM none, cancel none, error none, max RSS 47,431,680 B, min free 196,096,380,928 B,
4 samples, group census empty, SETTLED; independent ps census after the run: no PID 18080/18082 or PGID 18082.
stdout/stderr empty; no stop receipt (exit 0). Outputs frozen 0444 (sha256):
- rqls_assay_v3.smoke.sv2.launch.json: 54d67ca45435aa7cec07cc973a847507579b88855f3b04587ecff3f003e95e0b
- rqls_assay_v3.smoke.sv2.result.jsonl: 431d3e9da9d12cff064310fba779e1b865d6301d606eb0b90f61497e547d6a17
- rqls_assay_v3.smoke.sv2.samples.jsonl: 6f359b81ae769a399e2cd871456a217f82adf09d06e0d7672627f46cfa5668a0
- rqls_assay_v3.smoke.sv2.stderr.txt: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- rqls_assay_v3.smoke.sv2.stdout.txt: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- rqls_assay_v3.smoke.sv2.supervisor-receipt.json: b8c9eaf9adb123e9db6dbd518b7b7542af60cc60991d7c71fda095b3c22d3fa5

Result: A_anchors PASS 7/7 (values identical to the v2 smoke); C1_negative_v6 PASS (2 x 4000 iterations, RRR err
0.19/0.14, not polished since err > 1e-2, zero verified); C2_v5_classical_only PASS: 3/3 RRR endpoints (raw maxdev
1.4e-4, 8.2e-6, 1.7e-5) polished in 3-4 Gauss-Newton steps to maxdev 4.4e-16 (residual 1.2e-15..4.2e-15), each with
exactly 5 rays. end record mode smoke, gates PASS.
