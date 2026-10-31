# The N=2 coupled first-variation/complementarity system at the f261 interface

Owner: InfoResearch96h-2 / info-1. Native clock observed before drafting: `Thu Oct 29 19:05:34 PDT 2026`.

**AUTHOR-WRITTEN DERIVATION, UNREVIEWED.** This is the coupled-system deliverable requested by Main for the ORIGINAL f261 joint nonparallel finite-prefix problem at N=2: arbitrary canonical profiles F_0, F_1 with the actual coupling `C_0+D⊆C_1` and the exact geometric tail from C_1 — not independently chosen cores, not the diamond specialization. It uses only valid f261 inputs: the finite-profile reformulation (B1)–(B5), its exact moment/tail formulas, and the canonical profile class. No held output, no global claim, no diamond-subclass extension.

**Standing labeling correction (per Main):** the previous note `frontier-20261029-n2-diamond-diamond-subclass-closed-v1.md` (SHA `cb46deb6…`), together with its addendum `…-addendum-1-equality-case-v1.md` (SHA `a4b09384…`), is a COROLLARY of the already-supported f238 fixed-core gap-removal theorem — not a new frontier theorem and not an all-law N=2 solution. It is not extended further here.

## 0. Conditional standing of the N=2 problem

For ε>=ε0 the adopted N=1 result gives V<=1/2, so the actual-V cutoff `ceil(sqrt(2V))` is 1 and the N=2 system below is VACUOUS there. The system is derived under the CONDITION that the actual cutoff is 2, i.e. `1<sqrt(2V)<=2`. Whether that condition ever holds (equivalently V>1/2) is OPEN and is NOT attacked here; per Main's release requirement the range `0<ε<ε0` is not being solved. Everything below is conditional system-derivation at the interface, which is the requested deliverable.

## 1. The N=2 functional and its two blocks

Fix ε>0, b=e^(-ε), m=b/(1-b), v=m(1+m), T2=m+2m², T3=m+6m²+6m³, T4=m+14m²+36m³+24m⁴. Let G be geometric with P(G=j)=(1-b)b^j. For canonical profiles (t_0,F_0), (t_1,F_1) satisfying the f261 coupling (B1 at i=0):

    t_1>=t_0+1/2,
    F_1(y)>=F_0(y)+1              for 0<=y<=t_0,
    F_1(y)>=2t_0+1-y              for t_0<=y<=t_0+1/2,                (CPL)

the phase has levels C_0, C_1, C_1+jD (j>=1), and by the f261 formulas (B2)–(B3):

    Z=(1-b)A_0+b·Z_tail(t_1,F_1),
    N=(1-b)Q_0+b·N_tail(t_1,F_1),
    A_0=8∫_0^{t_0}(F_0-y)dy,
    Q_0=8∫_0^{t_0}[(F_0³-y_0³... )] — precisely Q_0=8∫_0^{t_0}[(F_0³-y³)/3+y²(F_0-y)]dy,
    Z_tail=8∫_0^{t_1}(F_1-y)dy+8t_1m+2T2,
    N_tail=(2/3)T4+(16/3)t_1T3+4t_1²T2+8∫_0^{t_1}[T2F_1+m(F_1²+y²)+F_1³/3+y²F_1-4y³/3]dy.

Put H_λ=N-λZ. Both blocks are pointwise convex in their profile variable: writing y for the height,

    C_0-block integrand derivative:  ∂/∂F_0 = 8[F_0²+y²-λ],
    C_1-block integrand derivative:  ∂/∂F_1 = 8[(F_1+m)²+v+y²-λ].

Define the two root functions

    R_0(y)=sqrt(max(λ-y²,0))            (C_0-only root; NO m-shift),
    R_1(y)=sqrt(max(λ-v-y²,0))-m        (C_1 tail root).

## 2. Independent roots are infeasible: the coupling is always active on the free-free region

Since v>0 and m>0, whenever both roots are real, `R_1(y)=sqrt(λ-v-y²)-m < sqrt(λ-y²)=R_0(y)`. The unconstrained joint point (F_0,F_1)=(R_0(y),R_1(y)) violates F_1>=F_0+1. Therefore at every interior optimum the coupling (CPL) is ACTIVE wherever both profiles are strictly inside their canonical box bounds t_i<F_i<2t_i-y.

## 3. The coupled root equals R_1 exactly

On an active interval F_1=F_0+1 and the feasible variations are: move the pair together (F_0+=δ, F_1+=δ), raise F_1 alone, or lower F_0 alone. Joint stationarity for the together-move is

    (1-b)[S²+y²-λ]+b[(S+1+m)²+v+y²-λ]=0,   S=F_0.                    (JS)

**Identity.** The positive solution of (JS) is exactly `S(y)=R_1(y)=-m+sqrt(λ-v-y²)`.

Written proof: put w=sqrt(λ-v-y²), so λ=w²+v+y². Then S=w-m, S+1+m=w+1, and

    S²+y²-λ=(w-m)²+y²-(w²+v+y²)=-2mw+m²-v=-m(1+2w)  [since v-m²=m],
    (S+1+m)²+v+y²-λ=(w+1)²+v-(w²+v)=2w+1.

Hence the left side of (JS) is `(1-b)(-m)(1+2w)+b(1+2w)=(1+2w)(b-(1-b)m)=0` because `m=b/(1-b)`. (Convexity in S of the together-direction second derivative 2(1-b)+2b>0 makes this the minimum.) The one-sided conditions also hold at S=R_1: raising F_1 alone has derivative (1+2w)>=0; lowering F_0 alone has derivative -m(1+2w)<=0. So the active-coupling optimum is F_0=R_1, F_1=R_1+1.

Exact rational spot-check: the identity was verified at 90 rational (w,m,y²) triples by exact Fraction arithmetic (diagnostic only; the written proof above is the argument).

## 4. The coupled complementarity system (the deliverable)

Let (F_0,F_1) be an optimal pair with value λ=V, under the standing condition of §0. Then, a.e. in y:

**(P1) C_0 profile.** On [0,t_0], F_0 is the clip of the SAME root R_1 onto its own box:

    F_0(y)=min(2t_0-y, max(t_0, R_1(y))).

Reason: on the free interior F_0=R_1 by §3; the box clips are the projections, by pointwise convexity of the C_0-block integrand.

**(P2) C_1 profile.** On [0,t_1], F_1 is the clip of the shifted root R_1+1 onto the coupling-adjusted box:

    F_1(y)=min(2t_1-y, max(t_1, L(y), R_1(y))),
    L(y)=F_0(y)+1           on 0<=y<=t_0,
    L(y)=2t_0+1-y           on t_0<y<=t_0+1/2,
    L(y)=-infinity          on t_0+1/2<y<=t_1.

Moreover wherever F_0(y)=R_1(y) (F_0 free), the value max(t_1,L,R_1) equals R_1+1 whenever R_1>=t_0... specifically: if R_1(y)>t_0 then L=F_0+1=R_1+1>R_1 and F_1=R_1+1 (active coupling, rigid translate); if R_1(y)<=t_0 then F_0=t_0 and F_1=max(t_1,t_0+1,R_1)=max(t_1,t_0+1) (coupling active iff t_1<t_0+1, slack iff t_1>=t_0+1). In particular the free-free part of the optimal pair is the RIGID DIAGONAL TRANSLATE

    F_1(y)=F_0(y)+1  wherever  t_0<F_0(y)<2t_0-y  and  F_1<2t_1-y.    (RIGID)

**(P3) Two scalar envelope equations.** The remaining unknowns are (t_0,t_1) with t_1>=t_0+1/2. With the profiles given by (P1),(P2), the reduced two-parameter functional `λ-red(t_0,t_1)=N/Z` must satisfy

    ∂/∂t_0 [N-VZ]=0,   ∂/∂t_1 [N-VZ]=0

at the optimum (envelope derivatives of the clipped functionals, computable in closed form by the endpoint-plus-box-boundary terms exactly as in the N=1 envelope calculus). These are two explicit scalar equations in (t_0,t_1,V).

**Summary of the reduction.** The joint nonparallel N=2 profile problem reduces EXACTLY to the two scalars (t_0,t_1): F_0 is the R_1-clip at t_0, F_1 is the (R_1+1)-clip at t_1 subject to the coupling floors, and (t_0,t_1) solve (P3) with the value V=N/Z. The C_0-only root R_0 never appears in the optimizer.

## 5. Exact first unproved steps (not done here)

1. **Existence/uniqueness of the (t_0,t_1) solution** of (P3): no existence, uniqueness or regime analysis of the two scalar equations is established. The N=1 convexity mechanism (single strictly convex regime) has no established analogue for the coupled pair; the t_0-block derivative is `8[F_0²+y²-λ]` WITHOUT the m-shift, so the two blocks' regime boundaries differ and the joint analysis is open.
2. **Consistency/attainment:** it is not proved that the clipped shapes (P1),(P2) satisfy (CPL) for all candidate (t_0,t_1) (corner interactions of the two clips), nor that the minimum over the two-scalar family is attained.
3. **Standing condition:** whether `1<sqrt(2V)<=2` ever holds (V>1/2) is open; the system is conditional.
4. **Boundary cases:** t_1=t_0+1/2 (tight corner) and t_1>=t_0+1 (slack coupling on the lower-clipped region) need separate envelope treatment in (P3).

## 6. Diagnostics disclosed

- Exact Fraction spot-check of the §3 identity: 90 rational triples, all zero. Diagnostic only.
- An earlier throwaway symbolic-polynomial script for §3 crashed (a helper accepted a dict where a scalar was expected); it is disclosed as a failed diagnostic and is non-evidence; the written proof and the corrected spot-check stand.
- No grid search over (t_0,t_1) was run; per Main's instruction no favorable-grid claims are made or implied.

## 7. Status

AUTHOR-WRITTEN, UNREVIEWED, NOT ADOPTED. Premises: f261 (B1)–(B5) machinery only, plus standard convexity/envelope calculus at the written level. The diamond-diamond corollary labeling of §standing is part of this packet's compliance. All historical NONINPUT boundaries hold. The open items are exactly §5.
