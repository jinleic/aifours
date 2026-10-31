# Two disjoint adjacent reflection pairs force a selector

Owner **MathOlson-2-2**. Native `/bin/date` before this write: **Wed Oct 28 17:55:04 PDT 2026**. Written all-variable proof, plus exact bounded checks disclosed below; no independent peer review or novelty determination.

## 1. Theorem and precise remaining form

Let p be any odd prime. Let W be an ACTUAL `D_(2p)` word of length `4p−1`, with `3p−3` rotations and `p+2` reflections. If W has two disjoint actual adjacent reflection pairs—indices `i,i+1,j,j+1` with `i+1<j`—then W has an original-order identity subsequence of length2p.

More generally, under a hypothetical no-selector assumption, the existence of even ONE adjacent reflection pair forces these facts:

* the rotations are exactly `2p−1` copies of `r^a` and `p−2` copies of `r^b`, for distinct exponents `a,b` with `a!=0`;
* for EVERY adjacent reflection pair `(r^y s,r^z s)` in original order, `z−y=−(a+b)`.

Thus a hypothetical avoiding word has at most ONE reflection run longer than one, and that run has length two or three. If it has length three, b=−a and the three reflection exponents are equal. It may instead have no adjacent reflections at all. These are necessary residuals, not constructions of avoiding words.

## 2. Named exact input and proof of the one-pair consequence

The core reduction and equality lemma from `frontier-20261028-dihedral-core-and-four-reflections-v1.md`, SHA256 `5e7f65b8764d4f52ccddadd9ea2934d0635ca5c2085a3c41e520b336a93c767f`, are inputs to this successor. Precisely: under no-selector there are `2p−1` copies of a nonzero rotation a and `p−2` extra rotations `b_i`, such that the translated sequence `d_i=b_i−a` is zero-sum-free; its subset-sum set A has size at least p−1; and if A misses one residue m then all d_i=−m. That source gives complete written proofs, including p=3. It is a same-owner theorem candidate, not yet independent-review acceptance.

For an actual adjacent reflection pair, no rotation occurs between the two reflections. Select ANY subset S of the extra rotations and exactly `2p−2−|S|` core rotations. Their total exponent is `−2a+sum_(i in S)d_i`, in the original word because the selected reflections form an adjacent pair. Let the reflection exponents be y,z in chronological order. The selected product is identity exactly when

`z−y ∈ −2a+A`.

If A were all F_p, this pair would work. Hence A has exactly p−1 values, missing some m, and the named equality lemma forces `d_i=−m` for ALL i. Thus all extras equal `b=a−m`, with b!=a, and the unique missing allowed target for EVERY adjacent reflection pair is

`z−y = −2a+m = −a−b`.  (1)

This establishes the one-pair consequence. It uses the same global A for every adjacent pair, not a pair-dependent missing value.

## 3. Two pairs and the actual selector

Choose two DISJOINT adjacent reflection pairs. By (1), each contributes exponent `y−z=a+b` to their two-reflection product. Select `p−2` core rotations and ALL `p−2` extra rotations. Their sum is `(p−2)(a+b)=−2(a+b)` in F_p.

Select the four reflections of the two pairs as well. The total number of selected original occurrences is `(p−2)+(p−2)+4=2p`. There is no rotation inside either adjacent pair. Before, between and after the two pairs the selected reflection parity is even, so every selected rotation enters the actual ordered product with positive sign. The exponent is `−2(a+b)+2(a+b)=0`; the reflection parity is even. This is an ACTUAL original-order identity selector, contradicting no-selector.

The theorem also holds when b=0 or b=−a; no division by b or a+b occurs. If a run has three reflections and (1) holds for each of its three pairs, its two adjacent differences and total first-to-third difference are all the same, hence that difference is zero; b=−a and the three exponents are equal. A run of four or more would itself supply two disjoint adjacent pairs.

## 4. Core-gap structural consequence

In the core reduction let `t_i` be the number of the `2p−1` a-rotations before reflection i. The same input prohibits `|t_j−t_i|` equal to p−1 or p. In particular, among the 2p integers `0,...,2p−1`, the p pairs `{k,k+p}` for `0<=k<p` show that the reflection prefix counts take at most p distinct values. There are p+2 reflection occurrences, so at least two occurrences are repetitions beyond the number of distinct core gaps.

If no adjacent reflections occur, every repeated reflection in a fixed core gap requires at least one intervening EXTRA rotation: no core rotation occurs inside that gap. Hence at least two extra rotations are needed. For p=3 there is only one extra, so any hypothetical avoiding word at p=3 necessarily has an adjacent reflection pair. This does not on its own rule it out.

## 5. Family that needs the separated-pair mechanism

For each odd prime p>=5, concatenate the following actual occurrences, with `r^(-1)=r^(p−1)` and every reflection equal to `r^4s`:

`[2p−1 copies r] · [2 copies r^4s] · r^(-1) · [3 copies r^4s] · [ (r^(-1), r^4s) repeated p−3 times ]`.

There are exactly `3p−3` rotations and `p+2` reflections. The reflection runs have lengths 2,3 and p−3 singleton runs. No run has length four, and the three-run has equal exponents, so the prior run theorem does not apply. The two initial runs contain disjoint adjacent pairs; selecting their first four reflections, p−2 of the initial r occurrences, and all p−2 `r^(-1)` occurrences gives the actual selector of §3.

For ANY two reflection positions, all core r's occur before them, while any intervening `r^(-1)` contributes a signed +1. Thus the signed +1 multiplicity is at least2p−1 and the signed −1 multiplicity is at most p−2, so the previous signed-pair sufficient condition fails for every pair. In fact there is no selector using exactly two reflections: their exponents are equal and any `2p−2` signed rotations have exponent `−2(1+v)` with `0<=v<=p−2`, nonzero mod p.

The previous fixed-I certificate also fails: its first `2p−2` r rotations all precede the reflections and have exponent sum −2, while all reflection exponents coincide. Every rotation gap is monochromatic, so the previous same-gap unequal-pair resource is zero. The quotient-type word has `2p−3>3` odd runs, and therefore fails the saturated separated-packet certificate. The previous short-reflection-run condition also fails: maximum unequal raw rotation pairs is p−2 and each run's directed difference support is `{0}`, so its strict support inequality is equality, not success. This is NOT an avoiding-word family; the four-reflection selector is explicit.

## 6. Checks and honest failed diagnostic

Actual checker `frontier-20261028-dihedral-two-adjacent-checker-v2.py`, SHA256 `0c832655ca236470e3dd465eb022189272b783eda90d33b74bdfda11859f2077`, returned `PASS_TWO_SEPARATED_ADJACENT_PAIRS_CORRECTED`, saved as `frontier-20261028-dihedral-two-adjacent-check-results-v2.json`, SHA256 `f5809951aa2838471bae13372c7146d29a812f16f75bc36fd4939b04842ee878`. It checked the explicit actual family at p=5,7,11,13, all its reflection pairs against the earlier signed/fixed-I conditions, exact run/gap/saturated-pair conditions, and the actual 2p-index four-reflection product. An odd-reflection-parity mutation was rejected in each case. This is one family at four primes, not a universal verification.

The FIRST proposed family checker, `frontier-20261028-dihedral-two-adjacent-checker.py`, SHA256 `8b67616d3f21f8a88e1598b9cca76c69314352758a33fce5d95ba067761ea9e1`, actually exited with `ValueError: prior signed-pair test unexpectedly qualifies`; it did not write a result file. Its first family placed an a-rotation by itself between two reflections, making that pair eligible for the earlier signed criterion. That failure was not a refutation of the theorem; it refuted the claimed strict-separation property of that illustrative family. The preserved first checker was not edited after pinning; the corrected family/checker above is a NEW successor.

No general original Olson closure, formal/kernel proof, external-model/human review or novelty is claimed. All other count bands remain open.

**END — disjoint adjacent-pair theorem, actual selector, and residual.**
