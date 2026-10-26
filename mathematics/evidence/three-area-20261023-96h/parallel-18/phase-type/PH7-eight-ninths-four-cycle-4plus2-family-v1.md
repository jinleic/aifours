# PH7 at 8/9: the entire actual four-cycle R4 / equal-rate S2 family is impossible

Status: WRITTEN AUTHOR CANDIDATE, requiring a fresh complete reconstruction. Actual pre-write `/bin/date` returned `Sun Oct 25 16:18:20 PDT 2026`. Same original102319 PH primary, original cutoff/deadline and HOLD v2/v9/v10/v11. The proof core was exposed in checkpoint032 before the temporary v98 review; that review was actually RETURNED before the post-v98 resumption/exposure ACK and this body. This is not a claim that the lead first arose after that ACK or was preregistered.

All operative mathematics here is exact rational/symbolic WRITTEN algebra. No interpreter/calculator/program/CAS, enumeration, solver, replay or kernel check was used. Earlier informal approximate primary scoping has ZERO proof/certificate credit and is permanently disclosed as an OWNER written-exactness PROCESS MAJOR in `primary-resumption-after-v98-ack-v1.json`, SHA256 `7f2ac1066196b651af9d7b4fed7093b6121e51df0d6a948751442c724ddd1a5d`; it is not a premise below. Both earlier cadence findings remain permanent too.

## 1. New principal/input coupling, literal class and exact theorem

Normalize d=1. Put

`z=8/9`, `nu=2z=16/9`, `s=z^2=64/81`,

`D_z(y)=y[(y+1)^2+z]^2`, `K=D_z(c)>0`, `y=Laplace_variable+c`, c>0.

Use the ACTUAL four-state upstream block

```
A=[-1,1,0,0
    0,-1,1,0
    0,0,-1,1
    s,0,0,-1],
```

with upstream exit column b0=e4. For ANY real v>0 let

```
F=[-v,1
    0,-v],             downstream entry t0=e1.
```

In R4,o,S2 order take the complete actual raw matrix

```
G=[ A        e4       0
    r^T     -ell      e1^T
    Dback    f        F ],

beta=(C,B,1,0,0,0,0),       gamma=K e7,       B,C>=0.
```

ALL4 components of r, ALL2 components of f and ALL8 entries of Dback are arbitrary actual NONNEGATIVE real matrix entries. Ell is initially any real number. No return is omitted.

THEOREM CANDIDATE: for EVERY v>0, B,C>=0 and all fourteen such return entries, the same-matrix characteristic/numerator cannot realize K/D_z(y). Hence no actual PH7 realization exists in this ENTIRE chosen4+2 principal/input family, irrespective of the hidden quadratic's real/nonreal discriminant or the return distribution.

This is NOT a statement that all PH7 matrices, all4+2 allocations or all four-state principal blocks have this form. It does not decide the unrestricted8/9 minimum; that remains{7,8} at the retained lower/upper imports.

The change from the earlier3+3 classes is substantive. The chosen A4 has an ACTUAL directed four-cycle and characteristic(X^2-z)(X^2+z), so it can support one exact desired complex pair at the principal-block level. Its cofactor degree and the relative-degree allocation differ. No old3x3 holding/cone certificate transfers. More importantly, all feedback terms below remain JOINT: they are NOT individually assumed divisible by X^2+z, and no positive quotient/cone projection is imposed.

## 2. Actual cofactor, input polynomial and full polynomial matching

Set X=y+1, t=v-1, Z=X+t. Direct multiplication gives

```
a_R=det(yI-A)=X^4-s,
v_R=adj(yI-A)e4=(1,X,X^2,X^3)^T,

a_S=det(yI-F)=Z^2,
w_S=e1^T adj(yI-F)=(Z,1).
```

Indeed(yI-A)v_R=(0,0,0,X^4-s)^T and w_S(yI-F)=(Z^2,0). Thus the ACTUAL numerator is

`Q(X)=beta_R v_R=X^2+B X+C`.

After the stated positive forward/output raw normalization, target relative degree5 forces the fourth upstream initial coordinate to0 and the third to1: a positive fourth coordinate would give a shorter3-edge input-exit path, while the third supplies the required4-edge leading coefficient. B,C retain all remaining nonnegative upstream initial weights. This is not an additional hidden-pair prescription.

Actual single-middle elimination gives the FULL polynomial identities

```
P7=det(yI-G)
  =(y+ell)a_R a_S-a_S r^T v_R-a_R w_S f-w_S Dback v_R,

beta adj(yI-G)gamma=KQ.
```

Clearing the actual principal resolvent denominators makes these valid even at singular principal values. Equality of the original transfer KQ/P7 to K/D_z REQUIRES

`P7=D_z Q`                                             (MATCH)

as an entire polynomial identity, even through common cancellations. No principal eigenvalue is presumed to survive arbitrary feedback merely because A4 contains it.

In y coordinates Q=y^2+(B+2)y+(B+C+1). Trace in(MATCH) forces

`ell=B-2t`, `k=ell-1=B-2t-1`.

Hence the exact feedback residual is

```
R=(X+k)(X^4-s)(X+t)^2-D_z Q
 =a_S r^T v_R+a_R w_S f+w_S Dback v_R.                 (R)
```

The same actual entries determine EVERY coefficient and the initial/exit transfer.

## 3. Every one of the fourteen actual generators and every residual coefficient

The physical generator polynomials on the right of(R) are:

|Return entry|Polynomial|
|---|---|
|r1|Z^2|
|r2|Z^2 X|
|r3|Z^2 X^2|
|r4|Z^2 X^3|
|f1|(X^4-s)Z|
|f2|X^4-s|
|D11|Z|
|D12|ZX|
|D13|ZX^2|
|D14|ZX^3|
|D21|1|
|D22|X|
|D23|X^2|
|D24|X^3|

They are ACTUAL cofactor products, not independently selected path factors. In particular f1,f2 have their true negative low coefficients in X; they are not declared coefficientwise nonnegative.

Write R_j=coefficient of X^j in R. The full direct expansion is

```
R5=(1+2t)B-C-(3t^2+2t+nu),
R4=C+nu(1-B)+k t^2,
R3=nu(B-C)-2s,
R2=nu C+2s(1-B),
R1=s[B-C-2tk-t^2],
R0=s[C-k t^2].                                      (E)
```

For checking the subtraction, the baseline product has coefficients

```
X7:1, X6:k+2t=B-1, X5:t^2+2tk, X4:k t^2,
X3:-s, X2:-s(k+2t), X1:-s(2tk+t^2), X0:-s k t^2.
```

The target D_z=(X-1)(X^2+z)^2 multiplied by X^2+B X+C has coefficients

```
X7:1, X6:B-1, X5:C-B+nu, X4:-C+nu B-nu,
X3:nu C-nu B+s, X2:-nu C+sB-s,
X1:s(C-B), X0:-sC.
```

Thus all high and LOW signs in(E) are fixed by the same characteristic and numerator. Every zero-entry boundary remains allowed.

## 4. All0<v<=1/2 are immediately excluded

For every t the actual leading coefficient is

`R5=r4+f1>=0`.

But if v<=1/2, t<=-1/2 and1+2t<=0. Also

`H:=3t^2+2t+nu=3(t+1/3)^2+13/9>0`.

With B,C>=0, equation(E) therefore gives R5<0. This includes the v=1/2 endpoint; no division by1+2t occurs there.

## 5. The entire1/2<v<1 range: use the correct changed high functional

Now-1/2<t<0. In the physical generator table, r4 has X4/X5 ratio2t while f1 has ratio t; all other degree4 generators have leading coefficient1. Consequently

`T2:=R4-2tR5=r3+f2+D14-t f1>=0`.                     (HI)

This is an identity for actual entries, NOT a positivity assertion for a polynomial quotient or for all X coefficients.

Put A0=1+2t>0, H=3t^2+2t+nu>0. From R5>=0 and C>=0,

`C<=A0 B-H`, `B>=H/A0`.

Exact collection of(E) gives

`T2=A0 C-H B+4t^3+3t^2+nu A0`.

Substitute the UPPER C bound because its coefficient A0 is positive. Then

`T2<=[(t+1)^2-nu]B-2t(t+1)^2`.

Here(t+1)^2<1<nu, so substitute the LOWER B bound into its NEGATIVE coefficient. Multiplying by A0>0 leaves the exact numerator

```
[(t+1)^2-nu]H-2t(t+1)^2 A0
 =-nu(nu-1)-t^2[2nu+(t+1)^2]<0.
```

Thus T2<0, contradicting(HI). No nonnegative-feedback tuple exists anywhere in this open interval, including all input/return-zero boundaries.

## 6. For v>=1, an EXACT nonnegative relation between ALL actual generators

Let t>=0. Define SIX actual basis generators

`F1=(X^4-s)Z`, `F2=X^4-s`,

`M0=1`, `M1=X`, `M2=X^2`, `M3=X^3`.

They correspond respectively to f1,f2,D21,D22,D23,D24, so they are not fictive polynomial directions. Every other actual generator has the following exact expression:

```
D11=M1+t M0,
D12=M2+t M1,
D13=M3+t M2,
D14=F2+t M3+s M0,

r1=M2+2t M1+t^2 M0,
r2=M3+2t M2+t^2 M1,
r3=F2+2t M3+t^2 M2+s M0,
r4=F1+t F2+t^2 M3+s M1+2ts M0.                       (GEN)
```

All coefficients are nonnegative for t>=0. Together with the six basis entries, this accounts for ALL14 returns. The cone of actual residual polynomials is EXACTLY the nonnegative span of these six physical polynomials: the basis is a subset of the original generators, and(GEN) expresses the rest positively. This is direct same-matrix cofactor algebra, not a quotient-positive-cone assumption, independent feedback divisibility or a claim that raw diagonal similarity preserves PH row sums.

The six polynomials have distinct leading degrees5 through0 and leading coefficient1. Therefore the unique basis coefficients of R are

```
F1: R5,
F2: R4-tR5,
M3: R3,
M2: R2,
M1: R1+sR5=zR3,
M0: R0+sR4=zR2.                                     (COEF)
```

The last equalities use nu=2z,s=z^2 and retain the negative low coefficients of f1/f2 exactly. Thus feasibility necessarily gives

`R5>=0`, `T:=R4-tR5>=0`, `C<=B-z`, `C>=z(B-1)`.

Only the FIRST THREE of these necessary conditions are needed below; no discarded lower coefficient can repair their contradiction.

## 7. An exact global polynomial contradiction for ALL v>=1

From R5>=0, let

`C<=U:=(2t+1)B-3t^2-2t-nu`.

Direct expansion gives

`T=(t+1)(C-tB+t^2)+nu(t+1-B)`.

Since t+1=v>0, T>=0 gives

`C>=L:=tB-t^2+[nu/(t+1)](B-t-1)`.

Their upper-minus-lower difference is EXACTLY

`U-L={[(t+1)^2-nu]/(t+1)}B-2t(t+1)`.

If(t+1)^2<=nu and t>0, this is strictly negative. If t=0, nonnegativity would force B=0, which makes R5=-C-nu<0. The equality(t+1)^2=nu has t>0 and is likewise impossible WITHOUT dividing by zero.

We are left with(t+1)^2>nu. Nonnegative U-L forces

`B>=2t(t+1)^2/[(t+1)^2-nu]`.                         (BLOW)

Meanwhile L<=C<=B-z and nu=2z give

`B<=(t+1)(t^2+z)/(t^2+2z-1)`.                       (BUP)

Its denominator is strictly positive since2z-1=7/9. Comparing(BLOW)/(BUP), whose denominators are now known positive, requires

```
0<=[(t+1)^2-2z](t^2+z)
      -2t(t+1)(t^2+2z-1)
  =-t^4+(3-5z)t^2+2(1-z)t+z-2z^2.
```

At the EXACT target z=8/9, this is

```
-t^4-(13/9)t^2+(2/9)t-56/81
 =-t^4-(13/9)(t-1/13)^2-719/1053<0.                  (NEG)
```

This contradiction is uniform over ALL t>=0, all B,C and all fourteen actual returns. No finite rate cap, numerical endpoint, sample, root approximation or timeout is used. Together with§4/§5 it proves the chosen-family theorem for EVERY v>0.

## 8. Initial/exit normalization was retained, not postponed as an implementation gap

The proof contradicts the raw characteristic/numerator identity BEFORE imposing PH row sums, so the latter cannot rescue it. To state the full realization interface precisely: if a matching nonnegative tuple existed, its actual y-quadratic would be

`Q(y)=y^2+(B+2)y+(B+C+1)`.

Both coefficients are positive; both hidden roots have strictly negative real parts, real or nonreal. MATCH would therefore make M=G-cI Hurwitz for every c>0, including accidental factor coincidences. Every phase reaches raw exit7 by the designated positive forward chain. Hence

`h0=(-M)^(-1)gamma=integral_0^infinity exp(Mt)gamma dt>0`.

Then

```
Tph=diag(h0)^(-1)M diag(h0),
alpha=beta diag(h0),
omega=diag(h0)^(-1)gamma,
Tph*1=-omega,            alpha*1=beta h0=K/D_z(c)=1.
```

This preserves ALL actual Metzler/Hurwitz, initial mass, row/exit and original transfer ties. The normalizer is proved positive from actual paths, not assumed from a spectrum. The coefficient contradiction says that no such successful pair exists, not that a missing normalizer stopped an otherwise delivered witness.

For general d>0, perform the dimensionless construction with c'=c/d and set the physical generator to dTph, leaving alpha unchanged and scaling its exit by d. Its transform is H_dimensionless(s/d), exactly the original repeated-pole law at b_pole^2/d^2=8/9. This is ordinary time scaling of the LITERAL class, not a WLOG declaration about arbitrary PH7 holdings or all4+2 graphs.

## 9. Exact residual, replacement and trust boundary

No B6, upper8, old selected holding result, unreviewed time-reversal theorem, SCC candidate or path-budget theorem is needed for this NEW negative polynomial proof. The determinant/adjugate, coefficient, nonnegative-generator relations and every sign/denominator/endpoint case are supplied. Standard elementary linear-algebra/quadratic-stability/positive-resolvent facts are named only for the conditional raw-to-PH interface.

The original unrestricted PH7 feasibility at8/9 remains NOT_PROVED/minimum{7,8} at retained B6 lower source `8ba04931bb26e9fec097cb75793aa99b2e5d4d2309da94e1be9328dacb830c25` and upper8 source `e110dd1fa23bdec2f7a2498e98b3dbfe31a645496f2f94641a97e3599b7b137a`. This theorem closes only the actual4-cycle A4/equal-rate acyclic S2 mechanism, including its entire feedback/input cone and unbounded v range. Arbitrary other A4 blocks, unequal S2 holdings, actual downstream two-cycles, other initial/exit arrangements and all other allocations remain free.

A replacement must CHANGE the actual principal/input coupling, not redistribute these14 returns. For example an actual downstream backward edge changes a_S from Z^2 to Z^2-l and changes the r generators themselves; the exact relations(GEN) cannot simply be imported to it, especially when l>t^2. No claim of success or rejection for that changed block is made here.

This single body is a parkable incremental theorem candidate, not a terminal park or round completion. Fresh full-source reconstruction/parent support is still required. No numerical/program/kernel/formal, human/configured-family, executable, novelty or priority acceptance is claimed. All pinned sources and parent wording overlays remain unchanged; the two cadence MAJORS and later written-exactness MAJOR stay permanent. Exact operative proof algebra here does not wash out approximate scoping history or confer scientific GO. The primary continues at the original full irreducible/path-positive gap and unchanged deadline.
