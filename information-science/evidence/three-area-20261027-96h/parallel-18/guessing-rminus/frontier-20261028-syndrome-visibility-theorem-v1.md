# A syndrome-visibility theorem for arbitrary syndrome supports

**Status: WRITTEN with an independently checked exact 308-CMI certificate; scientific review pending.** Let each of the ten ordered triangles of the original R-minus graph carry an arbitrary nontrivial finite group `G_t` (abelian or not), give each vertex one component per incident triangle, and let `sigma=(sigma_1,...,sigma_10)` be the vector of ordered triangle products. Let `X` be **any** original-neighbour FD law in this encoding, with arbitrary syndrome support `Sigma`, probabilities and correlations.

**Theorem.** If for every vertex

\[
v\in W_0=\{1,2,5,6,7,8,9,10\}
\]

the syndromes of the three triangles through `v` determine the whole vector `sigma` on `Sigma`, then

\[
\boxed{\quad H(X_V)\le\frac23\sum_{v=1}^{10}H(X_v).\quad}\tag{62}
\]

More generally, it is enough that `H(sigma|X_{N(v)})=0` for every `v in W_0`. Nothing is assumed at vertices 3 and 4.

## Proof

Write `S=sigma`; it is a function of `X_V`. For `v in W_0` the original FD recovers `X_v` from `X_{N(v)}`; the other two vertices of each triangle through `v` are original neighbours, so each incident triangle product is a function of `X_{N(v)}`, and by hypothesis so is `S`. For every vertex, conditional on `S` and on the other components of its three triangles, each component of `X_v` is the unique group solution of its product equation: `H(X_v|X_{L(v)},S)=0`, where `L(v)` is the union of the other vertices of those triangles. This holds at vertices 3 and 4 although `L(3)` and `L(4)` omit the original edge `3--4`.

`frontier-20261028-visibility-universal-dual-v1.json` SHA-256 `8049f65fad8cb5f4a79a4c75ddafbe3eaa4f6d1b1b14f32797eb4eca70e2cbd4` is an exact rational identity, averaged over the four factor-preserving graph automorphisms, expressing `Delta` as a combination of 308 elemental CMIs with negative multipliers and of vanishing terms only: original graph FDs, the local component FDs above, `H(S|X_{N(v)})` for `v in W_0`, and `H(S|X_V)`. Hence `Delta<=0`. No syndrome cardinality, entropy cap, conditional factor gate, two-syndrome theorem or lifting is used.

The independent checker `frontier-20261028-visibility-universal-dual-check.py` SHA-256 `897f5bff737c384ab43ce3d239480e3071dc0a4c8574e393edd67552e44e15df`, receipt SHA-256 `ba80c4206d53ef0f77a871c345d41fe23563e1beb5b87848175092fc5d1dfb68`, pushes every row through all four automorphisms, re-checks on each image that visibility is invoked only at vertices of `W_0`, checks all CMI signs, and verifies the averaged identity on all 2,047 raw entropy coordinates with exact `Fraction` arithmetic. It rejects a changed target, dropping visibility at vertex 7, and a flipped CMI sign.

## Corollaries

1. **Two syndrome values, independent proof route.** For `Sigma={s,t}` and `J={r:s_r!=t_r}`, vertex `v` sees `sigma` iff some triangle through `v` lies in `J`. If `J` covers all vertices the hypothesis holds, so `Delta<=0` follows **directly**, without the gap-preserving lift used in `frontier-20261028-two-syndrome-repaired-theorem-v1.md` SHA-256 `9feb6cd50a2b376b971c2091369b5c5ad7d50e18446ce4cd3293bfc718b776b1`. With the pinned noncover gate, this gives a second, independent proof of the two-syndrome theorem for arbitrary finite group factors (one value is trivial).
2. **Binary planes.** For a q=8 syndrome support inside an affine two-plane with direction space `D`, vertex `v` sees `sigma` iff every nonzero `d in D` is nonzero on some triangle through `v`. By exact enumeration in the owner's kernel, 13,338 of the 153,258 covering direction planes satisfy the hypothesis at all of `W_0` (180, 2,558, 6,672 and 3,928 with seven, eight, nine and ten varying factors).
3. Any strict-gain law in this encoding therefore has, for some vertex `v in W_0`, triangle syndromes at `v` that fail to determine `sigma`.

These are support-class statements; they do not bound strategies with unrestricted syndrome supports or improve the numerical guessing-number bound. Formal proof, independent scientific review and novelty clearance are not claimed.
