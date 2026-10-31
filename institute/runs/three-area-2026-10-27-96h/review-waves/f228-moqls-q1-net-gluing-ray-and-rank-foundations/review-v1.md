# f228 same-harness review: five-net uniqueness, actual-ray capacities and C2–C6

Review observation before writing: `2026-10-29T14:02:25-0700 PDT`, from `/bin/date`. This is a same-harness written mathematical review, not an independent-model-family, human, formal/kernel, executable-proof, novelty or parent acceptance. It reviews the complete pinned packet but gives the primary verdict only at the scoped five-net/C2–C6 cut. GAP3 is an **adopted conditional import**, not independently proved here.

## Finding and claim disposition

At the stated q1 interface and conditional on GAP3, I reconstructed the primary argument below and found **no FATAL, MAJOR or MINOR mathematical defect**. In particular, no hidden multi-intersection, multiplicity, repeated-ray, rank or finite-dimensional degeneracy invalidated the asserted no-intrinsic-C2-through-C6 conclusion. This is a scientific reviewer assessment for parent disposition, not adoption. Findings apply separately as follows:

| Claim | Disposition at this review cut |
|---|---|
| Five physical classes, actual component resolutions and STAR | No FATAL/MAJOR/MINOR found; reconstructed from the original ONBs. |
| `m=2,3` incidence bounds, including triple intersections | No FATAL/MAJOR/MINOR found; reconstructed exactly. |
| Every nonfixed Q-ray has multiplicity one | No FATAL/MAJOR/MINOR found, **conditional on imported GAP3**. |
| Mixed-cell matching and `L>=20` | No FATAL/MAJOR/MINOR found, after multiplicity one. |
| Covariance range rank `p>=5` and cross-map rank | No FATAL/MAJOR/MINOR found. |
| Actual-ray capacities in dimensions 2, 3, 4 and 5 | No FATAL/MAJOR/MINOR found; distinct-ray count and all-cell mass are kept separate. |
| No intrinsic C2, C3, C4, C5 or C6 at this q1 interface | No FATAL/MAJOR/MINOR found in the written deduction, conditional on GAP3. |
| C7/C8 lower/upper span windows | **Secondary inspection only:** selected algebra is reconstructed in Section 7 and no counterexample was found; this is not an independent disposition of those intervals or their realization. |
| Full q1 existence/nonexistence, realization of any C7/C8 span, phases and global gluing | **INCONCLUSIVE / unreviewed**. No assertion of either existence or nonexistence is made. |

No f218 transfer, other adopted gate, classicality premise for Q, external theorem about small components, solver outcome, author code, linked source, author receipt or sibling review is used. No LL, T2 or cyclotomic source is used or silently imported.

## 1. Freeze, measurements and actual source display

The first research artifact was the assigned manifest. Its measured whole SHA-256 was `39c795c6998a54324ed13b0e1590bbf48c1ed326cb73e6a7085d643f09513577`, exactly as assigned. Before opening either input body, the following were measured and compared to the manifest; all three fields matched for **both** inputs:

1. `institute/runs/three-area-2026-10-23-96h/MOQLS-unrestricted-four-family-ray-gap-intrinsic-and-local-span-budget-entire-parent-v1.md`: SHA-256 `2e254b56d108994844cf337c31b98fa851effca15a68a847c6cb2db84552bee4`, 9,675 bytes, 63 LF. Only its explicitly adopted Gate 1 GAP3 is a mathematical premise here.
2. `physics/evidence/three-area-20261027-96h/parallel-18/moqls8/frontier-20261029-q1-net-gluing-unique-rays-C7-C8-v1.md`: SHA-256 `3764ed7b169fc082a8db302069e841628d1bf1dfc60f2a9afa0a8ff94f4e88ea`, 19,263 bytes, 201 LF. This is the full target, not an adopted result.

Complete bodies were then displayed in manifest order, in the following **actual raw windows**, with both endings displayed, before any mathematical reasoning or scientific control:

- GAP3 source: `1–15`, `16–30`, `31–45`, `46–60`, `61–63`.
- Target: `1–15`, `16–30`, `31–45`, `46–60`, `61–75`, `76–90`, `91–105`, `106–120`, `121–135`, `136–150`, `151–165`, `166–180`, `181–195`, `196–201`.

The manifest itself was read in raw windows `1–15`, `16–30` after its assigned hash was matched. No body or linked research source was opened before both input measurements were completed. No author code was run, imported or compiled.

## 2. Physical net and component identities

For each classical member, its basis labels occur once on each row and column. Orthogonality of each pair of classical members' same-cell product basis makes each ordered label pair occur at most once, hence exactly once among 64 cells. Consequently row, column and the three symbol partitions form five actual classes of eight lines of size eight; lines of different classes meet exactly once, and two different cells lie on at most one line.

The Q entries on each of these lines are an ONB: for rows and columns by definition, and for a symbol line because the corresponding classical factor is constant and the Q/classical product vectors are orthogonal. This is a statement about the original cells, not an auxiliary affine completion or an assumed common output basis.

Let `C` be a nontrivial Q nonorthogonality component with span `W`, `dim W=r`. All rays outside `C` are orthogonal to W. Compressing any line's Q resolution to W shows that exactly `r` of its cells lie in C and form a W-ONB. Summing eight rows gives `sum_{z in C} P_z=8P_W`. For an actual C-cell y carrying u, the five lines through y have no other common cells. Each contributes `P_W-P_u` on its C-cells perpendicular to u; all other terms are positive. Thus the actual-cell operator inequality is

`A_u := sum_{z in C, Q_z perpendicular u} P_z >= 5(P_W-P_u)`.

A fixed singleton ray appears once per row and hence eight times; any ray different from u but overlapping u belongs to the same nontrivial component as u and is nonfixed. These statements also cover r=2 and all repeated occurrences; none assumes generic positions.

## 3. Multiple occurrences, exact intersections and partners

By imported GAP3 a nonfixed u has multiplicity `m=1,2,3`. Its occurrences cannot share any physical net line. For a cell z not carrying u, `k(z)` is the number of the `5m` lines through the occurrences containing z. Since two cells share at most one line, `0<=k(z)<=m`. The `m` copies of u themselves lie on no line through another occurrence.

Each occurrence contributes `5*7=35` incidences. For each pair of occurrences there are exactly 20 cross-class line intersections (the five equal-class pairs are disjoint), and each common point contributes one pair of its incident occurrence-stars. This remains true if three or more such intersections coincide. Therefore

`sum k(z)=35m`, and `sum binom(k(z),2)=20 binom(m,2)`.

Every z with `k(z)>0` is orthogonal to u. Writing `n_j=#{z:k(z)=j}` and including the `64-m` non-u cells:

- `m=2`: `(n_0,n_1,n_2)=(12,30,20)`, so at least 50 cells are perpendicular and at most 12 are mixed.
- `m=3`: `n_1=3n_3-15`, `n_2=60-3n_3`, `n_0=16-n_3`; nonnegativity gives `5<=n_3<=16`. The perpendicular union is `45+n_3>=50`, so at most 11 cells are mixed. These are necessary count possibilities, not an assertion that every one is geometrically realizable.

In each class the `m` u-lines have no mixed cells. The other `8-m` lines have at least two: the squared u-overlaps along the ONB sum to 1, and exactly one nonzero overlap would force another copy of u on that line. Thus `L>=2(8-m)`.

If a line has exactly two mixed cells x,z, the expansion of u in its ONB lies in `span(Q_x,Q_z)`, with both coefficients nonzero. The ray at z is therefore the unique ray in `span(u,Q_x)` orthogonal to Q_x. The partner differs from and overlaps u, hence is nonfixed. Different net lines through x have distinct partner **cells**, even when their partner rays coincide.

For `m=2`, `L=12`, so all six other lines of every class have exactly two mixed cells. Each mixed x has five distinct cells carrying its same nonfixed partner, contradicting GAP3. For `m=3`, `L=10` gives the same contradiction. At `L=11`, each class has precisely four two-entry lines and one three-entry line. The five three-entry lines contribute only 15 mixed incidences, so at least one of the 11 mixed cells is on at most one of them. Its other at least four lines have the same nonfixed partner at four distinct cells, again contradicting GAP3. Thus `m=1` for every nonfixed Q-ray. The proof does not assume the intersections are all different or the nonzero overlaps equal.

## 4. Matching, covariance, cross rank and small components

For a now-unique nonfixed u, each class has seven lines not containing u, each with at least two mixed cells. Write `L=14+s`, `s>=0`. In each class the total excess over two is s, so at least `7-s` of the seven lines are two-entry. A mixed cell cannot lie on two such lines: the partner argument would make two distinct cells carry the same nonfixed partner ray, contrary to uniqueness. Thus those lines form a matching across **all** five classes. If T is their number,

`5(7-s)<=T<=L/2=(14+s)/2`, hence `11s>=56`, `s>=6`, `L>=20`.

Let `H=W intersect u-perp`. Since the C-resolution is `8P_W`, the unique u-cell contributes one to the u-diagonal, and the u-perpendicular cells contribute zero, the mixed u-overlap squares sum to 7. Define

`F_u=sum_{z mixed} P_H P_z P_H=8I_H-A_u|_H <=3I_H`.

Thus `tr F_u=L-7>=13`. If `p=rank_C F_u`, positivity and the operator bound give `13<=3p`, so `p>=5`. In the real span `S=span_R{P_z:z in C}`, the cross-image of `Z -> P_u Z P_H` is generated by nonzero scalar multiples of the H-projections of the mixed rays; its complex span is exactly `range(F_u)`. Hence its real dimension is at least p. The kernel contains both `R P_u` and the real span `T_u` of u-orthogonal C projectors, in direct sum. Therefore `b:=dim_R S >= 1+dim_R T_u+5`. In particular `p<=dim_C H=r-1`, so `r>=6`. This rules out intrinsic C2–C5; zero projections, arbitrary phases, and real/complex rank distinctions do not evade the inequality.

## 5. Actual-ray capacities and intrinsic C6

All capacities here count distinct actual rays of the nontrivial C in a chosen subspace; the mass sums still count **all original cells**. For any `D subset W`, the C-resolution gives `sum_z ||P_D Q_z||^2=8 dim(D)`.

### Two-space

Let B be two-dimensional. For each distinct tested actual ray v in B, STAR(v) evaluated on the unique direction in B perpendicular to v yields at least five units of B-projection mass from cells perpendicular to v. For different v these positive-projection cell sets are disjoint: a B-projection orthogonal to two distinct B-rays is zero. Since total B-mass is 16, there are at most three distinct actual rays in B. If there are three and no orthogonal pair, their three actual occurrence cells each have B-mass one outside **all** three target sets, giving at least `15+3>16`, impossible. Thus any three contain an orthopair; the remaining ray is nonorthogonal to both and is unique. In particular two different unordered actual two-ONBs would require four distinct rays and cannot occur in B.

### Three-space

Let D be three-dimensional with N distinct tested actual C-rays. Compress STAR for each to D and take traces; each requires 10. For a cell of nonzero D-projection, all tested rays perpendicular to it lie in its D-orthogonal two-plane, which contains at most three actual rays by the two-space result. The total projection mass is 24, so `10N<=3*24`, `N<=7`.

If N=7, let d_i be the number of orthogonal neighbors of tested ray i. The slack `72-70` is at most 2. At the seven distinct tested-ray cells, projection mass is one, so `sum_i(3-d_i)<=2`. Each `d_i<=3`; the sum of degrees is even, and `21-sum d_i` is odd. The deficit is exactly one: six vertices have degree 3 and one has degree 2.

The three neighbors of each degree-3 vertex are actual rays in a two-plane, so they have an orthopair; in a two-plane three distinct rays have at most one orthopair. Thus each degree-3 vertex belongs to exactly one orthogonality triangle, and the degree-2 vertex to at most one. Triangles are disjoint. Covering all six degree-3 vertices forces exactly two triangles, with the degree-2 vertex outside. Each triangle is an actual three-ONB. The six triangle vertices have six edge endpoints left after their two internal edges; the outside vertex can absorb at most two, so at least two edges join the two ONBs.

Two disjoint three-ONBs cannot have two orthogonal cross-pairs. Their 3-by-3 transition matrix is unitary with no shared basis ray. Two zeros in a row or column leave a singleton, forcing a shared ray. If the two zeros occupy different rows and columns, those two rows have only one common possible nonzero position; their orthogonality forces another zero and hence a singleton. Contradiction. Thus `N<=6`. This argument does not assume real vectors or nonzero generic matrix entries.

### Four-/five-spaces and C6

For any d-space D containing N actual distinct C-rays, the same compression yields `5(d-1)N <= 8d*c_(d-1)`, where `c_(d-1)` bounds distinct actual rays in any `(d-1)`-space. Applying `c_3<=6` gives `c_4<=floor(32*6/15)=12`; then `c_5<=floor(40*12/20)=24`. Nonzero projections ensure the perpendicular tested rays lie in a genuine `(d-1)`-space, and zero projections contribute zero mass.

If `r=6`, the five physical lines through an actual u give five six-ONBs of W. Their other component cells total `5*(6-1)=25`; these cells are pairwise distinct by the net and their rays are pairwise distinct by uniqueness. All lie in the five-space `W intersect u-perp`, contradicting `c_5<=24`. Together with `r>=6`, no intrinsic C2–C6 remains. Any nonclassical Q consequently has one nontrivial C7 or C8 component; if C7, its one-dimensional complement is fixed. This is a necessary dimension statement only.

## 6. Independent, bounded integer controls and process deviation

These controls were authored in this review directory after the complete source displays; neither imports, runs, copies or compiles author code. They are supplementary checks, not quantum realizability or formal proof.

- `reviewer-f228-exact-controls.py`, final measured SHA-256 `b9ee8dede847d44440d0c3a8407824aee486e4665a9c5d7cf72136b48dc7889d`: `/bin/date` start `2026-10-29T14:01:14-0700 PDT`, end `2026-10-29T14:01:16-0700 PDT`, exit 0, 120-second cap. The exact incidence equations gave `(12,30,20)` for m=2 and `5<=n_3<=16`, maximum `n_0=11`, for m=3. Matching bounds rejected every `s=0,...,5` and did not exclude s=6. Of 810 labeled 7-vertex graphs with degrees `(3,3,3,3,3,3,2)`, 180 satisfied the local triangle condition; all 180 had exactly two cross-edges between the two disjoint triangles. Intended-reason negatives rejected wrong incidence total, negative counts, reused matching cell, self-edge, wrong graph degree sequence and the degree-three-neighbor condition.
- `reviewer-f228-unitary-support.py`, measured SHA-256 `0ce3dbac4423540c4764c37f2a77758b769ce50c5dca0e3f805c28d1a93d5270`: start and end `2026-10-29T14:02:07-0700 PDT`, exit 0, 120-second cap. Across all 512 3-by-3 support patterns, the necessary no-singleton and no-single-common-overlap conditions permitted one zero-free and nine one-zero patterns, no pattern with two or more zeros. Intended-reason negatives rejected a singleton row and a pair of rows with exactly one common nonzero. Necessary support conditions alone do not establish unitary realizability.
- **Process deviation, retained honestly:** the first run of the first control, then SHA-256 `12cf3c2c335ab5aaa0b6508ddfd7e6297ad572f085e6b9fbb17627cb0924fa94`, started and ended `2026-10-29T14:00:51-0700 PDT`, exit 1. The system Python lacked `int.bit_count`; its graph part was **incomplete/UNKNOWN**, not a pass. The owned control was changed to use `bin(...).count('1')`; the complete corrected run and its separate hash/receipt are above. Neither this runtime compatibility failure nor its partial output is mathematical evidence.

## 7. Separate C7/C8 inspection; exact residual

This section is secondary counterexample inspection, not an independent acceptance of the complete C7/C8 packet or a resolution of q1. On the assumptions already reconstructed, I found no counterexample to the following algebra:

- Five star ONBs in `H` are pairwise ray-disjoint. For two of them, a transition-support component with one ray per side would be a common ray; one with two per side would be two different actual two-ONBs in a plane, prohibited above. Unitarity makes each support block square. Consequently the only possible block partitions are `6` or `3+3` for C7, and `7` or `4+3` for C8. The intersection of the two real diagonal algebras has dimension equal to the block count, so their sum has dimension `2 dim(H)-g`.
- If `b(C7)<=16`, the cross-rank inequality gives `dim T_u<=10`; the connected 6-block already needs 11, while a `3+3` pair fills a 10-dimensional T_u. Every star projector is then block diagonal and, being rank one, its ray is in one 3-block or the other. At most six distinct rays/cells can occupy a 3-block, whereas STAR demands trace at least 15 there. This gives the packet's lower bound 17. The same argument for C8, using `dim T_u<=12` and block `4+3`, gives lower bound 19.
- For the upper spans, each of the five line-contrast spaces has dimension 7 and distinct contrast spaces are orthogonal. The constant plus these 35 contrasts leaves a rank-28 complement E. Q's projector Gram matrix G kills all contrasts and contains the constant, so its range dimension `a<=29`. For C8, `a=b`.
- For C7, the fixed ray has exactly one cell on every line. With `R` the **actual range projection** of G, `P=R-J` and `Z=E-P`, the C/f off-block entry of Z is `5/64-1/8` on the five collinear fixed cells and `5/64` on the remaining three. Thus its squared Frobenius norm is `56*(5*9+3*25)/64^2=105/64`. Since Z is a projection of rank `29-a`, its off-block X has `||X||_F^2<=rank(X)/4<=rank(Z)/4`, implying `29-a>=7`, `a<=22`, and `b=a-1<=21`.

These observations do not prove existence of a C7 or C8 configuration, eliminate either case, validate all physical phases or complete global gluing. No full q1 conclusion, novelty or cross-case transfer is authorized by this review.

## 8. Output integrity and boundaries

Only this review and the two reviewer-prefixed control files were written in the assigned wave directory. No Git, deletion, publication, infrastructure mutation, external search/model/API, unpinned source, author contact, solver, author-code execution, build, lint, formatter or test suite was used. The complete review-file SHA-256 is measured **after** the file is closed and reported to the parent with the handoff; it is not self-embedded.
