# P11R checkpoint 002: near-rigidity B* in {16,18} derived; deliverable = labelled partial + exact obstruction

Owner OlsonPP1Exclusion. /bin/date 2026-10-20T00:09:21-0700. Previous checkpoint-001.md SHA256
9652bd5d356e4b7ae9c8325efc6fcdc5081eb79e366aa3fd92a0c5980114892e (00:03:06). Written only; nothing frozen beyond scope/checkpoints.
Derived (CANDIDATE, unfrozen), residual p=11:
- LEMMA PAIR: with distinct P-runs a,b,c (k_P>=3), put c=0, choose gap runs g1<g2 in 1..11 with g1>=3, g2-g1>=3, g2<=9,
  {g1,g2} disjoint from {a,b} (always possible: g1=3 or 4 or 5); the three blocks [1,g1-1],[g1+1,g2-1],[g2+1,11] are pairwise
  non-adjacent of length >=2; splitting each block into two parts (a's part to P1, b's part to P2) gives disjoint P1,P2 with
  m(P1)=m(P2)=m(P1 u P2)=3, all meeting P and missing c, hence two-signed, hence full (window [2,16]).
- Window argument: full => B*<=20 and U' in [B*-nu0-21,-1-nu0]; B*=20 forces U'=-1-nu0 for all full sets, contradicting
  Lemma A on PAIR; so B* in {16,18}. B*=18: Lemma A on PAIR gives nu0<=1, so exactly one letter +3, others +-1, A- subset {-1}.
  B*=16: all letters +-1 (rotation rigidity), nu0<=3; nu0=0 gives all rotations equal, excluded by CJ'''.
- No cheap kill of the near-rigid residual: single-run (SR) tests only restrict tau_i to a few residues; window-only additivity
  over partitions gives at most nu0<=1; the K3 sorting needs the top three or four theta-runs of each alternating set inside one
  connected family of full patterns, which is the missing claim.
Decision (throttle, no long case sweep): freeze a labelled partial (structure + near-rigidity) with the exact obstruction.
Next: freeze proof/obstruction note, package, manifest, closing checkpoint, IRC, park.
