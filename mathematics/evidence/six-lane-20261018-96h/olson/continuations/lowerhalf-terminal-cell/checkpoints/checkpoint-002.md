# LOWER checkpoint 002: integer-form reduction located; drift/lift mechanism found on a test configuration

Owner OlsonPP1Exclusion. /bin/date 2026-10-19T21:39:33-0700. Previous checkpoint-001.md SHA256
24bb6be729a99c1bfa0e582050106de49d122f3b1cc8a2032fedb709957a57da (21:30:21). Written only; nothing frozen beyond scope/checkpoints.

New (notes, CANDIDATE, unfrozen):
- Integer form (uniform, from accepted sequence lemmas at their literal scopes): a T=0 arc P0 exists (p+1 block values);
  GRX at m=1 gives (ZP) at kappa'=kappa-1 for Y=X^{z0}; S1-sharp gives (S1) at kappa-1; Y has length p-1+2kappa=2p+2kappa'-k'
  with k'=p-1, so Y lies in setting (S') of the accepted FB verdict (kappa>=2; kappa=1 is Savchev-Chen directly). ZSTRUCT+FB:
  after normalising the generator to 1, every letter of X^{z0} is an odd integer b, positives sum Pi=W+n+<=2p-1, negatives sum
  nu=n+<=2kappa-3 (or 0), |b|<=p-2, ones abundant; hence for EVERY pattern P the signed subset sums of X^{z_P} (any size) are
  exactly the even integers in [-nu(P),Pi(P)] (greedy fill of the absolute values).
- Lift/drift mechanism: for patterns with full windows (all those sums realisable with admissible sizes), T(P) has a unique even
  lift in [Pi(P)+2,2p-2-nu(P)]; for P0 u Q these lifts are additive in Q (defect in (-2p,2p)), so an anchored chain with
  per-run increment <= -2 contradicts the window after <=(p-3)/2 runs. Worked by hand on kappa=1, B=1, all-singleton
  configuration: contradiction (s<=(p-3)/2 plus-runs vs p available).
- Remaining technical work: (a) which patterns have full windows (n_lo>0 for m<=kappa; n_hi<R for large m); (b) an anchor
  giving the sign of increments for kappa>=2 (all-plus or P0 boundary position); (c) runs with several letters / empty runs.
Blocker: (a)-(c) not yet settled uniformly. Next bounded action (<=30 min): write the integer-form lemma and full-window
criterion precisely; test the anchored chain on general kappa.
