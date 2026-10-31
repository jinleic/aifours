# A single varying triangle syndrome cannot yield an entropy gain

**Status: WRITTEN, exact FD/entropy tensorization; scientific review and novelty clearance pending.** In the fixed q=8 bit encoding of the standard ten-triangle factors, let an arbitrary original-neighbour R-minus FD law have triangle-syndrome support contained in

\[
\{s,\ s+e_t\}
\]

for any syndrome vector `s` and any single factor coordinate `t`. Then

\[
H(X_V)\le\frac23\sum_i H(X_i).
\]

Unlike the previous two-coset **cardinality** theorem, this rules out positive balance gap for **every distribution**, including arbitrary nonuniform weights and any FD-consistent support within those two adjacent syndrome classes. It does not cover two classes whose syndromes differ in more than one factor, or any larger syndrome support, and is not a global q=8 or unrestricted guessing-number proof. In particular it settles exactly, without a variational search, the one-outside-word reweighting attempt recorded in `frontier-20261028-triangle-one-word-reweight-result.json` SHA-256 `e55101d17e65b7c179f12c0722c98149c277074925c42814be5f1d99eb000b97`.

## Proof

Order the nine factors with fixed syndrome first and factor `t` last. Let `Z_r` be the three component bits in factor `r`, and let `Z_<r` be all prior factor bits. In each fixed-syndrome factor, any two bits determine the third, even after conditioning on the past, so

\[
H(Z_r\mid Z_{<r})\le\frac23\sum_{i\in T_r}H(X_i^r\mid Z_{<r}).
\]

For the last factor `t`, condition on **all nine other factor tuples**. Two support words with that same past which differ in only one of the three factor-`t` bits would differ in only one vertex symbol overall, while all of that vertex's original neighbours agree; this contradicts its FD. Hence, on every positive-probability conditional support, any two factor-`t` bits determine the third. The same entropy inequality therefore holds for factor `t`, even though its parity is not fixed.

Sum the ten inequalities. Because each vertex's previous factor components are functions of the full past,

\[
H(X_i^r\mid Z_{<r})\le H(X_i^r\mid X_i^{<r}).
\]

The chain rule turns the right side into `(2/3)sum_i H(X_i)` and the left side into `H(X_V)`. This proves the claim. No assumptions of independent factors or uniform probabilities are used. The fixed-factor tensorization and component encoding are pinned in `frontier-20261028-triangle-code-global-obstruction-v1.md` SHA-256 `bdf79fd631e8e58a734a4ef4c93f899e319f45712a219a876f527b52f1d61bb4`; the graph-FD support logic above is written mathematics, not a proof-assistant formalization or independent scientific review.
