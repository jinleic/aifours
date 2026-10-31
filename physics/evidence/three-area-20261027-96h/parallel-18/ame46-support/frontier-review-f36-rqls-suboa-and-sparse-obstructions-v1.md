# f36 — independent review: sub-OA intersections, two-sparse rays, Parker local family

Reviewer **PhysicsAME46-2**. Native observation immediately before writing: **`Wed Oct 28 17:39:21 PDT 2026`**; not an exact creation/completion/runtime clock. **Same-harness written reconstruction and reviewer-written exact checks; not formal/kernel, independent-model-family or novelty acceptance.**

## 1. Verdict, exact scopes and inputs

**NO SUBSTANTIVE DEFECT AT THE STATED SCOPES — 0 FATAL / 0 MAJOR / 0 MINOR against the three candidates.** The two OA counting theorems, the universal complex two-sparse ray bound and the fixed-incidence Parker local-completeness result reconstruct below. None is an unrestricted 100-ray QLS(10) no-go or an exact maximal-cardinality witness.

Read the complete assignment FIRST, SHA256 `c52e7b563ce341325d111429a9153e825e0ac255c7ea0dea49ba78a76e2d9ece`, then all three complete candidate files:

- **C1:** `frontier-20261028-suboa-intersection-obstruction-v1.md`, 93 LF, SHA256 `50c98f25fba210725c2ca768a85fbf677cd3d4390a71bc01fde6e84639aa9dc6`.
- **C2:** `frontier-20261028-two-sparse-cardinality-obstruction-v1.md`, 54 LF, SHA256 `ed80901c8664fc1e1370df5b19452c2ecda022ea837f3abb0a8324fc8384519d`.
- **C3:** `frontier-20261028-parker13-local-completeness-v1.md`, 89 LF, SHA256 `60c18a147f568aa2147c6035d213a11abf0c8dcda7d97fd3e5b4b8b763e7881f`.

The registered definition is `physics-5-rqls10-definitions-v1.md`, SHA256 `259ecf96d147a0bdb72145c5da8a3b9f98329726c6412ca7ed8cba566d613a6e`: ten row bases, ten column bases, ten disjoint actual transversal bases, 100 pairwise nonparallel rays for the original witness. Primary Parker 1959 section3 and the 12/13 actual certificates were independently read/reconstructed in my prior [f29 review](frontier-review-f29-rqls-classical-rigidity-and-rays-v1.md), SHA256 `4c77d5150986d9f2ad5e0f4f7c99819fdc90ce159fd085c8fdb1ebb879a9910c`. That is SAME-reviewer serial contact, not an independent-model review; the relevant constructions and new checks are restated here rather than assuming that prior verdict.

Historical held results are not premises. The author records two broken SMT models in C1 §4: their `unsat` results are explicitly INVALID as independent evidence and are not used here. No author contact, external-model/paid API, nested agent, Git, deletion or publication occurred.

## 2. Proper sub-OA size: the universal `n≥3k` count

An OA(n) is n² four-coordinate tuples, with each pair of coordinates a bijection to the n² ordered symbol pairs. A proper OA(k) subarray P has k² tuples, k symbols in EACH coordinate and the same pair-bijection property, with k<n. Let S_i be the selected symbols in coordinate i.

If a tuple outside P had two coordinates in the corresponding S_i, those two symbols already occur together in one P tuple, contradicting ambient pair uniqueness. Therefore each outside tuple contributes to at most ONE of the four sets `{x outside P:x_i∈S_i}`. In any ambient coordinate each symbol appears n times; each selected symbol appears k times in P. Each set therefore has k(n−k) members, while there are n²−k² outside tuples. Hence

`4k(n−k)≤n²−k²=(n−k)(n+k)`.

The hypothesis k<n makes n−k>0; cancellation yields **n≥3k**. No hidden selected n, OLS symmetry, source theorem or division at k=n is used. For an OA-derived single-pocket rotation, every original color still occurs outside P because n−k>0, while the pocket has only k transformed basis rays; hence that SPECIFIC construction has at most n+k rays. At n=10 it implies k≤3 and at most13, conditional on such a pocket existing. It does not bound arbitrary quantum arrays or multiple/overlapping surgeries.

## 3. Two disjoint subarrays: complete SAME-array count

Assume disjoint OA(k) subarrays P,Q with coordinate alphabets S_i,T_i. Put `t_i=|S_i∩T_i|`. At most one t_i is positive: if two coordinates had shared symbols, pair-bijection in EACH subarray produces two ambient tuples with the same chosen coordinate pair, so ambient uniqueness makes them the SAME tuple, contradicting disjointness. Let t be the sole positive overlap or0; `0≤t≤k`.

Let X be the n²−2k² tuples outside P∪Q. For x∈X the P-alphabet membership count and Q-alphabet membership count are each at most1 by the same uniqueness argument. Define A,B as the sets where these respective counts equal1; let I=|A∩B|, and J count the points in I where both memberships occur in the SAME coordinate.

- Outside P the four P-alphabet memberships total `4k(n−k)`. Q contributes exactly kt of them, since each shared symbol appears k times there. Thus `|A|=|B|=4k(n−k)−kt`.
- Across the12 ordered DISTINCT coordinate positions, ambient pair-bijection gives `12k²` S_i/T_j incidences. P contributes3kt and Q contributes3kt. A point of X contributes exactly one iff its S/T memberships occur in different coordinates. Therefore `I−J=12k²−6kt`.
- Each of the t shared symbols occurs n times in its one overlapping coordinate, k in P and k in Q. Its remaining n−2k occurrences are exactly the same-coordinate members of I, so `J=t(n−2k)` and `I=12k²+t(n−8k)`.

The SAME sets yield two nonnegative counts:

`|A\B|=4kn−16k²+t(7k−n) ≥0`,

`|X\(A∪B)|=n²−8kn+18k²+t(n−6k) ≥0`.                                             (OA)

For `n=3k+1`, the first is `−4k(k−1)+(4k−1)t≥0`. If t≤k−1, its RHS is at most `−(k−1)<0` for k≥2, so t=k. Substituting t=k in the second gives `1−k<0`, contradiction. Thus any two OA(k) subarrays of OA(3k+1) intersect in an actual ambient tuple. All overlap cases, including t=0 and t=k, are covered. This is a general written argument, not a replay of the broken SMT models or an extrapolation from a table census.

The correspondence with OLS is an exact coordinate dictionary: after designating two coordinates as row/column, the other two coordinates are Latin symbols whose ordered pair is unique. The obstruction is conditional on actual classical OA/subarray provenance; it does not force a general QLS to possess such subarrays.

## 4. Two-sparse rays: partner pairing and bound

Suppose an n²-cell array has k≥2 classes of n disjoint ONB blocks, each block of one class meeting each block of another in exactly one cell. Assume EVERY cell vector has support at most2 in ONE common ONB. No realness assumption is needed.

Inside any ONB block, two nonzero vectors whose supports intersect in exactly one coordinate cannot be orthogonal: their inner product has exactly one nonzero complex product. Let v have exact support `{a,b}`. A complete ONB must have another vector with nonzero a-coordinate, since the sum of squared a-coordinates over the block is1 and v uses nonzero b as well. Orthogonality forces that other vector to have exactly support `{a,b}`. There can be at most two mutually orthogonal nonzero vectors in this two-dimensional plane, so its partner is unique, and its ray is the unique orthogonal-complement ray R⊥ to v's ray R.

The k blocks containing a cell x meet only in x, so their R⊥ partners are k DISTINCT cells of the same ray. Apply the argument to any one of those partners: its k distinct partner cells all have ray R. Thus EVERY occurring two-support ray has multiplicity at least k. This uses the same actual array and all block intersections, not independent partner choices.

If s cells are singleton-supported and t=n²−s are two-supported, there are at most `min(n,s)` singleton rays and at most `floor(t/k)` two-support rays. The categories cannot be parallel. Hence

`C≤min(n,s)+floor(t/k)≤n+floor(n(n−1)/k)`.

For integer s≤n the first RHS is nondecreasing with s, and for s≥n it is nonincreasing; its maximum is at s=n. The all-singleton case t=0 is included. For ANY original 1-resolvable QLS(10), row/column/transversal classes have the required pairwise single-cell intersections, so k=3 and C≤40 under the **global common-basis two-sparse hypothesis**. This is not an assertion that every quantum array admits that basis.

Independent check on the actual Parker12 certificate found s=94, t=6, 12 rays and the six two-support cells each having three DISTINCT same-ray partners in their three blocks. It corroborates the instance and the profile-dependent bound12; it does not establish that the uniform40 bound is sharp.

## 5. Parker 13-ray object and exact gauge Jacobian

The same actual Parker certificate SHA256 `0108335bbbe2d35214761904172490bbbed6976d59dd19748aaa7843276dc9e5` was independently reconstructed and definition-checked in f29: 100 exact unit vectors, all30 actual ONB blocks, valid transversal labels, 13 rays/387 parallel pairs. The nine OA(3) pocket cells are transformed by `Q=I−(2/3)J`; `J²=3J`, so Q is orthogonal. Each fixed row/column/transversal block meets the pocket in zero or three distinct pocket colors; replacing Q by ANY U(3) preserves all its ONB constraints. Near Q its three rotated rays remain distinct from the ten outside standard rays, so that family has13 rays.

The ungauged real/imaginary derivative equations and exact assembly were independently verified in f29: `v_x·a_x=0`, and for each within-block x,y the real equation `v_y·a_x+v_x·a_y=0` and imaginary equation `v_x·b_y−v_y·b_x=0`. My directly assembled files have the author's corrected-v2 hashes and contain **1450×1000 real** and **1350×1000 imaginary** rows; all coefficients are integers (the original common denominator3 is a nonzero row scaling).

For the stated gauge I independently added the100 first-row coordinate zeros in EACH sector, 90 imaginary phase-alignment rows for the remaining cells, and the two imaginary anchor-coordinate zeros at cell(7,7). The anchor numerator is exactly `(1,−2,−2)` on colors7,8,9. The resulting own-root matrices have **1550×1000 real** and **1542×1000 imaginary** dimensions and match the author's gauge matrix bytes:

- real SHA256 `6c544d04942f27e957b655ca5576de3fb476934a766a5571bdbe1ecca1bf283e`;
- imaginary SHA256 `ceb2b3e2dddcac7673abd7dc1813373dde1c326589d60d5210507df4719ce3ba`.

My separate C++ exact modular elimination over the directly checked prime65521 returned **rank997/nullity3** and **rank999/nullity1**. Modular rank is a LOWER bound on rational rank, hence these are UPPER bounds on rational nullities. I separately loaded the author's rational vectors and verified every row over Q: three real vectors have identity values on free columns989,998,999, and one imaginary vector has free column989 equal1. Thus those four null vectors are independent, giving matching LOWER bounds. The characteristic-zero gauge-nullity is therefore **exactly 3+1=4**, not merely a modular guess. A mutated non-free rational entry was independently rejected at `null-vector failure row=78 free=989`.

## 6. The actual gauge and four-dimensional family

First align an exact nearby first-row ONB to its labelled reference ONB by one nearby common U(10), then phase-align each of the other90 vectors by its nonzero reference inner product. On the reference's ten standard rays, any remaining global gauge tangent is diagonal imaginary. The seven outside-color diagonal phases act trivially on the reference rays; the three pocket phases act on Q's nonzero entries. The two extra anchor conditions set the first two pocket-component imaginary variations to zero.

Writing phase differences relative to the third pocket coordinate, the anchor has squared weights `(1/9,4/9,4/9)` and the 2×2 derivative of those two conditions is

`[[8/9,−4/9],[−1/9,5/9]]`, with determinant `4/9≠0`.

Thus the residual two effective diagonal phase differences are removed, and the ordinary IFT gives a finite smooth nearby gauge. No exact radius is asserted. Stabilizer phases acting trivially on reference rays are not spuriously counted as tangent directions.

The embedded U(3) family has dimension9. Cell phases remove the right diagonal 3-torus; common global unitary phases remove the left diagonal 3-torus. Their stabilizer intersection is one-dimensional: every Q entry is nonzero, so `diag(t)Q=Q diag(s)` forces all six diagonal parameters equal. Hence the effective local family dimension is `9−(3+3−1)=4`. Its infinitesimal variations are actual full-constraint solutions, and after the valid gauge they give four independent tangent vectors. The exact gauge-nullity from §5 is also four, so the two tangent spaces agree.

## 7. Why the tangent equality does imply the local nonlinear claim here

The full real-analytic gauge-plus-constraint Jacobian has rank `997+999=1996` in2000 real variables: the modular lower bounds and exact rational null vectors establish equality, not just a sampled estimate. Choose 1996 independent equations. By IFT their common zero set near the reference is a smooth 4-dimensional manifold M; every fully feasible gauged array lies in M. We do NOT assume those selected equations imply all the omitted constraints.

The gauged embedded-U(3) family consists of genuine FULL solutions in M and has dimension4 with tangent equal to T(M). The inverse function theorem gives an open neighborhood in M covered by that family. Therefore any fully feasible gauged array sufficiently near the reference lies in the family. Undoing one common unitary and cell phases gives C3's actual labelled-array local completeness. Near Q the three transformed rays are pairwise distinct and different from the ten standard rays, so every such array has exactly13 rays. This reasoning does not assert that a mere tangent equality would suffice without the selected-equation manifold and inverse-map step.

The fixed reference, fixed labelled resolution, sufficiently-small neighborhood and same30 block constraints are essential. There may be other incidences or distant components; no unrestricted solution or obstruction is inferred.

## 8. Executed checks and artifacts

- `frontier-20261028-f36-gauge-null-verifier-v1.py`, SHA256 `82606dbd7946060def0d2290693a59c4ac78aac112986a6b6c7a0c27ba798af3`, independently appended gauge rows to my f29 independently assembled ungauged matrices and checked all four supplied rational null vectors against EVERY row. Receipt `frontier-20261028-f36-gauge-null-verifier-v1.json`, SHA256 `ba8a2654640e0b148a5cbc1ba50419eded36776ef47f364ee1c50fc438f41fa9`, records input hashes, row counts and free-coordinate identity.
- My C++ checker `frontier-20261028-f29-modrank-independent-v1.cpp`, SHA256 `f57bbd34f34cbc3d5fce8fa653fb34651f98dec1fc18bfe7c1587b90f3d1cc76` (compiled binary SHA256 `dec2d047afeadace2ffa76581d4f3a6b371c34b79673a9afba9da9940e4babf0`), was run on those own-root gauge matrices with65521 and returned the two rank/nullity pairs in §5. Its prime test, rank2 calibration and composite-modulus rejection were exercised and recorded in f29.
- A separate `Fraction` mutation control incremented a non-free entry of a claimed rational null vector; direct all-row verification rejected it at row78/free989. This was an actual targeted control, not an inference from a hash.
- `frontier-20261028-f36-two-sparse-partner-check-v1.py`, SHA256 `1e9dad0e2bf8a0fa50be9b4a20fb27dd6f903f5a3a568879899734f59b15d0e5`, independently checked the 12-ray input SHA256 `e64b0e90d6b0f908a07727de96f44bacf24a1abbf723b306de7e681189c05533`: 94 singleton/6 two-support cells, with three distinct same-ray partners in the actual three blocks of each. Receipt SHA256 `5d005dcbf728c6796b41499e965834248007a7836ef772e643befa85f4381ab5`.
- The f29 independent witness/primary-table and pairwise-ray code/receipts are pinned in that review. I did not independently replay the author's four-table OA census, invalid SMT outputs or bounded switch-growth experiment; these are nonloadbearing to the written OA/partner/local proofs and are not rebranded as successful exhaustive evidence.

These checks are reproducible local exact computations and written arguments, not independent-model-family review, formal proof or a complete mutation campaign. Source novelty and global original-target status are not established by them.

## 9. Final boundaries

C1 applies only to actual classical OA subdesigns; it does not cover arbitrary quantum arrays. C2 applies to arrays globally two-sparse in ONE common basis; no such restriction may be imposed WLOG on the target. C3 concerns one fixed Parker incidence and a neighborhood of one13-ray reference modulo common unitary/cell phases. Its local result is mathematically stronger than a tangent bound but remains local. The 100-ray existence/universal-obstruction target is not solved by any of them.

All earlier historical STOP/HOLD/ZERO records remain historical and were not treated as verified scientific premises. No author contact, external-model/paid API, nested agent, secrets, Git/push/publication, deletion or infrastructure mutation. This review returns to Main; I will resume the original AME research.
