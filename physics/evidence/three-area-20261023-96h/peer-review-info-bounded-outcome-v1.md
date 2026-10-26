# Independent written reconstruction: bounded-real strong-surrogate bounds

Before-creation clock observed: **2026-10-23T13:07:01-07:00**. Reviewer: PhysicsResearch96h, ordinary in-harness peer. No author file was changed; no scientific program, solver, model CLI, test suite or formal proof was run for this review.

## Snapshot and verdict

Assigned manuscript: `/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261023-96h/proof-bounded-outcome-sharp-bounds-v1.md`, SHA-256 **`618ee5c5fc3ebc503f4dc730d70572dbc807036fd49efc87ef65d2e798643a82`**, all 346 lines read.

**Original snapshot: 0 FATAL / 0 MAJOR / 1 MINOR.** No substantive defect found in Theorems 1–2, simultaneous attainment, the uniform example, or the matched factual-distribution comparison at the stated arbitrary-dependence/strong-surrogacy boundary. The minor is the precise binary latent-domain comparison at line 326, not a defect in the bounded-real theorem. The operative addendum's Bernoulliization repair was also independently reconstructed below and resolves that minor at its explicit scope.

This is not parent acceptance, historical-openness clearance, novelty certification, or human/kernel review. The existence of an earlier peer review was visible during source routing; the derivations below were reconstructed from the pinned manuscript and primary model, not inherited from its verdict.

## Finding M1 — MINOR: literal feasible-law sets differ

**Location:** original manuscript lines 320–326, especially line 326's “same feasible set”. Binary factual outcomes do not force the unobserved potential outcome to be binary. The bounded-real model's full latent-law set therefore strictly contains the all-binary source domain in general. Equality of the attainable gamma/delta projection requires an argument; it does not follow just from equality of the observed binary cells.

**Repair checked:** the operative `proof-bounded-outcome-sharp-bounds-ADDENDUM-1.md`, SHA `e0ea69c9d4a4848f09aeb1f742038c8c5371a1ceceda8f298b61d771f2dddf9b`, and its detailed `addendum-binary-potential-outcome-bridge-v1.md`, SHA `ed43ab642cfade18a51d4964161566e26247a64946d5589a8bf78b623bd68cc8`, were both read in full. Conditional on the original tuple, replace the missing-outcome variable Z by `Z'=1{V<=Z}` using an independent uniform V. Then `E[Z'|B,y,S1,Z]=Z`. Retain the binary factual y and define the missing potential outcome from Z' using the original normalization. This preserves the full factual measures and surrogate marginals; gamma and delta are affine expectations of Z with coefficients measurable in the conditioning tuple, so they are preserved. The new potential outcomes are both binary. The converse inclusion is immediate. Thus the two **projected attainable sets** agree, while the full latent-law sets need not.

The repair is mathematically sufficient. It does not retroactively change the finding on the immutable original snapshot. This review does not independently expand every one of the separate seven-piece companion formulas.

## Independent reconstruction

### 1. Compatibility and switching masses (lines 21–30, 72–74, 97–128)

For `B=S0` and factual `y=Y_B`, define Z as Y1 on B=0 and 1-Y0 on B=1. Then the surrogate-intervention contrast is `-y+Z` on B=0 and `y-1+Z` on B=1. Integrating gives `gamma=m1-m0-p+E[Z]=g_min+E[Z]`. Necessity is exactly `eta in [0,1]`.

Sufficiency is constructive: draw the supplied `(B,y)`, choose Z=eta, and choose S1 independently Bernoulli(q). Recover the missing potential outcome. Nothing in the model couples q to Z further, so there is no omitted compatibility restriction.

If `r=P(B=0,S1=1)`, `t=P(B=1,S1=0)`, then `q=p+r-t`. The inequalities `0<=r<=p0`, `0<=t<=p` give precisely

`max(0,q-p)<=r<=min(p0,q)`.

They imply `r+t<=p0+p=1`. Conversely selection of those masses in the two factual strata realizes every r in I. No extra constraint is needed because arbitrary dependence and latent randomization are explicitly allowed.

The treatment contrast is

`delta=t-A0-A1+E[Z 1_C]-E[Z 1_D]`,

with C,D the two switch sets. This is the correct sign for both types of switch.

### 2. Tail extrema, atoms and simultaneous attainment (lines 38–66, 148–164)

For fixed mass x, an upper selector includes the strict upper tail and splits only its threshold atom if necessary. Its difference from any feasible selector satisfies `integral (y-cutoff)(a_star-a) dmu>=0`; the total-mass equality cancels the cutoff term. The lower-tail argument reverses signs. The generalized-quantile integrals correctly handle subprobability masses, including atoms and zero-mass strata. An independent auxiliary uniform implements every fractional atom selection without changing the factual outcome measure.

The two strata are disjoint, so their tail extrema can be achieved simultaneously. After those choices define C,D, the variable Z can be assigned conditionally on the resulting partition without changing the sampled y. This justifies optimizing the factual-tail and missing-outcome terms separately. There is no illicit combination of incompatible threshold-by-threshold extrema.

### 3. Exact Z-budget allocation (lines 130–146)

The coefficient of Z is -1 on D, 0 on nonswitchers, and +1 on C. Fill D first, then the nonswitch set, then C. The minimum is `-eta` for eta<=t, `-t` for t<=eta<=1-r, and `-t+eta-1+r` thereafter. This is `-min(eta,t)+(eta-1+r)_+`.

Filling C, then nonswitchers, then D gives `min(eta,r)-(eta-1+t)_+`. In each case the final partly filled set can receive a constant Z in [0,1], or be split by an auxiliary variable. Zero-mass sets cause no division issue. The lower and upper elementary budget inequalities are both sharp **simultaneously**, by the ordered fill.

Substitution yields exactly F_eta and G_eta. Compactness gives an optimal mass. Mixtures of endpoint-attaining laws preserve every supplied measure, q, and gamma, and vary delta linearly, so the entire interval is attained. The hinge/tail decompositions establish convexity of F and concavity of G, not just continuity.

### 4. Positive-effect threshold and strictness (lines 174–234)

Because t<=1-r,

`F_eta(r)=dist(eta,[t,1-r])-W(r)`.

Hence `F_eta(r)<=0` exactly on `J_r=[t-W(r),1-r+W(r)]`. Every unexpanded interval contains `[r_max-h,1-r_max]`, which is nonempty by `r_max+t_max<=1`. Thus all expanded intervals share a point and their union is exactly the closed interval `[A_*,B_*]`; compactness/continuity attain both extreme endpoints.

When h>0, r_min=h gives t=0 and `A_*<=0`. Also `g_min<=0`, so gamma>0 implies eta>0 and eliminates the lower exterior component. Therefore `L>0` iff eta>B_* iff gamma>Gamma_*. At eta=B_*, every F is nonnegative and at least one equals zero.

For the strict-negative conclusion, only r with W(r)>0 matter. Nonnegative concavity implies W is positive on the interior of I whenever it is not identically zero. Their expanded open intervals still have a common point and their union is `(A_*,B_*)`, with extrema recovered by continuity. The singleton case is immediate. This proves the trichotomy under its additional W condition and explains why the W-identically-zero case is stated separately. No degenerate strictness overclaim was found.

The high-gamma branch follows from eta>=1-r_min: all eta>=t and all r+eta-1>=0, giving `F=eta-[1-r+W(r)]` and hence `L=gamma-Gamma_*`.

### 5. Uniform example, exact numbers and literal attaining law (lines 238–286)

For each measure `(1/2)Uniform[0,1]`, the unnormalized quantile is `Q(v)=2v`; therefore `ell(x)=x^2` and `u(x)=x-x^2`. Here `I=[1/4,1/2]`, `t=r-1/4`, and

`1-r+W(r)=1+t-r^2-t^2`.

Its derivative is `3/2-4r`, so r=3/8,t=1/8 uniquely maximize it. The value is `31/32`, and `Gamma_*=-1/2+31/32=15/32`. For gamma>=1/4 the high-gamma branch gives `L=gamma-15/32`.

The proposed law selects y>=1/4 in the B=0 half and y>=3/4 in the B=1 half, giving the stated switch masses. With `c=(8gamma-1)/3`, `Z=c` on C and 1 elsewhere, `E[Z]=3c/8+5/8`; hence `gamma=3c/8+1/8`. The factual tail integrals are `3/8-(3/8)^2=15/64` and `1/8-(1/8)^2=7/64`. Thus `delta=3c/8-22/64=gamma-15/32`. The endpoint c values 1/3 and 1 are valid.

The two displayed consequences are correct: gamma=2/5 gives -11/160; gamma=49/100 gives 17/800. These were checked by written rational arithmetic, not computation.

### 6. Bernoulli-factual comparison and source boundary (lines 288–328)

For the matched conditional Bernoulli(1/2) laws, `u_s(x)=min(x,1/4)`. On I, `u0(r)=1/4`, `u1(t)=t`, so W(r)=r. At eta>=3/4, `F_eta(r)=eta-1=gamma-1/2` for every r. At gamma=49/100 the sharp endpoint is -1/100, whereas the uniform factual law forces at least 17/800. The two factual laws have the same p_s,m_s,q,gamma but not the same complete observed distributions. Thus the comparison really demonstrates additional distributional information; it is not a contradiction of the binary theorem.

I directly read the primary [Yin–Liu–Geng–Luo arXiv:1607.05454v1](https://arxiv.org/html/1607.05454v1), specifically its binary restriction, randomization and strong-surrogacy potential-outcome model. It indeed restricts both Y0,Y1 to {0,1}. The Bernoulliization repair above is therefore necessary to justify equality of identified projections. Its sixteen-type elimination, journal proof and worldwide priority were not authenticated by this review.

## Limits

Theorem correctness here is under the exact supplied-information model, including an external fixed gamma and arbitrary latent dependence. No clinical identification, statistical estimation, continuous-surrogate result, novelty claim, or full-book resolution follows. The arbitrary-real endpoint theorem itself does not require importing the older binary elimination. The operative repair resolves the sole original-snapshot minor at the stated comparison boundary.
