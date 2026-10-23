# DELTA3 LOWER v1 - the whole lower family and the p7 kappa3 cell

Clock observed2026-10-21T23:03:47-0700 before exclusive creation; reasoning/drafting began earlier.
CANDIDATE written mathematics by hand, NOT reviewed/accepted. Complete derivations below were written
after Main acknowledged the delivered Step0 gate. Premature pre-gate observations and the independent
1945s hard-cadence breach remain TWO PERMANENT PROCESS MAJORs, fully preserved in errata1-3/checkpoints.
This proof does not cure them, assert independent discovery, or enlarge an R2 lemma by analogy.

## 0. Exact statement and direct accepted interfaces

C3(p,kappa): p>=7 prime; a word w of length4p-2 over D_(2p), EXACTLY R=p+3 rotations in ONE NONZERO
pair{rho_c,rho_-c}, all maximal CYCLIC CONSTANT reflection blocks odd, kappa=p-1-sum floor(l_i/2) in[2,p-1].
Identity means EXACTLY2p positions in increasing ORIGINAL index order. Any B, mixed/pure runs, genuine
empty gaps, all reflection values and all odd-block pairs remain. No B<kappa/purity/original-o_F/nonempty-
gap/rigidity/feasibility/inherited hypothesis or inverse-avoidance transport.

THEOREM D3-L (candidate). Every C3(p,kappa) word has such an identity subword if
 (A) p>=11 and3<=kappa<=(p-3)/2, OR (B) p7 andkappa3.
Kappa2 is OLD K2/P7L NF coverage as verified in the baseline audit, NOT a claim of this new proof.
This theorem covers the entire unbounded lower gap, not only the mandatory kappa3 diagnostic. Larger
kappa require the separate arc proof; no wider R/REFL/INV*/full-Olson/p5 statement is asserted.

General group convention: (v,eps)(v',eps')=(v+eps*v',eps*eps'),rho_x=(x,+1),sigma_y=(y,-1).
The direct inputs below are accepted at their ORIGINAL scopes, with ALL actual mandatory readings:
* General FND own authority: /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-REFLHI-v5-parent-verdict-v1.md;
  WHOLE SHA25613ee1ba86245fc549bd79c130a9fe15248ecc3fe9fc8428e875ca939c940a547;LF1-61.
* General W/setting: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/proof-REFLHI-arcs-v5.md;
  4e46374677e30bd7b306c6fcca9845a09b15daf93fa42a9f908d0beb8c8cff1c;37-47, through own bindings/errata1-5.
* GR0/H0/Z0/P0/normalisation: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/reflection/proof-K0star-r2.md;
  6681676e4f80018e792c7117ce9fc524a31aeb397c35880f57468ada9c0396e1;12-75, with its own authority,
  complete used GRX criterion/own M2 convention, and current TheoremP OWN proof/acceptance/both errata.
* Generic CONNECT/LIGHT own authority: /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-RP-LIFT-parent-verdict-v1.md;
  e90b8be22a7bc06b0c20e305274436ceb48784e5a1844005437058d04dff8652;1-31, all seven bindings.
* Generic proof bodies: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/proof-Rp-integer-lift-v1.md;
  34cb5e007095b6d3c9c9eb91b2385c9e52cd94f78cd5b82c73bac8a31961df69;80-114(CONNECT),140-148(LIGHT).
* Worker CONNECT overlay: /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/reflection-round2/proof-Rp-integer-lift-v1-erratum-1.md;
  298036b0977d23d7aef2be6eba5512ce3c2ba193826d9dff97ff3917d698a7cc;1-12. A decreasing coordinate
  keeps the preceding gap>=1; it does not preserve its value.
All ranges are ORIGINAL LF, hashes WHOLE-file. The actual direct bodies/own statements/corrections travel
in the final packet. No whole-pasted claim follows merely from these pins.

CONNECT: for1<=m,2m<k, the proper nonempty k-cycle patterns with exactly m intervals form a connected
one-index-toggle graph, and every index is toggled by some edge. This is generic k,m, not R=p-only.
LIGHT: n nonnegative weights on a cycle, n>=2f, admit an independent f-set of weight<=f/n times total;
also on a union of paths by adding edges to concatenate it into a cycle. Both complete used proofs supplied.
NOT imported: RP-LIFT's R=p FWIN/ILIFT/SIGN, RP2NE's delta1/2 theorem/SIGN-2Z, DELTA1/DELTA2 R-specific
lemmas or sign estimates, S(p),Lev,CT,CJ/TRANSFER/RED/RGR,PartII,AR(R0),V/DAV or an enumerated computation.

## 1. Actual R3 word counts, even lift and a reusable edge argument

Assume w avoids. Normalise c=1,A>=B by order-preserving automorphisms. Write w=R_1S_1...R_kS_k with
S_i=sigma_(y_i)^(2g_i+1),rotation counts a_i,b_i,r_i=a_i+b_i,d_i=a_i-b_i,theta_i=y_(i-1)-y_i in Z_p,
u_i=theta_i/2. Empty R_i imply theta_i!=0. Let H=sum g_i=p-1-kappa. Put
 R=p+3,F=3p-5,M=2p-R=p-3, k=F-2H=M+2kappa.                                              (1)
M and k are EVEN. Z0 gives0<=B<=kappa. P/P0 at its actual N=4p-2,F>=1 domain gives
 F+sum floor(r_i/2)<=3p-2, hence sum floor(r_i/2)<=3.                                      (2)
Let q=#nonempty runs,e=k-q,#nonempty EVEN runs=v. Then v<=3 and
 e=k-R+sum_(nonempty i)(r_i-1)>=2kappa-6+v.                                                (3)
No purity/zero-free assumption is used.

Let C=Z/(2p)Z and e0(t)=(p+1)t modulo2p be the UNIQUE EVEN lift of t in Z_p; it is well-defined/additive,
since p+1 is even and p(p+1) is divisible by2p. For every proper pattern P define
 E(P)=B+sum_(i in P)d_i in[0,R], u_P=sum_(i in P)theta_i/2,
 alpha_i=e0(theta_i)-d_i, psi(P)=-B+sum_(i in P)alpha_i=e0(2u_P)-E(P).
Always sum alpha_i=-D in C, D=A-B, because sum theta_i=0.                                   (4)

When the W window is the FULL floor interval
 I(P)=[-floor((R-E)/2),floor(E/2)],
its success is equivalent to psi(P) having a representative in[-R,0]. Forward: take t=2j, j in I(P)
congruent to u_P; t is even in[-(R-E),E],represents e0(2u_P),and t-E represents psi in[-R,0].
Conversely s in[-R,0] representing psi gives even t=s+E in[-(R-E),E], so t/2 is in I(P) and congruent to u_P.
Thus the classes outside that interval have unique integer representatives in[1,M-1]. No E<=p restriction.

EDGE-LIFT argument (proved here, applied separately below). Suppose on one or more CONNECT layers every
psi(P) has a representative N(P) in an integer interval of width W0, with2W0+1<2p.
An adding-i edge has difference N(P union{i})-N(P) representing alpha_i in[-W0,W0]. That interval has fewer
than2p integers, so at most one represents alpha_i. Every index has an edge; orient it as adding i and
call that integer h_i. All adding-i edges, on ALL those layers, share h_i; removing edges have-h_i.
Connectivity gives a separate c_m with N(P)=c_m+sum_(i in P)h_i. Constants across layers need not agree.
Since P^c belongs to the same layer,
 abs(sum_(i in P)h_i-sum_(i notin P)h_i)<=W0.                                              (5)
Also |h_i|<=W0 and sum h_i=-D modulo2p. This argument needs ONLY the actually supplied N interval.

On every such application h_i has parity d_i, hence r_i. An empty run has nonzero even h_i, magnitude>=2;
an odd run has odd nonzero h_i. Zeros can occur only in nonempty even runs. Let z=#zeros,Z their set,
E0 the empty set(|E0|=e),w_i=|h_i|,S=sum w_i. Then z<=v<=3,E0 disjoint Z, and
 w_i>=1+1_(i in E0)-1_(i in Z),
 S>=k+e+v-2z>=k+2kappa-6+2(v-z)>=k.                                                     (6)
For kappa>=4, S>k. Equality S=k forces kappa3,e=v=z, and all pointwise weights minimal.
Since at kappa3 also k=R, equality in sum_(nonempty)(r_i-1)>=v forces ALL odd nonempty runs singleton,
ALL even nonempty runs of length2; odd labels have magnitude1,empty labels2,even nonempty labels0.          (7)
This is a DERIVED equality case, not a label/run hypothesis.

## 2. Interior lower family: p>=11, 3<=kappa<=M/2-1

Set L=kappa+1,U=M/2. For EVERY m in[L,U] and EVERY integer E in[0,R],
 E-kappa+m-1>=E>=floor(E/2), p-m>=p-U=R/2>=floor(E/2).
Hence gamma_m(E)=floor(E/2) at the ACTUAL R=p+3; all patterns on all these layers have the floor window.
Avoidance/Section1 gives N(P) in[1,M-1], of width W0=M-2. CONNECT applies since1<=m and2m<=M<k.
The edge-lift argument gives(5) with W0=M-2, because2M-3=2p-9<2p.

We prove a NEW signed-sum contradiction. Start s_i=sign(h_i) on nonzeros, arbitrary at zeros, with sum s_i h_i=S.
Let2m0 be the cyclic change count. If all nonzeros have one sign choose that same sign at zeros(m0=0).
If they have both signs, every choice at zeros has m0>=1. The following cases are exhaustive.

A. L<=m0<=U. The aligned signs already give S>=k>M-2, contradicting(5).

B. m0>U. Its2m0 maximal constant-sign stretches alternate. Choose the odd/even family of m0 stretches
with smaller total weight<=S/2, and flip f=m0-U lightest stretches in it. They are nonadjacent, f<m0,
so exactly2f boundaries disappear. The new m is U and the signed sum is at least
 S U/m0>=S(2U)/k=SM/k>=M>M-2, since2m0<=k. No bound on the number of zero-weight stretches is needed.

C. 1<=m0<L. Put f=L-m0. Let J be the union of stretch interiors, n=|J|>=k-4m0.
Then n-2f>=M-2-2m0>=M-2-2kappa>=0, so LIGHT applies to an independent f-set in these disjoint paths.
Interior adjacency in the original cycle lies in one such path(endpoints excluded), so flipping this set
adds EXACTLY2f boundaries and gives m=L. Write gamma=2f/n<=1,e_J=|E0 intersect J|,z_J=|Z intersect J|.
The new sum is at least
 W_(J^c)+(1-gamma)W_J
 >=k+e-z-2f-gamma e_J+gamma z_J
 >=k-2f-z+(1-gamma)e
 =M-2+2m0-z+(1-gamma)e.                                                                  (8)
If m0>=2,2m0-z>=1. If m0=1,z<=1 the margin is positive; if z2, e>=2 and gamma<1 below.
For m0=1,z3, n>=M+2kappa-4>3kappa, because M>=8 and kappa<=M/2-1<M-4.
Thus gamma=2kappa/n<2/3, and (1-gamma)e>e/3>=1, strictly. This also supplies gamma<1 for z2.
In every case the new sum>M-2. Boundary gamma1 at larger m0 is permitted: its coefficient is NONNEGATIVE,
and the separate margin2m0-z is already strictly positive; no false strict-interior premise is used.

D. m0=0. LIGHT on the full k-cycle with f=L gives2L changes(k>=2L) and sum>=S(1-2L/k)=S(M-2)/k.
This is>M-2 if S>k. If S=k the sole remaining case is the one-sign kappa3 equality structure(7).
Section5 below excludes that actual word. Thus the interior family is proved. []

## 3. Lower-middle endpoint: p>=11, kappa=M/2=(p-3)/2

Now k=2M=4kappa,kappa>=4,S>k by(6). Use ONLY m=kappa. Then p-m=R/2 and
 gamma_m(E)=min(E-1,floor(E/2)).
For1<=E<=R-1 both sides are full floors. At E0 the W interval is[-R/2,-1], which forbids every even
representative of psi in[-R,-2] but may permit psi0. At E=R its interval[1,R/2] forbids representatives
in[-R+2,0] but may permit psi=-R, whose class has representative M. Thus ALL patterns on this layer
have allowed N(P) in[0,M]. This is a relaxation, not an assertion that both endpoints are always allowed.

Its width W0=M has2M+1=2p-5<2p; CONNECT applies2m=M<k. Section1 gives integer increments and(5) with
bound M. We construct signs with exactly2kappa changes and signed sum>M.
If m0=kappa, S>k>M. If m0>kappa, the light-stretch construction of Section2B gives new sum
>=S*kappa/m0>=S(2kappa)/k=S/2>M.
If1<=m0<kappa, put f=kappa-m0,J interiors,n>=k-4m0=4f. Thus gamma=2f/n<=1/2. LIGHT adds2f boundaries,
and the same explicit weight calculation gives new sum
 >=M+2m0-z+(1-gamma)e >M.
For m0>=2 the first margin>=1. For m0=1,z<=1 it is positive; for z2 the e term is positive; for z3,
e>=2kappa-6+z>=5 and1-gamma>=1/2, so-1+(1-gamma)e>=3/2>0.
If m0=0, LIGHT with f=kappa on the k=4kappa cycle gives sum>=S/2>M. All cases contradict(5).
This proves the endpoint uniformly, including p11,kappa4. No interior-range RP2NE lemma is assumed. []

## 4. Small prime p7,kappa3: an independent relaxed layer and its critical sign case

Here R10,F16,H3,k10,M4. Use m3; CONNECT applies2m6<k10. Directly
 gamma_3(E)=min(4,E-1,floor(E/2)).
For1<=E<=9 both E and10-E have full floors. At E0, I=[-4,-1]; at E10,I=[1,4]. The CRT forbidden
representatives in either endpoint case are the even values in[-8,-2]; only classes0 and4 may be added
to the ordinary complement[1,3]. Hence every pattern on F_3 has allowed N(P) in[0,4].
Width4 has2*4+1=9<14; Section1 yields |h_i|<=4 and complement bound(5)<=4. Counts(6)-(7) still hold,
with S>=10,e>=v>=z,z<=3. We now produce exactly6 changes and signed sum>4.

If m0=3, aligned S>=10 works. If m0>3, flip m0-3 light same-parity stretches as above, giving sum
>=S*3/m0>=S*6/10>=6>4. If m0=0, LIGHT with f3 gives sum>=S(1-6/10); this is>4 unless S10.
That one-sign equality is excluded in Section5, not assumed absent.

For m0=1/2, put f=3-m0,J interiors,n>=10-4m0. Thus n>=6 with f2 or n>=2 with f1; LIGHT applies.
The exact lower calculation gives
 new sum>=4+2m0-z+(1-gamma)e, gamma=2f/n.
For m0=2,2m0-z>=1 even at gamma1. For m0=1,z<=2 the margin is strict as before.
For m0=1,z3, gamma<=2/3 and e>=3; strictness can fail in this estimate ONLY if n6,e3.
If S>10, at least one pointwise weight exceeds the baseline1+1_E0-1_Z; both coefficients1 and
1-gamma>=1/3 are positive, making the inequality strict. If S10,(7) gives e=v=z3 and minimal weights.
If e_J<3 or z_J>0, the previously discarded gamma(e-e_J+z_J) is positive, again giving strictness.
The sole critical case has n6,e_J3,z_J0,S10. Its six interior vertices contain THREE empty weights2
and THREE singleton weights1. Three vertices in a union of paths contain a nonadjacent pair(a path has
no triangle). Flip two such unit interior vertices. This adds4 boundaries, giving m3, and the new sum is
10-2(1+1)=6>4. No scientific enumeration or LIGHT with n1 is used.
All mixed-sign/nonminimal cases contradict(5); Section5 excludes the one-sign S10 exception. []

## 5. One-sign minimum kappa3, valid in BOTH interior and p7 proofs

Here k=R=p+3,S=k,all nonzero labels have one sign,and(7) holds:e=v=z<=3,odd runs singleton/even runs2,
odd labels magnitude1/empty labels2/even nonempty labels0. Let B be after valid A>=B normalisation;
Z0 gives0<=B<=3. Sum h_i=-D modulo2p,D=p+3-2B.
Positive labels give sum h_i+D=2p+6-2B, divisible by2p ONLY when B3.
Negative labels give sum h_i+D=-2B, divisible by2p ONLY when B0. Thus B1/2 are impossible.
These are actual congruences, not an R2 classification or an input unit-label hypothesis.

B3, all labels positive. At most2v<=6 rotation letters lie in even runs, so A=R-B=p supplies at least
p-6>=1 positive singleton. For such index i,d_i=1,h_i=1 imply e0(theta_i)=2,theta_i=2,u_i=1.
The SINGLETON pattern has m1,E=B+d_i=4 and E-=p-1. At kappa3,
 gamma_1(4)=min(p-1,1,2)=1,
 gamma_1(p-1)=min(p-1,p-4,(p-1)/2)=(p-1)/2 (p>=7).
Its W interval[-(p-1)/2,1] contains1, contradicting avoidance. This window is evaluated separately;
m1 is not silently included in the fixed layers of Sections2/4.

B0, all labels negative. Every singleton has d_i=1,h_i=-1,theta_i=0,u_i=0. If e>=1, choose empty j,
whose h_j=-2 implies theta_j=-2,u_j=-1. There are k-2v>=p-3>=4 positive singleton runs, and at most two
are cyclic neighbours of j. Choose a NONADJACENT singleton i. P={i,j} has m2,E1,E-=p+2,u_P=-1.
Directly gamma_2(1)=min(p-2,-1,0)=-1 and
 gamma_2(p+2)=min(p-2,p,(p+1)/2)=(p+1)/2.
The LITERAL W interval[-(p+1)/2,-1] contains-1, even though its upper endpoint is negative. No false
“window contains0” assumption is imposed here. This is a direct m2 test, not the full-floor CRT interval.
If e0, then v=z0, all rotation runs are positive singletons and theta_i=0 for EVERY i. All reflection
block values are equal; F=3p-5>=2p reflections of one sigma_y exist, and any2p of them multiply to1.
Thus every one-sign exception is impossible. The theorem D3-L is complete. []

## 6. Scope, logical and permanent process boundary

The theorem treats the ENTIRE stated lower family and the complete p7,kappa3 word class. All cases
retain arbitrary original B/mixed runs/genuine empty gaps and extra odd-block pairs; their restrictions
were derived from avoidance, not imposed. The endpoint/p7 relaxed intervals were proved at the actual
R/m/E ranges; neither is an old full-floor theorem applied outside its domain. Layer constants remain
local; no cross-layer constant equality, feasible relaxation, converse NF theorem or model verification.

Each W selection is cyclically restored to increasing ORIGINAL index order: UV=1 implies
VU=U^(-1)(UV)U=1 across the cut, with the same selected positions. The group automorphisms preserve
identity and index order. The literal convention/even reflection parity/global-sign zero-condition
readings are supplied; no opposite group law is silently used.

This is candidate mathematical correctness only. The complete premature observations, parent PERMANENT
PROCESS MAJOR classification and independent1945s/145s hard-cadence PROCESS MAJOR travel in errata1-3
and all checkpoints. The proof's complete post-ACK derivation does NOT cure them or claim independence.
No new acknowledgement/reset/clock extension. No science code/computation/enumeration/assertions/tests/
solver/Lean/native/modelCLI/network/nested agent/paid API/Git/tmp/old-file mutation or extra target.
Parent alone hand-checks, runs BOTH full-source mathematical gates and decides acceptance. Other V3
values await the separate complete arc proof, not a narrowed replacement of the frozen whole target.
