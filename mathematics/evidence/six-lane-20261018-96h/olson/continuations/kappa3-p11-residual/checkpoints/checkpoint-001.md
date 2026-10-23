# P11R checkpoint 001: residual structure derived; framework on P-split sets under study

Owner OlsonPP1Exclusion. /bin/date 2026-10-20T00:03:06-0700. Scope P11R-scope-v1.md SHA256
14701fd9860d6b4288c4373f683cca6883273c7cd433322a5af81f0b61c9e00c frozen 23:55:39 before derivation. Written only; no computation.
Derived in notes (CANDIDATE, unfrozen), p=11, kappa=3, N=12, R=16:
- Frame (from accepted PL IF/LT, re-derived explicitly): t in {0,1,2}; #1>=11; u+>=8; every |c|<=7; Lemma N3 at p=11
  (A- in {{},{-1},{-1,-1},{-1,-1,-1},{-3},{-3,-1},{-5}}).
- New structural fact: c=-b on P0, so every P0-letter with b>0 is negative; hence letters(P0) are at most |A-|<=3 negative
  letters plus at most two positive letters with b<0 (the ZSTRUCT -1/-3 labels): the light T=0 arc carries <=5 letters; C0 is
  heavy (o(C0)>=8), so the frame is forced once the T=0 arc is chosen.
- Residual run classes: P-runs (k_P>=3 by Theorem P (S1)), N-runs (<=3, pure negative), empty runs (E>=1, E<=6).
- Fullness at p=11: m in {3,4} patterns are full iff X^(Q) two-signed; bad sets are exactly letters(Q)=A- or letters(Q^c)=A-;
  "P-split" sets (meeting P and missing a P-run) are good.
- Lift bounds: for full sets U' in [B*-nu0-21, -1-nu0]; every increment |d|<=20-B*. B*=20 forces U'=-1-nu0 for every full set,
  contradicting Lemma A on any disjoint full pair with full union; so B* in {16,18} once such a pair exists.
Blocker: the sorting step needs the top sets of the alternating sets to be in one connected family of full sets; in the
residual they may carry no P-run. Next bounded action (<=30 min): decide between a bounded framework proof on P-split sets
(connectivity by swaps) with a decomposition/sorting finish, and an exact-obstruction note; then freeze.
