# Checkpoint 013 (rqls10 continuation, successor worker)

Recorded 2026-10-19T03:24:11-0700 (from /bin/date). Owner ContinueRQLS10b. Target OPEN / UNKNOWN; no candidate. No
process running; lane tmp/ empty. Parent R9 audit (RUN/review/rqls10-v9-r9-parent-audit-v1.json) received: scoped
UNKNOWN, weak detection noted.

## Actual results since 012 (parent lead: exact non-symmetric trades)
- evidence/exact-trades-lemma-v1.md (b3eb8e1c...dc07): Lemma T (k-dimensional trade) and T2 (component form), complete
  proofs; classical case: rotating a proper union of components of G_(a,b) gives exact 12-ray 1-RQLS(10) and exact
  curves; the unsymmetric first-order excess 2 sum (c - 1) at classical points is integrated by these curves (Parker:
  6 = 2 x 3 from the inf-inf pairs; Z_9+1: 0); Proposition 3: rational R-trades from Parker points never exceed 13 rays
  (block structure F/K, finite rigidity, odd-norm quaternion parity rules out crossed coincidences), 13 attained;
  general unitary trades reach crossed mates; two crossed mates of parker2 (role B) allow finite-cell trades and reach 14.
- Exact stdlib probes rqls_exact_trades_v1 (2.4 s) and v2 (29.5 s), receipt evidence/rqls_exact_trades.receipt.md
  (b5ca8b19...7191): all reported states exact (0 bad Gram entries); max 13 (Parker starts), 14 (2 crossed-mate starts).

## Files (sha256)
- code/rqls_exact_trades_v1.py 4f8347e9...2967; evidence/rqls_exact_trades_v1.launch.json c3032908...3637;
  evidence/rqls_exact_trades_v1.result.json 0d69a99c...4e75
- code/rqls_exact_trades_v2.py 999ff603...56ad; evidence/rqls_exact_trades_v2.launch.json 0f5656e9...2591;
  evidence/rqls_exact_trades_v2.result.json caa7f7f7...d0ca
- evidence/exact-trades-lemma-v1.md b3eb8e1c10e1be983bf35a8966dd1398ea6034c68471869e84ab4e7e1d73dc07
- evidence/rqls_exact_trades.receipt.md b5ca8b19ec598ae1996293e5c142f149748492fb1572aa4f5f7c570f642f7191

## What remains
Upper bound for general unitary trade sequences (full search over crossed states); trades from other classical
OLS(10) with many disconnected pair graphs; W8 exact closure (E1)-(E4) secondary; WH_10 ansatz proposal (needs a GO for
any float search).
