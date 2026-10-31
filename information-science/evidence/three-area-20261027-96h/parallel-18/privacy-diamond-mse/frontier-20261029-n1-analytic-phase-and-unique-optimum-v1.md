# Analytic all-law solution on an explicit N=1 ε-interval

Owner: InfoResearch96h-2 / info-1. Native clock observed before drafting: `Thu Oct 29 16:06:15 PDT 2026`.

**AUTHOR-WRITTEN CANDIDATE, CONDITIONAL ON THE NAMED f261 SAME-HARNESS REDUCTION; NOT independently reviewed or parent-adopted.** This packet solves the reduced profile problem analytically on the entire explicit interval below: the value is given either by one algebraically isolated root or by one uniquely screened elementary arctangent root, with no residual profile minimization. It does not claim a radical formula or a solution outside that interval.

## 0. Scope, inputs and theorem

For ε>0 write b=e^(-ε), m=b/(1-b), v=m(1+m), and D={h∈R²:||h||_1<=1} with its FULL CLOSED boundary. Let F_b be ALL Borel probability laws satisfying `μ(A)<=b^(-1)μ(A+h)` for EVERY Borel event and EVERY h∈D. Put J(μ)=E|X|_2² and V=inf_(μ∈F_b)J(μ).

Let m_0 be the unique positive root of

    Δ(m)=24m⁴+48m³+26m²+2m-5/16=0,                                      (0a)

and set `ε_0=log((1+m_0)/m_0)`. Exact signs in §1 give `ln14<ε_0<ln15`. Let v_c be the unique positive root of

    2592v³+864v²+18v-1=0,                                                (0b)

and put `ε_t=2 asinh(1/(2sqrt(v_c)))`. Then `ε_0<ln15<ε_t<ln64`.

**Theorem A — analytic value, phase and unique original law for EVERY ε>=ε_0.** At every such ε, the original ALL-law value V is attained by exactly one law. It has the full-D-private shell density

    p_*(x)=b^ceil(d_1(x,C_*))/Z_*.

Its value and core are determined as follows, with all functions and screens defined explicitly in §§2–5:

* **Diamond branch, ε_0<=ε<=ε_t.** Let g be the larger positive root in (0,1) of the explicit quintic P_m in (7). It is uniquely isolated by the stated sign pattern. Put `V=M4(g)/(3M2(g))`, `C_*=gD`, and `Z_*=2M2(g)`.
* **Rounded branch, ε>ε_t.** There is exactly ONE d in the explicit screened interval I_m in (14) solving the single elementary equation `H_m(d)=0` in (17). Set `V=λ(d)`, `t=t(d)`, `c=t-d`, and Z_* from (16). The core is the D4 extension of

       0<=y<=t, y<=x<=F_*(y),
       F_*(y)=sqrt(V-v-y²)-m  for 0<=y<=c,
       F_*(y)=2t-y           for c<=y<=t.

  Here `0<c<t` and the terminal facet has positive width d. H_m uses only rational operations, square roots and one arctangent; its domain, existence and uniqueness are proved below.
* At ε=ε_t the diamond law is the unique optimum and the arc has zero length; no second optimizer is asserted.

This is a genuine interval statement, not a numerical ln64 variant. The theorem leaves the original finite-profile prefix problem **OPEN** for `0<ε<ε_0`; ε_0 is a sufficient one-core cutoff derived from one explicit trial, not a claim of the true maximal one-core range. Source/book equivalence, novelty, formal/human/configured-family verification, and global all-ε uniqueness remain unestablished.

### Named premise and provenance

The sole research-result premise is the **twice-corrected f261 parent disposition** `institute/runs/three-area-2026-10-27-96h/dispositions/info-1-privacy-all-epsilon-optimizer-complementarity-finite-tail-parent-v1.md`, SHA-256 `28335b2def1139d4141a3f62a74ef0f0063f57f2f7500d41d065466267381c97`. We use its actual all-law attainment, optimal-phase mixture, canonical essential supports, full-D feasibility, and exact tail `K_i=K_(i-1)+D` for i>=ceil(sqrt(2V)); no stronger optimizer conclusion is imported.

Before using the underlying source, the two mandatory corrections were actually read IN ORDER in full: `...addendum-1-f250-steiner-fibers.md`, SHA `6b8af7b2d672b470290f3673b5f799ac4ca8b5e015276f287bcdbe1a23a52e27`, LF 1–48; then `...addendum-2-f256-geometry-and-cap-scope.md`, SHA `89f91e9004c9563caf3d4cc831b1101c4e4ade8a138b006b5af7f00c1fddbb14`, LF 1–77; then the unchanged source `frontier-20261029-optimizer-complementarity-and-finite-tail-reduction-v1.md`, SHA `4263cf17acd50a6e1167d7c8b62560cd7c634c2d8711a808de70733cac659b43`, LF 1–90, 91–180, 181–274. The native clock observed after those ordered reads was `Thu Oct 29 16:02:34 PDT 2026`. This does not backdate any earlier read/review.

The threshold cubic agrees with the previously parent-supported **separated** v241 threshold `institute/runs/three-area-2026-10-23-96h/privacy-v241-separated-threshold-and-norm-gap-entire-parent-v1.md`, SHA `48274df7a84b16cd8ead4a0b9069b8359110e1b216bc72e6baea1de03e626138`, whose recorded scope imports LAW642/NORM148. That disposition is prior ancestry/context, NOT a premise here: §§3–4 derive the screen afresh from the explicit quintic. The same continuing author had prior LAW642/threshold exposure; no independent-authorship or clean-cognition claim is made. Held/withdrawn/ZERO bodies and consumers/guides, original threshold-v2/v214-A, MDA26 source text, f161/f162 and protected v214 bodies remain NONINPUT and were not opened for this packet. No historical finding is cured or reclassified.

## 1. Why the interval is one-core

Let G have P(G=k)=(1-b)b^k, k>=0, and `M_j(g)=E(g+G)^j`. Its ordinary moments are

    T2=m+2m²,  T3=m+6m²+6m³,  T4=m+14m²+36m³+24m⁴.                    (1)

For the feasible centered diamond shell with core (1/2)D, direct radial integration gives

    M2(1/2)=1/4+2m+2m²,
    M4(1/2)=1/16+5m+29m²+48m³+24m⁴,
    J(P_(1/2))=M4(1/2)/(3M2(1/2)).

The trial cost is <=1/2 iff Δ(m)<=0. Δ'(m)=96m³+144m²+52m+2>0 for m>=0, Δ(0)<0, and Δ tends to +∞. It has one positive root m_0, with exact signs

    Δ(1/14)=-725/38416<0,    Δ(1/13)=8171/456976>0.                    (2)

Thus ε>=ε_0 iff 0<m<=m_0, giving V<=J(P_(1/2))<=1/2. The f261 cutoff `i>=ceil(sqrt(2V))` is then i>=1, including equality. Every optimal phase is consequently a shell law of ONE compact canonical core K_0. By the f261 phase mixture, proving a unique optimal core law proves uniqueness among ALL original Borel laws.

For m<=m_0<1/13,

    0<v=m(1+m)<14/169<1/12.                                             (3)

The last strict inequality is 168<169 and is essential in the transition-sign proof; it is not silently divided through when it can vanish.

## 2. Exact one-core profile functional and clipping

A canonical core is determined by t>=0 and a continuous profile F on [0,t] with

    F(t)=t,  t<=F(y)<=2t-y,
    F nonincreasing, and F(y)+y nondecreasing.                            (4)

For t=0 take C={0}. Extend the first octant `{0<=y<=t, y<=x<=F(y)}` by D4. The shell `u_C=b^ceil(d_1(.,C))` is full-D private because l1 distance is 1-Lipschitz. Its finite unnormalized mass Z and moment N follow from the f261 parallel-geometry formula, or equivalently from strip/triangle integration:

    Z=8∫_0^t(F-y)dy+8tm+2T2,
    N=(2/3)T4+(16/3)tT3+4t²T2
      +8∫_0^t[T2F+m(F²+y²)+F³/3+y²F-4y³/3]dy.                         (5)

For fixed λ and t put H=N-λZ. The F-dependent part is 8 times the integral of

    G_λ(z,y)=z³/3+mz²+(T2+y²-λ)z,
    ∂_z G=z²+2mz+T2+y²-λ,      ∂²_z G=2(z+m)>0.

Its unique pointwise minimizer over the allowed interval z∈[t,2t-y] is

    R_λ(y)=sqrt(max(λ-v-y²,0))-m,
    F_(t,λ)(y)=min(2t-y,max(t,R_λ(y))).                                 (6)

The clip itself satisfies (4): it is continuous and nonincreasing; where the root is active above t, its slope magnitude is `y/(R+m)<=y/(t+m)<1`, while the constant and upper-facet pieces have slopes 0 and -1. Hence F+y is nondecreasing. Its shell law is an ACTUAL full-D feasible candidate. Denote the exact clipped signed functional by h_λ(t). For every canonical profile H>=h_λ(t), with equality only if F equals the clip a.e.; continuity upgrades equality to every y.

At λ=T2, `R_λ(y)<=0`, so the clip is the square F=t. Expanding (5) yields

    h_T2(t)=(2/3)T4-2T2² +[(16/3)T3-8mT2]t
             +8T2t²+(32/3)mt³+(8/3)t⁴>0     for all t>=0.

The constant is `(2/3)m+(22/3)m²+16m³+8m⁴` and the coefficient of t is `(16/3)m+24m²+16m³`, both strictly positive. Applying this to an f261 optimal one-core phase proves

    V>T2.                                                                 (6a)

## 3. The diamond quintic and the other value endpoint

For a diamond core gD, g>=0, (5) reduces to

    Z=2M2(g),  N=(2/3)M4(g),  J(P_g)=M4(g)/(3M2(g)),
    M2(g)=g²+2mg+T2,
    M4(g)=g⁴+4mg³+6T2g²+4T3g+T4.

Its derivative has the sign of

    P_m(g)=g⁵+5mg⁴+(2m+12m²)g³+(12m³-2m)g²
            -m(1+2m)(1+6m)g+m²(1+2m),                                    (7)

because `M4'M2-M4M2'=2P_m`. It has exactly two coefficient sign changes, regardless of the sign or vanishing of its g² coefficient. Its endpoint values are `P(0)=m²(1+2m)>0` and `P(1)=(1+m)²(1+2m)>0`.

Set x=g+m and τ=1+2m. The centered form is

    P=x⁵+2vx³-2vτx²-v(1+3v)x+2v²τ.                                      (8)

At `g_0=sqrt(v)-m∈(0,1)`, x=sqrt(v) and P=-v^(3/2)<0. Descartes' rule and the endpoint signs give exactly two simple positive roots, both in (0,1), with sign pattern +,-,+. Let g be the larger root. It is the UNIQUE global minimizer of J(P_g) over g>=0: the endpoint laws P_0=P_1 agree, J is strictly increasing after g through 1, and the only other stationary point is a maximum.

Write

    λ_g=M4(g)/(3M2(g)),  λ_P=T4/(3T2)=1/3+4m+4m².                     (9)

Since J(P_1)=J(P_0)=λ_P and J is strictly increasing on [g,1], λ_g<λ_P. Every diamond is feasible, and the positivity of h_T2 gives λ_g>T2. Thus

    T2<V<=λ_g<λ_P,  V<=1/2.                                              (10)

## 4. Exact diamond/rounded screen and its transition cubic

For any λ∈(T2,λ_P), the clip has three exhaustive t-regimes:

* D: `0<=t<=t_D=(sqrt(λ-v)-m)/2`, with F=2t-y;
* R: `t_D<t<t_U`, an initial root arc and final upper facet;
* L: `t>=t_U`, lower clipping with no upper facet, where `2t_U²+2mt_U+T2=λ`.

Indeed on the set where R_λ>=t, the function R_λ(y)+y is strictly increasing because `sqrt(λ-v-y²)=R+m>=t+m>y`. If R(t)>t this produces either the full upper clip or its unique arc/facet junction; if R(t)<=t it produces no upper clip and only lower clipping. The boundaries and one-sided derivatives match.

Let h_D,h_R,h_L denote h_λ in these regimes. In R put c for the arc/facet junction and d=t-c. Direct differentiation of (5), including the endpoint term and cancellation of the moving-junction contributions, gives

    λ=2t²+2d²+2m(t+d)+T2,
    h'_R(t)/16=C0+tv-P3(d),
    C0=T3/3-mT2/2=m/3+(3/2)m²+m³,
    P3(d)=(4/3)d³+2md²+m²d,
    d'=-(2t+m)/(2d+m),
    h''_R(t)=16[v+(2d+m)(2t+m)]>0.                                     (11)

For L, the profile-dependent derivative is a nonnegative integral and, using `λ<=2t²+2mt+T2`, its remaining terms are at least

    (16/3)T3-8mT2+16t(T2-m²)>0.                                        (12)

At t_U the R-side derivative is `16(C0+t_Uv)>0`; hence it is not a zero-minimum of a nonnegative h. The derivation is explicit: the root-arc part contributes no ∂_t F, the upper facet contributes 2, and on that facet `∂_zG=2(u²-d²)+2m(u-d)` with u=t-y; integrate from 0 to d and substitute the junction equation. The L lower-clip derivative contributes a nonnegative integral because t is to the right of the pointwise minimizer. §8 checks the complete resulting polynomial identities, not the geometric theorem.

### 4.1 The operational screen

The diamond minimizer is in the D regime at λ_g exactly when

    λ_g >= M2(g),                                                        (13)

since t_D>=g/2 is equivalent to `λ_g-v>=(g+m)²`, and `(g+m)²+v=M2(g)`.

If (13) holds, h_(λ_g)>=0 in D because J(P_z)>=λ_g for all z. At t_D its derivative is nonnegative: z=2t_D>=g, and both J(P_z)-λ_g and J'(P_z) are nonnegative. By (11) h increases throughout R, and by (12) throughout L. Thus h_(λ_g)>=0 for every t, with exactly one zero at t=g/2. The actual f261 optimal core is among these profiles, so V>=λ_g; the diamond trial gives V<=λ_g. Hence V=λ_g and every optimal phase has the same diamond core. At equality in (13), the zero occurs at the D/R boundary and the arc length is zero.

If (13) fails, at λ_g and t=g/2 the diamond profile is strictly above the clip on an interval near y=0, since `R_(λ_g)(0)<g`. Strict convexity of G gives h_(λ_g)(g/2)<0. Its clip is full-D feasible, so V<λ_g. No D-regime profile can attain V. An optimal profile cannot lie in L, including t_U: h_V is nonnegative everywhere because every clipped law is feasible, but (12) and the positive left derivative at t_U would otherwise make it negative immediately to the left. Hence it lies strictly in R. By h''_R>0, nonnegative h_V has at most one zero there; strict pointwise clipping gives one core and the f261 mixture gives one original law.

### 4.2 Eliminating the root screen to a cubic

At the larger diamond root let x=g+m>sqrt(v), and set

    G=2x⁴-4vτx-v-6v²,   Q=x²-v-1/6.

The centered moments obey `M2=x²+v` and `M4=x⁴+6vx²+4vτx+v+9v²`; hence `M4-3M2²=-G`. The exact all-variable identity

    2xP+(v-x²)G=6v(x²+v)(x²-v-1/6)                                    (13a)

therefore gives, at P=0,

    λ_g-M2(g)=2v Q/(x²-v).                                               (13b)

The denominator is positive. Put `x_c=sqrt(v+1/6)>sqrt(v)`. Since P is negative from sqrt(v) up to the larger root and positive after it, the sign of Q at that root is the OPPOSITE of the sign of P(x_c). At x_c, (13a) reduces to `12x_c P(x_c)=G(x_c)`. Write

    A=(1-12v)(1+6v)/18,  τ²=1+4v.

Using (3), A>0 and `G(x_c)=A-4vτ x_c`. Both terms compared are nonnegative, and the EXACT identity

    A²-16v²(1+4v)(v+1/6)
       =(1+6v)[1-18v-864v²-2592v³]/324                                  (13c)

shows

    sign[λ_g-M2(g)] = sign[2592v³+864v²+18v-1].                         (13d)

No squaring ambiguity is suppressed: A>0 is checked by (3), and the other factor `A+4vτx_c` is strictly positive. The cubic on the right is strictly increasing for v>=0, from -1 to +∞, so v_c exists uniquely. Since `v=b/(1-b)²=1/[4sinh²(ε/2)]` strictly decreases with ε, (13d) proves the branch allocation in Theorem A. Exact signs at v=1/50 and 1/40 bracket v_c; `64/3969<1/50<1/40<15/196` then give `ln15<ε_t<ln64`. Writing s_c=1/(4v_c), the same threshold has the unique-positive-root equation `2s_c³-9s_c²-108s_c-81=0`.

## 5. Rounded branch as ONE screened scalar equation

For the rounded branch v<v_c, define for d>0

    t(d)=[P3(d)-C0]/v,   c(d)=t(d)-d,
    λ(d)=2t(d)²+2d²+2m[t(d)+d]+T2.                                      (14a)

The exact screened interval is

    I_m={d∈(0,1/2): t(d)>d,  T2<λ(d)<λ_P,  λ(d)<=1/2}.                 (14)

No t- or F-minimization remains in this definition. On I_m put t=t(d), c=c(d), λ=λ(d), and

    A=λ-v,  Y=t+d+m,  θ=arctan(c/Y),  A=Y²+c².

Define the elementary integrals

    I0=(cY+Aθ)/2,
    I1=[c(2c²-A)Y+A²θ]/8,
    F1=I0-mc+2t(t-c)-(t²-c²)/2,
    F2=Ac-c³/3-2mI0+m²c+[(2t-c)³-t³]/3,
    F3=A I0-I1-3m(Ac-c³/3)+3m²I0-m³c+[(2t-c)⁴-t⁴]/4,
    Fy=I1-mc³/3+2t(t³-c³)/3-(t⁴-c⁴)/4.                                  (15)

They are exactly `∫F`, `∫F²`, `∫F³`, and `∫y²F`, with the arc and facet indicated in Theorem A. The two arc primitives follow from y=sqrt(A) sin θ; all square roots are real and Y>0 on I_m. Put

    Z(d)=8[F1-t²/2]+8tm+2T2,
    N(d)=(2/3)T4+(16/3)tT3+4t²T2
          +8[T2 F1+m F2+m t³/3+F3/3+Fy-t⁴/3],                            (16)
    H_m(d)=N(d)-λ(d)Z(d).                                                (17)

These are exactly (5) for the arc/facet core, and Z(d)>0.

**Existence.** Section 4.1 places the actual optimum in R. Its derivative vanishes, so (11) gives t=t(d) and λ=λ(d). Its value satisfies (10), putting it in I_m. Also λ<=1/2 and (14a) imply `2t²<λ<=1/2`, so t<1/2 and d<t<1/2. Thus its d is a root of (17) in I_m.

**Uniqueness.** `t'(d)=(2d+m)²/v>0`. The function t(d)-d starts negative, has derivative `[(2d+m)²-v]/v` strictly increasing from a negative value to +∞, and has exactly one positive zero. Thus `t(d)>d` is one interval. On it, λ'(d)=4t t'+4d+2m(t'+1)>0, so the remaining upper screens cut out an interval; the lower bound λ>T2 is automatic. Along that interval (11) gives ∂_t h=0. Differentiating the clipped functional in λ gives `∂_λ h=-Z(d)<0`: the root-arc ∂_F G vanishes, facet values do not depend on λ, and moving-junction terms cancel. Therefore

    H_m'(d)=-Z(d)λ'(d)<0.                                                (18)

There is at most one root on I_m. The actual optimum supplies it, proving the scalar equation and core formula in Theorem A. This argument does not silently select a local root by a numerical guess.

## 6. Full-law uniqueness and exact limits

In the D branch §4.1 showed the only zero of h_V is the diamond t=g/2. In the R branch h_V>=0 everywhere and h''_R>0, so its actual interior zero is unique. In either case strict convexity of G and continuity of canonical profiles make the optimizing F unique at that t. Every optimal f261 phase is the normalized shell of this SAME core, and its normalized density is therefore p_* in §0. The exact f261 mixture of optimal phases then implies every original all-law optimizer is the same probability law.

This conclusion uses the named parent-supported f261 theorem, not the earlier held threshold or any unreviewed successor. It makes no statement that every nonoptimal law is one-core, that ε_0 is a necessary cutoff, or that smaller ε have the same representation.

## 7. Review priorities

A full disjoint review should reconstruct: the trial cutoff including ε=ε_0; the positive h_T2 bracket; the two positive quintic roots and endpoint-law equality; every D/R/L switch and moving-boundary derivative; the sufficient/necessary diamond screen; all signs in (13a)–(13d), especially A>0 and the square comparison; the interval/monotonicity proof for the screened arctan equation; and transfer from the single optimal profile to ALL original Borel laws through f261. Check the prior v241 attribution separately from the f261-only proof premise. No external publication, source-equivalence or novelty inference follows.

## 8. Exact owner-run polynomial controls

The first cell below was executed successfully in one Python eval kernel and printed PASS A–D. An earlier version had a Python syntax error (one unclosed parenthesis), so it did not execute; the corrected complete cell below produced the stated output. The code uses only exact `fractions.Fraction` sparse-polynomial arithmetic. These controls verify the displayed finite identities and rational bracket comparisons, NOT f261, the clipping geometry, root-existence proof, global optimality or uniqueness.

```python
from fractions import Fraction as F
names=('x','m','t')
def var(s):
 e=[0,0,0];e[names.index(s)]=1;return {tuple(e):F(1)}
def cst(a):return {(0,0,0):F(a)} if a else {}
def add(*ps):
 o={}
 for p in ps:
  for k,v in p.items():o[k]=o.get(k,F(0))+v
 return {k:v for k,v in o.items() if v}
def sc(p,a):return {k:v*F(a) for k,v in p.items() if v*a}
def mul(*ps):
 o=cst(1)
 for p in ps:
  z={}
  for k,v in o.items():
   for h,w in p.items():
    j=tuple(k[i]+h[i] for i in range(3));z[j]=z.get(j,F(0))+v*w
  o={k:v for k,v in z.items() if v}
 return o
def pw(p,n):return mul(*([p]*n)) if n else cst(1)
def der(p,axis):
 o={}
 for k,v in p.items():
  if k[axis]:
   j=list(k);j[axis]-=1;o[tuple(j)]=v*k[axis]
 return o
x,m,t=(var(n) for n in names);g=add(x,sc(m,-1));one=cst(1)
v=add(m,pw(m,2));tau=add(one,sc(m,2))
T2=add(m,sc(pw(m,2),2));T3=add(m,sc(pw(m,2),6),sc(pw(m,3),6));T4=add(m,sc(pw(m,2),14),sc(pw(m,3),36),sc(pw(m,4),24))
M2=add(pw(g,2),sc(mul(m,g),2),T2)
M4=add(pw(g,4),sc(mul(m,pw(g,3)),4),sc(mul(T2,pw(g,2)),6),sc(mul(T3,g),4),T4)
P=add(pw(g,5),sc(mul(m,pw(g,4)),5),mul(add(sc(m,2),sc(pw(m,2),12)),pw(g,3)),mul(add(sc(pw(m,3),12),sc(m,-2)),pw(g,2)),sc(mul(m,add(one,sc(m,2)),add(one,sc(m,6)),g),-1),mul(pw(m,2),add(one,sc(m,2))))
Px=add(pw(x,5),sc(mul(v,pw(x,3)),2),sc(mul(v,tau,pw(x,2)),-2),sc(mul(v,add(one,sc(v,3)),x),-1),sc(mul(pw(v,2),tau),2))
assert P==Px and M2==add(pw(x,2),v)
assert M4==add(pw(x,4),sc(mul(v,pw(x,2)),6),sc(mul(v,tau,x),4),v,sc(pw(v,2),9))
assert add(mul(der(M4,0),M2),sc(mul(M4,der(M2,0)),-1))==sc(P,2)
G=add(sc(pw(x,4),2),sc(mul(v,tau,x),-4),sc(v,-1),sc(pw(v,2),-6))
H=mul(cst(6),add(pw(x,2),v),add(pw(x,2),sc(v,-1),cst(F(-1,6))))
assert add(sc(mul(x,P),2),mul(add(v,sc(pw(x,2),-1)),G))==mul(v,H)
assert add(M4,sc(mul(M2,M2),-3))==sc(G,-1)
print('PASS A: complete quintic, centered moments and screen-elimination identities')

# Square-free v-screen identity with an independent formal variable z.
z=x
Az=sc(mul(add(one,sc(z,-12)),add(one,sc(z,6))),F(1,18))
q=add(z,cst(F(1,6)))
lhs=add(pw(Az,2),sc(mul(pw(z,2),add(one,sc(z,4)),q),-16))
rhs=sc(mul(add(one,sc(z,6)),add(one,sc(z,-18),sc(pw(z,2),-864),sc(pw(z,3),-2592))),F(1,324))
assert lhs==rhs
print('PASS B: exact v-screen factorization, no radical or floating computation')

# Optimal-value lower bracket: h_{T2}(t) coefficients.
assert add(sc(T4,F(2,3)),sc(pw(T2,2),-2))==add(sc(m,F(2,3)),sc(pw(m,2),F(22,3)),sc(pw(m,3),16),sc(pw(m,4),8))
assert add(sc(T3,F(16,3)),sc(mul(m,T2),-8))==add(sc(m,F(16,3)),sc(pw(m,2),24),sc(pw(m,3),16))
# Junction-derived rounded derivative, treating x as d.
lam=add(sc(pw(t,2),2),sc(pw(x,2),2),sc(mul(m,add(t,x)),2),T2)
base=add(sc(T3,F(16,3)),sc(mul(t,T2),16),sc(mul(m,pw(t,2)),16),sc(mul(m,lam),-8))
ht=add(base,sc(pw(x,3),F(-64,3)),sc(mul(m,pw(x,2)),-16))
C0=add(sc(T3,F(1,3)),sc(mul(m,T2),F(-1,2)))
P3=add(sc(pw(x,3),F(4,3)),sc(mul(m,pw(x,2)),2),mul(pw(m,2),x))
assert ht==sc(add(C0,mul(t,v),sc(P3,-1)),16)
assert der(P3,0)==pw(add(sc(x,2),m),2)
print('PASS C: h_T2 positive coefficients and rounded envelope algebra')

# Rational endpoint/cutoff facts; these are not a global optimization check.
def delta(a):return 24*a**4+48*a**3+26*a*a+2*a-F(5,16)
def f(vv):return 2592*vv**3+864*vv*vv+18*vv-1
assert delta(F(1,14))==-F(725,38416) and delta(F(1,13))==F(8171,456976)
assert f(F(1,50))<0<f(F(1,40))
assert F(64,3969)<F(1,50)<F(1,40)<F(15,196)<F(1,12)
print('PASS D: m0 and phase-threshold rational brackets; no numerical root solver')
```

The following two small cells were then executed successfully in that SAME kernel; they printed PASS E and PASS F. They do not claim a separate fresh-kernel replay.

```python
# Additional exact identities, continuing from the successful A–D cell.
def subx(poly,q):
 out={}
 for (a,b,c),coef in poly.items():
  rest={(0,b,c):coef};out=add(out,mul(rest,pw(q,a)))
 return out
assert subx(P,m)==mul(pw(m,2),add(one,sc(m,2)))
assert subx(P,add(m,one))==mul(pw(add(one,m),2),add(one,sc(m,2)))
reduced={}
for (a,b,c),coef in P.items():
 rest={(a%2,b,c):coef};reduced=add(reduced,mul(rest,pw(v,a//2)))
assert reduced==sc(mul(v,x),-1)
assert T4==mul(T2,add(one,sc(m,12),sc(pw(m,2),12)))
print('PASS E: endpoints, P(sqrt(v))=-v sqrt(v), and lambda_P identity')
print('F(1/50)=',f(F(1,50)),' F(1/40)=',f(F(1,40)))
```

```python
# Extra exact trial expansions, following the successful A–D/E cells.
half=add(m,cst(F(1,2)))
M2h=subx(M2,half);M4h=subx(M4,half)
assert M2h==add(cst(F(1,4)),sc(m,2),sc(pw(m,2),2))
assert M4h==add(cst(F(1,16)),sc(m,5),sc(pw(m,2),29),sc(pw(m,3),48),sc(pw(m,4),24))
Dh=add(M4h,sc(M2h,F(-3,2)))
assert Dh==add(cst(F(-5,16)),sc(m,2),sc(pw(m,2),26),sc(pw(m,3),48),sc(pw(m,4),24))
print('PASS F: exact one-half diamond trial and monotone cutoff polynomial')
```

## 9. Assurance and residual

This is a CONDITIONAL AUTHOR-WRITTEN analytic successor to f261, not an independently reviewed or parent-adopted theorem. Its N=1 range is explicit and includes a nonempty diamond interval and an unbounded rounded interval; the rounded value is uniquely defined by the screened elementary equation, not claimed expressible by radicals. It does not solve the f261 nonparallel-prefix problem for `0<ε<ε_0`, settle publication/source priority or novelty, confer formal/kernel/human/configured-family assurance, or rehabilitate historical held material.
