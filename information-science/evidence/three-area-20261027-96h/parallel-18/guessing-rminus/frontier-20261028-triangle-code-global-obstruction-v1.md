# Every distribution on the ten-triangle code has nonpositive balance gap

**Status: WRITTEN, exact Shannon/chain-rule proof; scientific review and novelty clearance pending.** The local result `frontier-20261028-triangle-code-local-rigidity-v1.md` SHA-256 `9e30eebd81f30469f288872cd93320e3e3dcbd351405675c8773026340db3de2` admits a stronger **global fixed-support** conclusion: every probability law, uniform or not and with arbitrary correlations, supported on the explicit ten-triangle XOR code has

\[
H(X_V)\le\frac23\sum_{i=1}^{10}H(X_i).
\]

This includes laws supported on any subset of the `2^20` codewords. Therefore changing probabilities alone can never turn the standard triangle-code support into an R-minus strict-gain witness. This does **not** rule out a different support, a different original-neighbour strategy, or an unrestricted guessing-number improvement.

## A general product-support lemma

Let a support be a Cartesian product of finitely many factor supports. Each factor `t` has one component `X_i^t` at each vertex, possibly constant. Suppose that **every** law supported on factor `t` satisfies `H(Z_t)<=(2/3)sum_i H(X_i^t)`, where `Z_t` is the factor's entire tuple. Let the full vertex variable be `X_i=(X_i^1,...,X_i^T)`. Then every joint law on the product support, even one correlating the factors, obeys `H(X_V)<=(2/3)sum_i H(X_i)`.

Order the factors arbitrarily and put `Z_{<t}=(Z_1,...,Z_{t-1})`. For each value of `Z_{<t}`, the conditional distribution of `Z_t` is a law on factor `t`, so averaging the factor inequality gives

\[
H(Z_t\mid Z_{<t})\le\frac23\sum_i H(X_i^t\mid Z_{<t}).
\]

Since `X_i^{<t}` is a function of `Z_{<t}`, conditioning can only decrease entropy:
`H(X_i^t|Z_{<t})<=H(X_i^t|X_i^{<t})`. Sum over factors and use the chain rule on the joint tuple and on each `X_i` to obtain the global bound. The factor distributions need not be independent.

## Applying it to triangle XOR factors

Each triangle factor is an XOR-zero triple of bits, with all other vertex components constant. Any two of its bits determine the third, so for **any** law on that factor the three pairwise subadditivity inequalities give `3H(Z_t)<=2 sum_{i in T_t} H(X_i^t)`. The general lemma applies to the ten independent-coordinate factors of the standard triangle-code support. Independence here describes the **Cartesian product support**, not an assumption on the law `P` being bounded.

More explicitly, for any law on that support the following exact decomposition holds:

\[
\begin{aligned}
3\left(\frac23\sum_i H(X_i)-H(X_V)\right)
={}&\sum_t\sum_{\{i,j\}\subset T_t}
 I(X_i^t;X_j^t\mid Z_{<t})\\
&+2\sum_t\sum_{i\in T_t}
 I(X_i^t;Z_{<t}\mid X_i^{<t}).
\end{aligned}\tag{15}
\]

For each triangle and past value, any two bits determine `Z_t`, so the first sum equals `2 sum_{i in T_t}H(X_i^t|Z_{<t})-3H(Z_t|Z_{<t})`. The second sum is exactly the difference between conditioning each bit on its own previous components and on all previous factors. Every term is nonnegative. Equality holds if and only if every CMI on the right of (15) is zero for the chosen factor order.

The explicit triangle list, original-neighbour decoding and `2^20`-word construction are pinned in `frontier-20261028-linear-ingleton-bound-v1.md` SHA-256 `e056dd9695a4b3e308431441b4f15ec3a2d81f3c733c604cff8246796abf3da4`; exact triangle incidence evidence is SHA-256 `5bb5fc9254e205cf5f7b1cabb8373c1aebcfad546d7e49261441b8e5bd188796`. This written global lemma is stronger than the local Taylor/KL bound but neither requires nor establishes a general nonlinear graph bound, formal proof, independent scientific review or novelty clearance.
