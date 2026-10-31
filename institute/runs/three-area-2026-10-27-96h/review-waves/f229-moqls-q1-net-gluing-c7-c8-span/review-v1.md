# f229: q1 five-net, C7/C8 pivots and Gram-range review

Native clock observed before writing: `2026-10-29T14:02:31-0700 PDT` (`/bin/date`). This is a hostile **same-harness written review**, not an author acceptance, parent disposition, independent-model-family, human, formal/kernel, executable-witness, or novelty/priority verification.

## Verdict and findings

**Mathematical verdict: WRITTEN SUPPORTED, conditional on the single adopted GAP3 import**, at the exact q1 cut below. I reconstructed the actual five-net, STAR, uniqueness, mixed-cell matching and rank, the 2-/3-/4-/5-space capacities, the connected/split block pivots and both full-Gram upper bounds. No other foundational statement or f228 result is used. I found no FATAL or MAJOR mathematical defect. This is not a proof of GAP3 itself.

| Claim | Disposition |
|---|---|
| GAP3: nonfixed multiplicity at most 3 | **INCONCLUSIVE as an independent proof**; expressly adopted here, and the only imported mathematical theorem. |
| Five actual net classes, component line resolutions, STAR | Reconstructed; no FATAL/MAJOR/MINOR mathematical defect found. |
| Every nonfixed ray occurs once; L >= 20 and cross rank >= 5 | Reconstructed conditional on GAP3; no FATAL/MAJOR/MINOR mathematical defect found. |
| Distinct-ray capacities 3, 6, 12, 24 in dimensions 2, 3, 4, 5; exclusion of r <= 6 | Reconstructed conditional on GAP3; no FATAL/MAJOR/MINOR mathematical defect found. |
| C7 and C8 two-basis support blocks and lower bounds 17 and 19 | Reconstructed conditional on GAP3; no FATAL/MAJOR/MINOR mathematical defect found. |
| Full 64-by-64 Gram-range bounds C7 b <= 21 and C8 b <= 29 | Reconstructed; applied here conditional on the preceding q1 conclusions and GAP3. No FATAL/MAJOR/MINOR mathematical defect found. |
| Claimed windows and scope | Necessary only, not attained or shown optimal. **INCONCLUSIVE** for existence/nonexistence of q1 and all unaddressed targets. |
| Title's word “sharp” (target line 1) | **MINOR, exposition:** neither endpoint attainability nor optimality of the bounds is established. The body repeatedly says necessary only. Replace “sharp” with “necessary” if restating; do not infer a counterexample or a mathematical contradiction from this title. |

**Process disclosure:** no standalone pre-body/exposure ACK was created. The frozen manifest did not itself request such a file, but the general `aifours-cross-domain-review-wave` / `aifours-written-math-acceptance-protocol` skills describe an ACK before proof-body/arithmetic exposure. Conservatively this is a **PROCESS MAJOR under that broader protocol**, not a mathematical finding; it cannot be cured retroactively, and the parent must decide its procedural effect. No earlier author contact, author preview, sibling finding, or author-code execution was used in this review.

## Frozen inputs, actual read order and scope

The assigned manifest `manifest-v1.json` was the first research artifact. Its measured SHA-256 was `2dcbdc7da98302b8c224b57b8d578da235a50ad7d8d762227a50cf874cf5dfcf`, exactly the assigned full hash. Before displaying either input body, `shasum -a 256` and `wc -lc` measured **both** declared inputs and both matched the manifest:

1. `institute/runs/three-area-2026-10-23-96h/MOQLS-unrestricted-four-family-ray-gap-intrinsic-and-local-span-budget-entire-parent-v1.md`: SHA-256 `2e254b56d108994844cf337c31b98fa851effca15a68a847c6cb2db84552bee4`, 9,675 bytes, 63 LF. Read completely first in raw windows 1-15, 16-30, 31-45, 46-60, 61-63, including its ending. Only its stated Gate 1 GAP3 is adopted; its other reported gates and linked bodies are not premises.
2. `physics/evidence/three-area-20261027-96h/parallel-18/moqls8/frontier-20261029-q1-net-gluing-unique-rays-C7-C8-v1.md`: SHA-256 `3764ed7b169fc082a8db302069e841628d1bf1dfc60f2a9afa0a8ff94f4e88ea`, 19,263 bytes, 201 LF. Read completely second in raw windows 1-15, 16-30, 31-45, 46-60, 61-75, 76-90, 91-105, 106-120, 121-135, 136-150, 151-165, 166-180, 181-195, 196-201, including its ending. All windows were at most 15 lines. No mathematical reasoning or scientific control preceded the complete displays. There is no separately listed erratum input.

Target line references below refer to input 2. The adopted statement is that in an ordinary four-MOQLS(8), any nonfixed ray has global cell multiplicity at most three. The q1 assumptions are that the other three members are classical in their **independently chosen** output bases. No f161/f162 or held body, unlisted linked source, other adopted gate, prior review result, solver outcome, outside search/model/API, or author contact was used. No author code was run, imported, or compiled.

## Reconstruction: actual net, STAR and unique nonfixed rays

Each classical array is Latin on rows and columns. Orthogonality of its pair-product with another classical array makes each ordered symbol pair appear at most once; there are 64 cells and 64 possible ordered pairs, so each appears once. Rows, columns and the three symbol partitions give five classes of eight eight-cell lines, with exactly one intersection between lines of different classes. Two distinct cells share at most one line. A symbol line is a Q-ONB because its two cells have equal classical ray and their Q inner product must vanish. Rows and columns are Q-ONBs by definition. Thus these are **actual** Q lines, not independent auxiliary frames (lines 20-30).

Let W be any Q non-orthogonality component, dim W = r. Its complement consists of orthogonal components. Any actual line's orthonormal Q basis decomposes along those components, so exactly r line entries are an ONB of W. Summing over a class of eight disjoint lines gives `sum_(z in C) P_z = 8 P_W`. For an actual component cell y with ray u, each of the five lines through y supplies an `(r-1)`-ONB of `H = W ∩ u^perp`; their cells other than y are pairwise disjoint. They are a subset of the actual u-perpendicular component cells. Consequently

`A_u = sum_(z in C, Q_z perpendicular u) P_z >= 5(P_W - P_u)`.

This proves STAR directly from the actual five-line geometry, without importing an earlier STAR theorem or assuming the chosen subspace is itself a QLS. A ray occurring in all eight rows is perpendicular to every different ray, hence fixed; conversely a fixed one-dimensional component contributes once to each row, so its ray occurs eight times. Any different ray overlapping a nonfixed u belongs to the same nontrivial component and is itself nonfixed.

For a nonfixed u, GAP3 gives m = 1, 2 or 3 occurrences. Distinct occurrences cannot share a net line. For any non-u cell z, let k(z) count the 5m lines through those occurrences that contain z. It is at most m; each incidence is with a u-perpendicular cell. Each pair of occurrences has 5·4 = 20 intersections of lines of different classes, with same-class pairs disjoint; no such intersection carries u. Counting incidences and pairs, including triple intersections with their correct multiplicity,

`sum k = 35m`, `sum binom(k,2) = 20 binom(m,2)`.

For m=2 there are 20 cells with k=2 and 30 with k=1. For m=3, `n_2+3n_3=60`, `n_1=-15+3n_3`, hence `n_3>=5` and at least `45+n_3>=50` cells are perpendicular to u. The number L of cells with strictly intermediate squared overlap with u is therefore at most 12 for m=2 and 11 for m=3 (lines 40-60).

In each class, the m lines containing u contain no mixed cell; every other line contains at least two, since its Q-ONB expands u and a single nonzero coefficient would be a u occurrence. Thus `L>=2(8-m)`. If a line has exactly two mixed cells x,z, its ONB expansion puts u in the plane spanned by their orthogonal rays; z is the unique ray in `span(u,Q_x)` perpendicular to Q_x. Thus distinct two-entry lines through x produce distinct cells of the **same** nonfixed partner ray. At m=2, L=12 and all unused lines are two-entry, giving five partner occurrences, contradicting GAP3. At m=3, L=10 gives the same contradiction. If L=11, each class has one three-entry line and four two-entry lines; among the 11 mixed cells some meets at most one of the five three-entry lines, because their total incidences are 15. That cell has at least four same-ray partners, again contradicting GAP3. Hence m=1 (lines 61-70).

## Reconstruction: mixed matching, capacities and C6 exclusion

For unique u, write `L=14+s`. In each class at least `7-s` of the seven lines not through u are two-entry. The same partner argument and uniqueness make all such lines a matching on the mixed cells across all five classes: a cell in two of them would yield a repeated nonfixed partner. Therefore `5(7-s) <= L/2 = (14+s)/2`, so `s>=6` and `L>=20` (lines 72-79).

Let `F_u = sum_mixed P_H P_z P_H`. The component resolution and STAR give `F_u <= 3 I_H`. Since the one u cell accounts for one unit of its total overlap 8, the mixed overlaps sum to 7, so `tr F_u=L-7>=13`. The rank p of F_u is the complex span dimension of the H projections of the mixed rays; its nonzero spectrum is at most 3, hence `p>=5`. The real cross image `{P_u Z P_H: Z in S}` has real dimension at least p: its generators are nonzero scalar multiples of those projected rays, and their complex span is the F_u range. If `T_u` is the real span of all actual u-perpendicular projectors and `sigma_u=dim_R T_u`, the cross-map kernel contains the direct sum `R P_u ⊕ T_u`. Thus

`b >= 1 + sigma_u + 5`, and `r-1>=p>=5`.

The latter excludes r <= 5 (lines 80-102); no prior local-span theorem is assumed.

For the capacity proof, all tested rays below are distinct **actual** rays of a nontrivial component and thus have unique occurrence cells. Every projector mass is still counted by actual cells.

* In a two-space B, component resolution gives total B-projection mass 16. For each tested ray v in B, STAR evaluated in the unique B-direction orthogonal to v supplies at least 5 mass from cells perpendicular to v. These contributions for distinct tested rays are disjoint whenever their B-projection is nonzero: a cell perpendicular to both distinct rays has zero B-projection. Therefore at most three tested rays lie in B. If there are three and no orthopair, their three occurrence cells have weight one each and lie outside all three required perpendicular sets, giving mass at least 18, impossible. Thus three contain an orthopair; two different two-ONBs would require four distinct rays, since two 2D ONBs sharing one ray share both. The two-space cap and its orthopair refinement are proved.
* For a three-space D and N tested rays, compressing each STAR and taking trace yields 10N. A cell with nonzero D-projection can be perpendicular to at most three tested rays, because they lie in the two-plane of D perpendicular to its projection. Total D mass is 24, hence `10N<=72` and N<=7. If N=7, let d_i be the orthogonality degrees. At the seven distinct occurrence cells, each with D-weight one, the slack `72-70=2` implies `sum_i(3-d_i)<=2`. This sum is odd because `sum_i d_i` is even, and nonnegative, so it is exactly 1: six vertices have degree 3 and one degree 2. The three neighbors of a degree-3 vertex lie in a two-plane and, by the refinement, contain exactly one orthopair; every such vertex lies in exactly one triangle, while the degree-2 vertex lies in at most one. Thus triangles are disjoint. Covering the six degree-3 vertices requires two disjoint triangles, which use all six and leave the degree-2 vertex out. Each triangle is a 3D ONB. Their six third-edge endpoints can use at most two edges to the seventh vertex, so there must be at least two cross-orthogonality edges between the two bases. A 3-by-3 unitary between bases with no shared ray cannot have two zeros: two in a row/column force a singleton, and if they are in different rows/columns those rows have just one possible common nonzero entry, forcing another zero and then a singleton. Contradiction. Hence c_3<=6 (lines 107-119).
* For any d-space D, compress STAR for every tested ray and sum. A cell with nonzero projection has its perpendicular tested rays in a (d-1)-space, so `5(d-1)N <= 8d c_(d-1)`. With c_3=6 this gives c_4<=12 and c_5<=24. The derivation uses projection mass, not a fictitious subspace QLS (lines 121-124).

If r=6, the five actual lines through u contain 25 distinct other component cells, all in its five-dimensional perpendicular space. Uniqueness makes their rays distinct, contradicting c_5<=24. Thus every nontrivial component has r=7 or 8, and two cannot fit in dimension 8. For r=7 the orthogonal complement is one fixed ray; for r=8 there is none. A classical Q remains allowed (lines 126-132).

## Reconstruction: C7/C8 pivots and lower spans

Fix any actual u in the surviving component. Each line through u supplies an ONB of H of size h=r-1; the five bases are pairwise ray-disjoint by uniqueness. For two such bases E,F, form the bipartite graph of nonzero transition coefficients. Unitarity makes each connected component a square block. A 1-block would be a shared ray; a 2-block would give two different actual two-ONBs in the same plane, both impossible by the preceding reconstruction. Therefore h=6 permits only `6` or `3+3`; h=7 permits only `7` or `4+3` (lines 137-143).

For a self-adjoint operator diagonal in both bases, a nonzero transition coefficient equates the corresponding E and F eigenvalues. Connectedness therefore forces one independent real eigenvalue per support block; conversely a block scalar is diagonal in both bases. If there are g blocks, `dim(D_E ∩ D_F)=g` and hence `dim(D_E+D_F)=2h-g`. These are spans of actual star projectors and lie in T_u (lines 145-148).

* **C7:** if b<=16, the cross-kernel inequality gives sigma_u<=10. The connected block would contribute 11 dimensions and is impossible. In the 3+3 case the pivot contributes exactly 10, so it equals all of T_u. Every actual star projector is consequently block diagonal in the 3+3 decomposition. A rank-one block-diagonal projector is supported wholly in one block. In either 3-block, the trace of A_u is the number of distinct supported star rays, at most c_3=6, while STAR requires trace at least 5·3=15. Contradiction: b>=17.
* **C8:** if b<=18 then sigma_u<=12. The connected seven-block would contribute 13. A 4+3 pivot contributes 12 and exhausts T_u, so every actual star ray lies in one block. In the 3-block the trace is at most 6, contradicting the STAR lower bound 15. Thus b>=19.

The trace cap uses **actual** star cells, uniqueness and the independently reconstructed 3-space capacity; no counting of a virtual basis or unproved global capacity is involved (lines 151-159).

## Reconstruction: full Gram-range upper spans

Let G be the 64-by-64 real Gram matrix of all Q projectors, with rank a. Since the sum on every actual net line is the identity, `G h_l = 1`, and summing a whole net class gives `G 1 = 8·1`. Let `J=11^T/64`, and let R_j be the averaging projection onto functions constant on the eight lines of class j. Their pairwise products are J. The five seven-dimensional contrast subspaces and the constant are mutually orthogonal, so

`E = I - sum_j R_j + 4J`

is the projection of rank 28 onto their common complement. G kills the 35 contrasts and contains the constant in its range. If R is the orthogonal range projection of G, then `P=R-J` is a subprojection of E, and `Z=E-P` is a projection of rank `28-(a-1)=29-a`. Thus a<=29; in C8, b=a, giving b<=29 (lines 162-172).

In C7, the eight occurrences of the fixed ray form a transversal of every class, leaving 56 component cells. G and its range projection R are block diagonal across these two sets. For component x and fixed y, `P_xy=-1/64`, and at most one of the five net classes contains both cells. Thus the off-diagonal block X of Z has entries `-3/64` for a collinear pair and `5/64` otherwise. Each x is collinear with five distinct fixed cells and noncollinear with three. Therefore

`||X||_F^2 = 56(5·9+3·25)/4096 = 105/64`.

Writing B for Z's component principal block, the projection identity gives `XX*=B-B²`; since 0<=B<=I, each squared singular value of X is at most 1/4. Also `rank X<=rank Z=29-a`, whence `29-a >= ceil(4·105/64)=7`. The full span splits orthogonally as the component projector span plus the fixed-ray span, so `a=b+1` and b<=21 (lines 174-188).

An independent exact incidence reconstruction reaches the same rank conclusion without the singular-value inequality. Let D be the 56-by-8 zero-one collinearity matrix between component and fixed cells. Every row has five ones. Each fixed cell is collinear with 35 component cells. Two distinct fixed cells share no net line, and their 5·4 intersections from different classes give exactly 20 common component cells. Hence `D^T D = 15 I_8 + 20 1_8 1_8^T` and `64X=5 1_56 1_8^T-8D`. It follows that

`X^T X = (15/512)(8 I_8 - 1_8 1_8^T)`.

Thus X has rank exactly 7 and squared singular values 15/64 with multiplicity 7; `rank Z>=7` directly. This is a universal deduction from the five-net and fixed transversal, not a separate existence or optimality proof.

## Bounded exact control and its limits

The reviewer-owned `reviewer-exact-check.py` has SHA-256 `9e441fe7aba27d1017d13e1e20444036e735d7fb9ca4e21f76e508240606195b`. It was run once with a 120-second subprocess cap, start `/bin/date` `2026-10-29T14:01:43-0700 PDT`, end `/bin/date` `2026-10-29T14:01:43-0700 PDT`, elapsed 0.065 s, exit 0, empty stderr. It uses no author code. It constructs an abstract GF(8) five-net and transversal, verifies row/column/pair collinearity counts 5/35/20, the exact cross-Gram identity, rank 7 and norm 105/64; rational Householder block examples give projector-sum ranks 11, 10, 13 and 12 for blocks 6, 3+3, 7, 4+3. Three intended-reason negatives actually rejected: a flipped incidence failed `row-incidence is not five`; a changed cross entry failed `scaled cross-Gram mismatch`; a connected-six-as-rank-ten assertion failed `connected six-block is not split rank ten`. These are small exact examples/mutation controls, not universal proofs, a replay of author code, an MOQLS witness, or an executable acceptance. The universal arguments are written above.

## Exact residual and handoff

Conditional on GAP3 and the stated q1 assumptions, a nonclassical Q has exactly one nontrivial component, either `C7 + one fixed ray` with `17<=b<=21`, or `C8` with `19<=b<=29`. These are **necessary ranges only**: the argument does not construct any value, show either endpoint attainable, or establish optimality. Actual complex phases, all other cells, all five net ONBs and all pair-product constraints still have to glue in one object. The q1 witness-or-nonexistence question remains OPEN; there is no unrestricted-four-family, q2/q3, M(8), maximum-three, A10/A11, novelty or priority conclusion. Historical scopes and previously recorded process findings are not changed by this review.

The full review SHA-256 is measured after writing and supplied out of band to the parent; it is not self-embedded in the hashed file.
