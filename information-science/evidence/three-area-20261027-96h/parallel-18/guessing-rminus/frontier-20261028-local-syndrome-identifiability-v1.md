# Syndrome identifiability on the certificate's four vertex orbits

**Status: WRITTEN, conditional on the exact compact certificate and the actual group-factor decoder; scientific review pending.** The full-syndrome inequality (42) in `frontier-20261028-compact-full-syndrome-inequality-v1-addendum-1.md` SHA-256 `2f7a18d11fde89e9c94bf57ee376967f0f8294b1b6660699d6be2c4cc25eeed6` yields the following universal criterion.

Let `X` be any original-neighbour FD law on finite group triangle-factor components, and `S` the complete ten-factor syndrome vector. If `S` is determined by the syndrome of each one of the four triangles `123,145,389,4·8·10`, then `Delta<=0`. There is no restriction on the number of possible values of `S`, its probabilities, or the finite groups. This is a conditional support-class theorem, not a general upper bound for arbitrary original strategies.

## Proof

For a vertex `v`, its own block is a function of the original-neighbour tuple. Each factor syndrome incident to `v` is therefore a function of `X_{N(v)}`: the neighbour tuple directly supplies the other two factor components and supplies `X_v` through its graph FD. Every vertex in `{2,5,6,7,9,10}` belongs to at least one of the four certificate triangles `123,145,389,4·8·10`. Thus the original-neighbour tuple determines that triangle's product, and the premise implies `S` is a function of `X_{N(v)}`. The first two families of conditional entropies on the right of (42) vanish.

For each of the four listed triangles `T`, its factor syndrome is directly computable from `X_T`; by premise it determines `S`. Hence each triangle conditional entropy in (42) vanishes as well. The more general sufficient hypothesis for this criterion is

\[
H(S|X_{N(v)})=0\ (v=2,5,6,7,9,10),\quad
H(S|X_T)=0\ (T=123,145,389,4\,8\,10).
\]

Under these ten equalities the right side of (42) is zero and `Delta<=0`. The stated per-triangle-syndrome premise is sufficient, not claimed necessary. No binary-state assumption is used, and this note does not assert the ten conditions hold generally.
