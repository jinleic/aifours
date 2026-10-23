# Checkpoint 016 (rqls10 continuation, successor worker)

Recorded 2026-10-19T04:12:36-0700 (from /bin/date). Owner ContinueRQLS10b. Target OPEN / UNKNOWN; no candidate. No
process running; lane tmp/ empty. WH_10 GO request sent to Main 04:12 (launch owner to be named).

## Actual results since 015
- evidence/wh10-reduction-v1.md (7e77051c...0cac8): written reduction of the WH_10 single-orbit ansatz (W1-W9); any
  solution is maximal (Lemma W2); d = 2 and d = 6 have no solution (W7, exact, no import); reduction to a C^5 flat-plane
  problem; Chu/CRT-product sequences and MUB-pair planes excluded; triple not Clifford-equivalent to W8's.
- wh10_exact_v1 (EXACT, PID 73507, EXIT 0): CRT identities; 22 Gauss anchors exact with d rays; the 40 CAZACs of length 10
  over mu_20 are exactly the Chu sequences and none is class-flat -> no WH_10 solution with phases in mu_20 (scoped);
  d = 6 cross-checked by brute force (12 CAZACs, none class-flat).
- wh10_design_check_v1 (deterministic float, PID 74896, EXIT 0): all assay anchor gates pass when recomputed; Jacobian
  kernel at KP anchors: phase only (d = 5, 7), 3-dimensional (d = 9) -> KP gate limited to d = 5, 7.
- code/rqls_wh10_lm_v1.py + config frozen; GO request review/rqls10-wh10-GO-request-v1.md.

## Files (sha256)
- evidence/wh10-reduction-v1.md 7e77051c33431921c6d50ddcd8bd2f1c1ba961a0956cb2678f529d0290c0cac8
- code/wh10_exact_v1.py 9a06f84f...9b62; evidence/wh10_exact_v1.launch.json 8b3d4187...1159; result a3415954...6bdf
- code/wh10_design_check_v1.py e829d45e...425c; launch 44147784...990d; result 4ee856d1...0182
- evidence/wh10_exact_v1.receipt.md 9373b4201d18fdd5ae32ff6e10917bc137e53fd6d18873b11325404c3af9f11d
- code/rqls_wh10_lm_v1.py 39f6067fc481d0746bec370189e9753f20cadce5fc7e5225610075947dec14ab
- evidence/rqls_wh10_lm_v1.supervisor-config-v2.json 40371e8add66a2f05f5f0790d32343399fdd1450f2eddad68d5200f4dd7f489e
- review/rqls10-wh10-GO-request-v1.md 0d6f91f177d1cb01c22da18a91d1046ab23f9bb41d31159c587bb5e4f99493d7
- review/deviations-ContinueRQLS10b-v3.md (D-5 hash typo in the GO request, D-6 trade wording)

## Next
On a GO naming this worker: fresh stability gate && supervisor, receipt, analysis. Meanwhile (written, no GO needed):
flat-plane classification for the WH_10 line triple {(0,1), (1,0), (1,2)} of Z_5^2 (the WH_10 analogue of W8's E1).
