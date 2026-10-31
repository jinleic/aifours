# A universal three-cycle capacity reduction for the remaining PH7 graphs at 8/9

**WRITTEN CANDIDATE; independent peer review pending.** MathResearch96h-2. This is a necessary all-topology reduction, not yet an unsatisfiability proof. Its relevance is that the separately frozen `frontier-20261028-ph7-critical-two-or-three-cycle-theorem-v1.md` rules out the no-2/no-3 case, leaving graphs with a 2-cycle or a 3-cycle. That stronger theorem is under independent review; no acceptance is presumed here.

## 1. Universal conditions if there is no directed 2-cycle

Let G be any irreducible seven-state Metzler matrix with spectral bound0 and the target characteristic factor `D(y)=y[(y+1)^2+8/9]^2`. Positive Perron similarity converts it to a ROW generator without changing its diagonal. Sort its positive diagonal escape rates as

    0<a<=b<=c<=d<=e<=f<=g,

and let `e_j` be their elementary symmetric functions. Define

    q=e2-4e1+74/9,
    F=e3-4e2+(74/9)e1-28/3,
    H=e4-(70/9)e2+(212/9)e1-1007/27.

If its graph has NO directed 2-cycle, then necessarily

    q>0,       F>=0,
    H >= F(a+b+c+d),
    F <= e f g + b c d.                              (CAP)

All inequalities are exact and apply to arbitrary edge count and placement. If it has a directed 3-cycle, then F>0. Thus an 8/9 PH7 counterexample with no 2-cycle must solve(CAP) with F>0, assuming the separately stated no-2/no-3 obstruction.

## 2. Coefficient and outside-sum derivation

The determinant permutation expansion gives

    c6=e1, c5=e2, c4=e3-C3,
    c3=e4-[sum_(3-cycles C) w_C sum_(i outside C)u_i]-C4,

where C3 is the sum of directed 3-cycle weight products `w_C>0` and C4 is the sum of directed 4-cycle products. No 2-cycle terms or disjoint 2+2 terms are present. Matching the target characteristic polynomial gives `q` as above, `F=C3`, and

    H=C4+sum_(3-cycles C) w_C sum_(i outside C)u_i.

Every complement of a 3-cycle contains four of the seven diagonal rates, so its sum is at least `a+b+c+d`. Hence `H>=F(a+b+c+d)`. Irreducibility gives hidden Q Hurwitz, so q>0. These equations retain every 3- and 4-cycle and all short-cycle signs; they do not equate H with a single cycle unless the graph actually has that structure.

## 3. Exact capacity bound by random deterministic row maps

For the row generator, write each off-diagonal rate as `G_ij=u_i P_ij`, with `P_ij>=0`, `P_ii=0`, and each row of P summing to1. Independently let each vertex choose one successor according to its row of P. The resulting deterministic directed graph has outdegree exactly1 at each vertex, so all its directed cycles are vertex-disjoint.

The probability that any specified directed 3-cycle appears is the product of its three P entries. Consequently `F=C3` is exactly the expectation of the sum, over 3-cycles of the random deterministic graph, of `product_(i in C) u_i`. At most two disjoint triples fit in seven vertices.

The maximum sum of the products of two disjoint triples is `e f g+b c d`: leaving out any rate other than the smallest a cannot increase the sum, and among partitions of the six largest rates the maximum puts the largest three in one triple and the remaining three in the other. For the latter, the product of the two triple products is fixed, and `x+K/x` is convex, so its maximum over the possible products occurs at the extreme largest/smallest triple product. A graph with only one 3-cycle is also bounded by this nonnegative sum. Taking expectations gives the final inequality of(CAP). This argument does not require the stochastic deterministic maps to be irreducible and does not assume the cycles of the original graph are vertex-disjoint.

## 4. A smaller exact system for a single triangle and no four-cycle

If the graph has exactly ONE directed 3-cycle C and no directed 4-cycle, let its three diagonal rates be `x1,x2,x3` and the four outside rates `v1,...,v4`. Then the actual coefficient equations sharpen to

    F=w_C,       H=F(v1+v2+v3+v4),
    0<F<=x1 x2 x3,      q>0.                        (ONE3)

The final bound follows because each directed edge rate leaving vertex i is at most its row escape rate xi. In the eight-edge theta/figure-eight classification, the three remaining shapes with short cycle length3 and other cycle length>=5 fall in this subcase. The two shapes with a 2-cycle are not covered. No solution or exclusion of(ONE3) is claimed here.

Both(CAP) and(ONE3) are finite rational polynomial inequalities in the rates. Numerical explorations are not evidence of emptiness; an exact universal sign/SOS/CAD argument or an actual witness remains necessary. No PH7 answer at8/9, minimum8, novelty, independent-review acceptance or historical process cure is claimed.

END — full no-2-cycle candidates satisfy an exact 3-cycle capacity and outside-sum bound; one-triangle/no-four-cycle graphs satisfy an even smaller system.
