# Six fixed-syndrome hyperplanes cannot beat the q=8 code

**Status: WRITTEN with exact graph/factor-incidence checks; scientific review pending.** Fix the component encoding and ordered ten triangle factors of the standard q=8 R-minus code `W0`. For each of the factor indices

\[
\{1,2,3,6,8,10\},
\]

any original-FD-consistent q=8 support on which that factor's XOR syndrome is constant has at most `2^20` words. Therefore any q=8 fixed-point set strictly larger than the standard `2^20`-word code must realize **both** syndrome values for every one of these six factors. This can cover up to 512 syndrome classes per hyperplane and complements the separate three-coset bound; it is not a nonuniform entropy-gap exclusion or unrestricted guessing-number bound.

## Clique-factor proof

The six checked independent triples `I` of graph vertices meet the ten chosen factor triangles in exactly nine distinct factors; the factor missed by each triple is:

| Independent vertices `I` | Missed factor, one-based |
|---|---:|
| `1,9,10` | 10 |
| `2,4,6` | 6 |
| `2,5,8` | 3 |
| `3,5,7` | 8 |
| `3,6,10` | 2 |
| `4,7,9` | 1 |

For such an `I`, let `L_I` be the 9-dimensional subspace of all q=8 ambient words supported only on those three vertices. Any two distinct words in `L_I` are confusable: their difference support is a nonempty subset of an independent vertex set. Thus `L_I` is a 512-word clique.

The syndrome map takes `L_I` bijectively onto the 9-dimensional syndrome hyperplane where the missed factor bit is zero: each of the nine occurring factor bits belongs to exactly one vertex of `I`. In particular `L_I intersect W0={0}`. Hence `W0` translates of `L_I` are pairwise disjoint and partition the full `2^29`-word syndrome hyperplane. A translate by any word of opposite missed-factor syndrome gives the same partition for the other hyperplane. Each partition has `2^20` cliques, so an FD-consistent support in either hyperplane has at most `2^20` words.

## Exact evidence

`frontier-20261028-syndrome-hyperplane-check.py` SHA-256 `a051b8d9e01f10138bc19117d8ba60b132e7f37df0947556e14230155579c595`, receipt SHA-256 `ddc3c58d179f9602fa9284ca87efbf3bb14ce1a9193c47c4645638064b949a57`, independently enumerates the six graph-independent triples, verifies the disjoint nine-factor incidences and missed indices, and rejects a non-independent triangle control. Clique tiling and its implication are written arguments; no proof-assistant formalization, scientific review or novelty claim is made.
