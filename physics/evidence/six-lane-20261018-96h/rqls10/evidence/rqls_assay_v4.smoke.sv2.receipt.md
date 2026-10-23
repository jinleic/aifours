# Receipt: rqls_assay_v4 control-only smoke (parent GO 743df986...be73)

Recorded 2026-10-19T00:44:38-0700. GO institute/runs/six-lane-2026-10-18-96h/review/rqls10-assay-v4-smoke-parent-GO-v1.json sha256
743df986224dac8f98b8d886d58349f4086d936f1e04734f536ab6f418e0be73. Not a scientific resolution.

Chain (cwd lane, tool timeout 0, TMPDIR lane/tmp): stability_gate_v2 (projected 20,971,520 B) && owned_supervisor_v2
with evidence/rqls_assay_v4.smoke.supervisor-config-v2.json (c2caf474...); child code/rqls_assay_v4.py 286951e8....
Gate receipt evidence/stability-gate.v4-smoke.v2.json sha256 bf093aca28f3f0f3303faee428a5d349bd1c6c296877a48e4403e1a18b97f8be: PASS
(30 samples, span 290 s, last age 3 s, last free 195,485,794,304, max drop 72,867,840 <= allowed 15,165,482,858,
fresh free 195,485,802,496).
Supervisor: PID 25743; child PID 25745 = PGID 25745; start 2026-10-19T00:44:04-0700 (epoch 1792395844.87); wall 12.08 s;
EXITED, rc 0, no trips/SIGTERM/cancel/error, max RSS 66,027,520 B, group census empty, SETTLED; independent ps census
empty. No stop receipt. Outputs frozen 0444 (sha256):
- rqls_assay_v4.smoke.sv2.launch.json: c4a8f0a44e819b8c4beefd7699b16effaad39ba45c05ce6913fc54b553f78eb1
- rqls_assay_v4.smoke.sv2.result.jsonl: a041661f251efcd36f01f6645aaa387036a62fc82d947550b8eef78c44ac6e72
- rqls_assay_v4.smoke.sv2.samples.jsonl: 5dc75b4ca7365b0f0f41043c08ca93ecdbe065be6d47cecfccbfd37b8b4a2982
- rqls_assay_v4.smoke.sv2.stderr.txt: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- rqls_assay_v4.smoke.sv2.stdout.txt: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- rqls_assay_v4.smoke.sv2.supervisor-receipt.json: 3dcd4e9c350d71d7c595521aca8fcd5ae0778c72dd8dd11d013189575b054f75

Gates: A_anchors PASS (7/7); C1_negative_v6 PASS (2 runs, zero verified); **C1p_polisher_negative PASS,
non-vacuous**: both v = 6 endpoints (RRR err 0.142, 0.190) were force-polished for 20 Gauss-Newton steps; residual
stayed 2.10 / 2.26, maxdev 0.285 / 1.0, zero verified solutions; C2 PASS (3/3 polished, 5 rays). end mode smoke.
