# PH7 at 8/9: a multiple-exit, genuinely unequal downstream triple obstruction

Status: WRITTEN AUTHOR CANDIDATE, not yet independently reconstructed or parent-supported. Pre-write metadata clock: `/bin/date` returned `Sun Oct 25 11:41:40 PDT 2026`. Same frozen primary authority `primary-continuation-20261025-102319-v1.json`; HOLD v2 and parent errata v9/v10/v11 remain binding. No scientific interpreter, symbolic program, enumeration, solver, executable replay or kernel check was used for this manuscript. All identities and inequalities below are written derivations.

## 1. Exact statement, named import and non-promotion boundary

Normalize d=1. Put

`D(y)=y[(y+1)^2+8/9]^2`, `K=D(c)>0`, `H(s)=K/D(s+c)`, with c>0.

Let A be ANY real3x3 Metzler matrix with diagonal(-1,-1,-2): all six off-diagonal entries are arbitrary nonnegative real numbers, including zeros. There is NO designated positive upstream path. Let b0 be ANY nonnegative3-column of actual upstream exits to the middle phase, and beta_R ANY nonnegative3-row of actual initial weights. In particular b0 need not be e3 or have only one nonzero entry.

Choose delta,epsilon>=0 with

`theta=1+delta+epsilon in[1,3]`, `P=delta*epsilon<=1/40`.

The actual downstream matrix and the complete7x7 raw matrix are

```
F=[-1,1,0
    u,-(1+delta),1
    w,v,-(1+epsilon)],              u,v,w>=0,

G=[ A        b0       0
    r^T     -ell      e1^T
    Dback    f        F ],

beta=(beta_R,0,0,0,0),             gamma=K e7.
```

Every component of r,f and every one of the nine entries of Dback is an arbitrary actual nonnegative matrix entry; ell is initially any real number. The stated downstream path and sole final exit are retained. No actual backward/cross-feedback is suppressed.

THEOREM CANDIDATE, at the named B6 import: there is no such tuple for which G-cI is Hurwitz and beta(sI-(G-cI))^(-1)gamma equals H(s). Consequently there is no actual PH7 representation in this entire class, including multiple upstream exits, arbitrary upstream input support, absence of an upstream designated path, and genuinely unequal downstream triples.

The only substantive mathematical import is B6: the retained WRITTEN exclusion of ALL actual PH representations of order at most6 at z=b_pole^2/d^2=8/9>1/2. Its source is `proof-unrestricted-six-state-barrier-v1.md`, SHA256 `8ba04931bb26e9fec097cb75793aa99b2e5d4d2309da94e1be9328dacb830c25`. Its complete195-LF body has been read; its lower theorem is a named retained import, not newly executed or newly formally verified here. The operative parent qualification is section2, LF43-72, of `institute/runs/three-area-2026-10-23-96h/priority-written-dispositions-v1.md`, snapshot SHA256 `faf0335d8569a39c2fce54f09f4e8e1474021b60cf176bd16888e1a266048787`; only that section, not the whole parent document, is invoked. In particular the historically invented older PH6 clock is not adopted.

The earlier same-author q in[1,2] single-exit manuscript remains an unpromoted candidate. Neither its correctness nor a future acceptance of it is an input to this proof. All matrix, numerator and scalar arguments needed here are supplied below. The new class is not asserted WLOG among all PH7 matrices. The unrestricted minimum at8/9 is STILL undecided between7 and8 at the retained lower/upper imports.

## 2. Which old identities fail, and what replaces them

With multiple upstream exits, the leading cofactor column is b0, NOT e3. Thus the old identity R5=r3+f1 is false in general. The actual numerator is not the old coordinate expression Cbar-a either. Its leading coefficient and constant must be derived from the same beta_R,b0,A.

With both downstream nonunit holdings present, the actual downstream determinant acquires P X in addition to the changed X^2 term. The quantity playing the old return mass is now u+v-P, which MAY BE NEGATIVE. Therefore neither the old assumption M>=0 nor a deletion based on a nonnegative effective return mass transfers. For theta>2, the old U-term deletion also has the wrong sign.

The replacements are: an entrywise positive MATRIX adjugate cone for all upstream input/exit couplings; a load-bearing PH/Perron proof that ell>0; and signed effective-mass bounds which keep the p coefficient coupled to the actual return variables before substituting p. No feedback redistribution inside the already closed family is being treated as a new witness.

## 3. Positive upstream matrix cone without a designated path

Set X=y+1 and J=A+I. Thus diag J=(0,0,-1). Define actual nonnegative quantities

```
Abar=J12*J21+J13*J31+J23*J32,
G0=J12*J21+J12*J23*J31+J13*J32*J21.
```

Direct determinant expansion gives

`a_R=det(yI-A)=X^3+X^2-Abar X-G0`.

Both J+I and J^2+J are entrywise nonnegative. For the latter statement, its ith diagonal is sum_(j!=i)Jij Jji, since Jii^2+Jii=0. For i!=j its entry is

`(1+Jii+Jjj)Jij + sum_(k!=i,j)Jik Jkj`.

The first coefficient is1 for the pair{1,2} and0 for a pair containing3; the remaining term is nonnegative. This proves the claim for EVERY upstream off-diagonal topology, not just the old two normalized forward edges.

Put

```
c0=(J+I)b0>=0,
e0=(J^2+J)b0>=0,
d0=e0-Abar b0.
```

The ACTUAL adjugate column is

`v_R=adj(yI-A)b0=X^2 b0+X c0+d0`.                         (AR)

For example the full adjugate polynomial is X^2 I+X(J+I)+J^2+J-Abar I. Multiplication by XI-J gives a_R I, using the directly expanded characteristic identity J^3+J^2-Abar J-G0 I=0. In contrast to b0,c0,e0, d0 need not be nonnegative; its sign is never assumed.

## 4. Downstream cofactors and the full shared characteristic/numerator

Write

```
sigma=delta+epsilon=theta-1,
U=u+v>=0,
Ueff=U-P,
Z=w+epsilon*u>=0,
mu=Abar+Ueff,
V=G0+Z>=0.
```

The constraints retained for later use are

`mu>=-P`, `-P<=Ueff<=mu`, `Abar>=0`, `G0,Z>=0`.           (B)

They do NOT include Ueff>=0 or mu>=0.

Direct downstream adjugates give

```
a_S=det(yI-F)=X^3+sigma X^2-Ueff X-Z,
w_S=e1^T adj(yI-F)=(X^2+sigma X+P-v, X+epsilon,1).
```

Multiplying this row by

`yI-F=[[X,-1,0],[-u,X+delta,-1],[-w,-v,X+epsilon]]`

gives(a_S,0,0). In particular the same actual epsilon*u occurs in Z; no independent constant is chosen.

Let Q=beta_R v_R. Full single-middle-phase elimination, with denominators cleared, gives the polynomial identities

```
P7=det(yI-G)
  =(y+ell)a_R a_S-a_S r^T v_R-a_R w_S f-w_S Dback v_R,

beta adj(yI-G)gamma=KQ.
```

One may first solve the two actual principal resolvents and the remaining scalar middle equation away from their roots; polynomial clearing proves the identities everywhere, including singular principal values. Thus the ACTUAL transfer is KQ/P7.

Exact equality to K/D forces the ENTIRE identity

`P7=DQ`,                                                (T)

even if factors coincide or cancel. Since P7 and D are monic of degrees7 and5, Q must be monic of degree2. Therefore target matching itself forces

`beta_R b0=1`.

Set

`p-2=beta_R c0>=0`, `Cstar=beta_R e0>=0`.

The ACTUAL numerator is then

`Q=X^2+(p-2)X+Cstar-Abar`.

Its y-coordinate constant is p-1+Cstar-Abar; it is not fixed in advance, and both real and nonreal hidden pairs are allowed. Cstar,p,Abar remain tied to the SAME beta_R,b0,A. We use their necessary signs without claiming independent realizability.

Trace in(T) gives

`ell=p-theta-2`, `k=ell-1=p-theta-3`.

Accordingly the complete feedback residual is

```
R=(X+k)a_R a_S-DQ
 =a_S r^T v_R+a_R w_S f+w_S Dback v_R.                  (R)
```

No lower coefficient is discarded from this equality, and no separately selected spectrum is substituted for the actual numerator.

## 5. Actual PH normalization and the strictly positive middle holding

This section is essential: for the enlarged holding region, ell>0 is NOT assumed as a free polynomial inequality.

Assume toward contradiction a Hurwitz raw candidate M0=G-cI realizing H. Then

`h0=(-M0)^(-1)gamma=integral_0^infinity exp(M0 t)gamma dt>=0`.

If I is the set of positive coordinates of h0, a zero coordinate satisfies gamma_i=0 and M0_ij=0 for j in I: this follows from M0 h0=-gamma and nonnegative off-diagonal entries. Thus zero-h coordinates cannot return to I or contribute to the output. Restricting to I preserves the exact transfer. The principal Metzler block is Hurwitz, and positive scaling on I gives

```
Tph=diag(h0_I)^(-1) M0_II diag(h0_I),
alpha=beta_I diag(h0_I),
omega=diag(h0_I)^(-1)gamma_I,
Tph*1=-omega,        alpha*1=beta h0=H(0)=1.
```

This is an ACTUAL PH representation, with the original nonnegative initial/exit law. If any coordinate were removed its order would be at most6, contrary to the named B6 import. Hence h0>0 on all7 phases and the displayed normalization applies without removal.

Likewise every phase is initial-reachable: otherwise the reachable principal PH subsystem, closed under outgoing transient edges by the definition of reachability, would realize the same law in at most6 phases. Again B6 forbids this. Every phase is exit-co-reachable, both from h0>0 and from proper PH transience.

The exact inverse-transform asymptotic is

`f(t)=[K/(1+8/9)^2] exp(-ct)+O(t exp(-(c+1)t))`.

The Perron eigenvalue of an initial-reachable, exit-co-reachable dominant irreducible block cannot exceed -c. To see this without assuming all modes observable, fix a positive pre/post time tau. The vectors alpha exp(Tph tau) and exp(Tph tau)omega are strictly positive on that block. Restricting paths to it bounds f(t+2tau) below by a positive multiple of exp(lambda t), using its positive Perron right vector. If lambda>-c this contradicts the displayed exact asymptotic. Conversely -c is an actual pole of H, so it is an eigenvalue. Hence the shifted G has spectral abscissa0. Similarity does not change its diagonal entries or graph.

For a Metzler matrix every diagonal entry is at most its spectral abscissa, by shifting to a nonnegative matrix and applying principal-submatrix monotonicity. Thus ell>=0.

Suppose ell=0. Each upstream phase can reach the middle phase: every route from the upstream block to the sole output must first leave it through b0 into the middle phase. If some r_j>0, there is therefore a positive cycle from the middle phase to that upstream phase and back. If some f_i>0, the positive downstream path gives a cycle from the middle phase through downstream phase i and back. If some Dback_ij>0, the same downstream path followed by that edge and an upstream route back gives a cycle through the middle phase. A shortest such route gives a simple positive cycle.

Its middle diagonal is0 and all its other diagonals are strictly negative. The matrix retaining just this cycle has characteristic

`lambda*product_j(lambda+d_j)-product_of_cycle_edges`,   d_j>0,

so it has a positive real eigenvalue: its value at0 is negative and its leading term tends to positive infinity. Metzler monotonicity makes the spectral abscissa of G at least this positive value, a contradiction. Consequently ell=0 would force r=f=Dback=0.

But then G is block upper triangular with blocks A,0,F. The FOUR visible nonreal eigenvalues -1±i sqrt(8/9), each of multiplicity2, must distribute one conjugate pair to each real3x3 principal block: one such block cannot contain all four roots. A real3x3 Metzler block with that pair must have a real Perron third eigenvalue -a, with0<=a<=1, because its spectral abscissa is at most0 and at least -1. For that block B,

`tr(B^2)=a^2+2(1-8/9)>=sum_i Bii^2>=(a+2)^2/3`.

The first inequality uses nonnegative opposite-edge products and the second is Cauchy. Rearranging gives `(a-1)^2>=3*(8/9)=8/3`, impossible for0<=a<=1. Therefore

`ell>0`.                                               (PH)

This proof retains actual initial/output positivity and stability. It is not a trace-only rejection of the original problem, nor a claim about an arbitrary unstable raw polynomial match.

## 6. Every high-coefficient generator, with its actual signs

Let Rj=[X^j]R. In the following table j ranges over all three upstream coordinates. It lists ALL3 r entries, ALL3 f entries and ALL9 Dback entries, not just the ones nonzero in an old single-exit basis.

|Actual coefficient|([X5],[X4],[X3]) of its generator|
|---|---|
|r_j|(b0_j,c0_j+sigma b0_j,d0_j+sigma c0_j-Ueff b0_j)|
|f1|(1,theta,sigma+P-v-Abar)|
|f2|(0,1,1+epsilon)|
|f3|(0,0,1)|
|Dback_1j|(0,b0_j,c0_j+sigma b0_j)|
|Dback_2j|(0,0,b0_j)|
|Dback_3j|(0,0,0)|

Terms with a zero displayed triple are STILL in the full identity(R) at lower degrees. Direct multiplication of the actual a_R,a_S,v_R,w_S gives this table.

It follows that the SAME actual feedback entries satisfy

```
R5=r^T b0+f1>=0,

T4:=R4-sigma R5=r^T c0+f1+f2+(Dback b0)_1>=0,

S:=R3+mu R5
 =r^T(e0+sigma c0)+(sigma+u)f1+(1+epsilon)f2+f3
   +(Dback c0)_1+sigma(Dback b0)_1+(Dback b0)_2>=0.       (CONE)
```

The last identity uses d0+Abar b0=e0 and Ueff=u+v-P. In particular it is positive EVEN WHEN mu<0. The product P is not silently omitted, f2 has its actual1+epsilon coefficient rather than theta, and all multiple-exit/cross-feedback terms are retained.

## 7. Exact coefficient expansion and the full-input p bound

Put

`nu=16/9`, `rho=64/81`, `chi=34/9`, `K0=mu+nu`, `L=theta+1`.

K0>0 since mu>=-P>=-1/40. It is NOT the probability normalizer K=D(c).

For direct reconstruction, the full principal product is

```
a_R a_S=X6+theta X5+(sigma-mu)X4
 -(G0+Ueff+Z+sigma Abar)X3
 +(Abar Ueff-Z-sigma G0)X2
 +(Abar Z+G0 Ueff)X+G0 Z.
```

The target is D=(X-1)(X^2+8/9)^2 and Q=X^2+(p-2)X+Cstar-Abar. Its X7 through X3 coefficients are

`1, p-3, Cstar-Abar-p+chi, nu(p-3)-Cstar+Abar,`

`nu(Cstar-Abar-p+2)+rho`.

Subtracting from(X+k)a_R a_S gives

```
R5=L p-L^2-chi-Ueff-Cstar,

T4=theta Cstar-[K0+theta(theta-1)]p
      +3mu+2(theta-1)Ueff-V+F(theta),

F(theta)=nu(theta+2)+theta^3-theta.                      (E1)
```

The corresponding third functional is

```
S=[nu+2mu+(theta-2)Ueff-V]p-K0 Cstar
  +Abar Ueff-mu^2+K0 Abar-(nu+6)mu
  +(6-theta-theta^2)Ueff+4G0+(theta+2)Z-(2nu+rho).       (E2)
```

These are polynomial identities in the actual matrix/input quantities, valid even for signed Ueff,mu.

Compare the upper Cstar bound from R5>=0 with the lower one from T4>=0, multiplying by theta>0. Exact collection yields

```
H0*(p-theta-2)>=theta*nu+(theta-1)Abar+Ueff+V,
H0=2theta-nu-mu.                                       (H)
```

At p=theta+2 the upper-minus-lower expression is precisely the negative of the displayed right side. By(B) that right side is at least theta*nu-P>0. Since p-theta-2=ell>0 by(PH), H0>0. Also H0<=2theta-nu+P. Therefore

`p>=theta+2+(theta*nu-P)/(2theta-nu+P)`.

The denominator is positive throughout the stated domain. Subtract11/2 and multiply by it. The numerator is EXACTLY

```
2theta^2-7theta+56/9+(theta-9/2)P
 =2(theta-7/4)^2+7/72+(theta-9/2)P
 >=7/72-7/80=7/720>0.
```

We have proved the uniform STRICT bound

`p>p1:=11/2`.                                          (PBOUND)

This replaces, rather than assumes, the old50/9 or11 regimes.

## 8. Substitute the correct lower numerator bound, retaining signed mass

From T4>=0,

`Cstar >={[K0+theta(theta-1)]p-3mu-2(theta-1)Ueff+V-F(theta)}/theta`.

Since the coefficient of Cstar in(E2) is-K0<0, substitution gives an UPPER bound. Exact collection is

```
S<=-D0(mu,theta)*p+Abar Ueff+(3/theta)mu^2+A1(theta)mu+A0(theta)
 +(2-theta)[theta+3-K0/theta-p]Ueff
 +[4-K0/theta-p]G0+[theta+2-K0/theta-p]Z,                (S1)

D0=K0^2/theta-(3-theta)mu-(2-theta)nu,
A1=theta^2-7+nu+5nu/theta,
A0=nu*theta^2-80/27+512/(81theta).
```

For checking this collection, the non-p mu^2 coefficient is-1+(theta+3)/theta=3/theta. The non-p mu coefficient before simplification is -6+3nu/theta+nu+2nu/theta+theta^2-1. The constant is nu^2(1+2/theta)+nu(theta^2-1)-(2nu+rho), which gives the displayed A0. The Ueff factor uses6-theta-theta^2=(2-theta)(theta+3). No sign of Ueff or mu was used.

By(PBOUND), K0>0, G0,Z>=0 and theta<=3, the last TWO brackets in(S1) are strictly negative. Those two terms may be dropped. But the Ueff term may not be dropped with its old sign.

Collect its p contribution FIRST. Define

`Deff=D0-(theta-2)Ueff`.

We now prove Deff>0 on the entire stated domain, before using the lower p bound.

## 9. The coupled p coefficient is negative even when mu<0

For2<=theta<=3, Ueff<=mu and theta-2>=0 give

```
theta Deff>=theta[D0-(theta-2)mu]
 =[mu+(2nu-theta)/2]^2+theta(55theta-64)/36>0.            (DHI)
```

This complete-square identity is valid for ALL real mu; it does not secretly assume mu>=0.

For1<=theta<=2, Ueff>=-P gives Deff>=D0-(2-theta)P. Write

```
theta D0=mu^2+B(theta)mu+nu[(theta-1)^2+7/9],
B(theta)=theta^2-3theta+2nu=(theta-3/2)^2+47/36.
```

As a function of mu>=-P, this polynomial is strictly increasing: its derivative is at least47/36-2P>0. Thus

```
theta Deff>=P^2-(2nu-theta)P+nu[(theta-1)^2+7/9]
             >=112/81-23/360>0.                         (DLO)
```

We used P<=1/40 and2nu-theta<=23/9. Therefore Deff>0 in both cases, including theta=2.

Only NOW substitute p>p1 in the combined negative term. After dropping the two G0,Z terms already signed, this yields

```
S<=-p1 D0+Abar Ueff+(3/theta)mu^2+A1 mu+A0
       +(theta-2)L_U Ueff,
L_U=p1+K0/theta-theta-3.                                (S2)
```

Here L_U>0 uniformly. Indeed its lower bound p1-theta-3+(nu-P)/theta decreases with theta, so

`L_U>=5/54-P/3>=91/1080>0`.

Finally, the real identity `(Abar-Ueff)^2>=0` gives

`Abar Ueff<=(Abar+Ueff)^2/4=mu^2/4`,                    (AU)

without requiring Ueff>=0.

## 10. Entire lower theta interval, including negative mu

Suppose1<=theta<=2. Since theta-2<=0, L_U>0 and Ueff>=-P,

`(theta-2)L_U Ueff<=(2-theta)L_U P`.

Use(AU) in(S2). The resulting quadratic bound is

`S<=C2 mu^2+Bint mu+Cint`,                              (LOW)

where

```
C2=1/4-5/(2theta)<=-1,
Bint=theta^2-(11/2)theta+203/18-32/(3theta)
       +(2-theta)P/theta,
Cint=Cbase(theta)+(2-theta)[p1+nu/theta-theta-3]P,

Cbase(theta)=[144theta^3-792theta^2+1344theta-896]/(81theta).
```

For the linear coefficient,

```
18theta Bint=-38+(theta-2)(18theta^2-63theta+77)
                       +18(2-theta)P,
18theta^2-63theta+77=18(theta-7/4)^2+175/8>0.
```

Consequently18theta Bint<=-38+18P<0. Also crude termwise bounds give

`Bint>=1-11+203/18-32/3=-169/18>-10`.

Thus-10<Bint<0 throughout this closed interval.

For the constant, let t=theta-1 in[0,1]. Its unperturbed numerator is

```
144theta^3-792theta^2+1344theta-896
 =-200+192t-360t^2+144t^3
 <=-200+192t-216t^2
 =-216(t-4/9)^2-472/3.
```

Since81theta<=162, Cbase<=-236/243<-9/10. The perturbation is at most

`(p1+nu-4)P<=(59/18)/40=59/720<1/10`.

Hence Cint<-4/5. If mu>=0 all nonconstant terms in(LOW) are nonpositive. If-P<=mu<0, the quadratic term is still nonpositive and Bint mu<=10P<=1/4. Therefore throughout this entire interval

`S<-11/20<0`,                                          (LOWNEG)

contradicting(CONE).

## 11. Entire upper theta interval, not the old U deletion

Suppose2<=theta<=3. This time theta-2>=0, so Ueff<=mu and L_U>0 give

`(theta-2)L_U Ueff<=(theta-2)L_U mu`.

Use(AU) in(S2). Exact collection gives

```
S<=A2 mu^2+Bext mu+Cbase(theta),
A2=5/4-9/(2theta)<=-1/4,
Bext=-theta+145/18-128/(9theta).                        (HIGH)
```

Bext increases on[2,3], since its derivative is-1+128/(9theta^2)>0. Its exact endpoint values give

`-19/18<=Bext<=17/54`.

For Cbase, put t=theta-2 in[0,1]. Its numerator is

```
144theta^3-792theta^2+1344theta-896
 =-224-96t+72t^2+144t^3
 <=-224+120t<=-104.
```

Thus Cbase<=-104/243<-2/5. If mu>=0, the nonconstant part of(HIGH) is at most

`-(1/4)mu^2+(17/54)mu<=(17/54)^2=289/2916<1/10`.

If-P<=mu<0, its quadratic term is nonpositive and Bext mu<=(19/18)P<=19/720<1/10. In either case,

`S<-3/10<0`,                                           (HIGHNEG)

again contradicting the SAME actual feedback identity(CONE).

## 12. What has actually been excluded and what has not

The two intervals cover the WHOLE domain theta in[1,3], P<=1/40, with delta,epsilon>=0. Every actual coefficient/input-zero boundary and both theta endpoints were retained. No sampling, finite enumeration, hidden-pair discriminant restriction, row-sum assumption or missing-feedback ansatz was used. Negative mu and Ueff were handled explicitly rather than excluded.

This is a genuine two-dimensional unequal-downstream region, not another special rational holding tuple. For example downstream holdings(1,11/10,6/5) have theta=13/10 and P=1/50<1/40, so all three holdings are unequal. This example only illustrates membership; the proof is uniform on the whole domain. Both axes delta=0 and epsilon=0 are included up to a third/middle holding3, and arbitrary multiple upstream exits and arbitrary upstream topology were already quantified in the theorem.

For general d>0, change the time unit by d and replace c by c/d. The theorem concerns exactly the corresponding DIMENSIONLESS shifted holding ratios. It does not make those ratios WLOG for arbitrary PH7 matrices.

This candidate excludes ACTUAL PH7 or equivalent Hurwitz positive normalized transfers in the stated family, using B6 for the trimming/Perron gate. It does NOT claim that every possibly unstable raw polynomial match in the enlarged region is impossible. Its contradiction is nevertheless at exact same-matrix characteristic AND numerator ties: the positive functional was derived from every actual feedback entry and from beta_R adj(yI-A)b0, not from a trace screen or a chosen spectrum alone.

Still unresolved at the original point8/9 are general upstream holding multisets, a different first downstream holding, the rest of the unequal-downstream region (including P>1/40 or theta>3), different center/input/output placements, missing downstream designated path, other dominator allocations and any topology not reduced to this literal class. Multiple upstream exits are now included ONLY at the stated holdings and topology, not globally eliminated. There is still no actual PH7 coefficient witness and no all-topology empty-intersection certificate. The unrestricted minimum remains{7,8} at its retained imports; no full existence-band endpoint or original book problem is decided here.

The new source requires a fresh complete written reconstruction with the B6 input boundary exposed. No verdict for the older single-exit manuscript automatically accepts this enlarged class, and no union of import sets is silently promoted. Source-pinned written review, if later obtained, is not formal proof, Lean-kernel verification, human/configured-family review, executable acceptance, novelty or priority clearance. Earlier unadmitted arithmetic outputs are preserved under their additive qualification and supply no verification credit for this manuscript.
