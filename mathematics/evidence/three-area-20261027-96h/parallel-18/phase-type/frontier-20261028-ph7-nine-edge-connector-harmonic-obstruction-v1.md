# Universal harmonic constraint for the nine-edge connector template

Status: **WRITTEN**, pending independent mathematical review. This extends `frontier-20261028-ph7-nine-edge-length-six-connector-separation-v1.md` (SHA256 `ca03dc12f5eb30d2c247b8b37d6cd77ed9568dd96bd25703e728b4a14f977a23`) to all connector lengths. It imports the full-three-cycle logarithmic-derivative lemma from `frontier-20261028-ph7-nine-edge-hamiltonian-cycle-exclusion-v1.md` and, for §3 only, the one-omission lemma from `frontier-20261028-ph7-nine-edge-omitted-rate-obstruction-v1.md`, both at their unreviewed written cuts. It does not resolve the full original PH7 problem.

## 1. All connector lengths

In the two-disjoint-triangle/singleton graph, let the connector cycle have length `7-m`, so exactly `m` triangle vertices are omitted and `0<=m<=4`. Let `x>0` be the singleton's diagonal rate, and `t_1,...,t_m>0` the omitted vertices' diagonal rates. Suppose the generator has an algebraically repeated eigenvalue `lambda=-d+ib`, with `d>0` and `b^2/d^2>=3/4`. Then necessarily

`sum_{j=1}^m 1/[(t_j-d)^2+b^2] > 1/[(x-d)^2+b^2]`.

For `m=0` the sum is zero, yielding the previously proved unconditional Hamiltonian-connector exclusion. For `m=1` it becomes the strict separation `(x-d)^2>(t_1-d)^2`. The inequality imposes a rate restriction for every other connector length as well.

Proof. In the normalized variable or directly in the original scale, directed-cycle expansion gives

`P(y)=(y+x)*A(y)*B(y)-w*prod_{j=1}^m(y+t_j)`,

where `w>0` is the connector-cycle transition product and `A,B` are the two triangle polynomials. At the nonreal root no linear factor vanishes and the root equation ensures `A(lambda),B(lambda)!=0`. A repeated root implies

`A'(lambda)/A(lambda)+B'(lambda)/B(lambda) = sum_j 1/(lambda+t_j) - 1/(lambda+x)`.

Each summand on the left has strictly negative imaginary part by the imported full-block lemma, after scaling by `d`. Taking imaginary parts and dividing by `b>0` yields the displayed strict inequality. Complex conjugation handles negative `b`.

## 2. An explicit critical exclusion band for length five

At `z=b^2/d^2=8/9`, suppose the connector has length five, so `m=2`. If **both** omitted rates are at least `2d`, the singleton rate must obey

`|x-d| > d/(3*sqrt(2))`.

Indeed each omitted denominator is at least `d^2+b^2`, so the left side in §1 is at most `2/(d^2+b^2)`. If `|x-d|<=d/(3*sqrt(2))`, its right side is at least `1/(b^2+d^2/18)=2/(d^2+b^2)`, contradicting strictness. This is a necessary band, not an assertion that the remaining region is feasible.

## 3. Paths avoiding the singleton and a stronger length-five corollary

For a PH target transfer of relative degree five, suppose every supported simple input-to-exit path avoids the singleton. As in §2 of the length-six separation manuscript, nonnegativity excludes supported paths of length below four; the unvisited principal complement of a supported length-four or length-five path has determinant divisible by `y+x`, because the template graph has no two-cycles. Hence the adjugate numerator and the hidden quadratic `Q` are divisible by `y+x`. The exact determinant then forces

`prod_{j=1}^m(t_j-x)=0`.

Thus some omitted rate must equal `x` (and `m=0` is impossible). For `m=1` this is incompatible with §1, giving the earlier singleton-path necessity.

For `m=2`, suppose one omitted rate equals `x` and call the other `u`. Factoring the determinant gives

`P(y)=(y+x)*[A(y)*B(y)-w*(y+u)]`.

At a repeated nonreal root the bracket has a repeated root. Its logarithmic derivative equation has one full triangle block and one triangle block divided by `(y+u)`. If `u>=2d`, the imported one-omission lemma and the full-block lemma make the imaginary part of that equation strictly negative, a contradiction. Therefore **when all supported paths avoid the singleton in a length-five graph, one omitted rate equals `x` and the other is strictly less than `2d`**. This holds whether the two omissions belong to the same triangle or different triangles.

For example, with quotient orientation `A -> B -> singleton -> A`, input entirely in `A` and exit entirely in `B` has all simple supported paths avoiding the singleton, so it satisfies this equality and remaining-rate bound. No assertion is made about other input-output support choices.

The graph-specific conclusions do not require the pending universal template; applying them to all nine-transition critical PH7 candidates does. The capacity/overlap-budget, template, full-/one-omission lemmas, parent-adoption, formal-verification and novelty cuts remain exactly as stated in the referenced sources. No selected state, numerical exclusion, multisupport resolution, ten-edge conclusion, or 8/9 decision is claimed.
