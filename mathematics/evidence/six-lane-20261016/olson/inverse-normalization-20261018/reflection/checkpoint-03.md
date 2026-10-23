# Checkpoint 03 (OlsonReflectionRigidity), host clock 2026-10-18T05:37:59-0700

## Parent-accepted since checkpoint 02 (not gates)

- K0* and RED: R/olson-reflection-K0star-RED-parent-verdict-v1.md (879aeee7...c02a).
- B0S (r3) and MXG (r2), and the combined corollary that RES_<(p) has no avoider with k <= p for all primes p >= 5:
  R/olson-reflection-smallk-parent-verdict-v1.md (b71fcaf4...13b8).

## New files (sha256)

Errata versions requested by the verdicts (reviewed predecessors unchanged, each with a fix map):
- proof-B0S-r4.md: d76a179d86692bd59e291b9738c7ab66ca009726fa9cb407372f2e1f3eebb89c (Claude 9 MINOR)
- proof-MXG-r3.md: 07baf046ac3e0e1fdb85294b284c76f06a818e7d371c4c1d4355775720cc7f87 (Codex 1 + Claude 6 MINOR)

High-k, B = 0 [W, unreviewed]:
- proof-B0SP-r1.md: 2921280e86936b4767703df4916479d28b8f470d4b8d47b927e41bae0e48e2d7
- It proves Theorem B0S+: B = 0, all blocks odd, kappa >= 1, any number of empty runs, and
  (H1) k <= p + kappa + 1, (H2) R >= 4 kappa + 1, (H3) 2 kappa <= p - 1, imply solvability.
  For k <= p the hypotheses hold automatically.
- New range: p + 1 <= k <= min(p + kappa + 1, 2p - 2 kappa - 1).
- Open core for B = 0 with k >= p + 1, stated in Sec. 4:
  - LEMMA SIGMA: the singleton representatives sum to p.
  - A SELECTION LEMMA for P inside Z (plus fillers) when (H2) or (H3) fails.

Earlier in this session (already reported):
- proof-B0S-r1/r2/r3.
- proof-MXG-r1/r2: 579128c1...0c1c, f2235ed9...ae2f.
- notes-MXG-route-r1.md: 734e7a58...7ffe.

## Aids (not premises)

E10 (MXG replay):
- plan-E10.md: f79976c17906685e3b9160f63bd48c8f792e0c26698da926426406d1faf48aa1
- code/e10_mxg_replay.py: b133d8d5... (never run)
- code/e10_mxg_replay_v2.py: 0fb093d76420444f2fcc99428380230e9b919b4841fc840e06094813e4996951
- out/e10_mxg_replay.json: d59a95a4dce95eacd1a5c238a6b5014ec6396023cbb2c622fe9d57c65b8feb69
- Result: 6661 interval-feasible data, 0 failures; kills by MIX-R' (6555), W (102), GIANT (4); raw DP 337/337.
- Theorem A', AC', KS', ZP, C, R4' and SPLIT were NOT exercised.

E10b (residual-biased):
- plan-E10b.md: e7c84e435b9ed2b48527e66acb371c66dd5fc2978df4b52c5a8d496fcf8085e7
- code/e10b_mxg_residual.py: 3fd24eb8... (v1 stopped at start with a NameError; no output)
- code/e10b_mxg_residual_v2.py: ddef031f4d0a0f530ae17667964cb5807266b7bdac8919510040130218826a85
- out/e10b_mxg_residual.json: 02a7cb3c6906fa5113e06dcd79a6f5e9c73b96bc3ae5e2dd9113bf8ad40666e3
- Result: 64 kept data out of 15,000,000 tries, all killed by MIX-R'. The residual lemmas were again not reached.

E9 (B = 0 with k >= p + 1):
- plan-E9.md: da6eb0b3ef3480220867b123d0cb2113462aed0fcb97dcb7d9a0a87f564470b1
- code/e9_b0l_probe.py: 84c801b37ce478459bacc37ad2aaa95a16fa48e08431ff2c21a8816089bb196f
- out/e9_b0l_probe.json: c26ef0e4bb9d090417f066feffa205bfe4abfeb042214225375c8b17255c9889
- Result: Step 1 held in 426/426; every datum with k <= 12 (365) was killed, with minimal m = 2.

E9b (kill classification):
- plan-E9b.md: 0b829c0a8a721835580cb431cd023d59a378270d060b238959b66e729fcabaaf
- code/e9b_b0l_kills.py: 15a5e8f5... (crashed in json.dump after the run)
- out/e9b_b0l_kills.json: 554f32dd... (partial; kept)
- code/e9b_b0l_kills_v2.py: c80856edeba4405a5a654b5ae5e57e77ccb912dbd71818d7c74fd2aade0b835b
- out/e9b_b0l_kills_v2.json: ca3a6a40209fea98b4f48b99362f1aca6c496229fa62c91baf7cd81d7bc3b03b
- Result: 590 data, all in Case I. The greedy killed in all 517 data inside the bounds and in 70 of the 73 outside them.
  Defect pairs killed in 556 of 590; two-interval patterns inside Z killed in 581 of 590.

## Still open inside REFL-RES(p)

- k >= p + 1 with B = 0, outside (H1)-(H3).
- k >= p + 1 with 1 <= B < kappa. The RGR analogue is MIX_DEF_HIGH / NMH / GC; no G-version yet.
