# A nine-transition Hamiltonian-connector subcase is impossible

Status: **WRITTEN; one displayed Bernstein expansion WRITTEN-checked-in-kernel by rational symbolic arithmetic**. This is an exact spectral exclusion for the graph defined below, not an exclusion of all nine-transition graphs and not a solution of PH7 at `z=8/9`. It has not yet received the parent or an independent mathematical audit. It uses no selected numerical generator. The critical PH application also uses the separately review-pending graph-template reduction named in §4.

## 1. Statement and notation

Let `G` be a seven-state irreducible row generator with exactly these nine positive off-diagonal transitions: two vertex-disjoint directed triangles `A` and `B`; one edge from a vertex of `A` to a vertex of `B`; one edge from a vertex of `B` to the remaining vertex `x`; and one edge from `x` to a vertex of `A`. Suppose the three connector edges together with triangle edges form a **directed Hamiltonian 7-cycle**. Equivalently, within each triangle the connector enters at the successor of the connector's departure vertex and then traverses both internal edges before leaving.

Then no eigenvalue `lambda=-d+ib` with `d>0` and `b^2/d^2 >= 3/4` has algebraic multiplicity at least two. The sign of `b` is immaterial. In particular this graph cannot realize the repeated target pair at `z=8/9`.

Here a row generator has nonnegative off-diagonal entries and zero row sums; each listed edge is strictly positive. The conclusion concerns the characteristic polynomial only, so it excludes every choice of PH initial and exit vectors on this graph.

## 2. A three-cycle logarithmic-derivative lemma

Let `r1,r2,r3>0`, `0<=theta<=1`, and

`C(y)=(y+r1)(y+r2)(y+r3)-theta*r1*r2*r3`.

For `y=-1+ib`, `b>0`, and `z=b^2>=3/4`, one has `C(y) != 0` and

`Im(C'(y)/C(y)) < 0`.

Proof. Put `S=r1+r2+r3` and `v_i=(r_i-1)^2+z`. A direct expansion gives the exact identity

`-Im(C'(y)*conj(C(y)))/b = N := v1*v2+v1*v3+v2*v3+2*theta*r1*r2*r3*(S-3)`.

If `S>=3`, every `v_i>0` and the last term is nonnegative, so `N>0`.

Suppose `S<3`. Write `s=S/3` and `F=v1*v2+v1*v3+v2*v3`. On the positive simplex of this fixed sum,

`(partial_i F - partial_j F)/(2*(r_i-r_j)) = (r_k-1)^2 + 2*z - (r_i-1)*(r_j-1)`

when `r_i != r_j`. If both `r_i,r_j<1`, their last product is less than 1; if both exceed 1, their positive deviations have sum less than 1 (because `S<3`), so their product is less than `1/4`; if their deviations have opposite signs, their product is nonpositive. Therefore the displayed right-hand side is strictly positive since `2*z>=3/2`. Pairwise averaging reduces `F`, and hence

`F >= 3*((1-s)^2+z)^2`.

Also `r1*r2*r3 <= s^3` by AM-GM, and because `S-3<0` and `theta<=1`,

`2*theta*r1*r2*r3*(S-3) >= -6*s^3*(1-s)`.

Consequently `N >= 3*((1-s)^2+3/4)^2-6*s^3*(1-s)`. The latter quartic is strictly positive for `0<=s<=1`: its degree-four Bernstein coefficients, in order `k=0,...,4`, are

`147/16, 63/16, 39/16, 3/16, 27/16`.

That is, the quartic equals the sum of each listed coefficient times `binom(4,k)*s^k*(1-s)^(4-k)`. Every coefficient is positive. Thus `N>0` also when `S<3`. If `C(y)=0` the left side of the identity would vanish, so `C(y)!=0`, and dividing by `|C(y)|^2` gives the strict logarithmic-derivative claim.

The five rational Bernstein coefficients above were additionally computed in this owner's Python kernel using SymPy rational-polynomial expansion and the standard exact power-to-Bernstein formula; the displayed inequality is independently checkable from the formula and is not a formal proof-assistant verification.

## 3. Apply the lemma to the Hamiltonian-connector graph

Let the positive diagonal rates `-G_ii` on the two triangles be `a1,a2,a3` and `b1,b2,b3`, and let the singleton rate be `x>0`. Write `w_A` and `w_B` for the directed triangle edge products, and `w_H>0` for the Hamiltonian connector cycle's edge product. Row-generator constraints give

`0 < w_A/(a1*a2*a3) < 1` and `0 < w_B/(b1*b2*b3) < 1`,

because each triangle has exactly one vertex with both an internal positive edge and a positive connector edge. Put

`A(y)=prod_i(y+a_i)-w_A`, `B(y)=prod_i(y+b_i)-w_B`.

The determinant expansion over directed vertex-disjoint cycles is exactly

`det(y I-G) = (y+x)*A(y)*B(y) - w_H`.

Indeed the only simple directed cycles are the two disjoint triangles and the Hamiltonian connector cycle; their only nonempty disjoint pair is the two triangles. The Hamiltonian cycle uses all seven vertices, so its term is the positive product `w_H` with a minus sign and no remaining diagonal factor.

Rescale all rates and `lambda` by `d>0`, so the putative repeated root is `y=-1+i*sqrt(z)`. At any root of the determinant, `(y+x) A(y) B(y)=w_H>0`, so the three factors are nonzero. If it were a repeated root, differentiating the product and dividing by `w_H` would yield

`0 = 1/(y+x) + A'(y)/A(y) + B'(y)/B(y)`.

The imaginary part of the first term is `-sqrt(z)/|y+x|^2<0`. Each of the other two imaginary parts is strictly negative by §2. Their sum therefore cannot vanish. This contradiction proves the statement. Conjugation handles `b<0`.

## 4. Relation to the remaining PH7 graph problem

The separate, as yet parent-unadopted manuscript `frontier-20261028-ph7-critical-nine-edge-graph-template-v1.md` reduces a critical nine-transition PH7 to two disjoint directed triangles plus a connector cycle through the singleton. Label the triangles cyclically so the first connector departs `A` at `A0`, the next enters `B` at `B0`, and `B` is traversed for `k=0,1,2` internal edges before departure. If the last connector enters `A` at a vertex from which `ell=0,1,2` internal edges lead to `A0`, the connector cycle length is `3+k+ell`. The nine `(k,ell)` choices have lengths 3,4,5,6,7 with respective multiplicities 1,2,3,2,1. This paper eliminates only the length-seven choice; it does not assert that the eight other parameter choices are pairwise nonisomorphic or impossible.

The graph-template manuscript depends on the unreviewed target-specific triangle-imbalance capacity and overlap-budget results, and its PH caller additionally rests on the round's separately supported irreducibility reduction. Neither that pending dependency chain nor this single exact graph exclusion supplies a PH7 existence/exclusion at `8/9`, any conclusion for ten or more transitions, novelty clearance, an executable certificate, or formal verification. Earlier numerical optimizations are diagnostics only and are not inputs to this proof.
