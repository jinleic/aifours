# K3 checkpoint 001: p>=13 closes by hand (candidate); p=11 isolated, fullness criterion found

Owner OlsonPP1Exclusion. /bin/date 2026-10-19T23:40:40-0700. Scope K3-scope-v1.md SHA256
5b04e5ac805c225f25820d52447752ebc6a8d6278dde9e459a24ca38c7c12676 frozen 23:29:01 before derivation. Written only; no computation.
Derived (CANDIDATE, unfrozen), kappa=3, R=p+5, N=p+1, accepted Theorem S frame:
- Frame: t in {0,1,2}; labels t=1: {+1,-1} extra; t=2: {+1,+1,-1,-1} or {+1,+1,+1,-3} (ZSTRUCT+FB balance); #(b=1)>=(p+11)/2,
  u+>=(p+5)/2 after the light side (o(P0)<=3).
- Lemma N3: negative letters in {-1,-3,-5}; x(A-)=|A-|+nu0<=6 (zero-sums of size 8, 10, or 12 for {-5,-5} with a refined
  count u+>=10); so A- in {{},{-1},{-1,-1},{-1,-1,-1},{-3},{-3,-1},{-5}}, nu0<=5, 2Pi0+3+nu0>=2p+8.
- p>=13: every m=4 pattern has window [0,p+5]=[0,R] (2p-8>=p+5), hence is full. Family F={m=4}: theta_i via
  Q={i+1,i+3,i+5,i+7} and Q u {i} (both m=4); connectivity by interval shrinking and quadruple gap moves (5-sets with m=4);
  f0=0 via {0,3,6,9},{1,4,7,10} (union m=4); complement via {0,2,4,6}. RIG with top four of alternating sets: B*=R, all
  rotations +-1, theta>=-1, each alternating set has sum(theta+1)=3-nu0, nu0<=3.
- Final (p>=13): nu0=0 CJ'''; no empty runs if nu0>=1; nu0 in {2,3}: two non-adjacent +1-singletons, T=-4 hit with n=4;
  nu0=1: theta=1 run e (s_e>=1: {e,i} n=s_e+3; e={-1}: {e,i,j} n=2) or four theta=0 length-2 runs ({e,i} n=4).
- p=11: no full-window m (m=4 window [0,14]); proved: m=4 set is full if |Pos(Q)|,|Neg(Q)|<=14 (minimal representation
  argument, units u+>=8, labels<=7); m=3 set full iff X^(Q) two-signed. Lift framework connectivity/top-set membership at
  p=11 is word-dependent: not yet closed.
Next bounded action (<=30 min): freeze proof for p>=13 with p=11 explicitly isolated; then attempt p=11 (sorting with
two-signed m=3 sets) or record its exact obstruction.
