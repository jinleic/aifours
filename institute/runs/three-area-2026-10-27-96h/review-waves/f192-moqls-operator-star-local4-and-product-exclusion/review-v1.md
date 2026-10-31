# f192: independent same-harness review of operator-star, LOCAL4 and C4 product stratum

Native clock observed before this write: **2026-10-29T16:53:16Z** (`/bin/date -u`). Reviewer: ReviewF192MOQLSStarProduct. This is a written same-harness review with reviewer-authored exact finite controls, **not** a human, independent-model-family, formal/kernel, source-priority or novelty acceptance. The actual object throughout is four ordinary MOQLS(8), not a relaxed star-cover model.

## Dispositions

`F` = fatal mathematical finding, `M` = major, `m` = minor; counts are per claim. **SUPPORTED** means I reconstructed the written implication under its stated hypotheses and the sole named import, not that a finite diagnostic proves it or that the parent has adopted it. **INCONCLUSIVE** below names statements outside the proven cut.

| Claim | Verdict | Import/dependency |
|---|---|---|
| Per-mate partial tensor resolution, distinct-mate weight disjointness, threefold operator inequality, fivefold intrinsic-star cover and active-cell trace bound | **SUPPORTED; F=0, M=0, m=0** | Ordinary four-MOQLS ONBs only; GAP3 not used. |
| No isolated star ray in a nontrivial component | **SUPPORTED; F=0, M=0, m=0** | Fivefold cover plus **GAP3**. The isolated star ray need not be an intrinsic component. |
| `sigma_u >= r+1` for every actual ray of every intrinsic component with `r>=4` | **SUPPORTED; F=0, M=0, m=0** | Fivefold cover and **GAP3**; direct one-off-direction proof, not an imported generic span theorem. |
| Every actual `u` in an intrinsic C4 has full complex span of its `u`-active rays | **SUPPORTED; F=0, M=0, m=0** | Fivefold cover and **GAP3**, via no-isolated-star. Includes `dim A=1,2,3`, complex phases, coincident-plane and zero-overlap boundaries. |
| Intrinsic C4 real projector span `b>=9` and all-ray equality residual | **SUPPORTED; F=0, M=0, m=0** | Previous two results; therefore **GAP3**. Equality gives exactly `sigma=5`, real cross dimension 3, complex cross span 3, and the displayed entire block-diagonal kernel for every actual ray. |
| Ancillary C5 `b=10` possible dimension pairs | **SUPPORTED; F=0, M=0, m=0** | Same star bound and no-isolation; these necessary pairs do not exclude C5. |
| Arbitrary-complex 2-by-2 product-ONB split classification | **SUPPORTED; F=0, M=0, m=0** | Elementary complex two-dimensional orthogonality; neither GAP3 nor a catalog imported. Rectangular ONBs have both types. |
| Twenty-cell requirements, uniqueness of each factor's split basis, and exclusion of a common-product intrinsic C4 | **SUPPORTED; F=0, M=0, m=0** | Fivefold cover for the counts; **GAP3** for no isolated star and final contradiction. Each one-factor `20+20>32` concerns two distinct bases on the SAME factor. |
| Statement about the `REAL product-projector space` having dimension 9 | **m=1**, wording qualification, not a defect in the product exclusion | Dimension 9 is correct for **real local factors**. The real linear span of projectors of arbitrary complex local factors has dimension 16. See finding m-1. |
| Exhaustion of all C4 `b=9` geometries by one common product factorization; exclusion of arbitrary C4 `b=9` or C5 `b=10`; `LOCAL4>=10`, `LOCAL5>=11`, q4/four-family classicality, M(8), A10 or A11 | **INCONCLUSIVE / not established or claimed here** | Product-stratum exclusion is only conditional on a common product factorization. No other prior gate or solver outcome is adopted. |

**Sole research import, GAP3:** every nonfixed ray in an ordinary four-MOQLS member has global multiplicity at most three. This covers every ray of a component of dimension at least two: a ray occurring eight times occurs exactly once in every actual row, and is perpendicular to every other ray in that row, so its component is one-dimensional. Conversely a one-dimensional component occurs once in every row. Fixed multiplicity-eight rays remain allowed. I do **not** import the prior C2/C3, star, local-span, budget, q4 or any other gate. References in the scoped disposition were not opened.

## Exact frozen inputs, order and read coverage

The manifest was hashed first and matched the assigned SHA. All three full input hashes, byte counts and LF counts were checked before mathematical assessment; then every input was displayed in raw, contiguous short windows, in exactly this order, through its ending. No input-read-order deviation or hidden/elided coverage is claimed. Before the frozen manifest I read only the required runtime memory/skill guidance and directory navigation, not any other task mathematics; this distinguishes the task-input ordering from runtime setup.

| Sequence | Input | Full SHA-256 | Bytes | LF | Actual raw windows |
|---|---|---|---:|---:|---|
| 0 | `manifest-v1.json` | `16d2d7409eefbe8788955c5cd21cc374cce3b4437fe4142d73ac6daf10b749d1` | 3893 | 37 | 1-20, 21-37 |
| 1 | `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-23-96h/MOQLS-unrestricted-four-family-ray-gap-intrinsic-and-local-span-budget-entire-parent-v1.md` | `2e254b56d108994844cf337c31b98fa851effca15a68a847c6cb2db84552bee4` | 9675 | 63 | 1-12, 13-24, 25-36, 37-48, 49-63 |
| 2 | `/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/moqls8/frontier-20261029-operator-star-cover-and-local4-rigidity-v1.md` | `37dbb4c9b0c7464db82c3f59ef6119c2f9d65be850589a02e7e09015cfd61673` | 12138 | 106 | 1-12, 13-24, 25-36, 37-48, 49-60, 61-72, 73-84, 85-96, 97-106 |
| 3 | `/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/moqls8/frontier-20261029-C4-product-component-exclusion-v1.md` | `bfb192d7266c703d413b47cc3f99b5edffe9670b7cd9128d20dc6d0c1f50a01d` | 9922 | 80 | 1-12, 13-24, 25-36, 37-48, 49-60, 61-72, 73-80 |

The pinned prior disposition was read whole only to identify GAP3; the other seven gates were not imported. No linked prior author/reviewer bodies, sibling reviews, held payloads, external sources, author code, or model/API were consulted.

## Independent reconstruction

### 1. Operator identities, all cells, star cover

Let `Q,X1,X2,X3` be four distinct members, with every actual row and column an ONB of `C^8` and all six same-cell pair-product families ONBs. For a fixed cell `y`, with `P_z=|Q_z><Q_z|`, the resolution of the Q-X product ONB, partially evaluated in `X_y`, is exactly

`sum_z |<X_y,X_z>|^2 P_z = I_8`.

The `z=y` term is `P_y`. Every other cell in its row or column has zero X overlap. For any remaining cell not perpendicular in Q, Q-X product orthogonality makes the X overlap zero. Thus the remaining terms are precisely the off-row/off-column perpendicular cells and sum to `I_8-P_y`, including when other overlaps happen to be zero. For any `z!=y`, the three mate-pair ONBs make at most one of the three nonnegative weights nonzero; each is at most one. Consequently their sum `omega_z<=1`, and

`sum_{off-line Q-star} omega_z P_z=3(I_8-P_y)`,
`sum_{off-line Q-star} P_z >= 3(I_8-P_y)`.

For an intrinsic component C with span W of dimension r, the component spaces are mutually orthogonal. Compressing a row/column ONB to W shows every row and column contains exactly r component cells forming an ONB of W. Compress the inequality and add the disjoint row-star and column-star ONBs (each resolves `P_W-P_u`) to obtain

`A_u := sum_{z in C, Q_z perpendicular u} P_z >= 5(P_W-P_u)`.

Since `sum_{z in C} P_z=8P_W`, the complementary nonzero-overlap sum satisfies `T_u<=3P_W+5P_u`; its trace counts **cell occurrences**, yielding `#active<=3r+5`. Nothing is divided by an overlap. If an actual star ray g is perpendicular to every *other distinct* star ray, evaluating along g gives `m(g)>=5`. In a nontrivial C, GAP3 says `m(g)<=3`, a contradiction. For r=1 the star is empty; no claim of a nontrivial component is made.

### 2. Star-span bound, including the low-rank cases

For r>=4 let `d=r-1>=3` and choose the actual row ONB `E=(e_1,...,e_d)` inside `u^perp`. Its real diagonal projector space is in the star span. Suppose the real off-diagonal image has dimension at most one.

* If zero, every rank-one star projector is an E-axis. GAP3 caps each axis's global multiplicity by three, so `A_u<=3I_d`, contradicting the five-cover.
* Otherwise let `v` be a non-axis actual star ray and `X=Off(P_v)`. Every non-axis star ray w has `Off(P_w)=tX` for a nonzero real t. If v has support exactly two, all such w have that same two-coordinate support; an E-axis outside it exists because d>=3 and is an isolated star ray.
* If v has support at least three, equality of off-diagonal zero patterns forces w to have exactly the same support. For each supported i, choose different supported j,k and use rank-one purity:
  `|w_i|^2=(w_i conjugate(w_j))(w_k conjugate(w_i))/(w_k conjugate(w_j))=t |v_i|^2`.
  Normalized representatives give t>0 and then t=1, hence `P_w=P_v`. A unit vector perpendicular to v sees at most 3 from axis contributions and zero from v, again contradicting five-cover.

Therefore the off-diagonal image has real dimension at least two and `sigma_u>=d+2=r+1`. This proof does not assume the star is a union of complete ONBs. The `d=2` case is deliberately not included.

### 3. C4 full complex neighbour span

Let `A=span_C{Q_z:<u,Q_z> != 0}` for an actual u in a four-dimensional intrinsic component. The actual u is in A. Connectedness rules out `dim A=1`: then no distinct ray is nonorthogonal to u.

If `dim A=2`, take an actual mixed x in A. Any u-active ray perpendicular to x is the unique in-plane partner x'; every u-inactive ray perpendicular to x belongs to `A^perp`. A component row through x has three other orthogonal vectors, while `dim A^perp=2`, so x' is actual. It is perpendicular to every other distinct star-x ray, contrary to no-isolation. This also covers the potential degeneracy that x' might have been merely virtual: the actual line forces it.

Suppose `dim A=3`. Write `Pi=A intersect u^perp` and take a unit `pi` perpendicular to A. Every mixed active ray has projective form `u+r lambda`, `r!=0`, with lambda a unit direction in Pi. A pi-active actual ray is u-inactive. For such an x its pi-active star rays lie in `K_lambda=C pi + (Pi intersect lambda^perp)`. Five-cover, tested on pi, gives at least five total pi-weight in each K. Three distinct lambda directions give three planes meeting pairwise only in `C pi`. Across all component cells the total pi-weight is exactly 8; the common pi ray is counted at most three times, with multiplicity at most 3 if actual and 0 if not. Thus three directions imply `15<=8+2m(pi)<=14`. Exactly two directions must occur to span A.

Let their planes be `B1=span(u,lambda1)` and `B2=span(u,lambda2)`. An actual line without u has at least two u-active rays, since the line resolves u and one active vector alone would equal u. It has at most two: among three, two lie in the same Bi, span Bi and hence contain u, forcing all other line vectors u-inactive. With exactly two, expansion of u makes their Pi components cancel, so they lie in the same Bi and are in-plane partners. Therefore every actual mixed Bi ray has its actual in-plane orthogonal partner.

Every u-inactive star ray of a mixed B1 ray x is also perpendicular to x'. If no mixed B2 ray were perpendicular to x, x' would be isolated. Thus a cross-plane partner exists in each direction. Put `kappa=<lambda1,lambda2>`; distinct directions imply `|kappa|<1`, and existence of a mixed cross partner implies `kappa!=0`. For actual `x=u+r lambda1`, the consecutive cross, in-plane, cross, in-plane ratios are

`r -> s=-1/(kappa conjugate(r)) -> s'=conjugate(kappa) r -> t=-1/(|kappa|^2 conjugate(r)) -> r_new=|kappa|^2 r`.

All these rays are actual and mixed. Because `0<|kappa|^2<1`, a finite actual set cannot contain a minimum positive `|r|` and its strictly smaller successor. This is a universal finite-set contradiction, not a numerical orbit argument. The `kappa=0`, `|kappa|=1`, and `r=0` boundary cases have been separated rather than divided through. Hence A=W.

### 4. LOCAL4 and equality; ancillary C5

For Hermitian projector span S define the real-linear off-block map `D_u(Z)=P_u Z P_{u^perp}` and identify its image with `{u chi*:chi in L_u}`. Its kernel contains the direct sum of `R P_u` and the star-projector span, so

`b >= 1+sigma_u+dim_R L_u`.

The off-block images of active projectors have, up to nonzero complex scalars, the u-perpendicular projections of their rays. Full complex active span in C4 therefore gives `span_C L_u=u^perp` and `dim_R L_u>=3`. With `sigma_u>=5`, `b>=9`.

If b=9, equality in all inequalities holds **for every actual u**: `sigma_u=5`, `dim_R L_u=3`, `span_C L_u=u^perp`, and `S intersect BD_u=R P_u direct-sum span_R{P_v:v perpendicular u}`. There is no hidden additional block-diagonal kernel. These are necessary conditions, not a classification of S.

For the packet's ancillary C5 remark, the star argument gives `sigma>=6`. Also `dim_R L_u>=2`: dimension zero would isolate u intrinsically; dimension one would put all active rays in a common complex two-plane through u, and the same forced-partner argument as in C4 gives an isolated star ray. If b=10 the integer inequality leaves precisely `(sigma,dim_R L)=(6,2),(6,3),(7,2)` as necessary numerical pairs. They need not all be attainable and no pair is excluded by this argument.

### 5. Arbitrary complex product stratum

In a product ONB of `C^2 tensor C^2`, start with `a tensor b`. Each of the other three product vectors is perpendicular because its first factor is `a^perp` or its second is `b^perp`. At least two share one alternative. If two have first factor `a^perp`, their second factors are an ONB, so their orthogonal complement is `a tensor C^2` and the remaining two rays are `a tensor b, a tensor b^perp`: an A-split. The B-split case is symmetric. This is valid for arbitrary complex local rays and phases; a rectangular basis satisfies both alternatives.

For any actual A-split line with rays `a tensor b, a tensor b^perp, a^perp tensor c, a^perp tensor c^perp`, test the five-cover at the first two rays along, respectively, `a^perp tensor b` and `a^perp tensor b^perp`. Every nonzero tested star contribution comes from first factor `a^perp`, so adding gives `N_A(a^perp)>=10`. Applying the same argument to the other two rays gives `N_A(a)>=10`, hence the A-split basis consumes at least 20 original C cells. Distinct unordered qubit orthonormal bases cannot share even one projective ray, so two distinct A splitting bases require at least 40 **disjoint** cells, impossible because C has 8 rows times 4 component cells = 32. Likewise there is at most one B splitting basis. Do **not** add the A and B twenty-cell requirements directly: cells can be counted by both.

If there were no A splitting basis, every actual line would use the unique possible B splitting basis, and all actual rays would lie in the two nonzero, mutually orthogonal B sectors; C would not be connected. Similarly B must exist. Fix their local bases and the corresponding rectangular product ONB E. Each actual ray appears in an actual row which is A-split or B-split, so it has support at most two in E. Connectedness of a dimension-four component forces some ray x with support exactly two. A light ray perpendicular to x either is its unique in-plane partner x' or has support disjoint from x's two axes; a one-coordinate intersection cannot cancel. An actual line through x forces x' to occur because the remaining coordinate complement has dimension two, but the line needs three orthogonal companions. All other star-x rays are perpendicular to x', making x' isolated; five-cover and GAP3 rule this out. This proves the product-stratum exclusion for one common, possibly virtual, complex factorization, with no assertion that every `b=9` component has one.

## Finding m-1: distinguish real factors from real span

The product packet's closing phrase `the REAL product-projector space has dimension 3 times 3 = 9` is compatible with its immediately preceding **real-product** geometry, and is unused in the proof. It is ambiguous if `REAL` is read only as describing the scalar field of the span while local factors remain arbitrary complex rays. Real local rank-one projectors span `Sym(2,R)` of dimension 3 per factor, giving 9. In contrast, complex local rank-one projectors real-span `Herm(2)` of dimension 4 per factor; their product projectors real-span dimension 16. The exact control has both ranks. Recommended additive clarification: say **real local factors** for the 9-dimensional example; retain the arbitrary-complex hypothesis for the exclusion. No correction to its mathematical conclusion is required under the real-factor reading.

## Reviewer-owned exact controls and limitations

One bounded, standalone standard-library run, without author code: `python3 -B reviewer-controls-v1.py`. It started `2026-10-29T16:52:21Z`, ended `16:52:23Z`, exit **0**, tool wall time **1.74 s**, deadline **120 s**; 40/40 named checks passed. The time cap was not reached. Script and every input/output hash, native clock and exit are recorded in the receipt. Gaussian-rational/integer arithmetic and exact linear ranks were used; no floating-point scientific result is treated as proof.

* **Actual ordinary-family positive:** four complex-unitarily-rotated classical GF(8) Latin squares; all four actual row and column ONBs, all six 64-product ONBs, all 192 per-mate 8-by-8 operator identities, and 4,032 distinct-cell disjointness cases were checked exactly. This family has only eight one-dimensional intrinsic components with multiplicity eight, **not** a nontrivial C4 example. Its reducible ambient star explicitly shows why GAP3 cannot be applied to fixed rays.
* **Intended-reason family negatives:** duplicate a row entry (row orthogonality); duplicate Q as a mate (Q-mate product ONB, while line ONBs remain); duplicate two mates (mate-mate product ONB and disjoint weights fail, while all three Q-mate ONBs remain). These are rejected as invalid and are not treated as four-MOQLS counterexamples.
* **Partial-resolution mechanism:** a separate complete 2-by-2 product ONB has weights `1,0,9/25,16/25` and gives the identity exactly; removing the last term fails it. This is not a four-MOQLS fixture.
* **Star cone and neighbour mechanism:** support-two single-off-direction data exhibit the isolated third axis and fail five-cover at 3; among 512 finite complex integer rays, all eight with the tested support-three off-direction are the same projective ray. The tested support-three perpendicular vector also sees 3 rather than 5. Exact three-plane pi intersections check the overlap bookkeeping; a duplicate plane fails the required intersection. Six exact complex closure cycles with `kappa=(3+4i)/13` each satisfy all four orthogonality relations and contract by `25/169`; the deliberately missing conjugation fails orthogonality. Finite cycles illustrate, not prove, the universal descent.
* **Product mechanisms:** exhaustive orthogonal quadruples from 36 finite complex product rays give 18 A-only, 18 B-only and 9 both; a nonorthogonal quadruple is rejected. A separate 20-cell partial scalar fixture makes all four displayed P-A tests exactly 5 and both local counts 10; deleting a relevant ray breaks its scalar premise. It is reducible, has only 20 cells, and fails full five-cover along a same-sector direction, so it is not an actual C4 component. An all-light complex partner is isolated and its tested cover is 1, again an intended failure.
* **Residual distinction:** a connected 36-ray real-product finite configuration has real projector span 9; at two actual sample rays it has sigma 5, real cross dimension 3, complex active span 4, and the 6-dimensional block-diagonal kernel. It is **not** a four-MOQLS component: it has 36, not 32, cells and violates five-cover with tested value 3. A removed star sector drops rank from 5 to 3. A separate complex-product rank control gives 16, as in m-1. None of these partial fixtures drops ordinary-family assumptions from the theorem or proves existence/exclusion of a valid nontrivial family.

Artifacts in this directory:

* `reviewer-controls-v1.py` SHA-256 `def54bc429e858b7c3841f7bd1d02378f79da6333ef9f23395c4316b5c494ba5`.
* `reviewer-controls-output-v1.json` SHA-256 `501b35097e9b85d0c8388d79921d41fedc79ab0b466c516bf314750535be0f8c`.
* `reviewer-controls-receipt-v1.json` SHA-256 `e34d58c13e26450de79963f8680bad958606fa92571dcc3a86753b4b44183a40`.

## Exact remaining gap

To reach an unrestricted C4 span-nine exclusion one still needs a justified classification making every admissible `b=9` residual a common-product geometry, **or** an independent obstruction for the remaining nonproduct equality geometries. The present result does neither. C5 `b=10` and any actual-family coupling beyond these necessary local conditions remain unresolved. No q4 exclusion, four-family classicality, M(8), A10/A11, formal proof or novelty result follows here.
