# Full finite head: convex one-dimensional shapes at fixed supports

Observed clock before creation: **2026-10-23T17:58:33-0700**.

## 0. Literal status and purpose

This is a complete conditional representation/tool for the SAME unrestricted finite-ε V, not a solution of its remaining range and not another mechanism family or envelope constant. The original density problem is already a convex linear problem; no invention of convex optimization is claimed. The purpose is to retain genuinely coupled, possibly nonconvex planar heads while making their one-dimensional shape problem explicit.

It imports **only D0** as stated in `proof-small-optimum-matching-value-v1.md`, SHA `45bd223bd6118ab8c651de90d35af69bacc3edc6e2f7125683926aedeceb1221`: existence of an original global optimal geometric-valued density with simultaneous closed, unconditional coordinate-ideal levels and the coupled expansion sandwich. It does not import that manuscript's new small-regime value theorem. D0's actual coupled reconstruction is still not received/read by this owner. Thus this representation is CANDIDATE at that dependency boundary. No independent theorem/discovery count, novelty certificate, numerical run, or proof-assistant verification is claimed.

Throughout, D is the l1 unit diamond, b=exp(-ε), U=4/ε², and all ε>0 are allowed.

## 1. A bounded exact finite-head class

Set

```
L = ceil(sqrt(2U)) >= 1,
B = sqrt(pi) * U * b^(-(L+1)/2).
```

Consider all nonempty compact unconditional coordinate-order ideals K_0,...,K_L inside [-B,B]² such that

```
K_k + D ⊂ K_(k+1),   0<=k<L.
```

Extend them by K_(L+j)=K_L+jD for j≥1. Coordinate interchange is NOT required in this class. Define

```
n(x) = min{k>=0 : x in K_k},
u(x) = b^(n(x)),   Z=∫u,   N=∫|x|²u.
```

Every such sequence gives a genuine original law u/Z. Each set contains0; hence K_k⊃kD, and the index is finite everywhere. The set inclusions give |n(x+h)-n(x)|≤1 for every h∈D, including every boundary. Geometric tails of compact K_L make Z and N finite, and Z>0.

### Why the class includes a true global optimum

Take the D0 minimizer q=alpha*b^n with cost V≤U. For any density bounded by alpha, the bound P(|X|²≤s)≤pi*alpha*s gives, by tail integration,

```
V >= ∫_0^(1/(pi*alpha)) (1-pi*alpha*s)ds
  = 1/(2pi*alpha).
```

Thus alpha≥1/(2pi U). At x∈K_k, pointwise privacy gives q(x+h)≥b*q(x)≥alpha*b^(k+1) for every h∈D. Consequently

```
V >= alpha*b^(k+1) ∫_D |x+h|² dh
  = alpha*b^(k+1) (2|x|²+2/3),
|x|² <= pi*U²*b^(-(k+1)).
```

For k≤L, K_k lies in the stated common box. Also K_L⊃LD⊃B_(sqrt U). It contains B_(sqrt V), so the D0 sandwich forces every later level to be exactly K_L+jD. Hence a true global optimizer belongs to this finite-head class.

All members of the class are original feasible laws and a true optimizer belongs to it. Its minimum N/Z is therefore exactly V. This is a representation, not a computation of that minimum.

## 2. Exact profile constraints for every full-D shift

Let r_k be the vertical projection halfwidth of K_k. For fixed r=(r_0,...,r_L), write

```
K_k = {(x,y): |y|<=r_k, |x|<=F_k(|y|)},
F_k:[0,r_k]->[0,B] upper semicontinuous and nonincreasing.
```

Zero-width fibers are retained as actual axis points; they are not replaced by fictitious positive mass. Nonemptiness and coordinate-order closure make this representation exact, including endpoints.

The full coupling K_k+D⊂K_(k+1) is equivalent to BOTH

```
r_(k+1) >= r_k+1,
F_(k+1)(y) >= F_k(z)+1-|y-z|
```

for every 0≤z≤r_k and 0≤y≤r_(k+1) with |y-z|≤1. Indeed, the horizontal section of D at a vertical shift y-z is the entire interval of radius1-|y-z|. Negative source heights cannot give a larger right endpoint than their positive reflection when y≥0. These inequalities account for the entire diamond, not just its vertices or a sampled set of shifts.

At fixed r, all these constraints are affine inequalities in the F_k, as are positivity, the bound B and monotonicity. Their feasible profile set is convex. This does NOT assume that the planar K_k are convex; their profiles need not be concave.

For a tail j≥1, the exact profile of K_L+jD on [0,r_L+j] is

```
M_j[F](y) = max_{0<=z<=r_L, |y-z|<=j}
                 (F(z)+j-|y-z|).
```

The maximum exists. For fixed r_L and j, this operator is a supremum of affine functions of F and is therefore convex. It is not asserted affine.

## 3. Convexity of the signed shape problem

Put

```
phi_(y,λ)(s) = s³/3 + (y²-λ)s,   s>=0.
```

For fixed support vector r and λ∈[0,U], the exact signed numerator N-λZ is

```
4(1-b) sum_(k=0)^L b^k ∫_0^(r_k) phi_(y,λ)(F_k(y))dy
+
4(1-b) sum_(j>=1) b^(L+j)
            ∫_0^(r_L+j) phi_(y,λ)(M_j[F_L](y))dy.
```

The factor is4 because these are full quadrant profiles, not first-octant profiles. This follows directly from the layer identity u=(1-b)sum b^k 1_(K_k) and integration of x²+y² over 0≤x≤F_k(y).

Each finite-head integrand is strictly convex in its profile value: s³/3 is strictly convex on [0,infinity), and the other term is linear.

The tail needs a separate monotonicity argument; convexity of phi alone would not justify composition with M_j. Every admissible K_L contains LD⊃B_(sqrt U), so every K_L+jD does also. Thus its profiles satisfy

```
M_j[F_L](y) >= sqrt(max(U-y²,0))
```

whenever the right side is positive. On this range

```
d phi_(y,λ)/ds = s²+y²-λ >= 0.
```

Since λ≤U, phi is nondecreasing on the range actually used. Composition of this convex nondecreasing function with the convex operator M_j is convex. The same statement holds when y²≥U because phi is then nondecreasing for all s≥0.

The tails converge uniformly under the common head bound B: their areas and moments are bounded by constants times (B+j)² and (B+j)⁴, respectively, and the weights are geometric. Therefore the entire signed objective is convex at fixed r. It is strictly convex up to area-null profile changes, since every F_k occurs in a positive-weight strictly convex finite-head term.

An area-null change of a head may still change a later dilation; it is not automatically dismissed. If two minimizing tuples differ on positive measure in a head profile, strictness already follows from that head term. Otherwise, if some tail profiles M_j[F_L] differ on positive measure, the inequality M_j[theta F_L+(1-theta)G_L]≤theta M_j[F_L]+(1-theta)M_j[G_L], followed by monotonicity and strict convexity of phi, makes that tail term strictly smaller. Equality can therefore persist only when all represented head and tail level sets agree almost everywhere, which leaves the raw density and hence the law unchanged.

**Conclusion:** for each feasible fixed support vector r and each λ∈[0,U], the signed shape problem has at most one minimizing profile tuple up to the changes that leave the represented law unchanged almost everywhere. It is not claimed that N/Z itself is convex, or that the outer support selection is convex.

## 4. Attainment is not a hidden shape ansatz

The finite-head class is compact in the product Hausdorff topology. Nonempty compact subsets of the common box form a compact hyperspace; unconditionality, coordinate-order closure and the Minkowski inclusions are preserved under limits. A fixed support vector is a closed subfamily because projection maxima vary continuously under Hausdorff convergence.

A planar coordinate ideal has area-zero boundary: away from the axes it is a monotone-profile graph, with possible additional horizontal boundary segments only at countably many jumps. If such ideals converge in Hausdorff distance, their indicators converge almost everywhere. For an interior point, first take a slightly coordinatewise larger interior point and approximate that point from the convergent ideals; downward closure then includes the original point. Exterior points are eventually excluded by positive distance. Boundary and axis exceptions have zero area.

Thus each bounded-head area and moment is continuous. The same holds for every fixed dilation of K_L. The preceding geometric polynomial domination makes the full Z and N continuous. Uniformly,

```
Z >= (1-b)b^L Area(K_L) >= 2(1-b)b^L L² > 0.
```

Consequently both the full ratio problem and each feasible fixed-r signed shape problem attain their minima. The latter minimum is unique in the almost-everywhere sense just stated.

This does not turn the remaining full V into an explicit scalar formula: the support vector is still unknown, and the unique inner profile is not yet calibrated or expressed in closed form.

## 5. A concrete reason local obstacle equations are insufficient

Combining the earlier lowering and erosion-raising necessary conditions gives the local form, with R=√J,

```
K_k = (K_(k-1)+D) union ((K_(k+1) erosion D) intersect B_R)
```

almost everywhere for k≥1, and the analogous k=0 equation with empty lower obstacle. These are coordinatewise conditions, not a matching global dual.

A negative control is already available. For any b∈(0,1), take the disk core S=B_r with r=b/4 and its exact one-core law. Let its cost be J. If M is its density maximum, privacy at a top point gives1≥2bM; tail integration gives J≥1/(2pi M)≥b/pi>r². Thus S⊂B_(sqrt J), while S erosion D is empty because r<1.

Every S+kD is convex. By support-function separation,

```
(S+(k+1)D) erosion D = S+kD.
```

So this disk-core sequence satisfies the local lower/upper obstacle equations and the no-extra-top erosion condition at its own J. Nevertheless every positive-radius disk-core law is strictly improvable by the already written-checked disk-deformation packet (`proof-no-finite-disk-core-optimum-v1.md` with its mandatory notation addendum). The control is not a new disk-family result and is not claimed to satisfy every other possible inexpensive optimality test. It proves specifically that these local obstacle equations alone are insufficient.

This control does not refute the convex signed program: it is not claimed to minimize that program. It prevents treating coordinatewise stationarity as an all-law certificate.

## 6. Exact unresolved input and continuation discipline

The remaining required input is a genuine coupled calibration: solve the convex shape problem with a valid finite-shift dual and select its supports globally, or obtain another matching original-law lower/upper certificate. The unknown support vector and nonlocal tail envelope cannot be silently dropped. The original all-ε target is not declared solved by this representation.

The small-optimum matching manuscript remains a separate CONDITIONAL candidate at its stated pins and regime. Neither that manuscript nor this representation is promoted from these derivations. Standard convexity, layer-cake, compactness and morphological tools are not claimed inventions. NOVELTY_UNCLEAR remains. No scientific execution or independent verification was performed.
