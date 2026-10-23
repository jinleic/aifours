# Exact trades in 1-RQLS: lemma, the Parker/Z_9+1 classical points, and the trade-reachable cardinality

Recorded 2026-10-19T03:21:09-0700 (from /bin/date). Author ContinueRQLS10b; lead from the parent (IRC 03:0x). Lane-internal,
single author, unreviewed. Unrestricted 1-RQLS statements (Lemma T) are about moves, not about existence of maximal
squares; the target stays OPEN / UNKNOWN. No novelty claim.

## 1. Trade lemma (written, complete)
Setting: B a Latin square of order v, unit vectors q_p (p a cell), "lines" = rows, columns, B-classes; a 1-RQLS when
every line is an orthonormal basis (ONB) of C^v.
Lemma T. Let W be a k-dimensional subspace and C a set of cells such that, for every line L meeting C, the vectors of
L n C form an ONB of W. For any unitary V of W (extended by the identity on W-perp) put q'_p = V q_p (p in C),
q'_p = q_p otherwise. Then q' is a 1-RQLS with the same B.
Proof. Lines missing C are unchanged. If L meets C, L n C is an ONB of W, so the other vectors of L lie in W-perp and
are fixed by V, while V maps the ONB of W to an ONB of W; hence L' is an ONB.
Lemma T2 (k = 2, component form). Let S_W = {p : q_p in W}. A line meets S_W in at most 2 cells and, if in 2, they form
an ONB of W. Let Gamma_W be the graph on S_W with one edge per line meeting S_W twice (simple: two cells share at most
one line). If C is a union of connected components of Gamma_W in which every cell has degree 3, C satisfies Lemma T.
Proof. If p in C lies on L, degree 3 gives a second W-cell p' on L, adjacent to p, so p' in C and L n C = {p, p'}.
Classical case. For q_p = e_A(p) with A orthogonal to B and symbols a != b, W = span(e_a, e_b): S_W = the 20 cells
with A in {a, b}; every line has exactly one a-cell and one b-cell, Gamma_W = G_(a,b) (cubic bipartite, the union of
three perfect matchings) and EVERY component is admissible. If C = S_W the move is the global unitary V (+) I (gauge).
If G_(a,b) has c_(a,b) >= 2 components and C is a proper union of them, and V moves e_a and e_b off the coordinate axes
(e.g. V = [[3/5, -4/5], [4/5, 3/5]]), the result
has exactly 12 distinct rays (the 10 classical ones and V e_a, V e_b). The curve V(theta) = exp(theta [[0, -conj xi],
[xi, 0]]) is an exact one-parameter family through the classical point.

## 2. The unsymmetric first-order excess is integrated by trades
evidence/classical-tangent-theory-v1.md (733e4548...a375): at a classical point the first-order deformations mod cell
phases are x = xi on the a-cells and -conj(xi) on the s-cells of one component of G_(a,s) (one xi in C per component);
the gauge spans the "constant over the components of each pair" part; excess = 2 sum_(a<s) (c_(a,s) - 1). The tangent
at theta = 0 of the curve of section 1 applied to ONE component is exactly the first-order solution with that xi on
that component and 0 elsewhere. So every excess direction at a classical point is tangent to an exact curve of
1-RQLS(10) (an actual curve, not only a kernel vector). Exact component data (probe below): every Parker pair, in both
roles, has sum (c - 1) = 3, coming from the three pairs of inf symbols {7,8}, {7,9}, {8,9}, each with components of 6
cells (the corner) and 14 cells (the two inf diagonals of the 7 x 7 part); all 42 other pairs are connected. Hence the
6 unsymmetric excess directions at the Parker points are the tangents of these three trade families. All 20 Z_9+1 pairs
(both roles) have sum (c - 1) = 0: no non-gauge trade there (consistent with their excess 0 / local rigidity).
Remark (dimension). Near a Parker point the block-rotation family of section 3 (mod gauge and cell phases: the relative
position T^3 \ U(3) / T^3 of two ONBs of the 3-dimensional inf space) is 4-dimensional at generic points; the
6-dimensional first-order space is its tangent cone at the singular point "both ONBs equal".

## 3. How far successive trades go at the Parker points
Block structure (exact, from the Z_7 + 3 structure of both squares, here for vectors from A and resolution B; the other
role is symmetric). The 30 cells with A in {7,8,9} split into F (21 cells on the three A-inf diagonals of the 7 x 7
part) and K (the 9 corner cells), and no line meets both: finite rows, finite columns and the 7 finite B-classes meet
only F; corner rows, corner columns and the 3 B-inf classes meet only K (their non-corner cells carry finite
A-symbols: A(inf_r, j) = j + gamma_r, A(i, inf_c) = i + delta_c, and a B-inf class holds the three corner cells with the
three A-inf symbols). Lemma T with k = 3 and W = E_inf = span(e_7, e_8, e_9) therefore lets F and K be rotated by two
independent unitaries of E_inf.
Proposition 3 (R-trades: exact ceiling 13). Every configuration reachable from a Parker classical point by successive
trades with the rational rotation R (any planes, any order, commuting or not) has: finite-symbol cells unchanged, F
carrying an ONB (f_7, f_8, f_9) of E_inf constant along each A-inf diagonal, K carrying an ONB (c_7, c_8, c_9)
constant on each corner symbol class; hence at most 7 + 3 + 3 = 13 distinct rays, and 13 is attained.
Proof. Induction over moves; let W be a plane and C an admissible component. (i) W containing two finite rays e_a, e_s:
Gamma_W = G_(a,s), connected (exact data), so C = S_W, every other ray is orthogonal to W: gauge. (ii) W = span(e_a, y)
with y in E_inf: if y is carried only in F, the a-cells on K-lines have degree < 3; the only a-cell of degree 3 is one
finite-part cell (the 3 a-cells in inf rows, the 3 in inf columns and the 3 on B-inf diagonals have degree 2), and each
y-cell has three distinct a-neighbours, so every component with a degree-3 cell contains a blocked cell: no move; if y
is carried only in K, every a-cell has degree <= 1: no move; if y = f_k = c_k (same symbol) then Gamma_W = G_(a,k) of A,
connected: gauge. A "crossed" coincidence f_k = c_m (k != m) never occurs for R-trades: f = V_F e and c = V_C e with
V_F, V_C products of rotations by the quaternions 2 +- i, 2 +- j, 2 +- k (body-frame axes), so V_C^-1 V_F = M(q)/N(q)
with q integral of odd norm 5^n, whose off-diagonal entries 2(...)/5^n are never +-1. (iii) W inside E_inf: S_W n F is
a union of whole diagonals and S_W n K of whole corner classes; two diagonals form the connected 14-cell graph, two
corner classes the connected 6-cell graph, a single one is blocked, so moves rotate whole diagonal pairs or whole class
pairs and keep the form. (iv) Any other plane contains at most one configuration ray up to the cases above, its cells
are blocked. Attainment: the commuting pair below gives 13.
General unitary trades. Crossed coincidences ARE reachable with general unitaries (e.g. rotating the corner component
of G_(8,9) by a quarter turn turns the corner symbols 8, 9 into each other), i.e. the classical points of the "crossed
mates" A_pi (corner relabelled by pi) are trade-reachable. The probe below finds that for 58 of the 60 (pair, role, pi)
the finite pair graphs stay connected, but for parker2 in role B (vectors from B, resolution A), pi = (7,9,8) and
(9,7,8), all seven pairs {a, 8} (a finite) acquire a second component of 6 cells (a K_(3,3) on three rows, three
columns and three classes) - there trades can move finite-symbol cells, and the searches reach 14 rays.

## 4. Exact computations (stdlib Fractions; receipt evidence/rqls_exact_trades.receipt.md)
- rqls_exact_trades_v1: components for 25 classical pairs x 2 roles (as stated in section 2); at each of the 10 Parker
  (pair, role) starts: classical 10 rays and 0 bad Gram entries; 6 non-gauge moves; one trade (6-cell corner component)
  -> 12 rays, 0 bad entries; two commuting trades in different planes on disjoint cells -> 13 rays, both orders equal,
  0 bad entries; beam (width 6, depth 5): best 13, reached with overlapping (non-commuting) moves too; 0 moves ever
  touched a finite-symbol cell.
- rqls_exact_trades_v2: the 60 starts (10 x 6 corner relabellings): all 60 crossed mates are orthogonal mates; 58 have
  only the three inf-inf pairs disconnected, 2 (parker2 / role B / pi = 798 and 978) have 7 more ({a, 8}, a finite);
  beam (width 12, depth 6, 15,580 children): best 13 at 58 starts, 14 at the 2 special ones (8 finite-cell rays + 4 + 4
  inf rays, 2 shared); every reported state has 0 bad Gram entries (exact).

## 5. Answer to the lead
Trades are exact and genuinely non-classical (12-14 rays), and they explain the unsymmetric excess exactly. They do
NOT approach 100: from the Parker points rational R-trades stop at 13 (proved), general unitary trades reach at least
14 via a crossed mate and saturated at 14 in the bounded search; each trade moves whole graph components, so rays stay
shared by several cells. Nothing near a maximal configuration; no 100-ray claim. Open: an upper bound for general
unitary trade sequences (a full search over crossed states), and trades from other classical OLS(10) with many
disconnected pair graphs.
