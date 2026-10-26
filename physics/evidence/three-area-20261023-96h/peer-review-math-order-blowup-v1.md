# Independent written reconstruction: H_{1,2} order blow-up

Before-creation clock observed: **2026-10-23T13:13:28-07:00**. Reviewer: PhysicsResearch96h. No author edit, scientific execution, finite matrix instantiation, root approximation, model CLI or formal proof was performed for this review.

## Snapshot and verdict

Reviewed all 146 lines of `/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261023-96h/proof-H12-order-blowup-v1.md`, pinned SHA-256 **`f7e26a155b9cbd3b58dc7c29d08da53eb1e8fdba9dbc19cd1d6e149be5f4d353`**.

**0 FATAL / 0 MAJOR / 0 MINOR. No substantive defect found at the stated import boundaries.** The finite-order exclusion is elementary and reconstructs independently of PH existence. The assertion that the finite minimum order diverges combines that exclusion with the explicitly named O'Cinneide import in the already checked existence-threshold manuscript; it is not an explicit minimum-order formula.

## 1. Nonnegative Hankel-rank bound (lines 25–32)

For any order-n PH representation, `f(s_i+t_j)=alpha exp(Ts_i) exp(Tt_j)w`. A Metzler subgenerator has a nonnegative exponential: choose lambda so `T+lambda I>=0` entrywise and expand its exponential. The two displayed factors are nonnegative and have inner dimension n. This works for arbitrary nonnegative times, reducible representations and nonminimal state spaces. The nonnegative rank is therefore at most n.

This argument is not an ordinary-rank argument. The continuous Hankel kernel of the uncancelled transform retains algebraic rank five, but that gives no uniform five-state PH representation and does not bound its nonnegative rank.

## 2. Robust zero-diagonal obstruction (lines 34–60)

Assume a factorization with at most r factors, padded by zeros. Normalize each nonzero U column to sum to one, transferring the reciprocal scale to V. Set a zero factor to zero on both sides. Then `0<=U_iell<=1` and

`Σ_ell V_ell,j=Σ_i M_ij<=k M0`.

In particular each V entry is bounded by k M0. Put `tau=m/(2r k M0)` and `S_i={ell:U_iell>=tau}`.

If `S_i subset S_j` for distinct indices, the contribution to M_ij from ell outside S_i is at most `r tau k M0=m/2`. For ell inside S_i, the inclusion and `M_jj<=epsilon` force `V_ell,j<=epsilon/tau`. Their contribution is at most `r epsilon/tau`. Under `epsilon<m^2/(4r^2 k M0)` this is strictly below m/2. Hence M_ij<m, a contradiction.

Thus all S_i are distinct (indeed incomparable), impossible for k>2^r. The strict inequality, factor r^2, factor k and M0 all have the correct placement. The proof also covers zero columns and representations of order strictly below r.

## 3. Boundary double zero and uniform perturbation bounds (lines 62–93)

From the threshold proof,

`G_k'(x)=((1+k^2)^2/2) exp(-kx)(sin x-x cos x)`.

At xi, `G=G'=0`, and the derivative of the last factor is `xi sin xi>0` because xi is in `(2pi,5pi/2)`. Therefore G'' is positive. Twice differentiating the density at t_* leaves only its positive prefactor times `b_*^2 G''(xi)`; every other term contains G or G' and vanishes. The zero is exactly quadratic.

The ratio `f_boundary(t)/(t-t_*)^2` extends to `f_boundary''(t_*)/2>0`. It is positive at every other point of J by the uniqueness of the positive-time zero. Its compact minimum C0 is consequently strictly positive.

The beta rectangle stays bounded away from zero because epsilon0<beta_*/2. The exact density is continuously differentiable in beta there; the displayed C1 and M0 are finite, strictly positive upper bounds. The mean-value bound holds uniformly on J. For beta below beta_*, nonnegativity comes from the elementary threshold-density analysis, not circularly from an assumed PH representation.

## 4. Exact times and neighborhood size (lines 95–136)

With k=2^r+1 and `h=t_*/[4(k+1)]`, the s_i lie strictly between t_*/2 and 3t_*/4, and all t_j=t_*-s_j lie strictly between t_*/4 and t_*/2. Hence all times are positive. Their sums equal `t_*+(i-j)h` and lie within J. Every off-diagonal distance from t_* is at least h.

At the boundary, off-diagonal entries are at least C0 h^2. If delta<=C0 h^2/(2C1), perturbation leaves them at least `m=C0 h^2/2`, while the common diagonal is at most C1 delta. Substituting this m in Lemma R gives exactly the required additional bound

`C1 delta<C0^2 h^4/(16r^2 k M0)`.

The stated epsilon_r uses strict extra factors two, so every `0<delta<epsilon_r` satisfies both requirements.

The two nonconstant terms in epsilon_r are

`C0 t_*^2/[64 C1(k+1)^2]`,

`C0^2 t_*^4/[8192 C1 M0 r^2 k(k+1)^4]`.

They dominate `C/[r^2(k+1)^5]` for the two displayed upper choices of C, because `r>=1` and `k<=k+1`. Thus the lower bound with the fifth power is correct; no k-dependent factor was lost. The section-1 existential epsilon0 in the summary may be taken to be half the rectangle width epsilon0 used in the proof, matching the explicit `epsilon0/2` in line 129. This harmless constant renaming does not change the mathematical rate or conclusion.

## 5. Divergence and compatibility with the existence theorem (lines 138–146)

For every fixed r, the construction excludes every PH representation with n<=r throughout a nonempty left neighborhood of beta_*. The threshold proof establishes a continuous strictly positive probability density for every beta<beta_* and, at the declared characterization import, at least one finite PH representation there. Combining the two gives the precise limit: for each r there is a left neighborhood in which the finite minimum order exceeds r. Therefore the order tends to infinity as beta approaches beta_* from below.

The poles do not coalesce: a-c=d>0 is fixed and b approaches the positive finite value beta_* d; the reduced denominator still has one real simple pole and a conjugate double pair. The result therefore genuinely separates fixed transform degree from PH order.

I previously reconstructed the pinned existence-threshold proof, including its open-interval positivity convention and the modern primary characterization statement; that separate review is `peer-review-H12-existence-threshold-v1.md`. Its positive side remains a classical theorem import. The present nonnegative-rank obstruction does not require that import, while the phrase “minimum finite PH order diverges” does.

## Limits

No exact order in the residual band is obtained, no quantitative constant was numerically evaluated, and no finite matrix experiment was run. Classical nonnegative-rank/Hankel and positive-time-zero ideas require a separate matched priority audit. This is written in-harness checking, not parent promotion, global novelty, human review or kernel verification.
