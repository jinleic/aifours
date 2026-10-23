# Checkpoint 006 (rqls10 continuation)

Recorded 2026-10-19T01:20:18-0700. Owner ContinueRQLS10.

## Claim / actual result
- Target OPEN / UNKNOWN; no candidate.
- v7 K-only calibration SETTLED (GO 01d5132c...): gates pass; KP 16/16 at amplitudes 1e-3, 1e-2, 0.1 and 13/16 at 0.5;
  KR 48/256, all classical. Scope (addendum 1): finite known-classical recovery only; no transfer to unknown maximal
  configurations; target sensitivity uncalibrated.
- v8 R7 target assay frozen and GO requested: unchanged Reduced/LM/verifier (AST: only main() differs from v7), gating
  replays C3r (v = 7 maximal), C4r (v = 8 maximal), KPc, KRc, then 256 fresh forced Z_7+3 configs x 8 starts; 1800 s.
- W8 addendum 1 (written): Gram lemma X_r^dag X_r = I/2; antilinear couple maps and Kramers-type structure; the
  MUB-span sub-case with a common column frame is excluded by the K4-triangle parity (as in R11).

## Files (sha256)
- evidence/rqls_assay_v7.kcal.sv2.receipt.md: 0a2e39e93974bd1ead961cc2b2d87c39efaa6b25f9975ae65c9dc54a0af06881
- evidence/rqls_assay_v7.kcal.sv2.receipt-addendum-1.md: f3ea321fe88968b8280a36cb31f6ae57e47aad69e62b8df2bc2662c6af8621f4
- code/rqls_assay_v8.py: 0988a73bcdda95ba185dd1d4277294867801fc6f4ec1f9c0140416a14438bfc0
- review/rqls_assay_v7_to_v8.diff: fb2973c05ec5aece562a5eca30fa188c1cefcb75681c40ddb408c2ccb357984a
- evidence/rqls_assay_v8.r7.supervisor-config-v2.json: a763a6a7bb0c3bfe30a2b6fe45104e777e028ab3bb31d01dc1f5c980092b365d
- evidence/w8-wh5-c2-orbit-ansatz-addendum-1.md: 213f2fa7115d84c47b42c0237165a44c7d579d1f577498450ef97c092edc2fc9
- README.md: 38410d11469c412db5af4a0344558053eca069f5bfad9e0734f93b2d947bf387

## Blocker
v8 R7 GO pending. No process running.

## Next bounded actions
1. On GO: fresh gate && supervisor v2 + v8 config (timeout 0); receipt; report R7 counts as scoped UNKNOWN unless a
   maximal candidate appears (then numeric-only candidate, notify immediately).
2. Continue the W8 written model (general column frames) toward a reduced system for a later separately-gated LM.
