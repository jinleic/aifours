# A universal gluing inequality and almost-entropic separation

**Status: WRITTEN, based on the independently checked exact nine-row identity.** This addendum strengthens `frontier-20261028-star-primal-nonentropic-addendum-v1.md` (SHA-256 `f47010663e53aa3bdf443f6d9190109931fc6301686bc04acb7d20da8d1a0393`). The earlier addendum did not claim separation from the almost-entropic closure; the argument below establishes it for the **specific fixed star primal only**. It does not establish non-entropicity of the original-variable base projection with different auxiliaries and gives no numerical improvement to the guessing-number upper bound.

## Universal inequality

Let `X=(a,b,c,d,e,f,g,h,i,j)` and let `D,F` be **arbitrary** additional finite random variables. Define `L` as the following 16-term entropy expression; juxtaposition denotes a joint entropy:

\[
\begin{aligned}
L={}&-H(abcefgij)-H(abdefgij)+2H(abcdefghij)\\
&+H(abcefgijD)+H(abdefgijD)-H(abcdefgijD)-H(abefghijD)\\
&+H(abcefghijD)-H(abcdefghijD)\\
&-H(abefgijF)+H(abcefgijF)+H(abdefgijF)+H(abefghijF)\\
&-H(acefghijF)+H(acdefghijF)-2H(abcdefghijF).
\end{aligned}
\]

Every finite joint law satisfies **`L >= 0`**. No graph FD, source copy assumption or prior conditional independence is required. Therefore the same homogeneous linear inequality holds on the almost-entropic cone, by continuity and closure.

Proof. The exact identity in the preceding addendum states

\[
L=\sum_{k=1}^{8} I_k-2I(D;F\mid X),
\]

where the eight explicitly listed `I_k` are conditional mutual informations. Every entropy term in `L` lies within either `(X,D)` or `(X,F)`: there is no mixed `D,F` term. For any given law `P(X,D,F)`, construct

\[
Q(X,D,F)=P(X)P(D\mid X)P(F\mid X).
\]

The `(X,D)` and `(X,F)` marginals under `Q` are exactly those of `P`, so `L(P)=L(Q)`. Under `Q`, `I(D;F|X)=0`; every `I_k(Q)>=0`. The identity gives `L(P)=L(Q)=sum_k I_k(Q)>=0`. QED.

Permuting the ten original variables or substituting other auxiliary variables for `D,F` preserves the proof. In particular all `9*10P4=45,360` active-role/per-auxiliary-pair substitutions used in the accompanying exploratory LP are individually valid entropy inequalities. Their novelty is not asserted.

## Consequence for the fixed star primal

The exact independently verified fixed star marginals have

\[
L=-\frac{12637}{1725000}<0.
\]

They therefore cannot be the `(X,D)` and `(X,F)` marginals of any entropic vector and lie outside the projection of the almost-entropic cone: every almost-entropic vector satisfies `L>=0`. Consequently the **specified** star primal point is outside the almost-entropic cone, even up to positive scaling. This conclusion requires neither the star's `U`-independence equalities nor the existence of its other auxiliary variables.

Only the *particular auxiliary values* are excluded. The 1,023-coordinate original profile may still be entropic or almost-entropic with different copy marginals. The publisher LP and star-LP optimum proofs remain valid as LP statements; neither is promoted to a guessing-number bound. A reoptimized exact producer candidate has already passed the first `L` cut, showing that excluding the old fixed star point alone does not exclude the original profile.

## Exact evidence

* The eight CMI identities and the original fixed-marginal context are listed in `frontier-20261028-star-primal-nonentropic-addendum-v1.md`.
* Independent identity checker `frontier-20261028-cross-pair-farkas-independent-check.py` SHA-256 `b69af7b6bf2dad9726c8311c1d34e5ef9707a56218b2f3e38f50041e36245c51`; receipt SHA-256 `199a7471622c6c3085a669e2b43e7235676e680ee7e8cb3fa8f636449a1aff45`. It verifies all eight CMI rows, the `-2 I(D;F|X)` row, exact cancellation of mixed entropy coordinates, the 16 known-term coefficients and exact negative value, and rejects five in-memory mutations.
* The fixed star candidates are `frontier-20261028-crossbranch12-exact-candidate.json` SHA-256 `1037f7daf3cea8700b8b0a4a8c4f9981bc563a6b1038fdf91def9e921e84c739` and `frontier-20261028-crossbranch13-fixed-u-exact-candidate.json` SHA-256 `9744448c5473f3781ef616d46c5615dff649c0f4581dcf7f9bbd4b5c25ee9ce1`.
* The independently checked one-cut reoptimization `frontier-20261028-crossbranch13-one-cut-independent-check-result.json` SHA-256 `7a20443b80d1395167a693869071a21e8f92158685dd312feb9e0f42cf41816b` records first-cut value `4751/1725000`. This is a different auxiliary assignment, not an extension of the old fixed star point.

No cross-model review, proof-assistant verification, or novelty clearance was performed. The universal inequality's existence does not by itself improve the original numerical upper bound.
