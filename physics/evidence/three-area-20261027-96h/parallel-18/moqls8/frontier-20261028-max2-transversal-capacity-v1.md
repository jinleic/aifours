# Maximal-source two-MOLS nets: exact transversal capacity and a quantum support bound

**Status: WRITTEN all-variable implication plus independently cross-checked finite source census; mathematical review and source-classification authentication remain pending.** The finite results concern all 2,127 pairs actually present in the pinned local reader snapshot, not an unqualified claim about every possible order-8 pair.

For two classical MOLS A,B of order 8, a *common transversal* is an eight-cell set meeting every row, column, A-symbol line and B-symbol line once. Let `ν(A,B)` be the largest number of pairwise disjoint common transversals. The exact local-source census finds:

| ν | indexed pairs |
|---:|---:|
| 0 | 1,980 |
| 1 | 34 |
| 2 | 79 |
| 4 | 34 |

In particular, all 2,127 pinned pairs have `ν≤4`, and hence none admits a third classical MOLS. This last conclusion is independently demonstrated for the local pairs; it does not require trusting the word “maximal” in their source. Conversely, the positive count of 147 pairs with at least one common transversal shows that **absence of a third classical mate must not be confused with absence of any common transversal**.

## 1. A quantitative bound for any complex quantum mate

Let Q be ANY actual complex QLS orthogonal to the two classical mates A,B, with no fourth square, flatness or support-size premise. Independently normalize its first row to the coordinate rays `e_0,...,e_7`. For coordinate t let `h_t` be the number of its 64 cell rays equal to `e_t` up to phase; a cell not of this form is called *mixed*. Each h_t is at most 8 because no row of Q repeats a ray. If `h_t=8`, its eight cells meet every row exactly once; column ONBs and the two actual mate-symbol line ONBs likewise make them meet every line of the four-net exactly once. Thus they form a common transversal. Distinct full singleton-ray classes are disjoint, so at most ν coordinates can have `h_t=8`. Every other h_t is at most 7. Consequently

`mixed(Q) = 64 - Σ_t h_t ≥ 8 - ν(A,B)`.

This holds for arbitrary complex amplitudes and independently of any finite catalogue. There is also a catalogue-free **mixed(Q)≥6** for every nonclassical Q extending two classical mates: a mixed ray has at least two nonzero first-row coordinates. On each of its four net lines no singleton on one of its occupied axes can occur, while ONB completeness forces another mixed ray using that axis. The four other rays on those distinct lines are distinct, so at least five mixed cells exist. If exactly five existed, write the first x and the other four y_c according to the four line classes c through x. For every y_c, each of its other three class-lines must contain another mixed point, forcing the edges among the y's to use all three remaining line classes exactly once at that vertex. For any fixed class c, y_c already shares its c-line with x, and the other **three** y's each require exactly one c-edge among themselves. A matching cannot have three degree-one vertices; contradiction. Thus a nonclassical Q has at least six mixed cells.

Combining the two inequalities, every extra QLS on one of the 2,127 pinned pairs is nonclassical and satisfies:

| ν | minimum mixed cells in any Q |
|---:|---:|
| 0 | 8 |
| 1 | 7 |
| 2 | 6 |
| 4 | 6 |

If an actual four-family had two such extra members Q,R, both satisfy the same bound. Their support-surplus sum `Σ_x[(|S_Q(x)|-1)+(|S_R(x)|-1)]` is at least twice that number. This is a necessary budget only: it does not show that their mixed-cell sets are disjoint, exclude a q2 family, or resolve q3/q4/M(8)/A10/A11.

## 2. Exact count and packing evidence

The complete maximal-source reader snapshot `frontier-20261028-source-wanless-max2-complete-v1.txt` SHA256 **6786f29c22c354673df942485faeed7d462ebaf4e3916b7a649cc0ff6a303154** contains 4,254 listed squares grouped as 2,127 pairs. It was assembled from 128 exact raw-reader ranges with separator normalization; all 34,033 nonblank lines were retained and the first six pairs match the separately pinned excerpt. This does not assert HTTP-byte identity, source classification completeness, or pairwise nonisomorphism.

The integer bitmask dynamic program `frontier-20261028-max2-transversal-scan-v1.py` SHA256 2a111a93d57f4515455678613a0f74cd3dc8a2fb9afe0d735587d84eb0f8d2a0 validated every listed Latin/MOLS pair and counted all common transversals; full receipt SHA256 0745ac58eec8d02851910feedbff1ba29e6c8c8b247a1539d2f7e961b13142e4. An independently written C++ enumerator `frontier-20261028-max2-transversal-exhaust-v1.cpp` SHA256 d566062102319391d595296160d349e3a453086770ad5dee57e83e27ea3e0b21 tested every one of 8! column permutations for every pair (85,760,640 in total); its output CSV SHA256 379d3843d889cc1937e476788b5f57265cc95ece15f6e15cd276b224d585079d. It also passed a separate affine extendible positive control. `frontier-20261028-max2-transversal-compare-v1.py` SHA256 1a7905b73de652db3a9761f60f10af066d629f1f757fca0a39da32a0019f73f2 matches **every** DP count against the independent permutation result and rejects missing/altered case controls; receipt SHA256 6b15489aaeedffbc3c2c7b3b73fb5ba631026aeb696461da6a7e1e031c98fd9a.

There are exactly 147 positive-transversal pairs in this local data (counts 1,2,3,4,8,12 or19), and 1,980 with zero. For each positive case, `frontier-20261028-max2-transversal-packing-v1.py` SHA256 fe1d0327f73f3f4135d9f5425511b8a71b1e8b7ced8d4c7553be2b22739453d0 lists the complete common transversals and a maximum packing witness; receipt SHA256 0090a1762bfd8299b14da8d5c60e99ba104dd2cc55076b0bd5daed731d8d16ba. The separately coded full-subset checker `frontier-20261028-max2-transversal-packing-check-v1.py` SHA256 5676c544c152fc7299635e5d5b339ab4fc940480f7914c096a3bfd6def9cb8f1 verifies every listed transversal, completeness against the independently exhaustive counts, and every maximum/witness; receipt SHA256 **98a46239db44604f3adc40eecb7a507b21bf5a390ab7c5beca00c9e2438d5184**. It rejects changed maxima, missing transversals and invalid witnesses. A separately pinned extendible pair with 16 transversals has packing 8, providing a positive control.

Eight disjoint common transversals partition the board and yield the eight symbols of a third ordinary MOLS; conversely any third mate gives eight such transversals. Thus `ν≤4` genuinely proves no classical third mate for each of the 2,127 explicit local pairs, but says nothing by itself about quantum extension. The source reports these as the maximal two-MOLS species; transferring this finite result to all maximal pairs requires that external classification and faithful source mapping as named assumptions. The owner-local q2 certificates so far cover only six of these pairs, not all 2,127.
