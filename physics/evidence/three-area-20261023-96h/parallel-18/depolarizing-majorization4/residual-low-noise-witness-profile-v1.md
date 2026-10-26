# Exact necessary profile for a low-noise four-qubit counterexample

Observed activation/creation clock: **2026-10-23T14:47:24-0700**. PhysicsDepol4. Parent explicitly authorized this optional bounded written statement while the central-index reconstruction is pending. No optimization, eigensolver or scientific execution was run.

**Status:** a written witness-screening profile, not a found counterexample, unrestricted solution or novelty claim. The central candidate remains awaiting review. Its strong mechanistic overlap with the Zhang public claim remains governed by `source-audit-v2-zhang-prior-claim.md`; no clean novelty framing is restored here.

## 1. What is conditional on the central review

If the pinned central proof `10e4689c7ac8586fc920651eade6db37fa60be3b693f73b5f4ec7b6644fe6d23` is accepted, the only outstanding channel inequalities in this slot are

`0<p<2/3`, `k in{2,3,4}`.

The necessary conditions below concern those literal indices. They are valid using the already established U_2(2,3,4) and high-noise endpoint bounds; they do not themselves depend on accepting the new central argument. If that argument fails review, this list is not an exhaustive profile of every possible four-qubit counterexample.

Write `rho=|psi><psi|`, `X_s=sum_(|I|=s) rho_I tensor I_(I^c)`, and

`R=sum_i |r_i|^2`, `C=|<psi|sigma_y^tensor4|bar(psi)>|^2`.

A mixed-input violation implies a pure-input violation at the same p,k, by convexity of K_k and a finite pure decomposition. Thus purity is a valid reduction of a hypothetical counterexample, not an input ansatz.

## 2. The actual spectral partial sum must have an exact projector witness

For some rank-k orthogonal projector Pi,

`Tr[Pi D_p^tensor4(rho)] > a^4+(k-1)a^3 b`,                        (1)

where `a=1-p/2`, `b=p/2`. These are the correct first k product eigenvalues because p<2/3<1. A projector attaining the output's Ky-Fan sum always exists. Conversely, any Pi satisfying (1) proves a violation even if Pi is not itself the top-k spectral projector.

Define the exact nonnegative deficits

`d1=3k+1-Tr(Pi X_1)`,

`d2=3k+3-Tr(Pi X_2)`,

`d4=1-<psi|Pi|psi>`.

The first is nonnegative by the universal Kronecker-sum bound. The second is nonnegative by the actual inherited U_2(2,3,4) certificate package, read with its operative addendum/review. The third is nonnegative because Pi is a projector. The product reference sums are exactly `K_k(T_1)=3k+1`, `K_k(T_2)=3k+3`, `K_k(T_3)=k+3`, `K_k(T_4)=1`.

Let

`delta3=Tr(Pi X_3)-(k+3)`,

`u=p/[2(1-p)] in(0,1)`.

The expansion coefficients `a_s=(1-p)^s p^(4-s)2^(s-4)` obey

`a1/a3=u^2`, `a2/a3=u`, `a4/a3=1/u`.

Since the identity term has no deficit, the witness gap is **exactly**

`Tr(Pi D_p^tensor4(rho))-K_k(D_p^tensor4(0000))`

` =a3[delta3-u^2 d1-u d2-d4/u]`.                                  (2)

Therefore (1) is equivalent to the sharp projector-level requirement

`delta3 > u^2 d1+u d2+d4/u`.                                      (3)

In particular, a channel counterexample necessarily violates the compatible-marginal bound `K_k(X_3)<=k+3`. An arbitrary violation of that X_3 bound does not automatically violate the channel: its projector must also overcome the three displayed deficits at one common u.

## 3. Pure-state moment/rank exclusions that every witness must evade

The already separately reconstructed identities give

`Tr X_3=8`, `rank X_3<=13`, `Tr X_3^2=8+3R+2C`.

If K_k(X_3)>k+3, separate Cauchy on the leading k and remaining 13-k eigenvalues forces

`Tr X_3^2 > (k+3)^2/k+(5-k)^2/(13-k)`.

The strict inequality is justified because the comparison quadratic is increasing above its mean branch, and k+3>8k/13. Consequently every low-noise witness must satisfy the following strict conditions:

| k | necessary `3R+2C >` | necessary R-only condition |
|---|---|---|
| 2 | 117/22 | R>73/55 |
| 3 | 22/5 | R>24/25 |
| 4 | 157/36 | R>17/18 |

The R-only column uses the exact pure-state compatibility inequality `R+4C<=4`, so `3R+2C<=2+(5/2)R`. These thresholds are necessary exclusions, not sufficient existence criteria, and they are not asserted for a general mixed state's local Bloch data.

Equivalently, with `Z=sum_(i,a=x,y,z) sigma_a^(i)rho sigma_a^(i)` and `r=<psi|Pi|psi>`, the identity `X_3=2rho+Z/2` turns (3) into

`Tr(Pi Z)>2[k+3-2r+u^2 d1+u d2+(1-r)/u]`.                         (4)

This retains the same physical psi, exact projector Pi and channel parameter. Feasible points of the old loose PPT/Gram relaxation are not witnesses satisfying this physical interface.

## 4. Additional exact noise/overlap conditions, without launching an optimizer

At u=1, corresponding to p=2/3, the inherited all-input endpoint bound gives

`delta3<=d1+d2+d4`.

For a fixed physical pair (psi,Pi), set

`f(u)=d1 u^2+d2 u+d4/u`.

Its second derivative is `2d1+2d4/u^3>=0`. If `d4>=2d1+d2`, then f'(1)<=0, hence f'(u)<=0 throughout (0,1). Thus `f(u)>=f(1)>=delta3`, precluding (3). A low-noise witness therefore also necessarily satisfies

`1-<psi|Pi|psi> =d4 <2d1+d2`.                                     (5)

If d4>0, the unique minimum on positive u solves the explicit scalar equation

`2d1 u^3+d2 u^2-d4=0`.

Condition (5) forces its root to lie below one; an eligible projector still needs `delta3>f(u_min)`. This is a necessary exact one-variable comparison, not a numerical search result.

If d4=0, Pi contains psi and f(u) tends to zero as u decreases to zero. Hence an actual X_3 violation with a rank-k projector **containing psi** would imply a channel counterexample at every sufficiently small positive p. This is a genuine sufficient bridge for that special hypothetical witness configuration, not evidence that such a configuration exists. Without containment the d4/u penalty cannot be discarded.

The earlier near-product full-majorization snapshots would give a further G-based exclusion only **if their own reconstruction succeeds**. They are not used as accepted necessary conditions here.

## 5. Rational certificates are sufficient if any strict counterexample exists

There is no need to accept a floating-point eigenvalue violation. If a strict counterexample exists in the open p interval, continuity permits a nearby triple with rational p, a nonzero complex-rational vector z, and a full-column-rank complex-rational 16-by-k matrix V such that

`rho=z z^dagger/(z^dagger z)`,

`Pi=V(V^dagger V)^(-1)V^dagger`

still satisfies (1). Complex-rational vectors and subspaces are dense; normalize z by its quadratic norm and represent the subspace by its Gram projector. These formulas make rho positive of trace one and Pi a rank-k Hermitian idempotent **exactly**. All their matrix entries are complex rational; the normalization need not make the amplitudes of psi themselves rational.

For rational p, both sides of (1) are then rational numbers. The strict trace inequality is a complete violated-partial-sum certificate because `K_k(output)>=Tr(Pi output)`. No approximate spectral ordering, positivity tolerance or SDP status is sufficient in its place. This observation supplies a complete certificate format, not an actual witness or a finite search completeness claim.

## 6. Exact boundary of what was accomplished

This profile sharpens the unresolved low-noise question into a common-state/projector inequality (3), three strict moment exclusions, the overlap-versus-deficit condition (5), and an exact rational certificate interface. It does not solve K_k(X_3)<=k+3, refute the channel conjecture, validate the central proof before review, or resolve Zhang's uniform-support ambiguity. The old source snapshots and their separate review/priority gates remain unchanged.
