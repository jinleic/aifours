# Exact full finite-coordinate low-privacy J/L moment region

**AUTHOR CANDIDATE — WRITTEN with exact finite algebra checks; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 19:17:11 PDT 2026`.

## 1. The region, including the non-Pareto half

Let b=e^(-epsilon)->0, s=b^(1/4), and consider the original ALL Borel, ALL-event, FULL closed l1-unit-diamond-private noise laws. For such a law put `J=E|X|_2^2`, `L=E||X||_1`. Let R consist of all finite pairs (u,v) achievable along actual law sequences with

    J/s^2 ->u,       L/s ->v.                                             (1)

For EVERY REAL theta, let `c_theta(z)=|z|^2+theta||z||_1`, and define the unique threshold `T_theta>min c_theta` by

    integral_R2 (T_theta-c_theta)_+ dz=2/3.                              (2)

Let K_theta={c_theta<=T_theta}, A_theta=|K_theta|, and `V_theta=T'_theta`. The written claim is:

    R = { (u,v) : v>0, u>=U(v) },
    U(v)=T_theta-theta v,  where theta is the UNIQUE real root V_theta=v. (3)

Every boundary point AND EVERY finite vertical ray above it are attained by actual full-D private laws. The inverse theta exists because V_theta is continuous, strictly decreasing from infinity to zero as theta ranges from -infinity to infinity. Thus (3) is the COMPLETE finite-coordinate limiting moment region, not only its Pareto-efficient subregion. Its efficient part is the theta>=0 portion already described in unreviewed `frontier-20261028-critical-pareto-frontier-curvature-v1.md` (SHA-256 `e8215ca79efc28c32409d326a8d783960810d60d8e1b99ca305b0c2a486c32ef`). That prior note and the positive-theta theorem are NOT required imports for the proof here.

The striking exactly elementary part is the high-v boundary. Put `tau=1/sqrt(3pi)` and `v_c=2 sqrt(tau)`. For ALL v>=v_c,

    U(v)=v^2/2+tau.                                                       (4)

Hence the privacy constraint creates a strict additive `1/sqrt(3pi)` asymptotic squared-error toll beyond the elementary pointwise Cauchy lower bound `u>=v^2/2` throughout this half-line. This is a limiting assertion, not a finite-epsilon inequality or a statement that high-v points are Pareto efficient.

## 2. Real-theta threshold and all-law peak-floor bound

For theta>=0, min c=0; for theta=-a<0, min c=-a^2/2. In either case, G(T,theta)=integral(T-c_theta)_+ is continuous and strictly increasing above the minimum, starts at zero and diverges, so (2) is well-defined. K_theta is compact, has positive area and null boundary; for negative theta it may be disconnected. Set `I_theta=integral_(K_theta)c_theta`. Equation (2) is

    T_theta A_theta-I_theta=2/3.                                         (5)

We establish, for EVERY FIXED real theta, the scalarized all-law value and universal moment pair:

    inf_(mu, J<infinity) (J+theta sL) = T_theta s^2+O_theta(s^3),        (6)
    J/s^2 -> T_theta-theta V_theta,   L/s -> V_theta,                    (7)

for EVERY actual scalarized first-order-near-optimal sequence. The infimum for negative theta is over finite-J laws, so there is no undefined infinity-minus-infinity. Equation (6) is a proof device; negative theta rewards larger L, and its optimized laws need not be Pareto efficient.

Every feasible law has a bounded all-point density representative p. Let M=esssup p, select a point x0 with `p(x0)>=(1-s)M`, set `ell=b(1-s)M`, `g=p-ell 1_(x0+D)`, `y=s^2 M`, `g#(z)=s^2 g(sz)` and h=integral g#=1-2ell. Full-D privacy makes g nonnegative, and g#<=y.

For later centering with NEGATIVE theta, define

    Q(x)=integral_(x+D)||u||_1 du - 4/3.

The coordinate marginal of D is `2(1-|t|)_+`; consequently the second derivative of `integral_D |u_i+t|du` is `4(1-|t|)_+` away from endpoints. It follows for all x that

    0<=Q(x)<=2|x|^2.                                                     (8)

Thus the translated floor cost satisfies, for sufficiently small s depending on fixed theta,

    F_s(x)=integral_(x+D)(|u|^2+theta s||u||_1)du
           >= 2/3-O_theta(s)+|x|^2.                                      (9)

This handles negative theta without incorrectly treating its norm term as nonnegative.

For ANY T and cap y, the exact dual identity is

    integral c_theta g# = T h-y integral(T-c_theta)_+ + Delta,
    Delta=integral_(c<T)(T-c)(y-g#)+integral_(c>T)(c-T)g# >=0.            (10)

At T=T_theta, the positive-part integral is 2/3. The exact scaled total cost is `(1-s)y F_s(x0)+integral c_theta g#`. A shell upper law below bounds its normalized value above. Even for negative theta, Cauchy gives `J/s^2+theta L/s >= U-|theta|sqrt(2U)` where U=J/s^2, so such an upper bound forces U uniformly bounded. The squared-cost floor then bounds y above; since h->1, the capped-density squared-cost bathtub forces y away from zero. Substituting (9)–(10) gives

    (J+theta sL)/s^2 >= T_theta+(1-s)y|x0|^2-O_theta(s)y+Delta.         (11)

This proves the lower half of (6), and any first-order nearopt sequence has `x0->0` and `Delta->0`.

## 3. Actual upper law, all-law density limit and component moments

For S=sK_theta, define `n(x)=min{k>=0:x in S+kD}` and the density proportional to b^n. It is a genuine full-event private law by `|n(x+h)-n(x)|<=1` for every h in D. Convexity or connectedness of S is NOT required.

Its k=0 mass integral is s^2 A_theta and its scalarized numerator there is s^4 I_theta. Since K_theta is compact and nonempty, D+sK_theta contains a translate of D and lies inside a D-enlargement by O_theta(s); its symmetric difference with D has area O_theta(s). Consequently its first-shell physical cost integral is `2/3+O_theta(s)`, and k>=2 shell terms have total numerator O_theta(b^2). The exact layer-sum identity gives scalarized cost

    s^2[I_theta+2/3]/A_theta+O_theta(s^3)
      =T_theta s^2+O_theta(s^3).                                         (12)

This supplies the upper half of (6).

For a nearopt sequence, the nonnegative deficit in (10) controls the L1 distance between g# and `y 1_(c_theta<=T_theta)` outside an arbitrarily thin threshold band. The level set is null and the band is contained in a bounded sublevel, so its area tends to zero as band thickness tends to zero. Thus that L1 error tends to zero. Since h->1, y->1/A_theta and the full scaled law X/s converges in TV to Uniform(K_theta), even when K_theta is disconnected.

The J/s^2 bound gives uniform integrability of the scaled first norm, so `L/s->(1/A_theta)integral_(K_theta)||z||_1`. The identity G(T_theta,theta)=2/3 and differentiation under the bounded integral imply

    V_theta=T'_theta=(1/A_theta)integral_(K_theta)||z||_1.                (13)

Subtracting theta L/s from the nearopt scalarized limit gives J/s^2->T_theta-theta V_theta. This proves (7) without dropping the nonvanishing macroscopic privacy-floor contribution to J.

## 4. Strictly monotone parameter and the separated-disks branch

T is continuous and differentiable in theta by (13), and concave because it is the pointwise limit of infima of affine scalar objectives. It is STRICTLY concave: if equality held between two distinct theta values, an actual middle-theta nearopt shell would, by the nonnegative scalarized gaps, be nearopt for both endpoints. Section 3 would then force the same scaled law to be both Uniform(K_theta1) and Uniform(K_theta2). Equality of these regular-closed positive-area sublevels would force `||z||_1` to be constant on their common boundary by subtracting the two level equations, impossible on a nontrivial circular-quadrant boundary arc. Thus V_theta is continuous and strictly decreasing.

For theta=-a, write

    c_-a(z)=(|z1|-a/2)^2+(|z2|-a/2)^2-a^2/2.

Let tau=1/sqrt(3pi). If `a>=2 sqrt(tau)`, K_-a is exactly four radius-sqrt(tau) disks centered at `(±a/2,±a/2)`, up to shared null boundary points, each disk wholly in its quadrant. Direct integration yields

    integral(T-c_-a)_+ =4 * (pi/2)tau^2 =2/3,
    T_-a=-a^2/2+tau,       V_-a=a.                                        (14)

Thus V_theta->infinity as theta->-infinity and (4) follows for v=a>=v_c. At the opposite end, the rescaling `z=theta^(-1/3)w`, `T=theta^(2/3)t` gives `T_theta~theta^(2/3)`; concavity and secant slopes yield `V_theta~(2/3)theta^(-1/3)->0`. Hence V maps all R bijectively onto (0,infinity).

## 5. Necessity and constructive sufficiency of the ENTIRE region

For every feasible sequence with finite limiting (u,v), scalarization with any real theta and (6) gives `u+theta v>=T_theta`. No finite-u sequence has v=0: the peak floor yields `s^2 M<=3(J/s^2)/2`, and a capped-density l1 bathtub yields `L/s>=2/[3 sqrt(3U)]` whenever J/s^2<=U. For v>0, choose the unique theta with V_theta=v; then `u>=T_theta-theta v=U(v)`.

The shell law of §3 attains `(U(v),v)` and is sign-symmetric, hence EX1=0. For any chosen t>=0, mix it with its translate by e1 with weight `delta=t s^2` (for small s, delta<=1). Both components and their mixture are full-D private. Exactly

    J(mixture)=J(shell)+delta,
    |L(mixture)-L(shell)|<=delta.

Thus the mixture has limit `(U(v)+t,v)`. EVERY vertical ray in (3) is actually achieved, establishing equality of sets rather than merely a supporting-halfplane outer bound.

## 6. Checks, dependencies and claim limits

An in-kernel `fractions.Fraction` calculation checked the separated-disk coefficient `4*(1/2)*(1/3)=2/3` and that its floor quadratic contribution equals tau/2 when `tau^2=1/(3pi)`. A float diagnostic gave tau≈0.32573500793528 and v_c≈1.1414639861778908; it is not an interval proof. No actual all-law theorem, topology argument, strict concavity, or asymptotic was machine-verified. This note is a fresh written proof using standard density, bathtub, coarea/elementary geometric facts; it imports no named research theorem, LAW642, MDA, PMLR, v241 or f68. It has NOT been independently reviewed, formally checked, novelty-cleared or adopted by the parent. In particular, the nonconvex-core shell and the negative-theta peak-floor centering deserve disjoint review.
