# Candidate tool addendum: coordinate Steiner symmetrization preserves all plateau coupling

Actual clock observation preceding creation: **2026-10-23T16:29:57-0700**. Same finite-V problem. This extends the frozen coupled candidate `ae1e05470b233d2e51a3c56f45a58ab97ecd249a5ed479dc33c6d29ae4ea3958` and its closed-level addendum `87320046a2396eb936138af7c3eb3122a5e3451140a70171dce73cb270fd5596`. **The full conditional packet requires those complete bodies, not only their headers. CANDIDATE; no inherited verdict, execution or formal verification; NOVELTY_UNCLEAR.**

Steiner symmetrization and the elementary interval/moment facts below are **standard tools, not separately claimed discoveries**. The purpose is to justify an all-law geometric reduction while preserving every coupled privacy level, instead of silently assuming a symmetric/core family or using the invalid l1-angular averaging for mixed squared cost.

## 1. Exact reduction being justified

There is a genuine unrestricted finite-b MSE optimizer that can be represented by a geometric density with compact closed levels K_k satisfying

`K_k+D subset K_(k+1)`,

such that every K_k is invariant under signed coordinate permutations and is an **absolute-coordinate order ideal**:

`x in K_k and |z_i|<=|x_i| for i=1,2 imply z in K_k`.

These properties are **derived by feasible operations and optimality**, not assumed in the original all-Borel class. They do not imply convexity, l1-radiality or a single level0 core. The optimal head/value and a matching dual remain unknown. This is a reduction tool in the same structural attack, not an independently counted resolution of V.

## 2. A compact-set coordinate symmetrization, including zero fibers

For a nonempty compact A in R² write

`A_y={x:(x,y) in A}`, `L_A(y)=lambda_1(A_y)`, `I_A=projection_y(A)`.

Define

`S_x(A)={(x,y):y in I_A, |x|<=L_A(y)/2}`.

The explicit projection condition matters: an empty fiber must not create an unbounded line of zero-length fibers. Nonempty zero-length fibers contribute only their center point and do not affect area.

The projection I_A is compact and the fiber length is upper-semicontinuous. Indeed, if y_j tends to y, closedness gives `limsup 1_A(x,y_j)<=1_A(x,y)` pointwise; a common bounded x-interval dominates all fibers, so reverse Fatou gives `limsup L_A(y_j)<=L_A(y)`. The displayed centered-fiber set is therefore closed and bounded, hence compact. Fubini gives exactly

`|S_x(A)|=|A|`.

Inclusion is monotone: A subset B implies their projection inclusion and fiber-length inequality, hence S_x(A) subset S_x(B).

## 3. The interval-addition fact and exact Minkowski inclusion

For every nonempty compact E in R and every d>=0,

`|E+[-d,d]|>=|E|+2d`.

One complete elementary proof: let m=min E and M=max E, and list the disjoint open gaps of E in [m,M], of lengths l_j. Adding [-d,d] leaves gaps of lengths `(l_j-2d)_+` inside the new span [m-d,M+d]. Thus

`|E+[-d,d]|=|E|+2d+sum_j min(l_j,2d)>=|E|+2d`.

All gap sums are bounded by M-m, so this does not subtract divergent quantities. The singleton and d0 cases are included.

The diamond fiber at ordinate v is the centered interval of radius `1-|v|`, for |v|<=1. If `(x,y)` is in S_x(A)+D, decompose y=y1+y2 with y1 in I_A and |y2|<=1. The original fiber A_(y1) is nonempty. Its sum with that diamond interval is contained in the fiber (A+D)_y, so the preceding fact gives

`L_(A+D)(y)>=L_A(y1)+2(1-|y2|)`.

The decomposed x has absolute value at most half that right side. Also y belongs to the actual projection of A+D because both original fibers are nonempty. Therefore

`S_x(A)+D subset S_x(A+D)`.

This is an exact set inclusion for arbitrary compact A, **not requiring convexity**. Since S_x(D)=D and symmetrization is monotone, every exact level coupling is preserved:

`K_k+D subset K_(k+1)` implies `S_x(K_k)+D subset S_x(K_(k+1))`.

No privacy-budget splitting or change from diamond to another sensitivity norm occurs.

## 4. Squared-Euclidean moment decreases fiber by fiber

For a measurable subset E of R of finite length l, the centered interval I=[-l/2,l/2] has no larger x² moment:

`integral_E x² dx >= l³/12`.

To see the precise inequality and equality condition, the product

`(x²-(l/2)²)(1_E-1_I)`

is nonnegative inside and outside I; equal lengths eliminate the constant term. Equality holds iff E equals I up to one-dimensional measure zero, since the product is strictly positive on their symmetric difference apart from the two interval endpoints. If l0, both sets are null for the integral and the same a.e. statement holds.

For the planar fibers, the y² part is exactly preserved because the fiber lengths are unchanged. Hence, with M(A)=integral_A(x²+y²),

`M(S_x(A))<=M(A)`.

Equality holds iff almost every horizontal fiber is its centered interval a.e., equivalently `lambda_2(A symmetric-difference S_x(A))=0`. All compact-set moments used here are finite. This operator is not the l1-angular rearrangement: the resulting levels need not be homothetic diamonds, so it does not reassert the refuted mixed-cost conjecture.

## 5. Apply the operator to the entire optimal level sequence

Begin with a closed-level geometric optimizer `q=a b^min{k:x in K_k}` supplied by the operative coupled/closed-level candidate packet. It has K_0 of positive area, all K_k compact, all exact couplings, and

`1=a(1-b)sum_(k>=0)b^k|K_k|`,

`J=a(1-b)sum_(k>=0)b^k M(K_k)`.

Put `H_k=S_x(K_k)`. These sets are compact, nested, with `H_k+D subset H_(k+1)`. Their union is the whole plane, since a point of H_0 plus kD is contained in H_k. Thus the index `m(x)=min{k:x in H_k}` is finite everywhere and its geometric density

`q_S(x)=a b^m(x)`

has the full pointwise privacy ratio. Area preservation shows that it has **exactly unit mass**, with no changed normalization. The fiber moment bound and nonnegative full layer sums give `J(q_S)<=J`. This is a genuinely feasible all-level transformation, not a separate optimization of unrelated plateaus.

Since q is globally optimal, equality holds. Every individual moment deficit is nonnegative and every weight `a(1-b)b^k` is positive. The total weighted deficit is zero, so each level separately has

`M(K_k)=M(S_x(K_k))`.

Consequently `K_k=S_x(K_k)` a.e. for every k. The proof uses all levels and their exact couplings; it does not assume that an arbitrary one-core family contains an optimizer.

## 6. Obtain the full signed/permutation symmetry without an ansatz

Before amplitude selection, one may average any original optimal density over the eight signed coordinate permutations. Each pushforward preserves the full diamond privacy model, mass and squared-Euclidean cost. The finite average is therefore still optimal. Applying the base's amplitude-phase selection to that invariant density preserves the group symmetry, since the thresholding is a pointwise function of the density. Essential supports and the derived closed-level representative also preserve that symmetry. Null-set choices can be made group-invariant using the finite group union.

Hence the starting closed geometric optimizer in Section5 may be selected with exact signed/permutation-invariant K_k. This is an operation on an unrestricted optimizer, not a restriction imposed on the original feasible set.

It remains to pass from the a.e. fiber conclusion to the exact order-ideal property of those essential supports. Fix 0<t<=1 and the invertible coordinate contraction `T_t(x,y)=(tx,y)`. The centered-fiber set `S_x(K_k)` is exactly invariant under this contraction in the inclusion sense. Since it equals K_k a.e. and T_t maps null sets to null sets,

`lambda_2(T_t(K_k)\K_k)=0`.

The K_k are essential supports of their own Lebesgue restrictions: the closed-level addendum gives E_k=K_k a.e., and K_k was defined as the essential support of E_k. An invertible linear map transports that essential support exactly, so the essential support of T_t(K_k) is T_t(K_k). Taking supports in the a.e. inclusion yields the **exact** inclusion

`T_t(K_k) subset K_k`.

For completeness, a neighborhood of T_t(x) pulls back to a neighborhood of x; positive area near x maps to positive area by the positive determinant t. This proves the support transport and uses no regular boundary hypothesis. Passing t to0 uses closedness. Reflections and coordinate interchange then give contractions of either absolute coordinate and every sign choice. That is precisely the order-ideal property stated in Section1.

Thus there exists an optimal geometric pointwise-private closed-level representative with those unconditional/permutation symmetries and coordinate monotonicity. Neither convexity nor equality of density at all points with the same l1 norm has been proved or assumed.

## 7. Exact remaining head/dual obligation and trust boundary

The unknown compact head levels can now be studied, conditionally on the full packet, within absolute-coordinate order ideals rather than arbitrary nonsymmetric measurable sets. Their boundary profiles still need not be concave, and the coupled finite-prefix optimization has not been solved. Do not replace this with a convex-core or radial parameter family without a new proof. No exact V, explicit optimal head/density, matching finite-epsilon dual or independent discovery count is supplied.

The standard operator, finite group average, scalar interval inequality and fiber moment principle are mathematical tools, not claimed inventions. The model-specific coupling/equality argument is documented so those reductions are not silently assumed. The source-priority status of the resulting structural package is **NOVELTY_UNCLEAR**; the prior mechanism ancestry and current affine-square source qualifications remain operative. This is not a CND assertion: no ROC-tightness or monotone-likelihood-ratio requirement is imposed.

This addendum needs its own actual supplied-proof reconstruction together with the full named base/closed-level bodies. No earlier disk/peak/asymptotic verdict verifies it, and no scientific or formal execution occurred.
