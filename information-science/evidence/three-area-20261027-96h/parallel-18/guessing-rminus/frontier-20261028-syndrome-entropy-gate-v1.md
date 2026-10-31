# An entropy inequality for the triangle-syndrome variable

**Status: WRITTEN, exact conditional product-support argument; scientific review pending.** Fix the q=8 triangle-factor bit encoding, and for **any** joint law on the ten 3-bit vertex variables let `S` be the 10-bit vector of triangle XOR syndromes. With `Delta=H(X_V)-(2/3)sum_i H(X_i)`,

\[
\boxed{\quad 3\Delta+2\sum_i I(X_i;S)\le3H(S).\quad}\tag{19}
\]

No graph FD, uniformity or code-support assumption is needed for this inequality. In particular any q=8 original-FD strict-gap law must have a nonconstant syndrome and satisfy `sum_i I(X_i;S)<(3/2)H(S)`. If `S` is constant, (19) recovers the global product-support obstruction for **every** syndrome coset, not just the zero-syndrome code. This is an entropy restriction, not a numerical q=8 or unrestricted guessing-number upper bound.

## Proof and exact decomposition

Condition on `S=s`. Each triangle factor then has a fixed affine XOR parity, so any two of its three bits determine the third. The ten conditioned factor supports form a Cartesian product; the tensorization proof in `frontier-20261028-triangle-code-global-obstruction-v1.md` SHA-256 `bdf79fd631e8e58a734a4ef4c93f899e319f45712a219a876f527b52f1d61bb4` applies after conditioning:

\[
H(X_V\mid S)\le\frac23\sum_i H(X_i\mid S).
\]

Because `S` is a deterministic function of the full tuple, `H(X_V)=H(S)+H(X_V|S)`. Also `H(X_i)=H(X_i|S)+I(X_i;S)`. Substitution and rearrangement yield (19).

More precisely, for any order of factors and `Z_{<t}` the tuple of previous factor bits,

\[
\begin{aligned}
3H(S)-2\sum_i I(X_i;S)-3\Delta
={}&\sum_t\sum_{\{i,j\}\subset T_t}I(X_i^t;X_j^t\mid S,Z_{<t})\\
&+2\sum_t\sum_{i\in T_t}I(X_i^t;Z_{<t}\mid S,X_i^{<t}).
\end{aligned}\tag{20}
\]

The first term is the triangle pairwise-independence deficit under the fixed affine parity; the second is the cross-factor conditioning deficit. Both are nonnegative. This also shows exactly when (19) is tight for a given factor order.

`frontier-20261028-syndrome-entropy-identity-check.py` SHA-256 `9fc1ff07dfc7e910ebf5ae034d6f08929d82edb784c163c7c7ad1b5c7bbaacdb`, receipt SHA-256 `0eaf39ecc67afb491d03fb02974e83fe0b55705257b6269467caf9061e4cebd3`, checks (20) symbolically on 30 formal component bits plus one syndrome tuple: its residual is exactly the 30 conditional affine-XOR FD rows minus three copies of `H(S|X_V)`, all zero under the syndrome definition. It checks 109 entropy coordinates and rejects three intended coefficient mutations.

The result is an additive successor to the fixed-support theorem and its symbolic identity check; it does not imply that the syndrome-information lower bound needed to prove `Delta<=0` holds. No formal proof, independent scientific review or novelty claim is made.
