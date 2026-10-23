# PA(19,8,6): three whole ms06 M2 cases closed; 146 remain

Recorded at 2026-10-19T03:06:18-0700.

**CORRECTNESS-ACCEPTED SCOPED PARTIAL.** Runner v17 run-004 produced retained exact-input UNSAT proofs for whole lane-original M2 cases ms06 b156 (ms06_s00145), b187 (ms06_s00155) and b144 (ms06_s00174), each via the direct build_v2 encoding of the full skeleton case (no placement interval). The undecided count is now **146 = 83 ms06 + 63 ms09**. This does not settle PA(19,8,6); M1 and the M2H views are unchanged.

| Case | CNF SHA256 | Proof bytes | Provenanced replay |
|---|---|---:|---|
| ms06:b00156:direct | `7bea2b486a27a89a1b94734484005ea8a77534aa917d05644070aa16bce0a7ad` | 31832828 | VERIFIED, consumed = file bytes |
| ms06:b00187:direct | `8144bce4b68f57b6f5ad7f973507320ec82120f5e213d81284a2b996c5798006` | 60089519 | VERIFIED, consumed = file bytes |
| ms06:b00144:direct | `a29f834c8841e2d2ad32e96218aad8f2737dec989be9d6b1a13590d77692ee80` | 64177237 | VERIFIED, consumed = file bytes |

Evidence: [raw audit](pa19-run004-raw-parent-audit-v1.json), [replay results](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/pa19-ms06-provenanced-replay-v1/science-results-v1.json), [frontier v3](pa19-parent-frontier-v3.json). The parent launched the runner (GO 3f149766…), observed exit 0, checked C1–C7 intended outcomes and all 14 settled children, rehashed retained CNFs/proofs against the pre-registered pins, commits and summary, and replayed all three proofs sequentially with the provenanced drat-trim build a46c0c71… (same verifier algorithm, different build; the build's controls were qualified for run-003). Case identity: each id is the whole case in frontier v2's ms06 list; the direct encoding's completeness rests on the existing build_v2 trust base (Codex r8 reviewed the item-family change only). One DRAT algorithm, two builds: not independent verifiers. No novelty claim.
