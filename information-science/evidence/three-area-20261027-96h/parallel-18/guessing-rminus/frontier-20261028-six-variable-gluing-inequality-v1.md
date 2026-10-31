# A six-variable gluing inequality with an exact Shannon-cone separator

**Status: WRITTEN with two separately implemented exact checks.** The inequality is valid for all finite entropy laws and is not implied by the six-variable elemental Shannon inequalities. Its novelty is **not established**: it may be known or derivable from known non-Shannon inequalities. This result does not give a new numerical upper bound for the original R-minus guessing number. No cross-model review or proof-assistant verification was performed.

## Inequality and gluing proof

For arbitrary finite random variables `B,C,R,H,P,Q`, the following 16-term expression is nonnegative:

\[
\begin{aligned}
\Phi={}&-H(BC)-H(BR)+2H(BCRH)\\
&+H(BCP)+H(BRP)-H(BCRP)-H(BHP)+H(BCHP)-H(BCRHP)\\
&-H(BQ)+H(BCQ)+H(BRQ)+H(BHQ)-H(CHQ)+H(CRHQ)-2H(BCRHQ)\ge0.
\end{aligned}
\]

Indeed, direct symbolic expansion gives

\[
\begin{aligned}
\Phi={}&I(B;R\mid C,H,P,Q)+I(C;R\mid B,P,Q)+I(C;Q\mid B,H,P)\\
&+I(R;P\mid C,H,Q)+I(H;P\mid B,Q)+I(H;Q\mid B,C,R,P)\\
&+I(P;Q\mid B,R)+I(P;Q\mid B,C)-2I(P;Q\mid B,C,R,H).
\end{aligned}
\]

Although the right side includes a negative CMI, the left side uses only marginals of `Y=(B,C,R,H)` with `P` or with `Q` separately: no term contains both `P` and `Q`. Given any original law, replace the conditional joint law of `(P,Q)` given `Y` by the product of its two conditional marginals. This preserves every entropy in `Phi`, while making `I(P;Q|Y)=0`. The identity then expresses the unchanged `Phi` as eight nonnegative CMIs. Therefore `Phi>=0` for every finite law, and also on the almost-entropic cone by closure.

Conditioning the inequality on an arbitrary additional vector `Z` preserves it by applying it to each conditional distribution and averaging. The 12-variable graph-specific inequality in `frontier-20261028-universal-gluing-inequality-v1.md` (SHA-256 `a017351d672c37c170b5dff4cf6ce76467f5d2460fa04ce81d922de660b48dce`) is exactly this conditioned inequality with `Z=(a,e,f,g,i,j)`, `(B,C,R,H)=(b,c,d,h)` and `(P,Q)=(d'1,f'3)`.

## Exact six-variable Shannon-cone witness

Order the variable bits `B,C,R,H,P,Q` from least to most significant, and let entry `r[m]` be the set function value for subset mask `m`. The following integers, divided by `6,900,000`, give a polymatroid `r`:

```
 0–7:        0  3875000  6900000  6900000  3025000  6900000  8300000  8300000
 8–15: 2975000  5650000  8300000  8300000  5675000  8300000  8300000  8300000
16–23: 6598260 10309011 11178976 11178976  8461329 11329176 12075000 12075000
24–31: 9420084 12075000 12075000 12075000 10057128 12075000 12075000 12075000
32–39: 3280188  6928908  9708504  9708504  5950419  9585546 10950000 10950000
40–47: 5682009  8326158 10950000 10950000  8331852 10950000 10950000 10950000
48–55: 7996200 10825200 11466900 11466900  9479700 11577300 12205200 12205200
56–63: 9969600 12205200 12205200 12205200 10549200 12205200 12205200 12205200
```

All `6+15*2^4=246` six-variable elemental Shannon inequalities hold exactly, while

\[
\Phi(r)=\frac{-50548}{6900000}=-\frac{12637}{1725000}<0.
\]

Thus `Phi>=0` is **not** a nonnegative linear combination of the six-variable elemental Shannon inequalities; it is a genuinely non-Shannon-type entropy inequality in that precise cone-separation sense. This classification is not a novelty claim.

The witness was obtained by taking a rational 12-variable Shannon-polymatroid extension of the two previously fixed graph/copy marginals **without** imposing `I(P;Q|X)=0`, and contracting the six-variable background `Z`. The full 12-variable extension was separately checked on all `67,596` elemental Shannon rows; its value of `I(P;Q|X)` is `12599/34500`, not zero. The six-variable table alone is sufficient for the Shannon-cone separation; no graph, copying, or entropic realization is assumed in that separation.

## Pinned verification

* Compact self-contained witness `frontier-20261028-six-variable-nonshannon-witness-v1.json` SHA-256 `10aa3d5daa42b42223193b5a465aa32e5883b592a916be5d5941ee00bc5dc169`; standalone checker `frontier-20261028-six-variable-witness-check.py` SHA-256 `4b55faa53a9d3043eb4baa9d3fc497934247c37da83b0a04927854697d09fdf6`, receipt SHA-256 `31db5916d7ed6f3eda0d8f5283aeaba16f23f5a60c76f91f14d6830e26a90ad2`. It independently expands the nine CMI terms, verifies all 16 entropy coefficients and mixed-term cancellation, checks all 246 elemental inequalities and the exact negative value, and rejects five intended mutations.
* Separate 12-to-6 contraction checker `frontier-20261028-six-variable-gluing-separation-check.py` SHA-256 `699c5a71fea51e50da2ab5b338d1c200c92a9b03ca4abfbb909f9335b3c514f0`, receipt SHA-256 `f8fcf6201839f32df79baacdb97d81b2a7f89458843ba847c2227ece23f086f9`. It checks the full 12-variable Shannon vector, contracts the pinned background, checks the six-variable vector, and ties its coefficient map to the graph-specific term-map receipt.
* The 12-variable candidate is `frontier-20261028-crosspair-without-independence-candidate.json`, SHA-256 `0259b6597fcaa899a77bf5ccc4274eaaae825ee452304815fa3b44543e1a5bcb`. Source graph and auxiliary-profile provenance are recorded in the preceding addenda; they are not premises of the standalone six-variable inequality.

Applying all 45,360 tested graph-copy substitutions of this one inequality did not improve the specified star LP, as documented separately; other substitutions, inequalities, extensions and the original R-minus entropy-realizability gap remain open.
