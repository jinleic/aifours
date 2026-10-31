# Independent same-harness review: no intrinsic C4

**Disposition: WRITTEN_SUPPORTED at the frozen C4 cut, conditional on the expressly adopted GAP3. F=0; M=0; m=0; INCONCLUSIVE in-scope items: none.** This is a review recommendation, not a parent adoption. The review does not address the separate q4/original/M(8)/maximum-three/A10/A11 claims or transfer any f192 verdict.

Native clock observed before writing this review: **2026-10-29T13:17:01-0700 PDT** (`/bin/date`). It is a preceding observation, not a claimed file-creation time.

## Frozen inputs and actual sequence

The first research artifact opened was the wave manifest. Its full measured SHA-256 is `da5a17043bdec8734da4c57da4d7f51e06f68361c89a696986fc6e4a9a2db363`; the supplied task gave the prefix `da5a17043bde`, which matches. No full manifest hash was supplied independently, so a full-hash equality to a supplied value is not asserted. The initial manifest display truncated its requirements line; that line was subsequently read raw and complete. Before reading either input body, I measured both input hashes, bytes, and LF counts. They matched every value in the manifest:

| Order | Frozen input | Measured SHA-256 | Bytes | LF |
|---|---|---|---:|---:|
| 1 | `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-23-96h/MOQLS-unrestricted-four-family-ray-gap-intrinsic-and-local-span-budget-entire-parent-v1.md` | `2e254b56d108994844cf337c31b98fa851effca15a68a847c6cb2db84552bee4` | 9675 | 63 |
| 2 | `/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/moqls8/frontier-20261029-no-intrinsic-C4-complete-v1.md` | `27a4eb72c3f437cda04ace937dc75dfa331851afb847561bd8fc28854c52137d` | 8391 | 88 |

After measurement I displayed every declared body completely, serially in manifest order, in these actual `:raw` line windows, including their endings:

* Prior disposition: `1-12`, `13-24`, `25-36`, `37-48`, `49-60`, `61-63`.
* Candidate: `1-12`, `13-24`, `25-36`, `37-48`, `49-60`, `61-72`, `73-84`, `85-88`.

Only after both complete reads did I reconstruct the mathematics and write/run the independent controls below. The general independent-review procedure was consulted as process guidance, not as mathematical evidence; its external-model procedure was not invoked. Linked bodies, author code and receipts, prior or sibling reviews, external sources and model calls were not used as evidence.

## Per-claim assessment

All counts below are findings at the stated in-scope claim, not assertions of existence of a four-MOQLS family or a C4 example.

| Claim | F | M | m | INCONCLUSIVE | Disposition |
|---|---:|---:|---:|---|---|
| A putative intrinsic C4 yields 32 component cells, four in each row/column, and `sum P_z = 8 P_W` | 0 | 0 | 0 | No | Supported; orthogonal component decomposition and actual ONBs give it. |
| Three mate completeness and pair-product orthogonality imply the five-fold STAR operator bound and at least 15 star cells | 0 | 0 | 0 | No | Supported by the independent contraction and disjoint-weight proof below. |
| Every complex two-plane has at most three distinct actual component rays; three have an orthopair and the unpaired third has global multiplicity one | 0 | 0 | 0 | No | Supported; virtual target directions are handled explicitly. |
| GAP3 plus the 15-cell bound forces every actual C4 ray to have multiplicity one | 0 | 0 | 0 | No | Supported; the row counting and two-plane bridge are reconstructed below. |
| Every complex three-space has at most seven distinct actual component rays | 0 | 0 | 0 | No | Supported by the exact trace/incidence double count, including zero projections. |
| The 15 distinct star rays versus three-space capacity 7 exclude any intrinsic C4 in any member | 0 | 0 | 0 | No | Supported conditional on the specified GAP3 import. |
| Candidate §7's separate b9 terminology, C5-union/q4 composition, original-target/maximum and other named-program statuses | — | — | — | Out of scope; not assessed | No conclusions or verdict transfers are made about these. |

## Independent written reconstruction

### 1. Setting, component and import

For each member every actual row and column is an orthonormal basis of `H = C^8`, and for every two distinct members the 64 same-cell tensor products form an orthonormal basis of `H tensor H`. Hence at distinct cells `y,z`, for distinct members `M,N`, `⟨M_y,M_z⟩⟨N_y,N_z⟩=0`. These are the ordinary four-MOQLS hypotheses, not additional imported theorems.

Suppose one member `Q` has an intrinsic irreducible component `C` of complex dimension four; let its span be `W`. Intrinsic components are the orthogonal blocks of the nonorthogonality relation on rays. Thus every entry belongs to one block and all entries from different blocks are orthogonal. Write `q_z` for a unit `Q` representative at cell `z`, `P_z=|q_z⟩⟨q_z|`, and `P_W` for the projector on `W`.

Compress the resolution of any actual row (or column) to `W`: entries outside `C` vanish and the remaining entries are mutually orthogonal unit vectors resolving `P_W`. Exactly four remain. Over the eight rows there are 32 original component-cell occurrences, and

`sum_{z in C} P_z = 8 P_W`.  (1)

All occurrences of the same ray belong to this one component: two identical rays are nonorthogonal. A ray occurs at most once in each actual row and each actual column. If it occurred eight times, every row would contain it, making all other distinct `Q` rays perpendicular to it. It would therefore be a singleton intrinsic component, impossible inside the four-dimensional irreducible block. The sole adopted theorem, the pinned parent disposition's Gate 1 **GAP3**, says every nonfixed ray has global multiplicity at most three; hence every `C` ray has `m <= 3`. Neither the parent budget, C2/C3/C4 bounds, its separately adopted STAR, nor any linked body is imported. STAR is rederived next.

### 2. Complete three-mate STAR derivation

Fix an actual component cell `y`, write `u=q_y`, and fix one of its three mates `X`. The `Q-X` product ONB resolves the tensor identity. Sandwich the `X` factor with `X_y`:

`I_8 = sum_z |⟨X_y,X_z⟩|^2 P_z`.

The `z=y` term is `P_u`. At any other cell, a nonzero weight forces `q_z perpendicular u` by `Q-X` product orthogonality. A cell in the same row or column as `y` has zero weight because that `X` row or column is an ONB. Thus

`I_8 - P_u = sum_{z off y's row and column, q_z perpendicular u} w_X(z) P_z`,

where `w_X(z)=|⟨X_y,X_z⟩|^2` lies in `[0,1]`. For two distinct mates their weights cannot both be positive at any `z != y`: orthogonality of those two mates' product vectors at `y,z` makes the product of their overlaps zero. Consequently the sum of the three weights at an eligible cell is at most one.

Add the three identities and compress to `W`. Noncomponent projectors compress to zero. It follows in the positive-semidefinite order that the unweighted component-cell star sum *off* the row and column dominates `3(P_W-P_u)`. In the actual `Q` row of `y`, the other three component cells resolve `P_W-P_u`; the same is true in its column. These two triples are disjoint because the row and column intersect only at `y`. Adding both triples gives

`A_u := sum_{z in C, q_z perpendicular u} P_z >= 5(P_W-P_u)`.  (2)

Taking traces, `tr A_u` is the number of original star-cell occurrences and `tr(P_W-P_u)=3`; therefore there are at least `15` such cells. This derivation uses neither GAP3 nor a reality or span assumption.

### 3. Two-plane projection mass, including the unpaired third

Let `B` be any complex two-plane in `W`, even if neither of its basis directions is an actual ray. Trace (1) against `P_B`:

`sum_{z in C} ||P_B q_z||^2 = 8 tr P_B = 16`.  (3)

For any actual component ray `v` lying in `B`, denote by `t(v)` the one-dimensional ray in `B` perpendicular to `v`. It need not be an actual ray. Evaluate (2) for `v` on a unit representative of `t(v)`. Whenever `q_z perpendicular v`, its `B` projection is either zero or lies in `t(v)`, and its `t(v)` weight is its entire `B`-projection mass. Thus

`sum_{z: P_B q_z != 0 and ray(P_B q_z)=t(v)} ||P_B q_z||^2 >= 5`.  (4)

Orthogonal complementation is an involution on projective rays in the complex two-plane, so distinct actual `v` give distinct target rays `t(v)`. A nonzero projected cell has only one projective direction; the sets in (4) are therefore disjoint. Four actual rays would require at least 20 mass units, contradicting (3). Hence `B` contains at most three distinct actual component rays.

If there are three actual rays `v_1,v_2,v_3` and no two are perpendicular, the cells on each `v_i` have `B`-projection mass one and lie outside *all* three target-direction sets: equality with `t(v_j)` would mean `v_i perpendicular v_j`, including the impossible self-orthogonality case. There is at least one cell on each `v_i`, so these cells contribute at least three extra units beyond the three disjoint five-unit sets. This would give `16 >= 15+3`, a contradiction. Thus there is an actual orthopair `x,x'`. The third ray `v` is distinct from both and cannot be perpendicular to either, since each has a unique perpendicular ray within `B`. Its own cells lie outside all three target sets and each contributes one unit; every global occurrence is in `C`. Therefore `16 >= 15+m(v)`, and because `v` is actual, `m(v)=1`. No actual status was required for `t(v)`.

### 4. Original-row bridge to global multiplicity one

Let `u` be any actual `C` ray and let `m=m(u) <= 3` by §1. Its occurrences lie in `m` distinct rows. Each of those rows has exactly three other `C` cells, all perpendicular to `u`; hence these rows contribute exactly `3m` star cells. Suppose every row without `u` has at most one star cell. Then the total is at most

`3m + (8-m) = 8+2m <= 14`,

contradicting the 15-cell consequence of (2). Some actual row without `u` has at least two star rays, `v,w`. It cannot have three: three orthonormal vectors in the three-dimensional `u`-perpendicular subspace of `W` would leave only the ray `u` for the fourth component entry of that row. Thus that row has exactly two star rays. Its other two component rays, `x,x'`, form an actual orthopair in the two-plane `B = W intersect span(v,w)^perp`. As `u` is perpendicular to both `v,w`, it lies in `B`; since the row has no `u`, it is distinct from `x,x'`. The unpaired-third result of §3 forces `m(u)=1`.

Since `u` was arbitrary, every component occurrence has a globally distinct ray. In particular the at least 15 star *cells* of any chosen actual `u` now give at least 15 distinct actual star rays. The row argument uses GAP3 essentially; the multiplicity bound is not inferred from the control example.

### 5. Three-space capacity and final contradiction

Let `D` be any complex three-space in `W`. Enumerate the distinct actual `C` rays in it as `v_1,...,v_N`. They need not form a basis or a QLS. For each `i`, compress (2) to `D` and take the trace. Because `v_i` lies in `D`,

`sum_{z in C, q_z perpendicular v_i} ||P_D q_z||^2 >= 5(3-1)=10`.  (5)

Sum (5) over `i` and interchange the finite sums. For a cell `z`, set `a_z=P_D q_z`. If `a_z != 0`, then `v_i perpendicular q_z` is equivalent to `v_i perpendicular a_z`; such `v_i` lie in the complex two-plane `D intersect a_z^perp`. Section 3 bounds their number by three, regardless of whether `a_z` is itself an actual ray. If `a_z=0`, its weight is zero, and there is no need to bound its possibly larger incidence count. Using (1),

`10N <= sum_z ||a_z||^2 #{i: v_i perpendicular q_z}`
`    <= 3 sum_z ||a_z||^2 = 3*8*3 = 72`.

Thus the integer `N` is at most seven. This bound itself uses the STAR and plane lemmas but not the multiplicity-one step: the outer index counts distinct rays, whereas all cell occurrences remain in the weighted mass sum.

Choose any actual `C` ray `u` and take `D=W intersect u^perp`, a complex three-space. By §4 its at least 15 star cells are 15 distinct actual rays in `D`, contradicting `N <= 7`. The hypothetical intrinsic C4 therefore cannot exist in any member of any ordinary four-MOQLS(8), under the pinned GAP3. The proof never restricts the complex coordinates or projector span and makes no existence assertion for a nonclassical family.

## Own exact controls and receipts

These are bounded sanity checks, not a substitute for the written proof and not evidence from author code. I wrote only the reviewer-owned script `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f197-moqls-no-intrinsic-C4-complete/reviewer-exact-controls-v1.py`. Its SHA-256 at execution was `e4b4df4d2aef34f1b66d21e76f5332f330e0443c1c26670c99ce2eb78f2f9d8b`. A preceding native-clock observation before writing that script was `2026-10-29T13:15:45-0700 PDT`.

One run used the tool's 120-second deadline, started at `/bin/date` `2026-10-29T13:16:24-0700 PDT`, ended at `/bin/date` `2026-10-29T13:16:25-0700 PDT`, and exited `0`; no cap was reached. The script uses only Python standard-library exact integers and rational Gaussian coordinates, with no import or execution of author material. Specific observed checks and intended-reason negatives:

* Four independently constructed linear `GF(8)` classical squares passed all row/column and six pair-product label bijections. An exact Gaussian-rational unitary transformed the Q basis. For all 32 cells of the four-ray block `W`, the script checked each mate contraction, disjoint mate supports and the `3+2=5` contribution in every star direction. This `W` is **reducible**, a union of four singleton components, with multiplicity eight for each ray; it is not a C4 candidate. This is an intended negative for applying GAP3/uniqueness without the intrinsic/nonfixed hypothesis.
* Removing one mate leaves only `2+2=4` in that derived contribution, not 5. This is an intended negative for a two-mate version of the STAR proof, not a claim that the actual classical example's full star is below 5.
* Exact nonreal unit directions `x=(1,0)`, `x'=(0,1)`, `v=(3/5,4i/5)`, `v'=(4i/5,3/5)` checked orthogonality, distinct target directions and exclusion of `v` from them. Abstract disjoint mass buckets gave `5+5+5+1=16`; adding a second `v` unit gave `17>16`. A duplicate ray index yielded the same target, illustrating why distinctness is necessary. The buckets are not asserted to be a realizable frame or MOQLS.
* Row arithmetic gives at most 14 when `m<=3`; abstract counts `(3,3,3,3,1,1,1,0)` total 15 for `m=4` with no double-star row, an intended negative for dropping GAP3 from that bridge.
* For the reducible example, the genuinely complex three-space spanned in Q-label coordinates by `q0,q1,(3q2+4i q3)/5` has masses `1,1,9/25,16/25` and two actual Q rays. The exact double count was `10N=20 <= 32 <= 72`; `10*7<=72<10*8`. Four abstract distinct rays in a plane perpendicular to a third axis gave incidence degree four, the intended negative for dropping the two-plane cap. These checks neither construct a feasible saturating `N=7` configuration nor exclude arbitrary complex configurations by enumeration.

## Imports, gap and process

The only mathematical theorem imported is the parent disposition's expressly adopted Gate 1 GAP3, at its stated scope. Its underlying proof and linked bodies were not reopened or independently certified here. Everything else in the C4 argument is reconstructed above from the ordinary four-MOQLS definitions. The remaining scientific dependency is GAP3 itself; whether any ordinary four-MOQLS(8) exists or has other component types is outside this review. The separately conditional §7 composition and its external statuses are not assessed.

Contract deviations: none. The supplied manifest identifier was a hash **prefix**, so only that prefix could be compared against the independently supplied value; the complete measured hash is recorded above. No author code, external model, search, solver, author contact, Git operation, deletion, publication, infrastructure mutation, or unrelated build/lint/test/formatter was used.

**This same-harness review is not human review, independent-model-family review, formal/kernel verification, or novelty verification.**
