# First-order deformations at classical 1-RQLS points, unsymmetric and Z_7 + 3 forced form (v1)

Recorded 2026-10-18T23:54:32-0700. Lane-internal written derivation by ContinueRQLS10; unreviewed. Local, restricted statements only.
Exact finite inputs: evidence/classical_tangent_count_v2.result.json (sha256
724884347837943eb1a568c67b403de4e3db73dfb836eabd882b0bed96c1348f), computed from the five classical Parker-type pairs in
evidence/parker_z7p3_classical_v1.result.json.

## 1. Unsymmetric first order

Let X be a Latin square orthogonal to the resolution R, q_p = e_X(p). Perturb q_p = e_X(p) + eps delta_p with
delta_p = sum over s != X(p) of x_p(s) e_s (cell phases removed). For p != p' on a line, d<q_p,q_p'> = 0 reads
x_p'(X(p)) + conj(x_p(X(p'))) = 0. For symbols a != s let G_(a,s) be the graph on the a-cells and s-cells of X with an
edge between an a-cell and an s-cell sharing a row, a column or an R-class. Every row, column and R-class (X orthogonal
to R) contains exactly one a-cell and one s-cell, so G_(a,s) is a union of three perfect matchings: cubic, bipartite.
The equations say x_p'(a) = -conj(x_p(s)) on every edge {p,p'}, p an a-cell, p' an s-cell, and involve no other
unknowns. On a connected bipartite component the solutions are exactly x = xi on its a-cells and -conj(xi) on its
s-cells, xi in C. Hence

  dim_R (first-order deformations mod cell phases) = 2 * sum over a<s of c_(a,s),

c_(a,s) the number of components. The gauge u(v) acts (mod cell phases) by x_p(s) = X_(s,X(p)), i.e. one complex
parameter per symbol pair, constant over the components of that pair: dimension v(v-1). So

  excess (unsym) = 2 * sum over a<s of (c_(a,s) - 1),

and the excess directions are independent 2-symbol trade rotations on single components (the moves of R1). This makes
the old lane's remark "near classical points deformations are only 2-symbol trade rotations" precise at first order.

## 2. Z_7 + 3 ansatz

In the symbol basis U e_t = e_(t+1) (t in Z_7) and U e_(inf_k) = omega^(m_k) e_(inf_k) (omega = e^(2 pi i/7)). The ansatz'
tangent space at a classical Z_7-invariant point is the subspace fixed by the twisted action
x_(g p)(g s) = lambda_(X(p))^(-1) lambda_s x_p(s), lambda_t = 1, lambda_(inf_k) = omega^(m_k). g moves every symbol pair
except the three pairs {inf_k, inf_l}, so a component of any other pair lies in a free Z_7-orbit (one complex
parameter per orbit), while a g-invariant component of {inf_k, inf_l} must satisfy xi = omega^(m_l - m_k) xi.
With N7 free component orbits and N1 g-invariant components:
- forced form (m_1, m_2, m_3 distinct): dim = 2 N7; the commutant of U has dimension 16 and its symbol-diagonal part
  (acting by phases) dimension 4, so the gauge orbit has dimension 12 and spans exactly the "constant over components"
  parameters of the three finite-pair orbits and three mixed-pair orbits. excess_forced = 2 N7 - 12;
- classical U = shift (+) I_3: dim = 2 (N7 + N1), gauge orbit 22 - 4 = 18, excess = 2 (N7 + N1) - 18.

## 3. Result for the five Parker-type pairs (both roles: QLS = A with resolution B, and the reverse)

All ten cases: c_(a,s) = 1 for the 42 pairs other than {inf_k, inf_l}; each of the three inf-inf graphs has exactly two
components, the 14 finite cells on the two inf-diagonals and the 6 corner cells, both g-invariant. Hence
unsym excess 6 (three corner-or-diagonal trade rotations beyond gauge), N7 = 6, N1 = 6,
**excess_forced = 0** and excess with classical U = 6.

**Local rigidity (restricted).** With excess 0 the Zariski tangent space of the forced-form solution set at these
points equals the tangent space of the compact gauge orbit; by the slice theorem the point is isolated modulo gauge.
So in the Z_7 + 3 forced form (any distinct labels), no solution other than gauge images, in particular no maximal
one, lies near these ten classical points. This does not exclude maximal forced-form solutions elsewhere, nor near
other classical Z_7 + 3 pairs with more components. The L stage of the proposed assay (Jacobian kernel minus gauge and
representative-phase tangents at 300 classical forced-U points) is predicted to report excess 0 everywhere; a nonzero
numerical rank deficiency there would indicate a numerical or bookkeeping defect, not a deformation.
