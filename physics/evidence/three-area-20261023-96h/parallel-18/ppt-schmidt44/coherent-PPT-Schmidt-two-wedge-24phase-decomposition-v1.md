# A whole coherent PPTwedge has SN<=2: explicit24rank-two phase vectors and product residuals

PhysicsPPT44-2. Actual `/bin/date` before creation: **Sun Oct 25 13:39:58 PDT 2026**. **AUTHOR-WRITTEN CANDIDATE; fresh independent reconstruction and parent disposition pending.** This is a literal conic operator identity, not machine or finite-witness acceptance. No NEWscientific eval/program/arithmetic interpreter/enumeration/symbolic/numerical computation/solver/replay/compile, nativeGO, externalCLIor nestedagent. HOLD/v9/v10/v11and original deadline remain binding; older checkpoint013cadence miss remains disclosed.

Interface `checkpoint-031-coherent-PPT-Schmidt-two-wedge-lead-v1.json`, SHA-256 `f41a18697dfe5f8fd6cf04db4812d7e230d51a38bb38681188b0eec7ec9bb2ac`, was frozen after informal written leads, not called preregistered before all reasoning. This proof concerns the ACTUALstate, unlike the earlier diagonal moment control, which did NOTdecompose that state. No P44Schmidt3claim is made.

## 1. State, region, and named eligibility import

All indices are modulo4. Set E_q e_j=|j,j-q>, F_(j,0)=1/2,F_(j,1)=i^j/2, B=F F*. For0<s<1,t>0, let

```
R0=F[1 s;s 1]F*, R1=tB,
R2=diag(y0,y1,y2,y3), R3=diag(z0,z1,z2,z3),
y0=y2=t^2/4,
y1=t^2/[4(1+s)]+s/2, y3=t^2/[4(1-s)]+s/2,
z0=z3=(1+s)^2/(4t), z1=z2=(1-s)^2/(4t),
R=sum_q E_q Rq E_q*,
N=TrR=2+2t+s+t^2(2-s^2)/[2(1-s^2)]+(1+s^2)/t.             (1)
```

The full PSD/four-complex-PTblock proof, rank12/PTrank9, and actual failure of jointX/Jand the old rank8PTface are the named WRITTENimport `coherent-PPT-target-and-low-rank-peel-lifting-gate-v1.md`, SHA-256 `f7f7eb1befb0a9ff3fe368c91f69ca2373cb616737fa6219418befa8f4b3ab37`, Section1. This source does not confer independent or executable acceptance on that import.

**Theorem.** The normalized state R/Nhas Schmidt number AT MOSTtwo throughout the region

```
4y1y3>=1,  t^2<=1-s^2.                                  (2)
```

In particular this is not a Schmidt3candidate in that region. No statement that the Schmidt number is EXACTLYtwo, no extension of(2)to all0<s<1,t>0, and no unrestricted no-go is asserted.

The region is nonempty with interior: at(s,t)=(2/3,2/3),

```
y1=2/5, y3=2/3, 4y1y3=16/15>1,
t^2=4/9<5/9=1-s^2.                                      (3)
```

## 2. The only finite average used

Let Omega4={1,i,-1,-i}. For wuniform in Omega4,

```
avg w=avg w^(-1)=avg w^2=avg w^(-2)=0,
avg |w|^2=1.
```

Thus a vector whose three coefficient groups carry characters0,1,-1has phase-average projector equal to the sum of the three group projectors. This is an EXACTfinite Fourier identity. The four phases DEFINEthe decomposition; they are not samples of a universal positivity condition.

## 3. Eight rank-two vectors give R0and part of R2

For epsilonin{+1,-1}, put

```
A_epsilon=sqrt((1+epsilon s)/8),
h_epsilon(j)=A_epsilon(1+epsilon i^j),
p_epsilon=sqrt2 A_epsilon,
eta=sqrt(y1/y3)>0.
```

For w in Omega4define coefficient matrices

```
C_epsilon(w)=diag(h_epsilon)
       +p_epsilon[sqrt(eta)w E13+eta^(-1/2)w^(-1)E31].    (4)
```

After the simultaneous row/column order0,2,1,3, the even2by2block is diagonal with one entry zero: h_epsilon(0)h_epsilon(2)=0. It has rank1. The odd2by2block has diagonal product2A_epsilon^2and off-diagonal product p_epsilon^2=2A_epsilon^2. Hence that block has determinant zero and rank1. Consequently

```
rank C_epsilon(w)<=2                                    (5)
```

for EVERYdisplayed complexphase (indeed all nonzero w), with no real-vector restriction.

The phase average kills the high/low cross terms and the low/low13/31coherence, while keeping the highcoherences. Summing epsilon gives the EXACToperator identity

```
(1/4)sum_(epsilon,w) P(vec C_epsilon(w))
  =E0 R0 E0*+(eta/2)P(13)+[1/(2eta)]P(31).                (6)
```

To check the high block directly, h_epsilon=A_epsilon(u+epsilon v), with u_j=1,v_j=i^j. The sum of their projectors is

```
(1/4)(u u*+v v*)+(s/4)(u v*+v u*)=R0.
```

The two low populations follow from `2(A_+^2+A_-^2)=1/2`. Since sqrt(y1y3)>=1/2by(2),

```
r2_0=y0, r2_2=y2,
r2_1=y1-eta/2>=0,
r2_3=y3-1/(2eta)>=0.                                   (7)
```

Thus E0R0E0*+E2R2E2*is the eight rank-two phase projectors in(6)plus sum_j r2_jP(j,j-2).

## 4. Sixteen rank-two vectors give R1and part of R3

Put A=sqrt(t)/4,p=sqrt2 A. For k=0,1,2,3, set

```
h_k(j)=A(1-i^(-k)i^j),
r=k-1,l=k+1,
eta_k=sqrt(z_k/z_(k+2))>0,
N_k(w)=X[diag(h_k)
       +p(sqrt(eta_k)w E_rl+eta_k^(-1/2)w^(-1)E_lr)].     (8)
```

Before the invertible leftX, the kdiagonal is zero, the opposite k+2diagonal is2A, and the r/lblock has diagonal product2A^2and off-diagonal product p^2=2A^2. Therefore it consists of one rank-one r/lblock and one isolated nonzero diagonal: rankN_k(w)<=2EXACTLY.

After multiplying by X, the two low entries are positions(k,k+1)and(k+2,k-1), both difference3. Their phase-average populations are p^2eta_kand p^2/eta_k. For the high block,

```
sum_k h_k(j)conjugate(h_k(l))
 =4A^2(1+i^(j-l))=tB_(j,l).
```

The simultaneous shift of high rowlabels byXleaves Bunchanged because it depends only on j-l. Hence the ACTUALfulloperator identity is

```
(1/4)sum_(k,w)P(vec N_k(w))
 =E1 R1 E1*+sum_j n3_jP(j,j+1),
n3_j=(t/4)sqrt(z_j/z_(j+2)).                             (9)
```

Each opposite pair receives its two contributions from kandk+2, using eta_(k+2)=1/eta_k. There are no omitted coherences: they have characters1,-1or2and vanish in the exact phase average.

Here

```
sqrt(z_jz_(j+2))=(1-s^2)/(4t).
```

Thus the second condition in(2)gives

```
r3_j=z_j-n3_j>=0                                        (10)
```

for every j. E1R1E1*+E3R3E3*is therefore the sixteen rank-two phase projectors in(9)plus sum_jr3_jP(j,j+1).

## 5. Complete conic identity and normalized ensemble

Adding(6)and(9)with all product residuals gives the literal identity

```
R=(1/4)sum_(epsilon,w)P(vec C_epsilon(w))
 +(1/4)sum_(k,w)P(vec N_k(w))
 +sum_j r2_j P(j,j-2)+sum_j r3_j P(j,j+1).                (11)
```

Every coefficient is nonnegative by(2),(7),(10). Every displayed coefficient matrix has rank<=2, and the eight possible residual vectors are product. This is an operator decomposition of RITSELF, not only its diagonal moments or a witnessobjective.

For the unit trace state, replace every nonzero phase vector psi by psi/||psi||with weight `||psi||^2/(4N)`, and give the residual product vectors weights r2_j/N,r3_j/N. The weights sum to1by taking the trace of(11). They are NOTuniform1/24. Terms with a zero residual coefficient may simply be omitted; no singular division is needed in the stated open parameter domain. This proves SN(R/N)<=2with24rank-two terms and at most8product terms.

## 6. Explicit Gaussian-rational example, not a winning P44state

At(s,t)=(2/3,2/3), N=611/90. The density matrix is explicitly

```
rho=[sum_q E_q Kq E_q*]/2444,
K0(j,l)=90(1+i^(j-l))+60(i^j+i^(-l)),
K1(j,l)=60(1+i^(j-l)),
K2=diag(40,144,40,240),
K3=diag(375,15,15,375).                                  (12)
```

The four block traces are720,480,464,780and sum2444. All real/imaginary entries are integers divided by2444, with PSD/PPTat the named written import and the exact written SN<=2decomposition above. The rank-two vectors have algebraic square roots; the density matrix is Gaussian-rational. No machine check or real-rational-entry claim is made.

## 7. Exact scope, acceptance, and remaining primary work

This source establishes the displayed actual-state upper-bound region, pending independent written reconstruction. Reading `finite-witness-triple-verification` does not authorize the prohibited scientific/checker/CLIsteps, and none was performed. This is NOTa three-checker acceptance, kernel proof, solver certificate, human/vendor/family/novelty/SOTAor P44settlement.

The currently live rectangle s in[1/2,2/3],t in[9/10,11/10]is OUTSIDEthis wedge, since t^2>=81/100>3/4>=1-s^2. Its Schmidt number is NOTclassified by(11). The separate full-diagonal nonMEpair-family obstruction there (`all-phi-full-diagonal-coherent-rectangle-no-go-v1.md`, SHA-256 `2c5e33f0e16632ffb4063e2fd68b9850a0111d084bbff57149123e5202d8364c`) is not a substitute for SN<=2. Conversely, this exact decomposition does not transfer outside(2).

Retire the wedge as a source of Schmidt3candidates. The original full16entryD-(Q0+Q1)and true outside-quantifier geometries remain live; the missing deliverable is still a rational PPTstate with a universal COMPLEXSR2negative separator/certificate, or an unrestricted no-go. Old N4UNKNOWN/exit-unestablished, old21unreconstructed and all later overlays remain unchanged. No new scientificexecution/GOor deadline reset.
