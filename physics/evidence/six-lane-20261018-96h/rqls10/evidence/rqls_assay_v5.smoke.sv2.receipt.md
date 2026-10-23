# Receipt: rqls_assay_v5 smoke (parent GO 914e55bb...79a1)

Recorded 2026-10-19T00:54:13-0700. GO institute/runs/six-lane-2026-10-18-96h/review/rqls10-assay-v5-smoke-parent-GO-v1.json sha256
914e55bbef7d228f15d18c5d9aa613f294c3749827a6fc450c97254f7f0f79a1. Not a scientific resolution.

Chain (cwd lane, tool timeout 0, TMPDIR lane/tmp): stability_gate_v2 (projected 20,971,520 B) && owned_supervisor_v2 with
evidence/rqls_assay_v5.smoke.supervisor-config-v2.json (bc5151db...); child code/rqls_assay_v5.py 598c8677....
Gate receipt evidence/stability-gate.v5-smoke.v2.json sha256 3fc5ed7117cdb7ac1c62d41618d24e4b0a3063c0587a1ea84ba64b57cc6c3ede: PASS
(30 samples, span 291 s, last age 3 s, max drop 155,693,056 <= allowed 15,136,965,141).
Supervisor PID 27076; child PID 27079 = PGID 27079; start 2026-10-19T00:53:35-0700 (epoch 1792396415.08); wall 14.13 s;
EXITED, rc 0, no trips/SIGTERM/cancel/error, max RSS 75,284,480 B, group census empty, SETTLED; independent ps census
empty; no stop receipt. Outputs frozen 0444 (sha256):
- rqls_assay_v5.smoke.sv2.launch.json: 800a3a855621bda678c03ca61f3093251788c52944ea10dbc704c10f5bfc499b
- rqls_assay_v5.smoke.sv2.result.jsonl: c71d5dd8ae71a228743021941479419300813e54d703b6fd1cce60ebb15bd8cb
- rqls_assay_v5.smoke.sv2.samples.jsonl: 334c1a45b76dfd1f9ec62a8005d8c62ab4fd51cc1b5600edb63d376194fd1b64
- rqls_assay_v5.smoke.sv2.stderr.txt: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- rqls_assay_v5.smoke.sv2.stdout.txt: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- rqls_assay_v5.smoke.sv2.supervisor-receipt.json: 4c6370ca0b24a759357191ebbdcb8d73f7cfbadfb902705f5ae639f07c6d194e

Gates: A 7/7, C1, C1p (residuals 2.10 / 2.26 after 20 forced GN steps), C2 (3/3, 5 rays) and **A5 PASS** (reduced
residual 3.97e-15 at the classical Parker point; full verify maxdev 1.3e-15, 10 rays; 161 parameters).

K (8 random-start reduced-LM recoveries on Parker-type forced data, 200 iterations max): **0/8 verified**. Final
residuals 0.84-1.13 (5 STALL, 3 MAX_ITER), each run 0.19-0.42 s. The reduced LM does not recover the known classical
points from random starts in this sample, so per the GO's rule red1 (R7/R9 targets) is held. Numerical only.
