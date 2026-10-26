# CURRENT P44 CONSOLIDATION — one complete body: fullD, coherent states, balanced parity, inherited-positive cross-compression

**SINGLE COMPLETE PART 1/1.** PhysicsPPT44-2. Actual `/bin/date` observed before consolidation: **Sun Oct 25 14:55:00 PDT 2026**. Scope ACK: `checkpoint-039-current-consolidation-ack-and-scope-v1.json`, SHA256 `4b733d6014f1d91c7a508b96dcb24090ae7ba943a91e0a6f6283521156955e4b`. This is the requested current consolidation, not another fragmentary gate input, a new slot, or a reset of the original P44 problem.

**Status:** the existing adopted closed-rectangle result in Section4.4 retains its OWN parent WRITTEN verdict. Every additional claim explicitly requested below is an AUTHOR-WRITTEN candidate pending a fresh complete read/reconstruction/disposition of THIS body. New parts do NOT inherit the old verdict. No scientific program/eval/arithmetic interpreter/enumeration/symbolic or numerical computation/solver/replay/compile, nativeGO, externalCLI or nestedagent was launched for these proofs. All identities and inequalities are WRITTEN, not machine-checked. Metadata clocks/hashes/source reading only. Earlier withdrawn computations, the checkpoint013cadence miss, N4 UNKNOWN/incomplete/exit-unestablished and the old21-table NOT_RECONSTRUCTED status are not repaired or recertified.

The current authority remains scientific HOLDv2, later parent errata v9/v10/v11, and the original new-science cutoff **2026-10-27T11:05:38-07:00** and deadline **2026-10-27T12:35:38-07:00**. This consolidation does not backdate later overlays into earlier frozen packets.

## 0. Exact adoption request and status separation

The fresh written gate is requested ONLY for the following complete claims, proved in this body:

- **C1 / Section2:** the actual16-entry product-diagonal completion route D-Q, its full-COMPLEX inverse-Gram iff, the full four-complex-block PPT residual, and necessary coordinate/completion test families. This is a method characterization, NOT a feasible separating pair or an all-state no-go.
- **C2 / Section3:** complete positivity/PPT/rank/trace eligibility of the displayed R(s,t) family for0<s<1,t>0, with every complex PTblock retained.
- **C3 / Section4:** the14-phase operator identity, its exact general residual-sufficient region, and the exact OLD adopted closed rectangle. The old rectangle remains retired; only the explicitly additional general-domain statement is a new adoption request.
- **C4 / Section5:** a separate24-phase actual-state SN<=2 region, with its full vector/weight/residual identity. It is not inherited from C3.
- **C5 / Section6:** the EXACT SN<=2 criterion for the stated coherent opposite-offset COMPONENT, including complex phases/zero-noise boundaries, plus its explicit application to a genuinely phase-frustrated PPTtrial in Section7. This is not an arbitrary-state/P44 classification.
- **C6 / Section8:** actual inherited all-complex two-positivity and the three-positive shift for the six-dimensional source and its arbitrary complex isometric4x4 compressions; actual PPT source/compressions; all definitions/normalizations are explicit.
- **C7 / Sections9–10:** TWO precise uniform non-separation theorems: the SAME-compression source pair, and the ENTIRE literal complex R_x chart tested by this inherited witness class. Neither theorem promotes general decomposability or general SN<=2.
- **C8 / Section11:** the exact independent-compression trace formula and the still-UNPROVED negative gate. This is an exact reduction, NOT an existence or impossibility result.

Section12 separately identifies **context-only/superseded-as-primary-method** records. Their mathematics is not silently declared false, accepted, withdrawn, or closed by the14-phase theorem. They are NOT correctness premises or extra adoption requests in this gate. Section13 states the full original remaining problem without narrowing it.

## 1. Common conventions and complete standard imports

Work over COMPLEX finite-dimensional Hilbert spaces. Inner products are conjugate-linear in the first argument. P(v)=v v* for an unnormalized vector. A coefficient matrix C represents vec(C)=sum_ij C_ij|ij>; its Schmidt rank is rank(C), and ||vec(C)||^2=||C||_F^2. A Hermitian W is two-block-positive when <vec(C),Wvec(C)>=0 for EVERY complex rank(C)<=2, not just real C or selected vectors.

A PSDoperator has Schmidt number<=2 exactly when it is a finite conic sum of projectors onto such vectors. A displayed nonnegative conic identity becomes a convex unit-vector ensemble by dividing each coefficient times the vector's squared norm by the total trace. No uniform weights are inferred unless actually displayed. A negative expectation of a universally two-block-positive W on a PSDstate proves its Schmidt number>=3.

The ONLY standard facts used are the following elementary finite-dimensional facts; all specialized calculations are supplied below:

1. Spectral theorem; PSD iff its Hermitian quadratic form is nonnegative; cyclic traces, rank/nullspace identities, Cauchy–Schwarz, triangle inequality and weighted AMGM.
2. For P>=0, P-P(m)>=0 iff m is in rangeP and <m,Pdagger m><=1. This follows by whitening on rangeP. For a positive definite highblock H, block PSD is equivalent to PSD of the Schur complement L-K*H^(-1)K; its rank is rankH plus the residual rank.
3. Local linear maps do not increase pure Schmidt rank. Local isometries/unitaries preserve it. Local congruences preserve PSD and PPT, with the Bob factor conjugated under partial transpose. This does NOT preserve a Schmidt-number LOWER bound under a compression.
4. An expectation-preserving average of LOCAL unitaries preserves PSD/PPT. No nonlocal pinching or unproved J/X averaging is allowed. The only lossless twirl used for arbitrary D-Q states in Section2 is explicitly proved there.
5. For Omega_d=sum_j|jj> and SWAP F_d, P(Omega_d)^Gamma=F_d. For T_N=(I tensorN)F_d(I tensorN*), T_N=(N* tensorN)F_d is Hermitian and T_N^Gamma=P(vecN*). These also follow entrywise from the vec convention. F(A tensorB)=(B tensorA)F.
6. For Nth roots of unity, sum_w w^m=0 unless N divides m, when the sum is N. This is the finite geometric-series identity. Phase averages below DEFINE exact decompositions, not samples that certify an unexamined universal condition.
7. If a PSDsum has a kernel vector, every positive summand vanishes on that vector. Thus every pure vector in a conic decomposition lies in the range of the total operator.
8. P+Q^Gamma with P,Q>=0 is nonnegative on every PPToperator by cyclic trace. No stronger decomposability classification is imported as an all-M4 theorem.

All inequalities in Sections2–11 are exact written statements. There is no proof-assistant/kernel, executable finite checker, triple-checker, vendor/family/human, novelty/SOTA or publication acceptance here.

## 2. C1 — the surviving FULL16-entry D-Q residual

### 2.1 Actual negative rays and all coefficient domains

Indices are modulo4; i=sqrt(-1), Z=diag(1,i,-1,-i), X|j>=|j+1>. Let U1=I,U2=Z,U3=X,U4=ZX and Phi_U=vec(U)/2. The four normalized orthogonal rays define

```
Q0=P(Phi_I)+P(Phi_Z), Q1=P(Phi_X)+P(Phi_ZX), Q=Q0+Q1,
D=sum_(i,j=0)^3 d_ij P(ij), d_ij REAL,
W_D=D-Q.                                                   (2.1)
```

The SIXTEEN d_ij are independent. Product basis tests force d_ij>=1/2 on differences0/1 and d_ij>=0 on differences2/3 if W_D is two-block-positive. The strict d_ij>0 case loses no strict negative PPTopportunity WITHIN THIS ROUTE: if Tr(W_D rho)=-delta<0 for trace-one rho, W_D+epsilonI is still two-block-positive and still negative for0<epsilon<delta. Rational epsilon may be chosen for rational data. This does not regularize arbitrary witness forms into this class.

### 2.2 Full-COMPLEX inverse-Gram iff

For every COMPLEX4x2 isometry S (S*S=I2), and each column j, define

```
A_j(S)=S*diag(d_0j,d_1j,d_2j,d_3j)S,
V_j=[S*U1 e_j/2,S*U2 e_j/2,S*U3 e_j/2,S*U4 e_j/2],
G_D(S)=sum_j V_j* A_j(S)^(-1)V_j.                          (2.2)
```

When d_ij>0 all A_j are positive definite. Then

```
W_D two-block-positive IFF G_D(S)<=I4 for EVERYcomplex S.    (2.3)
```

Proof. Write every rank<=2 coefficient matrix C=SZ with columns z_j. Its positive energy is E=sum z_j*A_jz_j. Its four negative overlaps form h=sum V_j*z_j. Whitening by A_j^(1/2) makes the squared norm of this overlap map exactly lambda_max(G_D). This proves sufficiency. If G_Dv=gv for unit v and g>1, set z_j=A_j^(-1)V_jv. Then E=g,h=gv and expectation g-g^2<0 on an actual rank<=2 C. Every complex plane and lower rank is included. A scalar Gram, real-plane calculation or finite product/rank-two sample is NOT a substitute for(2.3).

### 2.3 FULLcomplex PPTblocks and exact objective

The four-element LOCAL group generated by Z tensorconjugate(Z) fixes every product-diagonal D and each Qray projector: a ray supported on difference q only gains a unit scalar. Its state twirl is therefore lossless for this W_D objective and preserves PPT. It leaves the general state

```
R=sum_(q=0)^3 sum_(r,k) Rq(r,k)|r,r-q><k,k-q|,
Rq Hermitian COMPLEX4x4.                                  (2.4)
```

No entry INSIDE these four blocks is discarded. PSD iff every Rq>=0. Partial transpose changes an entry into |r,k-q><k,r-q|, preserving total index tau=r+k-q. The COMPLETEfour PTblocks are

```
S_tau(r,k)=R_(r+k-tau)(r,k), tau=0,1,2,3.                  (2.5)
```

Thus trace-one PPT means ALLRq>=0, ALLS_tau>=0, sum_qTrRq=1. Put B_rk=(1+i^(r-k))/4. The restriction of Q on q0andq1 is B, so the ACTUALobjective is

```
F_D(R)=sum_(q,r)d_(r,r-q)Rq(r,r)-Tr(BR0)-Tr(BR1).            (2.6)
```

No J/X symmetry is imposed on this general input. In particular the special coherent states below are NOT a replacement for the arbitrary four COMPLEXblocks in(2.4)–(2.6).

### 2.4 Necessary complex rank-two tests, not sufficiency

For q0,1 define from the SAME d-array

```
h_(0,j)=(j,j),       ell_(0,j)=(j+1,j-1),
h_(1,j)=(j+1,j),     ell_(1,j)=(j,j+1),
delta_(q,j)=d_(h_(q,j))-1/2,
beta_(q,j)=d_(ell_(q,j)).                                  (2.7)
```

Adjacent highcoordinate pairs span only SR<=2vectors. Their actual2x2 Wblock has off-diagonal modulus sqrt2/4, giving

```
delta_(q,j)>0,
delta_(q,j)delta_(q,j+1)>=1/8.                              (2.8)
```

A further COMPLETEcomplex test family is as follows. Fix j, k=j-2,r=k-1,l=k+1, A_k=I-i^(-k)Z, and arbitrary z inC,w inC excluding0:

```
C_(q,j)(z,w)=X^q[A_k+(z-2)E_jj+sqrt2(wE_rl+w^(-1)E_lr)].   (2.9)
```

Before X^q, the kdiagonal is zero, the jdiagonal is z, and the r/lblock has diagonal product2/offproduct2. Hence rank<=2. It has only differencesqandq+2; its two relevant Qoverlaps have equal moduli |z+2|/2 and the other two vanish. With the actual shared coefficients, its Wexpectation is

```
delta_(q,j)|z|^2-2Re(z)+2(delta_(q,j-1)+delta_(q,j+1))
      +2(beta_(q,j)|w|^2+beta_(q,j+2)|w|^(-2)),             (2.10)
```

For the LITERALorder in(2.9), the coefficients of |w|^2,|w|^(-2)are (beta_(0,j),beta_(0,j+2))whenq0and (beta_(1,j+2),beta_(1,j))whenq1. Equation(2.10)uses the bijective reparameterization w<->w^(-1)ONLYin the q1family; no coefficient of D is changed or made independent. Infimizing over |w| and then over COMPLEX z gives the EIGHTnecessary inequalities

```
delta_(q,j)[2(delta_(q,j-1)+delta_(q,j+1))
                   +4sqrt(beta_(q,j)beta_(q,j+2))]>=1.    (2.11)
```

If a beta is zero the infimum is approached by finite nonzero w; a negative infimum would already yield a finite violating vector. There is no missed zero-delta branch because the nonzero linear term in z would violate positivity. These are analytic infinite-family necessary tests, NOT a sufficient replacement for(2.3).

**C1 exact remaining route:** a rational positive D and an actual state satisfying ALL(2.3)andALL(2.4)–(2.5)with F_D(R)<0, or a true uniform obstruction for this route. None is supplied. Even such a route-specific no-go would not classify arbitrary non-diagonal positive completions or all two-positive M4maps.

## 3. C2 — full eligibility of the actual coherent R(s,t)

For0<s<1,t>0, let E_qe_r=|r,r-q>, F_(r,0)=1/2,F_(r,1)=i^r/2, B=FF*, and

```
R0=F[1 s;s 1]F*, R1=tB,
R2=diag(y0,y1,y2,y3), R3=diag(z0,z1,z2,z3),
y0=y2=t^2/4,
y1=t^2/[4(1+s)]+s/2, y3=t^2/[4(1-s)]+s/2,
z0=z3=(1+s)^2/(4t), z1=z2=(1-s)^2/(4t),
R(s,t)=sum_q E_qRqE_q*,
N=TrR=2+2t+s+t^2(2-s^2)/[2(1-s^2)]+(1+s^2)/t.            (3.1)
```

Fhas orthonormal columns; the high coefficient eigenvalues are1+-s and t,t, and every low diagonal is positive. Thus R>=0with rank2+2+4+4=12and N>0. Its actual PTblocks are(2.5), with the following exhaustive structures:

- tau0, order highindices0,2then lowindices1,3: highdiagonal((1+s)/2,(1-s)/2), diagonal matching t(1-i)/4,t(1-i)/4, lowdiagonal(y1,y3)and lowcross is/2. Its exact Schur residual is (s/2)[1 i;-i 1], PSD rank1. Total rank3.
- tau2, order highindices1,3then lowindices2,0: highdiagonal1/2,1/2, same diagonal matching t(1-i)/4, lowdiagonal t^2/4,t^2/4and lowcross0. Schur residual0; total rank2.
- tau1, pairs1/0and3/2: highdiagonal t/2,t/2, lowdiagonals(1+s)^2/(4t),(1-s)^2/(4t), offentries(1+s)(1+i)/4,(1-s)(1+i)/4. Each2x2block has positive diagonal product equal to offmodulus squared, so rank2 total.
- tau3, pairs0/3and2/1: the corresponding same positive diagonals/offmoduli give two more saturated rank-one2x2blocks, rank2 total.

R2,R3are diagonal, B's opposite entries vanish, R0(2,0)=0and R0(1,3)=is/2; these account for EVERYentry, not just selected principal minors. Therefore the FULLstate is PPTwith PTrank9. The opposite coherence proves failure of jointXtranslation (it would map to the zero2/0entry), failure of Jinterchanging highq0/q1, and failure of the old rank8PTface. None of those restricted symmetries is used to infer the theorem.

At s=1/2,t=1, N=83/12and the explicit actual density is

```
rho=[sum_q E_qKqE_q*]/332,
K0(r,k)=12(1+i^(r-k))+6(i^r+i^(-k)),
K1(r,k)=12(1+i^(r-k)),
K2=diag(12,20,12,36), K3=diag(27,3,3,27).                 (3.2)
```

The traces96,96,80,60sum332. Real/imaginary entries are integers divided by332. This is Gaussian-rational, not a claim of real-only rational entries. Its SNupper bound is the actual operator identity next, not an attractive PPTcontrol promoted without a separator.

## 4. C3 —14phase actual operator identity, general residual region, and EXACTold retirement

### 4.1 Complete prototype/rank certificate

Write h_plus=1+s,h_minus=1-s,H=1-s^2=h_plus h_minus,u=t^2,a=H/u,d=sqrt(t/8),A_h=sqrt(h/8). For h=h_plusorh_minusdefine

```
b_h=(i-1)(1-a)d^2/A_h,
c_h=(1+i)(1-1/sqrt2)A_h^3/(a d^2),
e_h=(1+i)a d^3/A_h^2,
f_h=-i sqrt2 A_h^2/d,
M_h(w)=[2A_h            0          0       (1+i)d w]
       [2id w       (1+i)A_h     0         b_h w^2]
       [0           (i-1)d w     0         e_h w^3]
       [f_h w^-1     c_h w^-2    0         (1-i)A_h].     (4.1)
```

For ANYnonzero complexw, column2is zero and a second independent nullvector is

```
xi_h=(1,-a(d/A_h)(1+i)w,0,-(A_h/d)(1-i)w^-1)^T.          (4.2)
```

The four row cancellations, after their common wpower, are

```
2A_h-A_h(1+i)(1-i)=0,
2id-2iad-2id(1-a)=0,
2a d^2/A_h-e_h(A_h/d)(1-i)=0,
f_h-a(d/A_h)(1+i)c_h+2iA_h^2/d=0.                         (4.3)
```

They follow directly from(4.1),(1+i)^2=2iand2/sqrt2=sqrt2. The e2andxikernels are independent; the rows0/1,columns0/1minor is2(1+i)A_h^2!=0. Thus rankM_h=2overC, not just a real or sampled rank claim. A_h,d,aare positive/nonzero on the whole stated0<s<1,t>0domain;1-a is never divided by.

### 4.2 EVERYoperator entry in the exact average

Let Omega7be all seventh roots. The six coefficient groups have distinct residues0,1,2,5,3,6:

```
0: q0diagonal A_h(1+i^r),
1: q1vector d(i+i^r),
2: b_hE13, -2:c_hE31, 3:e_hE23, -1:f_hE30.
```

Hence exact averaging kills EVERYcross term BETWEENgroups, while retaining all coherences WITHINeach highgroup. Average the two families SEPARATELY and add their projectors:

```
M_plus(w)=M_(h_plus)(w),
M_minus(w)=X^2M_(h_minus)(w)X^(-2).                        (4.4)
```

The second is a simultaneous local-unitary row/columnshift, preserving rank. Its highq0vector becomes A_(h_minus)(1-i^r), and highq1vector becomes d(i-i^r). The two q0projectors expand to R0because A_plus^2+A_minus^2=1/4and A_plus^2-A_minus^2=s/4. The q1sum is2d^2(1+i^(r-k))=tB_(r,k), exactlyR1.

Put kappa=3-2sqrt2. The four lowmagnitudes are

```
B_h=|b_h|^2=(u-H)^2/(4h u),
C_h=|c_h|^2=kappa u h^3/(8H^2),
|e_h|^2=(2-h)^2/(4t), |f_h|^2=h^2/(4t).                  (4.5)
```

Thus the plusfamily supplies q3row2=z2,row3=z3; the shifted minusfamily supplies row0=z0,row1=z1. ALLofR3is exact. In q2the generated row1population is B_plus+C_minusand row3is C_plus+B_minus; rows0,2are zero. Therefore the literal identity is

```
r0=y0,r2=y2,
r1=y1-B_plus-C_minus,
r3=y3-C_plus-B_minus,
R=(1/7)sum_(w inOmega7)[P(vecM_plus(w))+P(vecM_minus(w))]
                         +sum_j r_jP(j,j-2).             (4.6)
```

Every high/lowand low/lowentry has been accounted for by the character groups. This is the ACTUALoperatorR, not merely moments.

### 4.3 Additional general-domain sufficiency, NOTold inherited acceptance

Straight substitution gives

```
r1=1/2-[h_plus h_minus^2/(4u)+kappa u h_minus/(8h_plus^2)],
r3=1/2+s-[h_minus h_plus^2/(4u)+kappa u h_plus/(8h_minus^2)]. (4.7)
```

For ANY0<s<1,t>0where BOTHprinted r1,r3are nonnegative, (4.6)proves SN(R/N)<=2. This is a sufficient parameter test, NOTan iffclassification of the entire two-parameter family. The unit-vector phaseweights are ||M||_F^2/(7N), and productweights r_j/N; their trace sum is1. They are NOTuniform1/14. This general-domain statement is part of THIS fresh adoption request, not silently covered by the earlier parent verdict.

### 4.4 EXACTpreviously adopted closed rectangle — permanently RETIRED

The OLDadopted domain is EXACTLY

```
1/2<=s<=2/3, 9/10<=t<=11/10.                              (4.8)
```

On it,4/5<u<5/4,h_plusin[3/2,5/3],h_minusin[1/3,1/2],0<kappa<1/5. The first bracket of(4.7)is less than5/32+1/144=47/288, giving r1>97/288. The second is less than125/288+15/32=65/72;1/2+s>=1gives r3>7/72. Also r0=r2=t^2/4>0. The relaxed strictubounds remain strict EVENat the original CLOSEDendpoints.

Hence the whole closed rectangle is SN<=2by14rank2rays plus4productrays. No universal complexSR2witness of ANYform can separate ANYstate there, including(3.2). A new Dlabel, fullD-Qnegativepart, SNRlabel or inherited witness cannot rescue the same actual state.

This exact claim was already adopted WRITTEN_SUPPORTED in `RUN/ppt-coherent-rectangle-SN2-parent-v1.md`, SHA256 `992874f1375664e66c6a9b438dd72e22776222a96dfe5d179606e12eef006682`, FULL27LFread by this owner. That parent consumed the complete238-LF14phasebody and actual273-LFv87-Creview,0F/0M/0m, plus ONLYthe original61-LFeligibility prefix. It conferred NOexecutable/triple-witness/kernel/vendor/family/human/novelty/exactSN2/unrestrictedP44acceptance. Its acceptance does NOTautomatically cover Sections4.3,5,6,7,8,9,10or11of this later consolidation.

## 5. C4 — a DIFFERENT24phase SN<=2wedge, fully stated and proved

For the SAMEfamily(3.1), consider the separate domain

```
0<s<1,t>0, 4y1y3>=1, t^2<=1-s^2.                        (5.1)
```

It has interior, e.g.s=t=2/3gives4y1y3=16/15>1and t^2=4/9<5/9. Its proof does not rely on the adopted rectangle.

For epsilon=+-1let A_eps=sqrt((1+epsilon s)/8),h_eps(j)=A_eps(1+epsilon i^j),p_eps=sqrt2A_eps,eta=sqrt(y1/y3). For w in the fourth roots define

```
C_eps(w)=diag(h_eps)+p_eps[sqrteta wE13+eta^(-1/2)w^-1E31]. (5.2)
```

Under row/columnorder0,2,1,3, the evenblock has onezero diagonal and rank1; the oddblock has equal diagonal/offproducts2A_eps^2and rank1. Hence each C_epshas rank2. Exact fourth-root averaging of characters0,+1,-1kills all cross terms. Summing epsilon yields

```
(1/4)sum_(eps,w)P(vecC_eps(w))
                  =E0R0E0*+(eta/2)P13+[1/(2eta)]P31.     (5.3)
```

The highidentity follows from the same u+-vexpansion as Section4. The missing q2diagonal is nonnegative because sqrt(y1y3)>=1/2: residuals y0,y2,y1-eta/2,y3-1/(2eta).

Next let A=sqrt(t)/4,p=sqrt2A. For k0..3put h_k(j)=A(1-i^(-k)i^j),r=k-1,l=k+1,eta_k=sqrt(z_k/z_(k+2)). Define

```
N_k(w)=X[diag(h_k)+p(sqrteta_k wE_rl+eta_k^(-1/2)w^-1E_lr)]. (5.4)
```

Before X, the kdiagonal is0,the opposite diagonal2A, and the r/lblock has diagonal/offproduct2A^2. Thus rankN_k=2. Summing kafterexact fourth-root averaging produces

```
(1/4)sum_(k,w)P(vecN_k(w))
       =E1R1E1*+sum_j n3_jP(j,j+1),
n3_j=(t/4)sqrt(z_j/z_(j+2)).                              (5.5)
```

Indeed sum_k h_k(j)conj(h_k(l))=4A^2(1+i^(j-l))=tB_jl; the simultaneous shift byXdoes not change this difference-dependent B. Each opposite lowpair gets its two contributions using eta_(k+2)=1/eta_k. Since sqrt(z_jz_(j+2))=(1-s^2)/(4t), the second condition(5.1)makes every z_j-n3_jnonnegative.

Adding(5.3),(5.5)and allprinted productresiduals gives the COMPLETEoperatoridentity forRwith8+16=24rank2rays and at most8products. Unit-vector weights are their normsq/(4N)and residualcoeff/N, not uniform1/24. All denominators are positive for0<s<1,t>0; equality in either(5.1)just permits zero residuals.

This proves SN<=2ONLYin(5.1). The old rectangle(4.8)is outside this wedge because t^2>=81/100>3/4>=1-s^2. The two proofs are separate; neither is promoted retrospectively by the other's verdict.

## 6. C5 — EXACTbalanced-parity SN<=2criterion for a coherent COMPONENT

### 6.1 Statement and NECESSITYoverallcomplexensembles

For t>0,|gamma|<=1,Y_j>=0define

```
S=t E0F[1 gamma;conjgamma 1]F*E0*+sum_jY_jP(j,j-2),
cE=sqrt(Y0Y2),cO=sqrt(Y1Y3).                              (6.1)
```

Then the EXACTcriterion is

```
SN(S)<=2 IFF
cE>=t|Im gamma|/2, cO>=t|Re gamma|/2, cE+cO>=t/2.          (6.2)
```

This component need not itself be PPT; this is NOTan arbitrary-state classification.

For necessity, every pure vector in an SR2decomposition lies in rangeS, hence has only differences0/2and highdiagonal h_j=a+b i^j. Its matrix is parityblockdiagonal. If h!=0both parityblocks are nonzero; otherwise vanishing h0,h2or h1,h3would implya=b=0. Rank<=2then forces EACHblockrank1, with offproducts

```
h0h2=a^2-b^2, h1h3=a^2+b^2.                              (6.3)
```

If h=0the absolute inequalities below are trivially valid regardless of low-only rank. Cauchy on the actual low populations yields sum|a^2-b^2|<=cEand sum|a^2+b^2|<=cO. The exact highcovariance yields sum|a|^2=sum|b|^2=t/4and sum aconj(b)=tgamma/4. For EACHcomplexa,b,

```
|a^2-b^2|>=2|Im(a conjb)|,
|a^2+b^2|>=2|Re(a conjb)|,
|a^2-b^2|+|a^2+b^2|>=|a|^2+|b|^2.                        (6.4)
```

Squaring proves the first two; two trianglebounds give at least2max(|a|^2,|b|^2)for the last. Summing proves ALLthree(6.2). No balanced-ray assumption was imposed on the necessity proof.

### 6.2 SUFFICIENCY: full finite phase construction, including boundary cases

Write gamma=u+iv,Amax=min(1,2cO/t),Bmax=min(1,2cE/t). Conditions(6.2)imply Amax>=|u|,Bmax>=|v|and Amax+Bmax>=1. Choose absolute means A,Bas follows:

- if |u|+|v|>=1, take A=|u|,B=|v|;
- otherwise take A=max(|u|,1-Bmax),B=1-A.

Then A>=|u|,B>=|v|,A<=Amax,B<=Bmax,A+B>=1,A^2+B^2<=1. Let L=A+B,r=sqrt(A^2+B^2). Except for the axis case L=r=1, the three quarter-unitcirclepoints (A/r,B/r),(1,0),(0,1)with probabilities

```
p=r(L-1)/(L-r), (1-p)A/L, (1-p)B/L                      (6.5)
```

are nonnegative, sum1and have mean(A,B). An axis uses its one point; L=1or r=1otherwise is already included. Independently flip the two signs with fixed means u/A,v/B(when a coordinate is0its sign is irrelevant). This creates at most12UNITcomplexphases xi_lwith probabilities p_lsuch that

```
sum p_lxi_l=gamma,
sum p_l|Re xi_l|=A, sum p_l|Im xi_l|=B.                   (6.6)
```

For each positive probability put h_j^(l)=sqrt(tp_l/4)(1+conj(xi_l)i^j). Their projectors sum to the highblock of(6.1), and

```
L_E=sum_l|h0h2|=tB/2<=cE,
L_O=sum_l|h1h3|=tA/2<=cO.                                (6.7)
```

If Y0Y2>0let etaE=sqrt(Y0/Y2),and ifY1Y3>0let etaO=sqrt(Y1/Y3). Choose unit square roots sigmaE,sigmaOof the phases of the respective highproducts. For EACHfifthrootw, form a matrix with diagonalh^(l)and entries

```
02: sigmaE sqrt(etaE|h0h2|)w,
20: sigmaE sqrt(|h0h2|/etaE)w^-1,
13: sigmaO sqrt(etaO|h1h3|)w^2,
31: sigmaO sqrt(|h1h3|/etaO)w^-2.                          (6.8)
```

Each parityblock has matching diagonal/offproductand rank1, so the whole matrix is SR<=2. The five characters0,+1,-1,+2,-2are distinct modulo5. Their exact average kills EVERYhigh/lowand low/lowcross, leaving the desired highblock and lowdiagonals etaE L_E,L_E/etaE,etaO L_O,L_O/etaO, respectively. They are at most the targetYvalues; add the nonnegative residual products. This is S ITSELF, not moments.

If a noisepair product is0, (6.7)forces ALLcorresponding highproducts zero. Use zero offentries instead of that undefined ratio; any remaining positive member of that pair is simply a productresidual. Thus no zero-noise boundary or zero phaseprobability is lost. Dividing byTrSnormalizes the vector weights normsq/(5TrS)and productresiduals/TrS. This proves sufficiency and completes the iff(6.2).

## 7. C5 application — a genuinely new frustrated PPTgeometry is nevertheless SN<=2

### 7.1 Escape of the old zero-entry highray representation

A nonzero I/Zray h_j=a+b i^jhas a zero entry only if |a|=|b|and its relative phase is one of the four roots. Any positive mixture of such rays with equal coefficient diagonals therefore has normalized offdiagonal in conv{1,-1,i,-i}, so |Re gamma|+|Im gamma|<=1. The trialgamma=1/2+3i/5has squared norm61/100<1but l1=11/10>1. It rigorously requires at least one all-four-entry highray, beyond the14/24templates. Escape alone is NOTSN3evidence.

### 7.2 Full actual PPTfamily and every PTblock

For0<s<1,t>0,gamma=u+ivwith u,v>0,u^2+v^2<1define

```
R0=F[1 s;s 1]F*, R1=tF[1 gamma;conjgamma 1]F*,
b0=1+u+v,b1=1-u+v,b2=1-u-v,b3=1+u-v,
y0=t^2b3^2/4,y2=t^2b1^2/4,
y1=t^2b0^2/[4(1+s)]+s/2,
y3=t^2b2^2/[4(1-s)]+s/2,
z0=(1+s)^2/[4t(1+v)]+tv/2,
z2=(1-s)^2/[4t(1-v)]+tv/2,
z3=(1+s)^2/[4t(1+u)]+tu/2,
z1=(1-s)^2/[4t(1-u)]+tu/2,
R2=diag(y),R3=diag(z),R=sum_qE_qRqE_q*.                   (7.1)
```

All original blocks are PSD. With the COMPLETEshuffle(2.5), the Schur structures are:

- tau0high0,2diagonal((1+s)/2,(1-s)/2), matching t b0(1-i)/4,t b2(1-i)/4to low1,3, lowcross is/2. Residual(s/2)[1 i;-i1].
- tau2high1,3diagonal1/2,1/2, matching t b1(1-i)/4,t b3(1-i)/4to low2,0, lowcross0. Residual0.
- tau1high1,3diagonal t(1+v)/2,t(1-v)/2, matching(1+s)(1+i)/4,(1-s)(1+i)/4to low0,2, lowcross-itv/2. Residual(tv/2)[1 -i;i1].
- tau3high0,2diagonal t(1+u)/2,t(1-u)/2, corresponding matching to low3,1, lowcross-itu/2. Residual(tu/2)[1 -i;i1].

Every residual is PSD, including the negative b2edge when u+v>1. These exhaust all entries. The state is PPT, rank12and PTrank3+2+3+3=11. Its full-rank marginals and changed ranks exclude a SINGLElocalfilter image of the old rank12/PT9state, not arbitrary filtered convex closures.

At s=1/2,t=1,u=1/2,v=3/5, the actual Gaussian-rational density is

```
rho=[sum_q E_qKqE_q*]/25129,
K0(j,k)=800(1+i^(j-k))+400(i^j+i^(-k)),
K1(j,k)=800(1+i^(j-k))+(400+480i)i^(-k)+(400-480i)i^j,
K2=diag(648,3152,968,816), K3=diag(2085,1200,1460,2000).     (7.2)
```

The traces6400,6400,5584,6745sum25129; rawscale3200Rhas TrR=25129/3200. Allreal/imaginary entries are integers divided by25129. No machine count is claimed.

### 7.3 Actual retirement by the NEWcriterion, not an attractive PPTcontrol

Split R0+R2andR1+R3. The latter is of(6.1)after a local Bobshiftq1->q0,q3->q2. For the first, t0=1,gamma0=s=1/2,cE=99/400,cO=sqrt(10047)/200>1/2. For the second, gamma1=1/2+3i/5,cE=sqrt(30441)/320>1/2,cO=sqrt15/8>1/4. These satisfy ALLthree(6.2), with second-component thresholds3/10and1/4. Both partialoperators have exact SR2decompositions, so their sum is SN<=2.

Thus this genuinely frustrated geometry is RETIREDas an SN3trial at the NEWauthor-written criterion, pending this fresh gate. It does not inherit the old rectangle's verdict; it has its own complete proof here. No all-(7.1)SNclassification is asserted.

## 8. C6 — genuinely different inherited all-COMPLEXpositive geometry

### 8.1 Exact source and independent universal proofs

Let J=diag(J2,J2,J2)onC6,J2=[0 1;-1 0], realskewunitary, J^2=-I. With unnormalizedOmega6andSWAPF6put

```
T_J=(I tensorJ)F6(I tensorJ*),
W6=2I36-P(Omega6)-2T_J,
R6=I36+P(Omega6)+T_J.                                    (8.1)
```

Ancestry is Park2602.09860v3Eq9andThm3.4atd6k2,p=-1/9,q=-2/9; the source's NORMALIZEDChoi convention gives W6=54C_L, equivalently the unnormalized Choi matrix of9L. Its capture hash is in the ledger. The direct proof below, not an unread source claim, is the correctness premise.

Compress Aliceonto ANYcomplex orthonormal k-plane, k=2or3, with basisa_i. ProjectedOmega6is m=sum_i|i>tensorconj(a_i), squared normk. The projectedT_Jis exactlyflip on Ck tensorV,V=span{J a_i}, and zero on BobVperp. The coefficient matrix of m's Vcomponent is skew, with entries <J a_j,conj(a_i)>; J^T=-Jgives this overCOMPLEXnumbers. Write its squared normq; it lies in the antisymmetricspace and the outside component has squared normk-q.

For P0=kI-2T, the relevant eigenvalues are k+2on the antisymmetricspace and koutside. The symmetricspace has eigenvaluek-2but no mcomponent. Thus mis in rangeP0and

```
<m,P0dagger m>=q/(k+2)+(k-q)/k
               =1-2q/[k(k+2)]<=1.                       (8.2)
```

Whitening proves P0-P(m)>=0on the ENTIREcomplexkx6compression. Therefore W6is two-block-positive and W6+I36is three-block-positive. No real planes or sampled product vectors are used.

Also R6>=0because T_Jis a Hermitian involution and I+T_J>=0. Its complete PTis

```
R6^Gamma=I36+F6+P(vecJ*)>=0.                              (8.3)
```

This is the actual PPTpositive half, not a borrowed Schmidt3lower-bound through projection.

### 8.2 Arbitrary complexisometries and actual matrices

For ANYA,B:C4->C6with A*A=B*B=I4, define localcompressions W_AB,R_ABof W6,R6. Every complexSR<=2vector embeds into one, so W_ABis universally two-block-positive. W_AB+I16is similarly three-block-positive. R_ABis PSDand PPT; for complexBits PTis the congruence of R6Gamma by A* tensorB^T and its adjoint, not an unjustified realtranspose.

Set

```
M=A*conjB,N=B*J A,T_N=(N* tensorN)F4=(I tensorN)F4(I tensorN*),
W_AB=2I16-P(vecM)-2T_N,
R_AB=I16+P(vecM)+T_N.                                    (8.4)
```

M,Nare operatornorm contractions. GenericMis NON-MEand genericNnonskew; the positive part2I-2T_Nis nonlocal, not merely a diagonalDrelabel. Source d6indecomposability does NOTautomatically survivecompression; canonical d4conclusions do NOTautomatically cover arbitraryunmatched data.

With x=||M||_F^2,y=||N||_F^2,z=<vecM,T_NvecM>real, the exact traces are

```
TrR_AB=16+x+y,
Tr(W_ABR_AB)=32+x-x^2-3z-2y^2.                            (8.5)
```

Indeed TrT_N=y,TrT_N^2=y^2,TrP(vecM)^2=x^2; this is symbolic trace algebra, not executed matrix multiplication.

## 9. C7A — COMPLETEsame-compression pair obstruction and a genuinely different control

### 9.1 Whole complex-domain inequality

Put P=A A*,Q=conjB B^T,Theta(X)=Jconj(X)J*. These are rank4projections inC6and a Frobenius-isometric anti-linear multiplicative involution. Cyclic traces give

```
x=Tr(PQ),y=Tr(PThetaQ),z=-Tr[QPTheta(QP)].                 (9.1)
```

Both x,yare in[2,4]by rank4intersection in dimension6. Let C=QPJ. Direct transpose identities give

```
C^T=-ThetaP ThetaQ J,<C^T,C>_F=z,||C||_F^2=x,
z+x=(1/2)||QP-ThetaP ThetaQ||_F^2.                        (9.2)
```

The last follows by computing the symmetricpart ofC, retaining everycomplexphase. Split the difference as(Q-ThetaP)P+ThetaP(P-ThetaQ). Projection norms are1; the two difference norms agree underTheta. Their squared norm is8-2y. With a=4-x,b=4-yin[0,2],

```
z+x<=4b, z<=-4+a+4b,
Tr(W_ABR_AB)>=a(4-a)+2b(2-b)>=0.                          (9.3)
```

The bound is strictwhen x<4. This closes ALLsame-compression pairs, not a parametergrid. It does NOTprove W_ABdecomposable on everyPPTinput or SN(R_AB)<=2.

### 9.2 Concrete rank16/PT11state, but honestly decomposable matched witness

A=B=(e0,e1,e2,e4)gives M=I4,N=J2oplus0and

```
rho=[I16+P(Omega4)+T_N]/22.                               (9.4)
```

It is rational/22,FULLrank16andPTrank11with full-rank marginals. I+T_Nhas a one-dimensionalOmega2kernel on the firstpair, filled byP(Omega4). Its PTis I+F4+P(vecN*), the rank10symmetricspace plus oneantisymmetricray. This escapes the retired rank12/PT9state/singlefilterorbits; a singularfilter cannot make its marginalrank4.

The witnessW_Nhasrank13, a negative2x2block[2 -2;-2 0]on normalizedOmegas of the two pairs, and W_NGammahas eigenvalue-1on normalizedvecN*. Non-PSDandnon-CCPare NOTindecomposability certificates. Here it is EXPLICITLYdecomposable: letNplus=J2oplusJ2,Nminus=J2oplus(-J2),Nsecond=0oplusJ2. W_Nplus/minusarePSDsinceTis an involution, Omega4lies in its-1spaceandP(Omega4)has eigenvalue4there. Then

```
W_N=(W_Nplus+W_Nminus)/2+2T_Nsecond,
T_NsecondGamma=P(vecNsecond*)>=0.                        (9.5)
```

This matched control cannotdetectANYPTTstate. Genericunmatched W_ABis NOTclassified by(9.5).

## 10. C7B — the ENTIREliteralcomplexR_xchart is missed by this inherited witness class

This is a DIFFERENTactualPPTinput, not the samecompressioncontrol. For anyx inC4put

```
a=00+11+22,b=01+12,c=10-21,
d_x=02+|3>tensorx,e=20+33,f=30,g=32,j=23,h_x=|0>tensorx,
R_x=P(a)+P(b)+P(c)+3[P(d_x)+P(e)+P(f)+P(g)+P(j)+P(h_x)].    (10.1)
```

Its trace is25+6||x||^2. It is the LITERAL[I4|x]published-corefilterchart, not an arbitrary furthernonunitaryoutputfilter paired with unchanged witnessbounds. Direct completePPTeligibility: withR3=P(a)+P(b)+P(c)+3P02+3P20,

```
R3Gamma=P(02+11-20)+2P(02+20)+P(01+10)
                              +P(12+21)+P00+P22,
R_xGamma=R3Gamma+3P(32+|0>tensorconjx)
               +3P(|3>tensorconjx)+3P(30+23)+3P33.         (10.2)
```

All terms arePSD. No old21table or nativeN4premise is used. RankR_x<=9by its ninegeneratorsandbothmarginals have rank4already fromaande. Thus it is outside the adopted rank12stateorbit; this observation is not an assertion about arbitraryconvexfilteredclosures.

For EVERYisometric W_ABin(8.4),

```
Tr(W_AB R_x)>=0 for ALLcomplexxandALLcomplexA,B.           (10.3)
```

Proof. W_AB+I16is THREEblock-positive from(8.2), so <a,W_ABa> >=-3because||a||^2=3. All generators otherthanaareSR<=2. In particular the ACTUALbufferpairf30,g32satisfies

```
<f,W_ABf>+<g,W_ABg>
=4-(|M30|^2+|M32|^2)-2(|N03|^2+|N23|^2)>=1,              (10.4)
```

by oneROWnorm ofMand oneCOLUMNnorm ofN, each<=1. Their coefficients3compensate the onlypotential-3coreexpectation. Everyothergeneratorb,c,d_x,e,j,h_xhas nonnegativeexpectation bytwo-block-positivity. Summingproves(10.3), including all simultaneousgenericcore/auxiliaryxcomponentsandallphases.

This theorem does NOTprove allR_xSN<=2or W_ABdecomposable onallPPTstates. Arbitraryadditionalnonunitaryoutputfilters are notcoveredwithouttransformingandprovingthecorrespondingwitnessbounds. The old x1111retirement remains atitsownaccepted37-termproof; its21tableandN4statusarenotrecertified.

## 11. C8 — EXACTsurviving independent-compression negative gate

Use INDEPENDENTcomplexisometries(A,B)forW6and(C,D)forR6. Their dataareM1,N1andM2,N2;letxj=||Mj||_F^2,yj=||Nj||_F^2. Both universalCOMPLEXSR2positivityandactualPPTarealreadyprovedinSection8. The EXACTremainingtraceconditionis

```
E=32+2x2+2y2-x1-2y1-|Tr(M1*M2)|^2
                    -z12-2z21-2|Tr(N1*N2)|^2 <0,
z12=<vecM1,T_N2vecM1>, z21=<vecM2,T_N1vecM2>.              (11.1)
```

This is the full symbolicoperatortrace;Tr(T_N1T_N2)=|Tr(N1*N2)|^2. For examplez12=Tr[M1* N2* M1^T N2^T],withallconjugationsretained. It is NOTasamepairsubstitution. Neithertheorem(9.3)northeRxcharttheorem(10.3)proves(11.1)nonnegative.

An explicitGaussian-rationalchoiceofallfourisometrieswithE<0wouldgivearationalPPTstateR_CD/TrR_CDanduniversallycomplexSR2negativewitnessW_AB,andhenceSN>=3atwrittenalgebraicscope. NOsuchinputhasbeenfoundorclaimedhere. Noristhereanunrestrictedno-gofor(11.1),allW_AB,allR_AB,orP44. The exactfirstunprovedstepisthenegativeeligiblecrosspair,oratrueuniformobstructionforit;theuniversalpositivehalfisnotmissingandnotbeingguessedfromeigenvalues.

The productdiagonalrouteofSection2alsoremainsaliveONLYonactualstatesoutsidetheprovedSN2regions. ThisdoesnotauthorizeanotherD/SNRlabelonthesameretiredrectangle. Auniformno-goforEorthefullDroutewouldSTILLnotbeanunrestrictedM4theorem.

## 12. Bound source ledger and separately labeled context-only records

### 12.1 Live source bindings

These SHA256s were freshly observed together in one metadata command before this consolidation. All paths except RUN are relative to this owner's exclusive root. Proofs for every requested claim are COMPLETEabove; ancestry is not an unseen extra proof premise.

|ID|Actual source|SHA256|Role in this current body|
|---|---|---|---|
|S1|anisotropic-Weyl-positive-background-consolidated-v1.md|fa39d6a671455eec40a7f05b0c48ec80cd3b63f0b395920609de8611a8d64d3c|Section2fullD ancestry; iff/PPT/tests fully rederived here|
|S2|coherent-PPT-target-and-low-rank-peel-lifting-gate-v1.md|f7f7eb1befb0a9ff3fe368c91f69ca2373cb616737fa6219418befa8f4b3ab37|Eligibility ONLYoriginalLF1–61; full proof reprinted Section3; omitted peel is NOTan imported theorem|
|S3|coherent-full-rectangle-SN2-14phase-kernel-certificate-v1.md|dcebacbc78e7a5ab25c4914a3b413d58d87398b093b617e1246e4ca73a0725d6|Complete14phaseproof rederived Section4; prior verdict ONLY(4.8)|
|S4|coherent-PPT-Schmidt-two-wedge-24phase-decomposition-v1.md|f0a6bda317cadd4ca6657cfd5c5d030acfd26b244e494f0fd2c917d367e3b338|NewrequestSection5; no14inheritance|
|S5|balanced-parity-exact-SN2-criterion-and-frustrated-PPT-example-v1.md|cff29ac85ad1073af3778e7def5111cea878484248a667c8391186a764e9b669|NewrequestSections6–7; no14inheritance|
|S6|inherited-two-positive-cross-compression-and-same-pair-no-go-v1.md|1c457b84beead2d5a367c5d74ad044ca04e64cd4d1d58dee8bd16b93ea0ae523|NewrequestSections8–11; allpositive/PPT/barrierproofs complete here|
|S7|2602.09860v3.txt|f8da946255c91889f77fbc1cc8f553e849f289255a341a280e9fa823afce27af|Publishedancestry ONLYEq9LF1960–2050/Thm3.4LF2238–2385; directproof(8.2)does not consume an unseen paperproof|
|P1|RUN/ppt-coherent-rectangle-SN2-parent-v1.md|992874f1375664e66c6a9b438dd72e22776222a96dfe5d179606e12eef006682|FULL27LFread; binding existing adopted boundary(4.8), not a new verdict for this body|

RUN means `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-23-96h/`. Source7is Park's arXiv2602.09860v3; no literature-wide status/priority clearance is inferred from reading its displayed portions.

### 12.2 CONTEXT ONLY — not extra correctness/adoption requests, not silently closed by14phase

The following immutable records remain on disk with their OWNclaims/receipts/limits. They are superseded ASCURRENTPRIMARYMETHODOBLIGATIONS or retained as context ONLY, not mathematically erased. No assertion of their current parent-review status beyond their own receipts is made here. They are NOTproofpremises for C1–C8.

|Context record|Freshly observed SHA256|Explicit non-transfer boundary|
|---|---|---|
|nonME-three-ray-complement-scalar-obstruction-v1.md|7f520ee82c7e26df39a5ac69943ec956ebd751dc38a250bcd1e838e3f6a657c4|Flat nonMEgeometry result is not an arbitraryD/globalclosure and not adopted by14phase|
|nonME-three-ray-local-filter-escape-ADDENDUM-1-v1.md|dded6b0159c6a0155076f006cd18f0e8ba946ac39859f23b4981be0b3fcdd7a9|Single-filterorbit statement is NOTcone/convexclosure escape; not needed here|
|all-phi-full-diagonal-coherent-rectangle-no-go-v1.md|2c5e33f0e16632ffb4063e2fd68b9850a0111d084bbff57149123e5202d8364c|Its strict quantitative witnessmargin does NOTfollow automatically from SN<=2; not retroaccepted or re-proved in this gate|
|anisotropic-Weyl-actual-PPT-face-rigidity-v1.md|63b7afafa63e5d8aca4652b25cb493770e7165adb6031a4af24bbcbeef2ec8c7|Specific two-range face condition, not arbitraryPPTinput/SNclassification|
|anisotropic-Weyl-actual-PPT-face-rigidity-ADDENDUM-1-corollary-v1.md|f926c30e4bef2eebf2b3e1db262a94d2bca41679265694f1283b0a24d8029f72|Specific corollary only; not consumed by laterstateproofs|
|all-diagonal-PPT-completions-of-Weyl-Q-moment-no-go-v1.md|42db78178c1400cd063707de9fd2f3321b6aefdb43d09aa2547d8f9034226a76|Moment nondetection is NOTan SN2operatoridentity or arbitraryDdecomposability|
|unequal-Weyl-coherences-low-noise-SN2-consolidated-v1.md|d964304d3c0b6050048911f7ff38842b30d483d72362bcdda283357ec544dfb3|Its own unequalconstant-high/low-only statefamily, not generalcomplexblocks|
|circulant-four-offset-background-PPT-no-go-consolidated-v1.md|72984522f6547301d39ffb2030fca584bd7af4f3864a3955281e172cfb89b5b0|Four-offsetwitness reduction is not arbitrary16entryD; objective-preservingreplacement is not original-stateSN2|

The reverse-peel/lower-output-rank/corrected6x6lifting material in S2AFTERoriginalLF61is likewise a freestanding method candidate, NOTaccepted by the14gate and NOTa correctness premise here. Older scalarfour-Weyl, arbitrary<=3MEscalar, one-BellD-type, two-Bellcyclic, two-level and oldauxiliary/corecompression routes remain at THEIRexact old scopes/dispositions; none is reopened as a winning method or silently upgraded to an unrestricted theorem. The oldx1111SN2retirement is still ONLYat its accepted37-termproof, not an old21table repair.

No context-only theorem is being declared true merely because the retiredrectangle is SN<=2. Conversely, non-adoption in THISgate is not a withdrawal of a separate earlier disposition. This table prevents hidden extra proof obligations and false inheritance.

## 13. Full remaining original problem, not a narrowed success

The original physics-3P44acceptance remains UNMET. It requires EITHER:

1. an explicit rational/Gaussian-rational4x4densityoperator with exact PSD/PPTand an actual Schmidt-number>=3certificate, in particular a Hermitian separator nonnegative on EVERYcomplexSR<=2vector with strictly negative expectation on that actualPPTstate; OR
2. a genuinely UNRESTRICTEDwritten theorem that every4x4PPTstate has Schmidt number<=2 (equivalently an appropriately complete all-mapno-go), not another state/witnessclass barrier.

No such state/separator pair or unrestricted theorem is delivered by this consolidation. The exact live cross-compression gap is(11.1); the exact fullDresidual is(2.3)–(2.6). Their nonempty/empty status is not guessed. Necessary test satisfaction is not universal positivity, inherited sourceindecomposability is not M4indecomposability, and sourceSN3does not survive projection by fiat. The symmetric-extension/kernel/executable gates requested for a winning finiteclaim have not been conferred; no nativeGOhas been issued.

The adopted rectangle(4.8)stays permanently RETIREDagainstANYwitness. Additional stateclasses retired by Sections5–7are only at their explicitly requested new WRITTENclaims pending this complete fresh gate. None changes the original cutoff/deadline, registryslot, oldresource/exit history, arithmeticadmissionhistory, or stronger verification/novelty requirements. The round remains active, not closed.

**END OF SINGLE COMPLETE CURRENT CONSOLIDATION — PART1/1.**
