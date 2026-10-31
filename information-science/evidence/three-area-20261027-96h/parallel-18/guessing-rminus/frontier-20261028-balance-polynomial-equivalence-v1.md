# A finite integer-polynomial witness for strict guessing gain

**Status: WRITTEN exact reduction.** This is not a strict-gain witness or an unrestricted upper bound. It builds on the balancing/type-class equivalence `frontier-20261028-entropy-balance-equivalence-v1.md` (SHA-256 `4013d40004f9e6576973517b5a36e634e294f6713f75ff44273d4266d920090e`). No formal proof, cross-model review or novelty clearance has been performed.

## Exact finite criterion

The original R-minus guessing number is strictly greater than `20/3` **if and only if** there exist:

* a finite alphabet `[q]` and a finite set `W` of ten-symbol words for which every two words that differ at a vertex also differ at some original neighbour of that vertex; and
* nonnegative integers `t[v,a]`, not all zero in any vertex row, such that

\[
\left(\sum_{w\in W}\prod_{v=1}^{10}t[v,w_v]^2\right)^3
>\prod_{v=1}^{10}\left(\sum_{a=1}^{q}t[v,a]^3\right)^2.
\tag{*}
\]

The pair condition is exactly the consistency condition for full-domain neighbour decoders: a decoder uses a lookup table on observed neighbour tuples and an arbitrary fixed output on tuples absent from `W`.

For `q=2`, write the two row entries as `u_v,t_v`. The condition is a weighted independent-set witness in the original 1,024-vertex binary confusability graph:

\[
\left(\sum_{w\in W}\prod_{v:w_v=0}u_v^2\prod_{v:w_v=1}t_v^2\right)^3
>\prod_v(u_v^3+t_v^3)^2.
\]

Setting all `u_v=t_v=1` reduces this to `|W|^3>2^20`; nonuniform integer weights permit other supports. A failure for a selected `q`, `W` or integer range is not a general impossibility result.

## Proof

For a fixed FD support `W`, let `P` range over probability laws on it and let `Q_v` be arbitrary probability laws on the vertex alphabets. Entropies below use natural logarithms. The Gibbs/KL variational identities imply

\[
\max_P\!\left(H(P)-\tfrac23\sum_v H(P_v)\right)
=\max_{Q_1,\dots,Q_{10}}
\log\!\left(\sum_{w\in W}\prod_v Q_v(w_v)^{2/3}\right).
\tag{1}
\]

Indeed, for each `P`, `-H(P_v)=max_{Q_v} E_P log Q_v(X_v)`; for fixed `Q`, maximizing `H(P)+E_P log product_v Q_v(X_v)^(2/3)` gives the logarithm of its normalizing sum. Zero probabilities use the usual limiting convention. Both maximizations can be interchanged on the finite compact probability simplices.

Given integers satisfying `(*)`, set

\[
Q_v(a)=\frac{t[v,a]^3}{\sum_b t[v,b]^3}.
\]

The quantity inside the logarithm in `(1)` is then strictly greater than one. Explicitly, the FD law

\[
P(w)=\frac{\prod_v t[v,w_v]^2}{\sum_{x\in W}\prod_v t[v,x_v]^2}
\]

has a strictly positive entropy-balance gap: its entropy gap is at least the positive logarithm in `(1)`. Its probabilities are rational. The triangle-balancing and type-class construction in the predecessor converts this law into a finite alphabet and total original-neighbour decoders with a strict gain.

Conversely, if the unrestricted guessing number is greater than `20/3`, the predecessor gives a finite FD law `P` with positive balance gap. Taking `Q_v=P_v` makes the quantity inside the logarithm in `(1)` greater than one. Approximate the finitely many cube roots `P_v(a)^(1/3)` by nonnegative rationals; the strict inequality survives by continuity. Clear denominators separately for each vertex to obtain nonnegative integer `t[v,a]` and `(*)`. This proves the equivalence.

This reduction replaces a continuous entropy witness by an integer comparison and exposes a joint **support plus weight** search. Neither the existence nor nonexistence of a witness has been established here.
