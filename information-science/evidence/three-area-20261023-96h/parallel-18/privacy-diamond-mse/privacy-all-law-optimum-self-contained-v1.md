# All-Borel diamond MSE: self-contained geometry, one-core calibration and uniqueness

Owner InfoResearch96h-2, original info-1. Actual preceding `/bin/date`: **Sun Oct 25 11:43:56 PDT 2026**, observed before this write, not an estimated creation instant or continuous-activity census.

**AUTHOR WRITTEN DEPENDENCY-CLOSURE CANDIDATE, UNREVIEWED.** This proves in one body the problem-specific analytical steps previously carried as S/C/X/A/B-geometry and CAL inputs. It is not an independent review, formal proof, new value/discovery count or novelty clearance, and does not retroactively replace any frozen import record. Explicit parent adoption after a separate complete reconstruction is still required.

## 0. Scope, ancestry and permitted standard imports

The REGISTERED target is unchanged: ALL Borel query-output-independent additive-noise laws on R2, EVERY shift in the full CLOSED unit-l1 diamond, squared-Euclidean loss, EVERY finite epsilon>0. No density, symmetry, convexity, radiality, independence or peak-attainment ansatz is placed on the original laws. Nonadditive/data-dependent channels and the broad book article are not claimed solved.

Cactus remains an UNBOUND auxiliary lead; its latest candidate is not used here or counted as a new primary. The1049assignment is PRIMARY research, as its additive contract clarification states. The v81 temporary review was actually returned before the separate primary-resumption ACK. Source/clock/hash work and WRITTEN reasoning only: no scientific interpreter/eval/program, symbolic calculation, enumeration, solver, replay, compilation, kernel, nested agent or model CLI.

The standard facts used without reproving their general theorems are: Radon–Nikodym and regularity/order of finite Radon measures; Tonelli and absolutely integrable signed Fubini; Prokhorov and Portmanteau; Rademacher and the Lebesgue density theorem; elementary compactness and dominated differentiation; and change-of-variable/chain rules for increasing bi-Lipschitz absolutely continuous functions. Every model-specific geometric, normalization, signed-gap and entire-core minimization step is proved below.

The source ancestry is preserved: shell/Minkowski mechanisms are prior Soria-Comas–Domingo-Ferrer2011/2013; generic density/attainment and rearrangement tools have prior coverage; the earlier fixed-active selector comparisons were prior comparative statics. This proof does not claim a new staircase mechanism or general symmetrization/selector theorem. The fresh bounded matching-norm comparisons in privacy-primary-source-refresh-v1.json do NOT clear mixed-cost novelty or stronger acceptance.

For authentication, the complete S367/C124/X125/A166/CAL269 bodies and the407LF uniqueness/lower-bound premises were actually read in1049. They supplied the lineage, not black-box mathematical premises in this body. Their frozen hashes and exact reads are recorded in checkpoints036/038. The578LF branch-arithmetic candidate was only read1–90 in this intake; its earlier numerical/kernel-labelled outputs, finite tables, Galois and transcendence calculations are NOT premises here. Historical arithmetic remains unadmitted and receives no verification credit.

## 1. Model and theorem

Fix0<b<1, epsilon=-log b, and

```
D={h: |h1|+|h2|<=1}.
```

A Borel probability law mu is feasible when

```
mu(E)<=b^(-1)mu(E+h) for EVERY Borel E and EVERY h in D.
```

Let V be the infimum of J(mu)=integral |z|_2^2 dmu(z). Put

```
m=b/(1-b),
T2=m+2m^2,
T3=m+6m^2+6m^3,
T4=m+14m^2+36m^3+24m^4,
v=T2-m^2=m+m^2,
lambdaP=T4/(3T2)=4m^2+4m+1/3.
```

**Theorem — WRITTEN candidate at the explicit standard imports in Section0.** There is a UNIQUE optimal Borel probability law. Its density, up to null-set version changes, is

```
p_*(z)=Z_*^(-1)b^n_*(z),
n_*(z)=min{k>=0 integer: z in S_*+kD},
S_*={z: |z|_1<=2t_*,
         |z|_2^2+2m|z|_infinity+T2<=lambda_*}.
```

Here t_*>0, lambda_*=V, T2<lambda_*<lambdaP and lambda_*<=4/epsilon^2. The terminal diamond facet has width strictly between0 and1/2. Section8 supplies globally screened D/R scalar systems determining the unique parameters with no unknown-profile optimization left. The construction is feasible for the FULL closed diamond. Equality is of probability LAWS, not of arbitrary pointwise density versions.

The logical proof order is: original all-law attainment/phase mixture; SAME-LAW optimal geometric regularization; four separate strict Steiner equalities; exact canonical parallel geometry and original-optimal cap raising; entire-core definition/ceiling; signed inverse-birth lower bound; independent entire-core calibration/uniqueness; all-original-law equality. In particular the lower bound does not import a one-core ansatz, V=W or a stationary root.

## 2. All-law foundations and the exact amplitude mixture

### 2.1 Density, positivity and finite cap are consequences

For a Borel Lebesgue-null N, integrate privacy over h in the area-two diamond. Tonelli gives integral_D mu(N+h)dh=0, hence mu(N)=0. Thus mu has a Borel density p.

For each fixed h, measure privacy yields p(x+h)>=bp(x) for a.e.x. Fubini in(x,h) gives this for a.e.h in D at a.e.x; integrating shows2b p(x)<=integral_(x+D)p<=1. Therefore0<M=esssup p<=1/(2b)<infinity. No attained maximum is assumed.

The density is positive a.e. Otherwise choose a bounded positive-area Borel subset A of{p=0}. Iterating privacy makes mu(A+t)=0 for EVERY t in R2, since t belongs to some jD. But Tonelli over all translations gives integral mu(A+t)dt=|A|>0, contradiction. Null-set versions may be clipped to[0,M] without changing the law.

### 2.2 Original attainment, with all-shift weak closedness

The product Laplace density epsilon^2 exp(-epsilon|x|_1)/4 is feasible by the triangle inequality and has cost U=4/epsilon^2. A minimizing sequence of cost<=U+1 is tight by Markov; Prokhorov gives a weak probability limit.

For ANY fixed h in D and nonnegative phi in C_c, privacy says

```
integral phi dmu_j<=b^(-1)integral phi(x-h)dmu_j(x).
```

Both tests pass through the SAME weak convergence. Radon measure order against all such tests gives the all-Borel inequality in the limit. The argument is for arbitrary h, not an h-dependent subsequence or an uncountable intersection of density exceptions. Portmanteau/truncation of |x|^2 gives lower semicontinuity and an attaining original law. Its cost is positive: zero second moment would put the probability on{0}, incompatible with absolute continuity.

### 2.3 Phases apply to EVERY finite-cost feasible density

For a in[bM,M), set

```
n_a(x)=min{k>=0:p(x)>a b^k},
r_a(x)=b^n_a(x), Z_a=integral r_a, q_a=r_a/Z_a.
```

At the null zero set use n_a=infinity,r_a=0. Joint measurability follows from countable indicators. The top set{p>a} has positive area for EVERY a<M. Minimality of the index, with a>=bM for its zero case, gives

```
bp/a<=r_a<=p/a, hence b/a<=Z_a<=1/a.
```

Every q_a has finite cost. For each fixed h, the original p inequality is independent of a; outside its fixed-h null set,

```
p(x)>a b^k ==> p(x+h)>a b^(k+1).
```

The reverse shift gives index difference<=1 and hence feasible q_a for EVERY a and EVERY fixed h in the measure sense. No common pointwise version for uncountably many h is assumed.

The elementary identity r_a=(1-b)sum_(k>=0)b^k1_(p>a b^k) and the substitutions u=a b^k partition[0,M]. Therefore

```
(1-b)^(-1)integral_(bM)^M r_a(x)da
 =sum_k integral_(b^(k+1)M)^(b^kM)1_(p(x)>u)du=p(x).
```

Tonelli gives the exact probability/cost mixture

```
integral_(bM)^M Z_a/(1-b)da=1,
J(p)=integral_(bM)^M J(q_a)Z_a/(1-b)da.                 (PH)
```

For an original optimizer, all J(q_a)>=V and their average is V; a single COST-defined full-weight phase set has geometric optimal q_a and positive-area top plateaux. This both supplies one geometric optimum and will later reach ALL original optimizers.

## 3. ANY geometric optimum: compact closed levels of the SAME law

Fix ANY original optimal geometric density q=alpha b^n, alpha>0, with a positive-area top plateau; J=V is its ACTUAL cost. Write E_i={n<=i} and K_i=ess-supp(1_(E_i)dx). No averaging or symmetry has occurred.

Every E_i has finite positive area. Fubini in the first diamond gives, for a.e.x,

```
J>=bq(x)integral_D |x+h|^2dh=bq(x)(2|x|^2+2/3).
```

Here |D|=2, centroid0, and each coordinate moment is1/3 by direct integration. On E_i this bounds |x|^2 by J/(2alpha b^(i+1)). Thus K_i is nonempty compact, nested, and E_i is in K_i a.e.

For EACH fixed h in D, index privacy gives(E_i+h) in E_(i+1) a.e. Translating essential supports yields K_i+h subset K_(i+1), and h was arbitrary. Hence

```
K_i+D subset K_(i+1) exactly.                           (FWD)
```

### 3.1 Positive-offset boundary and a.e. full dilation filling

For a.e.y the density inequality holds for a.e.h in D. If(1_Ei*1_D)(y)>0, it forces q(y)>=alpha b^(i+1). The convolution is positive on K_i+int D: a small ball around a support point fits in y-D and meets E_i in positive area.

For ANY nonempty compact K, its distance d(x)=dist_1(x,K) is Lipschitz. At a differentiability point outside K take a nearest z and u=(x-z)/d(x). For0<t<d(x), nearest-point and Lipschitz bounds give EXACTLY d(x-tu)=d(x)-t. Thus grad d dot u=1 and ||grad d||_infinity=1. A differentiable function constant on a density-one level set has gradient0: a nonzero gradient confines that level in arbitrarily thin slabs. Rademacher plus the density theorem therefore proves every positive level{d=r} has area0, in particular r=1.

Since K+D={d<=1} and K+int D={d<1}, the preceding convolution argument gives

```
K_i+D subset E_(i+1) a.e.                              (FILL)
```

No zero-area assumption on K_i's OWN boundary or convexity was used.

### 3.2 Actual lowering, not a frozen-height variation

For i>=0 take U=(E_(i+1) minus E_i) minus(K_i+D), intersect{|x|^2>J}. Lower q by the factor b on U. For a fixed h, discard only its original index exceptions and the fixed translated null set E_i minus K_i. A changed point originally has index i+1; an unchanged neighbor cannot have index<=i, since then the point would belong to K_i+D. Its index is i+1 or i+2. Changing the point to i+2 preserves the distance<=1. Both-changed/neither-changed cases and reverse pairs follow directly. Thus the new unnormalized density is feasible at EVERY fixed shift.

It has mass z'>=b>0 and normalized cost difference

```
-(1-b)integral_U(|x|^2-J)q(x)dx/z'.
```

Positive-area U would strictly improve the original optimum. Therefore U is null, and taking essential supports gives

```
K_(i+1) subset (K_i+D) union B_sqrt(J).                 (SAND)
```

For the top set U=E_0 intersect{|x|^2>J}, lowering index0 to1 is also feasible because old neighbors have index0or1. The same exact normalized sign proves K_0 subset B_sqrt(J). The density height alpha is a property of q, not a constraint preventing renormalization.

### 3.3 Simultaneous filling preserves THIS law

FWD and a point of K_0 show union_i K_i=R2. Define m(x)=min{i:x in K_i}, qhat=alpha b^m. FWD and -h give pointwise privacy for EVERY x,h in the closed D. Also qhat>=q a.e.

By SAND and FILL, all holes K_i minus E_i lie in B_sqrt(J) up to a countable union of null sets. Thus rho=qhat-q is nonnegative, bounded by alpha and supported there a.e., with finite mass/moment. Normalizing qhat changes cost by

```
integral_(B_sqrt(J))(|x|^2-J)rho(x)dx/(1+integral rho).
```

If rho had positive mass this would be STRICTLY negative, since the equality circle has area0. Hence rho=0 a.e. and qhat=q as laws, with no normalization change. Each hole is null (on a level-i hole the addition is at least alpha b^i(1-b)). Thus K_i is the essential support of its OWN Lebesgue restriction, with no arbitrary null appendages. We use this SAME-law closed, pointwise-private representative from now on.

## 4. Four separate strict Steiner equalities and canonical geometry

Use the two axis and two diagonal UNIT directions. In axis coordinates D has centered interval fibers; in diagonal orthonormal coordinates it is the centered square of half-side1/sqrt(2). Every one of these four centered-fiber operations fixes D exactly.

For compact A, define S_eA only over its ACTUAL perpendicular projection: a nonempty fiber becomes the centered interval of its length; empty fibers stay empty. Zero-length nonempty fibers become points, not unbounded lines. Fiber length is upper-semicontinuous by reverse Fatou on a common bounded interval; hence S_eA is compact. Fubini preserves area and inclusion is monotone.

For a nonempty compact E in R and d>=0,

```
|E+[-d,d]|=|E|+2d+sum_gaps min(length(gap),2d)>=|E|+2d.
```

The bounded gap sum follows by comparing old/new spans; singleton/zero cases are included. Apply this to a fiber of A and the centered D fiber. It proves EXACTLY

```
S_eA+D subset S_e(A+D).
```

For a fiber of length l, its centered interval uniquely minimizes its u^2 moment: integrate the nonnegative product(u^2-(l/2)^2)(1_E-1_interval). Equal lengths cancel the constant term; equality means equality a.e. The perpendicular-coordinate moment is preserved. Thus M(S_eA)<=M(A), equality iff A=S_eA a.e.

Apply ONE such operation to the WHOLE original level sequence K_i. Exact coupling and nesting survive, its levels cover the plane, and its geometric density is pointwise full-D-private. Area preservation keeps mass1; moment cannot increase. Original optimality forces equality. Each deficit has POSITIVE weight alpha(1-b)b^i, so EVERY level has zero deficit and K_i=S_eK_i a.e.

Repeat SEPARATELY for each of the four directions on the ORIGINAL levels. We do not sequentially replace levels or adopt an averaged optimum. For a reflection or a nonzero contraction in that fiber coordinate, null sets transport under the invertible linear map. The symmetric centered-fiber set is invariant or contains its contraction, so the corresponding equality/inclusion holds a.e. for K_i. Measure-regularity upgrades it exactly: a mapped point outside the closed K_i would have an open preimage neighborhood of positive original area, giving a positive-area failure. Zero contraction follows by closedness.

These exact reflections generate D4. Axis contractions give absolute-coordinate order ideals; diagonal contractions and swap give the ENTIRE segment between(x,y) and(y,x). Each K_i has a positive finite diagonal intercept t_i (positive top area supplies a point off both axes and hence a nondegenerate box). Its first-octant profile F_i is consequently

```
F_i(t_i)=t_i, t_i<=F_i(y)<=2t_i-y,
F_i nonincreasing and1-Lipschitz on[0,t_i].             (CAN)
```

Indeed diagonal contraction gives |z|_1<=2t_i; coordinate contraction gives the lower bound/monotonicity. For y1<y2<=t_i, the segment from(F_i(y1),y1) to its swap contains(F_i(y1)+y1-y2,y2), proving the Lipschitz bound. Convexity has NOT been assumed or obtained yet.

### 4.1 Exact nonconvex parallel geometry at EVERY real offset

For ANY t>=0 and ANY CAN profile F, define S by D4 extension of0<=y<=t,y<=x<=F(y), with S={0} at t=0. Its parallel S+rD has first-octant profile

```
F(y)+r,       0<=y<=t;
2t+r-y,       t<=y<=t+r/2.                             (PAR)
```

Here is a direct proof without convex parallel-body formulas. For target x>=y>=0, reflect and sort a source point into the same octant without increasing L1 distance. The sorting inequality follows because u->|x-u|-|y-u| is nonincreasing for x>=y. Write the sorted source(v,u),0<=u<=t,v<=F(u). Then x<=F(u)+r-|y-u|. For y<=t, Lipschitz gives at most F(y)+r. For y>=t use F(u)+u<=2t to get at most2t+r-y; larger y is impossible since x>=y. Horizontal shifts from(F(y),y) attain the first cap. Shifts from(t,t) attain the second and fill its whole interval. Thus PAR is exact, including all endpoints and all r>=0.

Set

```
A0=8 integral_0^t(F-y)dy,
M0=8 integral_0^t[F^3/3+y^2F-4y^3/3]dy.
```

Direct cap integration gives

```
Area(S+rD)=A0+8tr+2r^2,
Moment(S+rD)=M0+8r integral(F^2+y^2)dy
             +r^2[8 integral Fdy+4t^2]
             +(16/3)tr^3+(2/3)r^4.                    (MOM)
```

For explicit triangular accounting, the new first-octant part is half of a positive-quadrant triangle at(t,t); its moment is t^2r^2/2+tr^3/3+r^4/12. Multiplication by8 plus the old strip's expansion gives MOM. No smoothness, concavity or convexity assumption on F is hidden.

## 5. Cap raising at ORIGINAL optimality forces one global offset

CAN bodies are order ideals in the pair(r=max absolute coordinate,s=sum absolute coordinates). To verify this, sort a point(x,y). A dominated point(u,v) with v<=y follows by coordinate contraction. If v>y, it lies below(x+y-v,v), which is on the segment to the swap; then contract. Thus for x>=y>=0 and canonical H,

```
(x,y)+D subset H iff (x+1,y) in H.                      (ER)
```

Every neighbor has max<=x+1 and sum<=x+y+1, so is dominated by(x+1,y); necessity is the actual boundary shift(1,0).

FWD/PAR give t_(i+1)>=t_i+1/2 and F_(i+1)>=F_i+1 on[0,t_i]. Suppose a strict cap gap occurs. Continuity and t_i>0 supply an INTERIOR height and a point w strictly between these two caps. It lies in K_(i+1) minus(K_i+D), hence in the closed cost ball by SAND. Put z=w-(1,0). The cap bounds give z_x>F_i(y)>=t_i>y, so z is outside K_i, inside K_(i+1), and ER gives z+D subset K_(i+1). Subtracting1 from its larger coordinate STRICTLY lowers squared cost, since w_x>1. All margins persist on a bounded OPEN positive-area U inside the OPEN cost ball, with old index i+1.

Raise q on U to alpha b^i. Each raised source has every old neighbor at least alpha b^(i+1)=b times its new height. An unchanged source stays controlled because neighbors only increased; reverse pairs are included. Thus full pointwise privacy holds BEFORE normalization. The normalized cost change is integral_U(|z|^2-J)rho/(1+integral rho)<0, contradiction. No W or tail comparison was used.

Therefore

```
F_(i+1)(y)=F_i(y)+1 for ALL0<=y<=t_i, ALL i.            (CAP)
```

Define f(y)=F_i(y)-i using any i whose domain contains y. Since t_i>=t_0+i/2, every bounded interval is covered, and CAP makes f well-defined, nonincreasing and1-Lipschitz. Write t=t_0. Then f(t_i)=t_i-i and h(y)=y-f(y) is strictly increasing, with h(t_i)=i.

For x>=y>=0, x-f(y)<=i automatically implies h(y)<=i and y<=t_i. Hence the birth-domain constraint has NOT been discarded, and the CLOSED index is exactly

```
n(x,y)=max(0,ceil(x-f(y))).                             (IDX)
```

For y>=t set g(y)=y-f(y). It is locally AC/bi-Lipschitz, g(t)=0 and1<=g'<=2 a.e. In particular y-t<=g(y)<=2(y-t). For the one-core law generated by S=K_0, PAR gives the SAME raw rows below t and the tail offset2t-y above it, namely g0(y)=2(y-t). This is geometry, not an imported tail-optimality assertion.

## 6. Entire canonical-core class, feasibility and exact formulas

Let W be the infimum of normalized squared cost over ALL CAN cores, including nonconvex profiles and t=0. For such S put u_S=b^min{k:z in S+kD}. Its index is finite/Borel, and membership gives n(z+h)<=n(z)+1 for every closed-D shift, with reverse inequality from-h. Thus its normalized law is originally feasible, V<=W.

The positive layer identity

```
u_S=(1-b)sum_(k>=0)b^k1_(S+kD)
```

and MOM compute its finite positive mass Z and moment N. If G has P(G=k)=(1-b)b^k, then E binom(G,j)=m^j by the geometric series. Falling-factorial expansion gives E G=m and the printed T2,T3,T4. Therefore

```
Z_t(F)=8 integral_0^t(F-y)dy+8tm+2T2,
N_t(F)=(2/3)T4+(16/3)tT3+4t^2T2
 +8 integral_0^t[T2F+m(F^2+y^2)+F^3/3+y^2F-4y^3/3]dy.  (ZN)
```

The point core has Z=2T2,N=(2/3)T4 and cost lambdaP. In particular0<=W<=lambdaP. ONLY this definition/feasibility/ceiling is used in the next lower-bound section; entire-core uniqueness/stationary equations are not assumed there.

## 7. Full inverse-birth lower bound, with a SIGNED term integrated correctly

### 7.1 Actual tail substitution

For k=0,1,2 and s>=0 define

```
A_k(s)=integral_(z>=0) z^k b^ceil(z+s) dz,
R(s,y)=(2y^2-lambda)A_0(s)+2yA_1(s)+A_2(s).
```

For s>0 put j=ceil(s), gamma=j-s. The positive layer formula gives

```
A_k(s)=b^j E(gamma+G)^(k+1)/(k+1),
A_0'=-b^j,
A_1'=-b^j(gamma+m),
A_2'=-b^j(gamma^2+2m gamma+T2)
```

inside a phase. At integer s the A_k are CONTINUOUS: E(G+1)^r=T_r/b for positive r makes adjacent phase values agree. Thus no jump measure is created.

Let Y=g^(-1), Y0(s)=t+s/2 and delta=Y-Y0. The AC inverse theorem gives

```
Y(0)=t, 1/2<=Y'<=1,
delta(0)=0, 0<=delta'<=1/2, 0<=delta(s)<=s/2.
```

For raw tail rows x=y+z, squared cost is2y^2+2yz+z^2. The ACTUAL substitution s=g(y) is

```
I[Y]=integral_0^infinity R(s,Y(s))*Y'(s)ds.             (IB1)
```

The Jacobian is Y', not g'(Y), and no independent extra1/2 is inserted.

### 7.2 Cubic primitive and signed Fubini

Set

```
Q(s,y)=(2/3)A_0 y^3+A_1 y^2+(A_2-lambda A_0)y,
Phi(s,y)=(2/3)y^3+(gamma+m)y^2
                  +(gamma^2+2m gamma+T2-lambda)y.
```

Then Q_y=R and phasewise Q_s=-b^j Phi. All A_k and derivatives are bounded by C b^s, and Y<=t+s. Consequently every term is bounded by an exponentially decreasing polynomial, Q(s,Y(s)) tends to0, and phase-boundary terms telescope by continuity. AC integration by parts yields

```
I[Y]=-Q(0,t)+integral_0^infinity b^ceil(s)Phi(s,Y(s))ds.
```

Put

```
W0(s)=2Y0^2+2(gamma+m)Y0+gamma^2+2m gamma+T2-lambda,
T(u)=integral_(s>=u)b^ceil(s)W0(s)ds.
```

The exact cubic increment and delta(s)=integral_0^s delta'(u)du give

```
I[Y]-I[Y0]
 =integral_0^infinity delta'(u)T(u)du
 +integral_0^infinity b^ceil(s)[(2Y0+gamma+m)delta^2
                                          +(2/3)delta^3]ds. (IB2)
```

This use of Fubini is SIGNED. Its absolute bound is C integral(1+s)^3 b^s ds<infinity, since delta<=s/2 and delta'<=1/2. We do NOT assume W0 is pointwise nonnegative.

### 7.3 Exact phase sum and strictly positive integrated weight

For u>0 set j=ceil(u), gamma=j-u, tau=t+j/2>=1/2, and

```
A(tau)=2tau^2+2m tau+T2-lambda,
Cdiag(tau)=2tau^2+2(1+2m)tau+4m^2+4m+2/3.
```

On the partial phase, Y0=t+s/2=tau-eta/2, so W0=A(tau)+m eta+eta^2/2. Its integral is A(tau)gamma+m gamma^2/2+gamma^3/6. Complete later phase ell has integral A(tau+ell/2)+m/2+1/6. Expanding A(tau+ell/2)=A(tau)+(2tau+m)ell+ell^2/2 and using

```
sum_(ell>=1)b^ell=m,
sum ell b^ell=m(1+m),
sum ell^2 b^ell=m(1+m)(1+2m)
```

gives EXACTLY

```
T(u)=b^j K(tau,gamma),
K=m(Cdiag(tau)-lambda)+A(tau)gamma
                         +(m/2)gamma^2+gamma^3/6.       (IB3)
```

K increases with tau and decreases with lambda. For ANY lambda<=lambdaP, direct boundary expansion gives

```
K(tau,gamma)>=K(1/2,gamma;lambdaP)
 =2m^2(1-gamma)+m(11/6-2gamma+gamma^2/2)
                                      +(gamma+gamma^3)/6
 >=m/3>0,   0<=gamma<=1.
```

The middle bracket decreases to1/3; other terms are nonnegative. Thus T(u)>0 for every positive u. In IB2 all terms are now nonnegative. If delta is nonzero, its AC monotonicity and zero initial value make delta'>0 on a positive-measure set; the first integral is strictly positive. Hence

```
I[Y]>=I[Y0], with equality iff delta is IDENTICALLY0.   (IB4)
```

### 7.4 Conversion to the ORIGINAL all-law infimum

Take an attained original optimum and one optimal geometric phase from Section2. All preceding geometry applies. Let its RAW mass/moment be Z_o,N_o and let S=K_0 have one-core raw mass/moment Z_S,N_S. Use lambda=W, permitted by W<=lambdaP. IDX/PAR say raw rows below t agree. Every octant's remaining signed difference is IB2, so

```
N_o-W Z_o=Z_S(J_S-W)+8*(I[Y]-I[Y0])>=0.                (LB)
```

J_S>=W is the DEFINITION over the ENTIRE canonical class, not a trial-family optimum. Dividing by the ACTUAL positive Z_o gives V>=W. Class inclusion already gave V<=W. Therefore **V=W** without old Hfast/tail-A, a chosen scalar root or a supposed one-core reduction premise. This is an infimum proof via an attained original optimum, not a direct linear dual asserted for every arbitrary density.

For ANY geometric original optimum, LB is now equality. Both terms vanish, IB4 gives Y=t+s/2 and g(y)=2(y-t) everywhere, and IDX/PAR imply

```
K_i=K_0+iD for EVERY i; its core law attains W.         (EQ)
```

This alone does not yet identify all minimizing cores. That entire-class uniqueness is proved next, independently of Section7's original-class equality.

## 8. Entire-class CAL proved from ZN, not imported

### 8.1 Exact functional clipping and attained minimum

For fixed t,lambda, H=N-lambda Z has F-derivative

```
F^2+2mF+T2+y^2-lambda,
```

with strictly positive second derivative2(F+m). Its pointwise clipped minimum is

```
R_lambda(y)=sqrt(max(lambda-v-y^2,0))-m,
F_(t,lambda)=min(2t-y,max(t,R_lambda(y))).               (CLIP)
```

This is feasible in the WHOLE CAN class: the clipped root is nonincreasing, and where it exceeds t its absolute slope is at most y/(t+m)<=1; the other pieces preserve1-Lipschitzness and the endpoint t. Thus CLIP is exact strict functional minimization, not stationarity in a selected family.

Every core contains[-t,t]^2, so N>=8t^4/3, while Z<=8t^2+8tm+2T2. For t>=m,sqrt(T2), its cost is at least4t^2/27. A bound

```
A=m+sqrt(T2)+sqrt(27lambdaP/4)+1
```

therefore contains every core of cost<=lambdaP. H(t,lambda) at CLIP is continuous on[0,A], including t0. Its minimum is continuous and strictly decreasing in lambda: Z>=2T2 makes a lambda increase h lower the minimum by at least2T2*h. At lambda=0 it is positive; at lambdaP the point core gives0. Its unique zero is exactly W, attained by an actual core; no smaller cost is hidden outside[0,A].

The positive-end assertion uses N_t(F)>=(2/3)T4 for every t,F, so min_t H(t,0)>=(2/3)T4>0.

### 8.2 Strict value interval and positive top size

For diamond core gamma D,

```
J_D(gamma)=(1/3)E(G+gamma)^4/E(G+gamma)^2.
```

The gamma1 law is the point-core law a.e. At gamma1, E(G+1)^r=T_r/b for positive r, and

```
2T2*T3-m*T4=m^2(1+2m)>0.
```

Thus J_D'(1)>0; moving gamma below1 strictly improves lambdaP. Hence W<lambdaP and t_*>0.

If lambda<=T2, CLIP is F=t. At lambda=T2 direct substitution gives

```
H=(2/3)T4-2T2^2+[(16/3)T3-8mT2]t
                 +8T2t^2+(32/3)mt^3+(8/3)t^4>0.
```

The constant uses T4-3T2^2=m+11m^2+24m^3+12m^4>0; the linear coefficient is16m/3+24m^2+16m^3>0. Smaller lambda only increases H. Therefore W>T2.

The Laplace density's phases in Section2 have cores gamma D,0<gamma<=1, up to null boundaries, so are canonical class laws. Their exact average cost is4/epsilon^2. This independently gives W<=4/epsilon^2, without using V=W for the class calculation.

### 8.3 No lower clipping; convexity is a conclusion

Dominated difference quotients at CLIP give

```
H_t=(16/3)T3+16tT2+16mt^2-8lambda m
 +8 integral_(R<t)[t^2+2mt+T2+y^2-lambda]dy
 +16 integral_(R>2t-y)[(2t-y)^2+2m(2t-y)+T2+y^2-lambda]dy. (HT)
```

The upper-limit term at F(t)=t is included. Switching equalities have only finitely many y; equal boundary integrands and bounded local clip derivatives give continuous matching one-sided derivatives. No nonsmooth corner minimum is omitted.

Lower and upper clipping cannot coexist. On R>=t the function R(y)+y is increasing, since its root denominator is at least t+m>y. If R(t)<=t there is no upper clip; otherwise there is no lower clip. In the former regime lambda<=2t^2+2mt+T2, HT's base is at least

```
(16/3)T3-8mT2+16t(T2-m^2)>0,
```

and its lower integral is nonnegative. The positive attained minimum of H(t,W) cannot lie there. Thus

```
W>2t_*^2+2mt_*+T2.
```

The optimum is an arc followed by a NONZERO upper facet, or the full facet, and its core is exactly the S_* in Section1. It is convex as the intersection of a diamond and the convex sublevel of |z|^2+2m|z|_infinity. It lies STRICTLY in the cost ball |z|^2<W because T2>0. Initial convexity was never imposed.

### 8.4 Global uniqueness of the entire-core minimum

Fix lambda in(T2,lambdaP). Successive t regimes are full upper clip, rounded arc/upper facet, then lower clip. Their boundaries are

```
t_D=(sqrt(lambda-v)-m)/2,
2t_U^2+2mt_U+T2=lambda.
```

For the diamond regime, put x=2t+m and c3=T3-3mT2+2m^3=m+3m^2+2m^3>0. Then

```
H_D=(2/3)E(G+2t)^4-2lambda E(G+2t)^2,
H_D'/8=(2/3)x^3+(2v-lambda)x+(2/3)c3.                 (DC)
```

This cubic is strictly convex for x>0, with at most two positive zeros and sign pattern+,-,+ when both occur. At t0 it is positive even at lambdaP, by the identity in8.2. Hence the diamond regime has at most one positive local MINIMUM. A preceding maximum cannot have value below H(0,lambda)>0.

In the rounded regime write c for the junction and d=t-c in(0,t). The junction is

```
lambda=2t^2+2d^2+2m(t+d)+T2.
```

With u=t-y the upper integrand in HT is2(u^2-d^2)+2m(u-d); its integral is-4d^3/3-md^2. Therefore

```
H_t/16=C0+t v-P(d),
C0=T3/3-mT2/2=m/3+(3/2)m^2+m^3>0,
P(d)=(4/3)d^3+2md^2+m^2d,
d'=-(2t+m)/(2d+m),
H_tt=16[v+(2d+m)(2t+m)]>0.                            (RC)
```

The derivative matches DC at c0 and is positive at d0. If a diamond minimum has already occurred, its derivative stays positive to the junction and then increases; otherwise the rounded regime can contain at most one minimum. The remaining lower regime has positive derivative. Thus H has at most ONE positive local minimum capable of lying below H(0,lambda).

At lambda=W, H(0,W)>0 and its attained positive minimum is0. That minimum is therefore UNIQUE. Strict fixed-t functional minimization then makes the ENTIRE canonical optimal core unique, not just a stationary arc/facet trial solution.

Its terminal width d, with d=t in the diamond case, is strictly<1/2. If d>=1/2 set t'=t-1/2,F'=F-1 on[0,t']. The old terminal facet contains t', so F'(t')=t', and all CAN bounds hold. PAR proves S=S'+D EXACTLY. If t'>0,

```
u_(S')=(1-b)1_(S')+b u_S.
```

Because S' has positive area and is inside the STRICT cost ball, its normalized cost is lower than W, contradiction. If t'=0, S=D is the excluded point-core law. This is an ACTUAL class competitor, not an assumption of original one-core optimality. Hence0<d<1/2.

### 8.5 Exact globally screened scalar systems

No optimization over an unknown function or an unevaluated outer minimum is needed in the final characterization. Put

```
M1(q)=q+m,
M2(q)=q^2+2mq+T2,
M3(q)=q^3+3mq^2+3T2q+T3,
M4(q)=q^4+4mq^3+6T2q^2+4T3q+T4.
```

**D branch:** q=2t in(0,1), lambda in(T2,lambdaP),

```
P_m(q)=2M3(q)M2(q)-M4(q)M1(q)=0,
lambda=M4(q)/(3M2(q)),
lambda>=q^2+2mq+T2.
```

Direct finite multiplication gives

```
P_m(q)=q^5+5mq^4+(2m+12m^2)q^3+(12m^3-2m)q^2
        -(m+8m^2+12m^3)q+m^2+2m^3.                    (D)
```

This is a stationarity polynomial with GLOBAL screens, not a new minimal-polynomial/Galois claim. The screens put CLIP in its true diamond regime.

**R branch:**0<d<1/2, t(d)>d, lambda(d) in(T2,lambdaP), where

```
t(d)=[P(d)-C0]/v,
lambda(d)=2t(d)^2+2d^2+2m(t(d)+d)+T2,
c=t-d, A=lambda-v, w=2t.
```

Solve ONE elementary scalar equation H_R=0, with

```
J3(A,c)=[c sqrt(A-c^2)(5A-2c^2)+3A^2 arcsin(c/sqrt A)]/8,
Rint=-(2/3)J3+(mA-m^3/3)c-c^4/3+lambda c^2/2,
Uint=[w^3/3+mw^2+(T2-lambda)w]c
    +[-w^2-2mw+2lambda-T2]c^2/2
    +(2/3)(w+m)c^3-(2/3)c^4,
H_R=H_D+8(Rint-Uint).                                 (R)
```

These primitives follow by substituting CLIP into H: the free integrand is-(2/3)(A-y^2)^(3/2)+mA-m^3/3-(4/3)y^3+lambda y; the upper one is a polynomial in y. J3 follows from y=sqrt(A)sin(theta) and cos^4. A-c^2=(t+d+m)^2>0, so the principal arcsin is unambiguous.

Every screened stationary value0 is the unique positive minimum, not the earlier positive local maximum, by8.4; hence it is the unique global zero defining W. Conversely attainment supplies one of D/R. At c0 the same core is represented by the D boundary, not a second law. This gives the exact finite-b value lambda_* and core parameters without numerical root conventions or an elementary-inverse assertion.

For explicit normalization set J1(A,c)=[c sqrt(A-c^2)+A arcsin(c/sqrt A)]/2. In the rounded case,

```
Z_*=8[t^2-2tc+c^2/2+J1(A,c)-mc]+8tm+2T2.
```

At c0 this is the diamond normalizer2M2(2t). No fine rational bracket, old evaluated table or polynomial-remainder output is used.

## 9. ALL geometric optimizers, then ALL original laws

Return to ANY original geometric optimizer. Section7 gives EQ and its ACTUAL K_0 law attains W. Section8's uniqueness over the ENTIRE canonical class therefore identifies it with the SAME law mu_*, and unit mass fixes alpha=1/Z_*. No amplitude or null-set core description freedom creates a different law.

Now let p be ANY original optimal density; it need not be symmetric/geometric/continuous. PH's nonnegative cost gap has integral0, so one full-weight set G of phases, defined only by J(q_a)=V, consists of optimal geometric laws. The preceding universal argument makes q_a=mu_* as LAWS for EVERY a in G. G does not depend on a Borel event.

For arbitrary Borel E, joint measurability and PH yield

```
mu(E)=integral_(bM)^M q_a(E)Z_a/(1-b)da
     =mu_*(E)integral_(bM)^M Z_a/(1-b)da=mu_*(E).
```

There is no uncountable intersection of event-wise density exceptions, and no need for a jointly selected family of regularized representatives. The good set was a scalar-cost set, and each member's LAW was identified universally. This proves the singleton optimizer statement for ALL original Borel laws.

## 10. What trust cut this body closes, and what it does NOT accept

The problem-specific analytical chain is now presented without treating S/C/X/A/B-geometry or CAL as opaque research theorems:

- all-law density/attainment/phase mixture: Section2;
- same-law compact regular closed levels and cost-ball coupling: Section3;
- all FOUR ORIGINAL-level strict Steiner equalities, without averaging: Section4;
- nonconvex full-offset cap/area/moment and full-D erosion: Sections4–5;
- cap raising/global offset before W: Section5;
- positive signed inverse-birth lower bound and equality: Section7;
- ENTIRE class attainment/unique minimum/screens: Section8;
- all-original-law uniqueness: Section9.

Finite-head cutoffs, the older coupled finite-parameter selector theorem, Hfast/tail-A and numerical/Galois/transcendence computations are not needed for THIS analytical proof. Their old records/qualifications remain unchanged, not deleted or retrospectively made formal. In particular frozen kernel-labelled numerical material remains unadmitted; this body does not turn it into executed verification.

This is a SAME-AUTHOR complete supplied proof, NOT a fresh independent review. Until a separate complete-body reconstruction and explicit parent adoption, all new dependency-closure claims remain AUTHOR WRITTEN CANDIDATE. No stronger configured-family/human/formal/kernel/executable or source/novelty acceptance follows from having the argument in one file.

The mathematical target is exactly the owner-authorized modern planar subquestion, not the entire broad book article. The source/priority gate remains genuinely open: known shell, density/attainment, generic symmetrization and comparison principles are PRIOR; the matched2025/2026 radial theorems have different objective hypotheses but that is not a world-wide non-equivalence proof. No new mechanism invention, publishability/major-result or first-in-literature claim is made. The bounded source/corpus refresh is not exhaustive specialist clearance.

Original privacy-primary registration,18-owner/window identity and cutoff/deadline remain. No auxiliary cactus claim is a premise or a new primary. Mandatory v9/v10/v11/HOLD and the1049clarification remain binding. Only written reasoning, source reads and clock/hash metadata were used; no scientific program/interpreter/eval/symbolic calculation/enumeration/solver/replay/compile/kernel/buildtest, nested agent, external model CLI/contact/publication, Git/deletion/config/shared-root write or new GO. All frozen predecessor bytes remain intact. Delivery of this candidate is not completion of the96-hour request or evidence of continuous activity.
