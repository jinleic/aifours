# Actual noncirculant rational PPT target and exact complex reverse-peel gate

PhysicsPPT44-2. Actual `/bin/date` before manuscript: **Sun Oct 25 12:50:39 PDT 2026**. **AUTHOR-WRITTEN CANDIDATE; independent reconstruction and parent disposition pending.** Source/clock/hashonly; no scientific program/eval/interpreter/arithmetic enumeration/symbolic or numerical computation/solver/replay/compile. HOLDv2and v9/v10/v11remainbinding. Same originalP44, no new slot/GO/reset. Older checkpoint013cadence miss remains disclosed.

This manuscript supplies the full actual PPTstate from checkpoint021, an exact general rank-two-positive peeling refinement, and the literal non-MEanisotropic bridge and its PPTcost. It does NOTsupply a sound separating witness or claim Schmidt number3. The first unproved primary gate is explicit in Section7. This is a new representation of that live gate, not another scalar-control promotion or an unrestricted no-go.

The interfaces were frozen after informal written leads in `checkpoint-024-low-rank-peel-and-coherent-target-bridge-v1.json`, SHA-256 `4d6f485c351ed2e926a360eb51ff461525726b5bcaa3889d9d0d9eabd433e504`; this is not retroactive preregistration. Source ancestry is Yang–Leung–Tang1603.03534v1, Theorem2.7and its complete proof, actual read LF524–816of `1603.03534v1.txt`, SHA-256 `bae7f6812521bdd75a1bcd0f2a2affd7dd344e5feaf4109c2873259aeed1deea`. The literal correction/rank-refinement/targetcost below are rederived, not claimed to be that paper's conclusion or new SOTA.

## 1. Full coordinate-asymmetric PPT family

Indices are modulo4. Define embedding E_q e_r=|r,r-q>, F_(r,0)=1/2,F_(r,1)=i^r/2, and B=F F*, so B_rk=(1+i^(r-k))/4. For0<s<1,t>0put

```
R0=F [1 s;s 1]F*,   R1=tB,
R2=diag(y0,y1,y2,y3), R3=diag(z0,z1,z2,z3),
y=(t^2/4, t^2/[4(1+s)]+s/2, t^2/4,
             t^2/[4(1-s)]+s/2),
z=((1+s)^2/(4t),(1-s)^2/(4t),
             (1-s)^2/(4t),(1+s)^2/(4t)),
R(s,t)=sum_(q=0)^3 E_q Rq E_q*,
N(s,t)=2+2t+s+t^2(2-s^2)/[2(1-s^2)]+(1+s^2)/t,
rho(s,t)=R(s,t)/N(s,t).                                (1)
```

This specifies every entry of an actual16by16matrix. Each Rqis PSD: F's columns are orthonormal, the coefficient matrix has positive eigenvalues1+-s, R1is positive on its two-plane, and all y,zentries are positive. Their traces give the displayed N>0. RankRis2+2+4+4=12.

For clarity, the partial transpose preserves total-index tau=r+kmodulo4. Its four ACTUALHermitian blocks on basis{|r,tau-r>}have entries

```
S_tau(r,k)=R_(r+k-tau)(r,k).                             (2)
```

Here are all four PSDproofs, including the non-real phases.

- tau0: order highindices0,2then lowindices1,3. Highdiagonal is((1+s)/2,(1-s)/2). The high-to-low matrix is diagonal, each entry t(1-i)/4. The lowdiagonal is(y1,y3), with off-diagonal i s/2. Its exact Schur complement is `(s/2)[1 i;-i 1]`, which is PSDofrank1. Thus S0is PSDofrank3.
- tau2: order highindices1,3then lowindices2,0. Highdiagonal is(1/2,1/2), high-to-low is again diagonal t(1-i)/4, and lowdiagonal(t^2/4,t^2/4). The lowcross is zero, so the Schur complement is zero. These are two rank-one2by2blocks; S2has rank2.
- tau1: disjoint pairs of rowindices1/0and3/2. Each highdiagonal is t/2. The paired lowdiagonals are(1+s)^2/(4t),(1-s)^2/(4t), and high-to-low entries are(1+s)(1+i)/4,(1-s)(1+i)/4. In each case the positive diagonal product equals the squared off-diagonal modulus. Thus S1is PSDofrank2.
- tau3: disjoint pairs0/3and2/1with the same respective positive diagonals and off-diagonal moduli as tau1. Hence S3is PSDofrank2.

There are no other entries: R2,R3are diagonal; B's opposite entries vanish; and `R0(2,0)=0`, while `R0(1,3)=i s/2`. Thus(2)exhausts the entire partial transpose, not selected principal submatrices. It follows that R(s,t)is PPTwith PTrank3+2+2+2=9.

The nonzero opposite entry `R0(1,3)=i s/2` proves the state is not a common-Qplus-product-diagonal completion, not the earlier unequalconstantQ0/Q1pluslowdiagonal family, and not the paired-Bell eight-coefficient form. Joint Xtranslation maps this entry to R0(2,0)=0, so the target is genuinely shift-asymmetric. Jinterchanges the highdifference0/1supports, but R1's opposite entries vanish, so it is also not J-invariant. Its PT rank9cannot lie in the old rank8PTface. No restricted geometry is silently transferred.

### An explicit Gaussian-rational density matrix

At s=1/2,t=1, N=83/12. Define integer-Gaussian blocks

```
K0(r,k)=12(1+i^(r-k))+6(i^r+i^(-k)),
K1(r,k)=12(1+i^(r-k)),
K2=diag(12,20,12,36), K3=diag(27,3,3,27).
```

Then

```
rho(1/2,1)=[sum_q E_q Kq E_q*]/332.                     (3)
```

Traces of the four blocks are96,96,80,60, summing332. Every real and imaginary entry is an integer divided by332. This is Gaussian-rational, NOTa claim that all entries are real rational. The proof above certifies PSDand PPTin written algebra; no interpreter verified it. There is NOclaimed Schmidt3certificate for(3).

## 2. General exact reverse-peel criterion, including singular anchor blocks

Let any Hermitian W on C4tensorC4be grouped by an Aliceanchor basis vector, with

```
W=[A B;B* C], A12by12, C4by4.
```

If W is two-block-positive then C>=0. Compressing to the anchor and each other Alicevector gives an ordinary PSD8by8matrix: every vector supported on two Alicelevels has Schmidt rank<=2. Therefore rangeB_i*is contained in rangeCfor each BobblockB_i, hence rangeB*subsetrangeC.

Write Cdaggerfor the Moore–Penrose inverse and define

```
U=[B;C] Cdagger [B* C]>=0,
K=A-B Cdagger B*,
W=U+lift(K).                                            (4)
```

Rangecompatibility makes the displayed equality exact even when C is singular. Uis an actual PSDChoi matrix (a completely positive summand), not a guessed scalar noise term. Its Bob-vector expectation is the completed square

```
<x,Kx>+||C^(1/2)y+C^(dagger/2) sum_i B_i* x_i||^2,        (5)
```

for ket sum_i|i>x_i+|anchor>y.

For every COMPLEXBobtwo-plane V, let P_(C^(1/2)V)denote the orthogonal projector onto its exact linear image. Minimizing(5)over yIN Vgives

```
<x,Kx>+||(I-P_(C^(1/2)V))C^(dagger/2)sum_i B_i*x_i||^2,
                         x_i IN V.                     (6)
```

Thus W is two-block-positive IFF(6)is nonnegative for every V and all three Bobvectors x_iinV. This is an actual6by6PSDtest for EACHcomplexplane, not just the forward statement that K is positive. It is necessary because the minimizing yis inVand yields a genuine Schmidt-rank<=2ket; sufficient because every such ket has all its Bobvectors in some V. Lower Schmidt rank is included by extending its Bobspan.

For comparison, forward Choipeeling only says K is block-positive. That implication follows directly here: take x_i=a_i b(product on the three remaining Alicelevels)and set y=-Cdaggersum B_i*x_i. All Bobvectors then lie in span{b,y}, of dimension<=2, while the square in(5)vanishes. The converse 'Kblock-positive implies Wtwo-positive' is NOTvalid; the omitted lifting constraint is precisely(6).

## 3. Strengthened low-output-rank extension barrier

**Lemma.** If W is two-block-positive and rankC<=2, then the residual K in(4)is STILLtwo-block-positive, not merely block-positive.

Proof. For a dense set of complex Bobtwo-planes V, `C^(1/2)V=rangeC` when rankC<=2. For such Vthe correction in(6)vanishes because C^(dagger/2)B*xbelongs to rangeC. Therefore the compression of Kto all three Alicelevels timesV is PSD. Those compressed Kmatrices vary continuously with V; density gives the same PSDcondition for every V. This is exactly Ktwo-block-positivity. RankC0is trivial; ranks1and2use the open dense full-image condition. No pseudoinverse continuity at singular C is assumed: C is fixed throughout the argument.

**Two-step corollary.** A non-PSDtwo-block-positive4by4W cannot admit TWOsuccessive anchor peels of output rank<=2, with arbitrary Alicebasis choices at each step. The first residual remains two-block-positive on3by4. A second such peel leaves a two-block-positive2by4matrix, which is PSDbecause every2by4vector has Schmidt rank<=2. Adding both PSDsummands back makes the original WPSD, a contradiction.

This is a conditional structural no-go for cheap low-rank extension/lifting mechanisms, NOTan unrestricted M4decomposability theorem. A single peel still leaves the open3by4two-positive residual case; rank>=3anchors also remain outside the lemma. No unsupported low-dimensional decomposability import is used.

## 4. Literal non-MEnegative geometry and actual full16Dpeel

Use the new genuinely non-MEray

```
phi+=(Phi_I+Phi_Z)/sqrt2,
Q_phi+=P(phi+)+P(Phi_X)+P(Phi_ZX),
W_D=D-Q_phi+, D=sum_ij d_ij P(ij), d_ij>=0.              (7)
```

For generic Dthis is not a scalar completion, so the uniform scalarobstruction of `nonME-three-ray-complement-scalar-obstruction-v1.md` does NOTsettle it. The ray has diagonal coefficients

```
v=(1/sqrt2,(1+i)/(2sqrt2),0,(1-i)/(2sqrt2)).
```

Its nonuniform marginal proves it cannot be ANYpositive MEconic sum, as established in that predecessor's source/Gram section. The negative projection has rank3. The universal all-complex weighted Gram criterion is retained, not replaced by sampled planes or real vectors.

Now select Aliceanchor2. Put

```
h=d21-1/2,
C=diag(d20,h,d22,d23),
c1=(1-i)/4, c3=(1+i)/4,
B0=0, B1=-c1|0><1|, B3=-c3|2><1|.                       (8)
```

These are the ACTUALChoi blocks: v2=0kills the diagonal-ray anchor coherences, while the shifted pair's opposite coefficient is zero. Product tests force C>=0. Moreover the actual two-coordinate block on|10>,|21>has diagonal d10-1/2,h and nonzero off-diagonal-c1. Two-positivity makes it PSD, forcing h>0 (and d10>1/2). Other diagonal entries of Cmay vanish; the formulas do not silently assume invertibility.

The exact PSDpeeled part is

```
eta=-c1|10>/sqrt h+sqrt h|21>-c3|32>/sqrt h,
U=P(eta)+d20P(20)+d22P(22)+d23P(23).                    (9)
```

All its entries are rational-Gaussian when the d_ijare rational, despite the ket's square roots. It is PSD; its ket eta is generally SR3, and no SR2decomposition of U is asserted or needed.

For remaining Aliceindices i,jin{0,1,3}, the literal residual blocks are

```
K_ij=delta_ij diag_j(d_ij)
     -v_i conjugate(v_j)|i><j|
     -[b_ij+c_i conjugate(c_j)/h]|i-1><j-1|,
b_ij=(1+i^(i-j))/4, c0=0.                               (10)
```

Here `diag_j(d_ij)` means `diag(d_i0,d_i1,d_i2,d_i3)`: its j is a dummy Bobindex, independent of the outer inputindex j. There is no sum over inputindex in that positive part.

For x_iinVdefine

```
gamma(x)=conjugate(c1)<0,x1>+conjugate(c3)<2,x3>,
tau(V)=(1/h)||(I-P_(C^(1/2)V))e1||^2.
```

Then the FULLcomplexcriterion(6)specializes to

```
<x,Kx>+tau(V)|gamma(x)|^2>=0
for EVERYcomplex Bobtwo-planeVand ALLx0,x1,x3inV.        (11)
```

The correction is rankone, with0<=tau<=1/h. This is the precise additional lifting gate over ordinary positive3by4K. It works for singular Cother than the forced positive h, since the projector is onto the actual image C^(1/2)V. Neither forward-peel positivity alone nor a rank-one/sampled-plane check is sufficient.

## 5. Exact cost of that CPpeel on the actual eligible PPTtarget

For R(s,t)in(1), eta is supported on its difference1block tB. Its coefficient sums are

```
sum eta_r=(h-1/2)/sqrt h,
sum i^(-r)eta_r=-(h-1/2)/sqrt h.
```

Therefore its projector's exact expectation is t(h-1/2)^2/(2h). Adding the three productterms in(9)gives

```
c(D;s,t)=Tr[U R(s,t)]
 =t(h-1/2)^2/(2h)+d20 t^2/4
   +d22(1-s)/2+d23(1-s)^2/(4t)>=0.                      (12)
```

With sigma the local Aliceprojection of R(s,t)onto{0,1,3},

```
Tr[W_D R(s,t)]=c(D;s,t)+Tr[K sigma].                    (13)
```

Sigma is an actual3by4PPToperator, since local projections preserve PSDand PPT. Formula(13)exhibits the cost that a reverse-peel construction must really beat; an arbitrary positive indecomposable seed Kneed not survive that cost or satisfy(11).

At0<s<1,t>0, equality c=0forces

```
h=1/2, d20=d22=d23=0.                                  (14)
```

Then rankC=1. By Section3, if W_Dwere sound two-positive, Kwould already be two-positive on3by4. A negative score at this zero-cost corner would make sigma a PPT3by4state of Schmidt number3after normalization. Thus this corner is NOTa free bootstrap from ordinary3by4PPTentanglement: it requires an already stronger Schmidt-number phenomenon. This is a structural circular-seed barrier, NOTa claim that such3by4states are impossible.

## 6. What is and is not verified by the written work

The positivity/PPT/ranks of the full actual R(s,t), the precise general Schur correction, low-rank retention lemma, two-step PSDcorollary, actual anchorblocks, residual, and CPcost are WRITTENderivations, with declared source ancestry above. They were not machine-checked or independently reconstructed here. No6by6universal condition has been executed or certified for a new D.

The explicit Gaussian-rational state(3)is only an eligible PPTinterface; it is not presented as a winning Schmidt3candidate. No attractive state's PPTproperty substitutes for a universal complex SR2separator. The scalar nonMEclass is closed at its own written imports; this does not transfer to the anisotropic class(7). The full16DfixedQroute also remains open and is not replaced by this branch.

## 7. Exact first unproved primary step

Find an actual explicit rational Dsuch that BOTH(11)holds for every complex Bobplane AND(13)is strictly negative for an actual target(1), or prove a true obstruction to that full anisotropic class. Block-positive K alone, cheap CPcostalone, an indefinite PT, or finitely sampled product/rank-two vectors proves neither condition. At present no such Dand no unrestricted P44no-go has been delivered.

No N4retry/replay/native execution, old21table rehabilitation, stronger verification/family/vendor/formal/novelty/acceptance promotion, deadline reset or scienceGO is claimed. Primary research continues from the new exact lifting representation rather than parking this gate as completed P44.
