# Exact spectral reduction for all strongly connected seven-vertex, eight-edge graphs

**WRITTEN CANDIDATE; topology classification and formulas are not independently reviewed.** MathResearch96h-2, original math-1. This is a new representation of the remaining 8/9 question, not an exclusion or construction. Exact full-matrix numerator/PH realization remains an essential separate condition.

## 1. Fourteen graph shapes cover the entire 8-edge case

Let a directed graph on seven vertices have exactly eight distinct off-diagonal edges and be strongly connected. Every vertex has outdegree >=1, so exactly one vertex p has outdegree2 and all others have outdegree1. Similarly, exactly one vertex q has indegree2 and all others have indegree1.

Follow the two outgoing branches from p. Before encountering each other or returning to p they cannot enter a cycle not containing p, because every non-p vertex has only one outgoing edge and such a cycle could not reach p. Thus they meet at q (possibly q=p); when q!=p their unique shared return path goes from q to p. Every vertex lies on those two branches or their shared return path, since it is reachable from p. Let k be the number of edges of the shared return path, and l,m the numbers on the two p-to-q branches. Then

    k+l+m=8,    k>=0,    l<=m.

If k=0, the branches are two directed cycles with one shared vertex, so l,m>=2. If k>0, l,m>=1 but `(l,m)=(1,1)` is forbidden because it would be two copies of the same directed edge. The two branch labels are interchangeable. Thus the complete list is

    (k,l,m) = (0,2,6),(0,3,5),(0,4,4),
              (1,1,6),(1,2,5),(1,3,4),
              (2,1,5),(2,2,4),(2,3,3),
              (3,1,4),(3,2,3),
              (4,1,3),(4,2,2),
              (5,1,2).                              (SHAPES)

For k=0 the graph is a figure eight. For k>0 it is a directed theta graph. This classification is literal graph theory, not an optimizer-inferred list. A vertex/edge permutation or positive diagonal similarity does not change the graph shape.

## 2. Necessary and sufficient equations for the spectral part

Let G be an irreducible Metzler matrix on one of these graphs with spectral abscissa0. Write its diagonal `G_ii=-u_i`. The positive Perron right vector and `Gv=0` imply EVERY u_i>0. Call the two simple directed cycles C1,C2, whose edge-weight products are A,B>0. They share at least one vertex; hence the determinant permutation expansion has just the diagonal term and one term for each simple cycle, no disjoint-cycle product. Exactly

    P(y)=product_i(y+u_i)
         - A product_{i notin C1}(y+u_i)
         - B product_{i notin C2}(y+u_i).            (P)

At y=0, introduce

    theta=A/product_{i in C1}u_i,
    1-theta=B/product_{i in C2}u_i,
    0<theta<1.                                      (NORM)

For any fixed z>0 and `lambda=-1+i sqrt(z)` define

    F_j = product_{i in Cj} u_i/(lambda+u_i),
    S_j = sum_{i in Cj} 1/(lambda+u_i).              (FS)

Since lambda is nonreal, no denominator vanishes. The target nonreal pole has algebraic multiplicity at least2 **iff** the following TWO COMPLEX equations hold:

    theta F_1+(1-theta)F_2=1,
    theta F_1 S_1+(1-theta)F_2 S_2=0.               (SPEC)

Indeed they are exactly `P(lambda)=0` and `P'(lambda)=0`, after dividing by the nonzero diagonal product. Real coefficients then give the conjugate with the same multiplicity. These equations allow all real positive u_i independently and all theta in(0,1); equal rates are not assumed.

Conversely, for any shape in(SHAPES) and any positive u_i,theta satisfying(SPEC), choose the common-path edge weights1 and all branch edge weights1 except one unique edge per branch; set those two exceptional edge weights to the positive A and B determined by(NORM). This realizes the literal P. It is an irreducible Metzler graph with eigenvalue0. Its spectral abscissa must be0: the Perron root is real, and for each real y>0 the normalized expression `P(y)/product_i(y+u_i)` is strictly positive because every factor `u_i/(y+u_i)` is in(0,1). Thus no positive real root can be Perron. The conjugate target pair is at least double, and because 0 is simple for an irreducible Metzler matrix,

    P(y)=y[(y+1)^2+z]^2 Q(y),

where Q is a real monic quadratic whose roots lie strictly in the left half-plane. Therefore(SPEC), over all(SHAPES), is an exact IFF for the **nonnegative-matrix spectral skeleton** of the 8-edge problem.

It is NOT an iff for the original PH transform: one must still construct nonnegative input and exit vectors with the original four-edge delay, verify the actual numerator `K Q` of the SAME matrix, and perform positive diagonal PH normalization. A spectral skeleton alone is not a PH witness.

At z=8/9, one can express(SPEC) with rational coefficients by adjoining a formal symbol eta with `eta^2=-8/9`, setting lambda=-1+eta, multiplying by the positive real denominator products, and setting both coefficients in the basis(1,eta) to zero. Hence each case is an explicit finite semialgebraic feasibility problem in eight real unknowns `(u_1,...,u_7,theta)`. Sorting rates inside the common path and within each branch is allowed in this purely spectral test, since only their respective products/sums occur; this sorting does not assert that arbitrary PH inputs/exits are equivalent.

## 3. Bounded exploration and exact status

The earlier v4 graph at its separate algebraic endpoint is shape `(4,1,3)`: five common vertices and two vertices exclusive to the longer branch. Its exact determinant and normalization were checked in its own source/erratum. Thus this reduction contains and correctly reproduces an existing PH construction below 8/9; it does not merely change nomenclature.

The exploratory `frontier-20261028-ph7-eight-edge-spectral-search.py` considered all 14 abstract shapes with u_i in `[1/20,10]`, theta in `[10^-5,1-10^-5]`, four numerical starts each, z=8/9, and the four real parts of(SPEC) as residuals. All 14 shapes were attempted; the best numerical residual was about0.127 for `(4,1,3)`. The first seed for that shape came from the earlier exact algebraic endpoint; separate floating arithmetic at the actual earlier z verified both complex residuals to about 1e-13. The numerical result is `frontier-20261028-ph7-eight-edge-spectral-search-result.json`. This is only a bounded floating search, not a proof that any case, rate box, shape or PH problem is empty. There was no exact spectral witness at8/9, and no rationalization is implied by a low residual.

## 4. Relation to the 8/9 problem

The earlier WRITTEN candidate `frontier-20261028-ph7-global-irreducibility-v1.md` and the additive `frontier-20261028-ph7-minimum-eight-edges-v1.md` conditionally narrow every hypothetical PH7 representation at z>1/2 to a strongly connected graph with at least8 edges. This file analyzes **only** the exactly8-edge subcase. Even a rigorous proof that all(SPEC) are impossible at8/9 would exclude only eight-edge skeletons and leave all graphs with nine or more edges, not solve the original question. Conversely, any spectral solution must still pass the exact same-matrix numerator/normalization gate.

No independent review, executable exhaustive verification, novelty clearance, PH7 existence, min8 theorem, external publication, held-result adoption or process repair is claimed.

END — complete finite shape and all-variable spectral interface for the 8-edge subcase; exact 8/9 feasibility and all PH numerator questions remain open.
