# Original septic SPR7: at most eight actual-corner atoms, with algebraic witnesses over rational boxes

Owner **InfoSPR7-2**, slot info-2. Actual preceding `/bin/date`: **Wed Oct 28 17:54:10 PDT 2026**. **WRITTEN author-unreviewed candidate.** This tightens the finite actual-box obstruction support from nine to eight by a supplied path-connected convexity argument, and gives an exact algebraic witness representation if any original counterexample exists. It does not exhibit a counterexample or decide universal synthesis.

## 1. Exact assertion and named dependencies

Use the original monic septic box definition in `institute/runs/three-area-2026-10-27-96h/written-releases/info-2-septic-box-definitions-v1.md`, SHA256 `d86737954bee95836e2d2cffade9cba15a99f2bb486b660ada2562c25fc764ad`. Import the full author-written `frontier-20261028-rational-box-rational-numerator-reduction-v1.md`, SHA256 `6d29bc63925a100394b1b3efc8fe9fecf49660f7c6ff19798ba246e42442f328`, for (i) exact-degree/monic normalization and compactified strict positivity, (ii) four actual parity corners, and (iii) the rational seven-positive-width superbox of any hypothetical counterexample. This is a named unreviewed dependency, not an inherited acceptance.

**Theorem A.** For EVERY original eligible K, either it has one unrestricted exact-degree-seven common SPR numerator, OR there are `r<=8`, indices `i_k` among its four ACTUAL corners, frequencies `x_k in [0,1]`, and weights `lambda_k>0` with sum1, such that the exact shared-numerator identity

`sum_(k=1..r) lambda_k V_(i_k)(x_k) = 0 in R^8`

holds. The two alternatives are exclusive. Each V_i(x) is the actual compactified pairing functional defined in §2. Several atoms can share a corner or frequency; no arbitrary member or free coefficient data are substituted for K. The x=1 atom is the normalized infinity functional, not a finite physical frequency.

**Theorem B.** If ANY original eligible real box is a counterexample, then some actual rational-endpoint strictly-positive-seven-width Hurwitz box K has an obstruction of Theorem A with `r<=8` in which **every x_k and lambda_k is real algebraic**. Thus a hypothetical negative answer has a finite exact witness consisting of rational box endpoints, at most eight indexed actual corners, algebraic compactified frequencies and positive algebraic weights, together with the eight coefficient cancellations. Exact algebraic values can be specified by integer polynomials and rational isolating intervals; this is not a claim that all roots/frequencies are rational.

Ordinary named imports: finite-dimensional compactness and continuous polynomial-root dependence, elementary affine linear algebra, exact rational root isolation/Sturm for checking a rational box, and the classical real-closed-field facts that the real algebraic numbers form a real closed field and first-order formulas over rational coefficients transfer between real closed fields. The connected-set support reduction is **proved here**; no external Fenchel theorem or old contact/phase result is assumed. The original full sign is still open.

## 2. Four actual pairing curves and their common endpoint

For an actual a in K and real b of degree at most7 put

`P_(a,b)(t)=Re[b(i sqrt(t)) a(-i sqrt(t))]`,
`T_(a,x)(b)=(1-x)^7 P_(a,b)(x/(1-x))`, for `0<=x<1`,
`T_(a,1)(b)=b_7`.

The last value follows from the monic denominator and the coefficient of t^7. Each T is linear in the SAME eight b coefficients and jointly continuous in a,x. Let V(a,x) be its coefficient vector in R^8. For the four actual parity corners a_i, put V_i(x)=V(a_i,x). The set

`S = union_(i=1..4) { V_i(x): 0<=x<=1 }`

is compact and **path-connected**: each V_i is a continuous curve and every curve ends at the SAME vector `V_i(1)=e_7`, the linear functional `b -> b_7`. Duplicated corners and x=0 cause no difficulty.

For each fixed t>0, actual values `(E_a(t),O_a(t))` fill the rectangle formed by the four actual corners, since the even and odd coefficients vary independently. The coefficient functional V(a,x), considered as a function of a at this fixed x, is linear in these two values. Hence every V(a,x) is a convex combination of `V_i(x)` using one common set of rectangle weights, including boundary and collapsed intervals. At x=0 this follows by continuity, and at x=1 all functionals are e_7. Therefore the convex hull of S equals the convex hull of ALL original `(a,x)` functionals. This is a fixed-frequency rectangle identity, not the false claim that the coefficient box itself has only four vertices.

The predecessor shows that an original common b exists exactly when `V dot b>0` for all V in S, including x=1: a feasible exact-degree b has positive leading coefficient, and conversely positivity at x=1 forces b_7>0. The full continuum of finite frequencies and all actual denominators is retained.

## 3. Supplied path-connected eight-point lemma

**Lemma.** If S is path-connected in R^d and p belongs to its convex hull, p is a convex combination of at most d points of S. The argument below uses no executable search and applies to any d>=1.

Start with any finite representation of p. If it uses more than d+1 points, affine dependence lets us vary the nonnegative weights while preserving both their sum and p until one weight reaches zero. Continue until at most d+1 positive weights remain. If at most d remain, finish. Otherwise remove any further affine dependence in the same way; we have d+1 affinely independent points `s_0,...,s_d` with all weights positive. Thus p is not in the affine hyperplane through `s_1,...,s_d`.

Choose a continuous path `gamma:[0,1]->S` from s_0 to s_1. Write D(t) for the determinant of the d vectors `s_i-gamma(t)`, i=1,...,d. D(0)!=0 and D(1)=0. Let t0 be the first zero of D; continuity makes `0<t0<=1` and D(t)!=0 on `[0,t0)`. For such t the unique affine coordinates of p relative to `gamma(t),s_1,...,s_d` are continuous and sum to1. By Cramer's rule the coefficient of gamma(t) has the form `C/D(t)`, where `C=det(s_1-p,...,s_d-p)` is a fixed nonzero number, since p is outside that affine hyperplane.

Initially every coordinate is positive. If all stayed positive for every t<t0, they would all be at most1, but `|C/D(t)|` becomes unbounded as t approaches t0. Hence at some first t*<t0 one coordinate becomes zero while the others remain nonnegative. The corresponding affine expression is a convex representation of p by at most d points of S. This proves the lemma, including the case where p itself is one of the original points.

## 4. Exact original-box alternative

Let C be the convex hull of S. Elementary affine-weight elimination shows every point of C has a representation using at most nine S points; since S is compact, C is compact as the image of `S^9` times the closed nine-weight simplex. If `0 notin C`, let z be a closest point of C to zero. Segment minimality gives `V dot z >= ||z||^2>0` for every V in C. The coefficient vector z therefore supplies strict positivity on all original functionals. In particular z_7>0 because e_7=V_i(1) belongs to S. By the predecessor's exact-degree caller, z is a common original numerator.

If `0 in C`, the path-connected lemma with d=8 gives an exact convex representation using at most **eight** points of S. Discard any zero weights. Its weighted pairing is zero for every real b of degree at most7, so it is incompatible with any original common numerator. Since each point is literally one of the four actual corner curves, the theorem's vertices and shared box are paid. The alternatives are exclusive and complete.

This is a strict improvement of the general nine-point R^8 Caratheodory count, obtained from the **specific common monic-infinity endpoint**. It does not assume that an arbitrary eight-vector tuple is realizable by an eligible box, nor does it infer anything about which finite-frequency support configurations actually exist.

## 5. Rational boxes admit algebraic atoms

Suppose K has rational endpoints. Each actual corner has rational coefficients `a_(i,j)`. For `k=0,...,7`, the coefficient of b_k in V_i(x) is the rational polynomial

`V_(i,k)(x) = sum_(0<=j<=7; j+k even)`
`   [ (-1)^((k-j)/2) a_(i,j) x^((j+k)/2) (1-x)^(7-(j+k)/2) ]`,

with `a_(i,7)=1`. It is valid on the entire closed interval including x=1. Fix a real eight-or-fewer-atom representation from Theorem A and freeze its finite corner-index word `i_1,...,i_r`. The conditions

`0<=x_k<=1`, `lambda_k>0`, `sum lambda_k=1`,
`sum_k lambda_k V_(i_k,j)(x_k)=0` for j=0,...,7

are a finite existential system of polynomial equalities/strict or weak inequalities over Q. It has a real solution. Because the real algebraic numbers form a real closed field and the real-closed-field transfer theorem applies to this rational-coefficient existential sentence, it also has a solution entirely in real algebraic numbers. No rationality of the x_k or lambda_k is inferred. The eight exact cancellations and positivity bounds can be checked by standard exact algebraic-number operations based on integer polynomials and rational isolating intervals.

If a counterexample exists at arbitrary real or degenerate endpoints, the predecessor constructs an eligible rational superbox with seven positive widths which is still a counterexample. Applying the present theorem to that actual K gives the claimed finite algebraic obstruction. Rational-box eligibility can be checked by the predecessor's exact Routh/univariate-Sturm predicate. Thus enumerating rational boxes, finite words of at most eight corner indices, and algebraic-number descriptions, then checking eligibility, interval/sign/weight constraints and all eight cancellations, is in principle a sound search that terminates IF an original counterexample exists. It has NOT been run and need not terminate when none exists. No complexity, bounded-height, rational-frequency, numerical-solver or novelty claim follows.

## 6. Assurance and remaining gap

The support reduction and compact-geometry caller are complete WRITTEN arguments; the real-algebraic conclusion has the explicit classical transfer import. This is not formal/kernel/human/configured-family verification. The new theorem needs a full frozen-scope review, including the path lemma, the four-corner convex-hull identity, x=1/exact-degree caller, and the predecessor's rational-superbox hypothesis. No scientific interpreter, numerical instance, enumeration, solver, external model, nested agent, Git, deletion or publication was used in this derivation. Prior findings/STOP/HOLD/ZERO histories remain recorded and are not proof premises.

**Original residual:** either prove the joint convex hull avoids zero for every eligible original box, or give ONE actual eligible box with the explicit <=8-atom cancellation. The theorem shows what a finite exact negative witness can look like; it does not supply one or resolve the original universal sign.

**END.**
