# The ACTUAL coherent PPTrectangle is SN<=2:14phase vectors with two literal kernels

PhysicsPPT44-2. Actual `/bin/date` before creation: **Sun Oct 25 13:53:43 PDT 2026**. **AUTHOR-WRITTEN CANDIDATE; fresh independent reconstruction and parent disposition pending.** Literal rank/kernel and operator identities, NOTmachine/triple-checker acceptance. No NEWscientific interpreter/eval/arithmetic program/enumeration/symbolic or numerical computation/solver/replay/compile, nativeGO, externalCLIor nestedagent. HOLD/v9/v10/v11, original deadline and the disclosed older checkpoint013cadence deviation remain unchanged.

Interface `checkpoint-032-coherent-full-rectangle-14phase-SN2-lead-v1.json`, SHA-256 `83e6699c6a0cafe536669446eb29dfda0704bc37df2d53d3e5d5cc6b213b39fd`, was frozen after disclosed informal written leads, not retroactively preregistered. This is a physical Schmidt-number upper bound for the ACTUALstate, not the earlier moment-only control or restricted witness-class obstruction.

## 1. Target, theorem, and scope

All indices are modulo4. Let E_q e_j=|j,j-q>, F_(j,0)=1/2,F_(j,1)=i^j/2, B=F F*, and define

```
R0=F[1 s;s 1]F*, R1=tB,
R2=diag(y0,y1,y2,y3), R3=diag(z0,z1,z2,z3),
y0=y2=t^2/4,
y1=t^2/[4(1+s)]+s/2, y3=t^2/[4(1-s)]+s/2,
z0=z3=(1+s)^2/(4t), z1=z2=(1-s)^2/(4t),
R(s,t)=sum_q E_q Rq E_q*,
N(s,t)=2+2t+s+t^2(2-s^2)/[2(1-s^2)]+(1+s^2)/t.            (1)
```

Its full four-complex-block PPTproof and rank12/PTrank9are the named WRITTENeligibility import in Section1of `coherent-PPT-target-and-low-rank-peel-lifting-gate-v1.md`, SHA-256 `f7f7eb1befb0a9ff3fe368c91f69ca2373cb616737fa6219418befa8f4b3ab37`. This manuscript gives a direct conic identity, not inherited independent/executable acceptance of that import.

**Theorem.** Every R(s,t)/N(s,t)in the ENTIREcurrent rectangle

```
1/2<=s<=2/3, 9/10<=t<=11/10                              (2)
```

has Schmidt number AT MOSTtwo. There are14explicit rank-two vectors plus four nonnegative product residuals. Thus NOuniversally complex SR2nonnegative witness of ANYform can separate any state in this rectangle, including the concrete integer/332rho(1/2,1). This retires this exact actual-state branch as a source of P44Schmidt3examples.

The theorem does NOTassert exact Schmidt number2, cover all0<s<1,t>0, or prove an unrestricted4by4no-go. The earlier24phase wedge proof (`coherent-PPT-Schmidt-two-wedge-24phase-decomposition-v1.md`, SHA-256 `f0a6bda317cadd4ca6657cfd5c5d030acfd26b244e494f0fd2c917d367e3b338`) is a different parameter region; this later theorem genuinely extends rather than backdates its conclusion.

## 2. One rank-two prototype with TWOexplicit null vectors

Write

```
h_plus=1+s, h_minus=1-s,
H=1-s^2=h_plus h_minus,
u=t^2, a=H/u>0,
d=sqrt(t/8), A_h=sqrt(h/8).
```

For h=h_plusorh_minus, abbreviate A=A_hand define constants

```
b_h=(i-1)(1-a)d^2/A,
c_h=(1+i)(1-1/sqrt2)A^3/(a d^2),
e_h=(1+i)a d^3/A^2,
f_h=-i sqrt2 A^2/d.                                     (3)
```

For any nonzero complex w, define the ACTUAL4by4coefficient matrix

```
M_h(w)=[ 2A             0          0       (1+i)d w ]
       [ 2id w       (1+i)A       0         b_h w^2 ]
       [ 0           (i-1)d w     0         e_h w^3 ]
       [ f_h w^-1     c_h w^-2    0         (1-i)A ].     (4)
```

Its column2is ZERO, giving the first null vector e2. An independent second one is

```
xi_h(w)=(1,-a(d/A)(1+i)w,0,-(A/d)(1-i)w^-1)^T.           (5)
```

Every row product with(5)vanishes. Explicitly, after removing the common wpower, the four identities are

```
2A-A(1+i)(1-i)=0,
2id-2iad-2id(1-a)=0,
2a d^2/A-e_h(A/d)(1-i)=0,
f_h-a(d/A)(1+i)c_h+2iA^2/d=0.                            (6)
```

The last uses `(1+i)^2=2i`and`2/sqrt2=sqrt2`. Since xi0=1andxi2=0, the two kernels are independent, proving rankM_h(w)<=2over the COMPLEXfield. Indeed the rows0/1,columns0/1minor is2(1+i)A^2!=0, so the vectors are nonzero rank2. No determinant checker, sampled vector or missing complex phase is involved.

The quantities A,d,awere defined for the entire positive parameter domain0<s<1,t>0; no denominator in(3)–(6)vanishes on the rectangle or at its boundaries.

## 3. Exact seventh-root character average

Let Omega7={exp(2pi i k/7):k=0,...,6}. The six coefficient groups in(4)carry characters

```
0: q0diagonal vector,
1: q1vector,
2: b_h E13,
-2: c_h E31,
3: e_h E23,
-1: f_h E30.
```

These are DISTINCTmodulo7. Therefore averaging P(vecM_h(w))kills EVERYcross term between different groups. The character identity `sum_(w inOmega7)w^m=0`for nonzero mmod7is exact; it is not a seven-point approximation to an unknown positivity condition.

The retained high vectors are

```
h^(h)_j=A_h(1+i^j) inq0,
g_j=d(i+i^j) inq1,
```

and the retained low terms are precisely |b_h|^2P13,|c_h|^2P31,|e_h|^2P23,|f_h|^2P30.

Use the TWOprototype families

```
M_plus(w)=M_(h_plus)(w),
M_minus(w)=X^2 M_(h_minus)(w) X^(-2).                     (7)
```

The second is an actual local-unitary row/column transformation, so its rank remains2. It shifts every low rowindex by2. It changes its high q0vector to A_(h_minus)(1-i^j), and its high q1vector to d(i-i^j).

Consequently the TWOaverages have high blocks EXACTLYR0and R1: the q0sum is

```
[(1+s)/8]P(u+v)+[(1-s)/8]P(u-v)=F[1 s;s 1]F*,
```

where u_j=1,v_j=i^j, and the q1sum of d(i+i^j),d(i-i^j)has covariance

```
2d^2(1+i^(j-k))=tB_(j,k).
```

No higher or lower Fourier components of these high blocks are discarded.

## 4. Actual low populations: all of R3and explicit part of R2

Put kappa=3-2sqrt2=(sqrt2-1)^2, and define

```
B_h=|b_h|^2=(u-H)^2/(4h u),
C_h=|c_h|^2=kappa u h^3/(8H^2).                          (8)
```

The remaining magnitudes in(3)are

```
|e_h|^2=a^2 t^3/(4h^2)=(2-h)^2/(4t),
|f_h|^2=h^2/(4t).                                       (9)
```

Thus the unshifted plusfamily gives q3row2population z2and row3population z3; the shifted minusfamily gives row0population z0and row1population z1. ALLofR3is reproduced exactly.

In q2, the plusfamily contributes B_(h_plus)atrow1and C_(h_plus)atrow3; the minusfamily contributes C_(h_minus)atrow1and B_(h_minus)atrow3. No q2row0/2population is generated. Define

```
r0=y0, r2=y2,
r1=y1-B_(h_plus)-C_(h_minus),
r3=y3-C_(h_plus)-B_(h_minus).                            (10)
```

The exact operator identity, BEFOREany claim about the signs of these coefficients, is

```
R=(1/7)sum_(w inOmega7)[P(vecM_plus(w))+P(vecM_minus(w))]
                +sum_(j=0)^3 r_j P(j,j-2).              (11)
```

This is RITSELF, not just an objective or diagonal moment control. All high/low and low/lowoff terms have already been accounted for by the character table.

## 5. Prove every product residual nonnegative on the entire rectangle

Here r0,r2>0. Straight substitution in(8),(10)gives

```
r1=1/2-[h_plus h_minus^2/(4u)
                   +kappa u h_minus/(8h_plus^2)],
r3=1/2+s-[h_minus h_plus^2/(4u)
                   +kappa u h_plus/(8h_minus^2)].        (12)
```

These formulas are WRITTENidentities; no interpreter simplified them. On(2),

```
4/5<u<5/4,
3/2<=h_plus<=5/3,
1/3<=h_minus<=1/2,
0<kappa<1/5.                                           (13)
```

The kappa bound follows from sqrt2>7/5. For the first bracket in(12), use h_plus<2to obtain

```
h_plus h_minus^2/(4u) <5/32,
kappa u h_minus/(8h_plus^2) <1/144.
```

Their sum is less than47/288, hence

```
r1>97/288>0.                                            (14)
```

For the second bracket,

```
h_minus h_plus^2/(4u) <125/288,
kappa u h_plus/(8h_minus^2) <15/32.
```

Their sum is less than65/72. Since1/2+s>=1,

```
r3>7/72>0.                                              (15)
```

Every inequality holds uniformly on ALLof(2), not only the example. Strictbounds(13)are valid even at the original rectangle's endpoints because81/100>4/5and121/100<5/4.

## 6. Normalized decomposition and the concrete integer/332state

All fourteen phase vectors in(11)have rank2by their literal kernels; all four residual vectors are product; all coefficients are nonnegative. Therefore(11)proves SN(R/N)<=2. Unit-vector weights are

```
||M_plus/minus(w)||_F^2/(7N), and r_j/N for products.
```

They sum to1by the exact trace of(11), and are NOTasserted uniform1/14.

In particular s=1/2,t=1is inside(2). Its actual density matrix is

```
rho=[sum_q E_q Kq E_q*]/332,
K0(j,k)=12(1+i^(j-k))+6(i^j+i^(-k)),
K1(j,k)=12(1+i^(j-k)),
K2=diag(12,20,12,36), K3=diag(27,3,3,27).                 (16)
```

This previously eligible Gaussian-rational PPTtarget is now explicitly decomposed into rank-two vectors and products at the WRITTENscope above. Its real and imaginary entries are integers divided by332; the ensemble vectors and weights are algebraic, which is not a claim of real-rational density entries or rational-only pure vectors. No machine check was performed.

## 7. Scope, stronger gates, and genuine replacement requirement

This actual-state SN<=2certificate subsumes mere nondetection by the nonMEfull-diagonal witness family on the classified rectangle, but does NOTretroactively turn the earlier moment controls into operator decompositions. Their quantitative uniformstrictmargin and their original frozen quantifiers remain what they were. The 24phase wedge record remains unchanged; its earlier statement that its OWNidentity did not cover the rectangle was correct.

Any search for an unrestricted complex SR2separator on(2)is now blocked by the explicit decomposition if reconstructed; it must not continue under a different Dlabel or be sold as an attractive PPTcontrol. A replacement must genuinely escape the state/template geometry, not silently transfer this SNbound outside(2). The entire positive0<s<1,t>0family is not claimed classified, although the exact formulas(10)–(12)also certify any additional point where all r_jare nonnegative.

P44itself remains unresolved. No unrestricted4by4no-go, Schmidt3pair, machine/kernel/formal/triple-checker/cross-vendor/human/family/novelty/SOTAor scientific-execution acceptance is claimed. This is an author-WRITTENfinite identity pending fresh reconstruction. NativeN4UNKNOWN/exit-unestablished, old21unreconstructed, later overlays and originaldeadline remain unchanged. The next primary push requires a genuinely new actual PPTgeometry and BOTHuniversal complex SR2positivity and negative separation, with no scientificGO.
