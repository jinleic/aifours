# Addendum: the 46-support (4,4,4,4) profile has no quad-active P word

Owner **PhysicsAME46-2**. Native clock before writing: `Wed Oct 28 19:46:04 PDT 2026`; not an exact completion time. **WRITTEN author candidate**. This is an immutable additive extension, not an edit to `frontier-20261028-n46-4444-twoquad-exclusion-v1.md`, SHA-256 `be504a8b7e4b1afe359a44898af57a2814b5452236bc94d839f86ba2cc863773`; that packet's exact zero-fiber enumeration and all of its lower-bound prerequisites remain unreviewed.

## Claim

Under the same conditional N=46, t=26, residual-alphabet `(4,4,4,4)` hypotheses as the two-quad packet, **no** maximal P word can have all four coordinates active. The earlier packet handled n_4=2. Here the same checked zero-fiber obstruction also eliminates n_4=1. Thus the only remaining active-count profile in `(4,4,4,4)` is

`(n_0,n_1,n_2,n_3,n_4)=(0,2,18,6,0)`.                          (1)

No contradiction for (1), for the other alphabet profiles, or for N=46 globally is claimed.

## Proof

The P active and pair-active counts for `(4,4,4,4)` are 56 and 36, so `n_0+n_3+3n_4=6`. Exact nonnegative integer solving gives only

`(0,2,18,6,0)`, `(0,1,21,3,1)`, `(0,0,24,0,2)`.

The last case is the previously pinned two-quad candidate. Suppose the middle case, with exactly one quad and only one singleton-active P word. For an active symbol a at party i, let d_i(a) be its number of E partners at any other party. P pair injectivity makes this degree independent of the other party; residual fiber variation forces `d_i(a)≥2`, its partner alphabet gives `d_i(a)≤4`, and its four symbol degrees sum to 10. The degree multiset is therefore `(2,2,2,4)` or `(2,2,3,3)`.

Let s_i(a),q_i(a),h_i(a) count P words using a with respectively 1,3,4 active coordinates. Comparing the `6−d_i(a)` P words using a with the sum `3(4−d_i(a))` of their other-active incidences gives

`s_i(a)−q_i(a)−2h_i(a)=2d_i(a)−6`.                                 (2)

A degree-4 symbol would make the right side 2 and require at least two singleton-active P words using that symbol, but only one singleton exists globally. Thus every party has degree multiset `(2,2,3,3)`. If a symbol is used by the unique quad, h=1; if it had d=3, (2) would require `s=q+2≥2`, again impossible. Every quad symbol therefore has d=2.

Independently relabel the quad symbol at every party as 0, the other degree-2 symbol as 1, and the two degree-3 symbols as 2,3. The quad becomes 0000. Its maximal coefficient exhausts every pair row, so no E word has 0 in two coordinates. Since every residual pair value has exactly two E extensions, the local E symbol counts are exactly `[4,4,6,6]`. These are precisely the hypotheses of the zero-fiber enumeration in the two-quad packet; that enumeration deliberately forbids only repeated 0 and does **not** use a second quad 1111. Its two exact implementations find zero supports, so the one-quad case is excluded conditional on their normal-form and exhaustive-search review.

With both n_4=1 and n_4=2 excluded, only (1) remains. ∎

## Pinned inherited controls

The direct zero-fiber source SHA-256 is `8068b2c9f61430062b8279e5b575f093ddc56f7ba7cc425549a8de7a7f2b8c9f`, receipt SHA-256 `4612fd696383c1093e7222e3f5db14007859f930bf1104bb05d619781a0c1c59`. The independent balanced-column/meet-in-the-middle source SHA-256 is `67392e732f4149928c2be24dc6d184abfbb80d4c4301b687a21ceaccee888521`, receipt SHA-256 `f3e08a632783285201447b786777e2f14dc8f1da45b88397d94fca9489e5a567`. Their common orbit-representative input and independent whole-universe coverage check are described in the prior packet. These are same-harness exact checks, not independent scientific review or formal proof.
