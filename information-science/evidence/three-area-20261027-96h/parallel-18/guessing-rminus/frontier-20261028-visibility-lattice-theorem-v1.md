# The complete syndrome-visibility lattice for R-minus

**Status: WRITTEN with exact independently checked certificates for both directions; scientific review pending.** This strengthens `frontier-20261028-syndrome-visibility-theorem-v1.md` SHA-256 `df15ed135a477bb97dcbae58985baca2e95fc72e72d3a8d0a993bf94b5932f14` from eight visible vertices to the exact minimal sets.

## Setting

Use the ten ordered triangles of R-minus with arbitrary nontrivial finite groups `G_t`, one component per incident triangle at each vertex, and the full product-syndrome vector `sigma`. For an original-neighbour FD law `X`, let

\[
W(X)=\{v:\ H(\sigma\mid X_{N(v)})=0\}.
\]

For a support `Sigma` of `sigma`, `W(X)` contains every `v` whose three incident triangle syndromes determine `sigma` on `Sigma`: the graph FD recovers `X_v`, and the other vertices of its triangles are original neighbours. All laws satisfy `H(sigma|X_V)=0` and the local component FDs `H(X_v|X_{L(v)},sigma)=0` (group inverses), including at vertices 3 and 4.

## Theorem A: sufficiency

If `W(X)` contains one of the eight sets

\[
\{6\},\ \{7\},\ \{2,5\},\ \{9,10\},\ \{1,2,10\},\ \{1,5,9\},\ \{5,8,9\},\ \{2,8,10\},\tag{63}
\]

then `Delta(X)<=0`. These are three orbits under the four factor-preserving graph automorphisms. Exact rational identities for the representatives `{6}`, `{2,5}` and `{1,2,10}`, respectively `frontier-20261028-visibility-6-dual-v1.json` SHA-256 `0e4a6ff065e9bc3dbc5f07ec6878f60ca9fecb42ea94ccc74cf3ac8499c0a9ee` (155 CMIs), `frontier-20261028-visibility-25-dual-v1.json` SHA-256 `124d2b19a85cc36619728025185349215e6025e855d40c792e420fa5019ed164` (71 CMIs), and `frontier-20261028-visibility-12T-dual-v1.json` SHA-256 `89636ce3816400cdf8081c459eb4dc944fde8063b4bf2b1c3dc05aa722c5d8eb` (93 CMIs), express `Delta` as negative multiples of elemental CMIs plus graph FDs, local component FDs, `H(sigma|X_V)` and `H(sigma|X_{N(v)})` only for `v` in the stated set. The independent checker `frontier-20261028-visibility-general-dual-check.py` SHA-256 `e9b14a0cf76c98aaa9166ad96363623f57a0c5cd29c1b81dffddff633c586c2c`, receipt SHA-256 `59c9c593957b2343cc10920d744186493f4bb576514db20f8519e50dc5129667`, pushes rows through the listed stabilizer subgroup, re-checks each visibility use and all 2,047 raw coefficients exactly, and rejects altered targets and dropped visibility.

In particular: **if the three triangle syndromes at vertex 6 (factors `167,569,678`) determine the whole syndrome on the support, every FD law has `Delta<=0`.** The two-syndrome theorem for covering difference sets is an immediate special case, independent of the earlier lift.

## Theorem B: these rows prove nothing more

If `W` contains none of (63), then `W` is contained in one of

\[
\{1,2,3,4,8,9\},\ \{1,3,4,5,8,10\},\ \{2,3,4,10\},\ \{3,4,5,9\}.\tag{64}
\]

For the representatives `{1,2,3,4,8,9}` and `{3,4,5,9}`, `frontier-20261028-visibility-bad-polymatroids-v1.json` SHA-256 `a96790f70a505b6619254729d97340dbb6c8feaddf82b6b88b76d6e442751932` gives explicit rational polymatroids on `(X_1,...,X_10,sigma)` with `Delta=20/117` and `10/63`, satisfying all 28,160 elemental CMIs and all monotonicity rows, every graph FD and local component FD, `H(sigma|X_V)=0`, and visibility at every vertex of the set; checker `frontier-20261028-visibility-bad-polymatroid-check.py` SHA-256 `bc1725d5f79deb4c2e92eb1cbfcbd1e6728b20742b05f0c181eb1d2117908b25`, receipt SHA-256 `67dbfe681f285ac4b63ee0306927a80f51eb0790679a2682b8c4de0cb835adb2`. Hence no Shannon combination of these row types proves `Delta<=0` for such `W`. These polymatroids are not shown entropic and are **not** guessing strategies.

`frontier-20261028-visibility-dichotomy-check.py` SHA-256 `3ad3da2bbf3c24e2c6015192a3786eedab775821ce0daf422209db1cf7f9ba83`, receipt SHA-256 `4432727c59ccf2e268929f6cdd7547b15a033e3c0a3c34bc867ec7ed7aabe966`, verifies from the two pinned receipts that all 1,024 subsets split with no overlap: 904 contain a generator and 120 lie in a set of (64).

## Consequence for binary syndrome planes

Of all 174,251 binary syndrome direction planes: 20,993 have noncovering varying factors (noncover gate), 145,329 cover and have visibility containing a generator (Theorem A), and 7,929 cover with visibility in (64). Of these 7,929, 166 have four varying factors and are settled by `frontier-20261028-fourfactor-plane-complete-theorem-v1.md` SHA-256 `7148eb8fa7ef068743d927454c779290b0f3b4238940c7f4226b50bcb707cde5`. Thus, subject to review of all imports, `Delta<=0` holds for every original FD law supported in any affine translate of `174,251-7,763=166,488` direction planes; the remaining 7,763 have five to ten varying factors. A binary support with more than eight syndrome values cannot satisfy the incident-triangle-syndrome sufficient condition at any vertex; for such laws Theorem A applies only through the general entropy hypothesis `H(sigma|X_{N(v)})=0`, which is not established. No unrestricted guessing-number bound, strict-gain witness, formal proof or novelty claim is made.
