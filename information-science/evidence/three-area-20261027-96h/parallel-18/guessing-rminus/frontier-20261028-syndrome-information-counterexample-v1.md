# Mixed-syndrome entropy identity and a false shortcut

**Status: WRITTEN with exact integer checking.** This is an obstruction to one proposed route, not an improvement or a global upper bound for R-minus.

Use the triangle-coordinate cover from `frontier-20261028-triangle-entropy-no-gain-v1.md` (SHA-256 `9dece7da2d6297a1965e5e48e2075e8319b2b626cf652d5996a1f7a4506de480`). For an arbitrary joint law on its 30 binary component bits, let `S` be the ten triangle parity bits. Conditional on `S`, every triangle has a fixed sum and the preceding fixed-coset entropy identity applies. Because `S` is determined by the full word,

\[
2\sum_v H(X_v)-3H(X_V)
=G_{\mid S}+2\sum_v I(X_v;S)-3H(S),
\]

where `G_|S` is the preceding sum of conditional mutual informations with `S` added to every conditioning set, and is nonnegative. Thus a possible route to a global `20/3` upper bound would be to control the last two syndrome terms in the presence of the original FDs. **The tempting separate inequality `2 sum_v I(X_v;S) >= 3 H(S)` is false, even for an actual original-neighbour FD law.** Its failure does not by itself establish that the full entropy gap on the left is negative: `G_|S` remains present.

## Exact counterexample

Take the uniform law on the previously pinned 88-word binary original-R-minus winning support `frontier-20261028-fd-law-search-precise-result.json` (SHA-256 `c82613f4fb2ae9f70192eedf73c5cc755de332e3be4d8cb0ddedc20899586bfc`). At each vertex embed its bit as the first component of the triangle-coordinate `q=8` symbol and set the other two components to zero. An original-neighbour binary decoder lifts to a full-domain `q=8` decoder by reading neighbours' first components, applying the binary decoder, and outputting `(bit,0,0)`; unseen binary observations can be completed arbitrarily.

The exact comparison is

\[
3H(S)>2\sum_{v=1}^{10}I(X_v;S).
\]

The checker verifies all `38,280` vertex/pair FD conditions and uses only integer counts. For `n=88`, let `n_s`, `n_{v,b}` and `n_{v,b,s}` be the counts of each syndrome, vertex bit, and their pair. Writing `P(C)=product_c n_c^{n_c}`, the claimed strict inequality is exactly

\[
P(S)^{17}\prod_v P(X_v)^2
>88^{17\cdot88}\prod_v P(X_v,S)^2.
\]

The left and right integers have respectively 12,200 and 11,800 bits; the comparison is exact. The individual 28 syndrome frequencies and the result are in `frontier-20261028-syndrome-information-counterexample-result.json`, SHA-256 `7cac60b5a86c65cb7ebfd761e48c170d50fc3c2cb66a8331f7f0299198a82407`. The checker `frontier-20261028-syndrome-information-counterexample.py` has SHA-256 `d8397714a48ed65e7e7ceec0de16b700af2e5090ce7aa7635bc57b433c42a92b`.

The law is not claimed to beat `20/3`. No independent cross-model review, formal proof or novelty clearance was performed.
