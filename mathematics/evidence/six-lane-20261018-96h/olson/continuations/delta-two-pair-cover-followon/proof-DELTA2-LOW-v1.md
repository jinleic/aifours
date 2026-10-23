# DELTA2 LOW v1 - kappa2 for every prime p>=7

CANDIDATE written mathematics by hand, drafted after `/bin/date`2026-10-21T20:06:08-0700.
No parent/model acceptance, scientific computation or enumerated search is claimed. All earlier method
exposure and permanent process qualifications remain. This is a fresh R=p+2 proof, not an enlarged R=p
or R=p+1 theorem. It uses the generic accepted CONNECT/LIGHT statements only at their literal scopes.

## 0. Exact theorem and source interface

THEOREM D2-LOW (candidate). Let p>=7 be prime, and let u be a word of length4p-2 over D_(2p) with EXACTLY
R=p+2 rotation letters in one NONZERO pair{rho_c,rho_-c}. Every maximal CYCLIC CONSTANT reflection block
has odd length. If kappa=p-1-sum floor(l_i/2)=2, then some EXACTLY2p positions in increasing ORIGINAL index
order have identity product. Any B, mixed or pure runs, genuine empty gaps and all reflection values remain.
No B<kappa, new rigidity, nonempty-gap, feasibility or inverse-avoidance premise is imposed.

Direct accepted interfaces (absolute path; WHOLE-file SHA256; inclusive original LF):
* FND own authority: /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-REFLHI-v5-parent-verdict-v1.md;
  13ee1ba86245fc549bd79c130a9fe15248ecc3fe9fc8428e875ca939c940a547;1-61, all mandatory bindings/errata.
* General setting/W: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/proof-REFLHI-arcs-v5.md;
  4e46374677e30bd7b306c6fcca9845a09b15daf93fa42a9f908d0beb8c8cff1c;37-47. W has GENERAL R, not R=p.
* Normalisation/Z0/P0: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/reflection/proof-K0star-r2.md;
  6681676e4f80018e792c7117ce9fc524a31aeb397c35880f57468ada9c0396e1;12-75, with its own K0/RED authority
  and the separately supplied current TheoremP own proof/acceptance/both errata. No RED transfer is used.
* CONNECT/LIGHT own authority: /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-RP-LIFT-parent-verdict-v1.md;
  e90b8be22a7bc06b0c20e305274436ceb48784e5a1844005437058d04dff8652;1-31, all seven bindings.
* Generic proofs: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/proof-Rp-integer-lift-v1.md;
  34cb5e007095b6d3c9c9eb91b2385c9e52cd94f78cd5b82c73bac8a31961df69;80-114(CONNECT),140-148(LIGHT).
* CONNECT worker overlay: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/proof-Rp-integer-lift-v1-erratum-1.md;
  298036b0977d23d7aef2be6eba5512ce3c2ba193826d9dff97ff3917d698a7cc;1-12. Decreasing a coordinate keeps
  the preceding gap>=1; it does not preserve its numerical value.

CONNECT says that proper nonempty patterns of exactly m cyclic intervals are connected by one-index toggles,
and every run index is toggled by some edge, whenever1<=m,2m<k. It is genuinely generic in k,m.
LIGHT says that n nonnegative weights on an n-cycle, n>=2f, admit an independent f-set of weight<=f/n times
the total, also for a disjoint union of paths. Both complete used proofs/own scopes travel in the packet.
The RP-LIFT THEOREM, its R=p FWIN/ILIFT/SIGN, RP2NE's theorem/SIGN-2Z and DELTA1 lemmas are NOT premises.
The new CRT window, integer lift and all sign steps below are proved afresh. No CJ/TRANSFER/S(p)/Lev/CT,
HK1/HIGH-CORE, PartII, ARC+/SEG or machine check is used by THIS new proof.

## 1. Avoider data at the actual R=p+2 domain

Assume u avoids. Normalise c=1,A>=B by the accepted order-preserving group automorphisms. Write
u=R_1S_1...R_kS_k, R_i preceding S_i, l_i=|S_i| odd, a_i/b_i the positive/negative rotation counts,
r_i=a_i+b_i, d_i=a_i-b_i, theta_i=y_(i-1)-y_i in Z_p, u_i=theta_i/2. Indices are cyclic and empty runs genuine.
Then F=3p-4, H=p-3 and k=F-2H=p+2=R. Z0 gives 0<=B<=2. TheoremP/P0 gives
 F+sum floor(r_i/2)<=3p-2, hence sum floor(r_i/2)<=2.                                       (1)
Let q be the number of nonempty runs, e=k-q the number of empty runs, v the number of nonempty EVEN runs.
Since R=k,
 e=R-q=sum_(nonempty i)(r_i-1)>=v, and v<=2 by(1).                                        (2)
No run purity is assumed; every odd nonempty r_i has odd d_i, including mixed runs.

## 2. Fresh fixed window and CRT equivalence

Put M=p-2, L=3, U=(p-1)/2. For every integer m in[L,U],2m<=p-1<k and CONNECT applies.
For EVERY integer E in[0,R], not merely E<=p,
 gamma_m(E)=min(p-m,E-kappa+m-1,floor(E/2))=floor(E/2):
 E-kappa+m-1=E+m-3>=E>=floor(E/2), and p-m>=(p+1)/2=floor(R/2)>=floor(E/2).
Thus every proper nonempty pattern P with L<=m(P)<=U has the SAME floor-type W interval
 I(P)=[-floor((R-E(P))/2),floor(E(P)/2)], E(P)=B+sum_(i in P)d_i in[0,R].                    (3)

Let C=Z/(2p)Z and let e0:Z_p->C be the UNIQUE EVEN lift, explicitly e0(t)=(p+1)t modulo2p.
It is well-defined/additive because p+1 is even and p(p+1) is divisible by2p. Define
 alpha_i=e0(theta_i)-d_i, psi(P)=-B+sum_(i in P)alpha_i=e0(2u_P)-E(P) in C.
Since sum theta_i=0 and D=A-B,
 sum alpha_i=-D in C.                                                                    (4)
The W condition u_P in I(P) modp is EQUIVALENT to psi(P) having an integer representative in[-R,0].
Indeed the forward condition gives even t=2j in[-(R-E),E], with class e0(2u_P); then t-E is such a
representative. Conversely if s in[-R,0] represents psi, then t=s+E represents the even class e0(2u_P),
so t is even, lies in[-(R-E),E], and t/2 belongs to I(P) and is congruent to u_P modulo p.
R=p+2<2p, so the classes outside[-R,0] are exactly the integers[1,2p-R-1]=[1,p-3]=[1,M-1].
Avoidance therefore gives a unique representative
 N(P) in[1,p-3] for EVERY P in each F_m, L<=m<=U.                                          (5)

## 3. Fresh integer increments; all parity and size information

An edge adding index i changes N by an integer representing alpha_i and lying in[-(p-4),p-4]. This
interval has2p-7<2p integers, so at most one represents alpha_i. Every index has an adding edge by CONNECT
(orient its toggling edge the other way if necessary). Call its unique integer h_i. The same bound and
congruence apply on ALL layers m in[L,U]; all adding edges have increment h_i, all removing edges -h_i.
CONNECT yields a constant c_m on each layer with
 N(P)=c_m+sum_(i in P)h_i. No equality of c_m across layers is asserted or needed.
P and P^c lie on the same layer, hence(5) gives
 abs(sum_(i in P)h_i-sum_(i notin P)h_i)<=p-4 for EVERY 3<=m(P)<=U.                         (6)
Also h_i represents alpha_i, |h_i|<=p-4, and
 sum h_i=-D modulo2p.                                                                    (7)

Each h_i has parity d_i, hence parity r_i. An empty run has theta_i!=0, so its h_i is a NONZERO EVEN
integer with |h_i|>=2. An odd run has odd nonzero h_i. A zero h_i must belong to a nonempty even run.
Let z be the number of zeros, E0 the empty-run set(|E0|=e), and Z0 the zero set(|Z0|=z). Then
 e>=v>=z, z<=2; E0 and Z0 are disjoint. Put w_i=|h_i| and S=sum w_i.
Pointwise w_i>=1+1_(i in E0)-1_(i in Z0); the additional v-z nonzero even runs contribute at least one more.
Consequently
 S>=k+e+v-2z>=k=p+2.                                                                     (8)
S is ODD because sum|h_i|=sum h_i=sum d_i=R modulo2.                                        (9)
If S=k, equality in(8) forces e=v=z; every odd nonempty run has r_i=1, every even nonempty run r_i=2
(by(2)), odd-run labels have magnitude1, empty labels magnitude2, even nonempty labels are0. In particular
ALL weights are<=2 in this equality case.                                                   (10)
This equality structure is derived, not a unit-label assumption on the original target.

## 4. New LOW sign lemma, including p7

Claim. Unless ALL nonzero h_i have one sign AND S=k, there is a sign vector s_i in{+1,-1} with exactly2m
cyclic changes for some3<=m<=U and sum s_i h_i>p-4, contradicting(6).

Start with s_i=sign(h_i) on nonzero labels and either sign at zeros; the signed sum is S. Let2m0 be its
cyclic change count (m0=0 for one sign throughout). If the nonzero labels have both signs then EVERY
assignment at zeros has m0>=1. We prove all cases; in the remaining one-sign case take the same sign at zeros.

A. 3<=m0<=U. The starting signs work: S>=p+2>p-4.

B. m0>U. Since k=p+2 is odd, m0<=floor(k/2)=(p+1)/2=U+1, so m0=U+1. Among its2m0 nonempty constant-sign
stretches choose one of weight<=S/(2m0). Flip that whole stretch. Its two neighbours had the opposite sign,
so exactly two boundaries disappear, leaving2U changes (2m0>=8). The new sum is at least
 S(1-1/m0)=S U/(U+1)>p-4,
since S>=p+2 and (p+2)(p-1)/(p+1)=p-2/(p+1)>p-4. Zero-weight stretches cause no problem.

C. m0=1 or2, except temporarily p7,m0=2. Put f=3-m0. Let J be the union of the interiors of the2m0
constant-sign stretches. Each stretch excludes at most two endpoints, so n=|J|>=k-4m0.
If p>=11,m0=1 then n>=p-2>=9>2f=4; if p>=11,m0=2 then n>=p-6>=5>2f=2;
if p7,m0=1 then n>=5>4. Thus gamma=2f/n<1 in every current case.
LIGHT on these disjoint paths supplies an independent f-set Phi in J with weight<=f/n times W_J.
Original-cycle adjacency between two interior vertices lies in one such path: stretch endpoints are
excluded. Flipping Phi therefore adds EXACTLY2f boundaries, giving6=2L changes.
Write e_J=|E0 intersect J|,z_J=|Z0 intersect J|. The new signed sum is at least
 W_(J^c)+(1-gamma)W_J
 >= k+e-z-2f-gamma e_J+gamma z_J
 >= k-2f-z+(1-gamma)e
 =p-4+2m0-z+(1-gamma)e >p-4.                                                             (11)
Strictness: m0=2 gives2m0-z>=2; m0=1,z<=1 gives2m0-z>=1; m0=1,z2 gives e>=2 and1-gamma>0.
No e>z premise is assumed. The nonnegative-weight lower bounds are valid because1-gamma>0.

D. p7,m0=2 (the missing small-prime case). Four stretches cover9 vertices, so one has length>=3, yielding
an interior vertex. Flip that single vertex, adding two boundaries and obtaining6 changes.
If S>9, oddness(9) gives S>=11 and its weight<=|h_i|<=p-4=3, so the new sum>=11-6=5>3.
If S9, equality structure(10) gives weight<=2, so the new sum>=9-4=5>3. No LIGHT assertion with n1 is used.

E. m0=0. LIGHT on the full k-cycle with f3 (k>=9>=6) gives an independent three-set of weight<=3S/k.
Flipping it gives exactly6 changes and signed sum>=S(1-6/k)=S(p-4)/k. This is>p-4 when S>k.
If S=k this is the sole unexcluded case, with all nonzero h_i of one sign. The claim is proved. []

The positive set P={i:s_i=+1} of the obtained signs is proper nonempty with m(P)=m; its signed sum is the
left expression in(6), so(6) is contradicted. We are left only with the one-sign S=k case of(10).

## 5. The one-sign minimum case: B0/1/2 are ALL excluded

Here e=v=z<=2, all odd nonempty runs are singletons, all even nonempty runs have2 letters/label0, and
all nonzero h_i have one sign. Since S=k=p+2, their total is either +(p+2) or -(p+2).
Equation(7), with D=p+2-2B and 0<=B<=2, implies:
* positive total: sum h_i+D=2p+4-2B is divisible by2p ONLY if B2;
* negative total: sum h_i+D=-2B is divisible by2p ONLY if B0.
Thus B1 is impossible; B2 forces the positive sign, B0 the negative sign. These are exact congruences,
not an imported R1 label classification. There is at least one positive singleton run: A=R-B>=p,
at most2v<=4 rotation letters lie in the even runs, so at least p-4>=3 positive letters lie in singleton runs.

B2, all positive labels. Choose such a positive singleton i. Then d_i=1,h_i=1, so
 e0(theta_i)=h_i+d_i=2 modulo2p; theta_i=2 modulo p and u_i=1.
For P={i}, m1,E(P)=B+d_i=3,E-=R-3=p-1. At kappa2,
 gamma_1(3)=min(p-1,1,1)=1,
 gamma_1(p-1)=min(p-1,p-3,(p-1)/2)=(p-1)/2.
The W interval[-(p-1)/2,1] contains u_P=1. This gives the forbidden identity2p-subword.

B0, all negative labels. Every singleton has d_i=1,h_i=-1, so theta_i=0,u_i=0.
If e>=1, choose an empty index j. Its h_j=-2,d_j=0 imply theta_j=-2,u_j=-1.
There are k-2v>=p-2>=5 positive singleton runs. At most two are cyclic neighbours of j, so choose a
nonadjacent singleton i. P={i,j} has exactly m2 intervals, E(P)=1,E-=p+1 and u_P=-1. Directly,
 gamma_2(1)=min(p-2,0,0)=0,
 gamma_2(p+1)=min(p-2,p,(p+1)/2)=(p+1)/2.
Its W interval[-(p+1)/2,0] contains -1, again forbidden.
If e0, then v=z0, every rotation run is a singleton and theta_i=0 for EVERY i. All reflection-block
values y_i are equal, hence all F=3p-4>=2p reflection letters are one sigma_y. Any2p of them have product
sigma_y^(2p)=1 in original index order. This is also forbidden.
All exceptional cases are excluded; the assumption that u avoids is impossible. This proves D2-LOW. []

## 6. Scope and process boundary

The fixed window was proved for the ACTUAL R=p+2 and EVERY E in[0,p+2]; the singleton/two-index W tests
in Section5 are outside the fixed layers and were separately evaluated, not assumed to have the same window.
The m0=2,p7 sign step is explicit. No neutral-even count was silently made strict. No new proof assumes
unit labels, same-sign labels, run purity, B<kappa or nonempty gaps; the exceptional shape was derived only
from equality in the necessary count. Increasing-original-index order follows throughout from W and cyclic
conjugation: a selected product UV=1 remains VU=U^(-1)(UV)U=1 across the restored cut. Normalisation maps
identity products bijectively and never changes the selected index order.

This theorem covers the whole mandatory D2-LOW family, not the full DELTA2 target by itself. Other kappa
values require the separate arc-cover proof/baseline union. Parent alone controls reviews and acceptance.
All derivation is by hand; no scientific code, mathematical enumeration, assertion, solver, tests, Lean,
model/native/network/nested agent or old-file mutation. The1674s checkpoint gap remains a474s target miss
below1800, not erased by a delayed intermediate clock. No novelty/preregistration/corroboration claim.
