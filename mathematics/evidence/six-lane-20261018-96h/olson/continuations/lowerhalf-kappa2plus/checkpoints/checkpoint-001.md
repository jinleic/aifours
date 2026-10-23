# K2 checkpoint 001: hand derivation closes the kappa_hat=2 cell (candidate); writing the proof

Owner OlsonPP1Exclusion. /bin/date 2026-10-19T22:57:04-0700. Scope K2-scope-v1.md SHA256
37d39e81cad02fbe13f93d299d171c4e19b18a1be4f98b91b1704d137104593f frozen 22:46:31 before derivation. Written only; no computation.
Derived (CANDIDATE, unfrozen), kappa=2, p>=11, in the accepted Theorem S frame (light T=0 arc P0, labels c_l):
- Claim N: every negative letter has |c|<=3 and |Neg|+nu0<=4 (a negative B>=5 with B ones, or a prefix of {-1,-3}'s with
  <=7 ones, is an integer zero-sum of length in [6,p+3], forbidden at the empty pattern); so nu0<=3 and 2Pi0+3+nu0>=2p+6.
- F={Q: 3<=m(Q)<=(p-3)/2}: every member is full (window [0,R]); theta_i defined for every run via Q={i+2,i+4,i+6};
  F connected under single toggles (interval shrinking, then sliding independent triples); Lemma A on {0,2,4},{1,6,8}
  gives f=0, so U'(Q)=sum_Q theta on F; Lemma C on {0,2,4} and its complement gives sum_all theta=Pi0-nu0-2p.
- Sorting the alternating sets (top three in F): B*<=R, hence every |c|=1, nu0 in {0,1,2}; tight theta data.
- nu0=0: all rotations equal, cited B0S-CJ'''. nu0=2: all theta=-1, a singleton +1 run i has T({i})=-2, attained by
  three -1's and one +1 (n=4, arc window [4,p+3]). nu0=1: one theta=0 run per alternating set, even length, nonempty
  (empty-run rule), one of them all +1: T({e})=-r_e attained by r_e+1 minus-ones and one +1 (n=r_e+2).
Blocker: none found; Theorem P is not needed. Next: freeze proof-K2-v1.md, audit, manifest, package, park.
