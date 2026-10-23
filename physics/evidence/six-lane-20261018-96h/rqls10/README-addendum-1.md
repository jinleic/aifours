# rqls10 lane - navigation addendum 1 (successor worker ContinueRQLS10b)

Written 2026-10-19T02:46:23-0700 (from /bin/date). README.md (01:09, previous worker) is unchanged. Target: OPEN / UNKNOWN.
Receipts and notes are the authority; this file is navigation only.

## Written results (lane-internal, single author, unreviewed, restricted)
- W8 decision note: evidence/w8-decision-v1.md (b24334cf...5829). Proven: flat-plane normal form (Lemma 2), one
  vanishing complementary block => MUB-pair plane (Lemma 3), first-order dimension 2 at MUB-pair planes (Lemma 4, with
  Chebotarev's theorem), THEOREM A: in the WH_5 (x) C^2 orbit ansatz for Cay(Z_5 x Z_2), no three representatives can
  have MUB-pair (stabilizer-type) planes - any frames, any complementary bases, any cardinality. Conditional on the
  order-5 bi-unimodular classification: no MUB-pair representative at all (Proposition B). W8 NOT decided in writing.
- Addendum 1: evidence/w8-decision-v1-addendum-1.md (716051d9...97f5): float evidence that the 100 exotic flat planes are
  invariant under one of 25 conjugates of an order-3 Clifford U (cycling X -> Z -> T) and that b-couples change the
  stabiliser label by an element of L_b; Lemma 5 (exact): then all four representatives share one stabiliser, reducing
  W8 to a finite exact check; exact closure plan (E1)-(E4).
- Structural note + new ansatz proposal: evidence/structure-and-wh10-ansatz-proposal-v1.md (68a6c9c3...db37): WH_10
  single-orbit ansatz (R4's open cocycle class) <=> one vector of C^10 unbiased to the WH bases Z, X, X Z^-1; controls
  d = 2, 6 negative, d = 5, 7, 9 positive. Not run.

## Stdlib probes (float = evidence only; exact where stated)
- z5_flat_rank2_projectors_v1 (float; threshold defects D-1): receipt evidence/z5_flat_rank2_projectors_v1.receipt.md.
- w8_flat_planes_couples_v2 (crash, D-2), v3, v4, v5 (float): receipts ...v3.receipt.md, ...v4_v5.receipt.md (D-4).
- w8_exotic_structure_v1 (float): receipt inside the W8 addendum 1.
- z9p1_resolution_classes_v1 (EXACT integer enumeration): 2,025 Z_9+1 resolution squares, 24 classes, 12 with a known
  classical resolution: evidence/z9p1_resolution_classes_v1.receipt.md.

## R9 (forced Z_9+1 with in-run anchor), GO REQUESTED, NOT RUN
review/rqls10-r9-GO-request-v1.md (44552471...10e4db); code/rqls_assay_v9.py (e9079686...64db); diff
review/rqls_assay_v8_to_v9.diff (291edc71...f157); config evidence/rqls_assay_v9.r9.supervisor-config-v2.json
(a0f04bc0...c3e7). Launch owner must be named by the parent.

## Process
Checkpoints 008-011; deviations review/deviations-ContinueRQLS10b-v2.md (supersedes v1).
