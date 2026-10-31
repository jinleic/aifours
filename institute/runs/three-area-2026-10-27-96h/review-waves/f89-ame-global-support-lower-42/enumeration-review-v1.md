# Independent enumeration review: AME(4,6) global support 42 and 44

Native `/bin/date` clock observed immediately before exclusive creation: `2026-10-28T19:07:40-0700 PDT`.
Reviewer: `AMEGlobalEnumerationReview`; same-harness independent calculation, not an external-model or human review.

## Verdict and boundary

* **≥42, binding review packet v2:** FATAL **0**, MAJOR **0**, MINOR **0** in the reconstructed argument and assigned finite controls, **conditional on the named Tarry no-OLS(6) theorem**. No finite control below alone proves the global claim.
* **≥44, candidate v1 §§2–6:** FATAL **0**, MAJOR **0**, MINOR **0** in the reconstructed argument and assigned finite controls, conditional on the ≥42 dependency and Tarry. In particular, the one bipartite 12-term residual support is genuinely realizable in all three residual cuts, so excluding it requires the completion argument, not just a support or local-phase filter.
* **Standalone universal 2n+2 classification, v1:** FATAL **0**, MAJOR **0**, MINOR **0** in my reading of the written proof; the n=3,4,5,6 cases and constructive realizability are independently checked below. The correction from 1,000 to 900 realizable n=5 patterns is essential and is confirmed.
* **Manifest v3 dependency wording, separate MINOR scope observation:** its scope says the ≥44 claim depends on the new 2n+2 lemma. The pinned ≥44 candidate §§2, 3 and 6 actually uses the 2n and 2n+1 results: N=42 gives n=6 and |E|=12=2n; N=43 gives (n,|E|)=(6,13) or (7,14). No 2n+2 step occurs there. This does not impair either candidate; I reviewed the newly mandated standalone result anyway. This observation is not counted as a mathematical defect in the candidates.

These are review dispositions, not parent acceptance, formal proof, independent-family verification, or proof of Tarry. I do not establish novelty, priority, the true minimum, or an AME state with 42, 43, or 44 terms. No held/withdrawn body is used as a premise. The public [Pandya preprint](https://arxiv.org/html/2610.16673#S6) indeed states 38 as its cited lower bound and gives the 60-term state; that comparison is not a priority audit.

## Input and calculation binding

`manifest-v3.json` SHA-256 `0d6b417b5cba038801fb6d7a85c62a86aaf3757518431cc7d0f3c4ac36a669ba`. Its first 14 paths, hashes, lengths and LF counts are byte-identical and in the same order as v2; I read those 14 completely in exact raw windows in v2 order, then read v3's three appended inputs completely, in order. I rechecked the SHA-256, byte length and LF count of **all 17** against v3; all matched. Identity hashes do not validate claims. In particular, packet v2 SHA-256 `50e97ebd0a30f2bcb1999fa85896f88bf4590d89fd897c60d9de53fe5775bedf` is the binding ≥42 statement.

I wrote my own standard-library-only programs, exclusively created in this review directory; no author checker is imported or executed as proof. Results and immutable program identities:

| Own artifact | SHA-256 |
|---|---|
| `enumeration-independent-v1.py` | `317e3b8429bdd3f6dcb9c075906645501af69bb711a4270abd3a4d1c39581776` |
| `enumeration-independent-v1.json` | `c2254cf5e50e93aeacec00746f6d1099edc62bf4b4b443300d29600fb1b2e42e` |
| `enumeration-n7-independent-v1.json` | `937173cb9924e4ddbbf6223ff499fb2217356070a80d60ad7f9a6dd48cf565b3` |
| `enumeration-bipartite-v1.py` | `627a7ff15e9bd342d6136c28f2052c918db82c3c6db76a47d2c004725712a676` |
| `enumeration-bipartite-v1.json` | `443d4830224d2c2988d49ff25a2cda078d4f5e2e4ac76009ec2eaa84e44395c6` |
| `enumeration-pandya-v1.py` | `c65536bb386e34e858db84416087ea5bf0769627174bb52a50ee8f1cc6c60529` |
| `enumeration-pandya-v1.json` | `fbe2b925f62a67eacd84ca90897d633697d8a79ae365375b356c986c77480673` |

Programs write fixed-name receipts exclusively, so replay requires an empty authorized directory rather than overwriting these receipts. The supplemental bipartite program initially had a newline quoting syntax error; that failed before execution or receipt creation, was corrected, and then ran successfully. Importing my own program for the n=7 extension also created `__pycache__/enumeration-independent-v1.cpython-314.pyc` in this directory; it is retained under the no-deletion rule and is not a premise or receipt.

## ≥42: n=5 normal form and independent exhaustive enumeration

Let E be the residual support after saturated coefficients are removed. For **each of all six** pairs of tensor coordinates, suppose `|π_ij(E)|=n` and every displayed pair has at least two E extensions. For every coordinate i, if r values occur, each i-fiber must vary in at least two other coordinates. The variation incidence count gives `2r ≤ 3(n−r)`, hence `r ≤ floor(3n/5)`.

For n=5 each local coordinate has at most three values, and at least one, A, has exactly three because pair projections have size 5. Equality in the incidence count forces each A-fiber to vary in exactly two of the other coordinates, and each other coordinate to vary in two fibers using exactly two values there. Thus each of X,Y,Z is fixed in exactly one different fiber. The two-extension condition forces each fiber to be a **complete 2×2 rectangle**, hence E has 12 distinct points. This reduction is a written argument; the finite loop checks the resulting normal forms, not its universal premises.

I do **not** use the author's 27³ coordinate-option generator for the support enumeration. Relabel local symbols so that Y and Z in fiber A=0, and X in fiber A=1, have anchored two-set `{0,1}`. Directly enumerate these three entire rectangles:

* `A=0`: `{a} × {0,1} × {0,1}` — 3 choices;
* `A=1`: `{0,1} × {b} × T` — 9 choices;
* `A=2`: `U × V × {c}` — 27 choices,

where a,b,c range over three symbols and T,U,V independently range over their three two-subsets. This gives **729** gauged supports. For each coordinate the unnormalized anchored two-set has 3 choices; mapping its two symbols in increasing order to 0,1 and the third to 2 gives a bijective gauge choice. Therefore each gauged case has exactly 3³=27 labelled preimages, including padded smaller alphabets: 729×27=**19,683** labelled normal forms.

The independent set construction found **0** with remaining projection triple `(5,5,5)` and **24** gauged cases, equivalently **648** labelled cases, with `(5,5,6)`. Its entire **55-class** labelled projection histogram agrees entry-by-entry with the pinned direct receipt. This is stronger than needed for the n=5 contradiction because I do not require the remaining pairs to satisfy the extension-multiplicity condition before rejecting `(5,5,5)`.

I independently built the compatibility graph by scanning all **512** binary 3×3 incidence matrices per class and retaining the row-degree profiles 1,2,2. There are 27 vertices/class; edges join vertices exactly when their pair projection has size 5. The three bipartite edge counts are **144, 144, 144**; there are **1,080** two-edge wedges centered in the first class and **0 triangles**. With the shared canonical vertex order, my edge-mask digest is `cbf4ae8edce63a68fcd89175068562890e648ea275864135079638af59e0f249`, matching the author. Among **2,187** vertex pairs, **432** have size-5 projections; there are **0** disagreements with the stated singleton-in-base plus XOR characterization. Replacing XOR by OR is rejected in **432** cases. Thus the direct, graph and XOR author controls all agree with my independently constructed counts.

## Exact support-pattern classification, including the 2n+2 lemma

For each n and edge count, I count **labelled** n×n 0/1 support matrices with every row and column degree at least 2. A capped-column-degree dynamic program counts that universe. A separate enumeration generates sorted multisets of degree-2/3/4 rows, rejecting row pairs with exactly one common support, checks column degrees and restores row labellings by multinomial weight. The degree cap is exhaustive for total `2n+δ`, δ≤2. It then rejects column pairs with exactly one common support and records every connected bipartite component `(row count, column count, edge count)`. The overlap filters are necessary, not sufficient, for a unitary.

| n | nonzeros | all min-degree | no unique row overlap | also no unique column overlap | unitary realizations |
|---:|---:|---:|---:|---:|---:|
| 3 | 6 | 6 | 0 | 0 | 0 |
| 3 | 7 | 18 | 0 | 0 | 0 |
| 3 | 8 | 9 | 9 | 9 | 9 exact |
| 4 | 8 | 90 | 18 | 18 | 18 exact |
| 4 | 9 | 816 | 0 | 0 | 0 |
| 4 | 10 | 2,040 | 72 | 0 | 0 |
| 5 | 10 | 2,040 | 0 | 0 | 0 |
| 5 | 11 | 41,400 | 0 | 0 | 0 |
| 5 | 12 | 242,800 | 1,000 | 1,000 | 900 exact; 100 impossible |
| 6 | 12 | 67,950 | 1,350 | 1,350 | 1,350 exact |
| 6 | 13 | 2,559,600 | 0 | 0 | 0 |
| 6 | 14 | 28,031,400 | 21,600 | 0 | 0 |

For n=5, 12 entries, the 1,000 two-sided-overlap survivors split into **900** with components `(2,2,4)+(3,3,8)` and **100** with `(2,3,6)+(3,2,6)`. In the latter, three nonzero orthogonal rows would lie in a two-dimensional column space, so no unitary exists; equivalently the component rank is insufficient. The remaining 900 are exactly 3×3-complete-minus-one plus full 2×2, up to row/column permutations. This independently confirms the author's correction: **1,000 is not the number of unitary-realizable survivors**.

The constructive check is exact, stronger than numerical. My two real matrices are `H = (1/2)[[√2,√2],[√2,−√2]]` and `T = (1/2)[[√2,1,1],[−√2,1,1],[0,−√2,√2]]`. The checker verifies their row Gram matrices exactly in `Q(√2)`, not by floating point. They realize respectively K2,2 and K3,3 minus one edge, and their direct sums and independent row/column permutations realize every survivor marked “exact”: 9 T patterns at n=3, 18 H⊕H at n=4, 900 H⊕T at n=5, and 1,350 H⊕H⊕H at n=6. Deleting an entry of T is rejected by the exact Gram control. There are no other realizable patterns in the table because every excluded pattern violates a necessary condition.

As an extra check of ≥44 §6, the same independent code at n=7 found **0** no-unique-row-overlap patterns with 14 entries among **3,110,940** min-degree patterns, and **0** with 15 entries among **194,789,700** min-degree patterns; see the separate n=7 receipt. This is bounded corroboration, not the universal argument.

### Reconstructing the universal 2n+2 proof

For an actual complex unitary, a pair of rows or columns cannot have exactly one shared nonzero, and each disconnected support component must be square. Total row excess 2 means either one degree-4 row or two degree-3 rows.

* If one row has four columns, its degree-2 neighbors must use pairs within those four columns. Different occurring pairs cannot intersect in one column. All four columns need another neighbor, so the pairs are complementary; at most one neighbor can use either pair because two orthogonal degree-2 rows would span that pair's C² and force the exceptional row's restriction to vanish. Thus a pair of columns is supported on exactly two rows and forms a 2×2 unitary, exhausting the exceptional row's norm despite its other two nonzeros: contradiction.
* If two degree-3 rows have 0 shared columns, the degree-2 neighbors of one must all use the same two-subset of its triple and its third column has degree one. If they have 2 shared columns, any degree-2 neighbor of the remaining column overlaps the other exceptional row in exactly one. If they share all 3, every degree-2 neighbor uses a pair of these three; all such pairs must coincide and at most one neighbor is possible by the C² argument. Column orthogonality requires at least one neighbor. Thus there is exactly one, and the resulting isolated 3×3 block has 8 entries.

The remaining square unitary is degree-2 throughout, so its support is a disjoint union of 4-cycles: a longer even cycle has a pair of rows with one common column. Consequently n is odd, with one 3×3 eight-entry block and `(n−3)/2` full 2×2 blocks. Conversely `T ⊕ H ⊕ ... ⊕ H` gives every odd n≥3. The n≤6 enumerations corroborate this universal written proof, but do not by themselves establish it for arbitrary n.

The hardened author's n=3,4,5 2n+2 receipt agrees: row-degree candidates **9, 4,320, 1,250,000**, square-component survivors **9, 0, 900**, rectangular rejections **0, 0, 100**, and row-only false positives **0, 72, 0**. I obtained the candidate totals independently from the two possible row-degree multiplicities. The earlier one-excess control's entire n=2,3,4 row-only histograms also match my independent exhaustive histograms, including its 72 n=4 ten-entry row-only survivors; those 72 fail the additional column test, not the author's stated row-only filter.

## AME(4,2) spin-flip: exact and numerical checks

For a normalized pure four-qubit state, put `S_w = Σ_{wt(P)=w} Tr(ρP)^2`. Expanding the purity identities for the four 3-qubit/complementary 1-qubit pairs gives, **without assuming two-uniformity**,

`S_3 = 12 + S_1 − 2 S_2`, `S_4 = 3 − 2 S_1 + S_2`, and
`Tr(ρ ρ̃) = (1−S_1+S_2−S_3+S_4)/16 = (S_2−S_1−2)/4 ≥ 0`,

where `ρ̃ = Y^⊗4 overline(ρ) Y^⊗4`. This is a positivity statement for the two PSD matrices, not a numerical heuristic. Under the hypothetical two-uniform assumption, `S_1=S_2=0`; the exact rational sums are `(S_0,S_1,S_2,S_3,S_4)=(1,0,0,12,3)`, and the exact spin-flip expression is `(1−12+3)/16=−1/2`, contradiction. This agrees with review packet v2 §3.

My independent numerical code computed all 256 Pauli expectations and spin-flip overlaps on **256** seeded random equal-magnitude, Hamming-weight-two phase perturbations of the Higuchi–Sudbery state, plus **128** seeded Haar-complex states; seed `60281028`. The former have numerically maximally mixed one-qubit marginals (`max S_1 = 5.24e−32`) but are **not** assumed or claimed to be two-uniform. Their mean pair purity was at least `0.3333370759`, not `1/4`; individual pair purities ranged `0.2973615–0.3875533`. Across both groups the largest absolute discrepancy between direct spin-flip and the Pauli parity formula was `4.31e−16`, and the weight-3 identity's largest residual was `9.77e−15`. All computed spin overlaps were nonnegative. The unperturbed Higuchi–Sudbery control had weight sums approximately `(1,0,2,8,5)`, all six pair purities 1/3, and spin overlap approximately zero. No random two-uniform four-qubit state was generated: the argument says none exists.

## ≥44: residual enumeration and written coupling

For N=42, the ≥42 dependency forces t=30, n=6 and |E|=12. Each pair projection has six values, **each with exactly two E extensions**. Each residual coordinate has at most 3 values; at most one can have 2, and none is constant. Fix a ternary A. Its three fibers have four points each, and every other coordinate is balanced 2+2 in each fiber. If another coordinate is ternary, the A-to-it projection is a 2-regular 3×3 bipartite graph, the complement of a matching; independent relabelling makes the missing matching diagonal.

I generated each four-point balanced fiber independently by scanning all 256 subsets of a binary cube, then combined the eight admissible fibers in each of three A-fibers. For the normalized **512** all-ternary configurations, **0** have all six pair projection cardinalities six. For the **512** one-binary configurations, **4** have all six projections of size six, each has multiplicity two everywhere and equals `S × {0,1}`; their shared-coordinate graphs are **3 nonbipartite and 1 bipartite**. These counts and the 512/512 controls agree with the author receipt.

For the bipartite case, I independently took the six triples S from my own receipt, two-colored the graph, assigned signs ±1 according to the color on the B=1 slice, and checked the three integer numerator flattenings satisfy **M Mᵀ = 2 I₆ exactly**. Dividing by √2 realizes the residual block in every cut. This is only a 12-term residual fragment; it is not an AME(4,6) state and does not complete the 30 maximal entries.

For arbitrary residual coefficients, if graph-adjacent triples s,s′ share one of A,C,D, orthogonality in the cut with that coordinate and B on the row side gives `conj(r_s) r_s′ = −1`, for `r_s=u_s0/u_s1`. The involution `r ↦ −1/conj(r)` has no nonzero fixed point, so the graph must be bipartite. Selecting one B value per S vertex according to a 2-coloring gives six words pairwise distinct in every pair of coordinates. All their pair projections avoid those of the 30 maximal words; adjoining them produces an OA(36,4,6,2), equivalently two orthogonal Latin squares of order 6, contrary to the named Tarry import. This is the load-bearing global step for the bipartite control; finite residual enumeration does not decide extendability to 30 maximal words.

For N=43 the dependency gives t=30 or 29, hence respectively a 6×6 residual with 13 entries, or a 7×7 residual with 14 entries. A 2n+1 support is impossible: its single degree-3 row has neighbors of degree 2, which must use identical two-subsets of its three columns to avoid unique overlaps, leaving one column of degree one. A 2n support has all row and column degrees two and is a union of K2,2 blocks, impossible for odd n. These are universal written arguments; the n=6 and n=7 enumerations are controls. Together with the N=42 analysis, they support the conditional ≥44 argument.

## Reference witness and what remains out of scope

My separate exact parser checked the pinned 36-cell Pandya transcription without the author's checker. It has 60 entries, of which 12 have unnormalized coefficient √2 and 48 have coefficient ±1. For **all three** 36×36 cuts, the numerator matrix and its transpose both have exact Gram `2I` over `Q(√2)`. Therefore, after the stated `1/√72` normalization, the transcription is a 60-support AME witness. This verifies that transcribed tensor; it is not a novelty audit or a re-proof of the classical no-OLS(6) theorem.

Confirmed finite statements: the n=5 obstruction and graph/XOR controls; the n=3–6 support classification with exact realizations; the n=7 two extra support counts; the n=6 residual controls and one exact partial-unitary realization; the exact spin weight arithmetic, with numerical spin-flip checks; and the 60-support transcribed witness. Refuted as a realization count: the unfiltered earlier 1,000 n=5 summary (100 are disconnected rectangular patterns). Not reachable from bounded enumeration alone: all-n generalizations, extension of residual support to a full 36-word OA, the no-OLS(6) import, a formal proof or independent-family review, and novelty/priority.
