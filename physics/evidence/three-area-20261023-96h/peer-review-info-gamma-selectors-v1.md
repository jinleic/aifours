# Independent written reconstruction: gamma-independent quantile selectors

Before-creation clock observed: **2026-10-23T13:13:28-07:00**. Reviewer: PhysicsResearch96h. No author edit, computation, solver, model CLI or formal verification was performed for this review.

## Snapshot and verdict

All 99 lines of `/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261023-96h/proof-gamma-independent-selectors-v1.md` were read, with pinned SHA-256 **`52b33a6766c6d4cfd0a76638801a39747b82761f86ac54fd868a4601f239c429`**. The base F_eta/G_eta definitions were independently reconstructed in `peer-review-info-bounded-outcome-v1.md` against the pinned base theorem.

**0 FATAL / 0 MAJOR / 0 MINOR. No substantive defect found under the stated arbitrary-law bounded-real model.** Both fixed data-only optimizers, their median/clamp formulas, and the quantile interpretations reconstruct without differentiability or unique-optimizer assumptions. No independent novelty claim is established.

## 1. Elementary convex selector lemma (lines 31–55)

Relabel a,b so a<=b. The increment assumptions on W imply:

- below a, `f=-W` is nonincreasing;
- above b, `f=2r-a-b-W` is nondecreasing because the slope/increment of W is at most two;
- on [a,b], `f=r-a-W(r)`.

If I lies wholly on one side of [a,b], the appropriate endpoint of I is a minimizer, exactly as the median/clamp formula returns. Otherwise set `J=I intersect [a,b]`. Moving an exterior point to J cannot increase f by the first two observations. On J the remaining function r-W(r) is convex. Projecting any of its global I-minimizers onto J is a J-minimizer: convexity gives monotonicity away from the minimizer set on each side, including flat minimizer intervals.

When the two intervals intersect, projecting r0 first onto [a,b] and then onto I is the projection onto J. For intervals this is exactly `clamp_I(med(a,b,r0))`. This proves the lemma with ties, coincident a,b, endpoint minimizers and singleton I included.

## 2. Lower selector (lines 57–63)

The factual upper-tail integrals are nondecreasing, concave and 1-Lipschitz, including atomic measures. Their sum `W(r)=u0(r)+u1(r-h)` is therefore continuous, concave and has increments between zero and twice the change in r.

Since t=r-h,

`F_eta(r)=(r-(h+eta))_+ +(r-(1-eta))_+-W(r)`.

The lemma's r0 is any maximizer of W-r, exactly r_minus. Taking the two hinge locations h+eta and 1-eta gives the stated lower selector for every compatible eta. The ordering of those locations may reverse as eta changes; the median handles this without an additional case assumption.

## 3. Upper selector by exact outcome reflection (lines 65–77)

For the reflected factual variable y'=1-y, selecting mass x from its upper tail has integral `x-ell_s(x)`. Thus its combined upper-tail sum is

`Wbar=r+t-ell0(r)-ell1(t)`.

It satisfies the same increment hypotheses: each `x-ell_s(x)` is nondecreasing, concave and 1-Lipschitz.

Reflecting both potential outcomes changes gamma to -gamma and delta to -delta. The reflected factual first moments are `m_s'=p_s-m_s`, so

`g_min'=(p-m1)-(p0-m0)-p=-1-g_min`,

and hence `eta'=-gamma-g_min'=1-eta`. This verifies the normalization change, not merely the sign of delta.

Direct substitution gives

`-F_ref_(1-eta)(r)=r+t-(r-eta)_+-(t+eta-1)_+-ell0(r)-ell1(t)=G_eta(r)`.

The reflected lower selector therefore has hinge locations `h+1-eta` and eta, and its data-only optimizer is any maximizer of Wbar-r. This is exactly the claimed r_U. It maximizes the original G_eta because reflection negates the objective. The argument preserves all atoms and zero-mass strata.

## 4. The two crossings and the sign threshold (lines 79–95)

At an interior differentiability point the derivative of an upper-tail integral is `Q_s(p_s-x)`. Therefore

`(W-r)'=Q0(p0-r)+Q1(p-(r-h))-1`.

For the second objective, `Wbar-r=t-ell0(r)-ell1(t)` and its derivative is

`1-Q0(r)-Q1(r-h)`.

The manuscript correctly treats these as characterizations of the fixed concave optimizers, with endpoint/subgradient alternatives, not assumptions excluding atoms or nondifferentiable quantiles. They supply two data-only crossings independent of gamma.

Finally,

`B_*=max_r[1-r+W(r)]=1+max_r[W(r)-r]`.

Every r_minus therefore gives the same `Gamma_*=g_min+1-r_minus+W(r_minus)`, including nonunique choices. This correctly connects one of the fixed selectors to the previously proved exact sign threshold.

## Boundaries

The result is a symbolic sensitivity simplification of the existing one-dimensional sharp-bound formula. Its correctness does not authenticate earlier binary elimination, the unresolved Kuroki source interface, clinical assumptions, statistical inference or publication priority. Parent acceptance and human/kernel verification remain separate gates. No additional mathematical defect was found.
