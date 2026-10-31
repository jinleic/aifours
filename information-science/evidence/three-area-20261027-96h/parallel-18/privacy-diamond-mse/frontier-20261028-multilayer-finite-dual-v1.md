# All privacy layers: a stronger finite bound with the correct high-privacy scale

**AUTHOR CANDIDATE — WRITTEN, with explicitly nonrigorous floating illustrations; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 19:36:40 PDT 2026`.

## 1. Exact finite-epsilon all-law result

Fix b=e^(-epsilon) in (0,1), kappa>=0, and let J=E|X|^2, L=E||X||_1 under the original ALL-event, ALL-Borel, FULL closed l1-unit-diamond privacy condition. Define

    phi_kappa(x)=|x|^2+kappa||x||_1,
    G_kappa(T)=integral_R2(T-phi_kappa)_+ dx,
    q_b(x)=b^ceil(||x||_1),
    D_b,kappa(T)=integral_R2 q_b(x)(phi_kappa(x)-T)_+ dx.               (1)

There is a UNIQUE positive B_infinity solving

    G_kappa(B_infinity)=D_b,kappa(B_infinity).                           (2)

The WRITTEN source-independent theorem is that EVERY actual fully private law satisfies

    J+kappa L >= B_infinity.                                              (3)

For every b in (0,1), kappa>=0, this is STRICTLY stronger than the already stronger single-layer occupied-cap lower root in `frontier-20261028-overlap-corrected-finite-dual-v1.md`, SHA-256 `d57a58caedd6efd0751c5a4c6059c5c86db31446811e08bab317531da7d124f3`. That earlier candidate is cited only for comparison, not imported into the proof. No finite-b exact optimizer claim is made.

Unlike the single-layer bound, the new original-J lower bound grows at the CORRECT `epsilon^(-2)` order as epsilon->0. More precisely, for kappa=0,

    epsilon^2 B_infinity -> w_*,                                         (4)

where w_*>0 is the UNIQUE solution

    (pi/2)w^2 = integral_R2 e^(-||z||_1)(|z|^2-w)_+ dz.                  (5)

It satisfies 2<w_*<sqrt(32/pi); an uncertified floating diagnostic gives w_*≈2.490130073. Independently, the actual product-Laplace law `(epsilon^2/4)e^(-epsilon||x||_1)` is fully private and has J=4/epsilon^2. Thus these two explicit source-independent arguments put the actual all-law optimum between `w_*/epsilon^2+o(epsilon^(-2))` and `4/epsilon^2`; no claim that either bound equals the exact optimum is made.

## 2. Full multilayer floor and occupied residual cap

Full event privacy gives a bounded all-point density representative p; let M=esssup p and pick x0 with `p(x0)>=(1-eta)M`. For ANY x, n=ceil(||x-x0||_1) equal steps each belong to D, hence repeated privacy gives

    p(x)>=(1-eta)M q_b(x-x0).                                             (6)

This uses every actual privacy layer, not just x0+D. Let `q=q_b(.-x0)` and `g=p-(1-eta)M q`. Almost everywhere

    0<=g<=M[1-(1-eta)q].                                                  (7)

For arbitrary T>=0, the capped-density dual plus the floor contribution is exactly

    J+kappa L >= T-M G_kappa(T)
       +(1-eta)M integral q_b(x-x0)(phi_kappa(x)-T)_+ dx.                (8)

The positive-part cost h=(phi_kappa-T)_+ is even convex. Except at the measure-zero origin,

    q_b(x)=(1-b) sum_(k>=1) b^k 1_(kD)(x).                              (9)

Every function `x0->integral_(x0+kD) h(x)dx` is even convex and hence minimized at 0. Summing the positive coefficients gives the translate minimum at 0. Therefore (8) implies

    J+kappa L >= T+M[(1-eta)D_b,kappa(T)-G_kappa(T)].                   (10)

At T=0 the right root difference `G-D` is negative, and it is strictly increasing to infinity: G strictly increases for T>0, while D decreases continuously to 0. The unique root exists, and eta->0 gives (3). Finiteness follows from exponential q and quadratic phi.

## 3. Strict comparison to the one-layer occupied-cap root

Pointwise q_b>=b 1_D a.e., and q_b=b^2 on 2D\D. At the single-layer bound B_1, one has `B_1<=1/3+2kappa/3<1/2+kappa`, whereas outside D, `phi_kappa>=1/2+kappa`. Hence

    D_b,kappa(B_1) > b integral_D(phi_kappa-B_1)_+
                   = G_kappa(B_1).

The gap is strictly positive on 2D\D. Since `G-D` is strictly increasing, its zero B_infinity is strictly larger than B_1. This compares lower certificates only, not either one with the true optimum.

## 4. Explicit original-J root for small b

Define the exact positive geometric moments

    A_b=integral q_b =2b(1+b)/(1-b)^2,
    Q_b=integral q_b |x|^2
       =2b(1+11b+11b^2+b^3)/[3(1-b)^4].                                (11)

Whenever B_infinity<=1/2, its Euclidean disk sublevel lies in D, where q_b=b a.e. Hence the root equation becomes

    (1-b)(pi/2)B_infinity^2+A_b B_infinity=Q_b,
    B_infinity=2Q_b/[A_b+sqrt(A_b^2+2pi(1-b)Q_b)].                     (12)

The condition is equivalent to `(1-b)pi/8+A_b/2-Q_b>=0`. It certainly holds for every 0<b<=1/16: use `Q_b<=8b/3<=1/6` and `(1-b)pi/8>=45/128>1/6`. Outside that sufficient range, use the unmodified root (2); (12) is NOT asserted when its containment test fails.

## 5. High-privacy scaling, including exact elementary brackets

Set b=e^(-epsilon), `w_epsilon=epsilon^2 B_infinity` and x=z/epsilon. Equation (2) for kappa=0 becomes

    (pi/2)w_epsilon^2 = integral e^(-epsilon ceil(||z||_1/epsilon))
                                      (|z|^2-w_epsilon)_+ dz.            (13)

The exponential weight lies between `e^(-epsilon)e^(-||z||_1)` and `e^(-||z||_1)`. At fixed w these bounds, monotonicity and root bracketing imply (4)–(5). The limit's RHS H(w) is continuous, strictly decreasing, with H(0)=16 and H(w)->0, so w_* is unique. Since H(w)>=16-4w, at w=2 we have H(2)>=8>2pi and w_*>2. Since H(w)<=16, `w_*<=sqrt(32/pi)`, with strict inequality because the positive-part loss is nonconstant and w_*>0.

For the float diagnostic one convenient exact 1D form is

    H(w)=4 integral_0^(pi/2) exp[-a sqrt(w)]
           [2w/a^2+6sqrt(w)/a^3+6/a^4] dphi,
    a=cos(phi)+sin(phi).                                                  (14)

This follows by elementary radial integration, not from an external source.

## 6. Actual checks and scope

A Python `math` Simpson/bisection cell evaluated (14) at grids 256,512,1024, yielding roots 2.4901300790440795, 2.4901300730891816, 2.4901300727168802 respectively. These are FLOAT diagnostics, not interval enclosures or formal verification. Equations (1)–(14) are written standard-analysis arguments with no LAW642, MDA, PMLR or prior research theorem imported; no independent review, novelty clearance, finite-b exactness or parent adoption is claimed. Suggested review: every-step privacy floor, the layer-cake translation minimum, strict comparison, and the high-privacy rescaling.
