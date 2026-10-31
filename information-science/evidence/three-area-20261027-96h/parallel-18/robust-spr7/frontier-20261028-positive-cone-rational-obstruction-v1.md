# Septic common numerators are Hurwitz: a nonpositive-cone obstruction and a rational strict-witness route

Owner **InfoSPR7-2**, slot info-2. Actual preceding `/bin/date`: **Wed Oct 28 18:06:13 PDT 2026**. **WRITTEN author-unreviewed candidate.** This gives an exact additional dual representation and a conditional rational negative-witness route; it does not claim that any strict certificate or counterexample exists.

## 1. Original objects and named inputs

Let K be ANY actual independent closed monic septic coefficient box, degenerate widths allowed, all of whose members are strictly Hurwitz. The registered target requires one real b of EXACT degree7 such that `Re[b(iw)/a(iw)]>0` for EVERY a in K and every finite real w. Denominator and numerator orientation is b/a.

Import the original definition packet SHA256 `d86737954bee95836e2d2cffade9cba15a99f2bb486b660ada2562c25fc764ad`; the full rational-box/four-corner paper `frontier-20261028-rational-box-rational-numerator-reduction-v1.md`, SHA256 `6d29bc63925a100394b1b3efc8fe9fecf49660f7c6ff19798ba246e42442f328`; and the complete eight-atom alternative `frontier-20261028-connected-eight-atom-algebraic-obstruction-v1.md`, SHA256 `d8c1deeab9439e9f0644e2fde45c40a0c188904fbb2a56a8afdc8e989b4d90ac`. These are author-WRITTEN candidates and are not promoted by this import. The new homotopy argument below is independent of the eight-atom support claim; the exact finite dual equivalence explicitly consumes that full claim.

## 2. Every common numerator is Hurwitz with positive coefficients

Fix any actual a in K. A common exact-degree-seven b has leading coefficient b_7>0, because `b(iw)/a(iw)` tends to b_7 and cannot tend to a negative number while its real part is positive at all finite w. Divide by b_7, so both a and b are monic. Let

`a_theta=(1-theta)a+theta b`, `0<=theta<=1`.

For every real w,

`Re[a_theta(iw) conjugate(a(iw))]`
`= (1-theta)|a(iw)|^2 + theta Re[b(iw) conjugate(a(iw))] > 0`.

The first term is positive whenever theta<1 because a is Hurwitz; the second is positive whenever theta>0 by the actual SPR hypothesis. Thus `a_theta(iw)` never vanishes at ANY finite real w, including zero and theta=0,1. The segment remains monic degree7. Root continuity makes the count of roots in the open right half-plane constant along the segment; starting at Hurwitz a, its endpoint b is **strictly Hurwitz**.

Factoring b into real negative-root linear factors and conjugate left-half-plane quadratic factors shows every coefficient is strictly positive: each factor has positive coefficients and their product contains every intermediate degree. Hence every normalized original common numerator satisfies

`b_j>0 for j=0,...,7`, with `b_7=1`.

This is a NECESSARY fact derived from the full original pairing, not a pre-imposed positive-coefficient ansatz. The same proof shows `conv(K union {b})` is entirely Hurwitz: every point of that convex hull is `(1-theta)a+theta b` for some a in the convex K. The hull-stability condition alone is not claimed sufficient for SPR.

## 3. Exact nonpositive-coordinate dual alternative

Let `V_i(x) in R^8` be the four ACTUAL compactified pairing coefficient curves of the eight-atom predecessor, with `0<=x<=1`. Every original pairing is positive exactly when `V_i(x) dot b>0` for all i,x; x=1 records b_7 and introduces no extra restriction for an exact-degree original witness. Let a **nonpositive-cone certificate** be

`r<=8`, `i_k in {1,2,3,4}`, `0<=x_k<=1`, `lambda_k>0`, `sum lambda_k=1`,
`F_j:=sum_k lambda_k V_(i_k,j)(x_k) <=0` for all `j=0,...,7`.

**Theorem.** K has no original common exact-degree-seven numerator IFF such a certificate exists.

For the forward direction, the imported complete eight-atom alternative supplies an actual-corner certificate with **all F_j=0**, which is a special case. For the reverse, suppose b is an original witness. Section2 forces every b_j>0, and consequently `F dot b<=0`. But the same scalar is a positive weighted sum of actual strict pairings `V_i(x) dot b>0`, including at x=1, a contradiction. This includes F=0 and also certificates with only one strictly negative coordinate. It is an exact original-object obstruction, not a freely chosen vector or an assertion that any particular sign pattern is attainable.

Equivalently, for the compact convex hull C of the four curves, failure is `C intersects the closed nonpositive orthant`. The stronger-looking original zero-cancellation criterion is still equivalent for this special actual-box C: if such a nonpositive F exists, §2 excludes a common b, and the predecessor then supplies an exact zero in C. No analogous equivalence for arbitrary sets of vectors is asserted.

The legitimate benefit is that to refute a particular K one MAY exhibit eight coordinate inequalities rather than eight exact cancellations. The converse does **not** promise a strict-negative certificate; F=0 may be the only known form.

## 4. Strict negative certificates persist and can be rationalized

Assume, conditionally, that an actual K has a certificate as in §3 with the stronger property `F_j<0` for ALL eight j. Let `gamma=min_j(-F_j)>0`. Since K is compact and consists only of monic Hurwitz polynomials, there is eta>0 such that every coefficient vector within sup distance eta of K remains Hurwitz.

Consider any valid monic endpoint box K' whose lower and upper endpoints each differ from K's by at most delta, with `delta<min(eta,gamma/4)`. Map each a' in K' to a in K using the same interval interpolation parameter coordinatewise; this works for degenerate intervals and gives sup coefficient displacement at most delta. Thus K' is entirely Hurwitz. For each indexed actual corner i retain its parity endpoint-selection rule and the SAME x_k and lambda_k.

The coefficient of b_k in a compactified pairing is

`V_(i,k)(x)=sum_(0<=j<=7, j+k even) (-1)^((k-j)/2)`
`       a_(i,j) x^((j+k)/2) (1-x)^(7-(j+k)/2)`.

For x in `[0,1]` each displayed basis factor has absolute value at most1. At most four coefficients a_j with j<=6 have the required parity, and the leading a_7 remains1. Hence each `|V'_(i,k)(x)-V_(i,k)(x)|<=4delta`; because the lambda weights are positive and sum1, `F'_k<=-gamma+4delta<0`. Section3 therefore rules out any common numerator for EVERY such K'. For positive-width K this includes an ordinary open neighborhood in all fourteen endpoints; for a degenerate K it is a relative neighborhood of valid boxes, with nearby positive-width boxes available.

By rational density choose outward rational endpoints within this radius, making all seven widths positive. The eight strict inequalities and positive weights are continuous in endpoints, compactified nodes and normalized weights. Consequently one may also choose every x_k rational in `[0,1]` and every lambda_k positive rational with sum1, close enough to retain all eight strict signs. Thus:

**Conditional rational-witness theorem.** If ANY original eligible K admits a STRICT coordinatewise-negative certificate, then there is an eligible rational, seven-positive-width box with a finite certificate of <=8 actual corners, rational compactified nodes, rational positive weights, and eight rational strict-negative coefficient sums. This also yields an open family around that positive-width rational box. Such a certificate is checkable with exact rational arithmetic and the rational-box stability predicate from the predecessor.

The premise is stronger than mere original failure. The earlier algebraic zero-annihilator theorem does NOT imply that this strict premise is ever satisfied; there is no assertion that every negative box has rational nodes or a stable neighborhood of negative boxes.

## 5. Assurance and remaining gap

The homotopy, coefficient positivity and strict-certificate perturbation are written elementary arguments. The eight-atom and rational-stability callers are explicitly conditional on their complete named, unreviewed sources. Root continuity, compactness and rational density are ordinary named facts. No numeric instance, interpreter, solver, enumeration, scientific subprocess or external model was used for this result; no false precision, common-numerator optimality, novelty or original universal verdict is claimed.

The remaining scientific task is either to rule out ALL actual nonpositive-cone certificates, or to produce one valid actual K and certificate; the strict rational certificate is an especially checkable conditional route, not a substitute for that full alternative. The original problem remains OPEN. All previous process findings/STOP/HOLD/ZERO histories remain, without being used as mathematical premises or retrospectively reclassified.

**END.**
