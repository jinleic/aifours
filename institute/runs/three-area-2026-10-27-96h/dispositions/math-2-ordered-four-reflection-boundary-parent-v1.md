# Ordered four-term lemma and the odd-run reflection boundary

**Disposition: ACCEPT at the stated written-mathematics scope, with a separately conditional p=7 consequence.** Native clock read immediately before composing: **2026-10-28T19:34:37-0700 PDT**. This is a same-harness parent disposition, not a human, independent-model-family, formal/kernel, priority or novelty certification. It does not solve the original ordered-Olson problem or authenticate the complete historical residual interface.

## Accepted statements

1. For every odd prime `p`, every length-`p+2` sequence over `F_p` with unequal adjacent entries has four increasing positions `i<j<k<l` such that `x_i−x_j+x_k−x_l=0`.
2. For an actual original-order dihedral word with `F=3p−2` reflections, `o_F=p+2` odd constant-reflection runs and at most one even run, there is a product-one subsequence of exactly `2p` reflections. The subsequence is selected from the actual word in original order, not from an unordered multiset.
3. Under the candidate's actual raw-graph hypothesis `ν_M≤p−3` and reflection-selector failure, put `H=(F−o_F)/2` and `κ=p−1−H`. Then `κ≥0` and `2κ+e_F≤p−6`. Together with statement 2, the `κ=1` failure case requires `e_F≥2`, hence `p≥11`.

**Conditional only:** if the separately inherited lower-residual floor `o_F≥p+2` and the listed actual-word, reflection-failure and raw-matching hypotheses apply, the resulting lower residual class is empty at `p=7`. The floor and its historical `S(p)`/Lev ancestry were not reconstructed or authenticated in this review; without the floor, the derived inequality alone leaves necessary profiles `κ=0`, `e_F∈{0,1}`. No existence claim follows. The full `L_RES`, other selectors and other count bands remain open here.

## Independent reconstruction

If a zero-free adjacent-distinct sequence has full field support, the value `u−v+w` associated with each consecutive triple must occur inside that triple; adjacent inequality forces it to be the middle value. Thus all steps are the same nonzero `d`, and positions `1,2,3,p+2` give alternating sum `−pd=0`. If a value appears four times, or one value appears three times and another twice, a zero quadruple is immediate; the remaining triple-plus-singleton case has full support.

Otherwise all multiplicities are at most two. If `s` values are doubled, exactly `s−2` values are missing. Two doubled intervals that are disjoint or nested give a zero quadruple, so a zero-free sequence requires all doubled intervals to cross. For any ordered pair of distinct doubled values `(a,b)`, the value `2a−b` is distinct from both and cannot occur anywhere: in each crossing orientation and each insertion region, the review gives four increasing positions with alternating sum zero. Fixing `a` produces `s−1` distinct missing values, contradicting the `s−2` available values.

For statement 2, the `p+2` odd runs yield `H=p−2` disjoint equal-reflection pairs. Adjacent odd runs with the same label need an intervening even run; at most one such bad cyclic adjacency exists and can be cut. The four-term lemma supplies four representatives from distinct odd runs. Select them and all `H` pairs, giving `2p` actual reflections with product one. Returning from the cut to the original word rotates the selected product cyclically, and a cyclic rotation of a product equal to one remains one.

For statement 3, the raw graph is a proper subgraph of the reflection cycle; its components are paths. If `q` edges are absent and `o_M` components have odd size, `q≥o_M=F−2ν_M≥p+4`. Reflection failure excludes the all-equal label list, and absent edges occur only among the `F−(o_F+e_F)` equal-neighbor edges. Hence `o_F+e_F≤2p−6`. Reflection failure also forces `H≤p−1`, since `p` disjoint equal pairs alone give an original-order identity selector. Substituting `o_F=p+2κ` yields the bound.

## Evidence and limits

- [Frozen candidate](../../../../mathematics/evidence/three-area-20261027-96h/parallel-18/ordered-olson/frontier-20261028-olson-ordered-four-odd-boundary-v1.md): SHA-256 `7d4d356430303b1538cd1e621d0943ba9096be98fe3f53cce3184c7783a33fb5`; 98 LF, read in full.
- [Frozen manifest](../review-waves/f111-olson-ordered-four-odd-boundary/manifest-v1.json): `8579d24dc6e6a5ed1b7601aa6b28e92eb1dae5998af5a79fa5797f744513227d`.
- [Independent same-harness review](../review-waves/f111-olson-ordered-four-odd-boundary/review-v1.md): `b56f8ca26b26f651491e576d86475fb9b6b75f8a54facd71b47ce77f2ae735e2`; 79 LF, read in full. It reports **0 FATAL / 0 MAJOR / 0 MINOR** for the universal and conditional implications, with the historical floor explicitly unverified. Its own controls exhaust all 48 and 20,480 adjacent-distinct sequences for `p=3,5`, test cyclic graph masks, and verify 12 actual original-order selectors.
- [Parent control](../review-waves/f111-olson-ordered-four-odd-boundary/parent-ordered-four-check-v1.py): `a81500373188149777c5d21e486860348a64d55362c4637bd7b793974b333925`; [actual receipt](../review-waves/f111-olson-ordered-four-odd-boundary/parent-ordered-four-check-result-v1.json): `6fb8d73713deb63515b9469022db2d1680038a4c2cb0fb733169a65812e25bc4`. On 2026-10-28 at 19:32:04 PDT it independently enumerated all 16 and 4,096 translation-normalized adjacent-distinct sequences for `p=3,5`, with no counterexample. The shorter `p+1` controls `[0,1,2,0]` and `[0,1,2,3,4,0]` have no ordered zero quadruple. Finite checks do not prove the all-prime lemma.

No later family construction or historical caller predicate is used as a premise. No completed review here establishes the original conjecture, novelty, entropic or other unrelated claims.
