# Directed Renyi moduli and an exact translated-staircase identity

**AUTHOR CANDIDATE — WRITTEN with exact rational affinity checks; NOT independently reviewed or parent-adopted.** Native pre-write clock: `Wed Oct 28 18:22:55 PDT 2026`.

## 1. Original model and exact new conclusions

Fix EVERY finite epsilon>0, b=e^(-epsilon), the FULL CLOSED unit l1 diamond D, and ALL Borel laws F_epsilon satisfying the additive event inequality for EVERY Borel event and every h in D. Let V be the original squared-Euclidean infimum and mu_* its unique law.

For `delta>0` and Renyi order alpha define directed worst-case original-law moduli

    R_alpha^+(delta)=sup{D_alpha(mu||mu_*):mu in F_epsilon,J(mu)<=V+delta},
    R_alpha^-(delta)=sup{D_alpha(mu_*||mu):mu in F_epsilon,J(mu)<=V+delta}.

The candidate separates directions and the infinity endpoint:

1. **Reverse finite orders:** for EVERY fixed `0<alpha<infinity`, `R_alpha^-(delta)->0` as delta decreases to 0. For alpha>1 this is NEW relative to the earlier two-sided-KL/alpha<1 candidate.
2. **Forward orders above one:** for EVERY delta>0 and EVERY fixed `alpha>1`, including infinity, `R_alpha^+(delta)=infinity`. The cost slack is fixed, not merely a divergent sequence of near-optimal points.
3. **Reverse infinity:** for all sufficiently small delta>0, `R_infinity^-(delta)>=epsilon`; hence it does NOT converge to 0, even though every fixed finite reverse order does.
4. **Exact translation identity:** for ANY unit direction e and sufficiently short t>0, let `mu_t=tau_(te)mu_*` and `T=TV(mu_t,mu_*)`. For every finite alpha>0, alpha!=1,

       D_alpha(mu_t||mu_*)=D_alpha(mu_*||mu_t)
        = log[1+c_alpha T]/(alpha-1),
       c_alpha=[b^(1-alpha)+b^alpha-(1+b)]/(1-b);                         (1)

   at alpha=1 BOTH KL divergences equal exactly `epsilon*T`, and at alpha=infinity BOTH directed max divergences equal exactly epsilon. The original cost of mu_t is V+t^2.

The earlier KL candidate supplied forward/reverse KL and alpha<1 convergence plus a diverging forward alpha>1 sequence. This note strengthens the reverse FINITE range, the forward fixed-slack supremum, and gives exact translation formulas. It claims no matching optimal upper TV rate, no epsilon-uniform rate, no nonadditive channel, source priority or novelty.

## 2. Named inputs and f68 correction

- Parent-WRITTEN_SUPPORTED LAW642 original all-law theorem `privacy-all-law-self-contained-parent-v1.md`, SHA `c08f6353f121ef9e35da0e9d5e8ec9c87b0da838be0d1adf38b807010a1cd979`: unique centered optimizer mu_* with finite V and density `p_*=Z^(-1)b^(n_S)`, `n_S=min{k:x in S+kD}`, S compact convex centrally symmetric, 0 interior.
- My UNREVIEWED `frontier-20261028-all-law-tv-stability-v1.md`, SHA `3f6c2a61738cc92f615e375d88f6dfb10f96b553585b5c8468480a7ec9683f79`, gives the uniform near-optimal TV modulus. Its f68 review, SHA `901186e44e95fce0456f19ca06a411e5eb1b0f6b83cd7cc01b661d474f830b19`, found 0F/1M/1m; the diamond-radius repair is the ADDITIVE `frontier-20261028-all-law-tv-stability-v1-addendum-1-f68-radius-repair.md`, SHA `05d802dd109d144ac10655d1a1f0e42de652e4305f3b51239f6bbcc3e27f8cd4`. The corrected composite has NOT automatically been reviewed/adopted. It is used ONLY for conclusion 1; conclusions 2–4 and all translation computations are direct from LAW642 and elementary facts.

Renyi convention for alpha>0, alpha!=1 is `(alpha-1)^(-1)log integral p^alpha q^(1-alpha)`; alpha=1 is KL and infinity is essential supremum of log likelihood ratio.

## 3. Global reverse likelihood-ratio bound

Every law in F_epsilon has a density bounded above by `C=1/(2b)` and an all-point private representative via the shrinking-ball limsup. The canonical p_* additionally has an upper tail of the SAME exponential rate: if S subset M D, then membership `x in S+n_S(x)D` gives `n_S(x)>=||x||_1-M`, so

    p_*(x)<=Z^(-1)b^(-M) exp(-epsilon||x||_1).                          (2)

By the named corrected-TV theorem, omega_epsilon(delta)->0. Choose delta0>0 so all laws with J<=V+delta0 satisfy `mu(D)>=eta>0`, because mu_*(D)>0. For such a law, chain full-D privacy from each y in D to x and integrate y: its private representative obeys

    p(x)>=c exp(-epsilon||x||_1),       c=eta b^2/2>0.                    (3)

Thus the REVERSE likelihood ratio `r=p_*/p` has a fixed finite global upper bound `K=Z^(-1)b^(-M)/c`, simultaneously for all sufficiently near-optimal laws. It need not have a comparable bound tending to 1.

For fixed alpha>1, the function r^alpha is Lipschitz on [0,max(K,1)], and

    |integral r^alpha p-1|
       <= alpha max(K,1)^(alpha-1) integral |r-1|p
       = 2 alpha max(K,1)^(alpha-1) TV(mu,mu_*).                         (4)

The corrected TV modulus makes the right side tend to 0 UNIFORMLY over all costs<=V+delta, proving `R_alpha^-(delta)->0`. For alpha=1, Jensen gives `D_KL(mu_*||mu)<=D_2(mu_*||mu)`. For 0<alpha<1, `min(p,p_*)<=p_*^alpha p^(1-alpha)` and Holder show the affinity lies between `1-TV` and 1. This proves conclusion 1 for EVERY fixed finite alpha without requiring a new second-moment tail argument.

This argument is conditional on the ORIGINAL TV candidate TOGETHER WITH the f68 radius repair and the named LAW642/v241 imports. F68's original 0F/1M/1m verdict is preserved; this successor has not been independently reviewed by f68 or parent-adopted.

## 4. Arbitrarily large forward Renyi cost at ANY fixed positive slack

Fix ANY delta>0. For integers R large enough that `w=delta/R^2<1`, define

    nu_R=(1-w)mu_*+w tau_(R e1)mu_*.

The same-law translations and mixtures remain full-D private. Central symmetry of mu_* gives `J(nu_R)=V+wR^2=V+delta` EXACTLY. On a far positive-quadrant rectangle beyond both cores, both component densities drop by b under e1, so nu_R in fact has exact epsilon privacy.

Choose an actual ball A inside int S, with `mu_*(A)=a>0`, and put E_R=R e1+A. Then `nu_R(E_R)>=a delta/R^2`. Compactness of S and its exact staircase tail give `mu_*(E_R)<=C_1 exp(-epsilon R)`.

For any fixed alpha>1, Jensen/Holder yields

    D_alpha(nu_R||mu_*) >= epsilon R - [2alpha/(alpha-1)]log R
                           +[alpha/(alpha-1)]log delta - O(1),           (5)

which diverges as R->infinity. The event likelihood-ratio lower bound gives the same infinity-order conclusion. Thus the supremum is literally infinity at EVERY fixed positive delta, not just nonuniform in alpha or a particular sequence. Each constructed finite-R divergence is itself finite because iterating DP R times bounds `tau_(R e1)mu_* <= exp(epsilon R)mu_*`.

## 5. Exact all-order formula for short translations

Let `K_k=S+kD`, and take a Euclidean unit direction e. The Euclidean distance between distinct nested level boundaries is at least 1/sqrt(2), since D contains that-radius ball. For `0<t<1/(2sqrt(2))`, the level symmetric-difference bands of `K_k` and `K_k+t e` are pairwise disjoint. Each convex-body translation has equal entering and leaving AREA, denoted

    A_k(t)=|(K_k+t e) minus K_k|=|K_k minus (K_k+t e)|.

On an entering band, translated density / original density is 1/b; on its paired leaving band it is b. Both bands have area A_k and are crossed at ONLY this single level. Elsewhere the two densities agree. Hence

    T=TV(tau_(t e)mu_*,mu_*)=(1-b)/Z sum_(k>=0)b^k A_k(t).              (6)

Directly integrating the two constant density pairs gives the exact Renyi affinity

    integral p_t^alpha p_*^(1-alpha)
       =1+[b^(1-alpha)+b^alpha-(1+b)] T/(1-b).                           (7)

Interchanging the densities swaps alpha with 1-alpha and leaves the bracket unchanged. This proves (1) and equality of the two directed finite-order divergences for these translations. Taking alpha->1 or computing the two logarithmic bands directly gives

    D_KL(mu_t||mu_*)=D_KL(mu_*||mu_t)=epsilon T.                          (8)

Both entering and leaving bands have positive area for nonzero small t because S has interior, so the essential likelihood ratios attain respectively b^(-1) and b. Thus BOTH directed D_infinity values are exactly epsilon. The actual cost is V+t^2 by central symmetry, giving `R_infinity^-(delta)>=epsilon` for sufficiently small delta. This does not assert any upper bound on that worst-case reverse infinity modulus.

## 6. Exact arithmetic check and dependency propagation

For a synthetic b=1/2, gamma=1 diamond staircase and axis shift t=1/10, a previously directly integrated slice formula gives `T=79/2400`. Exact Fraction arithmetic produced

```text
alpha= 2 exact_affinity_coefficient= 3/2 exact_affinity= 1679/1600
alpha= 3 exact_affinity_coefficient= 21/4 exact_affinity= 3753/3200
KL equals (79/2400)*log(2), and max-divergence equals log(2) for this short translation
```

The last line is a human-readable formula label; the exact all-level/area identity is the written proof in §5, not certified by that print. This selected synthetic core is not claimed to be the original optimum.

The earlier `frontier-20261028-kl-renyi-order-cutoff-v1.md`, SHA `fbd0f94a2668ad8bb3cb86bac5977320031c3b293929b413528cb6acd5cb4e38`, has the additive f68 dependency qualification `frontier-20261028-kl-renyi-order-cutoff-v1-addendum-1-f68-dependency.md`, SHA `97bb6851bdffd601cd9a9452172a5972f5f968e36ededbf1a8af69b0a6d64424`. This successor explicitly carries the SAME TV-body/review/repair scope for its reverse finite-order theorem; it does not imply that any candidate or repair was reviewed automatically.

## 7. Review boundary

Request disjoint review of the uniform reverse likelihood bound, alpha-to-one argument, arbitrary fixed-slack forward construction, disjoint level bands and exact Renyi affinity. No formal/kernel/human/configured-family or independent-model acceptance, worldwide novelty, all-epsilon uniformity, or source-proof repair is claimed. Historical held outcomes are not accepted premises.
