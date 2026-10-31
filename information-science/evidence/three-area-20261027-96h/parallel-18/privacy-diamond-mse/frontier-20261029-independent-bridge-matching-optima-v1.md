# Independent bridge: unique matching-norm optima, unconditional L/J separation, LAW642-free ln 64 upper certificate

**AUTHOR CANDIDATE — WRITTEN plus owner-run exact `fractions.Fraction` certificates; NOT independently reviewed or parent-adopted.** Native clock observed before writing: `Thu Oct 29 07:50:02 PDT 2026`.

## 0. Purpose, results and dependency table

Parent disposition `institute/runs/three-area-2026-10-27-96h/dispositions/info-1-conditional-rounded-optimum-cost-incompatibility-parent-v1.md`, SHA-256 `2e0a8019b33575781cc9e9c383d12046890821406482f24cec9e83720b1974f4`, supports two claims only CONDITIONALLY. The explicit premise is that the all-law J optimizer exists uniquely as a convex-core shell for every ε, plus LAW642 screen sufficiency at ε=ln 64. This packet gives an independent bridge:

1. **Theorem 1.** For every ε>0, the first-norm cost `L=E||X||_1` and the l1-square cost `W=E||X||_1^2` each have a UNIQUE optimal law among ALL full-D-private Borel laws. Each is an explicit centered diamond staircase.
2. **Corollary 2.** Every l1-radial private law has `J>=J(P_gJ)`, with equality only for P_gJ. This is an independent replacement of the MDA26 radial bridge.
3. **Corollary 3.** Claim B of the disposition holds with NO premise. `Opt_L={P_gL}` and `inf_(Opt_L)J-V_J=J(P_gL)-V_J>=J(P_gL)-J(P_gJ)>0` for every ε. The exact margins are >37/5000 at ln 64, >3/500 at ln 32 and >1/10000 at ln 2.
4. **Proposition 5.** At ε=ln 64 an explicit actual full-D-private rounded-core law has certified cost below `163006627735070347894185905345799/10^33`. Hence the UPPER half of Claim A, `V_J<1630066277350704/10^16`, holds without LAW642. It also improves the adopted d67 competitor by more than 2.4×10^-7.
5. **Not established here:** the LOWER half `V_J>1630066277350703/10^16`, and the existence/uniqueness/shell identification of the J optimizer. These remain exactly the LAW642 premise. §7 lists what an independent proof still needs.

| Result | Research premise used | Standard mathematics used |
|---|---|---|
| Theorem 1, Corollaries 2–3 | **none** | Lebesgue differentiation, Tonelli, Brunn–Minkowski for compact planar sets, inner regularity, Prokhorov/weak closure, lower semicontinuity, layer cake/bathtub, Descartes' rule, IVT |
| Corollary 4 (ln 64 all-radial gap) | parent-adopted competitor `dispositions/info-1-ln64-nonradial-staircase-gap-parent-v1.md`, SHA `d67b0ac9cbde8c6d1f81f0f407106070ea3cee640984b4d166929b12d6dd6516`, plus Corollary 2 | — |
| Proposition 5 (ln 64 upper bound) | **none** | elementary geometry, exact integrals, alternating arctangent bounds |
| ln 64 lower half, J-optimizer identification | LAW642 parent `privacy-all-law-self-contained-parent-v1.md`, SHA `c08f6353f121ef9e35da0e9d5e8ec9c87b0da838be0d1adf38b807010a1cd979`, and source SHA `957cab2bcf3eff1860ff9f4b5a1e5838708aceaf894a97fdc2c5244c3e7d8e53` | not verified here |

No held material, MDA26 source text or f161/f162 material was opened or used.

## 1. Model and notation

Fix ε>0, b=e^(-ε), m=b/(1-b), and `D={h:||h||_1<=1}` (FULL closed diamond). F is the set of ALL Borel probability laws μ on R^2 with `μ(A)<=b^(-1)μ(A+h)` for EVERY Borel A and EVERY h∈D. We write

    L(μ)=E||X||_1,  W(μ)=E||X||_1^2,  J(μ)=E|X|_2^2,

and V_L, V_W, V_J for their infima over F. Let N have law `(1-b)b^k`, k>=0. Its moments are EN=m, `T2=EN^2=m+2m^2`, `T3=m+6m^2+6m^3` and `T4=m+14m^2+36m^3+24m^4`; set `M_j(g)=E(g+N)^j`. For g>=0, P_g is the centered diamond staircase with density `b^(max(0,ceil(||x||_1-g)))/(2M2(g))`; as laws, P_0=P_1. Put

    Q(g)=g^4+4mg^3+6m^2g^2-2m(1+3m)g+m^2,
    P(g)=g^5+5mg^4+(2m+12m^2)g^3+(12m^3-2m)g^2-m(1+2m)(1+6m)g+m^2(1+2m).

## 2. Theorem 1: unique first-norm and l1-square optima

**Theorem 1.** For every ε>0 and φ∈{φ_1(r)=r, φ_2(r)=r^2}, the cost `C_φ(μ)=E φ(||X||_1)` has exactly ONE minimizer in F. It is `P_gL` for φ_1 and `P_gJ` for φ_2, where g_L and g_J are the larger positive roots of Q and P, both in (0,1). Thus `V_L=(2/3)M3(g_L)/M2(g_L)` and `V_W=M4(g_J)/(2M2(g_J))`.

### 2.1 Existence

The product Laplace law `(ε^2/4)e^(-ε||x||_1)` is in F with finite C_φ. A minimizing sequence is tight by Markov's inequality; Prokhorov gives a weakly convergent subsequence. For fixed h∈D and nonnegative f∈C_b, `∫f dμ_n<=b^(-1)∫f(x-h)dμ_n(x)` passes to the limit. Two finite Borel measures ordered on nonnegative C_b functions are ordered on all Borel sets (closed-set approximation and regularity), so the limit is in F. C_φ is weakly lower semicontinuous (truncate φ at level R). A minimizer therefore exists.

### 2.2 All-point private density

Integrating the privacy inequality over h∈D and using Tonelli, `∫_D μ(A+h)dh=∫|D∩(x-A)|dμ(x)<=|A|`, hence `μ(A)<=|A|/(2b)`. So μ has a density bounded by 1/(2b). Let `f(x)=limsup_(r↓0,r rational) μ(B_r(x))/|B_r|` over open Euclidean balls. Then f is Borel, `f<=1/(2b)`, and f=dμ/dx a.e. by Lebesgue differentiation. Because `μ(B_r(x))<=b^(-1)μ(B_r(x+h))` for each r, we get `f(x+h)>=bf(x)` for EVERY x and EVERY h∈D.

### 2.3 Private l1-radial rearrangement and strictness

For s>0 let `A_s={f>s}`; then `|A_s|<=1/s`. Let `R(s)=sqrt(|A_s|/2)`, which is nonincreasing and right-continuous. The previous step gives `A_s+D⊆A_(bs)`. For compact C⊆A_s, C+D is compact and lies in A_(bs). Brunn–Minkowski gives `|C+D|^(1/2)>=|C|^(1/2)+sqrt(2)`. Inner regularity then yields

    R(bs)>=R(s)+1   whenever R(s)>0.                                      (1)

Define `f#(x)=sup{s>0: ||x||_1<R(s)}` (sup∅=0). Right-continuity gives `{f#>s}={||x||_1<R(s)}`, so f# is equimeasurable with f and is a probability density. If `||y-x||_1<=1` and `||x||_1<R(s)`, then (1) gives `||y||_1<R(bs)`, so `f#(y)>bs`. Taking the supremum over admissible s gives `f#(y)>=bf#(x)` EVERYWHERE; its law μ# is in F.

Layer cake gives `C_φ(μ)=∫_0^∞∫_(A_s)φ(||x||_1)dx ds` and the same with `R(s)D°` for μ#. Write R for R(s). For |A|=|RD|,

    ∫_A φ-∫_(RD) φ = ∫_(A\RD) φ-∫_(RD\A) φ >= φ(R)(|A\RD|-|RD\A|)=0,

and the inequality is STRICT if |A\RD|>0, since φ is strictly increasing and ∂(RD) is null. Hence `C_φ(μ#)<=C_φ(μ)`. If `C_φ(μ#)=C_φ(μ)<∞`, then `|A_s Δ R(s)D|=0` for a.e. s, and Tonelli gives f=f# a.e. **Every minimizer therefore has a density a.e. equal to a radially nonincreasing, everywhere-private f#.**

### 2.4 Phase decomposition into radial phases

Let p=f# for a minimizer and `M=p(0)=sup{s:R(s)>0}∈(0,1/(2b)]`. For a∈[bM,M) set `R_i(a)=R(ab^i)`. Then R_0(a)>0, `R_(i+1)(a)>=R_i(a)+1` by (1), and R_i(a)→∞. Put `n_a(x)=min{i>=0:||x||_1<R_i(a)}` and `u_a=b^(n_a)`. If `||y-x||_1<=1`, then `||y||_1<R_(n_a(x))+1<=R_(n_a(x)+1)`, so `u_a(y)>=bu_a(x)`.

**Identity:** for every x, `∫_(bM)^M u_a(x)da=(1-b)p(x)`. Indeed, with y=p(x)∈(0,M], a=Mb^σ (σ∈(0,1]) and `κ=log_b(y/M)>=0`, n_a(x) is the least integer n>=0 with σ+n>κ. So w=σ+n_a runs bijectively over (κ,κ+1], and

    ∫ b^(n_a) da = ∫_0^1 M b^(σ+n_a)|ln b| dσ = ∫_κ^(κ+1) M b^w |ln b| dw = (1-b)y.

Let Φ(R)=∫_(RD)φ(||x||_1)dx=∫_0^R φ(r)4r dr. Then `Z_a=∫u_a=(1-b)Σ_i b^i 2R_i(a)^2` and `N_a=∫φu_a=(1-b)Σ_i b^iΦ(R_i(a))`. By Tonelli `∫Z_a da=1-b` and `∫N_a da=(1-b)C_φ(μ)<∞`, so both are finite for a.e. a. With weights `w(a)=Z_a/(1-b)>0` (∫w=1) and phase laws `P_a=u_a/Z_a∈F`,

    μ=∫w(a)P_a da,       C_φ(μ)=∫w(a)C_φ(P_a)da.

Since C_φ(P_a)>=V_φ=C_φ(μ), **almost every phase P_a is itself a minimizer.**

### 2.5 Gap lemma: optimal radial phases have unit spacing

A *radial phase* is a sequence with 0<R_0 and R_(i+1)-R_i>=1, and finite Z and N. Its law, with density b^i on `{R_(i-1)<=||x||_1<R_i}`, is in F by the same index argument. Suppose it attains v=V_φ>0. Set `H(R)=Φ(R)-2vR^2`, so that `Σ_i b^iH(R_i)=(N-vZ)/(1-b)`. This sum is 0 for the optimal phase and >=0 for every radial phase. Since `H'(R)=4R(φ(R)-v)`, H is strictly decreasing on [0,ρ_v] and strictly increasing on [ρ_v,∞), where ρ_v=v for φ_1 and sqrt(v) for φ_2.

Suppose some `R_(i+1)-R_i>1`.

* If R_(i+1)>ρ_v, lower all R_j (j>=i+1) by a small δ. The sequence stays admissible, every H(R_j) strictly decreases, and the sum becomes negative: some feasible law beats V_φ, which is impossible.
* If R_(i+1)<=ρ_v, then R_j<ρ_v for all j<=i. Raising R_0..R_i by a small δ is admissible and again makes the sum negative.

Hence **R_(i+1)=R_i+1 for all i.**

### 2.6 Scalar step (endpoint exclusion via C'(1)>0)

With R_i=t+i (t>0) the phase law is P_t, and `C_(φ_1)(P_t)=(2/3)M3(t)/M2(t)`, `C_(φ_2)(P_t)=M4(t)/(2M2(t))`. The exact polynomial identities in (t,m), checked in §9,

    M3'M2-M3M2' = Q,        M4'M2-M4M2' = 2P,                             (2)

show that the costs' derivatives have the signs of Q and P. Both polynomials have exactly two coefficient sign changes. Their endpoint values are `Q(0)=m^2`, `Q(1)=(1+m)^2`, `P(0)=m^2(1+2m)` and `P(1)=(1+m)^2(1+2m)`, all positive. In x=g+m, v=m(m+1), τ=1+2m=sqrt(1+4v),

    Q=x^4-2vτx+3v^2,    P=x^5+2vx^3-2vτx^2-v(1+3v)x+2v^2τ,

and at `g0=sqrt(v)-m∈(0,1)`, `Q=2v^(3/2)(2sqrt(v)-τ)<0` and `P=-v^(3/2)<0`. So each has exactly two simple positive roots, both in (0,1). Each cost is increasing on (0,r_1), decreasing on (r_1,g_φ) and STRICTLY increasing on (g_φ,∞). The laws P_0 and P_1 are equal, and 1∈(g_φ,∞), which is where `C'(1)>0` enters. Hence C(0)=C(1)>C(g_φ), and the unique minimizer over t>0 is g_φ. The optimal radial phase is therefore P_(g_φ).

### 2.7 Conclusion

By §§2.3–2.6, a.e. phase of any minimizer equals P_(g_φ), so `μ=∫w(a)P_(g_φ)da=P_(g_φ)`. With §2.1 this proves existence and uniqueness. This reconstructs, for these two costs in this 2D l1 model, the known staircase-optimality conclusion of the matching-norm literature (positive prior ancestry, including MDA26's matching-norm theorem) and adds uniqueness. **No novelty or priority is claimed.**

## 3. Corollary 2: all l1-radial laws for J

If μ∈F has a density a.e. equal to a function of ||x||_1, then `J(μ)=(2/3)W(μ)`. In each quadrant, the coordinates `x=(ru,r(1-u))` have Jacobian r, so u is uniform on [0,1] and independent of r, and `E[u^2+(1-u)^2]=2/3`. Hence `J(μ)>=(2/3)V_W=J(P_gJ)`, with equality iff μ=P_gJ by Theorem 1. On staircases `J(P_g)=M4/(3M2)`, so the scalar J minimizer is g_J.

## 4. Corollary 3: Claim B without any premise

By Theorem 1, Opt_L={P_gL}. Also g_L<g_J strictly. Let `R=2x^3-(1+6v)x+2vτ`; exact multiplication gives P=xQ+vR. At Q=0, `R=[3(x^2-v)^2-x^2]/x`. With `z=x_L^2/v>1` (since g_L>g0), the Q-root equation and τ^2=1+4v give

    1/v-3(z-1)^2/z=(z-1)^3(z+3)/(4z)>0,

so R<0 and P(g_L)<0. Thus g_L lies strictly between P's two roots, and g_L<g_J. Since g_J is the unique minimizer of J(P_g) over g>0,

    inf_(μ∈Opt_L) J(μ)-V_J = J(P_gL)-V_J >= J(P_gL)-J(P_gJ) > 0   for every ε>0.   (3)

No restricted-infimum compactness or J-optimizer premise is needed. Exact Fraction certificates (§9A) give lower bounds on the margin `J(P_gL)-J(P_gJ)`: more than 37/5000 at ε=ln 64, more than 3/500 at ε=ln 32 and more than 1/10000 at ε=ln 2.

## 5. Corollary 4: no l1-radial law is J-optimal at ln 64

The parent-adopted d67 result says that `J(P_S)+10^(-6)<J(P_γ)` for every centered diamond staircase. By Corollary 2 the infimum over ALL l1-radial private laws is `J(P_gJ)`. Hence every l1-radial law has `J>J(P_S)+10^(-6)`. This is the optional all-radial strengthening that d67 declined to admit without MDA26. Here it rests on the new, unreviewed Corollary 2 instead.

## 6. Proposition 5: a LAW642-free upper certificate at ε=ln 64

### 6.1 Core

For 0<c<t set Y=2t-c+m, A=Y^2+c^2 and z=c/Y. Use the first-octant profile

    F(y)=sqrt(A-y^2)-m  on [0,c],    F(y)=2t-y  on [c,t],

and let K be the D4 orbit (closed) of {0<=y<=t, y<=x<=F(y)}. Then F is continuous (F(c)=2t-c) and nonincreasing, with `F'>=-z>-1` on the arc. Also F(t)=t, `F(y)>=t>=y`, and F(y)+y is nondecreasing, so `F(y)+y<=2t`.

### 6.2 Distance and privacy

For x∈Q1, axis reflections and the down-set property of K∩Q1 give `d_1(x,K)=x1+x2-max{k1+k2:k∈K∩Q1,k<=x}`. In octant 1 (x1>=x2>=0), using that F(y)+y is nondecreasing with maximum 2t at y=t,

    d_1(x,K)=(x1-F(x2))_+  if x2<=t,       d_1(x,K)=x1+x2-2t  if x2>t.

The shell law P_K has density `b^(ceil(d_1(x,K)))/Z_K`. It is in F because `|d_1(x+h,K)-d_1(x,K)|<=1` for h∈D.

### 6.3 Exact moments

Write K_k=K+kD={d_1<=k}. In octant 1, for y<=t the slice of K_k is y<=x<=F(y)+k; for t<=y<=t+k/2 it is y<=x<=2t+k-y. Exact integration gives the tail-layer polynomials `k^2/4` (area) and `k^4/12+tk^3/3+t^2k^2/2` (second moment), both checked as identities in (t,k) in §9. The layer identity `b^(ceil d)=(1-b)Σ_k b^k 1_(K_k)` and the moments of N then give

    Z_K = 8∫_0^t(F-y)dy + 8tm + 2T2,
    N_K = (2/3)T4 + (16/3)tT3 + 4t^2T2 + 8∫_0^t[T2F + m(F^2+y^2) + F^3/3 + y^2F - (4/3)y^3]dy.

On the arc, `∫_0^c sqrt(A-y^2)dy=(cY+Aθ)/2` and `∫_0^c y^2sqrt(A-y^2)dy=(c(2c^2-A)Y+A^2θ)/8`, where `θ=asin(c/sqrt(A))=atan(z)` because sqrt(A-c^2)=Y. The second antiderivative was checked by differentiation. Everything else is polynomial, so Z_K,N_K∈Q+Qθ and J(P_K)=N_K/Z_K is monotone in θ.

### 6.4 Certificate

Take m=1/63, t=1882704899884406/10^16 and c=92748081344954/10^16. Rational alternating bounds on atan(z) give the exact rational enclosure

    163006627735070347894185905345798/10^33 < J(P_K) < 163006627735070347894185905345799/10^33,
    339888889366/10^12 < Z_K < 339888889367/10^12.

Therefore, **without LAW642,**

    V_J(ln 64) <= J(P_K) < 1630066277350704/10^16,    J(P_S)-J(P_K)>24/10^8,

where P_S is the adopted d67 competitor. A separate FLOAT direct layer quadrature, summing 40 layers in each octant region, gave Z≈0.339888889366123 and J≈0.163006627735071. This is a diagnostic only. If LAW642 holds, its root value λ_* ≤ J(P_K); this is consistent with the conditional bracket and does not certify it.

## 7. What remains conditional, and the next step

The LOWER half needs `J(μ)>=λ_low` for EVERY μ∈F. A LAW642-free route, NOT completed here, is:

* (R1) existence, as in §2.1;
* (R2) phase decomposition for nonradial f with `K_i={f>ab^i}` and K_i+D⊆K_(i+1), as in §2.4;
* (R3) four Steiner symmetrizations (axes and diagonals) preserve exact Minkowski inclusions slice-by-slice and strictly lower ∫|x|^2 unless the set is invariant, so optimal phases are D4-symmetric and 4-direction convex;
* (R4) minimal shells K_i=K_0+iD: once (R3) supplies a point of K_0 at (or arbitrarily near) the origin, K_0+D contains B(0,sqrt(λ)) whenever sqrt(2λ) is below 1 by that margin (e.g. λ<1/2 with 0∈K_0), so excess shell area only adds positive |x|^2-λ;
* (R5) the octant geometry of §6.2 and pointwise convexity of the integrand in F; every such profile has F(y)∈[t,2t-y], so `H(t,F;λ)>=H(t,CLIP;λ)`;
* (R6) a certified one-variable verification that `min_t H(t,CLIP;λ_low)>0`.

(R1), (R2) and (R5) are direct extensions of §§2 and 6. The remaining work is (R3)–(R4), where exact measurable representatives are needed, and the certified t-scan (R6). Until those are done, the J-optimizer identification and V_J>λ_low remain LAW642-conditional.

## 8. Corrections acknowledged

f158 corrected consolidated-packet LF151: `J'(1)>0`, not `J'(0)>0`, excludes the equal endpoint laws. The same incorrect justification appears in my earlier unreviewed `frontier-20261028-all-epsilon-mean-j-gap-law-only-v1.md` (SHA `5964bb8caa8588935de115f864b095d6678198380cebbfaa3cd63df2932ae0e9`) LF49, and in `frontier-20261028-all-epsilon-mean-j-gap-two-premises-v1.md` (SHA `3ed8c0cc98f82484dee9f56b466d616717a8d9192f9b82bd1b6217a757e8865c`) LF41. Their conclusions survive by the same J'(1)>0 argument. Those files remain frozen; for Claim B they are superseded by Corollary 3. `frontier-20261028-laplace-nonoptimal-all-epsilon-v1.md` uses J'(0)>0 only for nonconstancy and an MVT sign argument, which remain correct.

## 9. Owner-run exact controls

All assertions below were executed in the owner's Python eval kernel with `fractions.Fraction`; each printed PASS. Float values are labelled diagnostics.

* **Polynomial identities (separate cells).** Over sparse (g,m) polynomials: both identities (2); the x-forms of Q and P; P=xQ+vR; endpoint values at m∈{1/63,1/31,1,5}; `(z^2+3)^2-16z-12(z-1)^2=(z-1)^3(z+3)`; the tail-octant layer polynomials k^2/4 and k^4/12+tk^3/3+t^2k^2/2 by exact polynomial integration in (t,k,y); and T1..T4 against 60-term exact partial sums at b=1/64, with error <10^-60.
* **Arc integrals.** A FLOAT Simpson diagnostic agreed with both closed forms to relative error <3×10^-15.

A. Selector instances and strict L/J margins:

```python
from fractions import Fraction as F
def selector_instance(mv, aL, zL, aJ, zJ, margin):
    Q=lambda x: x**4+4*mv*x**3+6*mv*mv*x*x-2*mv*(1+3*mv)*x+mv*mv
    P=lambda x: (x**5+5*mv*x**4+(2*mv+12*mv*mv)*x**3+(12*mv**3-2*mv)*x*x
                 -mv*(1+2*mv)*(1+6*mv)*x+mv*mv*(1+2*mv))
    T2=mv+2*mv*mv; T3=mv+6*mv*mv+6*mv**3; T4=mv+14*mv*mv+36*mv**3+24*mv**4
    M2=lambda x: x*x+2*mv*x+T2
    M4=lambda x: x**4+4*mv*x**3+6*T2*x*x+4*T3*x+T4
    assert Q(0)>0 and Q(aL)<0<Q(zL) and Q(1)>0
    assert P(0)>0 and P(aJ)<0<P(zJ) and P(1)>0
    assert zL<aJ
    assert M4(aL)/(3*M2(zL)) - M4(zJ)/(3*M2(aJ)) > margin
selector_instance(F(1,63),F(2975366184837612,10**16),F(2975366184837613,10**16),
                  F(3761763123,10**10),F(3761763124,10**10),F(37,5000))
selector_instance(F(1,31),F(3646185443795757,10**16),F(3646185443795759,10**16),
                  F(441266095196338192,10**18),F(441266095196338193,10**18),F(3,500))
selector_instance(F(1),F(7061732346792597254817,10**22),F(7061732346792597254818,10**22),
                  F(7271025149432606453616,10**22),F(7271025149432606453617,10**22),F(1,10000))
print('PASS A')
```

B. LAW642-free ln 64 upper certificate:

```python
from fractions import Fraction as F
b=F(1,64); m=b/(1-b)
T2=m+2*m*m; T3=m+6*m*m+6*m**3; T4=m+14*m*m+36*m**3+24*m**4
def atan_bounds(z):
    s=sum((-1)**k*z**(2*k+1)/F(2*k+1) for k in range(12))
    return s, s+z**25/F(25)
t=F(1882704899884406,10**16); c=F(92748081344954,10**16)
assert 0<c<t
Y=2*t-c+m; A=Y*Y+c*c; z=c/Y; assert 0<z<1
add=lambda *p:(sum(q[0] for q in p),sum(q[1] for q in p))
sc=lambda p,s:(p[0]*s,p[1]*s)
cst=lambda r:(r,F(0))
I0=(c*Y/2, A/2); I1=(c*(2*c*c-A)*Y/8, A*A/8)
intF  = add(I0, cst(-m*c+2*t*(t-c)-(t*t-c*c)/2))
intF2 = add(cst(A*c-c**3/3), sc(I0,-2*m), cst(m*m*c+((2*t-c)**3-t**3)/3))
intF3 = add(sc(I0,A), sc(I1,-1), cst(-3*m*(A*c-c**3/3)), sc(I0,3*m*m),
            cst(-m**3*c+((2*t-c)**4-t**4)/4))
inty2F= add(I1, cst(-m*c**3/3+2*t*(t**3-c**3)/3-(t**4-c**4)/4))
Z = add(sc(add(intF,cst(-t*t/2)),8), cst(8*t*m+2*T2))
N = add(cst(F(2,3)*T4+F(16,3)*t*T3+4*t*t*T2),
        sc(add(sc(intF,T2),sc(intF2,m),cst(m*t**3/3),sc(intF3,F(1,3)),inty2F,cst(-t**4/3)),8))
lo,hi=atan_bounds(z); vals=[]
for th in (lo,hi):
    Zv=Z[0]+Z[1]*th; Nv=N[0]+N[1]*th
    assert Zv>0 and Nv>0
    vals.append(Nv/Zv)
Jlo,Jhi=min(vals),max(vals)
assert F(163006627735070347894185905345798,10**33) < Jlo <= Jhi < F(163006627735070347894185905345799,10**33)
assert F(339888889366,10**12) < Z[0]+Z[1]*lo and Z[0]+Z[1]*hi < F(339888889367,10**12)
JPS=F(4355768046089487574226880288026708390699272667,26721376640271909097532496900000000000000000000)
assert Jhi < F(1630066277350704,10**16) and JPS-Jhi > F(24,10**8)
print('PASS B')
```

The upper-certificate assertions were first run split across two cells (one-sided bounds, then the two-sided J and Z enclosures). Before this file was finalized, block B exactly as displayed was re-executed verbatim as one fresh cell and printed `PASS B`; block A was executed verbatim and printed `PASS A`. Arithmetic checks certify finite computations only; they do not verify the written proofs.

## 10. Scope

This is a WRITTEN author candidate, with all mathematical steps written above and owner-run exact arithmetic. It has no independent, cross-model, human or formal verification, and no parent adoption. The original J problem's lower half and optimizer identification remain LAW642-conditional. Theorem 1 concerns only the two matching-norm costs. No source equivalence, priority or novelty is claimed. Priority review: §2.3 privacy of the rearrangement and its strictness; §2.4 phase identity and a.e. optimality; §2.5 gap-lemma perturbations; §2.6 root and sign analysis; §6.2 octant distance formula; and §6.3 layer integrals.
