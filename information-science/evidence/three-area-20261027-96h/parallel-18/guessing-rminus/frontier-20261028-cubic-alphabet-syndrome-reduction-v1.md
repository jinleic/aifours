# The unrestricted strict-gain problem reduces to three-syndrome cubic alphabets

**Status: WRITTEN; scientific review pending.** The original strict guessing-number question is equivalent to the existence of a finite cyclic-group factor support with at least three syndrome values:

\[
\operatorname{gn}(R^-)>20/3
\quad\Longleftrightarrow\quad
\exists m\ge2,\ W\subset(\mathbb Z/m\mathbb Z)^{30}:
\begin{cases}
W\text{ is original-neighbour FD-consistent},\\
|W|>m^{20},\\
|\{\text{ten-triangle syndrome vectors of }w:w\in W\}|\ge3.
\end{cases}\tag{32}
\]

The 30 coordinates are grouped into three triangle components per vertex as in the pinned group-factor construction. The `>=3` clause follows from the two-syndrome group theorem `frontier-20261028-two-syndrome-group-alphabet-bound-v1.md` SHA-256 `06c2f1c7f9cf9c06b0dc1d90cfbcb265d719837c209d70ed46f6773fd01be204`, which is subject to scientific review and imports the pinned proper-subgraph inequality. This equivalence does not prove that such a support exists or rule out all such supports.

## Proof

The reverse direction is immediate: each vertex alphabet has size `q=m^3`, the FD support defines total original-neighbour decoders, and `|W|>m^20=q^(20/3)` gives a strict fixed-alphabet gain.

For the forward direction, by the definition of guessing number there is a finite alphabet of size `q>=2` and an FD-consistent support `W_0` with `|W_0|>q^(20/3)`. For every positive integer `n`, the Cartesian product `W_0^n` is FD-consistent on a `q^n`-symbol alphabet, using coordinatewise decoders. Let `m_n=ceil(q^(n/3))` and inject the `q^n` symbols into `m_n^3` symbols; extend every decoder arbitrarily on unobserved neighbour tuples. The embedded product remains an FD-consistent support of size `|W_0|^n`.

Writing `r=|W_0|/q^(20/3)>1`, for all sufficiently large `n`,

\[
\frac{|W_0|^n}{m_n^{20}}
\ge\frac{r^n}{(1+q^{-n/3})^{20}}>1.
\]

Choose any bijections between each `m_n^3`-symbol vertex alphabet and three cyclic-group coordinates, one per incident triangle. By the two-syndrome group theorem, the resulting strict support cannot have one or two syndrome vectors, proving (32). The same conclusion holds for any choice of nontrivial groups of order `m_n` assigned to the factors and any such vertex relabelings. No new strategy is claimed here; this is a quantifier-complete reduction of the original target, with written amplification and the cited theorem as its load-bearing input.
