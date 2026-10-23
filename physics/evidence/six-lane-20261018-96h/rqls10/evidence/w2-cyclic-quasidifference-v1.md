# W2: cyclic quasi-difference ansatze Z_n + h for 1-RQLS(10) (new representation, v1)

Recorded 2026-10-18T23:29:14-0700. Lane-internal written derivation by ContinueRQLS10; unreviewed. Restricted ansatz only: nothing here is
a statement about arbitrary 1-RQLS(10). The target remains OPEN.

## 0. Ansatz Q(n,h)

Fix n + h = 10 with n >= 2, h >= 1. Rows, columns and symbols are each Z_n u {inf_1..inf_h}. A permutation g acts by
i -> i+1 on the finite parts and fixes every inf, and
- B(i+1, j+1) = B(i,j) + 1 (inf + 1 = inf), i.e. g is an autotopism of B fixing h rows, h columns, h symbols;
- there is a unitary U on C^10 with q_(g.p) parallel to U q_p for every cell p.

Normalisations. Row inf_a is a bijection from columns to symbols commuting with g, so the symbols carry the same
orbit structure (one n-cycle plus h fixed points), and any translation-type action can be relabelled to the one
above. Then U^n q_p is parallel to q_p for every cell. **We study the sub-ansatz U^n = scalar** (after rescaling,
U^n = I and U = sum_m omega^m P_m with omega = e^(2 pi i/n), eigenspaces E_m of dimension d_m). If U^n is not
scalar, every line is adapted to the eigenspace splitting of U^n (a split ansatz in the sense of R5 with an extra
cyclic symmetry); that case is **not covered** here.

Structure of B (forced). Corner cells (inf_a, inf_b) are fixed, so the corner is a Latin subsquare L of order h on the
inf symbols. Column inf_b is g-equivariant from rows to symbols, so B(i, inf_b) is finite for finite i; hence the finite
cells of symbol inf_c form exactly one diagonal orbit {(i, i + d_c)}. Write D_inf = {d_c}, D_fin = Z_n minus D_inf,
B(i, i+d) = i + beta_d (d in D_fin), B(inf_a, j) = j + gamma_a, B(i, inf_b) = i + delta_b. B is Latin iff beta and
beta - id are injective on D_fin, {delta_b} = Z_n minus beta(D_fin), {gamma_a} = Z_n minus (beta - id)(D_fin), and L
is Latin.

Representatives: v_d = q_(0,d) (d in Z_n; u_c := v_(d_c)), w_a = q_(inf_a,0), w'_b = q_(0,inf_b), corner
c_ab = q_(inf_a,inf_b). With q_(g^k p) = U^k q_p the 3n + 3h lines reduce to:
- (R0) row 0 = {v_d : d in Z_n} u {w'_b};
- (C0) column 0 = {U^(-d) v_d : d in Z_n} u {w_a};
- (S0) class 0 = {U^(-beta_d) v_d : d in D_fin} u {U^(-gamma_a) w_a} u {U^(-delta_b) w'_b};
- (Ia) row inf_a = {U^k w_a} u {c_ab : b}; (Ib) column inf_b = {U^k w'_b} u {c_ab : a};
  (Ic) class inf_c = {U^k u_c} u {c_ab : L(a,b) = c}.
All other lines are U-translates of R0, C0, S0. MAX10 under Q(n,h) is: R0, C0, S0, Ia, Ib, Ic orthonormal bases and
all 100 rays distinct.

## 1. Lemmas (exact, elementary)

**Lemma 1 (orbit lines).** {U^k x : k in Z_n} is orthonormal iff ||P_m x||^2 = 1/n for every m. Hence every d_m >= 1
and sum_m (d_m - 1) = h. (Gram entries are the Fourier transform of the weights ||P_m x||^2.)

**Lemma 2 (corner location).** A corner vector c is an eigenvector of U, say c in E_m. If c lies on an inf-line with
the orbit of x, then c is orthogonal to the orbit iff c is orthogonal to P_m x. If d_m = 1, P_m x (norm 1/sqrt n)
spans E_m, which is impossible; so corner vectors lie in eigenspaces with d_m >= 2.

**Lemma 3 (trace identity).** Taking the trace of the E_m-diagonal block of the frame identity for R0 (or C0, S0),
with ||P_m x||^2 = 1/n for the 2h flat vectors u_c, w'_b (resp. u_c, w_a; w_a, w'_b):
  sum over d in D_fin of ||P_m v_d||^2 = d_m - 2h/n   for every m.
In particular d_m >= 2h/n for every m.

**Proposition 4 (which (n,h) survive).**
- n = 6, h = 4: d_m >= 4/3 forces all d_m >= 2, sum >= 12 > 10. **Impossible** (any cardinality).
- n = 4, 3, 2 (h = 6, 7, 8): d_m >= 3, 5, 8 respectively, sum > 10. **Impossible** (any cardinality).
- n = 8, h = 2: the 2x2 corner has all four cells pairwise sharing a row, column or symbol, so the four corner vectors
  are orthonormal inside S = sum over d_m >= 2 of E_m, dim S = 2 + #{m : d_m >= 2} <= 4. If one eigenspace has
  dimension 3, dim S = 3 < 4. Otherwise two eigenspaces of dimension 2 and, by Lemmas 1-2, the two corner vectors of
  each inf-line are the two lines E_m1 minus P x and E_m2 minus P x, one in each eigenspace; so the label map on the
  2x2 corner must differ on every pair of cells sharing a row, column or symbol, i.e. on all six pairs, with only two
  labels. **Impossible** (any cardinality).
- Remaining: (n,h) = (9,1), (7,3), (5,5).

**Lemma 5 (Z_7 + 3 corner forcing).** If the nine corner rays are pairwise distinct then exactly three eigenspaces
E_m1, E_m2, E_m3 have dimension 2 (the other four have dimension 1), and each class of the orthogonal mate of the
corner square L (the three "share-nothing" triples) lies in one of them, bijectively.
Proof. Two corner cells sharing nothing lie in one mate class; cells of different mate classes share a row, column or
symbol, so the spans S_1, S_2, S_3 of the mate classes are mutually orthogonal inside S, dim S = 3 + #{d_m >= 2} <= 6.
Three pairwise nonparallel vectors span >= 2 dimensions, so equality holds throughout: three eigenspaces of dimension 2
and dim S_k = 2. A 2-dimensional span of three nonparallel eigenvectors cannot meet two eigenspaces (eigenvectors of
distinct eigenvalues are orthogonal and the third vector would be parallel to one of them), so S_k is an eigenspace.
Consequences: each inf-line contains exactly one corner vector in each E_mk, and for every flat representative x on
that line, P_mk x = (1/sqrt 7) e^(i theta) c_perp, where c_perp spans E_mk minus c. The classical Parker-type
situation (U = shift (+) I_3, d = (4,1,...,1)) is thus never maximal, and no maximal Z_7 + 3 configuration is a
continuous deformation of a classical one.

**Lemma 6 (Z_9 + 1).** One eigenspace E_m* of dimension 2, the corner vector c lies in E_m*, and
P_m* w = P_m* w' = P_m* u (up to phases), all spanning E_m* minus c with norm 1/3. Lemma 3: for d_m = 1,
sum_(d in D_fin) |P_m v_d|^2 = 7/9; on E_m*, sum_(d in D_fin) P_m* v_d v_d^* P_m* = I - (2/9)|c_perp><c_perp|.

**Lemma 7 (Z_5 + 5).** All five eigenspaces have dimension 2, D_fin is empty (all five finite diagonals carry inf
symbols, so B has two disjoint 5x5 subsquares on the inf symbols), each inf-line has exactly one corner vector in each
E_m, the eigen-label of the 5x5 corner is a Latin square orthogonal to L, and in each E_m the five corner vectors of
label m satisfy sum_k |c_k><c_k| = (5/2) I_2 (diagonal block of R0). This is **not** the rectangular half-split of R5
(no invariant 5+5 subspace splitting of the vectors is imposed), so R5 does not apply.

## 2. Reduced systems and counts

Z_7 + 3 (with Lemma 5 applied): unknowns are the four general vectors v_d (d in D_fin), the phases of the nine flat
representatives (four 1-dimensional components of modulus 1/sqrt 7 and three 2-dimensional components fixed up to
phase by the corner), and nine corner rays (three per 2-dimensional eigenspace, pairwise distinct). After the gauge
group U(2)^3 x U(1)^4 this is about 129 real unknowns against 270 real equations (R0, C0, S0). The unreduced problem
has 1800 unknowns against 2700 equations (ratio 1.5), so the symmetric reduction does not make the system generic-
ally solvable; a solution would be a special algebraic object, as all known constructions at other orders are.
Z_9 + 1: about 159 unknowns against 270 equations. Z_5 + 5: no general v_d; only flat representatives and the corner.

## 3. What this changes

- New exact restricted exclusions: cyclic Z_n + h symmetry with U^n scalar is impossible for (n,h) = (8,2), (6,4),
  (4,6), (3,7), (2,8), for **every** cardinality (unreviewed).
- New forced structure: maximal Z_7 + 3 solutions need U with eigenvalue multiplicities (2,2,2,1,1,1,1); the corner
  data then fix all 2-dimensional components of the nine inf-orbit representatives up to phase.
- Open sub-ansatze, materially different from the old families: Z_9 + 1, Z_7 + 3 (forced form), Z_5 + 5. These are
  the targets of the proposed numerical assay (W4), which needs an item GO.
