# Full-law Euclidean/squared-l1 mixed-loss frontier

**AUTHOR CANDIDATE — WRITTEN with exact rational scalar controls; NOT independently reviewed or parent-adopted.** Native pre-write clock: `Wed Oct 28 18:38:16 PDT 2026`.

## 1. Original model and exact new assertion

Fix EVERY finite epsilon>0, b=e^(-epsilon), and let F_epsilon consist of ALL Borel laws obeying epsilon privacy for EVERY Borel event and EVERY shift in the FULL CLOSED unit l1 diamond D. Put

    J(mu)=E_mu||X||_2^2,       W(mu)=E_mu||X||_1^2,
    V=inf_F J,                 W_*=inf_F W,
    H(lambda)=inf_(mu in F) [J(mu)+lambda W(mu)],    lambda>=0.

The objectives are squared Euclidean and squared l1; this is NOT PMLR's first-power l1 objective. Every infimum in H is over the SAME original all-law class, not a radial ansatz. Define mu_J as the unique actual J optimizer and `W_J=W(mu_J)`.

At the explicitly named parent-supported inputs and written strict-equality proof below:

1. For every lambda>=0, H(lambda) is finite and ATTAINED. It is nondecreasing, concave and globally Lipschitz with constant W_J. For any actual minimizers at 0<=lambda<kappa, their J costs are nondecreasing and W costs nonincreasing with the weight.
2. `H(lambda)>=V+lambda W_*` always. If the actual original core is diamond (epsilon<=epsilon_t), equality holds for ALL lambda>=0 and mu_J is the UNIQUE H minimizer. If the actual core has the separately supported rounded arc (epsilon>epsilon_t), the inequality is STRICT for EVERY lambda>0. Equality at lambda=0 is tautological in both regimes.
3. The actual all-law frontier has the exact end asymptotics

       H(lambda)=V+lambda W_J+o(lambda)                    as lambda->0+,
       H(lambda)=(lambda+2/3) W_*+o(1)                   as lambda->infinity.  (1)

   For ANY choice of H minimizers as lambda->0, the laws converge weakly and in Euclidean W2 to mu_J. As lambda->infinity, their W values converge to W_*, their J values converge to `(2/3)W_*`, and EVERY weak cluster law is a W optimizer. This note does NOT assume or assert uniqueness of all W-optimizers or a unique limiting law at infinity.

The strict rounded-side statement requires actual attainment, not an inference from a trial family or an unattained infimum. It neither proves a new source's optimizer nor gives a scalarized finite-lambda selector/threshold, strict concavity, a uniform epsilon gap, nonadditive channels or novelty.

## 2. Exact research inputs and noncircularity

- Parent LAW642 `privacy-all-law-self-contained-parent-v1.md`, SHA `c08f6353f121ef9e35da0e9d5e8ec9c87b0da838be0d1adf38b807010a1cd979`, gives finite V and unique original mu_J with actual convex core.
- Parent separately adopted v241 `privacy-v241-separated-threshold-and-norm-gap-entire-parent-v1.md`, SHA `48274df7a84b16cd8ead4a0b9069b8359110e1b216bc72e6baea1de03e626138`, states the actual core is a full diamond exactly at/below its positive threshold and has a genuine rounded arc above. Its LAW642/NORM148 and historical review qualifications remain.
- Parent MDA alternative per-cost/rearrangement theorem `privacy-MDA26-entire-norm-cost-and-weighted-decay-parent-v1.md`, SHA `75614a6fc5cb66d9b26f13e64e58935fe6ea52121948e7a56592b91611576ac3`, supplies full-law matching-norm W attainment and a fully private equimeasurable radial rearrangement. The strict equality conclusion below is derived here, not automatically imported. The printed-source NR-A/NR-D qualifications persist.

No earlier unreviewed own equality/TV/asymptotic candidate, f68 radius assertion, v253 composition, or external-publication independent-optimality claim is a premise. Ordinary imports: Tonelli/layer cake, strict geometric bathtub, Prokhorov/Portmanteau, weak closure of Radon measure order, and weak-plus-second-moment W2 convergence.

## 3. Every W optimizer is centered radial and has J=(2/3)W_*

Let mu be ANY actual W-minimizer; one exists by the named per-cost theorem and has W_* finite because a feasible product-Laplace law has finite second moments. Its source-provided centered nonincreasing D-radial rearrangement p-sharp is fully private, equimeasurable and has no greater W-cost. For any finite-volume density superlevel A_s and equal-area centered ball B_s=R_s D,

    integral_(A_s) r^2 - integral_(B_s) r^2
      = integral_(A_s minus B_s)(r^2-R_s^2)
       +integral_(B_s minus A_s)(R_s^2-r^2) >=0.

An l1 sphere has zero planar area; strict monotonicity of r^2 makes the inequality strict unless the two sets agree a.e. W-optimality and layer cake force equality for almost every s, hence the SAME original law equals its centered radial rearrangement. This argument does not claim anything for non-strict radial costs.

For every such radial density, quadrant polar integration gives extended identity `J=(2/3)W`; in particular every W optimizer has

    J=(2/3) W_*.                                                         (2)

This is an equality for a proved radial optimizer, not the false pointwise identity J=(2/3)W for an arbitrary original law. It does NOT by itself prove that the W optimizer law is unique.

## 4. Attainment and exact diamond/rounded equality criterion

For any lambda>=0, a minimizing sequence for H has bounded J because `J+lambda W>=J`; an explicit feasible finite-cost law supplies a finite upper bound. Tightness/Prokhorov give a weak limit. For each fixed h, the nonnegative compactly supported continuous-test form of the full event inequality passes through the SAME weak sequence; Radon measure order then gives every Borel event. The arbitrary h is not tied to an exceptional subsequence. Thus the limit is still in F. Both J and W are nonnegative lower semicontinuous integrals, so H is attained.

For all mu, `J>=V` and `W>=W_*`, hence `H>=V+lambda W_*`. On the diamond side, mu_J is centered D-radial and `V=(2/3)W_J`. Choose an actual W optimizer nu; by (2), `J(nu)=(2/3)W_*`, so `V<=(2/3)W_*`. Since `W_J>=W_*`, the reverse inequality follows. Therefore W_J=W_*, and mu_J attains the lower bound for every lambda. Equality in H forces J=V and LAW642 uniqueness makes mu_J the only minimizer, including lambda=0.

On the rounded side, the actual core of mu_J has a genuine curved arc and cannot be a centered diamond. If mu_J were W-optimal, §3 would force its density to be centered D-radial nonincreasing; its highest superlevel would then be a centered D-ball a.e. The actual canonical highest superlevel is the compact convex core S; equality of the two convex bodies up to null sets forces equality of the sets, contradicting the genuine arc. Thus W_J>W_*. Every W optimizer also differs from the unique mu_J and by (2) has `J=(2/3)W_*>V`.

For lambda>0, H is attained. If its value equalled `V+lambda W_*`, its attaining law would have to attain BOTH separate minima, forcing it to equal mu_J and contradicting `W_J>W_*`. Hence the strict rounded-side inequality. This is an actual-minimizer argument, not nonattainment-based handwaving.

## 5. Concavity, monotone choices, and the lambda=0 endpoint

H is the infimum of affine nondecreasing functions of lambda, so it is concave and nondecreasing. Let mu_lambda be ANY minimizer for lambda>0. Comparison with mu_J gives

    J(mu_lambda)+lambda W(mu_lambda) <= V+lambda W_J.

Since J>=V, `W(mu_lambda)<=W_J`. Thus, for kappa>lambda>=0, comparison at the lambda minimizer gives `H(kappa)-H(lambda)<=W_J(kappa-lambda)`; nondecrease gives the other side, proving global Lipschitz continuity.

For 0<=lambda<kappa, take ANY choices mu_lambda,mu_kappa. The two optimality inequalities imply

    W(mu_lambda)>=W(mu_kappa),       J(mu_lambda)<=J(mu_kappa).           (3)

No strict monotonicity is inferred; a whole interval of shared minimizers is not excluded.

As lambda->0+, `V<=J(mu_lambda)<=V+lambda W_J`. Tightness and weak privacy closure show every cluster law is the unique mu_J. Hence the whole family of arbitrary choices converges weakly and J moments converge to V; the standard W2 criterion yields Euclidean W2 convergence. Since `W(x)=||x||_1^2<=2|x|_2^2`, W2 convergence and uniform integrability yield `W(mu_lambda)->W_J`. Moreover

    0 <= [J(mu_lambda)-V]/lambda <= W_J-W(mu_lambda) ->0.

Substitution proves `H(lambda)=V+lambda W_J+o(lambda)`.

## 6. The lambda=infinity endpoint without W-optimizer uniqueness

Let nu be ANY W optimizer. It is finite-cost and has `J(nu)=C:=(2/3)W_*` by §3. For ANY lambda>0 and ANY H-minimizer mu_lambda,

    J(mu_lambda)+lambda W(mu_lambda) <= C+lambda W_*,
    0<=W(mu_lambda)-W_* <=(C-V)/lambda,
    J(mu_lambda)<=C.                                                     (4)

Thus any sequence lambda->infinity and any choices of minimizers has a weakly convergent subsequence, because J is bounded. A weak cluster law is private, W-lower-semicontinuity and (4) make it W-optimal, and §3 forces its J value to be C. J-lower-semicontinuity then yields `J(mu_lambda)->C` along the WHOLE arbitrary-choice sequence. Finally

    0<=lambda[W(mu_lambda)-W_*] <= C-J(mu_lambda)->0.

Hence `H(lambda)=lambda W_*+C+o(1)`, proving the second part of (1). Any weak cluster is W-optimal; if future review proves W uniqueness, one may strengthen this to convergence to that single law, but this note does not assume it. No unsupported interchange of minimization and lambda limit is made.

## 7. Bounded exact radial controls

At exact b=1/2, two actual centered diamond staircases give the following Fraction outputs (the identity J=(2/3)W holds for this radial class):

```text
feasible centered staircase gamma= 1/2 W= 1697/136 J= 1697/204 mixed_lambda1= 8485/408 identity= True
feasible centered staircase gamma= 3/4 W= 10763/864 J= 10763/1296 mixed_lambda1= 53815/2592 identity= True
for lambda=1 mixed centered-radial objective factor= 5/3
```

These are actual full-D-private laws, but they do NOT test the unrestricted rounded-side minimum or establish (1)–(4). The arguments above are written, conditional on the three named parent results. In particular no PMLR first-norm selector is promoted to a squared-cost optimizer.

## 8. Review and nonclaims

Request disjoint review of strict rearrangement equality, the global J/W-common-minimizer criterion, all-shift weak closure, arbitrary minimizer choices and BOTH endpoint asymptotics. No all-lambda closed-form H, scalarized core, phase diagram beyond the lower-bound equality criterion, original nonadditive channel, independent-model/human/formal/kernel or novelty acceptance is claimed. Historical held material is not an input.
