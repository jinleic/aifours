# Independent finite/case-cover review of the complete U13 packet

## Disposition and boundary

**INCONCLUSIVE on U13.** I found no FATAL, MAJOR, or MINOR mathematical defect in the finite checks described below. That is not a finding that the 23 written proofs are valid, and it is not a blanket U13 verdict. The finite incidence cover is exhaustive within the stated bounds; the separate support-cardinality and coordinate-incidence searches are necessary relaxations, not QLS or four-MOQLS realizability tests. Several of their survivor counts remain nonzero. Universal complex-vector arguments, the actual mate-product implications, and the entire dependency chain still require written-proof review.

The explicit exact complex QLS below has 12 mixed cells. It is a countercontrol to a *mutated stronger QLS-only* claim, not to the candidate U13, which requires three mutually orthogonal mates. No mate is constructed or claimed. This is an independent same-harness scientific slice, not independent-family, human, formal/kernel, novelty, publication, or parent acceptance.

## Frozen input, reading, and reconstructed hypotheses

I read `manifest-v1.json` first, then verified the complete source's SHA-256, byte length and LF count before reading **all LF 1–852**. The manifest SHA-256 was `aceb255e826d501b3049eb38604a90d9cad0764dafc673854f1e62fd2c0bd364`; the one source was 142,557 bytes, 852 LF, SHA-256 `2eeda45e6c4396530b856c1aef85816fd84076ecd82e782738ac95aa8d529775`. A live verification clock read `2026-10-28T21:25:44-0700 PDT`. The chapter-specific coverage matrix is below. I did not read or import the sibling proof-review report or its code, or author/sibling executable code.

My reconstruction: an order-8 QLS has a unit vector in each cell, with each row and column an ONB of its own complex eight-space. For every pair of members and distinct cells x,y, pair-product orthogonality gives `<M_x,M_y><N_x,N_y>=0`. Choose any actual row of Q as the coordinate-ray basis. A mixed cell is not a ray from that basis. For a line with k mixed cells, its other 8−k coordinate rays are distinct, so the mixed rays form an ONB of the complementary k-coordinate subspace. Thus a nonempty mixed line has k≥2; its k=2 cells have the same 2-support; and a k=3 line has at most one 2-support cell. Two complex vectors with a single shared nonzero coordinate have nonzero inner product, but an overlap of two or more coordinates can cancel. No chosen local bases of distinct members are identified. Incidence transposition leaves the originally chosen Q basis fixed.

For nonzero mixed count m≤12, the mixed-cell graph therefore has minimum degree two, r,c≤6, and rc≥m. The graph search covers every such r,c, including impossible pairs; the empty m=0 classical case is outside the nonclassical assertion. It canonicalizes permutations of rows and columns and, for square boards, transposition. Labeled counts below refer to labels on the *active* r×c board, not choices of positions in an 8×8 board.

## Complete finite incidence and necessary-relaxation coverage

`finite-controls-v1.py` enumerated nondecreasing row masks and then quotiented column permutations; the diagonal-shape canonicalization also quotiented transpose. It independently checked 26 bounded labeled counts against a direct cell-subset enumerator. The P05 author's six m=10 labeled counts were reproduced as `(1,54,210,2040,2580,2040)` in the claimed shape order. The 5×5 m=10 count is from the row-mask enumerator, not from the bounded ≤20-cell direct subset crosscheck.

The support-size DFS checks only necessary rules: size between 2 and the smaller incident degree, at most one size-2 ray on a 3-line, the relevant 4-line 2/3 prohibitions, disjoint-or-equal packing of 2-supports, and evenness if an entire line has size-2 supports. Separately, the coordinate-incidence DFS uses exact row/column coordinate-projector balance, at least two incident occupied neighbors per coordinate, degree-2 propagation, and some forced full-3 propagation. It enumerates up to eight axes, with pruning. **The two DFSs are separate:** even when both return a witness, their witnesses need not be jointly compatible, much less have complex amplitudes or mates.

| m | all graph orbits | orbits passing both separate necessary tests |
|---:|---:|---:|
| 1, 2, 3 | 0 each | 0 |
| 4 | 1 | 1 |
| 5 | 0 | 0 |
| 6 | 2 | 1 |
| 7 | 1 | 0 |
| 8 | 6 | 5 |
| 9 | 6 | 1 |
| 10 | 20 | 7 |
| 11 | 27 | 2 |
| 12 | 99 | 34 |

This is 162 graph orbits total for m=1,…,12. At m=11 both separate tests survive only on 4×4; this is consistent with the P06 shape reduction, conditional on the line-size facts used by the search. Nonzero numbers in the last column are **not** counterexamples and do not refute any chapter.

For m=12, the complete active-board partition is:

| r×c, up to transpose | labeled graphs | graph orbits | orbits passing both separate necessary tests |
|---|---:|---:|---:|
| 2×6 | 1 | 1 | 1 |
| 3×4 | 1 | 1 | 1 |
| 3×5 | 270 | 3 | 2 |
| 3×6 | 690 | 5 | 2 |
| 4×4 | 1,428 | 7 | 5 |
| 4×5 | 28,770 | 28 | 4 |
| 4×6 | 27,150 | 14 | 5 |
| 5×5 | 242,800 | 26 | 7 |
| 5×6 | 146,100 | 10 | 3 |
| 6×6 | 67,950 | 4 | 4 |

The machine-readable receipt retains every m/r/c entry, even zero shapes, the complete degree-profile tables and the two separate witness types. In particular, these loose relaxations do not test the full support-size/coordinate compatibility of P10's 3×4 case.

### Focus: 4×4 and 5×5

At m=12 define A=`(4,4,2,2)`, B=`(4,3,3,2)`, C=`(3,3,3,3)`. An independently written direct 4×4 cell-subset enumerator reproduced all 1,428 labeled graphs:

| unordered profile pair | AA | AB | AC | BB | BC | CC |
|---|---:|---:|---:|---:|---:|---:|
| labeled graphs | 36 | 288 | 72 | 720 | 288 | 24 |

BB consists of 144 labeled graphs with the degree-2 row/column intersection present and 576 with it absent. The fixed-degree-label P21 enumeration contains one present and four absent graphs. The necessary local support-size rules, **including** the stronger rule that three support-2 rays on a 4-line force its fourth to have support 2, reject all four absent graphs and leave exactly one size assignment for the present graph. This remaining assignment is not a QLS realization. The P21 3-space identity is independently checked below; the finite cardinality result alone does not exclude the present graph. Deliberately removing the three-support-2 rule creates one extra spurious present assignment, with high-line sizes `(4,2,2,2)`; the intended failure is that two rays fill a 2-plane, forcing the fourth ray to avoid that plane, contrary to full 4-support.

For the m=12 5×5 B/B profile, B here means `(3,3,2,2,2)`. A second, independently written direct row-neighborhood enumerator fixes the two high rows and two high columns and checks all 1,486 resulting labeled graphs; 100 choices of those high-line labels give the total 148,600. Its counts agree with the first enumerator:

| reason or boundary type | labeled graphs over all high-line choices |
|---|---:|
| a degree-3 line meets at least two degree-2 lines | 122,500 |
| two paths, vertex counts `(2,6)` | 7,200 |
| two paths, vertex counts `(3,5)` | 14,400 |
| two paths, vertex counts `(4,4)` | 3,600 |
| two 2-paths plus one 4-cycle | 900 |

After the first line is removed, the high/high core is indeed complete and the boundary classification is exhaustive. A 2-path joins two high lines through a common degree-2 line. Their common 2-support and the full-3 high-core rays give the exact 3-space contradiction described below. Thus the two 2-path categories, 8,100 labeled graphs, have this additional QLS-only obstruction, subject to the actual line/support reasoning; no mate is needed for that step. The other 18,000 labeled `(3,5)` and `(4,4)` boundary graphs require the separate actual mate argument, not the graph census. A mutant that omits the two 2-path categories loses exactly 8,100 labeled graphs; omitting the 4×4 BB absent case loses exactly 576.

## Exact projector, cycle, and algebra controls

* **P10 coordinate projectors.** Fix the first 4-axis row set to `{0,1,2,3}` by axis relabeling and enumerate all other 4-subsets of eight axes with repetition. Of 25 row multisets with no singly occupied axis and eligible 3-axis column sets, precisely one balanced model exists: the three row sets coincide, and the four column sets omit the four distinct axes. This is a finite check of the coordinate-projector implication, not of the later no-mate argument. Dropping projector balance admits the recorded unequal row sets `{0,1,2,3}`, `{0,1,2,4}`, `{0,1,3,4}` with four copies of column set `{0,1,2}`; its coordinate counts visibly disagree.
* **P17/P22 projectors.** With a fixed four-axis K, all relevant ordered 2-/3-subsets were enumerated. P17 has 72 balanced ordered models, all forcing distinct omitted axes whose union is U. P22 has 24 balanced ordered models, all forcing `{C1,C2}={TA,TB}`. Dropping the P22 balance permits the explicit repeated `C1=C2=TA` mutant recorded in the receipt.
* **P08/P09/P12/P15 support-cycle bookkeeping.** A separate enumerator considered 721 row-canonical m=12 incidence graphs whose line degrees are 2 or 4 with at least one 4-line, and all line partner pairings. The 1,449 pairings satisfying the necessary condition that the two disjoint support pairs of a 4-line are in different constant-support cycles have cycle partitions `(4,8)` (630), `(6,6)` (489), or `(4,4,4)` (330). This is finite partner bookkeeping, not an actual support assignment or transition-matrix theorem. If the distinct-cycle condition is dropped, the stored 3×6 mutant has one 12-cycle; it is invalid because a single constant-support cycle would have to use both disjoint support pairs on one 4-line.
* **Three-space identity (P11/P12/P14/P21).** In an ONB `u1,u2,z`, with `x1=αu2+βz` and `x2=γu1+δz`, independent formal polynomial expansion gives `<x1,x2>=conj(β)δ`. Full 3-support makes β,δ nonzero, so orthogonality fails. The exact complex unit-vector control gives `16i/25`; dropping one full-support hypothesis gives an orthogonal pair with inner product exactly zero. This illustrates why the nonzero hypothesis is load-bearing.
* **P19/P20 cross-Gram algebra.** For `C=[[0,a],[b,0]]`, formal expansion gives `C* C=diag(conj(b)b,conj(a)a)`. If its two source planes share a unit vector, `||C||=1`; hence an off-diagonal entry has modulus one, so Cauchy equality makes the corresponding unit rays collinear in the intersection. A concrete Gaussian-rational plane pair has cross-Gram `[[0,1],[-7/25,0]]`. The mutation using disjoint planes in C⁴ gives zero cross-Gram and no shared ray: the common-plane hypothesis cannot be removed. The finite control verifies the algebra and example; it is not a formal proof of the geometric application in every P19/P20 case.
* **P16 and final support pigeonholes.** All 16 assignments of the two opposite-corner slots to three mates or to nobody leave at least one mate with neither slot; the two-mate mutant can occupy both. Three nonempty pairwise disjoint supports on two axes have zero assignments; two mates have two assignments, and three axes admit six. These checks do not establish the antecedent pair-product or saturation statements.
* **P07/P21/P23 subgraphs and support sets.** For fixed low-line labels in P07 B/B, all 27 graphs (9 low/low present, 18 absent) and all 99 permitted support-cardinality assignments were checked; the full-3 high/high subgraph is connected in each. For P21's 4-line lemma, all 24 possible 2/3/3 support-pattern choices without single-coordinate overlap split into 12 equal-3-set and 12 distinct-3-set cases; the corresponding vector consequences remain as explained in the source. For P23 the cubic 4×4-minus-matching graph has 108 full-support deletion patterns with remaining minimum degree two: 105 connected and 3 disconnected, each the two K₂,₂ cores. Allowing degree one gives a stored disconnected `(1,3)+(3,1)` mutant. Separately, all 52 overapproximating choices of the five ray-class supports obeying the degree-3 at-most-one-2-support rule have a common coordinate; omitting that rule admits the stored no-common-coordinate mutant. These finite tests do not by themselves prove the continuous cube-ray classification or mate exclusion.

## Actual exact complex-vector countercontrol

The two separately written stdlib checkers generate and independently check the same explicit complex order-8 QLS. All 1,024 row/column Gram entries are checked with Gaussian rational arithmetic, not floating point. Let the first three coordinates carry

`p=(-1,2i,2)/3`, `q=(2,-i,2)/3`, `q'=(2,2i,-1)/3`,

`r=(3q+4i q')/5`, `s=(4i q+3q')/5`,

and embed them in C⁸ by adding zeros. The upper-left 4×4 block is

```
e3  p   q   q'
p   e3  q'  q
r   s   e3  p
s   r   p   e3
```

For local indices i,j=0,…,3, the upper-right and lower-left blocks contain `e_(4+(i+j mod 4))`, and the lower-right block contains `e_(i+j mod 4)`. Row 4 is an actual coordinate ONB in order `[4,5,6,7,0,1,2,3]`; relabeling coordinates by this row gives the stipulated normalization. The 12 off-diagonal cells of the upper-left block are the only mixed cells, all have full 3-support, and the incidence profile is C/C. The two square bases differ: their cross-Gram is `[[3/5,4i/5],[4i/5,3/5]]`.

The targeted mutation replacing the upper-left `q` by the already present `p` is rejected for the intended **row-orthogonality** failure at row 0, cells 1 and 2, with inner product 1; unit norm alone is not the reason. This QLS is a concrete counterexample to the false strengthening “every nonclassical QLS has at least 13 mixed cells.” It is not a counterexample to U13, and it supplies no orthogonal mate, pair-product ONB, or four-family witness.

## Chapter coverage matrix

The ranges cover every source chapter; the right column states what this finite slice checked, not a chapter-wide proof acceptance.

| chapter and LF | finite or algebra slice checked | material still outside this slice |
|---|---|---|
| P01, 56–96 | m≤7 graph minima and size restrictions | actual one-/two-mate dimension and product contradictions |
| P02, 97–139 | bounded all-degree-2 graph shapes and cycle incidence | all complex exclusive-axis/grouping/triangle and transition arguments |
| P03, 140–192 | all m=8 graph shapes and local size rules | 3D completion and actual three-mate pigeonhole |
| P04, 193–233 | m=9 size relaxation leaves the 3×3 board; finite disjoint-support pigeonhole | full-support identification and actual 5D mate saturation |
| P05, 234–306 | all six m=10 shape counts; fixed-high 4×4 boundary gives 8 `(2,4)` and 8 `(3,3)` | arbitrary-complex path/core amplitudes and mate saturation |
| P06, 307–337 | all m=11 non-4×4 shapes fail the implemented necessary size rules | full written justification of every geometric implication |
| P07, 338–392 | 4×4 profiles, both low/low cases, 99 high-core full-support assignments and connectivity | actual 3D rays, QLS completion, mate spans/products |
| P08, 393–418 | finite small cycle pairings and transition-row pigeonhole instance | exclusive-axis hypothesis and general complex transition matrices |
| P09, 419–461 | all six-side incidence profiles and support-2 cycle pairings | bridge of actual mate subspaces and its product support disjointness |
| P10, 462–508 | complete fixed-axis finite projector implication plus mutation | nonzero-coordinate selection and no-mate vector contradiction |
| P11, 509–529 | 3×5 profiles and formal 3-space identity | the full vector reduction for every profile |
| P12, 530–572 | 4×5 graph/profile cover, degree-2/4 cycle partitions, 3-space identity | actual bridge/exclusive-cycle imports and remaining vector steps |
| P13, 573–603 | all 5×5 B/B high/low and boundary graph types | actual path/core mate-ray orthogonality and dimension counts |
| P14, 604–616 | two-path census and formal 3-space identity | its use on actual full-support rays and dependence on P13 |
| P15, 617–639 | complete 5×5 profiles and degree-2/4 partner-cycle partitions | exclusive-axis and bridge implications for actual mates |
| P16, 640–666 | A/A incidence and two-opposite-slot pigeonhole | crossed partitions, simultaneous boundary orthogonality, saturation |
| P17, 667–699 | A/B graph count and all fixed-K projector identity models | derivation of the common K and nonzero-overlap contradiction |
| P18, 700–718 | A/C incidence, 3-space identity | full actual disjoint-support selection and mate dimension argument |
| P19, 719–735 | cross-Gram formal identity and a positive complex example | universal geometric hypotheses, actual transition supports and mate argument |
| P20, 736–750 | cross-Gram formal identity and intersection mutation | proof that its particular planes/rays meet every required hypothesis |
| P21, 751–787 | both B/B low/low graphs, strengthened exact size enumeration, 4-line support sets and 3-space identity | complete continuous support/projection derivation |
| P22, 788–818 | B/C incidence and fixed-K projector identity enumeration | actual full-support projections and final vector saturation |
| P23, 819–852 | cube full-support graph cases; 52 support-set overapproximations; exact QLS countercontrol | general cube-ray classification and three actual mates |

## Reproducibility, receipts, and limits

All scripts are independently written for this slice, use Python 3.14.3 standard library only, and refuse to overwrite their output. Rerun from this review directory with a **fresh** output name, for example `python3 finite-controls-v1.py --out finite-replay-controls.json`; the other scripts have the same `--out` interface. `finite-casechecks-v1.py`, `finite-algebra-v1.py`, and `finite-early-v1.py` also bind the existing first receipt by its SHA. No unbounded solver campaign, model API, author code, or sibling code was used.

| actual run and native clock | code SHA-256 | output SHA-256 |
|---|---|---|
| `finite-controls-v1.py`, 21:30:58–21:31:06 PDT, 8.055 s → `finite-results-v1.json` | `d95cd3f87335c8dc3697cac3c46b0ed5e88e3cf3dabd5820717cd227ff6070e0` | `a4198e71ad26ac718c15d3dce23ef320689043f7090e53a3ecef31005388f91d` |
| `finite-casechecks-v1.py`, 21:33:24–21:33:25 PDT, 1.079 s → `finite-casechecks-v1.json` | `375a8bbf64f255448f0d98c91f951b6b39a3046079e553dab18342830f3be426` | `2c79018a3e6d7aacdeb0c7b672ae56cf58a22ee4be4ba33caafa02ae68992c9b` |
| `finite-algebra-v1.py`, clock 21:34:32 PDT → `finite-algebra-v1.json` | `2eab80d02a7409a4b9f4074bd75fb979c0f194f86992f85dfc8d97a78f4f5623` | `95f72f72ae1dace1b26114bf9db1ec15b56d4175276b7baa9ad9fc4741a85255` |
| `finite-early-v1.py`, clock 21:35:16 PDT → `finite-early-v1.json` | `9b653d17f4e98f6af79068c04050f9cd3d69e529eb172a1f1570347b87784011` | `9345c5eff5af401017604682acf9137114ff5b1bfcf72f014c52cac9a531f02e` |
| `finite-p21-size-v1.py`, clock 21:35:58 PDT → `finite-p21-size-v1.json` | `d4cc83d4c1a2dd534068db9285da8ad81d8fd8b89529ec67c9247d1fb12900fd` | `aac8abbd1119b086b6ab03b7573832f5b36cd6b900c886ac04b5a5741cb157d3` |

The native artifact-hash capture clock was `2026-10-28T21:36:35-0700 PDT`. The counters and mutations in the receipts are reproducible bounded checks, not formal certificates, a search of all complex amplitudes, a proof that surviving relaxations are realizable, an exhaustive mate search, or a global/nonexistence/novelty result.
