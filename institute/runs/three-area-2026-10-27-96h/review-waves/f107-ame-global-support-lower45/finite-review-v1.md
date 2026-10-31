# Independent finite review: AME(4,6) global support ≥45 candidate

## Verdict and boundary

**INCONCLUSIVE for the global ≥45 theorem.** No FATAL, MAJOR, or MINOR discrepancy was found in the finite claims exercised here. The independently implemented finite controls reproduce the stated incidence/parity and mixed-support counts; every one of the 576 mixed-case projection survivors has a one-column row overlap and a one-row column overlap in the AD|BC cut. None is a physical AME tensor. The other two cuts do **not** exhibit this particular obstruction in any of the 576. The stated rank-four shadow bound is independently derived below and supported by exact Gaussian-rational calculations, including a non-diagonal complex example.

This does not adopt ≥45, establish the prerequisite ≥42 or ≥44 statements, prove Tarry's no-OLS(6) theorem, review source priority, or establish the full normal-form reduction from all normalized complex AME(4,6) states. It is a same-harness computation and written analysis, not blinded, cross-vendor, human, formal/kernel, or novelty verification. In particular, graph-filter survivors are necessary-support candidates, not demonstrated unitary matrices or physical states. The named classical no-OLS(6) theorem is an import.

## Inputs, execution, and reproducibility

The manifest was read first. All ten complete input byte strings were then hash/length/LF checked and their mathematical bodies read in manifest order. CR count was zero for each. The source programs were read for their stated scope; **none was executed or imported**. This review's program was written after those readings and is an independent implementation, not a blinded reading.

| Manifest role, in read order | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| ≥42 dependency | 11,168 | 107 | `50e97ebd0a30f2bcb1999fa85896f88bf4590d89fd897c60d9de53fe5775bedf` |
| ≥44 dependency | 10,465 | 79 | `89e2de23d4777697bd4e2b55e5925f3bd50f5f07c2e0e18aeb548ddd70052a30` |
| Two-excess unitary dependency | 5,264 | 43 | `4a6d012d39ae8ae3acd0bb2ba04d0f79c824a9002633a0d2a45d91038119bec0` |
| ≥45 candidate | 15,561 | 103 | `26a4115ff62f56320af2647c550072255d0ab7c6c90de49ef83025d9219a1121` |
| Author parity program | 3,203 | 79 | `e8fd4a05b0305fe399b39230c965cffb9110d68701346d258b34b8a5525950ee` |
| Author parity receipt | 432 | 16 | `78fb02b43d535fb1228c3e940b5c45afabb49278c2aeb0816ff1bd9fa4886494` |
| Author mixed program | 3,765 | 84 | `77cb2b5ebaca90b43c06f996a1d4279be19130d4a2751d89808bc21d73741a82` |
| Author mixed receipt | 1,749 | 146 | `3c7e09fc9bfcb4dd20d5c8149feddad2a5722893c58117a69f0d02d8fa320cc2` |
| Author shadow program | 1,872 | 38 | `9ed98305b8ad05ce15642dc05da8a3024a7d352929bdb53b4f062b7feee72017` |
| Author shadow receipt | 322 | 7 | `2db5eeabadae4bcee850cd0078622e49777bfadeb4a2f478c3ac8940bb685f96` |

Manifest SHA-256: `b1565273e7c79e38346cc455e1a6e93943da91421f6d003d523b3005cb3b9300`. The [independent checker](finite-check-v1.py) has SHA-256 `79f5f43b471445a97a73621ff3c7168c32d8a8fcde938ce8a2441c103aefe069`; the [execution receipt](finite-receipt-v1.json) has SHA-256 `fe6a0ccaab37b5fef71570ddf2dff23a6cc9b6c79ec481586d3a8ebc92e76ca0`. The receipt also repeats all source byte pins, gives concrete witnesses, counts and controls, and records the Python/platform/argv. It was produced by the actual command, from this review directory:

```
python3 -B finite-check-v1.py finite-receipt-v1.json
```

The checker refuses to overwrite its receipt. It recorded start `2026-10-29T02:15:04.119105+00:00`, finish `2026-10-29T02:15:05.172215+00:00`, and monotonic elapsed time `1.052922167116776` seconds; shell-reported wall time was 1.18 seconds. No author code, network, paid API, or external model was used.

## R44, R34, and ternary-pair parity

For each labeled incidence matrix, the checker enumerated four row subsets of size two and checked column degrees from first principles. It obtained 90 quaternary 4×4 degree-two matrices; 12 ternary 4×3 matrices with degree vector `(2,3,3)` and the degree-two symbol labeled 0; and 36 ternary matrices when that low label ranges over all three values. These are labeled counts, not isomorphism classes. For each ordered matrix pair and all 16 masks including the empty mask, it counted each rectangle cell directly modulo two, rather than importing the author's parity code. In the table, counts exclude the empty mask:

| Ordered pair type | Matrix pairs | All masks tested | Even masks of weight 2 | Even masks of weight 4 |
|---|---:|---:|---:|---:|
| 4/4 | 8,100 | 129,600 | 216 | 108 |
| 3/4, all low labels | 3,240 | 51,840 | 216 | 0 |
| 3/4, low label 0 | 1,080 | 17,280 | 72 | 0 |
| 3/3, all low labels | 1,296 | 20,736 | 216 | 216 |
| 3/3, both low labels 0 | 144 | 2,304 | 24 | 24 |

There were no nonempty zero-parity masks of weight 1 or 3. Every 4/4 survivor has both matrices split into two `K₂,₂` components with the same fiber partition; for a weight-two mask it is one partition cell. Every 3/4 survivor uses exactly the ternary matrix's duplicate-row pair and that pair is a cell of the quaternary split. For 3/3, the weight-two mask is the common duplicate pair, while the weight-four case has complementary duplicate pairs. Thus the finite R44/R34 assertions and the auxiliary 3/3 classification at the stated sizes are confirmed, conditional only on the matrix definitions and exact implementation.

Targeted counterexample controls: two valid degree-two 4×4 graphs with different fiber partitions, encoded by row masks `(3,3,12,12)` and `(3,12,3,12)`, have nonzero parity for full mask 15. For ternary `(6,6,3,5)` and quaternary `(3,3,12,12)`, duplicate mask 3 has even parity but mask 15 does not. Invalid row-degree and column-degree mutations are rejected for their respective intended reasons. These controls prevent replacing the parity hypothesis by merely having individually valid incidence graphs.

## Mixed `(3,3,4,4)` normal forms and all flattenings

Write the ordered coordinates as `(A,B,C,D)` of sizes `(4,3,3,4)`, with the low-degree symbols of B and C relabeled 0. The review is exhaustive **conditional on** the candidate's residual facts: four A-fibers of four distinct words; each other coordinate takes two values twice in each fiber; B and C have incidence degrees `(2,3,3)`; D has degrees `(2,2,2,2)`; and each global pair projection has eight values, each with two extensions. The relabeling is a normalization, not a count of all labels in an ambient six-symbol product basis.

The generator first enumerates all `C(8,4)=70` four-subsets of a binary cube and retains the eight balanced subsets. Exactly two are full on all three coordinate pairs; for each of BC, BD, and CD exactly two are correlated on that one pair and full on the other two. Thus each of the four fibers has four possible correlation *types*, with two actual balanced point sets per type. This generates all `12×12×90 = 12,960` labeled incidence triples and all `4⁴` type assignments per triple, without assuming the author's displayed normal form. Rectangle parity is a necessary filter before direct pair-count testing:

* **144** incidence/type parity forms; all have `(F_BC,F_BD,F_CD)=(15,p,15−p)` for a two-bit mask `p`. Each of the six labeled choices of `p` occurs 24 times.
* **0** parity forms have an empty full-fiber mask. The checker included empty masks and all four correlation types, rather than assuming this exclusion. Indeed, an empty full mask forces all four fibers correlated on that pair; the two other pairs are then full on all four fibers, one of which is 3/4, contradicting R34. Thus this particular mixed-case observation does not require the no-OLS import, once the stated incidence/balance and parity hypotheses hold.
* **2,304** actual four-fiber supports were constructed from the 144 forms, with all 16 independent binary point-set choices per form. Exactly **576** have all six pair projections of cardinality eight and every pair-value multiplicity exactly two; **1,728** fail a pair-projection cardinality check. A support uniquely recovers its labeled fiber incidence sets and correlation types, so these are distinct normalized supports, not merely repeated generator paths.

For each of those 576 supports, the implementation checked **both** row and column supports in **each** of the three complementary 2|2 flattenings:

| Cut | No unique overlap | Unique overlap among rows and among columns |
|---|---:|---:|
| AB\|CD | 576 | 0 |
| AC\|BD | 576 | 0 |
| AD\|BC | 0 | 576 |

A concrete 16-word support and both obstruction witnesses are retained in the receipt. In its AD|BC flattening, rows `(0,1)` and `(2,3)` have BC supports `{(1,1),(1,2)}` and `{(1,1),(2,1)}`, respectively, with the single common column `(1,1)`. Conversely, columns `(1,1)` and `(1,2)` meet only in row `(0,1)`. Any putative matrix with exactly that support has a nonzero single term in the corresponding inner product, irrespective of complex phases, so it cannot be unitary. This is an obstruction, not a construction of a state.

A targeted mutation removes one support word and is rejected for support cardinality; another changes `(0,0,1,0)` to `(1,0,1,0)` while retaining 16 distinct words and is rejected specifically for pair-projection multiplicity. As separate overlap controls, the two 2×2 blocks `(3,3,12,12)` have no unique row or column overlap, while the six-cycle `(3,6,5)` has both.

## Small unitary-support lemmas

The independent support-graph enumeration also examined every row-degree pattern for sizes `n=2,3,4,5` and excess `e=0,1,2` above `2n`, pruning branches as soon as a unique row overlap occurs and subsequently checking column degrees, unique column overlaps, and balanced bipartite component sizes. The raw counts below are computed combinatorially before this pruning; passing counts are **support graphs**, not claims that arbitrary graph filters prove unitarity.

| `n` | Raw / passing at `e=0` | Raw / passing at `e=1` | Raw / passing at `e=2` |
|---:|---:|---:|---:|
| 2 | 1 / 1 | 0 / 0 | 0 / 0 |
| 3 | 27 / 0 | 27 / 0 | 9 / 9 |
| 4 | 1,296 / 18 | 3,456 / 0 | 4,320 / 0 |
| 5 | 100,000 / 0 | 500,000 / 0 | 1,250,000 / 900 |

At `n=5,e=2`, 1,000 graphs pass the row/column overlap filters; 100 have rectangular 2×3 and 3×2 connected components and fail the square-component condition, leaving 900 with a 3×3 eight-entry component plus a 2×2 component. The explicit masks `(7,7,24,24,24)` are a negative control: they pass both overlap filters but have component shapes `(2,3,6)` and `(3,2,6)`, where the third number is edge count. They are not a new finding: the pinned unitary dependency already discloses this correction. A unitary support component must have equally many rows and columns, since its rows and columns are each orthonormal in the other's ambient dimension.

For sharpness, the exact real rational matrix

```
  [  3/5     4/5       0  ]
  [ -12/25   9/25     4/5 ]
  [ -16/25  12/25    -3/5 ]
```

has eight nonzeros and both Gram matrices exactly `I₃`. This prevents the false strengthening that every odd-size no-singleton unitary needs at least `2n+3` support entries.

The general one- and two-excess arguments can also be reconstructed directly; these are written mathematics, not consequences of the `n≤5` enumeration alone. At exactly `2n`, every row and column has degree two, and a cycle longer than four would contain a unique-overlap row pair; hence all components are 2×2 and n is even. At `2n+1`, the single degree-three row has all neighbors using two of its three columns; distinct choices overlap once, so all neighbors use the same pair, leaving its third column with degree one, impossible.

At `2n+2`, either there is one degree-four row or two degree-three rows. In the degree-four case, degree-two neighboring rows use two of its four columns; distinct occurring pairs must be disjoint, and the column-degree condition forces two disjoint pairs. Two degree-two rows cannot use the same pair: they would span `C²`, leaving no nonzero restriction of the exceptional row orthogonal to both. Consequently each pair supports exactly two columns on two rows, a unitary 2×2 subblock that exhausts the exceptional row norm, contradicting its other nonzeros. In the two-degree-three case, their intersection cannot have size one; if zero, one of the first row's three columns has no other neighbor; if two, a degree-two neighbor of its third column would meet the second row in exactly one column. Thus they share all three columns. All other rows meeting them use the same pair, and at most one such row can occur by the same `C²` argument; at least one must occur because three orthonormal columns cannot be supported on two rows. This isolates an eight-entry 3×3 unitary block. All remaining support is degree two and hence 2×2 blocks, so n is odd. The rational 3×3 matrix above and any full 2×2 unitary provide sharp examples for odd n. This written argument covers the candidate's n=6 and n=7 uses; the finite enumeration itself stops at n=5.

## Exact three-qubit shadow inequality and controls

Using Pauli matrices `I,X,Y,Z`, the checker represented every matrix entry as a pair of rational numbers `(real, imaginary)`. It explicitly checked all 64 three-qubit Pauli strings under `P ↦ Y⊗3 conjugate(P) Y⊗3`: the sign is `(-1)^weight`, with weight counts 1, 9, 27, 27. It also checked all 192 two-qubit partial traces of those basis matrices.

For an arbitrary three-qubit **density** matrix with all two-qubit marginals `I₄/4`, Pauli coefficients of weights one and two vanish. Its Hermiticity makes its remaining coefficients real, so

```
ρ = (I₈ + Σ_weight-3 r_P P)/8,
ρ̃ = (I₈ − Σ_weight-3 r_P P)/8 = I₈/4 − ρ.
```

Complex conjugation followed by unitary conjugation preserves positive semidefiniteness, so `ρ̃≥0` and hence `ρ≤I₈/4`. Together with `ρ≥0` and `Tr ρ=1`, this gives `rank ρ≥4`. This proof applies to every such mixed state; the finite Pauli-basis checks verify its algebra but are not a formal proof.

The exact sharp example is `ρ=(I₈+Z⊗3)/8`, equivalently the equal mixture of the four even-parity computational basis states. It has rank four, spectrum `{1/4 (×4), 0 (×4)}`, and all three pair marginals `I₄/4`. The checker also conjugates it by the genuinely complex rational unitary `U⊗I⊗I`, where `U=(1/5)[[3,4i],[4i,3]]`; its full off-diagonal matrix, rank, three marginals, spin identity, and `4ρ²=ρ` are checked exactly. Both examples saturate the eigenvalue bound.

Targeted controls: deleting one of the four diagonal components and renormalizing produces rank three but fails all three pair-marginal tests; omitting complex conjugation in spin flip fails already on `YII`. The Hermitian trace-one operator `(I₈+2Z⊗3)/8` has the correct two-qubit marginals and satisfies the spin identity but has eigenvalues `−1/8` and `3/8`: it is not positive semidefinite and explicitly shows why positivity cannot be omitted from the spectral inequality.

## Remaining unverified reductions and acceptance conditions

The finite mixed enumeration does not itself derive the residual incidence/balanced-fiber hypotheses, the alphabet case split, the grouped-qubit construction, or the global coverage of `(2,4,4,4)`, other four-valued cases, and the three/four-ternary cases. Nor does it establish the full ≥42 and ≥44 dependency chain, the fiberwise-free completion argument in the other alphabet cases, or the classical no-OLS(6) import. Those written mathematical steps remain separate review obligations. No 45-term state, exact global minimum, priority, or novelty claim is made here.
