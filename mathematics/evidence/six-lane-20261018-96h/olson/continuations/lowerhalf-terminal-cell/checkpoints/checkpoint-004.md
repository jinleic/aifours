# LOWER checkpoint 004: alternating-set sorting gives rotation rigidity (candidate, kappa<=~p/3); tight structure

Owner OlsonPP1Exclusion. /bin/date 2026-10-19T21:59:48-0700. Previous checkpoint-003.md SHA256
63d96b981bbac9b6dbe3653c8d4fc2caac321b4d0aa28cc392d0a66cc55e051b (21:47:06). Parent IRCs (KP3, KP4 accepted at own cells)
noted; lower half unchanged. Written only; nothing frozen beyond scope/checkpoints.

New hand derivation (CANDIDATE, unfrozen), original orientation, integer form (letters c odd, Pi0/nu0 = positive/negative
totals, B*=Pi0+nu0>=R, equality iff all |c|=1; nu0<=2kappa-1 by (S1) for X):
- For every FULL pattern S (all even v in [-nu(S),Pi(S)] realisable inside the window) H(S)=sum_S(tau_i+X_i) has a unique
  representative U(S) in [Pi0+1,2p-1-nu0] with parity sigma(S)=sum_S c; U'(S)=U(S)-2p is additive on disjoint full S1,S2 with
  full union (defect in (0,4p), = 2p); complements: U'(S)+U'(S^c)=K*:=Pi0-nu0-2p; single-run increments theta_i (unique rep
  of h_i in (-p,p) with parity sigma_i) are well defined, and U'(S)=sum_S theta on any connected full family containing two
  disjoint full members with full union.
- Sorting on an alternating set (every other run, m=(p+1)/2): every (kappa+1)-subset is full (m=kappa+1, n_lo=0) when the
  size caps n_hi allow (about kappa<=p/3), so its theta-sum <= -1-nu0; hence at most kappa thetas >=0 per alternating set and
  sum_{alt} theta <= -1-nu0-((p+1)/2-kappa-1). Adding both alternating sets and using sum_all theta = K* gives
  B* <= R, so B*=R: ALL rotations lie in {gamma,-gamma} (rigidity), with every inequality tight (all but kappa thetas
  per parity class equal -1, top-kappa sums = -nu0).
- kappa=1 cell: singletons are full via (+1,-1) pairs or flipped letters; same additive mechanism gives a contradiction in
  all three Theorem-P run shapes (worked by hand, incl. the one-(-1) case with parity).
Blocker: (a) fullness/size-cap lemma for the families used (density of Pos(S),Neg(S)); (b) kappa>p/3 (n_hi cuts);
(c) pair case: tight structure must be contradicted using partial-window patterns (m<=kappa, e.g. arcs).
Next bounded action (<=30 min): write the fullness lemma precisely and re-check the sorting argument's hypotheses.
