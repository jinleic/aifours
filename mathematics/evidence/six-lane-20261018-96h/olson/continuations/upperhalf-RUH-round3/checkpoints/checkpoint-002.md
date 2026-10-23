# RUH3 checkpoint 002: R2 closes by hand (candidate); writing the proof; R1 next

Owner OlsonPP1Exclusion. /bin/date 2026-10-19T17:47:50-0700. Previous checkpoint-001.md SHA256
7c8baf99c4d3f584744254f90c306b287e6e5ae8516de7135ec9aa5ae349cf70 (17:36:42). Hand derivation only; nothing frozen yet.

Derived (CANDIDATE, unfrozen), SH range p>=13, 5<=e<=(p+2)/3, e<=c<=2e-1, mu=floor(c/2), eps=c-2mu:
- Missing-set lemma, Case I (c<=2e-2): B0=[e-mu-eps,e-1] in M; the component U=[L,R'] of M containing B0 (1<=L, |U|<=c)
  contains every forced interval t(Y)+[max(m,e-mu),m+e-1] (|U|+|F|>=c+1); unique integer lifts, additive (|defect|<p);
  for every Y with m(Y)<=e: l0-max(0,m-e+mu) <= sum_Y theta <= r0+1-m, l0=L-e+mu in [1-e+mu,-eps], r0<=l0+mu+eps-1.
  Positive empties: E+<=max(0,r0); negative: m(Y-)>=e-mu impossible, E-<=-l0; so E<=ceil(c/2)-1.
- Case II (c=2e-1): t>=e forces M = two pieces, all t equal, a pair contradicts; so t in [1,e-1], U=[1,R'] with R'>=e+1,
  additive lifts, |Y|+m(Y)<=e, E<=e-1.
- Position lemma (uniform): with Lemma L, E+|Q|>=c+1, c<=2e-1, E<=e-1 and 3E<2(c+1): contradiction. P=Q u I (I = every
  other Q-free position of each empty cluster) has 2m(P)-1 = E+2r_Q-1+o_FF+o_QQ-o_FQ >= E-1; equality case: a Q-block of
  length>=2 trades its first run for the preceding empty; all Q-blocks singletons force E>=2|Q|, i.e. 3E>=2(c+1).
- Hence R2 (and uniformly e<=c<=2e-1 for every e>=5 in the SH range) is excluded; c<=e-1 by re-deriving RUH2 Theorem A.
Next: freeze proof-RUH3-v1.md (all RUH2 inputs re-derived inline), then attack R1 (3e>p+2).
