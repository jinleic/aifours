# Independent in-harness written review: bounded-outcome surrogate bounds v1

Before-creation clock observed: **2026-10-23T12:58:53-07:00**. Reviewer: `MathResearch96h`, at the parent's explicit request. Read-only review of the author's files; the sole review output is inside the reviewer's owned mathematics root. No scientific code, enumeration, numerical experiment, CLI delegate or proof assistant was run. This is neither cross-vendor nor kernel/human acceptance.

## Snapshot and verdict

Entire proof read: `/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261023-96h/proof-bounded-outcome-sharp-bounds-v1.md`, lines1–346, **SHA256 `618ee5c5fc3ebc503f4dc730d70572dbc807036fd49efc87ef65d2e798643a82`**.

Entire selection read, including the full long table/provenance lines: adjacent `selection-v1.md`, lines1–69, **SHA256 `03906f26cb32ab3bf08de51c79fd304b792856510b0b0658dfd0a72adfe407c2`**. Hashes are metadata identity checks, not mathematics.

**Verdict: no substantive mathematical defect found in Theorems1/2, endpoint attainment or examples at the stated unrestricted dependence model. Findings: 0 FATAL /0 MAJOR /1 MINOR.** The minor is a repairable missing explicit binary-feasible-set bridge in the baseline-comparison wording; a complete short repair is supplied below. Correctness is separate from novelty, clinical assumptions and full-book scope.

## Finding M1 — MINOR: same identified set, not literally the same feasible set

**Location:** proof line326, especially “uniqueness of the minimum and maximum of the same feasible set”, compared with lines7,32 and the source's binary restriction.

The present model allows both potential outcomes in [0,1]. Merely making the *factual* outcomes binary does not make the latent missing outcome binary, so its feasible law set is not literally the sixteen-type law set of Yin et al. Equality of the identified intervals is true, but the brief reduction should explicitly justify it instead of identifying the two feasible law sets.

**Exact repair, independently derived:** retain B,y,S_1 and Z from the manuscript. When y is binary, let V be an independent uniform variable and replace Z by Z'=1_{V<=Z}. Define the missing potential outcome from Z' exactly as in step1. Then both potential outcomes are binary; E[Z'|B,y,S_1,Z]=Z; hence all mu_s and q are unchanged, and both gamma and delta are unchanged by (10)/(11), which are affine in Z. Conversely every binary law is already allowed in the bounded-real model. Thus the two models have the same attainable (gamma,delta) projections and the same identified interval, though different feasible law sets. This is consistent with the optional group-splitting construction at line146.

Suggested wording: “After the conditional Bernoulliization of the missing outcome described above, the binary and bounded-real models with binary factual laws have the same attainable gamma/delta projections. Conditional on the source theorem's sharpness, the two endpoint formulas agree.” No substantive theorem needs weakening.

## Independent reconstruction

### 1. Compatibility and the missing outcome

On B=0, Y_1-Y_0=Z-y; on B=1, Y_1-Y_0=Z+y-1 with Z=1-Y_0. Thus

    E[Y_1-Y_0]=m_1-m_0-p+E Z=g_min+E Z.

Necessity is exactly 0<=eta<=1. For sufficiency, choosing Z=eta and S_1 Bernoulli(q), independent of (B,y), is a genuine law with the supplied complete factual measures. Recovering the missing outcome gives values in [0,1]. No additional q/gamma compatibility condition arises because arbitrary dependence is explicitly allowed. Endpoint eta0/1 causes no exception.

### 2. Switch masses and quantile-tail optimization

Let C={B0,S_1=1}, D={B1,S_1=0}, r=P(C), t=P(D). The relation q=p+r-t gives t=r-h. The inequalities r in[0,p_0], t in[0,p] reduce exactly to

    max(0,h)<=r<=min(p_0,q).

This interval is nonempty for all p,q in[0,1]; the two disjoint switch masses satisfy r+t<=1. There is no omitted joint-law constraint.

Conditioning the indicator of C on the factual y in stratum0 gives a measurable selector a_0(y) in[0,1] of mass r; likewise D gives a_1(y) of mass t. Conversely such selectors are implemented with an auxiliary uniform variable. The threshold-exchange integral in Lemma1 is valid at atoms, including cutoff0/1 and mass0/full mass. Therefore the attainable extreme factual sums are exactly upper/lower unnormalized quantile integrals. The upper tails are concave and lower tails convex, with continuity following directly from bounded integrands and mass increments.

### 3. Budget allocation and simultaneous atomic attainment

The objective independently reduces to

    delta=t-A_0-A_1+E[Z1_C]-E[Z1_D].

For the minimum, allocate eta to D first, then its complement outside C, then C. The exact optimum is

    -min(eta,t)+(eta-1+r)_+.

For the maximum, allocate to C, then outside C union D, then D, giving

    min(eta,r)-(eta-1+t)_+.

These follow both from coefficient-ordered filling and from the simultaneous lower/upper mass inequalities. At every fixed switch partition, all available budget is allocated exactly, with a fractional final group split or assigned a constant. No division by a zero mass is necessary.

Choose the upper factual tails for the minimum and lower tails for the maximum, then assign Z within the resulting partition. That assignment changes only the missing outcome, never the factual y. This proves that factual-tail extrema and budget extrema can be attained simultaneously even when the measures have atoms. The gamma mean is exactly g_min+eta throughout, not an after-the-fact adjustment.

Substituting gives precisely F_eta/G_eta. F is convex in r; G is concave after writing min(eta,r)=r-(r-eta)_+. On compact I both extrema are attained. Mixing complete endpoint laws keeps the entire pair of factual measures, q and gamma fixed and interpolates delta linearly; therefore the complete interval, not only its endpoints, is attained.

### 4. Sign threshold, including degeneracy

Since t<=1-r,

    F_eta(r)=dist(eta,[t,1-r])-W(r).

Therefore F_eta(r)<=0 iff eta lies in the closed interval J_r=[t-W(r),1-r+W(r)]. Every base interval [t,1-r] contains [r_max-h,1-r_max], which is nonempty because r_max+t_max<=1. Thus all J_r have a common point. Compactness/continuity makes their union exactly [A_*,B_*].

For h>0, r_min=h has t0, so A_*<=0. Also g_min<=0; with gamma>0, eta>0. Hence eta cannot fall below A_*, and L>0 iff eta>B_*, equivalently gamma>Gamma_*.

At eta=B_* every F is nonnegative and an endpoint-maximizing r gives zero, so L0. If W is not identically zero, its concavity and nonnegativity imply strict positivity at every interior r of a nondegenerate I. Restricting to those r with W>0 preserves the infimum/supremum endpoints by continuity. Their open intervals have a common point as well, so their union is (A_*,B_*). Thus gamma<Gamma_* in the stated h>0,gamma>0 regime yields an actually attained strictly negative lower bound. If I is a singleton with W>0 the same conclusion is immediate. If W is identically zero, F is a distance and L>=0; the text correctly does not claim a negative law in that case. The distinction between L>=0 and L>0 is retained.

### 5. Uniform example and exact law

For half-mass Uniform[0,1], the quantile is Q(v)=2v for0<v<1/2, so ell(x)=x^2 and u(x)=x-x^2. With h1/4 and t=r-1/4,

    B(r)=1+t-r^2-t^2,
    B'(r)=3/2-4r.

Thus the unique optimum is r3/8,t1/8, B_*31/32, Gamma_*15/32. For gamma in[1/4,1/2], eta>=3/4=1-r_min and the exact high-gamma branch is L=gamma-15/32.

The proposed selectors y>=1/4 on B0 and y>=3/4 on B1 indeed give the required switch masses and q3/4. With c=(8gamma-1)/3 on C and Z1 off C, the budget is

    E Z=3c/8+5/8=gamma+1/2=eta.

On B1 the missing outcome is0, as stated. The factual selected integrals are15/64 and7/64, so delta=3c/8-22/64=gamma-15/32. At gamma2/5 this equals-11/160; at gamma49/100 it equals17/800. This is symbolic arithmetic, not executed numerical evidence.

### 6. Matched means-only countercomparison

For the two conditional Bernoulli(1/2) factual laws, u_s(x)=min(x,1/4). On I=[1/4,1/2], t=r-1/4, hence W(r)=1/4+t=r. For gamma>=1/4, eta>=3/4, so F_eta(r)=r+eta-1-W(r)=eta-1=gamma-1/2 for every r. At gamma49/100, the sharp lower endpoint is-1/100. These data have exactly the same p_s,m_s,q,gamma as the uniform case, so a guarantee based only on those summaries must allow a negative effect and cannot recover the full-uniform-law guarantee17/800. This does not contradict the prior binary theorem.

### 7. Boundary cases and computational interpretation

Direct substitution at p0 and p1 reproduces the manuscript's singleton-I formulas. Quantile endpoints are never used at positive Lebesgue measure, so atoms and zero strata are handled. For finite support, the listed hinges r=h+eta and r=1-eta for F are correct, and adding tail breakpoints gives a finite exact piecewise-linear evaluation; no such evaluation was executed. The stated differentiable crossing Q_0(p_0-r)+Q_1(p-t)=1 is the derivative of1-r+W(r), with the explicit subgradient caveat adequate at jumps.

## Source and promotion boundary

I opened Yin–Liu–Geng–Luo's actual arXiv:1607.05454v1 HTML, the binary/randomization/strong-surrogate model, §5.1 equations, Theorem1 statement/sharpness and its seven lower/upper pieces. Its supplied data interface matches the stated binary restriction, subject to the Bernoulliization clarification above. I did not replay or authenticate its full16-type elimination or the published journal PDF. The new Theorems1/2 do not require importing that elimination: the constructive derivation above is independent. Kuroki2013's full result remains unread here; priority is not cleared. No full-book, clinical, statistical-inference, continuous-surrogate or unbounded-outcome claim is accepted by this review.

The review applies only to the exact pinned proof/selection. Application of wording fixes must be recorded separately; it does not retroactively change this original-snapshot verdict.
