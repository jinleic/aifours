# The explicit PH7 endpoint is a STRICT LOCAL maximum over all seven-state generator topologies

**EXACT WRITTEN + SYMBOLIC/RATIONAL CANDIDATE; independent review and parent adoption pending.** MathResearch96h-2. This strengthens the tangent-only theorem `frontier-20261028-ph7-all-edge-first-order-barrier-v1.md` SHA256 `85c2e178a432231687a22102cf7b1fd2aad08035bde6dea9516cab707f77ff37`. Its exact algebraic endpoint is the separate v4 source and mandatory identity-scope correction named in that theorem. No 8/9 exclusion or global maximum is claimed.

## 1. Result

Let G* be the explicit algebraic seven-state ROW generator in the first-order source, with transition graph

    1->2->3->4->5, 5->1, 5->6->7->1,

and let z_* be its exact isolated frequency-square, `820420341/10^9<z_*<820420541/10^9`. There exists an open neighborhood U of `(G*,z_*)`, in the full space of all 42 off-diagonal rates and z, with the following property:

> If G is ANY real seven-state row generator with nonnegative off-diagonal entries and `(G,z)` belongs to U, and if its actual characteristic polynomial is divisible by `D_z(y)=y[(y+1)^2+z]^2`, then `z<=z_*`, with equality ONLY at `(G,z)=(G*,z_*)`.

All 42 possible directed edges are allowed: this is not limited to a previously chosen topology. The statement concerns the spectral skeleton alone and imposes no PH input/exit, numerator or shortest-path conditions. Therefore any PH7 construction whose positive-Perron-normalized generator lies in this neighborhood cannot extend the exact band upward. Remote components, nonsmooth jumps to another representation, and the original target at 8/9 remain completely open.

## 2. The exact first-order and constraint interface

Use the actual four residual polynomials `F=(F4,F3,F2,F1)` of the full characteristic polynomial defined in §3 of the first-order source. Their vanishing is equivalent to divisibility by D_z for row generators. At the endpoint, name the eight positive rates

    x1=rate(1->2), x2=rate(2->3), x3=rate(3->4), x4=rate(4->5),
    a=rate(5->1), b=rate(5->6), v1=rate(6->7), v2=rate(7->1),

and let s be the vector of the other 34 initially zero rates. The endpoint values are `x1=...=x4=U`, `a=a_*`, `b=U-a_*`, `v1=v2=V`. Define the dependent coordinates `d=(x1,a,v1,z)` and the five free active coordinates `w=(x2,x3,x4,b,v2)`.

The first-order source defines the dual L by

    K=(J_(1->2)^T; J_(5->1)^T; J_(6->7)^T; J_z^T),
    K L=(0,0,0,1)^T.

Its exact full-graph checker proves `det K` is in `(-30,-20)` over the algebraic endpoint enclosure; `L^T J_z=1`; the Lagrangian gradient on all eight active rates is exactly0; and every absent-edge cost `L^T J_e>1/100`. In particular the four equality constraints have full rank with respect to d. The corresponding Lagrangian is

    ell(G,z)=z-L^T F(G,z),

with L frozen at the endpoint.

## 3. Explicit five-dimensional tangent and Hessian

Within the eight-edge face, the **actual** characteristic polynomial, allowing all eight active rates to vary independently, is

    P(y)= [product_(j=1)^4 (y+xj)] (y+a+b)(y+v1)(y+v2)
          - [product_(j=1)^4 xj] [a(y+v1)(y+v2)+b v1 v2].  (P8)

It follows from the diagonal permutation and the two actual cycles; it is not an independently chosen polynomial. In the active-coordinate order `(x1,x2,x3,x4,a,b,v1,v2,z)`, a basis for the kernel of the full 4-by9 constraint Jacobian at the endpoint is

    t1=(-1, 1,0,0, 0,0, 0,0,0),
    t2=(-1, 0,1,0, 0,0, 0,0,0),
    t3=(-1, 0,0,1, 0,0, 0,0,0),
    t4=(-k, 0,0,0, k-1,1, 0,0,0),
    t5=( 0, 0,0,0, 0,0,-1,1,0),
    k=U/(U-a_*) >0.                                  (TANGENT)

The first four independent dependent-coordinate derivatives are encoded by invertible K, so this is the entire five-dimensional tangent, not a chosen subspace. The exact checker differentiates(P8), verifies every component of `J t_i=0`, and constructs the Lagrangian Hessian

    H = -sum_(j=1)^4 L_j Hessian(F_j)

at the endpoint. Denote `D=det K`, `w0=adj(K)e4`, and let `h` and `l` be the following two exact Hessian numerators:

    h=-sum_j (w0)_j t1^T Hessian(F_j) t2,
    l=-sum_j (w0)_j t5^T Hessian(F_j) t5.

Direct symbolic algebra gives the ENTIRE 5-by5 reduced Hessian, in the ordered basis(TANGENT), as

    (h/D) * [ 2 1 1 k    0
              1 2 1 k    0
              1 1 2 k    0
              k k k 2k²  0
              0 0 0 0   0 ]  +  (l/D) e5 e5^T.    (HESS)

The checker proves uniformly on the certified rational endpoint/branch box that

    -30<D<-20,        h>8,        l>30,        k>0.    (H-SIGN)

The upper-left 3-by3 matrix is `I+11^T` and positive definite. Its Schur complement in the four-by-four bracket is `2k²-3k²/4=5k²/4>0`. Thus that bracket is positive definite; since both `h/D` and `l/D` are strictly negative, the full reduced Hessian(HESS) is NEGATIVE DEFINITE. This conclusion is exact, not inferred from numerical eigenvalues.

## 4. Turning the Hessian and all-edge signs into strict local maximality

Because K is invertible, the ordinary implicit function theorem solves the four equations `F=0` locally for d as smooth functions of `(w,s)`. In particular z is a smooth function `phi(w,s)` near the endpoint, with

    grad_w phi=0,             d phi/ds_e = -L^T J_e < -1/100.

The chain rule for the implicit constraint identifies `Hess_w phi` with(HESS), hence it is negative definite. Therefore there is a smaller neighborhood and a constant c>0 such that

    phi(w,0) <= z_* - c ||w-w_*||²,

with equality only when w=w_*. By continuity of all 34 partial derivatives, in an even smaller neighborhood each `partial phi/partial s_e < -1/200`. For s>=0, integration along `tau s`, 0<=tau<=1, gives

    phi(w,s)-phi(w,0) <= -(1/200) sum_e s_e.

Combining the two inequalities proves the strict local result in §1. The proof allows all absent transitions simultaneously; it does not require a first-order path or rule out a merely higher-order escape by assumption. □

## 5. Exact verification and stated nonclaims

Actual completed invocation:

    python3 frontier-20261028-ph7-all-edge-second-order-check.py
    SymPy 1.14.0 exact tangent Hessian negative definite PASS: 5 active directions

Checker `frontier-20261028-ph7-all-edge-second-order-check.py`, **65LF/3457B**, SHA256 `76777635c2e8dd9d2c83ca29d60b6f896c618d47d89d393c2f57be7153ce8871`. Certificate `frontier-20261028-ph7-all-edge-second-order-certificate.json`, **22LF/611B**, SHA256 `def834e8fc14850c0ced0c8e4f5f847edd37f3abba46f612d232151facbfd1e1`. The checker verifies(P8)'s coefficient residuals, full tangent basis, every symbolic Hessian matrix entry, and exact rational interval bounds(H-SIGN). It does not check the separate 34-edge signs, which are the explicit pinned first-order dependency, nor the v4 root existence/normalizer, which have their own pinned exact certificates.

The interval is obtained from the v4 rational contraction root plus the first-order branch-rate enclosure, not a floating optimizer. The local proof uses ordinary determinant algebra, exact polynomial arithmetic, the implicit function theorem, continuity and Taylor's theorem. It does not prove all possible seven-state generators are near G*, does not locate the critical ratio within that neighborhood, does not exclude any remote solution, and gives no 8/9 or minimum8 theorem. No formal/kernel, human, independent-family, novelty or stronger-gate claim is made. Historic holds remain nonpremises and findings are not cured.

END — strict local spectral maximum across all 42 edges at the exact algebraic PH7 endpoint; the global bridge to 8/9 remains open.
