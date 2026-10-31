# Exact hidden-quadratic factorization for one ten-edge support slice

Status: **WRITTEN, with the eight path-numerator factorizations checked in the owner's SymPy kernel**, pending independent review. This identifies the hidden-root type and observable support geometry for a specific ten-transition graph; it does **not** exclude the graph, give a PH realization, or settle PH7 at `8/9`.

## 1. Fixed graph and actual support condition

Consider an irreducible seven-state row generator with positive edges exactly

`0->1, 0->3, 0->6, 1->2, 2->0, 3->4, 4->5, 5->6, 6->2, 6->4`.

Write the edge rates, in the order listed, as `e0,...,e9>0`, and its diagonal escape rates as row sums. There are no directed two-cycles. Its directed triangles have vertex sets `{0,1,2}`, `{0,2,6}`, and `{4,5,6}`. This graph appeared in a bounded floating search (`frontier-20261029-ph7-ten-edge-shared-triangle-search-result-v1.json`, SHA256 `e40f60a05b78e60c05eb3e6b3fb3400b2cd358f14e775eddfff402269d9be893`); that numerical result is diagnostic only and is not used below.

For any nonnegative input/exit pair realizing the target transfer, relative degree five forces every supported input-to-exit shortest distance to be at least four and at least one distance to equal four. The separately frozen five-edge path theorem `frontier-20261028-ph7-five-edge-path-and-hidden-sum-bound-v1.md` (SHA256 `f38f7874e21431cf3a1661c566570b215f656c59d9d9d0b1c73bc876ea31381b`) further requires a supported simple five-edge path whenever `z>1/5`. This paper makes the additional support restriction that the **entire** input and exit supports lie in one of the eight minimal pairs listed in §3; supports outside these pairs are not covered.

## 2. An exact factorization example

Suppose input is supported at vertex 1 and exit is supported on `{4,5}`. Every relevant simple path has four or five edges; the two length-four and two length-five paths share their prefix and have a common `4->5` extension. The full adjugate numerator, up to the positive factor `alpha_1*e3*e4`, is

`[y*beta_4+beta_4*e7+beta_5*e6] * [y*(e1*e5+e2*e9)+e1*e5*(e8+e9)+e2*e5*e9]`.

The formula retains all four actual paths and all complement determinants; it is not based on one selected path. If the target transform is realized, relative degree five forces `beta_4>0` and hence a strictly positive leading coefficient. The hidden quadratic `Q` is the monic normalization of this product, and both its roots are real and strictly negative. A length-five simple path to vertex 4 is absent, so the supported-five-edge theorem also forces exit vertex 5 to be supported.

## 3. Eight minimal support rectangles

The same full path-adjugate expansion factors into a product of two real linear polynomials with nonnegative coefficients for each support rectangle below:

| Input support contained in | Exit support contained in |
|---|---|
| `{1}` | `{4,5}` |
| `{1,2}` | `{5}` |
| `{3}` | `{0,2}` |
| `{3,4}` | `{0}` |
| `{4}` | `{0,1}` |
| `{4}` | `{0,3}` |
| `{4,5}` | `{1}` |
| `{4,5}` | `{3}` |

All actual supported path weights are nonnegative, and the target's relative degree guarantees a nonzero quadratic leading coefficient. The same conclusion holds if one or more listed input/exit weights vanish but the remaining supports still meet the relative-degree and five-edge-path requirements. The eight factorizations were checked symbolically from all simple paths in the owner's Python/SymPy kernel; they are not a machine-checked exhaustive classification of every admissible support rectangle, nor an independent scientific review.

The factorization follows structurally from the fixed graph's serial prefix/suffix and its two alternative routes through `0->3->4` and `0->6->4`: the complementary diagonal factor for one route is the other's unused branch rate, so summing route weights gives a single real linear factor. For the first row the explicit identity in §2 is the complete proof; the other rows require the analogous actual path expansions and may be independently reconstructed from the stated ten edges.

## 4. Nonclaims

The hidden roots being real does not itself contradict the target: the round's separately written hidden-pole separation theorem explicitly permits two distinct real roots, and all-target `tr(G^2),tr(G^3)` constraints have real-root-feasible regions. The graph also has other admissible support rectangles not asserted to reduce to these eight. Thus this document is an exact scoped reduction, not a selected-optimizer exclusion, formal proof, novelty assertion, parent adoption, or complete `8/9` decision.
