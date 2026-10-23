# LOWER checkpoint 003: anchored arc chain in integer form; windows have width <p; plan to freeze partial

Owner OlsonPP1Exclusion. /bin/date 2026-10-19T21:47:06-0700. Previous checkpoint-002.md SHA256
753a50b995b611fc0b645544e9a315ec4ca4d4b772a26ca79264950ebee1f524 (21:39:33). Written only; nothing frozen beyond scope/checkpoints.

New (notes, CANDIDATE, unfrozen):
- Balance from accepted FB gives n- <= n+ = nu, and Pi >= L+n+ = p-1+2kappa-n-; hence every arc window, written in the
  coordinate U = V + beta(S) (S = the part of the complement arc C0 added to the T=0 arc P0, beta = coefficient sum),
  has width <= p-3: full windows [Pi+2, 2p-2-nu], partial ones enlarged only by max(0,2kappa-#Neg) at the top (or
  max(0,2kappa-#Pos) at the bottom). So lifts are unique, consecutive increments equal theta_i := the even representative
  of h_i = tau_i + X_i in (-p,p), and U(S) = 2p + sum_{i in S} theta_i for every two-sided extension S (anchor: T(P0)=0).
- (S1) for X and for X^{z0} forces a light/heavy split of the T=0 cut (one side holds <= kappa coefficient-one letters);
  WLOG P0 light.
- Window-fill caveat: the achievable sizes need a density argument (abundant ones); proving the two-hole description
  in both regimes (Pos-heavy / Neg-heavy) exactly is the remaining technical step before the chain contradiction.
Blocker: global contradiction not yet derived (need endpoint constraints on Theta = sum_{C0} theta and the regime switch).
Next bounded action (<=30 min): freeze the uniform partial (range/coverage, run structure via Theorem P, dominance,
integer form with exact interval lemma, light/heavy cut) as proof-LOWER-structure-v1.md; then continue the chain argument.
