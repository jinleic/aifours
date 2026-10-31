# Two-Ingleton certificate and quantitative nonlinear gate

**Status: WRITTEN with separate exact rational certificate checking.** This strengthens `frontier-20261028-linear-ingleton-bound-v1.md` (SHA-256 `e056dd9695a4b3e308431441b4f15ec3a2d81f3c733c604cff8246796abf3da4`). The original unrestricted upper bound is not improved here.

## Exact two-defect identity

Use the graph, the eight-element automorphism group `G`, the graph-FD notation, and the definition

\[
J(A,B;C,D\mid Z)=I(A;B\mid C,Z)+I(A;B\mid D,Z)
+I(C;D\mid Z)-I(A;B\mid Z)
\]

from the preceding packet. Let the two specific conditional Ingleton expressions be

\[
\begin{aligned}
J_1&=J(2,4;1,3\mid 5,6,7,8,9,10),\\
J_2&=J(2,5;3,6\mid 1,4,7,8,10).
\end{aligned}
\]

For **every** finite joint law satisfying the original graph FDs, the exact certificate gives

\[
\frac23\sum_{v=1}^{10}H(X_v)-H(X_V)
=\sum_{i=1}^{99}a_i\,\overline{I_i}
+\frac16\,\overline{J_1}+\frac1{12}\,\overline{J_2},
\qquad a_i>0,
\]

where a bar denotes the average over the eight graph automorphisms. The 99 terms are named conditional mutual informations; all weights and arguments are in the certificate JSON. The graph FD rows in the identity have multipliers `-2/3,-4/3,-4/3` and vanish for the stated laws. No Ingleton nonnegativity is assumed for this exact identity.

Since all CMI terms are nonnegative, with `Delta=H(X_V)-(2/3)sum_v H(X_v)` one has the unrestricted graph-FD inequality

\[
2\overline{J_1}+\overline{J_2}\le -12\Delta.
\]

If `M=max_v H(X_v)` and `epsilon=H(X_V)-(20/3)M>0`, then `Delta>=epsilon`. Thus at least one of **these two** Ingleton instances, under **one of the eight** graph automorphisms, must be at most `-4 epsilon`. This replaces the 83-shape, weaker quantitative gate in the preceding packet. It is a necessary condition on a genuinely nonlinear strict-gain law, not a sufficient construction and not an unrestricted upper bound.

For representable rank functions, both Ingleton expressions are nonnegative by the subspace proof in the preceding packet. This certificate independently establishes `h(V)<=(2/3)sum_v h(v)` and hence the same exact finite-field vector-linear/affine optimum `20/3` attained by the explicit `q=8` code.

## A warning against bounding each defect too optimistically

A simple four-atom law on the original graph shows that a universal pointwise lower bound `J_1 >= -c M` with `c<7/69` is false, even before averaging. Put all vertices 5–10 constant zero. Let `(X_1,X_3)` have probabilities `(2,1,1,2)/6` on `00,01,10,11`, set `X_2=X_1 OR X_3`, and set `X_4=X_1 AND X_3`. These are exactly the four binary words `0,6,3,15` in vertex-bit order. All original-neighbour FDs hold: vertices 2 and 4 decode from 1 and 3, while either of 1 and 3 is determined by the other together with 2 and 4; the constant vertices decode trivially.

Both `X_1` and `X_3` are fair, so `M=1` bit. Given either `X_1` or `X_3`, one of `X_2,X_4` is constant; hence the two positive conditional mutual informations in `J_1` vanish. Direct entropy calculation gives

\[
J_1=3-2\log_2 3=\log_2(8/9)<-1/8<-7/69.
\]

The first strict inequality follows from the integer comparison `9^8=43046721 > 2^25=33554432`. If both defects were uniformly bounded below by `-c M` under every automorphism, the two-defect inequality would give `H(V)<=(20/3+c/4)M`; improving the inherited `1847/276=20/3+7/276` that way would require `c<7/69`, which this original-graph law rules out for the unaveraged `J_1`. The graph average and the joint combination may behave differently; this example does not rule out an improved bound exploiting them, and is not itself a strict-gain law.

## Evidence and scope

* LP proposal `frontier-20261028-defect-multiplier-lp.py` SHA-256 `4df96dcf80bbcca8291246f9af7dcc7e7e3a59a0a3e4d15b93a2c4ebb7b2fe0a`; float receipt SHA-256 `0653cb9625c0be1a168ba5461e54be8a6fb33e6eea82d394629f00997d1f073e`. It proposed the multiplier sum `1/4`; neither float objective nor asserted optimality is needed for the result.
* Exactifier `frontier-20261028-two-ingleton-exactify.py` SHA-256 `e1dfa6f3eea05caeb9f7e395675c34334d8e0310b4db7c9c395b61250744b4fb`; exact 104-row certificate `frontier-20261028-two-ingleton-exact-dual-v1.json` SHA-256 `b8d049baf687e6b38024c085369970c0b05fa46e4c1ba7517b9c2c7a652b5d9c`.
* Separate verifier `frontier-20261028-two-ingleton-independent-check.py` SHA-256 `bf0f7122772b7fc8cd978cf56a02474e64806f8cc2143956ff9ec2f52b9447b8`; receipt SHA-256 `3d1505ee4afeb3b992a2e03b6ba4a9787923eef2322390dd58617896c07722fd`. It reconstructs graph, automorphisms, 185 orbits and all 104 named rows; checks CMI/Ingleton signs, exact coefficients and both `(arguments,condition,weight)` entries; verifies the `q=8` lower code; and rejects five intended mutations.
* Four-atom witness checker `frontier-20261028-diamond-ingleton-witness.py` SHA-256 `1ce126b8ea8a9e8e6c122db43b7f2b66fc085510dab4555dba6e9406df553656`; receipt SHA-256 `cb8fcc169d2d0889e5787eced4df44616547e809256ab02e493292cb8cd6fca5`. It checks all 60 original-FD word/vertex conditions, exact atom counts and the integer comparison.

No formal proof, cross-model review or novelty clearance was performed. The exact rank bound and arbitrary-law conditional identity must not be promoted to an unrestricted `20/3` upper bound.
