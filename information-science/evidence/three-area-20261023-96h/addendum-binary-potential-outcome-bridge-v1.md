# Operative addendum: binary factual data versus binary potential outcomes

**Status: CANDIDATE / written correction and proof.** This addendum addresses the parent's exact feasible-set distinction. Read it with `proof-bounded-outcome-sharp-bounds-v1.md` and `proof-binary-reduction-v1.md`; their frozen bytes are not changed. No program or new review is claimed by creating this addendum.

## 1. Corrected statement

For binary factual data, the bounded-real model in the main manuscript still permits nonbinary **unobserved** potential outcomes. Yin et al.'s binary model requires both potential outcomes Y_0,Y_1 to be binary. Therefore these are **not literally the same full-data feasible set**. The main manuscript Section 6.2's phrase about minima/maxima of the same feasible set must be read as a claim about the **same projected attainable delta interval**, justified by the explicit bridge below, not by equality of the underlying law sets.

The companion's direct four-hinge calculation recovers the seven lower and upper expressions algebraically; it does not by itself identify the latent domains. The following lemma supplies that missing domain comparison and makes the source match exact.

## 2. Conditional Bernoulliization lemma

Suppose a compatible bounded-real law has factual outcomes y=Y_B in {0,1}, where B=S_0. Keep the original B,y,S_1,Z from the main proof, with

    Z=Y_1 on B=0,  Z=1-Y_0 on B=1.

Enlarge the probability space by a uniform R on [0,1], independent of the entire original tuple, and set

    Z'=1{R<=Z}.

Then

    E[Z' | B,y,S_1,Z]=Z.                                   (1)

Define new potential outcomes by

    on B=0:  Y_0'=y,       Y_1'=Z',
    on B=1:  Y_1'=y,       Y_0'=1-Z'.                      (2)

Both Y_0',Y_1' are binary. The full factual law (B,Y_B') equals the original law of (B,y) exactly; S_0 and S_1 themselves have not changed. Hence the entire supplied mu_0,mu_1 and q are preserved.

The surrogate intervention effect is also preserved, since (1) gives

    E[Y_1'-Y_0'] = g_min+E[Z']
                 = g_min+E[Z] = gamma.                     (3)

Let C={B=0,S_1=1}, D={B=1,S_1=0}. These sets are measurable with respect to the conditioning tuple in (1). Therefore

    E[(1_C-1_D)Z'] = E[(1_C-1_D)Z].                        (4)

The factual tail terms A_0=E[y 1_C], A_1=E[y 1_D] and switch mass t are unchanged. Equation (11) of the main manuscript now yields

    E[Y'_(S_1)-Y'_(S_0)]
      =t-A_0-A_1+E[(1_C-1_D)Z']
      =t-A_0-A_1+E[(1_C-1_D)Z]
      =delta.                                              (5)

A randomized treatment T can be taken independently of the enlarged latent tuple; thus the same strong-surrogate structural interpretation remains valid, with no new treatment-dependent potential outcomes.

Every bounded-real law with binary factual data has therefore been mapped to an all-binary potential-outcome law with the same observables, gamma and delta. The converse inclusion is immediate because binary outcomes are bounded real outcomes. Consequently the **entire projected delta sets are equal**, not just the extrema. Compatibility and interval attainment match as well.

## 3. Consequence for the primary-source baseline

Equations (8)–(9) of `proof-binary-reduction-v1.md` are an independent algebraic reduction of the scalar quantile formulas to the exact seven lower and seven upper terms in Yin–Liu–Geng–Luo's Theorem 1. The conditional Bernoulliization lemma now proves that the two latent-domain conventions have exactly the same attainable delta projection on binary factual data. This closes the domain bridge without importing the source's sharpness argument or claiming equality of full feasible-law sets.

**Correction scope:** the main arbitrary bounded-real Theorem 1, its constructive attainment, Theorem 2 and uniform example are unchanged. This repairs a baseline-comparison justification, not a claimed new binary theorem. All-binary sharp bounds remain prior work. Parent and independent acceptance of this new addendum must be recorded separately; their earlier readings cannot be retroactively extended to it.
