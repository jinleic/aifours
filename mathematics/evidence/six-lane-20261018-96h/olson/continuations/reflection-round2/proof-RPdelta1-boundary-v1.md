# RP-2NE delta=1: the upper endpoint kappa=(p-3)/2 (new candidate boundary proof)

OlsonReflectionSuccessor.  Frozen after /bin/date observation 2026-10-19T09:03:54-0700.  CANDIDATE_UNVERIFIED, written only:
no computation, finite search, model call, test/build or scientific process.  Scope: scope-RPdelta1-boundary-v1.md,
9137410530bb8ef109dbc10987d615661252fa9bb232c60ecd8e9d25ce2df6e1.  No existing candidate, receipt or snapshot is changed.

## 1. Exact new statement and accepted inputs

**Theorem D1-END (candidate).**  For every prime p>=7, let w have length4p-2 over D_(2p), with exactly R=p+1 rotation letters,
all in one nonzero pair {rho_x,rho_-x}.  Suppose every maximal cyclic CONSTANT reflection block has odd length, and
   kappa:=p-1-sum_i floor(l_i/2)=(p-3)/2.
Then w contains exactly2p letters in increasing ORIGINAL index order whose ordered product is identity.
ANY B, no run-purity, B<kappa, inherited condition or reflection-value restriction.  In particular the new smallest cell
is p=7,kappa=2,R=8.  p=5,kappa=1 is NOT claimed.

This is a new boundary beyond the accepted RP-2NE upper limit (p-5)/2, not an automatic application of that theorem or of
a reviewer's optional suggestion.  The difference in its LIGHT endpoint is checked explicitly in Sec.3.

Accepted authority (read in full, whole-file SHA checked before this slice):
* V2NE: RUN/review/olson-RP2NE-parent-verdict-v1.md,
  320d817a4b24d2c39f04806ce84ab1977fd68f5869b8c7be0da5184d166d2eab, all FIVE bindings.  Source proof-RPdelta-two-neutral-v1.md
  e6471758f0e5aaba016286ccfb0e901ecb5fc670b980728407c9bbd468c8fa20.  Import only its definitions, fixed-window calculation
  and zero-increment criterion at their proved algebraic scopes; the changed boundary inequalities are re-derived below.
* VL: RUN/review/olson-RP-LIFT-parent-verdict-v1.md,
  e90b8be22a7bc06b0c20e305274436ceb48784e5a1844005437058d04dff8652, all SEVEN bindings.  Source proof-Rp-integer-lift-v1.md,
  34cb5e007095b6d3c9c9eb91b2385c9e52cd94f78cd5b82c73bac8a31961df69.  CONNECT: the pattern graph F_m is connected and every
  run index is toggled for 1<=m and 2m<k; LIGHT: an independent f-set of nonnegative weight at most f/n times total exists
  for n>=2f on a cycle or a union of paths.  No strict n>2f requirement is part of LIGHT.
* V5: RUN/review/olson-REFLHI-v5-parent-verdict-v1.md,
  13ee1ba86245fc549bd79c130a9fe15248ecc3fe9fc8428e875ca939c940a547, full governing overlays/bindings.  Import W and Fact2.1
  at the all-odd setting(S), and P0 directly from K0star-r2:73-75
  (6681676e4f80018e792c7117ce9fc524a31aeb397c35880f57468ada9c0396e1), accepted under verdict
  879aeee781a080d1b1cb4a4489f62e45e2fa332f7c2d9242f725cfae1d00c02a and carried into v5.  P0 states e_R<=e_F+2kappa,
  including empty runs as even; its all-odd consequence is o_R>=k-2kappa.
RUN/ means /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/.
No SEG-k/TRANSFER/region-B/B-prime or STAB candidate is used.  The unsent zero-sign addendum (which weakens e>z) is NOT an
import: this proof retains e>z exactly, as required by V2NE binding4.

## 2. Fixed window, CONNECT and zero counts at the boundary

Normalise x=1 and A>=B by the accepted automorphisms.  In the maximal cyclic decomposition R_i precedes constant block S_i;
r_i=a_i+b_i, d_i=a_i-b_i, theta_i=y_(i-1)-y_i in Z_p and u_i=theta_i/2.  Empty runs are genuine (theta_i!=0 there).
Put
   M:=p-1 (EVEN, >=6),   k=M+2kappa=2M-2=2p-4,
   L:=kappa+1=M/2,   U:=p-floor(R/2)=p-(p+1)/2=M/2=L.
Thus just ONE layer m=L is used.  2m=M<k=2M-2, so CONNECT applies, including complements and a toggling edge for EVERY run.
For every integer E in [0,R], ceil(E/2)>=0=kappa+1-m and floor(E/2)<=floor(R/2)=(p+1)/2=p-m.  Fact2.1 therefore gives the
floor-type window
   I(P)=[-floor((R-E(P))/2),floor(E(P)/2)],   E(P):=A_P+B_(P^c), 0<=E(P)<=R.
W's implication is at exactly this window; no false E<=p bound is assumed (R=p+1 here).

Let C=Z/(2p)Z, e(theta) the UNIQUE even class congruent to theta modp (equivalently (p+1)theta mod2p).  Define
alpha_i=e(theta_i)-d_i, psi(P)=-B+sum_(i in P)alpha_i=e(2u_P)-E(P).  The even-integer test from V2NE gives:
u_P hits I(P) iff psi(P) has a representative in [-R,0] (even t in [-(R-E),E], then s=t-E; conversely t=s+E is even).
The complementary classes are exactly [1,2p-R-1]=[1,M-1].  Thus an avoider gives N(P) in [1,M-1] representing psi(P)
for every P in F_m.
Every adding-edge increment represents alpha_i and lies in [-(M-2),M-2], a set of 2M-3=2p-5<2p integers.  CONNECT's edge
existence and that uniqueness define h_i in this interval for EACH i; every edge adding i has increment h_i, a removing
edge -h_i.  Connectivity yields N(P)=c+sum_(i in P)h_i, with one constant c on the sole layer.  P^c is in the same layer, so
   abs(sum_(i in P)h_i-sum_(i notin P)h_i)<=M-2,     for EVERY P in F_m.                                      (1)
No R=p-only nonzero-increment conclusion is borrowed.  Zero increments are exactly d_i even and theta_i=d_i modp.
They are confined to NONEMPTY EVEN rotation runs: an empty run has d_i=0, theta_i!=0, and therefore even nonzero h_i.
Let z=#zero increments, v=#positive even runs, o=#odd runs, q=o+v, e0=g_E=k-q=#empty runs.  P0 gives o>=k-2kappa=M;
R>=o+2v gives v<=1, hence z<=1.  Also q<=R-v, so
   e0-z>=k-R+(v-z)=p-5+(v-z)>=p-5>=2.                                                                      (2)
The empty-run indices form a marked set Z of e0>z indices disjoint from the zeros, with abs(h_i)>=2 there.  Every other
nonzero h_i has abs(h_i)>=1.  Thus S=sum_i abs(h_i)>=k+e0-z>k.  These counts require no purity or B<kappa assumption.

## 3. Endpoint sign lemma (new, all cases)

**Lemma SIGN-1Z-END.**  Let M>=6 be EVEN, k=2M-2, kappa=M/2-1 and m=M/2.  Suppose integers h_i on the k-cycle have z<=1
zeros and a marked set Z of e0>z nonzero indices with abs(h_i)>=2 (all other nonzero magnitudes>=1).  Then there are signs
s_i with exactly2m=M cyclic changes and sum_i s_i h_i>M-2.
Proof.  Set w_i=abs(h_i), S=sum w_i>=k+e0-z>k.  Initially choose s_i=sign(h_i) on nonzero indices and either sign at a zero;
this gives signed sum S.  Let 2m0 be its cyclic sign-change count.

A. m0=m.  The initial signs have the required changes and sum S>k>M-2.

B. m0>m.  The 2m0 maximal constant-sign stretches alternate; same-parity stretches are nonadjacent since m0>=m+1>=4.
At most z stretches have weight0; S>=2m0-z.  Choose the lighter family of m0 same-parity stretches, weight<=S/2, and flip
the f=m0-m lightest members.  They are nonadjacent and f<m0; exactly2f boundaries disappear (each boundary touches at most
one flipped stretch), leaving 2m changes.  The flipped weight is <=f S/(2m0), so the signed sum is >=S m/m0.
If z=0 this is >=2m=M.  If z=1 it is >=2m-m/m0>M-1.  In both cases it exceeds M-2.

C. 1<=m0<m.  Put f=m-m0>=1.  Let J be the indices strictly interior to their initial stretches (both neighbours share
the same initial sign).  Since each of the 2m0 stretches has at most two noninterior vertices,
   n:=|J|>=k-4m0,   n-2f>=M-2-2m0>=0,
where the last inequality uses m0<=m-1=M/2-1.  Thus n>=2f>=2, including the BOUNDARY n=2f; LIGHT applies with a
NONNEGATIVE, not necessarily positive, coefficient 1-gamma, gamma:=2f/n<=1.  J's interiors form disjoint paths;
original-cycle adjacency between two interior vertices stays inside one such path (VL binding5).  Choose an independent
Phi subset J, |Phi|=f, of weight<=f/n times W_J and flip it.  Each flipped vertex has its same-sign old neighbours unflipped,
so each adds two boundaries, leaving exactly2m.  Let e_J=|Z intersect J|, z_J=#zero indices in J.  From the pointwise bound
w_i>=1+1_(i in Z)-1_(h_i=0), the signed sum is >=
   W_(J^c)+(1-gamma)W_J
   >=k+e0-z-2f-gamma e_J+gamma z_J
   >=k-2f-z+(1-gamma)e0
   =M-2+2m0-z+(1-gamma)e0.
Now 2m0-z>=1 (m0>=1,z<=1).  The last expression is therefore >M-2 even if gamma=1 and the marked-weight term vanishes.
This is the NEW boundary reason; it does not claim that accepted SIGN-2Z's strict coefficient stays positive here.

D. m0=0.  Apply LIGHT to the full cycle with f=m=M/2, n=k=2M-2 (n>=2f as M>=2).  The independent flip set has weight
<=mS/k, so flipping it creates exactly2m changes and a sum >=S(1-2m/k)=S(M-2)/k>M-2 by S>k and M-2>0.
All cases give the claimed sign vector.  []

Applying this lemma to the h_i of Sec.2, the positive set P of the resulting signs is in F_m, but its signed sum exceeds
M-2, contradicting (1).  Hence the assumed avoider cannot exist.  This proves D1-END.  []

## 4. Exact added cell and middle I.14 gaps (no pending candidate counted)

Only accepted numerical coverage of V5 I.14 and accepted RP-2NE (V2NE) is used in this comparison.  SEG-k/TRANSFER/region-B/
B-prime remain outside it, regardless of what their running reviews may eventually establish.
For R=p+1 (delta1), accepted RP-2NE gives [2,(p-5)/2]_Z for p>=11; I.14 SEG-num is inside that low band.  I.14 K2P+
gives [(p+3)/2,p-4]_Z, interpreted as empty if its lower endpoint exceeds its upper one.  D1-END adds exactly
   kappa=(p-3)/2,   k=2p-4,   R=p+1,   p>=7,
which lies in neither accepted band.  For p=7 this is kappa2; for p11 it is kappa4; no pre-existing lower RP-2NE band is
assumed at p7.  Conditional on accepting this NEW boundary theorem, for EVERY p>=11 the remaining universal R=p+1 values
among feasible residual kappa>=2 are exactly
   kappa in {(p-1)/2,(p+1)/2} union {p-3,p-2,p-1}.                                                          (3)
In particular the MIDDLE gaps are the TWO points (p-1)/2 and (p+1)/2.  The point (p-3)/2 is the endpoint closed here,
not an accepted consequence of a review comment.  At p7 the middle/top sets overlap and the remaining set is {3,4,5,6};
at p5 this proof does not apply and delta1 has no new universal coverage.

For comparison R=p+2 (delta2) is UNCHANGED by this file.  For p>=11 its accepted low band is [3,(p-5)/2]_Z and its
I.14 high band is [(p+3)/2,p-5]_Z, with SEG-num inside the low band.  The remaining residual values are exactly
   {2} union [(p-3)/2,(p+1)/2]_Z union [p-4,p-1]_Z,                                                        (4)
with overlaps counted once.  Thus delta2 still has THREE middle points (p-3)/2,(p-1)/2,(p+1)/2, plus kappa2 and the top
four points.  This is a numerical-ledger comparison, not realizability or existence of avoiders; accepted structural
criteria and the B=0 slice may exclude individual words there.

The new result is all-odd length4p-2 solvability at exactly delta1's one upper-kappa boundary.  It is not unrestricted
REFL(p), INV*, arbitrary rotation rigidity, a local padding rule, formal verification or priority.  The independent
(delta2,kappa2) question is not used, weakened into scope, or answered by this proof.

## 5. Review focus

Recheck the sole layer L=U=M/2, M even>=6, 2m=M<k=2M-2; n>=2f>=2 and equality n=2f in CaseC; z<=1 and e0-z>=p-5>=2;
strictness from 2m0-z>=1 without weakening e0>z; all four sign cases; the unique even lift and E(P) in [0,p+1] rather than
[0,p]; and exact complement-ledger equations(3),(4).  Parent owns dual reviews and final verdict.  No computational aid.
