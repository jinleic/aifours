# Exact normalization of all three-state q=8 syndrome supports

**Status: WRITTEN elementary finite geometry; scientific review pending.** Every three-element subset of the binary ten-factor syndrome space `F_2^10` is an affine translate of `{0,u,v}` for independent nonzero vectors `u,v`. Two such triples are translates of one another exactly when they lie in parallel affine planes with the same two-dimensional direction subspace. Indeed, every triple is the complement of its unique fourth point in a two-dimensional affine plane, and translation acts transitively on the four possible missing points and on plane cosets.

Thus the total `C(1024,3)=178,433,024` three-element syndrome subsets reduce, under independent fixed flips of the ten factor parities, to exactly

\[
\binom{10}{2}_2=\frac{(2^{10}-1)(2^{10}-2)}{(2^2-1)(2^2-2)}=174,251
\]

direction-subspace classes. Each direction plane has 256 affine translates and four triples per translate. Any desired syndrome translation is achieved by flipping one component bit in each selected triangle factor; that is a bijection of the vertex alphabets and preserves entropies and original-neighbour FDs.

The previously certified bipartition theorem covers only **one** such direction subspace (and its translates); the three further factor-color partitions yield three more specified subspaces. Their joint four-case result plus the equivariant-color census is therefore a strictly limited subset of 174,251, not a solution of all three-syndrome supports. The finite geometry is elementary, not a formal proof or novelty claim, and does not import the disputed two-syndrome result.
