# RUH3 checkpoint 001: uniform missing-set lemma derived; position endgame partially uniform

Owner OlsonPP1Exclusion. /bin/date 2026-10-19T17:36:42-0700. Scope frozen 17:30:02 (RUH3-scope-v1.md SHA256
c6601f27ab4b1752b7d76ae769c1c1229160367b20b8da0ba4ab60a138815bbb). Hand derivation only; nothing frozen yet.

Derived in notes (CANDIDATE, unfrozen), SH range, e<=c<=2e-1, mu=floor(c/2):
- Case I (c even, or c odd <=2e-3): the all-plus block B0 (mu elements, plus e-mu-1 for odd c) meets every forced interval
  F(Y)=t(Y)+[max(m,e-mu), m+e-1] (sizes add to c+1), so all forced residues lie in ONE integer interval U=[L,R'] inside [1,p-1]
  with |U|<=c. Integer lifts tau(Y) of the empty-run sums are ADDITIVE for all Y with m(Y)<=e (the defect D satisfies
  2-e-eps<=D<=2e-2<p), and tau(Y) lies in [l0-max(0,m-e+mu), r0+1-m] with r0-l0<=mu+eps-1, l0<=-eps, r0>=-1.
  Consequences: no set of negative empty runs has m>=e-mu (L>=1), so their independence number is <=e-mu-1; positive ones
  satisfy |Y|+m(Y)<=r0+1<=mu; E<=mu-1 (all positive), <=mu+eps-1 (mixed), <=mu+eps (all negative).
- Case II (c=2e-1): two-piece exclusion of t>=e, then all t in [1,e-1], s(Y)+m(Y)<=e, E<=e-1.
- Position endgame: with I = an independent set of empty runs not adjacent to Q and D = alternate interior drops in the
  Q-blocks, Lemma L gives a contradiction whenever min(e, 2(m(Q)+|I|+|D|)-1) >= E+|D|; this closes every case with
  E <= (e-1)/2 + m(Q) + iota and enough interior Q-drops; the remaining corner is E large with few separators.
- Blocker: the corner E > (e-1)/2 + m(Q) + iota (only possible for larger mu); deciding whether the missing-set structure
  (clustered empty runs give interior separators) closes it uniformly. Next bounded action (<=30 min): settle the corner or
  freeze the M-lemma + position partial with the exact smaller residual.
