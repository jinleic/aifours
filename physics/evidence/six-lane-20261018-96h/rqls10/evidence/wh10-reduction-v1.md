# WH_10 single-orbit ansatz: exact reduction, controls and status (v1)

Recorded 2026-10-19T03:53:04-0700 (from /bin/date; written in the following minutes). Author ContinueRQLS10b.
Lane-internal, single author, unreviewed, NOT parent-accepted. Restricted ansatz only; the target (maximal 1-RQLS(10))
stays OPEN / UNKNOWN. No novelty claim. Extends evidence/structure-and-wh10-ansatz-proposal-v1.md
(68a6c9c313a468c31e0fe7ca77769789c6829a9f9396ea7bc979b8bbcd31db37) and corrects nothing in it.

## 0. Ansatz (H_d)
omega = e^(2 pi i/d), X e_t = e_(t+1), Z e_t = omega^t e_t on C^d (t in Z_d), D_(a,c) = X^a Z^c. Latin square
B = Cay(Z_d), B(i,j) = i + j. One unit vector x; cell (i,j) carries q_ij = X^i Z^j x. (H_d): every row, column and
B-class is an orthonormal basis (ONB). zeta_n := e^(2 pi i/n). Identities used: Z X = omega X Z, Z^j X^i = omega^(ij) X^i Z^j,
Z^-1 X = omega^-1 X Z^-1, (X Z^-1)^i = omega^(-i(i-1)/2) X^i Z^-i, Z^-s X Z^s = omega^-s X.

## 1. Lemma W1 (line conditions; written, complete)
(a) Row i ONB  <=>  |x_t|^2 = 1/d for all t. [Row i = X^i {Z^j x}_j; <Z^j x, Z^j' x> = sum_t |x_t|^2 omega^((j'-j)t), and a
    weight vanishes at all nonzero frequencies iff it is constant.]
(b) Column j ONB  <=>  |<F_k, x>|^2 = 1/d for the Fourier basis F_k (eigenbasis of X). [X^i Z^j = omega^(-ij) Z^j X^i, so
    column j = Z^j {X^i x}_i up to phases; same argument in the eigenbasis of X.]
(c) Class s ONB  <=>  |<f_k, x>|^2 = 1/d for the eigenbasis f_k of U := X Z^-1. [Class s = {X^i Z^(s-i) x}_i = phases x
    {U^i Z^s x}_i; U^d = omega^(-d(d-1)/2) I, so U is a weighted cyclic shift with d distinct eigenvalues lambda_k = lambda_0
    omega^k; the weights w_k = |<f_k, Z^s x>|^2 must be constant; Z^-s U Z^s = omega^-s U, so Z^-s f_k is again an eigenvector
    of U and the condition is the same for every s.]
For even d: f_k(t) = zeta_(2d)^(-t^2) omega^(-kt) / sqrt d, U f_k = zeta_(2d) omega^k f_k (direct check: f(t+1)/f(t) = lambda^-1
omega^-t, and zeta_(2d)^(-(t+d)^2) = zeta_(2d)^(-t^2) because d is even). For odd d: f_k(t) = lambda_k^-t omega^(-t(t-1)/2)/sqrt d.
Form for d = 10, h = sqrt10 x: (i) |h_t| = 1; (ii) |sum_t h_t omega^(-kt)| = sqrt10 for all k; (iii) |sum_t zeta_20^(t^2)
omega^(kt) h_t| = sqrt10 for all k. So h AND h.c (c_t = zeta_20^(t^2), 10-periodic) are both bi-unimodular (CAZAC); in
Bjorck's form z_t = h_(t+1)/h_t and z'_t = z_t zeta_20^(2t+1) are BOTH unimodular cyclic 10-roots.

## 2. Lemma W3 (CRT; written, complete; exact check in the probe below)
e_t -> e_(t mod 2) (x) e_(t mod 5) identifies C^10 with C^2 (x) C^5 and gives X -> X_2 (x) X_5, Z -> Z_2 (x) Z_5^3
(because t = 5(t mod 2) + 6(t mod 5) mod 10), hence X Z^-1 -> X_2 Z_2 (x) X_5 Z_5^2. Each factor pair has products of
eigenvalues pairwise distinct (+-1 times fifth roots; +-i times c zeta_5^k, and -1 is no fifth root of unity), so the
three eigenbases of C^10 are PRODUCT bases: Z <-> (sigma_z basis) (x) B_Z, X <-> (sigma_x basis) (x) B_X,
XZ^-1 <-> (sigma_y basis) (x) B_2, where B_Z, B_X, B_2 are the eigenbases of Z_5, X_5, X_5 Z_5^2 on C^5 (WH_5 lines
L_Z = <(0,1)>, L_X = <(1,0)>, L_2 = <(1,2)> of Z_5^2; X_2 Z_2 = [[0,-1],[1,0]] has the sigma_y eigenbasis).
Same for d = 6: Z_6 -> Z_2 (x) Z_3^2, X_6 -> X_2 (x) X_3, X_6 Z_6^-1 -> X_2 Z_2 (x) X_3 Z_3 (lines (0,1), (1,0), (1,1) of Z_3^2).

## 3. Theorem W4 (reduction to C^5; written, complete)
Write x = sum_j e_j (x) b_j (j in Z_2) and M = [b_0 b_1] in C^(5x2), so <u (x) v, x> = v^* M conj(u). Pair the axes
(z, x, y) with (B_Z, B_X, B_2). Then x satisfies (H_10) iff
 (a) M^* M = I_2 / 2, i.e. M = Phi V / sqrt2 with Phi^* Phi = I_2 (a plane S = range Phi) and V in U(2);
 (b) S is flat in B_Z, B_X and B_2: v^* P v = 2/5 for every v in these bases (P = Phi Phi^*);
 (c) S contains unit vectors q_Z, q_X, q_2, pairwise unbiased inside S (|<q_a, q_b>|^2 = 1/2), with q_a flat in B_a
     (|<v, q_a>|^2 = 1/5 for every v in B_a).
Proof. Flatness of x in (Pauli-a basis {u_0, u_1}) (x) B_a is |v^* M conj(u_j)|^2 = 1/10 for j = 0, 1, i.e. v^* M M^* v = 1/5
and v^* M s_a M^* v = 0 with s_a := sigma_a^T (conj(u_0) conj(u_0)^* - conj(u_1) conj(u_1)^* = +-sigma_a^T). Summing over v in
B_a: tr(s_a M^* M) = 0 for a = z, x, y, so M^* M has no Pauli component; tr M^* M = |x|^2 = 1 gives (a). Then
v^* P v = 2 v^* M M^* v = 2/5 gives (b), and H_a := 2 M s_a M^* = Phi (V s_a V^*) Phi^* is an involution of S
(H_a = Q_a - Q_a^perp, Q_a the projector onto q_a) with v^* H_a v = 0 on B_a; with (b) this is |<v,q_a>|^2 = 1/5. The s_a
anticommute, so the q_a are pairwise unbiased. Conversely, given (b), (c): the involutions eps_a (2 q_a q_a^* - P) form an
orthonormal Pauli frame on S; choose eps_2 = +-1 so that its orientation equals that of (Phi s_a Phi^*)_a; SU(2) -> SO(3)
is onto, so some V maps one frame onto the other, and M = Phi V / sqrt2 satisfies all conditions (they are invariant under
H_a -> -H_a).
Lemma W2 (maximality; written, complete). Every solution of (H_10) has 100 pairwise nonparallel rays. Proof: D_w x is
parallel to D_w' x iff x is an eigenvector of D_(w'-w). Order 2: w in {(5,0), (0,5), (5,5)}, all on the three used
cyclic subgroups, whose generators have 10 distinct eigenvalues; x flat in that eigenbasis has full support, so it is an
eigenvector of no nonscalar power. Order 5: D_(2a,2c) = I_2 (x) W_5 with W_5 a nonscalar WH_5 operator (5 distinct
eigenvalues, 1-dimensional eigenspaces), while x has Schmidt rank 2 by (a). Order 10: D_w^2 is proportional to D_(2w)
of order 5.

## 4. Corollaries (written, complete)
W5 (products). Schmidt rank 1 violates (a). Every 10-periodic quadratic-phase sequence h_t = zeta_20^(a t^2) omega^(bt) is a
product: zeta_20^(a t^2) = i^(a t^2) zeta_5^(-a t^2) and i^(a t^2) depends only on t mod 2; omega^(bt) = (-1)^(bt)
zeta_5^(-2bt). So no Chu/Gauss-type sequence (and no CRT product of a length-2 and a length-5 sequence) solves (H_10).
W6 (MUB-pair planes). If S = span(psi_m, psi_m') for two vectors of one complementary WH_5 basis (lines (1,1), (1,3),
(1,4)), the only B_a-flat unit vectors of S are psi_m and psi_m' (up to phase), for each a; (c) fails. Proof: for v in B_a
pick u on the line of B_a with D_u psi_m parallel to psi_m'; then <v, psi_m'> = c lambda_u(v) <v, psi_m>, where lambda_u(v)
runs through the 5 distinct eigenvalues c' zeta_5^j of D_u and |<v, psi_m>|^2 = 1/5. For q = alpha psi_m + beta psi_m',
5 |<v,q>|^2 = |alpha + beta c lambda_u(v)|^2 = 1 for all v forces Re(conj(alpha) beta c c' zeta_5^j) = 0 for five values of j,
hence alpha beta = 0.
W7 (negative controls). d = 2: a qubit state flat in the sigma_z, sigma_x, sigma_y bases has Bloch vector 0: impossible.
d = 6: Theorem W4 holds verbatim with C^3 and the lines (0,1), (1,0), (1,1). A plane S of C^3 is flat in a basis iff its
normal line y has |<v,y>|^2 = 1/3, so y is unbiased to Z_3, X_3 and the (1,1) basis. Unit vectors of C^3 unbiased to Z_3 and
X_3: y ~ (1, a, b), |a| = |b| = 1; the three Fourier conditions are equivalent to a + b/a = -1/b, whose conjugate equation
gives (a - b)(a - 1)(b - 1) = 0, hence exactly six solutions (a, b) in {(w,w), (w2,w2), (1,w), (1,w2), (w,1), (w2,1)}
(w = zeta_3, w2 = w^2) = the vectors of the bases (1,1) and (1,2). Excluding the (1,1) basis, y lies in the (1,2) basis,
so S is a MUB-pair plane and W6 (with p = 3: three ratios c zeta_3^j) excludes it. So (H_6) has NO solution - exact, no
import; consistent with the imported nonexistence of 1-RQLS(6) used as gate C1 in v7/v8.
W8 (odd-d positive anchors). For odd d, x_t = omega^(a t^2 + b t)/sqrt d with gcd(2a, d) = gcd(2a + 1, d) = 1 solves (H_d)
(quadratic Gauss sums of modulus sqrt d for the X- and the U-condition, coefficients a and a + 1/2 respectively). It is an
eigenvector of X Z^(2a), whose subgroup <(1, 2a)> is a maximal isotropic subgroup, so the configuration has exactly d
distinct rays (non-maximal). Valid a: d = 5: {1, 3, 4}; d = 7: {1, 2, 4, 5, 6}; d = 9: {2, 5, 8}.
W9 (relaxed d = 10 anchors and an internal consistency test). If x is flat only for a subset A of the three bases, the
proof of (a) still gives tr(sigma_a M^* M) = 0 for a in A. Exact relaxed anchors: Chu zeta_20^(t^2) (rows and columns;
CRT factor (1, i): Bloch axis y), the constant vector (rows and classes; factor (1, 1): axis x), e_0 (columns and classes;
factor (1, 0): axis z) - in each case the Bloch vector of M^* M is along the unused axis, as predicted.

## 5. Status and prerequisite (scoped)
(H_10) <=> a plane S of C^5 flat in B_Z, B_X, B_2 containing three pairwise unbiased vectors q_a flat in B_a; any solution
is automatically a MAXIMAL 1-RQLS(10) (Lemma W2). MUB-pair planes are excluded (W6). The remaining case needs the
classification of flat planes for the triple {L_Z, L_X, L_2}. Warning (written, complete): this triple is NOT equivalent to
the W8 triple {L_Z, L_X, L_T = <(1,4)>} under the extended Clifford group: line <(a,c)> -> c/a in P^1(F_5) sends them to
{inf, 0, 2} and {inf, 0, 4}; the extended Clifford group acts on lines through matrices of determinant +-1, i.e. as PSL(2,5)
(complex conjugation acts as diag(1,-1), which equals diag(3,2) of determinant 1 up to the scalar 3); a map fixing inf and 0
is z -> alpha z with alpha a square, and {inf, 0, 2} has a stabiliser inducing all of S_3 (z -> 1/(z-2), z -> 2-z, both of
square determinant), so no element maps {inf, 0, 4} to {inf, 0, 2}. Hence the W8 flat-plane numerics (130 planes) cannot be
transported to WH_10 by any (anti)unitary Clifford symmetry (other correspondences are not claimed either way); WH_10 needs
its own flat-plane classification (an "E1" for the other triple class). Exact closure is therefore not available now; the
numerical assay (separate GO request) tests (H_10) directly, and the exact stdlib probe (receipt to follow) tests every
CAZAC sequence of length 10 over mu_20 against condition (iii).
