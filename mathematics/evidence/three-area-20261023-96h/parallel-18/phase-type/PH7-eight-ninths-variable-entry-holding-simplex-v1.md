# PH7 at 8/9: variable first downstream holding, signed cubic budget and a whole holding simplex

Status: WRITTEN AUTHOR CANDIDATE, not fresh independent/parent acceptance. Pre-write metadata clock: `/bin/date` returned `Sun Oct 25 12:13:18 PDT 2026`. Same frozen102319 primary authority; HOLD v2 and parent errata v9/v10/v11 remain binding. No scientific interpreter, symbolic program, enumeration, solver, executable replay or kernel check was used. Every new polynomial identity, derivative and rational inequality here is a written derivation.

The498-LF first-downstream-holding1 predecessor, `PH7-eight-ninths-multiple-exit-unequal-triple-cone-v2.md`, SHA256 `d69a835e49896629eee196bb59e853eee277455bd3be95e3caf9185fe1919089`, is preserved unchanged and remains an author candidate. It is NOT a correctness input. This single consolidated manuscript supplies the complete new matrix, numerator, cone, normalization and signed-constant proof; no predecessor verdict is silently widened.

## 1. Literal class, theorem and named import

Normalize d=1. Define

`D(y)=y[(y+1)^2+8/9]^2`, `K=D(c)>0`, `H(s)=K/D(s+c)`, c>0.

A is ANY real3x3 Metzler matrix with diagonal(-1,-1,-2). All six off-diagonal entries are arbitrary nonnegative real numbers, including zeros. There is NO designated positive upstream path. The actual initial row beta_R and actual upstream exit column b0 are arbitrary nonnegative3-vectors: MULTIPLE upstream exits are allowed.

Choose kappa,delta,epsilon>=0 with

`kappa<=1`, `s0=kappa+delta+epsilon<=2`, `theta=1+s0 in[1,3]`.

The actual downstream matrix, complete raw matrix and boundaries are

```
F=[-(1+kappa),1,0
    u,-(1+delta),1
    w,v,-(1+epsilon)],                 u,v,w>=0,

G=[ A        b0       0
    r^T     -ell      e1^T
    Dback    f        F ],

beta=(beta_R,0,0,0,0),                gamma=K e7.
```

All3 components of r, all3 components of f and ALL9 entries of Dback are arbitrary actual nonnegative matrix entries. Ell is initially any real number. The downstream positive3-path and sole final exit are retained, with no backward/cross-feedback suppressed.

THEOREM CANDIDATE at B6: no tuple in this entire selected holding simplex has G-cI Hurwitz and beta(sI-(G-cI))^(-1)gamma=H(s). Therefore no actual PH7 exists in this class, including variable FIRST downstream holding, arbitrary/asymmetric remaining downstream holdings, multiple upstream exits, arbitrary upstream input and arbitrary upstream off-diagonal topology.

The sole substantive mathematical import is B6 LOWER EXCLUSION: every actual PH representation of order at most6 is impossible at z=b_pole^2/d^2=8/9>1/2. Source `proof-unrestricted-six-state-barrier-v1.md`, SHA256 `8ba04931bb26e9fec097cb75793aa99b2e5d4d2309da94e1be9328dacb830c25`, complete195-LF body read. This is a retained WRITTEN import, not newly executed, formally verified or priority-cleared here. Its operative parent qualification is section2, LF43-72, of `institute/runs/three-area-2026-10-23-96h/priority-written-dispositions-v1.md`, snapshot SHA256 `faf0335d8569a39c2fce54f09f4e8e1474021b60cf176bd16888e1a266048787`; only that section is invoked, not whole-document coverage or a historically withdrawn exact clock.

Background only: retained upper8 at this point is `proof-eight-state-cubic-cancellation-v1.md`, SHA256 `e110dd1fa23bdec2f7a2498e98b3dbfe31a645496f2f94641a97e3599b7b137a`. It is not a proof input here or newly reconstructed. The unrestricted minimum is STILL{7,8} at those retained lower/upper imports. This literal class is NOT asserted WLOG for arbitrary PH7 matrices.

## 2. The property that FAILS before this new coupling is attempted

Changing the first downstream holding from1 to1+kappa changes the actual cubic constant. Put

```
P2=kappa*delta+kappa*epsilon+delta*epsilon,
P3=kappa*delta*epsilon.
```

The effective downstream constant is now

`Zeff=epsilon*u+kappa*v+w-P3`,

which may be NEGATIVE. Consequently the old deletion of a negative Z bracket using Z>=0 is invalid. The old nonnegative effective return mass also fails because Ueff=u+v-P2 can be negative. These failures were recorded before this proof in checkpoint021/022; no feedback redistribution inside the first-holding1 cone is being presented as a new witness.

The replacement explicitly budgets the negative cubic constant P3 and couples it to the p coefficient before using any lower bound. The kappa<=1 restriction is also honest: it is exactly what keeps the ACTUAL f1 coefficients in the new high-generator cone nonnegative. It is not a sorting or WLOG assumption about the entry phase.

The physical symmetric-product bounds are

`0<=P2<=s0^2/3<=4/3`, `0<=P3<=s0^3/27<=8/27`.          (PROD)

The first follows from the sum of three squared differences; the second is AM-GM for the three actual nonnegative shifts. Neither P2 nor P3 is an independently selected polynomial parameter.

## 3. Upstream matrix adjugate cone with arbitrary input/exit coupling

Put X=y+1 and J=A+I, so diag J=(0,0,-1). Direct determinant expansion gives

```
Abar=J12*J21+J13*J31+J23*J32>=0,
G0=J12*J21+J12*J23*J31+J13*J32*J21>=0,
a_R=det(yI-A)=X^3+X^2-Abar X-G0.
```

Both J+I and J^2+J are entrywise nonnegative. For the latter statement the ith diagonal is sum_(j!=i)Jij Jji, since Jii^2+Jii=0. An off-diagonal entry is

`(1+Jii+Jjj)Jij+sum_(k!=i,j)Jik Jkj`.

The first coefficient is1 for{1,2} and0 for a pair containing3. This proves positivity for EVERY upstream off-diagonal topology, not just a selected forward path.

Define

```
c0=(J+I)b0>=0,
e0=(J^2+J)b0>=0,
d0=e0-Abar b0.
```

The actual adjugate column is

`v_R=adj(yI-A)b0=X^2 b0+X c0+d0`.                       (AR)

Indeed its full adjugate is X^2 I+X(J+I)+J^2+J-Abar I; multiplication by XI-J gives a_R I using the directly expanded characteristic identity J^3+J^2-Abar J-G0 I=0. No positivity of d0 is assumed. The leading column is b0, not e3, so the old single-exit cofactor/initial parameterization cannot be substituted.

## 4. Actual downstream cofactor and full same-matrix transfer equality

Set

```
Ueff=u+v-P2,
Zeff=epsilon*u+kappa*v+w-P3,
mu=Abar+Ueff,
V=G0+Zeff.
```

The actual bounds are

`mu>=-P2`, `-P2<=Ueff<=mu`, `Zeff>=-P3`, `G0,Abar>=0`.   (B)

Neither mu,Ueff,Zeff nor V is assumed nonnegative.

Direct expansion gives

```
a_S=det(yI-F)=X^3+s0 X^2-Ueff X-Zeff,
w_S=e1^T adj(yI-F)=(X^2+(delta+epsilon)X+delta*epsilon-v,
                    X+epsilon,1).
```

Multiplication by `[[X+kappa,-1,0],[-u,X+delta,-1],[-w,-v,X+epsilon]]` gives(a_S,0,0). Its first component has constant kappa*delta*epsilon-epsilon*u-kappa*v-w, explaining the signed Zeff from the SAME actual entries.

Solving the two principal resolvents and the remaining scalar middle equation, then clearing denominators, gives the polynomial identities

```
P7=det(yI-G)
  =(y+ell)a_R a_S-a_S r^T v_R-a_R w_S f-w_S Dback v_R,
beta adj(yI-G)gamma=KQ,             Q=beta_R v_R.
```

Polynomial clearing makes these valid even at singular principal values. The transfer is KQ/P7, so matching H requires the ENTIRE polynomial identity

`P7=DQ`,                                               (T)

even for coincident/cancelled factors. Degrees and leading coefficients force Q monic of degree2 and beta_R b0=1. Therefore, putting

`p-2=beta_R c0>=0`, `Cstar=beta_R e0>=0`,

the ACTUAL numerator is

`Q=X^2+(p-2)X+Cstar-Abar`.

Its y-coordinate constant is p-1+Cstar-Abar, not an independently fixed hidden constant. Both real and nonreal hidden pairs are retained, as are all actual beta_R,b0,A dependencies.

Trace in(T) forces

`ell=p-theta-2`, `k=ell-1=p-theta-3`.

The full actual feedback residual is thus

```
R=(X+k)a_R a_S-DQ
 =a_S r^T v_R+a_R w_S f+w_S Dback v_R.                  (R)
```

Every lower coefficient remains part of this equality; no separately selected spectrum replaces the actual numerator.

## 5. Actual PH normalization, reachability and the strict ell>0 gate

Assume a successful Hurwitz raw realization M0=G-cI. Then

`h0=(-M0)^(-1)gamma=integral_0^infinity exp(M0 t)gamma dt>=0`.

Let I be its positive-coordinate set. A zero coordinate in M0 h0=-gamma forces gamma_i=0 and M0_ij=0 for j in I, by nonnegative off-diagonal entries. Zero-h phases cannot return to I or contribute to output; restriction to I preserves the transfer. Its principal Metzler block is Hurwitz. Positive scaling gives the ACTUAL PH law

```
Tph=diag(h0_I)^(-1)M0_II diag(h0_I),
alpha=beta_I diag(h0_I),
omega=diag(h0_I)^(-1)gamma_I,
Tph*1=-omega,       alpha*1=beta h0=H(0)=1.
```

Any removed phase would give order at most6, forbidden by B6. Hence h0>0 on all7 states. Likewise every state is initial-reachable: otherwise its outgoing-closed reachable PH subsystem realizes the same law in at most6 phases. Every state is exit-co-reachable from h0>0 and proper PH transience.

The exact target density asymptotic is

`f(t)=[K/(1+8/9)^2]exp(-ct)+O(t exp(-(c+1)t))`.

A dominant initial-reachable/exit-co-reachable irreducible block cannot have Perron eigenvalue lambda>-c. Fix a positive pre/post time tau. Alpha exp(Tph tau) and exp(Tph tau)omega restrict to strictly positive vectors there. Confine the middle paths to that block and dominate a positive Perron right vector: f(t+2tau) is at least a positive multiple of exp(lambda t), contradicting the exact asymptotic. Conversely -c is an actual pole and hence an eigenvalue. Therefore G has spectral abscissa0, without assuming all modes observable.

A Metzler diagonal is at most its spectral abscissa by a nonnegative shift and principal-submatrix monotonicity. Thus ell>=0. Suppose ell=0. Every upstream state can reach the middle, since every route from its block to the sole output first passes through b0. A positive r_j therefore creates a cycle through the middle; a positive f_i does so using the downstream path; a positive Dback_ij does so using that path and an upstream route back. Shortest routes give a simple cycle.

The matrix retaining only that cycle has its middle diagonal0, all other diagonals strictly negative, and characteristic

`lambda product_j(lambda+d_j)-product_of_cycle_edges`, d_j>0.

Its value at0 is negative and its leading term tends to positive infinity, so it has a positive real eigenvalue. Metzler monotonicity contradicts the spectral abscissa0 of G. Therefore ell=0 would force r=f=Dback=0.

Then G is block upper triangular with blocks A,0,F. The FOUR visible nonreal roots -1±i sqrt(8/9), each of multiplicity2, must distribute one pair into each real3x3 principal block. Neither can hold all four. The remaining eigenvalue of each is its real Perron root -a with0<=a<=1. For such a Metzler block B,

`tr(B^2)=a^2+2(1-8/9)>=sum_i Bii^2>=(a+2)^2/3`.

The first inequality uses nonnegative opposite-edge products and the second is Cauchy. It implies(a-1)^2>=8/3, impossible for0<=a<=1. Hence

`ell>0`.                                              (PH)

This gate uses physical stability, positivity and normalization at the named B6 boundary. It is NOT a statement about arbitrary unstable raw polynomial matches or a trace-only resolution of the original target.

## 6. COMPLETE changed high-generator cone for the variable first holding

Let Rj=[X^j]R. In this table j runs through ALL three upstream coordinates, covering3 r entries,3 f entries and ALL9 Dback entries.

|Actual coefficient|([X5],[X4],[X3])|
|---|---|
|r_j|(b0_j,c0_j+s0 b0_j,d0_j+s0 c0_j-Ueff b0_j)|
|f1|(1,theta-kappa,delta+epsilon+delta*epsilon-v-Abar)|
|f2|(0,1,1+epsilon)|
|f3|(0,0,1)|
|Dback_1j|(0,b0_j,c0_j+(delta+epsilon)b0_j)|
|Dback_2j|(0,0,b0_j)|
|Dback_3j|(0,0,0)|

These follow by multiplying the actual a_R,a_S,v_R,w_S. A zero high triple does not remove lower coefficients from(R). Consequently the SAME actual feedback entries satisfy

```
R5=r^T b0+f1>=0,

T4:=R4-s0 R5
 =r^T c0+(1-kappa)f1+f2+(Dback b0)_1>=0,

S:=R3+mu R5
 =r^T(e0+s0 c0)+[(1-kappa)(delta+epsilon)+u]f1
   +(1+epsilon)f2+f3+(Dback c0)_1
   +(delta+epsilon)(Dback b0)_1+(Dback b0)_2>=0.          (CONE)
```

All signs follow from kappa<=1, not an omitted entry or a false Zeff>=0 assumption. The cancellation uses d0+Abar b0=e0 and P2=kappa(delta+epsilon)+delta*epsilon. The last functional is nonnegative even if its weight mu is negative.

## 7. Exact target coefficients and an actual lower bound for p

Put

`nu=16/9`, `rho=64/81`, `chi=34/9`, `K0=mu+nu`, `L=theta+1`.

K0>=nu-P2>=4/9>0. It is NOT the probability normalizer K=D(c).

The complete principal product is

```
a_R a_S=X6+theta X5+(s0-mu)X4
 -(G0+Ueff+Zeff+s0 Abar)X3
 +(Abar Ueff-Zeff-s0 G0)X2
 +(Abar Zeff+G0 Ueff)X+G0 Zeff.
```

The target DQ has X7 through X3 coefficients

`1, p-3, Cstar-Abar-p+chi, nu(p-3)-Cstar+Abar,`

`nu(Cstar-Abar-p+2)+rho`.

Direct subtraction gives

```
R5=L p-L^2-chi-Ueff-Cstar,
T4=theta Cstar-[K0+theta(theta-1)]p
      +3mu+2(theta-1)Ueff-V+F(theta),
F(theta)=nu(theta+2)+theta^3-theta,                     (E1)

S=[nu+2mu+(theta-2)Ueff-V]p-K0 Cstar
  +Abar Ueff-mu^2+K0 Abar-(nu+6)mu
  +(6-theta-theta^2)Ueff+4G0+(theta+2)Zeff-(2nu+rho).   (E2)
```

These identities are valid with signed Ueff,mu,Zeff,V. Compare the upper Cstar bound from R5>=0 with the lower one from T4>=0. Exact collection yields

```
H0*(p-theta-2)>=theta*nu+(theta-1)Abar+Ueff+V,
H0=2theta-nu-mu.                                      (H)
```

At p=theta+2 the upper-minus-lower expression is exactly the negative of the displayed right side. That side is at least theta*nu-P2-P3>0: even the coarse bound nu-4/3-8/27=4/27 is positive. By(PH) its multiplier ell is positive, so H0>0. Since H0<=2theta-nu+P2,

`p>=theta+2+(theta*nu-P2-P3)/(2theta-nu+P2)`.           (PB)

Use the actual product bounds(PROD) in this positive fraction. In s0 coordinates its denominator is at most

`B=s0^2/3+2s0+2/9`,

and its numerator is at least

`N=16(s0+1)/9-s0^2/3-s0^3/27>0`.

Thus p>=s0+3+N/B. Subtract26/5 and multiply by B. The numerator, multiplied by135, is exactly

```
40s0^3+126s0^2-324s0+174
 =(s0-9/10)^2(40s0+198)+681/50>0.
```

So p>26/5 on the whole selected simplex. Also

`N-(2/3)B=(2-s0)(s0^2+17s0+22)/27>=0`.

We may use BOTH lower bounds

`p>26/5`, `p>=theta+8/3`, hence `ell>=2/3`.             (PBOUNDS)

The second need not be strict at s0=2. No artificial hidden coefficient or fixed-holding WLOG has been introduced.

## 8. Signed constant substitution: the p coefficient must include P3

T4>=0 gives the LOWER bound

`Cstar >= {[K0+theta(theta-1)]p-3mu-2(theta-1)Ueff+V-F(theta)}/theta`.

Its coefficient in(E2) is-K0<0. Substitution and exact collection give

```
S<=-D0*p+Abar Ueff+(3/theta)mu^2+A1 mu+A0
 +(2-theta)[theta+3-K0/theta-p]Ueff
 +[4-K0/theta-p]G0+[theta+2-K0/theta-p]Zeff,            (S1)

D0=K0^2/theta-(3-theta)mu-(2-theta)nu,
A1=theta^2-7+nu+5nu/theta,
A0=nu*theta^2-80/27+512/(81theta).
```

For reconstructing the collection, the non-p mu^2 term is-1+(theta+3)/theta=3/theta; its mu coefficient before simplification is-6+3nu/theta+nu+2nu/theta+theta^2-1. The constant is nu^2(1+2/theta)+nu(theta^2-1)-(2nu+rho). The Ueff factor uses6-theta-theta^2=(2-theta)(theta+3). No effective sign was assumed.

The G0 bracket is negative, since p>26/5>4 and K0>0. Drop its nonpositive term. The Zeff bracket is also negative, since p>theta+2; but Zeff itself may be negative. Use the ACTUAL bound Zeff>=-P3 instead of deleting its term:

`[theta+2-K0/theta-p]Zeff <=P3[p-theta-2+K0/theta]`.

Collect ALL resulting p contributions first. Define

`Dtotal=D0-(theta-2)Ueff-P3`.

We prove Dtotal>0 before substituting either lower p bound.

For2<=theta<=3, Ueff<=mu gives

```
D0-(theta-2)Ueff
 >=[mu+(2nu-theta)/2]^2/theta+(55theta-64)/36.
```

The complete-square identity is valid for every real mu. Therefore

`Dtotal>=23/18-8/27=53/54>0`.                         (DHI)

For1<=theta<=2, P2<=1/3,P3<=1/27. Since Ueff>=-P2,

```
theta[D0-(theta-2)Ueff]
 >=P2^2-(2nu-theta)P2+nu[(theta-1)^2+7/9]
 >=112/81-23/27=43/81.
```

To justify evaluating the intermediate polynomial at mu=-P2, write theta D0=mu^2+[(theta-3/2)^2+47/36]mu+nu[(theta-1)^2+7/9]. It increases for mu>=-P2: its derivative is at least47/36-2/3=23/36>0. Consequently

`theta Dtotal>=43/81-2/27=37/81>0`.                   (DLO)

Let a denote ANY valid lower bound p>=a. After the coupled negative coefficient has been signed, substitution gives

```
S<=-a D0+Abar Ueff+(3/theta)mu^2+A1 mu+A0
       +(theta-2)L_U Ueff
       +P3[a-theta-2+K0/theta],
L_U=a+K0/theta-theta-3.                               (S2)
```

In§9/§10 take a=26/5; in§11 take a=theta+8/3. Both are valid at theta=5/2, so their overlap need not use the same weaker lower bound.

We will use two true bounds on the shared product:

`Abar Ueff<=mu^2/4` for all real mu,

and `Abar Ueff=Abar(mu-Abar)<=0` if mu<=0.              (AU)

## 9. Entire interval 1<=theta<=2, including negative mu and Zeff

For a=26/5 and theta<=5/2, L_U is positive. Indeed

```
L_U>=43/15-4theta/3+13/(9theta)>=1/9>0,
```

using P2<=(theta-1)^2/3 and monotonic decrease of the displayed function up to5/2. Here theta-2<=0, so Ueff>=-P2 gives

`(theta-2)L_U Ueff<=(2-theta)L_U P2`.

Use(AU) in(S2). Then

`S<=C2 mu^2+Bint mu+Cint`,                            (LOW)

with

```
C2=1/4-11/(5theta)<=-17/20,
Bint=B0+(2-theta)P2/theta+P3/theta,
B0=theta^2-(26/5)theta+467/45-48/(5theta),
Cint=Cbase+(2-theta)[26/5+nu/theta-theta-3]P2
              +P3[26/5-theta-2+nu/theta],
Cbase=[720theta^3-3744theta^2+6288theta-4096]/(405theta).
```

Bint<0. In fact

```
45theta Bint=-74+(theta-2)(45theta^2-144theta+179)
                       +45(2-theta)P2+45P3,
45theta^2-144theta+179=45(theta-8/5)^2+319/5>0.
```

The right side is at most-74+15+5/3<0.

For negative mu let t=theta-1 in[0,1]. B0 is concave, because B0''=2-96/(5theta^3)<0 on[1,2]. Its endpoint values are-154/45 and-37/45, so

`Bint>=B0>=-154/45+(13/5)t`.

Using mu>=-P2 and P2<=t^2/3 gives

```
Bint mu<=(-Bint)P2
       <=154t^2/135-13t^3/15
       <=(154/405)(308/351)^2<3/10.                   (LINLOW)
```

The derivative of this cubic is t(308-351t)/135, so the exact maximum is the displayed value at t=308/351. The final inequality is the rational cross-product10*154*308^2<3*405*351^2, not a program output.

The constant numerator expands as

```
720theta^3-3744theta^2+6288theta-4096
 =-832+960t-1584t^2+720t^3
 <=-832+960t-864t^2
 =-864(t-5/9)^2-1696/3.
```

Since405theta<=810, Cbase<=-848/1215. The two positive perturbations of Cint are at most

```
(134/45)*(4/81)=536/3645,
(179/45)*(1/27)=179/1215,
```

respectively: (2-theta)P2<=(1-t)t^2/3<=4/81, while the two remaining brackets are bounded by134/45 and179/45. Hence

`Cint<=-1471/3645<-2/5`.

If mu>=0, both nonconstant terms in(LOW) are nonpositive. If mu<0, its quadratic is still nonpositive and(LINLOW) bounds its linear term by less than3/10. Therefore

`S<-1/10<0`                                         (LOWNEG)

throughout this interval, contradicting(CONE).

## 10. Entire interval 2<=theta<=5/2

Continue to take a=26/5. L_U>=1/9 remains positive. The constant Cbase is the same as in§9. For t=theta-2 in[0,1/2], its numerator is

```
720theta^3-3744theta^2+6288theta-4096
 =-736-48t+576t^2+720t^3
 <=-736+420t<=-526,
```

using t^2<=t/2,t^3<=t/4. Thus

`Cbase<=-1052/2025<-1/2`.                             (CMID)

Also P3<=1/8, P3/theta<=1/16, and

`P3[a-theta-2+nu/theta]<=(1/8)(6/5+8/9)=47/180`.       (ZMID)

If mu>=0, use Ueff<=mu, L_U>0 and(AU) in(S2). Exact quadratic collection yields

```
S<=[5/4-21/(5theta)]mu^2
   +[-theta+349/45-592/(45theta)+P3/theta]mu
   +Cbase+P3[a-theta-2+nu/theta].
```

The quadratic coefficient is at most-43/100. The unperturbed linear bracket increases from-37/45 to-1/150 and is negative; thus the whole linear coefficient is at most1/16. Its quadratic-plus-linear maximum is at most

`25/11008<1/100`.

Together with(CMID)/(ZMID) this gives S<-7/180.

If mu<0, Ueff<=mu<0 implies Abar Ueff<=0 and(theta-2)L_U Ueff<=0. The negative mu term P3 mu/theta can also be dropped. The remaining nonconstant bound is

`[(3-a)/theta]mu^2+B0 mu`.

Here(3-a)/theta<=-22/25, and B0 increases on[2,5/2] from-37/45 to-191/900. Its quadratic-plus-linear maximum is therefore at most

`1369/7128<1/5`.

Combining with(CMID)/(ZMID) gives

`S<-1/2+1/5+47/180=-7/180<0`.                         (MIDNEG)

This contradicts(CONE) for both signs of mu, throughout the entire middle interval.

## 11. Entire interval 5/2<=theta<=3

Now use a=theta+8/3. The corresponding unperturbed constant is

`Cbase=-32theta/27+272/81-512/(243theta)`.

Define the exact envelope including the negative-Zeff budget

```
Fenv(theta)=Cbase+[(theta-1)^3/27]*(2/3+nu/theta)
 =[6theta^3-2theta^2-318theta+858-528/theta]/243.
```

It decreases on[5/2,3]. Its derivative numerator is

`18theta^2-4theta-318+528/theta^2`

`<=162-10-318+2112/25=-2038/25<0`.

At5/2, Fenv=-1339/4860<-1/4. Hence

`Fenv<-1/4`                                          (ENV)

on the entire interval.

### 11.1 Nonnegative mu

Now L_U=-1/3+K0/theta>=7/27>0. Use Ueff<=mu and(AU) in(S2). The quadratic coefficient is

`1/4-5/(3theta)<=-11/36`.

The unperturbed linear coefficient is5/3-112/(27theta)<=23/81. The additional P3/theta is at most8/81: (theta-1)^3/theta increases, so its maximum over this interval occurs at3. The constant is bounded by Fenv. Thus

```
S<=-(11/36)mu^2+(31/81)mu+Fenv
 <=961/8019+Fenv<1/8-1/4=-1/8.                        (HIPOS)
```

### 11.2 Negative mu with L_U>=0

Abar Ueff and(theta-2)L_U Ueff are nonpositive. Bound the Zeff contribution by replacing K0<=nu, giving the same envelope(ENV). The remaining nonconstant polynomial is

```
[-1+1/(3theta)]mu^2+Bneg mu,
Bneg=theta/3-7/9-16/(27theta).
```

Its quadratic coefficient is at most-13/15. Bneg increases from-49/270 to2/81. For mu<=0, the maximum is consequently at most

`2401/252720<1/100`.

By(ENV), S<-1/4+1/100<-1/5.

### 11.3 Negative mu with L_U<0 — do NOT delete this term

The actual inequality L_U=-1/3+(mu+nu)/theta<0 forces

`mu<theta/3-nu<=-7/9`.

Put x=-mu>=7/9. The preceding nonconstant bound is at most

`-(13/15)x^2+(49/270)x`.

Its derivative is negative for x>=7/9, so it is at most its value there,

`-931/2430`.

The term with L_U can now be POSITIVE, but it has an actual physical bound. From mu>=-P2 and(PROD),

`L_U>=1/3-theta/3+13/(9theta)>=-5/27`.

Since Ueff>=-P2, theta-2<=1 and P2<=4/3,

`(theta-2)L_U Ueff <=20/81`.

Using(ENV),

`S<-1/4-931/2430+20/81=-1/4-331/2430<0`.               (HINEG)

This handles precisely the sign branch which a false old deletion would have lost. The three subcases cover ALL real mu in the last interval; together they give S<-1/8, contradicting the SAME actual positive cone.

## 12. Full coverage, actual gain and exact original residual

The proof covers EVERY kappa,delta,epsilon>=0 with kappa<=1 and their sum at most2. No tiny-product condition or finite sample is used. P2 may reach4/3, P3 may reach8/27, Ueff and mu may be negative, and Zeff may be negative. All actual initial/exit couplings, all upstream off-diagonal topologies and all feedback-zero/input-zero boundaries in the literal class were retained.

This is a genuinely new principal/input coupling, not another restriction inside the already closed first-holding1 class. For example kappa=1/2,delta=1/3,epsilon=1/4 gives three unequal downstream holdings; with u=v=w=0 its Zeff=-1/24. The old Zeff>=0 argument cannot even be applied to that tuple. The example only illustrates strict enlargement and the sign failure: the exclusion itself is uniform on the full stated simplex, not proved by example or enumeration.

The contradiction is at SAME-MATRIX characteristic AND actual numerator/initial/exit ties. Every r,f,Dback entry occurs in the complete determinant and generator table. The trace/Cauchy step serves only the indispensable physical ell>0 gate, and is not substituted for the coefficient proof. Hurwitzness and all PH row/initial/exit normalizations were explicitly retained. Positive raw coordinate normalization of downstream path edges is not claimed itself to preserve physical row sums; the h0 normalization restores those ties. For d>0, change time unit by d and replace c by c/d; the theorem concerns exactly the stated dimensionless shifted holding ratios, not arbitrary holdings declared WLOG.

No actual PH7 witness at8/9 and no ALL-TOPOLOGY empty-intersection certificate has been obtained. Remaining cases include upstream holding multisets other than(1,1,2), downstream holdings below1 or outside the stated sum/entry bounds, other center/input/output placements, missing downstream designated path and other dominator allocations. Multiple upstream exits and absence of an upstream designated path are covered ONLY at the literal stated holding/topology boundary, not globally eliminated. The unrestricted minimum remains{7,8} at B6 and retained upper8. No full existence-band endpoint, full minimum-order function or original book problem is decided here.

A FRESH COMPLETE written reconstruction must expose the named B6 lower import and read this entire new source. No old review of361,475 or498LF automatically accepts the variable-entry simplex. The proof is complete at its declared import boundary, but author-written/source-pinned mathematics is not formal proof, Lean-kernel verification, human/configured-family review, executable acceptance, novelty or priority clearance. Earlier unadmitted arithmetic outputs remain preserved and additively qualified and supply no verification credit here. Machine/kernel checks for this manuscript: NONE.
