# LAW642-free lower half at ε=ln 64: strict Steiner equalities, minimal shells, and a certified t-scan

Owner: InfoResearch96h-2 / original info-1. Native clock observed before this write: `Thu Oct 29 09:24:54 PDT 2026`.

**AUTHOR-WRITTEN CANDIDATE, with owner-run exact finite arithmetic. UNREVIEWED; NOT PARENT-ADOPTED.** This is the ONE additive packet requested by Main after freezing `frontier-20261029-independent-bridge-matching-optima-v1.md` (SHA-256 `58600f53f9e4c554566527d0800870485e4f9f97c262b5a08c9b6cd86d56dddc`) as f181. No frozen predecessor is edited. All load-bearing mathematics is supplied below; the bridge is not an assumed theorem.

**Meaning of LAW642-free:** no LAW642 theorem, optimality statement, selector, screen sufficiency or source-equivalence claim is a premise. This is NOT a claim of independent authorship or unaffected cognition: the same continuing owner authored LAW642, and consulted its own earlier text during this work, as disclosed in checkpoints 007–008. All formulas needed here are derived below. Held/withdrawn/ZERO material, MDA26 source text, f161/f162, and protected old threshold/v214 bodies remain NONINPUT and were not opened for this packet. f158 and d67 dispositions provide only the requested scope/context; neither is a mathematical premise.

## 0. Exact result and dependencies

Put

    λ_lo = 163006627735070347894185905345794/10^33,
    λ_hi = 163006627735070347894185905345795/10^33.

**Theorem B (the lower half and its matching upper half).** In the full model of §1, at ε=ln 64,

    λ_lo < V_J < λ_hi.                                                   (B)

Thus the original ALL-Borel, EVERY-closed-diamond-shift squared-Euclidean optimum has a certified-width-10^-33 value bracket. The upper half comes from an actual rational-parameter feasible shell law. The lower half uses the complete Steiner/minimal-shell reduction below, not LAW642.

**Corollary C (identification at this ε only).** There is exactly one J-optimal probability law at ε=ln 64. It is the distance-shell law of the D4 extension of the octant core

    0<=y<=t_*,   y<=x<=F_*(y),
    F_*(y)=sqrt(V_J-v-y^2)-m   on [0,c_*],
    F_*(y)=2t_*-y              on [c_*,t_*],
    m=1/63, v=m(1+m), d_*=t_*-c_*.

The junction is genuine: 0<c_*<t_*. The exact boxes are

    c_* ∈ (9274808134495397323165995922,9274808134495397323165995923)/10^30,
    d_* ∈ (17899568185394517443007219151,17899568185394517443007219152)/10^29,
    t_* ∈ (18827048998844057175323818743,18827048998844057175323818744)/10^29.

The structural reduction of §§2–6 requires V_J<1/2, a condition established here by the upper certificate. It is NOT asserted for arbitrary ε. The registered general-ε question is not silently replaced by this instance.

| Claim | Research-result premises | Standard inputs / finite controls |
|---|---|---|
| Existence, density, phase mixture | none | Prokhorov, regularity, Lebesgue differentiation, Tonelli, lower semicontinuity |
| Four symmetries and exact representatives | none | one-dimensional centered-interval moment inequality; slice-by-slice interval expansion; essential support |
| Minimal shells when V_J<1/2 | none | optimality, exact Minkowski inclusions, ||x||_1^2<=2|x|_2^2 |
| Canonical geometry, ZN, clipping, envelopes | none | elementary geometry, geometric series, integration, Leibniz rule |
| Bracket (B), parameter boxes | none | §§2–9 plus exact Fraction / Q(sqrt D) / alternating arctangent bounds in §10 |
| Novelty, primary-source equivalence, formal proof, independent review | not established | not implied by this packet |

## 1. Model and notation

Fix ε>0, b=exp(-ε)∈(0,1), and the FULL CLOSED diamond `D={h∈R^2:||h||_1<=1}`. Let F be ALL Borel probability measures μ on R^2 satisfying

    μ(A)<=b^(-1)μ(A+h)     for EVERY Borel A and EVERY h∈D.                 (DP)

There is no original density, symmetry, independence, convexity or radiality ansatz. Put `J(μ)=∫|x|_2^2 dμ(x)` and `V=V_J=inf_(μ∈F)J(μ)`.

For Lebesgue-measurable A write |A| for area, `M(A)=∫_A|x|_2^2 dx`, and `Φ_λ(A)=M(A)-λ|A|`. A minimal-shell law of a nonempty compact core C has unnormalized density

    u_C(x)=b^min{k>=0:x∈C+kD}=b^ceil(d_1(x,C)),   d_1=inf_(z∈C)||x-z||_1. (SHELL)

Ceil(0)=0. Because d_1 is 1-Lipschitz in the l1 metric, its ceiling changes by at most one under a closed-D shift. Thus the normalized law P_C satisfies (DP). Its mass and moment are finite: C is bounded and its shells have at most polynomial area and moments, weighted geometrically. In particular no convexity of C is needed for feasibility.

Let G have probability `(1-b)b^k` at k>=0. Put m=EG=b/(1-b), v=m(1+m), and

    T2=EG^2=m+2m^2, T3=m+6m^2+6m^3, T4=m+14m^2+36m^3+24m^4,
    M_j(g)=E(g+G)^j.

These follow, for example, by differentiating `(1-b)/(1-bs)` j times at s=1 to get factorial moments j!m^j, then expanding ordinary powers into factorial powers. In particular

    M2(g)=g^2+2mg+T2,
    M3(g)=g^3+3mg^2+3T2g+T3,
    M4(g)=g^4+4mg^3+6T2g^2+4T3g+T4.                                      (MOMENTS)

## 2. Existence, an all-point private density, and nonradial optimal phases

### 2.1 Existence and density

The product Laplace density `(ε^2/4)exp(-ε||x||_1)` is feasible and has J=4/ε^2. A minimizing sequence with bounded J is tight by Markov's inequality; Prokhorov gives a weak probability limit μ. For every fixed h∈D and nonnegative bounded continuous f, (DP) gives `∫f dμ_n<=b^(-1)∫f(x-h)dμ_n(x)`, which passes to μ. Decreasing bounded-continuous approximations to indicators of closed sets, then inner regularity for Borel sets, give (DP) for μ. J is weakly lower semicontinuous, since it is the supremum of the integrals of the bounded continuous functions min(|x|^2,R). Hence V is attained.

Integrating (DP) over the area-two diamond and applying Tonelli gives

    2b μ(A)<=∫_D μ(A+h)dh=∫|D∩(x-A)|dμ(x)<=|A|.

Thus μ has density bounded by 1/(2b). Define the Borel representative `f(x)=limsup_(r↓0,r rational) μ(B_r(x))/|B_r|`, with Euclidean balls. It is the density a.e., bounded everywhere by 1/(2b), and the ball form of (DP) gives

    f(x+h)>=b f(x)     for EVERY x and EVERY h∈D.                          (POINT)

It is positive somewhere, and finite chains of D-shifts propagate positivity to every point. Write `M=sup_x f(x)∈(0,1/(2b)]`.

### 2.2 Rooted phase sequences

A rooted phase sequence consists of nonempty Borel E_0 and Borel E_i, i>=0, satisfying `E_i+D⊆E_(i+1)`, with finite positive mass and finite moment for `u_E=b^n`, `n(x)=min{i>=0:x∈E_i}`. The index is finite because E_i contains a translate of iD. The sequence is nested (0∈D), and the index argument gives (POINT) for u_E. The normalized law is feasible. Pointwise geometric summation and Tonelli give

    Z_E=(1-b)Σ_(i>=0)b^i|E_i|,
    N_E=(1-b)Σ_(i>=0)b^i M(E_i),
    H_λ(E):=Σ_(i>=0)b^i Φ_λ(E_i)=(N_E-λZ_E)/(1-b).                       (PHASE)

The series of absolute values of the signed terms is bounded by the two nonnegative finite series. In particular H_V(E)>=0 for every such sequence.

### 2.3 Mixture identity, without radiality

For a∈(bM,M) set `E_i(a)={f>ab^i}`, `n_a=min{i>=0:x∈E_i(a)}`, and `u_a=b^n_a`. These are rooted sequences with the exact inclusion from (POINT), apart from possible infinite mass/moment. For every x,

    ∫_(bM)^M u_a(x)da=(1-b)f(x).                                         (MIX)

For completeness, put y=f(x), κ=log_b(y/M)>=0 and a=Mb^σ, σ∈(0,1). The index n_a is the least integer n>=0 with σ+n>κ. The quantity w=σ+n runs once through (κ,κ+1], with slope one on its pieces. Therefore the integral is `∫_κ^(κ+1)Mb^w|log b|dw=(1-b)y`. Endpoint equalities have a-measure zero.

Tonelli gives `∫Z_a da=1-b` and `∫N_a da=(1-b)J(μ)`. Thus for a.e. a both are finite, Z_a>0, and the normalized phase P_a is feasible. With `w(a)=Z_a/(1-b)`,

    μ=∫w(a)P_a da,   ∫w=1,   J(μ)=∫w(a)J(P_a)da.                        (OPT-MIX)

If μ is optimal, a.e. P_a is optimal. If a selected optimal phase has |E_0|=0, then E_1 has positive area because it contains x_0+D for any x_0∈E_0. Removing that null initial level and reindexing multiplies u by 1/b a.e., so the normalized law is unchanged. We may therefore fix an optimal phase with |E_0|>0 and H_V(E)=0.

## 3. Four separate strict Steiner equalities

Use unit directions e1,e2,(e1+e2)/sqrt(2),(e1-e2)/sqrt(2). In coordinates (p,w) along e^perp and e, let `ℓ_A(p)=|{w:p e^perp+w e∈A}|` and

    S_e A={p e^perp+w e: |w|<ℓ_A(p)/2},

with the whole line when ℓ_A=∞ and the empty interval when ℓ_A=0. For Borel A the section-length function is Borel, and so is S_eA. Fubini gives |S_eA|=|A|; it is monotone in A and preserves a.e. equality of sets. The centered interval of length ℓ minimizes ∫w^2 dw among measurable subsets of the line with that length, uniquely up to a null set: subtract the two equal-area pieces inside/outside [-ℓ/2,ℓ/2], where w^2 is respectively below/above (ℓ/2)^2. Hence

    M(S_eA)<=M(A), with equality at finite moment iff A=S_eA a.e.          (STEINER)

**Exact inclusion lemma.** For any of the four directions, `A+D⊆B` implies `S_eA+D⊆S_eB` as actual sets. Indeed D_q is a centered interval [-δ(q),δ(q)] whenever nonempty. For axis directions δ(q)=1-|q|, |q|<=1. In diagonal coordinates D is the square with both half-sides 1/sqrt(2).

Fix x=(p,w)∈S_eA and h=(q,v)∈D. The original fiber B_(p+q) contains A_p+[-δ(q),δ(q)]. Every nonempty compact C⊆A_p has expansion of length at least |C|+2δ(q): C plus the two exterior endpoint intervals already has that measure. Inner regularity yields `ℓ_B(p+q)>=ℓ_A(p)+2δ(q)` when ℓ_A(p)>0; the infinite case follows from arbitrarily large compact lengths. Thus `|w+v|<ℓ_A(p)/2+δ(q)<=ℓ_B(p+q)/2`, proving the inclusion, including boundary shifts.

Apply each S_e SEPARATELY to all levels of the optimal phase E. The exact inclusion lemma makes another rooted phase; its Z is the same and its N is no larger. Optimality forces equality. By (PHASE), a nonnegative weighted sum of the differences M(E_i)-M(S_eE_i) is zero; every difference is zero. Consequently

    E_i=S_eE_i a.e.   for EVERY i and EACH of the four directions.        (FOUR)

This is not an assertion that four successive operations automatically preserve all earlier symmetries. It is four separate equality arguments at the original optimum.

## 4. Exact compact representatives and minimal shells

### 4.1 Essential supports really equal these levels a.e.

Write `supp_ess(A)={x: |A∩B_r(x)|>0 for every r>0}`. It is closed and depends only on the a.e. class. For each E_i, the double symmetrization B=S_e2 S_e1 E_i agrees a.e. with E_i by (FOUR) and a.e. preservation. Explicitly B has form

    B={ (x,y): |y|<L(x)/2 },  L(x)=∫1_{|x|<ℓ_Ei(y)/2}dy.

L is even and nonincreasing in |x|. Thus B is 1-unconditional and its first-quadrant part is a coordinate down-set. Such a set has null planar boundary: at every continuity point of its nonincreasing height function the vertical boundary section has at most one point; the jump points are countable, and axes are null. Therefore interior(B)⊆supp_ess(B)⊆closure(B) implies `supp_ess(B)=B` a.e.

Set K_i=supp_ess(E_i). We have proved

    K_i=E_i a.e.,  |K_i|<∞, M(K_i)<∞.                                    (REP)

### 4.2 Closed centered sections in all four directions

If A has centered interval sections in direction e, then its essential support has closed centered interval sections in that direction. Reflection symmetry is inherited. For the interval property, the map T_α:(p,w)↦(p,αw), 0<α<=1, sends A into A, contracts balls and multiplies area by α. Thus a positive-measure intersection in every ball about x implies the same about T_αx. Let α↓0 and use closedness. This proves the claim on every line, not just a.e. lines.

By (FOUR), K_i=supp_ess(S_eE_i) for each e, so K_i has this property in all four directions. The reflections generate D4. Axis-centered sections make K_i∩Q1 a down-set. Positive area implies a point with both coordinates nonzero; its centered coordinate rectangle lies in K_i, giving 0∈int K_i. Finite area plus anti-diagonal convexity bounds the set: for x∈K_i, reflect to Q1 and let s=||x||_1. The segment to the swapped point contains (s/2,s/2), whose centered coordinate square has area s^2 and lies in K_i. Hence s^2<=|K_i|. Every K_i is compact.

### 4.3 Exact closed-D inclusions

For x∈K_i,h∈D, each translated set `(E_i∩B_r(x))+h` lies in `E_(i+1)∩B_r(x+h)` and has positive measure. Hence

    K_i+D⊆K_(i+1) EXACTLY.                                               (CLOSED)

No null-set replacement is fed into a Minkowski sum without this argument. The phase built from K_i equals the original one a.e., by (REP).

### 4.4 Minimal shells when V<1/2

Put C=K_0 and C_i=C+iD. Then C_i⊆K_i exactly by (CLOSED), and C_i contains iD since 0∈C. For i>=1, a point outside C_i is outside D, hence

    |x|_2^2 >= ||x||_1^2/2 > 1/2 > V.

Thus `Φ_V(K_i)-Φ_V(C_i)=∫_(K_i\C_i)(|x|^2-V)>=0`, strictly unless that difference has zero area. At i=0 the sets are equal. The minimal-shell sequence is feasible with finite mass/moment, so

    0<=H_V((C_i))<=H_V((K_i))=0.

Every nonnegative term difference is zero. Therefore K_i=C+iD a.e. for every i, P_C is optimal, and the original optimal phase equals P_C. This proves the needed reduction for ANY V<1/2: every optimal law has a.e. phases that are minimal-shell laws of compact D4-symmetric cores with centered interval sections in the four directions. The condition V<1/2 will be verified by the independent upper construction in §8.

## 5. Canonical profiles: the missing slope property is proved directly

For any such core C, let `t=max{s>=0:(s,s)∈C}>0` and `F(y)=max{x>=0:(x,y)∈C}` for 0<=y<=t. Its first-octant part is exactly `0<=y<=t, y<=x<=F(y)`. Axis-centered sections make F nonincreasing. Also F(t)=t: otherwise the anti-diagonal segment from (F(t),t) to its swap contains a diagonal point beyond (t,t). Hence F(y)>=t.

For 0<=y<=y'<=t, we have y'<=t<=F(y). The anti-diagonal segment from (F(y),y) to (y,F(y)) therefore contains

    (F(y)+y-y', y')∈C.

Thus F(y')>=F(y)+y-y', or F(y)+y<=F(y')+y'. This is the required property; it does not require cap-raising, an unproved order-hull assertion or a LAW642 input. Together with monotonicity it yields

    0<=F(y)-F(y')<=y'-y,   t<=F(y)<=2t-y,   F(t)=t.                       (CAN)

F is continuous and 1-Lipschitz. Conversely any F satisfying (CAN) defines a compact D4-symmetric coordinate down-set by extending this octant. Write C_(t,F) for it. We only need the latter down-set property for its distance and moments.

## 6. Distance geometry and the full arbitrary-profile moment formula

For x∈Q1 and any 1-unconditional coordinate down-set C, reflect a candidate nearest point into Q1 and then replace it by its coordinatewise minimum with x. These operations stay in C and cannot increase l1 distance. Thus

    d_1(x,C)=x1+x2-max{k1+k2:k∈C∩Q1,k<=x}.

If x1>=x2>=0, swap an admissible k if necessary: the sorted k is still dominated by x and has the same sum. Now (CAN) gives

    d_1(x,C_(t,F))=(x1-F(x2))_+      if x2<=t,
    d_1(x,C_(t,F))=x1+x2-2t         if x2>t.                             (DIST)

For the first line, an exterior x has x1>F(x2), and every sorted k<=x obeys `k1+k2<=F(k2)+k2<=F(x2)+x2`; the last bound is attained by (F(x2),x2). For the second line all core sums are <=2t, attained by (t,t)<=x. Interior x has distance zero. D4 extends the formula to the plane.

Let Z,N be the unnormalized mass and moment of the shell law. Then

    Z=8∫_0^t(F-y)dy+8tm+2T2,
    N=(2/3)T4+(16/3)tT3+4t^2T2
      +8∫_0^t[T2F+m(F^2+y^2)+F^3/3+y^2F-4y^3/3]dy.                    (ZN)

Here is the complete integration, including the tail region. By D4, integrate one octant and multiply by 8. In the strip x2=y<=t, (DIST) gives density 1 for y<=x1<=F(y), then b^k on F(y)+k-1<x1<=F(y)+k. The line mass is F-y+m, and its squared-cost integral is

    (M3(F)-y^3)/3+y^2(F-y+m).

Use (MOMENTS) and integrate in y. In the remaining triangle put x1=t+p,x2=t+q, p>=q>0, s=p+q. The density is b^ceil(s). The line mass integral over q∈[0,s/2] is s/2, and the line moment is

    ∫_0^(s/2)[(t+s-q)^2+(t+q)^2]dq=t^2s+ts^2+s^3/3.

For j>=0, geometric summation by parts gives `∫_0^∞b^ceil(s)s^j ds=E G^(j+1)/(j+1)`. Thus the triangle contributes T2/4 to Z/8 and `t^2T2/2+tT3/3+T4/12` to N/8. Combining the strip and triangle gives (ZN). All boundaries are null; polynomial geometric tails justify all integrals.

For the full facet F=2t-y, the core is the diamond 2tD. Writing g=2t, (ZN) gives

    Z=2M2(g),   N=(2/3)M4(g),   J(P_g)=M4(g)/(3M2(g)).                    (DIAMOND)

This also follows by directly integrating over diamond radii. As normalized laws P_0=P_1, since the unnormalized densities differ by a constant factor a.e.

## 7. Pointwise clipping and the complete three-regime t-calculus

For fixed t,λ put H(t,F;λ)=N-λZ. Its F-dependent part is `8∫_0^t G_λ(F(y),y)dy`, where

    G_λ(z,y)=z^3/3+mz^2+(T2+y^2-λ)z,
    ∂_z G=z^2+2mz+T2+y^2-λ,   ∂_zz G=2(z+m)>0 for z>=0.

The unique minimizer over z∈[t,2t-y] is

    R_λ(y)=sqrt(max(λ-v-y^2,0))-m,
    CLIP_(t,λ)(y)=min(2t-y,max(t,R_λ(y))).

Consequently

    H(t,F;λ)>=h_λ(t):=H(t,CLIP_(t,λ);λ),                                 (CLIP)

with equality iff F=CLIP a.e. The clip itself satisfies (CAN): it is continuous/nonincreasing, and where R exceeds t its slope magnitude is `y/(R+m)<=y/(t+m)<1`; the other pieces have slopes 0 and -1. Thus CLIP+y is nondecreasing and its endpoint value is t. Its shell law is feasible for every t>0.

For the following regime formulas assume λ>T2. Put A=λ-v and

    t_D=(sqrt(A)-m)/2,   2t_U^2+2mt_U+T2=λ.

Then 0<t_D<t_U, and there are exactly three successive regimes:

* **D, 0<t<=t_D:** CLIP=2t-y, so `h_λ(t)=(2/3)M4(2t)-2λM2(2t)`.
* **R, t_D<t<t_U:** CLIP=R on [0,c], then 2t-y on [c,t], with 0<c<t. Put d=t-c. The junction equation is

    λ=2t^2+2d^2+2m(t+d)+T2.                                              (JUNCTION)

* **L, t>=t_U:** CLIP=max(t,R), with no upper clip.

To justify completeness, on the interval where R>=t the function R(y)+y has strictly positive derivative, because its root denominator R+m>=t+m>y. If R(t)>t, R>=t throughout [0,t]; its sum with y is increasing, giving either the full upper clip (R(0)>=2t) or the unique junction. If R(t)<=t, the set where R>=t is [0,y1] or empty, with R(y1)=t and R(y)+y<=t+y1<=2t there; hence there is no upper clip. These conditions are respectively the displayed t_D and t_U equations. The formulas meet continuously by the jointly continuous clip and bounded integration over compact t-intervals.

Here are the derivatives needed for a certified scan. Write

    B(t;λ)=(16/3)T3+16tT2+16mt^2-8λm,
    C0=T3/3-mT2/2=m/3+(3/2)m^2+m^3,
    P3(d)=(4/3)d^3+2md^2+m^2d.

In R,

    h_λ'(t)/16=C0+tv-P3(d),
    d'=-(2t+m)/(2d+m),
    h_λ''(t)=16[v+(2d+m)(2t+m)]>0.                                      (RC)

In L,

    h_λ'(t)=B(t;λ)+8∫_(R(y)<t)[t^2+2mt+T2+y^2-λ]dy
             >=(16/3)T3-8λm.                                           (LC)

Derivation, not an imported envelope theorem: separate H into its F-independent polynomial part and `8∫G`. Leibniz differentiation contributes the endpoint G(t,t); combining it with the polynomial derivative gives B(t;λ). On upper clipping ∂_t F=2; on lower clipping it is 1; on R it is 0. Moving-breakpoint terms cancel because the two F values agree there. Thus add `16∫_(R>2t-y)∂_zG(2t-y,y)dy` and `8∫_(R<t)∂_zG(t,y)dy` to B.

In R substitute u=t-y in the upper integral. By (JUNCTION) its integrand is `2(u^2-d^2)+2m(u-d)`, whose integral from 0 to d is `-4d^3/3-md^2`. Substitution in B and expansion give the first formula (RC). Differentiating (JUNCTION) gives d'; P3'(d)=(2d+m)^2 gives the positive second derivative. In L the lower integrand is nonnegative precisely because t is to the right of the root R; dropping it and the positive t-terms gives (LC). These arguments also give matching one-sided first derivatives at t_U, where (RC) equals `16(C0+t_Uv)>0`.

## 8. The certified scan and proof of Theorem B

All finite inequalities invoked here are asserted by the displayed §10 cell. A separate exact domain check gave `T2<1/50<4/25<λ_lo<λ_hi<1/2`.

### 8.1 Actual feasible upper law

Use t40,c40 from the code, Y=2t40-c40+m, A=Y^2+c40^2, and the profile

    F40(y)=sqrt(A-y^2)-m on [0,c40],   F40(y)=2t40-y on [c40,t40].

It is continuous at c40; on the arc the slope is between -c40/Y and 0, with c40/Y<1. Hence it satisfies (CAN). Its shell law P_K40 is feasible by §1 and (DIST). In (ZN), N and Z are affine in `θ=arctan(c40/Y)`. Exact alternating arctangent bounds give λ_lo<J(P_K40)<λ_hi. Therefore V<λ_hi<1/2, supplying—not assuming—the hypothesis for §4.4.

### 8.2 D regime

For all g∈[0,1], the sign of d/dg[J(P_g)] is the sign of

    P(g)=g^5+5mg^4+(2m+12m^2)g^3+(12m^3-2m)g^2
         -m(1+2m)(1+6m)g+m^2(1+2m),

since expansion gives `M4'M2-M4M2'=2P`. Its coefficients at m=1/63 have exactly two sign changes. The code certifies `P(0)>0, P(aJ)<0<P(zJ), P(1)>0`, with aJ=3761763123/10^10 and zJ=aJ+10^-10. Descartes' rule therefore gives exactly two simple positive roots r1<aJ<r2<zJ<1, and J increases, decreases, then increases. Since J(P_0)=J(P_1)>J(P_r2), its minimum on [0,1] is J(P_r2). Positive coefficients make M4 and M2 increasing on g>=0, so

    min_(0<=g<=1)J(P_g)>=M4(aJ)/(3M2(zJ))>λ_hi.

For every λ∈[λ_lo,λ_hi], the D-regime g=2t is <1, since `2t<=sqrt(λ-v)-m<1`. Thus h_λ(t)>0 throughout D.

### 8.3 R regime at λ_lo: convexity replaces a grid scan

Parametrize the junction by c, put S=sqrt(λ-v-c^2), and

    t=(S+c-m)/2, d=(S-c-m)/2.                                           (CPAR)

These satisfy (JUNCTION). The code checks 0<c<t at ca,cb and the exact signs `h'(t_a)<0<h'(t_b)`; ta<tb because dt/dc=(1-c/S)/2>0 here. By (RC), the minimum over the ENTIRE rounded interval lies in [ta,tb]. On that interval its tangent at ta gives

    min_R h_(λ_lo) >= h_(λ_lo)(ta)-|h_(λ_lo)'(ta)|(tb-ta)>27/10^35.        (TANGENT)

The final strict inequality is evaluated with rational outward sqrt and arctangent bounds by the code. Convexity makes h larger to the left of ta and to the right of tb, so there is no unscanned t-cell. This is a whole-interval certificate, not a numerical grid or stationary-point assumption.

### 8.4 L regime and conversion to ALL laws

The code certifies `(16/3)T3-8λ_hi m>0`. By (LC), h_(λ_lo) increases throughout L. Its boundary value at t_U is positive by continuity from (TANGENT). Thus h_(λ_lo)(t)>0 for every t>0.

Take an attained original optimum, an optimal phase, and the optimal canonical core C_(t,F) from §§2–5, now authorized mathematically by V<1/2. Then

    (V-λ_lo)Z_C = N_C-λ_lo Z_C = H(t,F;λ_lo)>=h_(λ_lo)(t)>0.

Z_C>0, so V>λ_lo. With §8.1 this proves (B) for ALL original Borel laws, not just symmetrized or shell laws.

## 9. Identification, uniqueness, and parameter boxes at ln 64

At λ=V, the CLIP core is feasible for every t>0, so h_V(t)>=0 everywhere. Each optimal phase's canonical core has H(t,F;V)=0; (CLIP) forces h_V(t)=0 and F=CLIP a.e. Both F and CLIP are continuous by (CAN), so they agree everywhere.

By §8.2 the zero is not in D. By (LC) L is strictly increasing, and it cannot start at zero: its matching left derivative at t_U is `16(C0+t_Uv)>0`, which would give negative h just to the left. Therefore the zero lies in the open R interval. Strict convexity (RC) gives exactly one such zero-minimum t_*, with h_V'(t_*)=0. Every optimal phase is consequently the same normalized shell law of this unique core. By (OPT-MIX), every original optimal measure is that law. This proves Corollary C's existence/uniqueness, without a global-ε assertion.

For the boxes, write A=V-v, S=sqrt(A-c^2) in (CPAR). Let f(c,λ)=h_λ'(t(c,λ))/16. On the rectangle c∈[ca,cb], λ∈[λ_lo,λ_hi], the code proves d>0, c<S and `(2d+m)^2>v`. At fixed c,

    ∂_S f=[v-(2d+m)^2]/2<0,

so f decreases with λ. At fixed λ, dt/dc>0 and (RC) makes f increase with c. Thus

    f(ca,V)<=f(ca,λ_lo)<0<f(cb,λ_hi)<=f(cb,V).

The unique stationary junction c_* lies between ca and cb. S decreases with c and increases with λ; rational outward sqrt bounds at the rectangle corners give the displayed d_* and t_* boxes. This is precisely part III of the code.

## 10. Complete exact finite certificate

The following cell was executed verbatim in a fresh Python eval kernel before this packet was written. It printed all three PASS lines. It uses only `fractions.Fraction`, integer `isqrt`, and the explicit quadratic field a+b sqrt(D); no binary-float input, numerical solver or interval-library black box is used. `atan_bounds` uses 20 terms, an even count, so the alternating sum is a lower bound and adding the next term is an upper bound. For N/Z affine in θ, the ratio is monotone or constant wherever Z>0, so endpoint ratios enclose it.

For checking the `moments` transcription, the two arc primitives are

    I0=∫_0^c sqrt(A-y^2)dy=[cY+Aθ]/2,
    I1=∫_0^c y^2 sqrt(A-y^2)dy=[c(2c^2-A)Y+A^2θ]/8,

where Y=sqrt(A-c^2)>c, θ=arctan(c/Y). Expand F=S_y-m, S_y^2=A-y^2, and integrate the facet 2t-y; substitution in (ZN) is exactly `moments`. The quadratic-field sign routine compares rational squares only when its two terms have opposite signs. Every field calculation in a call uses the same D.

```python
# Certificate for Theorem B / Corollary C (all section references are to THIS packet).
from fractions import Fraction as F
from math import isqrt

class QS:
    """Exact a + b*sqrt(D), D>0 rational."""
    __slots__=('a','b','D')
    def __init__(s,a,b,D): s.a=F(a); s.b=F(b); s.D=F(D)
    def _c(s,o): return o if isinstance(o,QS) else QS(o,0,s.D)
    def __add__(s,o): o=s._c(o); return QS(s.a+o.a,s.b+o.b,s.D)
    __radd__=__add__
    def __neg__(s): return QS(-s.a,-s.b,s.D)
    def __sub__(s,o): return s+(-s._c(o))
    def __rsub__(s,o): return s._c(o)-s
    def __mul__(s,o): o=s._c(o); return QS(s.a*o.a+s.b*o.b*s.D,s.a*o.b+s.b*o.a,s.D)
    __rmul__=__mul__
    def __truediv__(s,o): return QS(s.a/F(o),s.b/F(o),s.D)
    def __pow__(s,n):
        r=QS(1,0,s.D)
        for _ in range(n): r=r*s
        return r
    def sign(s):
        a,b,D=s.a,s.b,s.D
        if b==0: return (a>0)-(a<0)
        if a>=0 and b>0: return 1
        if a<=0 and b<0: return -1
        if a>0: return 1 if a*a>b*b*D else (-1 if a*a<b*b*D else 0)
        return 1 if b*b*D>a*a else (-1 if b*b*D<a*a else 0)
    def bounds(s,lo,hi):
        x=s.a+s.b*lo; y=s.a+s.b*hi; return (min(x,y),max(x,y))

def sqrt_bounds(x,scale=10**70):
    q=x*scale*scale; k=isqrt(q.numerator//q.denominator)
    lo,hi=F(k,scale),F(k+1,scale); assert lo*lo<=x<hi*hi; return lo,hi
def atan_bounds(z,terms=20):
    assert 0<z<1
    s=sum((-1)**k*z**(2*k+1)/F(2*k+1) for k in range(terms))
    return s, s+z**(2*terms+1)/F(2*terms+1)

b=F(1,64); m=b/(1-b); v=m*(1+m)
T2=m+2*m*m; T3=m+6*m*m+6*m**3; T4=m+14*m*m+36*m**3+24*m**4
C0=m/F(3)+F(3,2)*m*m+m**3

def moments(t,c,Ycoef,A,mk):
    """(ZN) of section 6 for the arc/facet profile: N,Z as pairs (r0,r1) meaning r0+r1*theta."""
    add=lambda *p:(sum((q[0] for q in p),mk(0)),sum((q[1] for q in p),mk(0)))
    sc=lambda p,s:(p[0]*s,p[1]*s)
    cst=lambda r:(r,mk(0))
    I0=(Ycoef*(c/2),mk(A/2)); I1=(Ycoef*(c*(2*c*c-A)/8),mk(A*A/8))
    intF  = add(I0, cst(-m*c+2*t*(t-c)-(t*t-c*c)/2))
    intF2 = add(cst(mk(A*c-c**3/3)), sc(I0,-2*m), cst(m*m*c+((2*t-c)**3-t**3)/3))
    intF3 = add(sc(I0,A), sc(I1,-1), cst(mk(-3*m*(A*c-c**3/3))), sc(I0,3*m*m),
                cst(-m**3*c+((2*t-c)**4-t**4)/4))
    inty2F= add(I1, cst(-m*c**3/3+2*t*(t**3-c**3)/3-(t**4-c**4)/4))
    Z = add(sc(add(intF,cst(-t*t/2)),8), cst(8*t*m+2*T2))
    N = add(cst(F(2,3)*T4+F(16,3)*t*T3+4*t*t*T2),
            sc(add(sc(intF,T2),sc(intF2,m),cst(m*t**3/3),sc(intF3,F(1,3)),inty2F,cst(-t**4/3)),8))
    return N,Z

lam_low=F(163006627735070347894185905345794,10**33)
lam_high=F(163006627735070347894185905345795,10**33)
assert v<lam_low<lam_high<F(1,2)

# ---- (I) upper bound: the actual feasible shell law P_K40 (canonical arc/facet profile) ----
def shell_cost(t,c):
    Y=2*t-c+m; A=Y*Y+c*c; z=c/Y; assert 0<c<t and 0<z<1
    N,Z=moments(t,c,Y,A,lambda r:F(r))
    lo,hi=atan_bounds(z); vals=[]
    for th in (lo,hi):
        Zv=Z[0]+Z[1]*th; Nv=N[0]+N[1]*th; assert Zv>0 and Nv>0; vals.append(Nv/Zv)
    return min(vals),max(vals)
t40=F(1882704899884405717532381874371113060926,10**40)
c40=F(92748081344953973231659959220098184342,10**40)
Jlo,Jhi=shell_cost(t40,c40)
assert lam_low<Jlo<=Jhi<lam_high
print('PASS I   V_J <= J(P_K40) < lam_high')

# ---- (II) H_min(t;lam_low)>0 for every t>0 (section 7 regimes) ----
def canonical_R(c,lam):
    A=lam-v; Dv=A-c*c; assert Dv>0
    S=QS(0,1,Dv); mk=lambda r: QS(r,0,Dv)
    t=(S+(c-m))/2; d=(S-(c+m))/2
    Ht16=C0+t*v-(F(4,3)*d**3+2*m*d*d+m*m*d)
    N,Z=moments(t,c,S,A,mk)
    H=(N[0]-Z[0]*lam, N[1]-Z[1]*lam)
    return dict(t=t,d=d,Ht16=Ht16,H=H,Dv=Dv)
def H_interval(c,lam):
    r=canonical_R(c,lam); slo,shi=sqrt_bounds(r['Dv'])
    thlo,_=atan_bounds(c/shi); _,thhi=atan_bounds(c/slo)
    al=r['H'][0].bounds(slo,shi); be=r['H'][1].bounds(slo,shi)
    pr=[be[0]*thlo,be[0]*thhi,be[1]*thlo,be[1]*thhi]
    return r,(al[0]+min(pr),al[1]+max(pr)),(slo,shi)
# (IIa) diamond regime: J(P_g) >= J(P_r2) > lam_high for all g in [0,1]
Pc=[m*m*(1+2*m), -m*(1+2*m)*(1+6*m), 12*m**3-2*m, 2*m+12*m*m, 5*m, F(1)]
sg=[x>0 for x in Pc]; assert sum(sg[i]!=sg[i+1] for i in range(5))==2
Pq=lambda x: sum(c_*x**i for i,c_ in enumerate(Pc))
M2q=lambda x: x*x+2*m*x+T2
M4q=lambda x: x**4+4*m*x**3+6*T2*x*x+4*T3*x+T4
aJ=F(3761763123,10**10); zJ=F(3761763124,10**10)
assert Pq(0)>0 and Pq(aJ)<0<Pq(zJ) and Pq(1)>0
assert M4q(aJ)/(3*M2q(zJ))>lam_high
# (IIb) rounded regime: convexity (RC) + tangent bound around the stationary junction
ca=F(9274808134495397323165995922,10**30); cb=F(9274808134495397323165995923,10**30)
ra,(Hal,Hah),(sal,sah)=H_interval(ca,lam_low); rb,(Hbl,Hbh),(sbl,sbh)=H_interval(cb,lam_low)
assert ra['Ht16'].sign()<0<rb['Ht16'].sign()
assert ra['d'].bounds(sal,sah)[0]>0 and rb['d'].bounds(sbl,sbh)[0]>0 and ca>0
ta_lo=ra['t'].bounds(sal,sah)[0]; tb_hi=rb['t'].bounds(sbl,sbh)[1]
ht=ra['Ht16'].bounds(sal,sah); slope=16*max(abs(ht[0]),abs(ht[1]))
assert Hal-slope*(tb_hi-ta_lo)>F(27,10**35)
# (IIc) lower-clip regime: H' >= (16/3)T3-8*lam*m > 0
assert F(16,3)*T3-8*lam_high*m>0
print('PASS II  H_min(.;lam_low)>0 on diamond, rounded and lower-clip regimes')

# ---- (III) boxes for the optimizer's junction, facet width and diagonal parameter ----
c_hi=cb
assert canonical_R(ca,lam_low)['Ht16'].sign()<0 and canonical_R(c_hi,lam_high)['Ht16'].sign()>0
S_lo=sqrt_bounds(lam_low-v-c_hi*c_hi)[0]; S_hi=sqrt_bounds(lam_high-v-ca*ca)[1]
d_lo=(S_lo-c_hi-m)/2; d_hi=(S_hi-ca-m)/2; t_lo=(S_lo+ca-m)/2; t_hi=(S_hi+c_hi-m)/2
assert d_lo>0 and (2*d_lo+m)**2>v and c_hi<S_lo
assert F(17899568185394517443007219151,10**29)<d_lo<=d_hi<F(17899568185394517443007219152,10**29)
assert F(18827048998844057175323818743,10**29)<t_lo<=t_hi<F(18827048998844057175323818744,10**29)
print('PASS III c_* in (ca,cb); d_* and t_* in 29-digit boxes')
```

Supplementary separate exact controls (not imported proof premises): sparse Fraction polynomial arithmetic checked (DIAMOND)'s Z/N substitutions, the facet integrand, the B-to-RC expansion, C0, P3'(d), implicit d', and the triangular slice moment identity; all printed True. Another cell checked `M4'M2-M4M2'=2P`, both arc antiderivative numerators after clearing sqrt(A-y^2), the four facet integrals used in `moments`, and P's endpoint values; all C1–C9 printed True. Bounded 80-term rational geometric-sum comparisons were consistency checks only, not replacements for the infinite-series derivation in §6. Prior Decimal/float root location and quadrature were diagnostic only and supply no bound in this packet.

The separate domain assertion was:

```python
from fractions import Fraction as RF
regime_m=RF(1,63)
regime_T2=regime_m+2*regime_m**2
regime_lo=RF(163006627735070347894185905345794,10**33)
regime_hi=regime_lo+RF(1,10**33)
assert regime_T2 < RF(1,50) < RF(4,25) < regime_lo < regime_hi < RF(1,2)
print('PASS DOMAIN: T2 < 1/50 < 4/25 < lambda_lo < lambda_hi < 1/2')
```

It was separately executed successfully; the main cell's PASS is not represented as checking this additional assertion.

## 11. Review boundary and precise residual

This packet supplies a complete AUTHOR-WRITTEN route to the lower half at ε=ln 64 and to its instance-specific identification. All original quantifiers are retained in the reduction; no selected state or lattice-only privacy model replaces (DP).

The mathematical claims still require full hostile review and parent disposition. Priority review points: §3's exact fiber inclusion and strict equality; §4.1's a.e.-to-essential-support argument; §4.2's every-line centered sections; §4.3's exact closed-shift inclusion; §4.4's minimal-shell sign; §5's anti-diagonal segment proof of the slope bound; §6's full triangle contribution; §7's moving-boundary derivatives; §8's convex-tangent certificate and all three regimes; §9's uniqueness and box monotonicity.

Exact arithmetic checks finite computations only. They are not Lean/kernel/formal verification of the measure geometry, independent-model or human review, source-equivalence, novelty/priority clearance, automatic acceptance of any older packet, or parent adoption. No general-ε all-law optimum theorem is claimed here. The earlier `frontier-20261029-ln64-tight-bracket-certificate-v1.md` remains frozen at SHA `cb816595dff4c4f6466dee7023a3918725cbf1654fabc4262dfa28fe0c8fc746`, with its explicitly LAW642-conditional wording; this new packet does not retroactively relabel it. All prior process findings, quarantines, NONINPUT boundaries and the unchanged research deadline remain.
