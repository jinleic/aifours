# PH7 at 8/9: the full unequal downstream triangle with arbitrary upstream input/exits

Status: WRITTEN AUTHOR CANDIDATE. Pre-write metadata clock: `/bin/date` returned `Sun Oct 25 11:55:11 PDT 2026`. Same frozen primary authority `primary-continuation-20261025-102319-v1.json`; HOLD v2 and parent errata v9/v10/v11 remain binding. No scientific interpreter, symbolic program, enumeration, solver, executable replay or kernel check was used. Every new identity, derivative and rational inequality below is a written derivation.

This complete successor REMOVES the artificial P<=1/40 restriction from v1. The475-LF v1, SHA256 `0acda5ff21b6e530c8a2552bd90bd233b21f586447d5266ba6636481645f0659`, remains unchanged as a weaker author candidate. Neither v1 nor the earlier361-LF single-exit q in[1,2] manuscript is a correctness premise. All shared matrix/input identities and the replacement scalar proof are supplied here. No older verdict is transferred to this larger scope.

## 1. Exact theorem and named import boundary

Normalize d=1 and set

`D(y)=y[(y+1)^2+8/9]^2`, `K=D(c)>0`, `H(s)=K/D(s+c)`, c>0.

Let A be ANY real3x3 Metzler matrix with diagonal(-1,-1,-2), all six off-diagonal entries arbitrary nonnegative real numbers, including zeros. There is NO designated positive upstream path. Let b0 be ANY nonnegative3-column of actual upstream exits to the middle phase and beta_R ANY nonnegative3-row of actual initial weights. In particular there may be MULTIPLE upstream exits.

Choose arbitrary delta,epsilon>=0 with delta+epsilon<=2. Define

`theta=1+delta+epsilon in[1,3]`, `P=delta*epsilon`.

The actual matrices and boundaries are

```
F=[-1,1,0
    u,-(1+delta),1
    w,v,-(1+epsilon)],                 u,v,w>=0,

G=[ A        b0       0
    r^T     -ell      e1^T
    Dback    f        F ],

beta=(beta_R,0,0,0,0),                gamma=K e7.
```

Every entry of r,f,Dback is an arbitrary actual nonnegative matrix entry. Ell is initially any real number. The downstream positive3-path and sole final exit are retained, with no omitted backward or cross-feedback.

THEOREM CANDIDATE at B6: no such tuple has G-cI Hurwitz and beta(sI-(G-cI))^(-1)gamma=H(s). Hence no actual PH7 exists anywhere in this entire unequal-holding triangle and arbitrary-upstream-input/exit class.

The sole substantive mathematical import is the LOWER part of B6: all actual PH representations of order at most6 are excluded at z=b_pole^2/d^2=8/9>1/2. Source: `proof-unrestricted-six-state-barrier-v1.md`, SHA256 `8ba04931bb26e9fec097cb75793aa99b2e5d4d2309da94e1be9328dacb830c25`, complete195-LF body read. This is a retained WRITTEN import, not newly executed, newly formally verified or newly priority-cleared here. The operative parent qualification is section2, LF43-72, of `institute/runs/three-area-2026-10-23-96h/priority-written-dispositions-v1.md`, snapshot SHA256 `faf0335d8569a39c2fce54f09f4e8e1474021b60cf176bd16888e1a266048787`; only that section is invoked, not a whole-document coverage claim or its historically withdrawn exact clocks.

For background ONLY, the retained pointwise PH8 ceiling is `proof-eight-state-cubic-cancellation-v1.md`, SHA256 `e110dd1fa23bdec2f7a2498e98b3dbfe31a645496f2f94641a97e3599b7b137a`. It is not a proof input to this restricted exclusion and is not reconstructed anew here. At those retained lower/upper imports the unrestricted minimum remains{7,8}: this theorem does not choose it.

## 2. The exact old properties which do not transfer

Multiple upstream exits change the leading cofactor vector from e3 to b0. The old R5=r3+f1 identity and the old scalar numerator Cbar-a therefore do NOT transfer. Both the leading input coefficient and its constant must come from the same actual beta_R,b0,A.

Two nonunit downstream holdings add P X to the actual downstream determinant. The effective return Ueff=u+v-P, and its total mu below, can be NEGATIVE. The old nonnegative-mass deletion is not valid. For theta>2 even the old U-term sign is reversed. The proof replaces precisely these failures with a positive MATRIX adjugate cone, a physical/Perron ell>0 lemma, and a signed-mass estimate using the actual identity P=delta*epsilon. It is neither feedback redistribution in the closed class nor a trace-only rejection.

The physical product is not a freely chosen polynomial parameter:

`0<=P<=((theta-1)^2)/4<=1`,                             (PROD)

by(delta-epsilon)^2>=0. No additional small-product cap is imposed.

## 3. Complete upstream adjugate cone for arbitrary topology and exit column

Put X=y+1 and J=A+I, so diag J=(0,0,-1). Define

```
Abar=J12*J21+J13*J31+J23*J32>=0,
G0=J12*J21+J12*J23*J31+J13*J32*J21>=0.
```

Direct determinant expansion gives

`a_R=det(yI-A)=X^3+X^2-Abar X-G0`.

Both J+I and J^2+J are entrywise nonnegative. For the latter statement, its ith diagonal is sum_(j!=i)Jij Jji because Jii^2+Jii=0. For i!=j its entry is

`(1+Jii+Jjj)Jij+sum_(k!=i,j)Jik Jkj`.

The first coefficient is1 for{1,2} and0 for a pair containing3. This proves positivity for every upstream off-diagonal topology, not just a selected pair of forward edges.

Set

```
c0=(J+I)b0>=0,
e0=(J^2+J)b0>=0,
d0=e0-Abar b0.
```

The ACTUAL adjugate column is

`v_R=adj(yI-A)b0=X^2 b0+X c0+d0`.                       (AR)

Indeed its full adjugate is X^2 I+X(J+I)+J^2+J-Abar I. Multiplication by XI-J gives a_R I using the directly expanded characteristic identity J^3+J^2-Abar J-G0 I=0. The vector d0 may have negative entries; no positivity of it is assumed.

## 4. Actual downstream cofactor, numerator and FULL characteristic equality

Write

```
sigma=delta+epsilon=theta-1,
U=u+v>=0,
Ueff=U-P,
Z=w+epsilon*u>=0,
mu=Abar+Ueff,
V=G0+Z>=0.
```

The signs which actually hold are

`mu>=-P`, `-P<=Ueff<=mu`, `Abar,G0,Z>=0`.                (B)

In particular mu,Ueff are NOT assumed nonnegative.

Direct downstream determinants/adjugates give

```
a_S=X^3+sigma X^2-Ueff X-Z,
w_S=e1^T adj(yI-F)=(X^2+sigma X+P-v, X+epsilon,1).
```

Multiplying that row by `[[X,-1,0],[-u,X+delta,-1],[-w,-v,X+epsilon]]` gives(a_S,0,0), so epsilon*u in Z is tied to the same matrix entries.

Clearing the actual two principal resolvents and the remaining scalar middle equation gives the polynomial identities

```
P7=det(yI-G)
  =(y+ell)a_R a_S-a_S r^T v_R-a_R w_S f-w_S Dback v_R,

beta adj(yI-G)gamma=KQ,        Q=beta_R v_R.
```

They extend to singular principal values by polynomial clearing. Thus equality of the transfer KQ/P7 with K/D forces

`P7=DQ`,                                               (T)

as a FULL polynomial identity, even under coincident or cancelled factors. Degree and leading coefficient force Q monic of degree2 and hence beta_R b0=1. Put

`p-2=beta_R c0>=0`, `Cstar=beta_R e0>=0`.

The actual numerator is exactly

`Q=X^2+(p-2)X+Cstar-Abar`.

Its y-coordinate constant is p-1+Cstar-Abar. It is not fixed beforehand; both real/nonreal hidden pairs are allowed. These quantities retain their shared beta_R,b0,A dependence, not independent realizability.

Trace in(T) forces

`ell=p-theta-2`, `k=ell-1=p-theta-3`.

The entire actual feedback residual is therefore

```
R=(X+k)a_R a_S-DQ
 =a_S r^T v_R+a_R w_S f+w_S Dback v_R.                  (R)
```

Every lower coefficient remains in this equality. No separately chosen spectrum substitutes for the same-matrix input ties.

## 5. Load-bearing actual PH normalization and ell>0

Assume a successful Hurwitz raw candidate M0=G-cI. Then

`h0=(-M0)^(-1)gamma=integral_0^infinity exp(M0 t)gamma dt>=0`.

If I is the set of its positive coordinates, a zero coordinate in M0 h0=-gamma forces gamma_i=0 and M0_ij=0 for j in I, by nonnegative off-diagonal entries. Such zero-h states cannot return to I or contribute to output. Restriction to I preserves the transfer. Its principal Metzler block is Hurwitz, and

```
Tph=diag(h0_I)^(-1)M0_II diag(h0_I),
alpha=beta_I diag(h0_I),
omega=diag(h0_I)^(-1)gamma_I,
Tph*1=-omega,        alpha*1=beta h0=H(0)=1.
```

This is the actual PH initial/exit normalization, not merely a spectrum. If any state were removed, B6 would forbid the resulting order at most6. Hence h0>0 on all7 states. Likewise all7 states are initial-reachable: otherwise their outgoing-closed reachable PH subsystem realizes the law in at most6 states, again contrary to B6. All states are exit-co-reachable from h0>0 and proper PH transience.

The target density has exact asymptotic

`f(t)=[K/(1+8/9)^2]exp(-ct)+O(t exp(-(c+1)t))`.

A dominant initial-reachable/exit-co-reachable irreducible block cannot have Perron eigenvalue lambda>-c. Fix any positive pre/post time tau. The restrictions of alpha exp(Tph tau) and exp(Tph tau)omega are strictly positive on that block. Confine the middle paths to it and dominate its positive Perron right vector: f(t+2tau) is at least a positive multiple of exp(lambda t), contradicting the exact asymptotic. Conversely -c is an actual pole and therefore an eigenvalue. Thus shifted G has spectral abscissa0, without an assumption that every mode is observable.

A Metzler diagonal is at most its spectral abscissa, by a nonnegative shift and principal-submatrix monotonicity. Consequently ell>=0. If ell=0, every upstream state can reach the middle phase, because all routes from its block to the sole output first pass through b0 into the middle. A nonzero r_j then creates a positive cycle through the middle. A nonzero f_i does so using the downstream path; a nonzero Dback_ij does so using that path and an upstream route back. Choosing shortest routes gives a simple cycle.

On that cycle the middle diagonal is0 and every other diagonal is strictly negative. The matrix retaining only the cycle has characteristic

`lambda product_j(lambda+d_j)-product_of_cycle_edges`, d_j>0.

Its value at0 is negative and its leading term tends to positive infinity, so it has a positive real eigenvalue. Metzler monotonicity forces a positive spectral abscissa for G, a contradiction. Hence ell=0 would require r=f=Dback=0.

Then G is block upper triangular with blocks A,0,F. Its FOUR visible nonreal roots -1±i sqrt(8/9), each of multiplicity2, must distribute one pair into each real3x3 block. A block cannot hold all four. The third eigenvalue of either block is its real Perron root -a with0<=a<=1, since its spectral abscissa is at most0 and at least -1. But

`tr(B^2)=a^2+2(1-8/9)>=sum_i Bii^2>=(a+2)^2/3`

for such a Metzler block B. The first inequality uses nonnegative opposite-edge products and the second is Cauchy. It gives(a-1)^2>=8/3, impossible for0<=a<=1. Thus

`ell>0`.                                              (PH)

This physical/Perron gate is essential. No assertion about arbitrary unstable polynomial matching systems follows from it.

## 6. ALL actual feedback generators and a positive functional for signed mu

Let Rj=[X^j]R. In this table j ranges over all three upstream coordinates, so the table covers3 r entries,3 f entries and ALL9 Dback entries.

|Actual coefficient|([X5],[X4],[X3])|
|---|---|
|r_j|(b0_j,c0_j+sigma b0_j,d0_j+sigma c0_j-Ueff b0_j)|
|f1|(1,theta,sigma+P-v-Abar)|
|f2|(0,1,1+epsilon)|
|f3|(0,0,1)|
|Dback_1j|(0,b0_j,c0_j+sigma b0_j)|
|Dback_2j|(0,0,b0_j)|
|Dback_3j|(0,0,0)|

Every entry follows by multiplying the actual a_R,a_S,v_R,w_S. A zero high triple does not remove its lower coefficients from(R). Hence

```
R5=r^T b0+f1>=0,

T4:=R4-sigma R5=r^T c0+f1+f2+(Dback b0)_1>=0,

S:=R3+mu R5
 =r^T(e0+sigma c0)+(sigma+u)f1+(1+epsilon)f2+f3
   +(Dback c0)_1+sigma(Dback b0)_1+(Dback b0)_2>=0.       (CONE)
```

The cancellation d0+Abar b0=e0 and Ueff=u+v-P proves the last sign EVEN IF mu<0. Both unequal holdings, all multiple upstream exits, the actual1+epsilon coefficient of f2, and every cross-feedback entry have been retained.

## 7. Exact coefficient identities, with no sign assigned to effective returns

Put

`nu=16/9`, `rho=64/81`, `chi=34/9`, `K0=mu+nu`, `L=theta+1`.

K0>=nu-P>=7/9>0 by(PROD); it is not K=D(c). The complete principal product is

```
a_R a_S=X6+theta X5+(sigma-mu)X4
 -(G0+Ueff+Z+sigma Abar)X3
 +(Abar Ueff-Z-sigma G0)X2
 +(Abar Z+G0 Ueff)X+G0 Z.
```

The target DQ has X7 through X3 coefficients

`1, p-3, Cstar-Abar-p+chi, nu(p-3)-Cstar+Abar,`

`nu(Cstar-Abar-p+2)+rho`.

Subtracting gives the exact identities

```
R5=L p-L^2-chi-Ueff-Cstar,
T4=theta Cstar-[K0+theta(theta-1)]p
      +3mu+2(theta-1)Ueff-V+F(theta),
F(theta)=nu(theta+2)+theta^3-theta,                     (E1)

S=[nu+2mu+(theta-2)Ueff-V]p-K0 Cstar
  +Abar Ueff-mu^2+K0 Abar-(nu+6)mu
  +(6-theta-theta^2)Ueff+4G0+(theta+2)Z-(2nu+rho).       (E2)
```

Compare the upper Cstar bound from R5>=0 and the lower one from T4>=0. Exact collection yields

```
H0*(p-theta-2)>=theta*nu+(theta-1)Abar+Ueff+V,
H0=2theta-nu-mu.                                      (H)
```

At p=theta+2 the upper-minus-lower expression is the negative of that right side. It is at least theta*nu-P>0: indeed P<=(theta-1)^2/4<=1 while theta>=1 and nu>1. By(PH) its multiplier p-theta-2=ell is positive, so H0>0. Since H0<=2theta-nu+P,

`p>=theta+2+(theta*nu-P)/(2theta-nu+P)`.                (PB)

The denominator is positive for theta>=1. Both forthcoming bounds use the PH holding gate and the ACTUAL product constraint, not a free choice of p.

## 8. New piecewise p lower bound on the WHOLE unequal triangle

First, subtract21/4 from(PB) and multiply by the positive denominator. The numerator is

`2theta^2-(13/2)theta+52/9+(theta-17/4)P`.

Its P coefficient is negative on[1,3]. Use(PROD) to bound it below by

```
[36theta^3+63theta^2-594theta+679]/144
 ={(theta-11/6)^2(36theta+195)+283/12}/144>0.
```

Thus p>21/4 throughout the WHOLE triangle, without P<=1/40.

Second, ell>3/4 follows from(PB), because the numerator after comparing its fraction with3/4 is at least

`[-63theta^2+166theta+129]/144`.

The bracket is concave in theta and its endpoint values at1 and3 are232 and60, so this is at least60/144>0. Hence p>theta+11/4 as well.

We may therefore use the continuous piecewise lower bound

```
p>pstar(theta),
pstar=21/4                 for1<=theta<=5/2,
pstar=theta+11/4           for5/2<=theta<=3.            (PSTAR)
```

These are derived lower bounds, not independent hidden coefficients. The two expressions agree at theta=5/2.

## 9. Correct lower-input substitution and coupled negative p coefficient

T4>=0 gives

`Cstar>={[K0+theta(theta-1)]p-3mu-2(theta-1)Ueff+V-F(theta)}/theta`.

The Cstar coefficient in(E2) is-K0<0, so substituting this LOWER bound gives an UPPER bound. Exact collection is

```
S<=-D0*p+Abar Ueff+(3/theta)mu^2+A1 mu+A0
 +(2-theta)[theta+3-K0/theta-p]Ueff
 +[4-K0/theta-p]G0+[theta+2-K0/theta-p]Z,               (S1)

D0=K0^2/theta-(3-theta)mu-(2-theta)nu,
A1=theta^2-7+nu+5nu/theta,
A0=nu*theta^2-80/27+512/(81theta).
```

For reconstruction, the non-p mu^2 coefficient is-1+(theta+3)/theta=3/theta. Its mu coefficient before simplification is-6+3nu/theta+nu+2nu/theta+theta^2-1. The constant is nu^2(1+2/theta)+nu(theta^2-1)-(2nu+rho). The Ueff factor uses6-theta-theta^2=(2-theta)(theta+3). No sign of mu or Ueff was used.

By(PH),(PSTAR),K0>0 and G0,Z>=0, the last TWO bracket terms are nonpositive and may be dropped. The Ueff term must instead be retained in the p coefficient. Put

`Deff=D0-(theta-2)Ueff`.

For2<=theta<=3, Ueff<=mu gives

```
theta Deff>=theta[D0-(theta-2)mu]
 =[mu+(2nu-theta)/2]^2+theta(55theta-64)/36>0.           (DHI)
```

This identity holds for EVERY real mu, not only positive mu.

For1<=theta<=2, use Ueff>=-P and P<=1/4. Write

```
theta D0=mu^2+B(theta)mu+nu[(theta-1)^2+7/9],
B(theta)=(theta-3/2)^2+47/36.
```

This polynomial increases for mu>=-P: its derivative is at least47/36-2P>=29/36>0. Evaluating at-P gives

```
theta Deff>=P^2-(2nu-theta)P+nu[(theta-1)^2+7/9]
             >=112/81-23/36=241/324>0.                (DLO)
```

Thus Deff>0 on the entire triangle. Only NOW replace p by pstar in the combined negative term. We obtain

```
S<=-pstar D0+Abar Ueff+(3/theta)mu^2+A1 mu+A0
                 +(theta-2)L_U Ueff,
L_U=pstar+K0/theta-theta-3.                            (S2)
```

L_U is strictly positive. For theta<=5/2, (PROD) bounds it below by

`11/4-5theta/4+55/(36theta)>=17/72>0`.

For theta>=5/2 its lower bound is

`1/4-theta/4+55/(36theta)>=1/108>0`.

Both displayed functions decrease on their intervals, so their right-endpoint values prove the bounds. Finally the real identity(Abar-Ueff)^2>=0 gives

`Abar Ueff<=mu^2/4`,                                  (AU)

with NO positivity assumption on Ueff.

## 10. First entire interval: 1<=theta<=2

Here(theta-2)L_U<=0 and Ueff>=-P, so its contribution in(S2) is at most(2-theta)L_U P. Use(AU). The upper bound becomes

`S<=C2 mu^2+Bint mu+Cint`,                            (LOW)

where

```
C2=1/4-9/(4theta)<=-7/8,
Bint=B0(theta)+(2-theta)P/theta,
B0=theta^2-(21/4)theta+379/36-88/(9theta),
Cint=Cbase(theta)+(2-theta)[21/4+nu/theta-theta-3]P,
Cbase=[144theta^3-756theta^2+1272theta-832]/(81theta).
```

Bint<0 uniformly, since

```
36theta Bint=-62+(theta-2)(36theta^2-117theta+145)
                      +36(2-theta)P,
36theta^2-117theta+145=36(theta-13/8)^2+799/16>0.
```

The right side is at most-62+36P<=-53<0.

Negative mu cannot be ignored. Let t=theta-1 in[0,1]. B0 is concave on[1,2] because B0''=2-176/(9theta^3)<0, and its endpoint values are-7/2 and-31/36. Thus

`Bint>=B0>=-7/2+(95/36)t`.

For-P<=mu<0 this implies

```
Bint mu<=(-Bint)P
       <=(7/8)t^2-(95/144)t^3
       <=2058/9025<1/4.                              (LINLOW)
```

The cubic maximum is obtained by differentiating: its derivative is t(84-95t)/48, so the maximum occurs at t=84/95; direct substitution gives2058/9025. This is an exact written interval inequality, not a finite sample or interpreter calculation.

For the constant, its unperturbed numerator is

```
144theta^3-756theta^2+1272theta-832
 =-172+192t-324t^2+144t^3
 <=-172+192t-180t^2
 =-180(t-8/15)^2-604/5.
```

Since81theta<=162, Cbase<=-302/405. The perturbation in Cint is at most

`(109/36)*(1/27)=109/972`:

the first factor bounds21/4+nu/theta-theta-3, while(2-theta)P<=(1-t)t^2/4<=1/27. Hence

`Cint<=-302/405+109/972=-3079/4860<-3/5`.

If mu>=0 the nonconstant terms in(LOW) are nonpositive. If mu<0 the quadratic remains nonpositive and(LINLOW) bounds the linear term by less than1/4. Therefore throughout this entire interval

`S<-7/20<0`,                                         (LOWNEG)

contradicting(CONE).

## 11. Middle entire interval: 2<=theta<=5/2

Now(theta-2)L_U>=0 and Ueff<=mu, so its contribution is at most(theta-2)L_U mu. Use(AU) with pstar=21/4. Exact collection gives

```
S<=C2 mu^2+Bmid mu+Cbase,
C2=5/4-17/(4theta)<=-9/20,
Bmid=-theta+281/36-40/(3theta),                       (MID)
```

where Cbase is the same function as in§10. Bmid increases because-1+40/(3theta^2)>0. Its endpoint values give

`-31/36<=Bmid<=-1/36<0`.

For t=theta-2 in[0,1/2], the constant numerator is

```
144theta^3-756theta^2+1272theta-832
 =-160-24t+108t^2+144t^3
 <=-160+66t<=-127,
```

using t^2<=t/2 and t^3<=t/4. Since81theta<=405/2,

`Cbase<=-254/405<-3/5`.

If mu>=0 both nonconstant terms in(MID) are nonpositive. If-P<=mu<0, their quadratic part is still nonpositive and

`Bmid mu<=31P/36<=31/64`,

because P<=(theta-1)^2/4<=9/16. Thus in the entire middle interval

`S<-3/5+31/64=-37/320<0`,                             (MIDNEG)

again contradicting the SAME actual cone.

## 12. Last entire interval: 5/2<=theta<=3

Use Ueff<=mu and(AU) as in§11, but now pstar=theta+11/4. The exact quadratic collection is

```
S<=C2 mu^2+Bhi mu+Chi,
C2=1/4-7/(4theta)<=-1/3,
Bhi=7/4-40/(9theta),
Chi=-4theta/3+296/81-64/(27theta).                     (HIGH)
```

Bhi increases from-1/36 to29/108. Chi decreases on this interval because-4/3+64/(27theta^2)<0, and at theta=5/2 it equals-254/405. Hence Chi<-3/5 everywhere here.

If mu>=0, the nonconstant terms in(HIGH) are at most

`-(1/3)mu^2+(29/108)mu<=841/15552<1/10`.

If-P<=mu<0, the quadratic is nonpositive and Bhi mu<=P/36<=1/36<1/10, using(PROD). In either case,

`S<-1/2<0`,                                          (HIGHNEG)

contradicting(CONE).

## 13. Exact coverage, assurance and the ORIGINAL remaining gap

The three intervals cover EVERY theta in[1,3] and EVERY actual pair delta,epsilon>=0 with their sum at most2. The entire product range P<=((theta-1)^2)/4 was used, including P=1 at delta=epsilon=1. Thus v1's small-product cap has genuinely disappeared. All input-zero, internal-edge-zero and feedback-zero boundaries are retained; negative mu,Ueff are explicitly handled. The upstream input/exit coupling is arbitrary, not a hidden single-exit or positive-upstream-path ansatz.

This is a uniform same-matrix characteristic AND numerator obstruction, not a trace-screen rejection. Every actual r,f,Dback appears in the full determinant identity and complete high-generator table, and the actual beta_R adj(yI-A)b0 supplied the numerator. The trace/Cauchy argument has only the load-bearing PH purpose of ruling out ell=0; it is not substituted for the actual coefficient proof.

The raw-to-PH normalization retains Hurwitzness, nonnegative initial/exit law, all row sums and initial mass1. Conversely actual PH matrices represented by the literal raw coordinates lie within the theorem. Positive raw coordinate normalization of designated downstream edges is not claimed to preserve physical row sums by itself; those are restored by the explicit h0 normalization. For general d>0, change time unit by d and replace c by c/d. The theorem concerns precisely the corresponding dimensionless shifted holding ratios, NOT arbitrary holdings declared WLOG.

No actual PH7 realization at8/9 is supplied and no ALL-TOPOLOGY empty-intersection certificate is established. Still unresolved are other upstream holding multisets, a first downstream shifted holding different from1, delta+epsilon>2, other center/input/output placements, a missing downstream designated path and other dominator allocations. Multiple upstream exits and absence of an upstream designated path are now covered ONLY in the literal new holding class, not globally eliminated. The unrestricted minimum remains{7,8} at the retained B6/upper8 imports. No full existence-band endpoint, full minimum-order function or original book problem is decided.

This source needs a FRESH COMPLETE written reconstruction with the named B6 import disclosed. No review of the old361-LF or475-LF candidates accepts this full triangle automatically. The new body is complete at its stated import boundary; old author candidates are historical leads, not silently accepted inputs. Written/source-pinned acceptance, if later obtained, is not formal proof, Lean-kernel verification, human/configured-family review, executable acceptance, novelty or priority clearance. Earlier unadmitted arithmetic outputs remain preserved and additively qualified; none supplies verification credit here.
