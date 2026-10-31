# Near-optimal matching-cost laws: TV/W1 versus TV/W2

**AUTHOR CANDIDATE — WRITTEN with one exact rational mixture check; NOT independently reviewed or parent-adopted.** Native pre-write clock: `Wed Oct 28 18:12:21 PDT 2026`.

## 1. Actual all-law conclusions

Fix EVERY finite epsilon>0, put b=e^(-epsilon), and let F_epsilon be ALL Borel probability laws satisfying epsilon privacy for EVERY Borel event and EVERY shift in the full CLOSED unit l1 diamond. Define

    L(mu)=E_mu ||X||_1,       W(mu)=E_mu ||X||_1^2,
    L_*=inf_(mu in F_epsilon)L(mu),     W_*=inf_(mu in F_epsilon)W(mu).

At the explicitly named, as-yet UNREVIEWED equality/erosion inputs below, the unique all-law minimizers are the actual centered staircases `mu_L=Q_gamma1`, `mu_W=Q_gamma2`, with 0<gamma1<gamma2<1. For fixed epsilon:

1. ANY feasible sequence with `L(mu_n)->L_*` converges to mu_L in TOTAL VARIATION and in Wasserstein-1 for the l1 ground metric. Its density converges to the optimum in every finite Lp norm. Both directions of KL divergence also converge to zero.
2. ANY feasible sequence with `W(mu_n)->W_*` converges to mu_W in TOTAL VARIATION and in Wasserstein-2 for the l1 ground metric, hence also in Euclidean W2. Its density converges in every finite Lp norm, and both KL directions go to zero.
3. FIRST-moment near-optimality does NOT imply finite-second-moment convergence or Euclidean W2 convergence. An explicit exact-epsilon, full-D-private sequence in §6 has `L(mu_n)-L_*<=1/n` but `E|X|_2^2=E_mu_L|X|_2^2+n`, diverging.

The Wasserstein claims use the actual whole-law moment convergences, not TV alone. These are matching-cost/source-interface results; they do not identify the registered Euclidean optimizer or extend PMLR's first-moment theorem to a squared-cost theorem.

## 2. Exact named inputs

- Parent-WRITTEN_SUPPORTED alternative matching-norm per-cost attainment `institute/runs/three-area-2026-10-23-96h/privacy-MDA26-entire-norm-cost-and-weighted-decay-parent-v1.md`, SHA `75614a6fc5cb66d9b26f13e64e58935fe6ea52121948e7a56592b91611576ac3`.
- My UNREVIEWED strict-cost equality/unique all-law optimizer candidate `frontier-20261028-strict-radial-optimizer-equality-v1.md`, SHA `e4f4a4909e5cf6ae734f17fdaf2edb4c4919c9162048dc2cf249209b99c5ff97`, with its scalar root/order dependency `frontier-20261028-universal-pmlr-selector-separation-v1.md`, SHA `4c92d56867a959298836063d0045634cd61a0efb8f3175fcb701c4ac4a722fc6`.
- My independent UNREVIEWED geometric iff `frontier-20261028-staircase-erosion-tv-criterion-v1.md`, SHA `2390d99df92b2a2254cc431a8c849613d0aea478dd00421a10e4ec25dce76758`: weak->TV continuity at Q_S iff the core erosion `{x:x+D subset S}` has planar area zero.

These are written-support/author dependencies at their precise states, not automatically reviewed theorems. No LAW642, v241, v253, Euclidean-optimum proof, publisher proof repair, or held source is used here. Standard imports include Portmanteau/Prokhorov, the Wasserstein weak-plus-moment criterion, Radon density and elementary relative entropy.

## 3. Compactness and TV at either actual staircase optimizer

For i=1,2 the scalar optimizer core is S_i=gamma_i D with gamma_i<1. Its erosion by D is EMPTY: if some x+D were contained in the centrally symmetric convex gamma_i D, symmetry and averaging would imply D subset gamma_i D, impossible. Thus the named erosion criterion applies to Q_gamma_i.

Suppose L(mu_n)->L_*. The first l1 moments are bounded, so Markov tightness and Prokhorov give a weakly convergent subsequence. Every weak limit is full-D private: pass the nonnegative compactly supported continuous-test version of the event inequality for each h through the SAME subsequence, then use Radon measure order. Lower semicontinuity of ||x||_1 makes its cost <=L_*. The named all-law uniqueness forces the limit to be mu_L. Every subsequence has this same limit, so the WHOLE original sequence converges weakly to mu_L. Erosion-null weak-to-TV continuity then gives TV(mu_n,mu_L)->0.

The argument for W is identical with the squared l1 moment, giving weak then TV convergence to the unique mu_W. It uses full original laws, not only radial mechanisms. It also gives a uniform cost-gap-to-TV modulus tending to 0 for each fixed epsilon by the standard contradiction/sequential selection argument; no numerical upper rate is supplied.

## 4. Wasserstein orders and all finite density Lp norms

For any metric d and p>=1, the standard Wasserstein criterion says weak convergence plus convergence of the pth d-distance moment to the limiting pth moment is equivalent to W_p convergence. In the mean problem the actual assumption is precisely convergence of `E d_1(X,0)` with `d_1(x,y)=||x-y||_1`; hence `W_1^{d_1}(mu_n,mu_L)->0`.

In the squared problem, the assumption is precisely convergence of `E d_1(X,0)^2`, so `W_2^{d_1}(mu_n,mu_W)->0`. The Euclidean distance is bounded above by d_1; taking the SAME couplings shows ordinary Euclidean W2 is no larger. TV is separately supplied by §3, not a consequence of Wasserstein alone.

Privacy plus Tonelli gives every feasible density the same a.e. upper bound C=1/(2b). Thus for every finite 1<=p<infinity,

    ||p_n-p_*||_p^p <= C^(p-1)||p_n-p_*||_1 =2C^(p-1)TV(mu_n,mu_*),

with p_*=the appropriate cost optimizer density. This establishes all finite density Lp convergences simultaneously. It does not establish L-infinity or pointwise uniform convergence.

## 5. Both relative-entropy directions

TV convergence to either actual positive staircase implies eventual mass `mu_n(D)>=eta>0` in the fixed unit diamond. Replacing densities by bounded ball-limsup pointwise-private representatives and chaining unit-diamond shifts yields one common bound

    c exp(-epsilon||x||_1) <= p_n(x),p_*(x) <= 1/(2b),                  (1)

for all x and all sufficiently late n. On every compact diamond, both are uniformly bounded away from 0 and infinity, so local L1 convergence makes BOTH `p_n log(p_n/p_*)` and `p_* log(p_*/p_n)` integrals tend to 0.

For either cost problem, the actual l1 first moments converge to the limiting first moment. In the W case this follows from W2^{d1}; in the L case it is the assumption. Weak convergence plus first-moment convergence gives uniform integrability of ||x||_1 (e.g. truncate a continuous distance function and compare the converging moments). Combined with (1), it makes the tails of BOTH log-likelihood integrals uniformly small. Thus both KL directions go to zero. This is not inferred from TV without privacy/moment bounds and is not a claim for Renyi orders >1.

## 6. Sharp negative example for W2 under mean near-optimality

Let X have the actual mean-optimal law mu_L=Q_gamma1, which is centered, symmetric and has finite second moment. For each integer n>=2 set

    R_n=n^2,       w_n=n^(-3),
    nu_n=(1-w_n)mu_L + w_n tau_(R_n e1) mu_L.

Both components are full-D-private and their mixture is private for EVERY event. The reverse triangle inequality gives

    0 <= L(nu_n)-L_* <= w_n R_n = 1/n -> 0,                            (2)

where the lower bound uses global mean optimality. Central symmetry gives E X=0, so the exact Euclidean second moment is

    E_nu_n |X|_2^2 = E_mu_L |X|_2^2 + w_n R_n^2
                  = E_mu_L |X|_2^2+n -> infinity.                      (3)

Consequently Euclidean W2 cannot converge to mu_L; in fact the reverse triangle inequality in L2 couplings bounds it below by the difference of the square roots of these second moments, which diverges. Meanwhile `TV(nu_n,mu_L)<=w_n` and the obvious coupling gives `W1^{d1}<=w_n R_n=1/n`, consistent with claim 1.

These laws also have EXACT epsilon privacy. Far in the positive quadrant, the centered staircase density and its R_n e1 translate BOTH drop by exactly b under the same shift e1. Their mixture has the same exact drop on any bounded open rectangle there, and its event ratio attains e^epsilon. The counterexample is not a finite-parameter nonprivate approximation or a source-derived claim.

A bounded Fraction check at n=10 produced

```text
n= 10 shift= 100 weight= 1/1000 mean_gap_upper= 1/10 euclidean_second_moment_increase= 10
exact_mixture_privacy_ratio_preserved_by_convexity: True
```

The last Boolean checks only that the chosen mixture weight lies in (0,1); the full privacy proof is the written convexity/far-tail argument above. One selected n is not the asymptotic proof.

## 7. Limits and review obligations

All-law uniqueness and the erosion criterion are explicitly UNREVIEWED author candidates; the preceding parent per-cost existence result alone does NOT establish this full conclusion. Request disjoint review of the compactness/metric-moment criteria, the mean-cost uniform-integrability KL tail and the exact translated-mixture caller. No global Euclidean optimizer, named-publication priority, nonadditive channel, formal/kernel/human/configured-family or independent-model acceptance is claimed. Historical held results remain unvalidated nonpremises.
