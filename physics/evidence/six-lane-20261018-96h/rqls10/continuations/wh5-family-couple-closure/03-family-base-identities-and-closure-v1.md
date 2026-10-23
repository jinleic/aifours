# The family F is closed under flat couple maps: base identities and exact closure proof (v1)

Recorded after actual `/bin/date`: 2026-10-19T18:37:04-0700. Written in the following minutes. ContinueRQLS10b.
Single author, UNREVIEWED, written only, not Lean-checked. No computation or enumeration. Scope frozen in00
(fb3caaa56640dd03d3baf9bf8696ba176a798fe45ebbc50f5fedd87f4e498049).
This note supplies all remaining family-specific hypotheses of note02 and proves CLOSURE. It does NOT classify all
flat planes, prove nonexistence for all W8 configurations, or settle maximal 1-RQLS(10), which remains OPEN/UNKNOWN.

## 1. Constants and elementary identities
Let zeta=exp(2pi i/5), omega=exp(2pi i/3), phi=(1+sqrt5)/2, N=15+3sqrt5.
  alpha=2cos(2pi/15), beta=2cos(8pi/15), gamma=2cos(4pi/15), delta=2cos(14pi/15), kappa=alpha-beta;
  A=sqrt5+alpha-delta, B=sqrt5+beta-gamma;
  p=3(5-sqrt5)/20, c=sqrt((3-sqrt5)/40), s=sqrt((3+sqrt5)/120), e=1/sqrt5;
  g=c gamma, d=c delta, a=s sqrt(A), b=s sqrt(B), G=g+d, R0=3(1-sqrt5)/20.
Here a,b are real scalars, not triangle invariants. Triangle invariants below are denoted T0,T1,T4.

**Lemma 5.** All square roots are positive real. One has
  alpha+beta=phi, gamma+delta=-1/phi, alpha beta=1/phi-1, gamma delta=-phi^2,
  gamma^2=2+beta, delta^2=2+alpha, alpha gamma=alpha+1/phi, beta delta=beta+1/phi;
  kappa^2=9-3phi, A+B=3sqrt5, AB=kappa^2, A-B=kappa+gamma-delta>0;
  (2+beta)A+(2+alpha)B=6sqrt5,
  (2+beta)A-(2+alpha)B=(3-sqrt5)kappa+2(gamma-delta)>0;
  g>0, d<0, G<0, d^2>g^2, a>b>0,
  gd=-1/20, g^2+d^2+a^2+b^2=2/5, g^2+d^2-a^2-b^2=R0<0, ga>-db.

Proof. The first line follows from 2cos(u)2cos(v)=2cos(u+v)+2cos(u-v) and
2cos(u)+2cos(v)=4cos((u+v)/2)cos((u-v)/2), with 2cos(pi/5)=phi and 2cos(2pi/5)=phi-1=1/phi.
For example alpha beta=2cos(2pi/3)+2cos(2pi/5)=1/phi-1,
gamma delta=2cos(6pi/5)+2cos(2pi/3)=-phi-1=-phi^2, and gamma+delta=-1/phi.
The other displayed products follow by substituting the named angles in the same formulas.
Then kappa^2=(alpha+beta)^2-4alpha beta=9-3phi.
Writing u=alpha-delta and v=beta-gamma gives u+v=sqrt5 and
uv=alpha beta-alpha gamma-beta delta+gamma delta=-1-3phi, hence AB=5+sqrt5(u+v)+uv=9-3phi.
A-B=kappa+gamma-delta>0; kappa>0 and gamma>delta follow from decreasing cos on[0,pi].
A>0 is immediate from alpha>0>delta; AB>0 then gives B>0. Expanding the weighted sum/difference using the first
line gives exactly the two displayed identities. The difference is positive because3>sqrt5, kappa>0 and gamma>delta.
Angles give gamma>0>delta; gamma+delta<0 implies |delta|>gamma, hence G<0 and d^2>g^2.
Since c^2 phi^2=(3-sqrt5)phi^2/40=1/20, gd=-1/20.
Also g^2+d^2=c^2(4+phi)=(11-3sqrt5)/40 and a^2+b^2=3sqrt5 s^2=(5+3sqrt5)/40.
Their sum and difference are as claimed. Finally
  (ga)^2-(db)^2=c^2 s^2[(2+beta)A-(2+alpha)B]>0;
ga>0 and -db>0, so ga>-db. QED.

## 2. Projector and flatness facts re-derived, not imported from E1/E2
Define F e_m=f_m, Q=diag(zeta^(2t^2)), U=Q F^*, R=diag(zeta^(t^2)).
For tau=(sigma,sigma') in {+1,-1}^2 set
  X_tau=(e,-g+i sigma b,-d+i sigma a,-d-i sigma a,-g-i sigma b),
  Y_tau=(e,-d+i sigma' a,-g-i sigma' b,-g+i sigma' b,-d-i sigma' a),
  x_tau=R X_tau, y_tau=R Y_tau, M_tau=X_tau X_tau^*+Y_tau Y_tau^*, P_tau=R M_tau R^*.
These are exactly the frozen coordinates, only aa,bb have been renamed a,b.

**Lemma 6.** x_tau,y_tau are orthonormal eigenvectors of U for -omega,-omega^2 respectively.
Consequently P_tau is a rank2 orthogonal projector, U P_tau U^*=P_tau, and P_tau is flat in Z,X,T.

Proof. The Gauss sums G1=sum_t zeta^(t^2)=sqrt5 and G2=sum_t zeta^(2t^2)=-sqrt5 follow from
zeta+zeta^4=1/phi and zeta^2+zeta^3=-phi. Completing the square gives
sum_t zeta^(h t^2+k t)=zeta^(-k^2/(4h)) G_h when h!=0 (all exponents modulo5).
It follows directly that
  U e_j=g_(-j), U g_m=-zeta^(3m^2) f_(-m), U f_j=zeta^(2j^2)e_j, U^3=-I.
For mu=omega or omega^2 put v_(mu,j)=e_j-mu^2 g_(-j)-mu zeta^(3j^2) f_j.
The preceding three identities give U v_(mu,j)=-mu v_(mu,j).
Let a0=v_(omega,0), b0=v_(omega,1)-v_(omega,4), a1=v_(omega^2,0), b1=v_(omega^2,1)-v_(omega^2,4).
Their coordinate expansions are
  sqrt5 a0=(1+sqrt5,-gamma zeta,-delta zeta^4,-delta zeta^4,-gamma zeta),
  sqrt5 b0=(0,B,kappa zeta^3,-kappa zeta^3,-B),
  sqrt5 a1=(1+sqrt5,-delta zeta,-gamma zeta^4,-gamma zeta^4,-delta zeta),
  sqrt5 b1=(0,A,-kappa zeta^3,kappa zeta^3,-A).
For completeness the expansions use, with eps=exp(pi i/15), zeta=eps^6, omega=eps^10:
  omega^2 zeta^2+omega=gamma zeta, omega^2 zeta^3+omega=delta zeta^4,
  omega zeta^2+omega^2=delta zeta, omega zeta^3+omega^2=gamma zeta^4,
  (zeta-zeta^4)(omega^2 zeta^2-omega zeta^3)=beta-gamma,
  (zeta-zeta^4)(omega zeta^2-omega^2 zeta^3)=alpha-delta,
  (zeta^2-zeta^3)zeta^3(omega^2-omega)=kappa zeta^3.
Each identity is the sum/product formula for cos or sin at the stated angles; the last has its negative when omega
and omega^2 are exchanged. These identities inserted in the definition of v yield every displayed coordinate.
Parity t->-t makes a0,a1 even and b0,b1 odd, so each even/odd pair is orthogonal. Lemma5 gives
  ||sqrt5 a0||^2=||sqrt5 a1||^2=(1+sqrt5)^2+2gamma^2+2delta^2=N,
  ||sqrt5 b0||^2=2(B^2+kappa^2)=6sqrt5 B,
  ||sqrt5 b1||^2=2(A^2+kappa^2)=6sqrt5 A.
Also c=sqrt(p/N), s=sqrt((1-p)/(6sqrt5)), and sqrt(p)(1+sqrt5)/sqrtN=e.
Using AB=kappa^2 and kappa>0 in these coordinates gives
  x_tau=sqrt(p) a0/||a0||+i sigma zeta sqrt(1-p) b0/||b0||,
  y_tau=sqrt(p) a1/||a1||+i sigma' zeta sqrt(1-p) b1/||b1||.
Both have norm1. Their eigenvalues differ, so they are orthogonal since U is unitary. Thus P_tau is a projector
commuting with U. Its Z-diagonal is2e^2=2/5 at0 and g^2+d^2+a^2+b^2=2/5 elsewhere (Lemma5).
Because U permutes the three bases Z->T->X->Z by the displayed identities, commutation with U transfers that
constant diagonal to the other two bases. QED.

## 3. Exact nondegeneracy for tau=(+,+)
For M=M_(+,+), let q(t)=M_(t+1,t), r(t)=M_(t+2,t), and T(t)=r(t)conj(q(t)q(t+1)).
The coordinates have M_(-r,-s)=conj(M_(r,s)). Direct expansion gives
  q0=e(-G+i(a+b)), q1=2d(g+i b), q2=R0+2i(da-gb),
  (q(t))=(q0,q1,q2,q1,q0),
  r0=e(-G+i(a-b)), r1=2g(d+i a),
  (T(t))=(T0,T1,T1,T0,T4).
All q(t) are nonzero: q0 has real part -eG>0, q1 has nonzero real part2dg, and q2 has real partR0<0.
By Lemma6 and note01, q(t)=k(z_t+z_t^(-1))+b0 for some k,b0.

**Lemma 7 (F1).** Im(T0 conj(T1))>0.
Proof. Cancelling the repeated q1 factor,
  Im(T0 conj(T1))=|q1|^2 Im(r0 conj(q0) conj(r1) q2).
Put V=r0 conj(q0)/e^2 and W=conj(r1)q2/(2g). The exact expansions are
  Re V=G^2+a^2-b^2>0, Im V=2Gb<0,
  Re W=d(g^2+d^2+a^2-b^2)-2gab<0,
  Im W=a(d^2-g^2+a^2+b^2)-2dg b>0.
Every strict sign follows immediately from Lemma5. Thus Im(VW)=Re V Im W+Im V Re W>0, and e^2,2g,|q1|^2 are positive.
QED. No numerical sign assumption is used.

**Lemma 8 (F2 and k!=0).** q0/q2 is not real, and k!=0.
Proof. The direct expansion is
  Im(q0 conj(q1))=2de[ga+(2g+d)b]=2de[(ga+db)+2gb]<0,
because ga>-db, g,b>0 and d<0 (Lemma5). Hence q0,q1 are not proportional over the reals, so k!=0.
For h_t=z_t+z_t^(-1), the three values at t=0,1,2 are phi,-1/phi,-2. The representation qj=k h_j+b0 therefore gives
  Im(q0 conj(q2))=((phi+2)/sqrt5) Im(q0 conj(q1))!=0.
Indeed q2 is the real affine combination of q0,q1 fixed by these three distinct h-values; h0-h1=sqrt5.
Since q2!=0, this is equivalent to q0/q2 not real. QED.

## 4. The other three labels by an exact dilation, not extra sign cases
Let S e_t=e_(3t), so (S M S^*)_(r,s)=M_(2r,2s). The coordinates immediately give
  S M_(sigma,sigma') S^*=M_(-sigma',sigma).
Specifically X_tau(2t)=Y_(-sigma',sigma)(t), Y_tau(2t)=X_(-sigma',sigma)(t), with the columns exchanged.
The four labels (++),(-+),(--),(+-) are one S-cycle.

**Lemma 9.** S preserves the tilde-flatness conditions of note01, in both directions; it also normalizes diagonal
unitaries and maps the subgroup {lambda Z^c} to itself.
Proof. Computational diagonals are permuted. The transformed first/second columns are q2(2t),q4(2t).
The old q2 has support{0,+2,-2}, so q2(2t) has support{0,+1,-1}; the old q4 is an adjoint shifted q1 and has
support{0,+1,-1}, so q4(2t) has support{0,+2,-2}. These are exactly the two tilde-flatness conditions.
The inverse follows by applying S three more times (S^4=I). For a diagonal E, its new entries are e_(2t).
If e_t=lambda zeta^(ct), they become lambda zeta^(2ct); the converse holds because2 is invertible modulo5. QED.

**Theorem 10 (diagonal-orbit closure, all four explicit planes).** For every tau and diagonal unitary E,
  E P_tau E^* is flat in Z,X,T iff E=lambda Z^c, |lambda|=1, c in Z_5.
Proof. For tau=(++), Lemmas6-8 verify EVERY hypothesis of note02 Theorem4, so its proof applies and yields the result
for M_(++). Repeatedly conjugating by S and using Lemma9 yields it for every M_tau. Since R commutes with E and
M is tilde-flat exactly when R M R^* is physically flat (note01), this is the stated result for P_tau. QED.
No earlier E1/E2 theorem is a premise of this closure proof.

## 5. All WH translates and all bases; retained phases
Let D_w=X^a Z^c, w=(a,c). Each D_w permutes each of Z,X,T up to vector phases: those bases are the eigenbases of
Z,X,XZ^(-1), and conjugation by D_w multiplies each such operator by a fifth root of unity. Thus D_w preserves flatness.
Let K be computational conjugation, K_b conjugation in basis b, and Anti_b={D K_b:D unitary diagonal in b}.

**Lemma 11 (exact base compatibility set against ALL flat projectors).** If P' is any flat rank2 projector and
A in Anti_Z satisfies A P_tau A=P', then for some |lambda|=1 and c in Z_5,
  A=lambda Z^c Q K, and P'=Z^c P_(-tau) Z^(-c).
Conversely every such A and P' works.
Proof. From the coordinates Q conj(P_tau) Q^*=P_(-tau), since Q conj(R X_tau)=R conj(X_tau)=R X_(-tau).
Write A=D K with D diagonal. Then A P_tau A=D conj(P_tau)D^*=(D Q^*) P_(-tau)(D Q^*)^*.
Theorem10 forces D Q^*=lambda Z^c, i.e. D=lambda Z^c Q; the converse follows from that identity and flatness. QED.
Antiunitaries in Anti_b are involutions, so the notation A P A agrees with A P A^(-1). Multiplication by any scalar
lambda of modulus1 changes the antiunitary, but not its action on projectors; no such phase has been dropped.

For the transport to the other bases, the identities in Lemma6 and direct Weyl conjugation give
  U X U^*=Z^(-1), U Z U^*=zeta^2 XZ^(-1),
  U D_(a,c) U^*=(unimodular) D_(c,-a-c).
Consequently U transports the lines L_Z={(0,c)}, L_T={(a,-a)}, L_X={(a,0)} cyclically in that order.
Also U Anti_Z U^(-1)=Anti_T and U^2 Anti_Z U^(-2)=Anti_X: U sends each original basis vector to a phase multiple
of a vector in the new basis, so diagonal operators are transported to diagonal operators and conjugation is
transported to a diagonal multiple of the new conjugation. Inverses give equality of the whole Anti sets.
Similarly D_w Anti_b D_w^(-1)=Anti_b. Conjugating Lemma11 by D_w, U and U^2 now proves:

**Theorem 12 (closure under ALL flat couple maps).** Fix any P=D_w P_tau D_w^* in F and b in{Z,T,X}.
The set of A in Anti_b whose image A P A is flat is precisely the following union of five circles:
  b=Z: {lambda D_w Z^c Q K D_w^(-1): |lambda|=1, c in Z_5};
  b=T: D_w U {lambda Z^c Q K: |lambda|=1, c in Z_5} U^(-1) D_w^(-1);
  b=X: D_w U^2 {lambda Z^c Q K: |lambda|=1, c in Z_5} U^(-2) D_w^(-1).
The flat image planes are exactly D_(w+l) P_(-tau) D_(w+l)^* for l in L_b.
Thus every flat couple partner of any member of F is in F. There is no assumption that F exhausts flat planes.
Proof. U P_tau U^*=P_tau by Lemma6, WH factors differing by scalar have identical projector conjugation,
and the line transformation is as displayed. The Anti equalities and flatness invariance prove necessity and
sufficiency, not just containment. QED.

## 6. Scope of the consequence for W8
This package proves closure, not the internal-F triangle theorem. Conditional on BOTH claims from the separate
unreviewed E2/E3 candidate c625b377edf9706d9b14942389dee6f05bf716a1b18fedab38632dbe135708ec:
(HW) every W8 couple satisfies P_s=A P_r A for A in the corresponding Anti_b;
(HF) no W8 solution has all four representative planes in F;
Theorem12 implies that a W8 solution cannot have even ONE representative plane in F: its three incident couples
put the other three in F, contradicting(HF). This is explicitly conditional until those claims receive parent review.
No claim is made about solutions all of whose planes are outside F, a classification of such planes, arbitrary
QLS mates, or maximal-cardinality 1-RQLS(10). Parent owns independent review and verdicts.

Imports used: elementary character orthogonality, trigonometric sum/product identities, degree/root bound for
polynomials, linear algebra of unitary eigenspaces, and the definitions/proved Lemmas1-4 in notes01-02 of this package.
No Fejer-Riesz/Haagerup/Chebotarev classification, computation, floating-point premise, or novelty/priority claim.
