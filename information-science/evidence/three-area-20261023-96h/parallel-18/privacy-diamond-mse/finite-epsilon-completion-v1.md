# Finite-epsilon completion: exact branch algebra, a unique optimal law, and an inverse-birth lower bound

Actual `/bin/date` observation before creation: **Sun Oct 25 03:56:45 PDT 2026**.

## 0. Status and precise deliverable

**NEW AUTHOR WRITTEN CANDIDATE; new claims are NOT covered by the predecessor's parent acceptance.** This is an additive successor to `privacy-global-optimum-consolidated-v1.md`, SHA-256 `e11b53b6e177caaf11d26f86c42531d0600d60f76ecdce3db7e0e8b7caa91821`. No pinned source is edited.

For the original additive-noise problem, at every finite epsilon>0, this manuscript supplies:

1. An explicit generic minimal quintic for the diamond parameter, an algebraic privacy-phase transition, and exact rational root/value enclosures. The diamond inverse is generically NOT expressible by radicals: already b=1/2 gives Galois group S5.
2. A rational-polynomial/arctangent form for the rounded equation, a strictly monotone isolation procedure, and a necessary correction to the requested algebraic premise: **at every positive algebraic m in the rounded regime, its parameter and optimal value are transcendental. They have no minimal polynomial over Q(m), and cannot be expressed by radicals over that field.** This is a proved obstruction, not an unevaluated claim that an elementary inverse is impossible.
3. A classification of ALL original optimal Borel probability laws: **there is exactly one optimal law**, with the density already constructed in the predecessor, up to Lebesgue-null changes of density version.
4. A second analytical lower-bound slice V>=W1, using inverse birth coordinates and an exact nonnegative Stieltjes/cubic gap. It does not use the old Hfast potential, its control-state verification, the tail-A conclusion, or the already composed equality V=W1. It DOES share the explicitly named structural B-geometry imports. Thus it is not a second independent proof of those imports, nor a blind or different-author review.

**Scope labels.** `WRITTEN` below means ordinary supplied-proof mathematics with the stated imports. `WRITTEN-checked-in-kernel` is used only for the declared finite integer/Fraction identities and enclosures, not for a proof-assistant kernel. No formal, human, cross-model, novelty, worldwide-priority, nonadditive-channel, or broad book-article conclusion is asserted.

## 1. Model and named imports

Set

```
D={h in R^2: |h1|+|h2|<=1},
b=exp(-epsilon) in (0,1),
m=b/(1-b), v=m+m^2,
T2=m+2m^2,
T3=m+6m^2+6m^3,
T4=m+14m^2+36m^3+24m^4,
lambdaP=T4/(3T2)=4m^2+4m+1/3.
```

The original feasible set consists of ALL Borel probability laws satisfying

```
mu(E)<=b^(-1)mu(E+h)
for every Borel E and EVERY h in the FULL CLOSED diamond D.
```

The objective is integral |z|_2^2 dmu(z), and its infimum is V. This is the query-output-independent additive-noise model, not all data-dependent DP channels.

### Frozen mathematical imports

All root-relative sources in this table are in this owned directory; B is in the AME owner's read-only root. Their hashes were observed directly in this continuation.

| Name | Source and SHA-256 | Exact import used here |
|---|---|---|
| S | `proof-coupled-level-tail-saturation-v1.md` — `ae1e05470b233d2e51a3c56f45a58ab97ecd249a5ed479dc33c6d29ae4ea3958` | Every feasible law has a bounded positive a.e. density; original attainment; exact positive amplitude mixture; compact essential supports, forcing and cost-ball sandwich for any geometric optimizer. |
| C | `proof-coupled-level-tail-ADDENDUM-1-closed-levels.md` — `87320046a2396eb936138af7c3eb3122a5e3451140a70171dce73cb270fd5596` | Simultaneous filling leaves the SAME geometric optimal law unchanged, gives measure-regular compact closed levels and pointwise full-D privacy; R7 actual backward raising. |
| X | `proof-coupled-level-tail-ADDENDUM-2-coordinate-Steiner.md` — `15a4d1eda329a5f8eb22207c8fce9750f906d5f3cba8d290a65bde5426c29007` | Whole-level Steiner operation, exact Minkowski feasibility, positive layer weights, strict centered-fiber moment equality, support transport. Its optional preliminary group averaging is NOT used here. |
| A | `proof-coupled-level-tail-ADDENDUM-3-diagonal-Steiner.md` — `6da3be079457f4558a32d422c04185e01e0f996fccfe6719152da2c53f55ad36` | Diagonal Steiner operation; canonical profiles and exact nonconvex Minkowski cap formula. |
| CAL | `outer1-entire-one-core-minimum-calibration-v1.md` — `7c615bb1b645c1a77a20354efd7798cd5ff8836b3eb72e0a3223994f076a7a89` | Entire canonical one-core class W1; attained unique canonical core; T2<W1<lambdaP; screened D/R systems; strict fixed-profile minimization. No original all-law equality is imported for the new lower-bound proof. |
| G | B review, `physics/evidence/three-area-20261023-96h/parallel-18/ame46-support/peer-review-privacy-OUTER1-all-law-bridge-v1.md` — `f742f3ebfda9c00db2289b847a1ef2054636f5e34ee6cc3b2b80390aba80ac53`, Sections4–7 | For a geometric original optimum already having the simultaneous canonical properties: R7 forces exact common-cap increments; one global offset f and exact ceiling index; all birth constraints; genuine one-core raw-row agreement and full-D feasibility. The conditional tail-A splice in Section8 is NOT consumed. |

The predecessor and parent consolidated/equality/source-boundary dispositions retain their existing component-level WRITTEN_SUPPORTED status. The universal quantifiers and lower-bound argument proved here are NEW, not backdated into those dispositions.

Named standard imports are also explicit: Tonelli/Fubini and absolute-integrability interchange; change of variables and chain rule for bi-Lipschitz absolutely continuous functions; essential-support regularity; the one-dimensional strict centered-interval second-moment principle; Descartes' rule; Gauss' lemma and monic specialization; finite-field polynomial gcd/irreducibility; the Frobenius factorization theorem for square-free prime reduction; elementary Galois specialization and primitive permutation groups; and the classical Lindemann theorem that exp(alpha) is transcendental for nonzero algebraic alpha. These standard theorems are not new research claims and were not formally replayed.

## 2. Diamond branch: minimal polynomial and exact phase split

### 2.1 The explicit quintic

**Claim D1 — WRITTEN, imports CAL and elementary moment algebra; displayed polynomial expansion WRITTEN-checked-in-kernel.** Put q=2t and let

```
Mj(q)=E(G+q)^j,  P(G=k)=(1-b)b^k, k>=0.
```

Here Mj uses q rather than the predecessor's argument t. Thus

```
M1=q+m,
M2=q^2+2mq+T2,
M3=q^3+3mq^2+3T2q+T3,
M4=q^4+4mq^3+6T2q^2+4T3q+T4.
```

The stationarity equation is exactly P_m(q)=0, where

```
P_m(q)=q^5+5mq^4+(2m+12m^2)q^3+(12m^3-2m)q^2
       -(m+8m^2+12m^3)q+m^2+2m^3.                 (D1)
```

There are exactly TWO positive roots, both in (0,1), counted without multiplicity. Write q_+(m) for the larger. To see the root selection without a numerical convention, the normalized diamond cost is

```
J_D(q)=(1/3) M4(q)/M2(q),
J_D'(q)=(2/3)P_m(q)/M2(q)^2.
```

Its endpoint costs satisfy J_D(0)=J_D(1)=lambdaP, and both endpoint derivatives are positive, by `2T2*T3-m*T4=m^2(1+2m)>0` and geometric reindexing at q=1. Hence the derivative is negative somewhere between them. In (D1), the descending coefficient signs have exactly two changes, regardless of the sign or vanishing of the q^2 coefficient. Descartes therefore permits only two positive roots counting multiplicity. The positive/negative/positive signs just proved force two distinct simple roots in (0,1). The larger is the unique positive local minimum and varies continuously with m>0.

Its cost is

```
lambda_+(m)=(2/3)M3(q_+)/M1(q_+)=J_D(q_+).        (D2)
```

It lies strictly between T2 and lambdaP: CAL gives W1>T2 and W1<=J_D(q_+), while the endpoint derivative at q=1 gives strict improvement below lambdaP.

The sole remaining diamond screen is

```
C_m(q_+):=2M3(q_+)-3M2(q_+)M1(q_+) >=0,
C_m(q)=-q^3-3mq^2+3mq+2m+9m^2+6m^3.             (D3)
```

This is exactly `lambda_+>=M2(q_+)`, not an optional shape condition.

### 2.2 The privacy-phase transition is an algebraic cubic

**Claim D2 — WRITTEN, imports D1, CAL, continuity/Descartes; reduction identity and rational endpoint signs WRITTEN-checked-in-kernel.** There is exactly one positive v_c solving

```
2592v_c^3+864v_c^2+18v_c-1=0.                    (D4)
```

Set `m_c=(sqrt(1+4v_c)-1)/2` and `b_c=m_c/(1+m_c)`. Then, for EVERY finite epsilon:

```
m>=m_c  (equivalently b>=b_c): diamond branch D;
0<m<m_c: rounded branch R.
```

At equality the two descriptions give the SAME full diamond and the rounded free arc has zero length; it is counted once.

Here is the exact elimination. Put x=q+m and c3=v(1+2m). In these variables,

```
Ptilde=x^5+2vx^3-2c3x^2-(v+3v^2)x+2vc3,
Ctilde=-x^3+3vx+2c3,
Ptilde+(x^2+5v)Ctilde=v[(12v-1)x+12c3].         (D5)
```

A simultaneous zero with x>0 forces v<1/12 and `x=12c3/(1-12v)`. Substitution into Ctilde=0 gives exactly (D4). Its derivative is positive for v>=0 and it changes sign between 0 and 1/12, so it has one positive root.

For orientation, at m=1, C_m(q)>13 on (0,1). At m=1/100 the following exact checks isolate q_+ between 33/100 and 34/100:

```
P_(1/100)(33/100)=-374289/1000000000,
P_(1/100)(34/100)=25041/156250000.
```

Throughout that interval,

```
C_(1/100)(q) <= -(33/100)^3+(3/100)(34/100)
                +2/100+9/10000+6/1000000
             = -4831/1000000 <0.
```

Continuity of q_+ and the unique possible simultaneous-zero parameter now prove the sign split globally. CAL's globally screened alternatives identify the sign-nonnegative case as D and its complement as R. This does not infer the phase from a sampled numerical plot.

Strict rational transition enclosures are

```
245348357/10^10 < v_c < 245348358/10^10,
239607196/10^10 < m_c < 239607197/10^10.
```

### 2.3 Minimality and the obstruction to radicals

**Claim D3 — WRITTEN, imports D1, Gauss/monic specialization, finite-field irreducibility and the named Galois/group theorems. Finite modular arithmetic and resultant coefficients are WRITTEN-checked-in-kernel.** Over Q(m), (D1) is the generic minimal polynomial of q_+. At the concrete admissible parameter m=1, it specializes to

```
f(q)=q^5+5q^4+14q^3+10q^2-21q+3.                (D6)
```

Its reduction modulo17 has ascending coefficients `[3,13,10,14,5,1]`. Exact modular arithmetic gives

```
x^17 mod f  =8+6x+12x^2+5x^3+6x^4,
x^289 mod f =2+2x+x^2+3x^3+x^4,
gcd(f,x^17-x)=gcd(f,x^289-x)=1  in F17[x].
```

A reducible quintic has a factor of degree1 or2, so these gcds prove irreducibility. Consequently f is irreducible over Q. Since (D1) is monic in q, a factorization over Q(m) would give monic positive-q-degree factors over Q[m] and hence a nontrivial factorization at m=1. This proves its generic minimality. At a particular algebraic specialization m, the minimal polynomial is the irreducible factor of the specialized polynomial selected by its exact root interval; generic irreducibility is not asserted at every specialization.

Modulo13 the factorization is

```
f=(x^2+x+8)(x^3+4x^2+2x+2).
```

The quadratic has nonsquare discriminant8 modulo13. The cubic's values at x=0,...,12 are respectively

```
2,9,4,6,8,3,10,9,6,7,5,6,3,
```

so it has no root. The factors are distinct irreducibles. Frobenius therefore supplies cycle type(2,3), whose cube is a transposition. Irreducibility makes the Galois group transitive of prime degree5, hence primitive. A primitive group containing a transposition is S5: the graph of conjugate-transposition edges has invariant connected-component blocks; primitivity makes it connected, and its edge transpositions generate S5. Thus the admissible m=1 root is NOT expressible by radicals. Good separable specialization also forces the generic Galois group over Q(m) to be S5. A universal radical inverse in m is therefore unavailable.

For completeness the actual optimal VALUE at m=1 has minimal polynomial

```
243L^5-4131L^4+20952L^3-62064L^2+374400L-778816. (D7)
```

The Sylvester resultant of (D6) and

```
3L(q+1)-2(q^3+3q^2+9q+13)
```

is -24 times (D7). Its degree is at most5 in L, and six exact rational determinant evaluations recover every coefficient. Moreover Q(q) has prime degree5; L is not rational, since a rational L would make q satisfy the displayed cubic. Hence Q(L)=Q(q), proving minimality of (D7) and the same obstruction to radicals for the value itself.

## 3. Rounded branch: an exact arctangent root, not an algebraic number

### 3.1 Removing the square root from the root equation

**Claim R1 — WRITTEN, imports CAL and elementary identities.** Retain the predecessor's definitions

```
C0=T3/3-m*T2/2=m/3+(3/2)m^2+m^3,
P(d)=(4/3)d^3+2md^2+m^2d,
t(d)=[P(d)-C0]/v,
L(d)=2t(d)^2+2d^2+2m(t(d)+d)+T2,
c=t-d, U=t+d+m, a=L-v, w=2t.
```

On the genuine rounded domain, `0<d<1/2`, `c>0`, and `T2<L<lambdaP`. The junction identity gives

```
a=U^2+c^2, sqrt(a-c^2)=U>0,
arcsin(c/sqrt(a))=arctan(c/U), 0<c/U<1.
```

Define the rational expression

```
Aint=[w^3/3+mw^2+(T2-L)w]c
     +[-w^2-2mw+2L-T2]c^2/2
     +(2/3)(w+m)c^3-(2/3)c^4,
B=(2/3)M4(w)-2L*M2(w)
  -(2/3)cU(5a-2c^2)
  +8[(ma-m^3/3)c-c^4/3+L*c^2/2-Aint].
```

Here `Mj(w)=E(G+w)^j`, following Section2's shift convention. The scalar equation is exactly

```
F_m(d):=B(m,d)-2a(m,d)^2 arctan(c(m,d)/U(m,d))=0. (R1)
```

Everything except the single arctangent is rational in m,d. There is no quadrature, square-root branch ambiguity, or unselected polynomial root.

### 3.2 Strict monotonicity and exact rational isolation

**Claim R2 — WRITTEN, imports CAL, R1 and envelope differentiation; finite endpoint evaluations WRITTEN-checked-in-kernel.** On the admissible rounded interval,

```
t'(d)=(2d+m)^2/v>0,
L'(d)=(4t+2m)t'(d)+4d+2m>0,
F_m'(d)=-Z(t(d),L(d))*L'(d)<0.                  (R2)
```

Indeed t(d) imposes the exact outer stationarity H_t=0, while H_L=-Z for the pointwise-minimized signed numerator. Thus chain-rule differentiation gives (R2); Z>0 is the ACTUAL normalizer, not a sampled denominator.

For rational r in (0,1), let

```
S_N(r)=sum_(k=0)^(N-1) (-1)^k r^(2k+1)/(2k+1).
```

The alternating-series theorem gives strict rational enclosures

```
S_(2n)(r) < arctan(r) < S_(2n+1)(r).
```

At rational m,d all other quantities in (R1) are rational, so these give certified rational lower/upper bounds for F_m(d). Enumerate rational admissible endpoints until a positive-left/negative-right pair is found, then bisect. Strict monotonicity and the interior existence supplied by CAL for m<m_c make this terminate to any prescribed rational width. If a midpoint's sign is unresolved, increase n; no floating arithmetic or numerical quadrature is needed.

For clarity the admissible domain is an interval: `c(d)>0` holds above the unique positive root d0 of

```
(4/3)d0^3+2m*d0^2-m*d0-C0=0.
```

Its left side starts negative and has strictly increasing derivative after its one positive derivative zero. Above d0, t>d>0, L>T2 automatically and L is strictly increasing; L<lambdaP supplies at most one upper endpoint, together with d<1/2. Therefore sign-bracketing cannot accidentally select a disconnected branch.

For algebraic m the same procedure uses exact ordered algebraic arithmetic for the coefficients and the same alternating arctangent bounds; that general algorithm was not executed here. For an arbitrary real input m, (R1), (R2), the exact phase criterion, and the unique admissible zero remain a valid exact mathematical characterization. Effective rational computation requires an effective certified representation of that input real; no algorithm can promise such data for an unspecified noncomputable real.

### 3.3 Why a rounded minimal polynomial cannot be supplied

**Claim R3 — WRITTEN, imports R1 and the classical Lindemann theorem.** Suppose m>0 is algebraic and lies in the rounded regime. Then its admissible root d, t(d), c(d), and optimal value L(d) are all transcendental over Q, and hence d has no minimal polynomial over Q(m).

If d were algebraic, all of t,c,U,a,B would be algebraic. Equation(R1) would make

```
theta=arctan(c/U)=B/(2a^2)
```

a NONZERO algebraic number. But

```
exp(2i*theta)=(U+i*c)^2/a
```

would then be algebraic, contradicting Lindemann because 2i*theta is nonzero algebraic. Thus d is transcendental. The functions t(d) and c(d) are nonconstant cubic polynomials in d with algebraic coefficients, and L(d) is a nonconstant degree-six polynomial with algebraic coefficients. If any of their values were algebraic, d would satisfy a nonzero polynomial over the algebraic numbers and would itself be algebraic, the same contradiction.

In particular no radical expression over algebraic m and algebraic constants can yield these numbers. This excludes an algebraic/radical inverse; it does NOT establish that every conceivable elementary transcendental formula is impossible. A local algebraic-function formula over Q(m) for a rounded branch would also specialize at some algebraic m in its open interval to an algebraic d, so such a formula is impossible. The exact replacement for a nonexistent minimal polynomial is the monotone analytic root plus rational isolation, not a fabricated algebraic equation.

### 3.4 Exact finite tables

**WRITTEN-checked-in-kernel, exact finite scope only.** The separately frozen `finite-epsilon-exact-tables-v1.json`, SHA-256 `16dd75b44ce298e875c5bd046318a94fc19a0b20d299f99190ad10cecf5ad274`, records endpoint residual enclosures, all branch screens, finite-field certificates, and methods. The following table abbreviates its strict intervals. Each parameter interval has the stated COMMON denominator; each cost interval has common denominator10^6. For D the parameter is q=2t, not t.

| m | b | Branch and parameter | Strict parameter numerator interval /10^8 | Strict V numerator interval /10^6 |
|---|---|---|---|---|
| 1 | 1/2 | D, q | (72710251,72710252) | (8304606,8304607) |
| 1/2 | 1/3 | D, q | (68776254,68776255) | (3282438,3282440) |
| 1/10 | 1/11 | D, q | (55167224,55167225) | (638155,638156) |
| 1/100 | 1/101 | R, d | (15234146,15234147) | (120316,120317) |
| 1/1000 | 1/1001 | R, d | (6818582,6818583) | (29497,29498) |
| 1/10000 | 1/10001 | R, d | (3071909,3071910) | (8035,8036) |

Every R endpoint used the 24-term lower and25-term upper arctangent sums. D signs are negative-left/positive-right for P_m; R signs are positive-left/negative-right for F_m. All cost bounds are rational OUTER enclosures, not rounded binary output. Three exact R parameter/value instances are consequently certified transcendental by ClaimR3, even though their strict rational brackets are finite.

## 4. Universality of the geometric imports, without preliminary averaging

**Claim U1 — NEW WRITTEN universality lemma, imports S,C,X,A and the strict interval equality principle.** Let q be ANY geometric-valued original optimal density, normalized to unit mass, with positive-area top plateau. Then the SAME closed levels supplied by C are canonical D4 levels. No group averaging and no choice of a different optimizer is necessary.

Write

```
q=alpha*b^n,
K_i={n<=i} in the C closed representative,
K_i+D subset K_(i+1),
q=alpha*(1-b)*sum_(i>=0)b^i*1_(K_i).
```

The K_i are compact and measure-regular, and every layer weight is strictly positive. For EACH direction e equal to an axis direction or a diagonal direction, apply Steiner S_e to the ENTIRE original sequence. All four such directions have centered interval fibers of the ACTUAL sensitivity diamond, so

```
S_e(K_i)+D subset S_e(K_i+D) subset S_e(K_(i+1)).
```

The transformed levels cover the plane, preserve every area, and define a genuinely full-D-private density with the SAME normalizer. Its quadratic moment is no larger. Original optimality forces equality of the total moment. All individual weighted deficits are nonnegative, so each K_i separately has zero deficit. Strict one-dimensional fiber equality gives

```
K_i=S_e(K_i) a.e. for every i and each of the four directions.
```

This argument is applied separately to the ORIGINAL sequence for each e; it does not sequentially replace levels and assume an earlier equality survived.

Reflection in e and every nonzero contraction in e preserve null sets. The centered-fiber representative is invariant under the reflection and contains its contractions. Thus the corresponding a.e. inclusions hold for K_i. Measure-regularity upgrades each inclusion to an exact one: an image point outside the closed K_i has an open preimage neighborhood carrying positive original area, and invertibility gives a positive-area violation. Zero contraction follows by closedness. Consequently the ORIGINAL levels have the axis and diagonal reflections and contractions simultaneously. Axis reflections plus a diagonal reflection generate D4. The standard A profile argument now gives, at each diagonal intercept t_i>0,

```
F_i(t_i)=t_i, t_i<=F_i(y)<=2t_i-y,
F_i nonincreasing and 1-Lipschitz.
```

This is the missing quantifier extension: S and C apply to any geometric optimizer, while X/A's feasible whole-sequence operation and strict equality apply without a symmetry assumption. Initial averaging was only an existential convenience in the frozen construction.

**Claim U2 — WRITTEN application of the SHARED G import, not a second proof of G.** The G Sections4–6 cap/R7 lemma applies to ANY optimal sequence satisfying the properties just proved and the S/C cost-ball sandwich. Its proof uses actual original optimality, the full-D erosion test, and open positive-area improvement; none of its hypotheses requires an earlier averaging choice. Therefore every such q has

```
F_(i+1)(y)=F_i(y)+1 on every old domain,
f(y)=F_i(y)-i whenever y<=t_i,
n(x,y)=max(0,ceil(x-f(y))) for x>=y>=0.
```

For t=t_0 and y>=t, set g(y)=y-f(y). Then

```
g(t)=0, 1<=g'<=2 a.e.,
g is bi-Lipschitz on [t,infinity),
y-t<=g(y)<=2(y-t).
```

The raw one-core law generated by S=K_0 agrees with the raw original law for y<=t and has g0(y)=2(y-t) above t. This consumes ONLY G's structural export, not its conditional tail splice or any equality conclusion. This is exactly the shared import boundary for the second lower-bound slice below.

## 5. Independent second analytical lower bound: inverse birth coordinates

### 5.1 The new representation and its exact signed identity

**Claim L1 — NEW WRITTEN, imports U2/G, geometric moments, bi-Lipschitz AC change of variables, Tonelli/Fubini with the bounds below.** Fix ANY lambda<=lambdaP. In the first octant x=y+z, define

```
A_k(s)=integral_(z>=0) z^k b^ceil(z+s) dz, k=0,1,2,
R_lambda(s,y)=2y^2*A_0(s)+2y*A_1(s)+A_2(s)-lambda*A_0(s).
```

For s>0 let j=ceil(s), gamma=j-s. Geometric layers give

```
A_k(s)=b^j E(gamma+G)^(k+1)/(k+1),
A_0'=-b^j,
A_1'=-b^j(gamma+m),
A_2'=-b^j(gamma^2+2m*gamma+T2)
```

on phase interiors. The A_k are continuous at integer s, because the length polynomials vanish at zero and geometric reindexing matches the limits. In particular no delta term is silently omitted at an integer phase.

INVERT the unknown trajectory, rather than differentiating a fast-flow value function:

```
Y(s)=g^(-1)(s),
Y0(s)=t+s/2,
delta(s)=Y(s)-Y0(s).
```

Then Y(0)=t, `1/2<=Y'<=1`, delta(0)=0, and `0<=delta'<=1/2` a.e. Thus delta is AC and nondecreasing, with `0<=delta(s)<=s/2`. The signed original tail is

```
I[Y]=integral_(s>=0) R_lambda(s,Y(s))*Y'(s) ds.
```

Introduce the elementary cubic primitive

```
Q(s,y)=(2/3)A_0(s)y^3+A_1(s)y^2
       +(A_2(s)-lambda*A_0(s))*y,
Phi(s,y)=(2/3)y^3+(gamma+m)y^2
         +(gamma^2+2m*gamma+T2-lambda)*y.
```

Then Q_y=R and Q_s=-b^j Phi. Integration by parts gives

```
I[Y]=-Q(0,t)+integral_(s>=0)b^ceil(s)*Phi(s,Y(s)) ds. (L1)
```

All boundary and interchange claims are quantitative: Y(s)<=t+s, delta(s)<=s/2, and each A_k is bounded by b^s times a constant depending only on b,k. Every integrand and differentiated boundary term is therefore an exponentially decaying polynomial. Q(s,Y(s)) tends to zero at infinity. The continuous Q values telescope across phase boundaries. These facts justify AC integration by parts and absolute-integrability Fubini below without a hidden smooth original density assumption.

Put

```
W(s,y)=Phi_y(s,y)
      =2y^2+2(gamma+m)y+gamma^2+2m*gamma+T2-lambda,
a0(s)=b^ceil(s)*W(s,Y0(s)),
T(u)=integral_(s>=u)a0(s) ds.
```

The EXACT cubic expansion, not just a local convexity inequality, is

```
Phi(s,Y0+delta)-Phi(s,Y0)
 =W(s,Y0)*delta+(2Y0+gamma+m)*delta^2+(2/3)delta^3.
```

Since delta(s)=integral_0^s delta'(u)du, absolute Fubini yields

```
I[Y]-I[Y0]
 =integral_(u>=0) delta'(u)*T(u)du
  +integral_(s>=0)b^ceil(s)*[(2Y0(s)+gamma+m)*delta(s)^2
                            +(2/3)*delta(s)^3]ds.       (L2)
```

This inverse-birth/Stieltjes identity is the new representation. No Hfast, Hfast_g, Hamilton-Jacobi equation, unknown-state derivative sign, or tail-A inequality appears in its derivation.

### 5.2 Exact positivity of the reference-tail weight

**Claim L2 — NEW WRITTEN phase summation; its final polynomial identity is WRITTEN-checked-in-kernel. Imports L1 and exact geometric power sums.** For u>0 set

```
j=ceil(u), gamma=j-u, T0=t+j/2>=1/2,
A(T0)=2T0^2+2mT0+T2-lambda,
Cdiag(T0)=2T0^2+2(1+2m)T0+4m^2+4m+2/3,
K(T0,gamma)=m(Cdiag(T0)-lambda)
           +A(T0)*gamma+(m/2)*gamma^2+gamma^3/6.
```

A direct scalar phase sum gives

```
T(u)=b^j*K(T0,gamma).                              (L3)
```

For completeness, on the first partial phase, `Y0(s)+gamma_s/2=T0`, so

```
W(s,Y0(s))=A(T0)+m*gamma_s+gamma_s^2/2.
```

Its integral is `b^j[A(T0)gamma+m*gamma^2/2+gamma^3/6]`. Complete phase ell>=1 contributes

```
b^(j+ell)*[A(T0+ell/2)+m/2+1/6].
```

Using `sum b^ell=m`, `sum ell*b^ell=v`, and `sum ell^2*b^ell=m+3m^2+2m^3` gives the remaining term `b^j*m(Cdiag(T0)-lambda)`, proving (L3). These are reference-tail scalar sums, not a calibration along the unknown trajectory.

K is increasing in T0 and decreasing in lambda. Consequently

```
K(T0,gamma)
 >=K(1/2,gamma;lambdaP)
 =2m^2(1-gamma)+m(11/6-2gamma+gamma^2/2)
   +(gamma+gamma^3)/6
 >=m/3>0,       0<=gamma<=1.                       (L4)
```

The bracket multiplying m decreases to1/3 on[0,1]. Thus T(u)>0 at every positive u. Every term on the right side of (L2) is nonnegative, and it vanishes only when delta is identically zero: a nonzero AC nondecreasing delta with delta(0)=0 has delta'>0 on a positive-measure set. We have proved

```
I[Y]>=I[Y0], with equality iff Y(s)=t+s/2 everywhere. (L5)
```

Unlike the old potential argument, (L2) also displays explicit nonnegative quadratic and cubic remainder terms. The only polynomial sign needed here is on the REFERENCE tail T0=t+ceil(u)/2, while global comparison follows from convexity and the nondecreasing inverse displacement. The old all-unknown-state potential sign is not imported.

### 5.3 The original all-law lower bound, with actual normalizers

**Claim L3 — NEW WRITTEN all-law lower-bound slice, imports S/C for original attainment, U1/U2/G, CAL, and L1–L2.** Take an original attained optimizer of cost J=V and use S's positive amplitude mixture to select one geometric optimal component. Apply U1/U2 to it. Let r_o=b^n be its raw density, with mass Z_o and moment N_o; thus J=N_o/Z_o. Let r_S be the raw one-core density generated by its K_0, with actual mass Z_S>0 and moment N_S.

Use lambda=W1<lambdaP in (L2). The raw rows below t agree exactly by G. The other rows have the new inverse representations above. The EIGHT sectors have equal integrals and null interfaces. Hence

```
N_o-W1*Z_o
 =N_S-W1*Z_S+8*(I[Y]-I[Y0])
 =Z_S*(J(r_S/Z_S)-W1)+8*(I[Y]-I[Y0]) >=0.          (L6)
```

The first term is nonnegative by the definition of W1 over the ENTIRE canonical class, not by a stationary-profile restriction. The second is nonnegative by the independent inverse-birth identity. Division by the actual Z_o proves J>=W1. Original attainment therefore gives **V>=W1 in the original all-Borel/full-continuous-diamond model**. Each canonical core is originally feasible by G, so the reverse inequality V<=W1 is immediate from class inclusion.

This proof did NOT assume the predecessor's V=W1 or consume the old tail-A comparison. Its shared structural imports are precisely disclosed; it is a new analytical lower-bound slice, not a new reviewer verdict on the shared geometry. Full-D sensitivity was preserved before the inverse change of variables and was never replaced by grid shifts, a coordinate-only privacy relaxation, or split budgets.

## 6. Classification of ALL original optimizers

**Claim U3 — NEW WRITTEN uniqueness theorem, imports S's exact positive amplitude mixture, C/X/A via U1, G via U2, L1–L3, and CAL's unique canonical core.** For every finite epsilon>0 there is exactly ONE original optimal Borel probability law.

First take ANY geometric optimal density, not a group average and not a preselected symmetric phase. U1/U2 give its canonical structure. Since L3 gives V=W1, the left side of (L6) is zero. Both right-side terms are nonnegative, so both vanish. Equality in (L5) forces

```
Y(s)=t+s/2, g(y)=2(y-t),
K_i=K_0+iD at EVERY level.
```

The equality of the first term in (L6) means K_0 is a W1-optimal canonical core. CAL's strict fixed-profile/outer calibration identifies it with its unique core S*. Thus EVERY geometric optimal law is the SAME law

```
p_*(z)=b^n_(S*)(z)/Z_*,
n_(S*)(z)=min{k>=0:z in S*+kD},
S*={z: |z|_1<=2t,
          |z|_2^2+2m*|z|_infinity+T2<=V},
Z_*=integral b^n_(S*)(z) dz.
```

The parameters are D's q=2t or R's d,t(d), selected exactly by Sections2–3. The normalizers and closed boundary assignments are exactly those already supplied in the predecessor. No new arbitrary shell masses or unnormalized probability law is introduced.

Now let p be ANY original optimal density, without geometric values, symmetry or an attained peak assumption. S proves `0<M=ess sup p<infinity`, positivity a.e., and the exact feasible amplitude-phase representation, for h in[bM,M),

```
r_h=b^n_h, n_h(x)=min{k>=0:p(x)>h*b^k},
Z_h=integral r_h, q_h=r_h/Z_h,
p(x)=1/(1-b)*integral_(bM)^M r_h(x)dh,
1=integral_(bM)^M Z_h/(1-b)dh,
J(p)=integral_(bM)^M J(q_h)*Z_h/(1-b)dh.
```

Every q_h is genuinely feasible with finite cost, and `Z_h/(1-b)>0`. Since every feasible cost is at least V and the displayed probability average equals V, q_h is optimal for almost every phase under those weights. Every such geometric optimal law is p_* by the first part. Integrating the law of each phase therefore gives, for every Borel event E,

```
mu(E)=integral q_h(E)*Z_h/(1-b)dh=mu_*(E).
```

No common uncountable family of pointwise density exceptions is needed: this is the exact measurable probability-mixture identity. Consequently the FULL optimizer class is the singleton `{mu_*}`. Different Borel density versions may differ on Lebesgue-null sets, but are not different laws; such versions need not themselves satisfy every pointwise ratio. Translations, nonsymmetric densities, non-geometric mixtures, and independent-coordinate alternatives do not yield additional optimal laws.

## 7. Exact arithmetic record, assurance boundary, and parkable state

The finite arithmetic in this continuation was explicitly authorized owner work inside the persistent eval kernel. Every successful proof-arithmetic operation used Python integers and `fractions.Fraction`; there was NO float arithmetic. A SymPy import was attempted and failed because the module is unavailable; no SymPy arithmetic, installation, external CAS, or native fallback was performed.

The exact machine-checked scope is:

- Expansion of (D1), its shifted-x form, and the transition reduction (D5).
- Rational phase-orientation signs, and strict rational isolation of the cubic v_c and corresponding m_c.
- Six strict parameter/value brackets and every displayed branch screen; R endpoint signs use alternating24/25-term rational arctangent bounds.
- Finite-field modular powers/gcds, mod13 factor multiplication and all13 cubic root tests.
- Six exact Sylvester determinants and degree-five interpolation for (D7).
- The polynomial equality in (L4) at T0=1/2, lambda=lambdaP.

The following are WRITTEN, NOT machine/formally checked: the generic minimality and Galois implications, Lindemann application, all measure/AC/interchange arguments, universality of symmetrization and G's applicability, the inverse-birth lower-bound proof, and the classification of all original optimal laws. These are the load-bearing NEW claims requiring their own hostile reconstruction before parent promotion. The predecessor's accepted components do not pre-accept this successor.

The algebraic request is resolved with its necessary mathematical distinction: D has the explicit generic minimal quintic and exact root isolation; R at algebraic m has no minimal polynomial because it is transcendental, but has an exact strictly monotone rationally certifiable analytic root and the executed exact brackets above. No unsupported universal elementary inverse is asserted. No original-law classification gap remains in the written argument at the named imports; the remaining gap is assurance/reconstruction of this new successor, not a silently retained family of unclassified laws.

Novelty remains **NOVELTY_UNCLEAR** and all prior EQ-V1 attributions remain binding: selector monotonicity is PRIOR, generic attainment is PRIOR, shell/Minkowski ancestry is PRIOR, and the broad book article is not claimed solved. The new lower-bound slice shares supplied structural geometry and is not blind, cross-vendor, human, formal, or an independently implemented finite-certificate replay.

All parent errata throughv6, the global scientific-launch HOLD, prior cadence deviations and unchanged deadline remain binding. This owner started no native scientific program, background job, solver, model CLI or nested agent; made no network publication, git operation, deletion, shared-root edit or parent-record change. All new outputs live only in this exclusive owned root. `park-v2.json` binds the delivered successor and exact table by actual SHA-256.
