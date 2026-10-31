# A five-variable gluing inequality with an exact Shannon-cone witness

**Status: WRITTEN with a standalone exact integer checker; independent scientific review and novelty clearance pending.** This is the specialization `B=constant` of `frontier-20261028-six-variable-gluing-inequality-v1.md` (SHA-256 `f5c83b572ecc2ec25a62b22e24e405a897b37152385a11a1e31f37f567a07075`). It is a non-Shannon-type entropy inequality in the precise sense below, but may be known or implied by existing non-Shannon inequalities. It does not settle or numerically improve the R-minus guessing-number bound.

## The inequality

For arbitrary finite random variables `C,R,H,P,Q`,

\[
\begin{aligned}
\Psi={}&-H(C)-H(R)+2H(CRH)\\
&+H(CP)+H(RP)-H(CRP)-H(HP)+H(CHP)-H(CRHP)\\
&-H(Q)+H(CQ)+H(RQ)+H(HQ)-H(CHQ)-H(CRHQ)\ge0.
\end{aligned}
\]

Direct expansion gives the exact identity

\[
\begin{aligned}
\Psi={}&I(C;R\mid P,Q)+I(C;Q\mid H,P)+I(R;P\mid C,H,Q)\\
&+I(H;P\mid Q)+I(H;Q\mid C,R,P)+I(P;Q\mid R)+I(P;Q\mid C)\\
&-2I(P;Q\mid C,R,H).
\end{aligned}
\]

All terms in `Psi` use only `(C,R,H,P)` or `(C,R,H,Q)` marginal entropies. Given any joint law, replace the conditional law of `(P,Q)` given `(C,R,H)` by the product of its two conditional marginals. This preserves every term in `Psi` and sets the negative CMI to zero, so the remaining seven CMIs prove `Psi>=0`. Conditioning on any additional vector yields another valid inequality by averaging conditional laws. The inequality is also valid on the almost-entropic cone by closure.

## Exact Shannon-cone separation

Order variable bits `C,R,H,P,Q` from least to most significant. The following integers, divided by four, give all subset-mask values of a five-variable polymatroid:

```
 0–7:   0 4 4 6 4 6 6 6
 8–15:  3 5 5 7 7 7 7 7
16–23:  3 5 5 7 5 7 7 7
24–31:  5 6 6 7 7 7 7 7
```

All `5+10*2^3=85` five-variable elemental Shannon inequalities hold exactly. The inequality evaluates to `Psi=-2/4=-1/2`. Thus `Psi>=0` cannot be a nonnegative linear combination of five-variable elemental Shannon inequalities. This establishes a **non-Shannon-type** inequality without asserting it is new to the literature.

The candidate integer vector was obtained from a floating LP proposal and then checked independently with integer arithmetic; solver optimality is not part of the proof. The reduction from the 16-term six-variable inequality is also checked symbolically by setting `B` constant.

## Evidence

* Exact 32-coordinate witness `frontier-20261028-five-variable-nonshannon-witness-v1.json` SHA-256 `def19d886c86451744a8928a050c779658a6f0228afeccd83487a2b26d2d0392`.
* Standalone checker `frontier-20261028-five-variable-witness-check.py` SHA-256 `b087bb37fd2040aa22976b4c1fb8e9a5e04a37947276279f477b6a764a4cc837`; receipt SHA-256 `95a4d8df8c5f619a31cf9f20376c39956e648256aca0d0d19c306eadbd1d2efc`. It independently expands the seven-CMI/one-negative-CMI identity, verifies the five-variable coefficients equal the `B=constant` six-variable reduction, checks all 85 elemental rows and the exact `-1/2` value, and rejects five intended mutations.
* A complete exact scan of all `967,680` disjoint five-singleton original-variable assignments with optional disjoint conditioning on the fixed publisher-LP base profile found no violation; receipt `frontier-20261028-fivevar-original-singleton-scan-result.json` SHA-256 `a43c41af99e9038078a28359a77b249e0cb360d655cb045999b006c4402312b5`. This is only that substitution scope on one rational LP profile, not an entropy-realization test or a general graph bound.

No proof-assistant formalization, cross-model review, or novelty/SOTA clearance has been performed. A true original-graph improvement would require an actual finite FD law with positive entropy-balance gap or a separately certified unrestricted upper inequality.
