# The triangle-code law is a strict local maximum of the balance gap

**Status: WRITTEN, elementary relative-entropy argument; scientific review and novelty clearance pending.** Let `P0` be the uniform law on the explicit ten-triangle binary R-minus code from `frontier-20261028-linear-ingleton-bound-v1.md` SHA-256 `e056dd9695a4b3e308431441b4f15ec3a2d81f3c733c604cff8246796abf3da4`. It has `2^20` support words, uniform 3-bit singleton marginals, pairwise independent singleton variables, and `Delta(P0)=0`.

For any law `P` on the **same support**, write `P(w)=P0(w)(1+f(w))`, where `E_0 f=0`. If `epsilon=||f||_infinity<1/5`, then with entropies in natural units,

\[
\boxed{\quad
\Delta(P)\le -\frac{1-5\epsilon}{6(1-\epsilon^2)}\,E_0[f^2]\le0.\quad}
\]

The inequality is strict unless `P=P0`. Thus no sufficiently small probability perturbation of the uniform ten-triangle code, while keeping its support fixed, can produce a strict R-minus gain. All such laws retain the original graph FDs. This does not rule out large perturbations, other supports, or the unrestricted guessing-number conjecture.

The same statement holds for any finite joint reference law `P0` that is uniform on its support, has uniform singleton marginals and pairwise-independent singleton variables, and has `Delta(P0)=0`; no linearity is needed for the local argument.

## Proof

Use natural logarithms and write `D` for relative entropy. Uniformity of the joint reference and all its singleton marginals gives the exact identity

\[
\Delta(P)=\Delta(P_0)-D(P\Vert P_0)+\frac23\sum_{i=1}^{10}D(P_i\Vert P_{0,i}).\tag{13}
\]

Put `g_i(X_i)=E_0[f|X_i]`. The singleton density relative to `P0_i` is `1+g_i`; also `E_0 g_i=0` and `||g_i||_infinity<=epsilon`. Because the singleton variables are pairwise independent under `P0`, the centered subspaces of functions of distinct `X_i` are mutually orthogonal in `L^2(P0)`. Conditional expectation is the orthogonal projection onto each such subspace, so Bessel's inequality gives

\[
\sum_i E_0[g_i^2]\le E_0[f^2].\tag{14}
\]

For `|x|<=epsilon`, the function `phi(x)=(1+x)log(1+x)-x` has `phi(0)=phi'(0)=0` and second derivative `1/(1+x)`. Integrating its elementary second-derivative bounds yields

\[
\frac{x^2}{2(1+\epsilon)}\le\phi(x)\le\frac{x^2}{2(1-\epsilon)}.
\]

As the linear terms have mean zero, applying the lower estimate to the joint relative entropy and the upper estimate to every singleton relative entropy, then using (14), gives

\[
\Delta(P)-\Delta(P_0)
\le -\frac{E_0f^2}{2(1+\epsilon)}
+\frac{2}{3}\frac{E_0f^2}{2(1-\epsilon)}
=-\frac{1-5\epsilon}{6(1-\epsilon^2)}E_0f^2.
\]

This proves the claim.

## Why the reference has the stated properties

Each listed triangle carries an independent uniform XOR-zero triple. Every vertex belongs to exactly three factors, giving a uniform 3-bit marginal. Within any one factor any two of the three bits are independent; different factors are independent. Therefore any two vertex vectors are independent. The ten factors contribute 20 joint bits, and the ten singleton entropies sum to 30 bits, so the balance gap is zero. Exact incidence and code evidence are pinned in `frontier-20261028-triangle-balance-matrix-result.json` SHA-256 `5bb5fc9254e205cf5f7b1cabb8373c1aebcfad546d7e49261441b8e5bd188796` and in the cited linear-rank packet.

This is a local, fixed-support obstruction, not formal proof, cross-model review, novelty clearance or an unconditional bound for other laws.
