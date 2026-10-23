# E2/E3 for the explicit family F of 100 U_w-invariant flat planes: exact couple-compatibility sets and K4 exclusion (v1)

Recorded after actual `/bin/date`: 2026-10-19T17:44:48-0700 (written in the following minutes). Author ContinueRQLS10b.
Lane-internal, single author, UNREVIEWED, not Lean-checked. Scope frozen before derivation: 00-scope-freeze-v1.md
(c29b8bf7a8e46c4ebbf4402bf160080079b8dd3bcf6e00fceaaa368d14d7877a). Every fact used from the unreviewed W8 slice or the
unreviewed E1 candidate is re-derived below. No computation; decimal values in brackets are orientation only.

## 0. Outcome: EXCLUSION of the family F (and exact E2 sets)
**Theorem A (E2).** The 100 planes D_w P_tau D_w^* (w in Z_5^2, tau in {+-1}^2) of F are pairwise distinct, and for
b in {Z, X, T}: C_b(D_w P_tau D_w^*, D_w' P_tau' D_w'^*) is nonempty iff tau' = -tau and w' - w lies in L_b; then it is
a circle {lambda A_0 : |lambda| = 1} (explicit A_0 in Theorem 12), and for every frame V of the first plane, A V J is a
frame of the second with all beta_b-rows orthogonal (every A in the circle, every V). Each plane has exactly 5 partners
per basis.
**Theorem B (E3).** No solution of the W8 ansatz, of any cardinality, has all four representative planes in F.
Not claimed: F contains all flat planes (it does not contain the 30 MUB-pair planes; whether other flat planes exist is
open); anything about W8 solutions with some plane outside F; anything about 1-RQLS(10) (OPEN / UNKNOWN).

## 1. Notation and identities
zeta = e^(2pi i/5), omega = e^(2pi i/3), eps = e^(i pi/15) (eps^30 = 1, eps^15 = -1, zeta = eps^6, omega = eps^10).
X e_t = e_(t+1), Z e_t = zeta^t e_t, ZX = zeta XZ; D_(a,c) := X^a Z^c. beta_Z = (e_t), beta_X = (f_m),
f_m = 5^(-1/2) sum_t zeta^(mt) e_t, beta_T = (g_m), g_m = 5^(-1/2) sum_t zeta^(2t^2 + mt) e_t. Q = diag(zeta^(2t^2)) (so
g_m = Q f_m), R = diag(zeta^(t^2)) (R^2 = Q), Pi e_t = e_(-t), F = sum_m f_m e_m^*, U = Q F^*. K = complex conjugation in
beta_Z (K y = conj(y)); for an operator M, K M K = conj(M) (entrywise). Lines: L_Z = {(0,c)}, L_X = {(a,0)},
L_T = {(a,-a)}. phi = (1 + sqrt5)/2. alpha = 2cos(2pi/15), gamma = 2cos(4pi/15), beta = 2cos(8pi/15),
delta = 2cos(14pi/15) [1.827, 1.338, -0.209, -1.956]; kappa := alpha - beta; A := sqrt5 + alpha - delta,
B := sqrt5 + beta - gamma; N := 15 + 3sqrt5.
**Lemma 1.** (a) zeta + zeta^4 = 1/phi = phi - 1, zeta^2 + zeta^3 = -phi, phi^2 = phi + 1, sqrt5 = 2phi - 1;
G(a) := sum_t zeta^(a t^2) gives G(1) = sqrt5, G(2) = -sqrt5; for a != 0, sum_r zeta^(a r^2 + b r) = zeta^(-b^2 (4a)^(-1)) G(a).
(b) alpha + beta = phi, gamma + delta = -1/phi, alpha beta = 1/phi - 1, gamma delta = -phi^2, alpha gamma = alpha + 1/phi,
beta delta = beta + 1/phi, gamma^2 = 2 + beta, delta^2 = 2 + alpha, kappa^2 = 9 - 3phi.
(c) A + B = 3 sqrt5, AB = kappa^2; A > B > 0 is proved in Lemma 6; kappa > 2; (2+beta)A + (2+alpha)B = 6 sqrt5;
(2+beta)A - (2+alpha)B = (3 - sqrt5) kappa + 2(gamma - delta) > 0.
Proof. (a) s = zeta + zeta^4 and s' = zeta^2 + zeta^3 have s + s' = -1, s s' = -1, s = 2cos(2pi/5) > 0; t^2 runs through
0,1,4,4,1 and 2t^2 through 0,2,3,3,2, so G(1) = 1 + 2s, G(2) = 1 + 2s'. Completing the square: a r^2 + b r =
a(r + h)^2 - b^2 (4a)^(-1), h = b (2a)^(-1). (b) Sum-to-product and product-to-sum with 2cos(pi/5) = phi,
2cos(2pi/5) = 1/phi, 2cos(3pi/5) = -1/phi, 2cos(2pi/3) = -1, 2cos(6pi/5) = -phi, 2cos(22pi/15) = beta,
2cos(28pi/15) = alpha: alpha + beta = 4cos(pi/3)cos(pi/5); gamma + delta = 4cos(3pi/5)cos(pi/3); alpha beta =
2cos(2pi/3) + 2cos(2pi/5); gamma delta = 2cos(6pi/5) + 2cos(2pi/3); alpha gamma = 2cos(2pi/5) + alpha; beta delta =
beta + 2cos(2pi/5); gamma^2 = 2 + 2cos(8pi/15); delta^2 = 2 + 2cos(28pi/15); kappa^2 = (alpha + beta)^2 - 4 alpha beta
= phi + 1 + 4 - 4(phi - 1). (c) A + B = 2sqrt5 + phi + 1/phi. With u = alpha - delta, v = beta - gamma: u + v = sqrt5,
uv = alpha beta - alpha gamma - beta delta + gamma delta = -1 - phi - 1/phi - phi^2 = -1 - 3phi, so AB = 5 + 5 - 1 - 3phi
= kappa^2. kappa^2 > 4 iff phi < 5/3 iff sqrt5 < 7/3 (5 < 49/9). Expanding with (b): (2+beta)A = 2sqrt5 + 2alpha -
2delta + sqrt5 beta - 1 - beta and (2+alpha)B = 2sqrt5 + 2beta - 2gamma + sqrt5 alpha - 1 - alpha; their sum is
4sqrt5 - 2 + phi + 2/phi + sqrt5 phi = 6sqrt5 (2/phi = 2phi - 2, sqrt5 phi = phi + 2), their difference is
3(alpha - beta) + 2(gamma - delta) - sqrt5(alpha - beta); positive since alpha > beta, gamma > delta (cos decreasing on
[0, pi]) and 3 > sqrt5. QED

## 2. The W8 couple structure (re-derived from the W8 hypotheses; necessary direction suffices)
(H) Cells ((i1,i2),(j1,j2)) of Z_5 x Z_2 carry q = (X^(i1) Z^(j1) (x) I_2) x_(i2 j2), x_r <-> 5 x 2 matrix X_r
(r in {00,01,10,11}); every row, column and B-class (B(i,j) = i + j) of the 10 x 10 array is an orthonormal basis of
C^10. Couples: M_Z = {00-01, 10-11}, M_X = {00-10, 01-11}, M_T = {00-11, 01-10}; b(r,s) the basis of the couple {r,s}.
**Proposition 2.** Assume (H). (i) For every couple {r,s} in M_b and every v in beta_b: |v^* X_r|^2 = |v^* X_s|^2 = 1/5
and (v^* X_r)(v^* X_s)^* = 0. (ii) X_r^* X_r = I/2, so V_r := sqrt2 X_r is an isometry, P_r := V_r V_r^* a rank-2
projector (range S_r). (iii) For every couple {r,s} in M_b there is A in Anti_b := {D K_b : D unitary diagonal in beta_b}
with V_s = A V_r J (J = [[0,1],[-1,0]]) and hence P_s = A P_r A. (iv) Conversely, for every isometry V and every
A in Anti_b, A V J is an isometry with range A(range V), and the beta_b-rows of V and A V J are orthogonal; if
|v^* V|^2 = 2/5 for v in beta_b they also have equal norms.
Proof. (i) Row (i1, i2): after X^(-i1) (x) I it is orthonormal iff tr(X_r^* Z^k X_s) = delta_(k,0) delta_(r,s) for
r, s in {(i2,0),(i2,1)} and all k; tr(X_r^* Z^k X_s) = sum_t zeta^(kt) h(t), h(t) = (e_t^* X_s)(e_t^* X_r)^*, and
character inversion on Z_5 gives h(t) = delta_(r,s)/5: this is (i) for b = Z. Columns: X^i Z^j = zeta^(-ij) Z^j X^i and
X^k = sum_m zeta^(-mk) f_m f_m^* give (i) for b = X with M_X. Classes: X^i Z^(-i) is a unimodular multiple of
(X Z^(-1))^i, (X Z^(-1))^k = sum_m zeta^((3-m)k) g_m g_m^*, and g_m^* Z^(s1) = g_(m - s1)^*, giving (i) for b = T with M_T.
(ii) For {r,s} in M_b and v in beta_b, sqrt5 [v^* X_r ; v^* X_s] is unitary, so summing
(v^* X_r)^*(v^* X_r) + (v^* X_s)^*(v^* X_s) = I/5 over v gives G_r + G_s = I (G_r = X_r^* X_r) for all six pairs;
for distinct r, s, t: G_r = I - G_s = G_t and G_r + G_t = I. (iii) For v in beta_b the rows v^* V_r, v^* V_s have norm^2
2/5 and are orthogonal; in C^(1x2) the orthogonal complement of a nonzero row rho is spanned by conj(rho) J, so
v^* V_s = lambda_v conj(v^* V_r) J with |lambda_v| = 1. For D := sum_v lambda_v v v^* and A := D K_b (K_b the
conjugation in beta_b) one has v^*(A y) = lambda_v conj(v^* y), hence V_s = A V_r J (J real). The projector of
range(A V_r J) = A S_r is (A V_r)(A V_r)^* = A P_r A: indeed (A V)(A V)^* y = sum_k A v_k <A v_k, y> =
A sum_k v_k <v_k, A y> because A is an antiunitary involution (K_b D K_b = conj-diagonal, so A^2 = I, and
<A a, b> = conj(<a, A b>)). (iv) (A V)^*(A V) has entries <A v_i, A v_j> = conj(delta_ij); rows by v^*(A y) =
lambda_v conj(v^* y) and conj(rho) J orthogonal to rho. QED
Hence: in any solution of (H), S_s = A S_r with A in Anti_(b(r,s)) for all six couples. (Everything below about W8 uses
only this.)

## 3. U and its transport properties (re-derived)
**Lemma 3.** U e_s = g_(-s), U g_m = -zeta^(3m^2) f_(-m), U f_s = zeta^(2s^2) e_s; U^3 = -I.
Proof. (F^* v)_t = <f_t, v>. F^* e_s = f_(-s); F^* f_s = e_s; (F^* g_m)_t = (1/5) sum_r zeta^(2r^2 + (m-t)r) =
(G(2)/5) zeta^(3(m-t)^2) by Lemma 1(a) ((8)^(-1) = 2 in Z_5, -2 = 3); multiplying by zeta^(2t^2):
(U g_m)_t = (G(2)/5) zeta^(3m^2 - mt). So U g_m = (G(2)/sqrt5) zeta^(3m^2) f_(-m) = -zeta^(3m^2) f_(-m). Then
U^3 e_s = U^2 g_(-s) = -zeta^(3s^2) U f_s = -e_s. QED
**Lemma 4.** (a) U D_(a,c) U^* = (unimodular) D_(M(a,c)), M(a,c) := (c, -a - c); M L_Z = L_T, M L_T = L_X, M L_X = L_Z.
(b) U Anti_Z U^(-1) = Anti_T and U Anti_T U^(-1) = Anti_X. (c) D_w Anti_b D_w^(-1) = Anti_b for all w, b.
(d) For A in Anti_b and unitary W with W Anti_b W^(-1) = Anti_b': A P A = P' iff (W A W^(-1))(W P W^*)(W A W^(-1)) = W P' W^*.
Proof. (a) F^* X F = Z^(-1) (F^* X f_m = zeta^(-m) e_m), F^* Z F = X (F^* f_(m+1) = e_(m+1)); Q X Q^* e_t =
zeta^(4t + 2) e_(t+1) = zeta^2 X Z^(-1) e_t. So U X U^* = Z^(-1), U Z U^* = zeta^2 X Z^(-1), and U X^a Z^c U^* =
Z^(-a)(zeta^2 X Z^(-1))^c = (unimodular) X^c Z^(-a-c). M(0,1) = (1,-1), M(1,-1) = (-1, 0), M(1,0) = (0,-1).
(b) U K U^(-1)(sum c_s g_(-s)) = U K sum c_s e_s = sum conj(c_s) g_(-s), so U K U^(-1) = K_T; U(diagonal in beta_Z)U^(-1) is
diagonal in beta_T (U e_s = g_(-s)). U K_T U^(-1) is conjugation in the basis U beta_T = {-zeta^(3m^2) f_(-m)}; conjugation
in a basis {theta_j v_j} (|theta_j| = 1) equals (sum theta_j^2 v_j v_j^*) K_v, so it lies in Anti_X; diagonal operators go
to diagonal ones; the inverse maps work the same way. (c) D_w maps each vector of beta_b to a unimodular multiple of a
vector of beta_b (beta_b is the eigenbasis, with five distinct eigenvalues, of W_b in {Z, X, X Z^(-1)}, and
D_w W_b = zeta^k W_b D_w for some k), so (b)'s argument applies. (d) Conjugate the identity by W. QED

## 4. The family F: definition and U-invariance (re-derived)
**Lemma 5.** tr U = 1 and for mu in {omega, omega^2}, v_(mu,s) := e_s - mu^2 g_(-s) - mu zeta^(3s^2) f_s satisfies
U v = -mu v; the eigenvalues -omega, -omega^2 have multiplicity 2, -1 multiplicity 1.
Proof. By Lemma 3, U v = g_(-s) + mu^2 zeta^(3s^2) f_s - mu e_s = -mu v. U_(t,t) = zeta^(t^2)/sqrt5 gives tr U = 1; with
U^3 = -I the multiplicities (n_1, n_2, n_3) of (-1, -omega, -omega^2) satisfy: real trace forces n_2 = n_3, and
-n_1 + n_2 = 1, n_1 + 2n_2 = 5. QED
**Lemma 6.** Put a := v_(omega,0), b := v_(omega,1) - v_(omega,4), a' := v_(omega^2,0), b' := v_(omega^2,1) - v_(omega^2,4).
Then (coordinates t = 0, 1, 2, 3, 4):
  sqrt5 a = (1 + sqrt5, -gamma zeta, -delta zeta^4, -delta zeta^4, -gamma zeta),  sqrt5 b = (0, B, kappa zeta^3, -kappa zeta^3, -B),
  sqrt5 a' = (1 + sqrt5, -delta zeta, -gamma zeta^4, -gamma zeta^4, -delta zeta), sqrt5 b' = (0, A, -kappa zeta^3, kappa zeta^3, -A);
||sqrt5 a||^2 = ||sqrt5 a'||^2 = N, ||sqrt5 b||^2 = 6 sqrt5 B, ||sqrt5 b'||^2 = 6 sqrt5 A, and A > B > 0.
Proof. sqrt5 (v_(mu,s))_t = sqrt5 delta_(t,s) - mu^2 zeta^(2t^2 - st) - mu zeta^(3s^2 + st); hence sqrt5 a_t =
sqrt5 delta_(t,0) - mu^2 zeta^(2t^2) - mu and sqrt5 b_t = sqrt5(delta_(t,1) - delta_(t,4)) + (zeta^t - zeta^(-t))
(mu^2 zeta^(2t^2) - mu zeta^3). With powers of eps: omega^2 zeta^2 + omega = eps^2 + eps^10 = gamma eps^6; omega^2 zeta^3 +
omega = eps^8 + eps^10 = -delta eps^9 = delta zeta^4 (eps^9 = -zeta^4); omega zeta^2 + omega^2 = eps^22 + eps^20 =
-delta eps^21 = delta zeta (eps^21 = -zeta); omega zeta^3 + omega^2 = eps^28 + eps^20 = gamma zeta^4;
(zeta - zeta^4)(omega^2 zeta^2 - omega zeta^3) = (eps^6 - eps^24)(eps^2 - eps^28) = beta - gamma;
(zeta - zeta^4)(omega zeta^2 - omega^2 zeta^3) = (eps^6 - eps^24)(eps^22 - eps^8) = alpha - delta;
(zeta^2 - zeta^3) zeta^3 (omega^2 - omega) = eps^18 (eps^12 - eps^18)(eps^20 - eps^10) = (alpha - beta) zeta^3, and the
omega^2-version has the opposite sign; t = 3, 4 follow from evenness of a and oddness of b (Pi e_t = e_(-t),
Pi g_m = g_(-m), Pi f_m = f_(-m)). Norms: (1 + sqrt5)^2 + 2(2 + beta) + 2(2 + alpha) = N; 2B^2 + 2kappa^2 = 2B(A + B) =
6sqrt5 B > 0 (a squared norm of a nonzero vector), so B > 0, likewise A > 0; A - B = kappa + (gamma - delta) > 0. QED
**Definition/Lemma 7 (the family).** p := 3(5 - sqrt5)/20 (0 < p < 1), c := sqrt(p/N) = sqrt((3 - sqrt5)/40),
s := sqrt((1-p)/(6 sqrt5)) = sqrt((3 + sqrt5)/120), e := 1/sqrt5, g := c gamma (> 0), d := c delta (< 0),
bb := s sqrtB, aa := s sqrtA (> 0). For tau = (sigma, sigma') in {+-1}^2 define x, y as in the scope freeze, i.e.
x_t = zeta^(t^2) X_t, y_t = zeta^(t^2) Y_t with
  X = (e, -g + i sigma bb, -d + i sigma aa, -d - i sigma aa, -g - i sigma bb),
  Y = (e, -d + i sigma' aa, -g - i sigma' bb, -g + i sigma' bb, -d - i sigma' aa),
and P_tau := x x^* + y y^* = R P~_tau R^*, P~_tau := X X^* + Y Y^*. Then x = sqrt(p) a/||a|| + i sigma zeta sqrt(1-p) b/||b||
and y = sqrt(p) a'/||a'|| + i sigma' zeta sqrt(1-p) b'/||b'||; so x, y are orthonormal eigenvectors of U (for -omega,
-omega^2), P_tau is a rank-2 projector, and U P_tau U^* = P_tau. F := {D_w P_tau D_w^*}.
Proof. By Lemma 6 the right-hand side of x has t-coordinate sqrt(p)(1 + sqrt5)/sqrtN = 1/sqrt5 at t = 0
(p(6 + 2sqrt5)/N = (5 - sqrt5)(3 + sqrt5)/(10(5 + sqrt5)) = 1/5), zeta(-c gamma + i sigma s sqrtB) at t = 1 (B/sqrt(B) =
sqrtB), zeta^4(-c delta + i sigma s sqrtA) at t = 2 (zeta * zeta^3 = zeta^4, kappa/sqrtB = sqrt(AB/B) = sqrtA), and the
parity-mirrored values at t = 3, 4; likewise for y. Unit norms: p + (1 - p) (a perpendicular to b). Orthogonality:
different eigenvalues of a unitary. QED

## 5. Moduli of the entries of P_tau (diagonal-conjugation invariants)
**Lemma 8.** Write tau of class + if sigma = sigma', class - otherwise. With R0 := 3(1 - sqrt5)/20 (< 0):
  P~_01 = -e[(g + d) + i(sigma bb + sigma' aa)],  P~_02 = -e[(g + d) + i(sigma aa - sigma' bb)],  P~_04 = conj(P~_01),
  P~_03 = conj(P~_02),  P~_14 = R0 - 2i(sigma g bb + sigma' d aa),  P~_23 = R0 - 2i(sigma d aa - sigma' g bb),
  P~_12 = P~_34 = 2d(g - i sigma bb) [class +] or 2g(d + i sigma aa) [class -],
  P~_13 = P~_24 = 2g(d - i sigma aa) [class +] or 2d(g - i sigma bb) [class -].
The squared moduli take six values, A1 := (3/10 + 2s^2 kappa)/5, A2 := (3/10 - 2s^2 kappa)/5, C1 := 4d^2(g^2 + bb^2),
C2 := 4g^2(d^2 + aa^2), E1 := R0^2 + 4(g bb + d aa)^2, E2 := R0^2 + 4(g bb - d aa)^2, arranged as
  class +: |01|^2 = A1, |02|^2 = A2, |12|^2 = C1, |13|^2 = C2, |14|^2 = E1, |23|^2 = E2;
  class -: |01|^2 = A2, |02|^2 = A1, |12|^2 = C2, |13|^2 = C1, |14|^2 = E2, |23|^2 = E1
(|jk| short for |P~_jk| = |P_jk|). All are > 0, and: A1 - A2 = E2 - E1 = (4/5)s^2 kappa; C1 + C2 = phi/25;
C2 - C1 = [(3 - sqrt5)kappa + 2(gamma - delta)]/300 > 0; A1 > 3/50 > C1; A2 < R0^2 <= E1.
Proof. Entries: X_4 = conj(X_1), X_3 = conj(X_2), Y likewise, and X_0 = Y_0 = e; expand (e.g. P~_12 = X_1 conj(X_2) +
Y_1 conj(Y_2) = 2gd + i[sigma(g aa - d bb) - sigma'(g aa + d bb)]). Identities: g^2 = c^2(2 + beta), d^2 = c^2(2 + alpha),
bb^2 = s^2 B, aa^2 = s^2 A, so g^2 + d^2 + aa^2 + bb^2 = c^2(4 + phi) + 3sqrt5 s^2 = (11 - 3sqrt5)/40 + (5 + 3sqrt5)/40 = 2/5;
gd = c^2 gamma delta = -phi^2 (3 - sqrt5)/40 = -1/20 (phi^2(3 - sqrt5) = 2); aa bb = s^2 sqrt(AB) = s^2 kappa;
g^2 - bb^2 + d^2 - aa^2 = (11 - 3sqrt5)/40 - (5 + 3sqrt5)/40 = R0. Hence |P~_01|^2 = e^2[g^2 + d^2 + 2gd + aa^2 + bb^2 +
2 sigma sigma' aa bb] = (3/10 +- 2s^2 kappa)/5. E2 - E1 = -16 gd aa bb = (4/5)s^2 kappa. C1 + C2 = 8g^2 d^2 +
4c^2 s^2[(2+alpha)B + (2+beta)A] = 1/50 + 24sqrt5/1200 = phi/25 (c^2 s^2 = 4/4800); C2 - C1 = 4c^2 s^2[(2+beta)A -
(2+alpha)B] > 0 (Lemma 1(c)). Positivity: A2 >= (g + d)^2/5 = c^2/(5 phi^2) > 0 (g + d = c(gamma + delta) = -c/phi);
C1, C2 > 0 as g, d != 0; E1, E2 >= R0^2 > 0. A1 > 3/50 and C1 < (C1 + C2)/2 = phi/50 < 3/50. Finally A2 < R0^2 iff
(2/5)s^2 kappa > 3/50 - (27 - 9sqrt5)/200 = (9sqrt5 - 15)/200 iff 2(3 + sqrt5)kappa > 27sqrt5 - 45, which holds because
kappa > 2 gives 2(3 + sqrt5)kappa > 12 + 4sqrt5 and 12 + 4sqrt5 > 27sqrt5 - 45 iff 57 > 23 sqrt5 iff 3249 > 2645. QED
**Corollary 9 (two rotation invariants).** For a Hermitian M put Dist_j(M) := sum_t |M_(t,t+j)|^2. Dist_j is unchanged by
M -> E M E^* (E diagonal unitary) and by M -> X^a M X^(-a). For tau of class +, Dist_1(P_tau) = 2A1 + 2C1 + E2 and
Dist_2 = 2A2 + 2C2 + E1; for class - these two values are exchanged; and Dist_1(class +) - Dist_1(class -) =
[(3 + 2sqrt5)kappa - (gamma - delta)]/75 > 0. Moreover the cyclic sequence (|M_(t,t+1)|^2)_t of P_tau, namely
(A1, C1, E2, C1, A1) for class + and (A2, C2, E1, C2, A2) for class -, is not constant.
Proof. Invariance: |e_t M_(t,t') conj(e_t')| = |M_(t,t')|; the shift permutes the pairs at cyclic distance j.
Difference: 2(A1 - A2) - 2(C2 - C1) + (E2 - E1) = (12/5)s^2 kappa - [(3 - sqrt5)kappa + 2(gamma - delta)]/150 =
[(6 + 4sqrt5)kappa - 2(gamma - delta)]/150, positive since kappa > 2 and gamma - delta < 4. Non-constancy: A1 > C1 and
A2 < E1 (Lemma 8). QED

## 6. Rigidity under diagonal conjugation
**Lemma 10 (no diagonal conjugation to the complex conjugate).** For every tau, no diagonal unitary E satisfies
E P~_tau E^* = conj(P~_tau).
Proof. Rows rho_t := (X_t, Y_t) of the orthonormal frame [X Y] have Bloch vectors n(t) = (|X_t|^2 - |Y_t|^2,
2Re(conj(X_t)Y_t), 2Im(conj(X_t)Y_t)): n(0) = (0, 2/5, 0), n(1) = (Delta, r, 2I), n(4) = (Delta, r, -2I) with
Delta = g^2 + bb^2 - d^2 - aa^2 = -c^2 kappa - s^2(A - B) < 0 and I = Im(conj(X_1)Y_1) = sigma d bb - sigma' g aa, which is
nonzero: for sigma' = sigma it is sigma(d bb - g aa) with d bb < 0 < g aa; for sigma' = -sigma, (g aa)^2 - (d bb)^2 =
c^2 s^2[(2+beta)A - (2+alpha)B] > 0. So n(0), n(1) + n(4), n(1) - n(4) are linearly independent (determinant
-(16/5) I Delta != 0) and the five Bloch vectors are not coplanar (X, Y are orthonormal since x, y are and R is a
diagonal unitary). Now suppose E P~ E^* = conj(P~) with E diagonal unitary. The antiunitary Psi := K E satisfies
Psi P~ Psi^(-1) = K conj(P~) K = P~ and Psi^2 = conj(E) E = I. So Psi preserves S~ = range P~; its fixed set W in S~ is a
real form (v + Psi v, i(v - Psi v) in W; <a, b> real on W), and a real-orthonormal basis (w1, w2) of W is an
orthonormal basis of S~ with e_t w_t = conj(w_t), i.e. each row (w1_t, w2_t) is a unimodular multiple of a real row.
Real rows have Bloch vectors in the plane {third coordinate = 0}; passing to the frame [X Y] applies one rotation of
SO(3) to all Bloch vectors, so the n(t) would be coplanar - contradiction. QED
**Lemma 11 (rigidity).** Let E be a diagonal unitary, a in Z_5 and tau, tau' in {+-1}^2 with E P_tau E^* = X^a P_tau' X^(-a).
Then a = 0, tau' = tau and E is scalar.
Proof. Dist_1 of both sides agree (Corollary 9), so tau, tau' are in the same class; then P_tau and P_tau' have the same
moduli pattern (Lemma 8), and the cyclic sequence (|M_(t,t+1)|^2) of the right side is the sequence of P_tau' rotated by
a; equality with that of the left side (= that of P_tau) for a != 0 would make the sequence invariant under rotation by a
generator of Z_5, i.e. constant, contradicting Corollary 9. So a = 0. If tau' = -tau: P_(-tau) = R conj(P~_tau) R^*
(conj(X) is X with sigma -> -sigma, likewise Y), so E P~_tau E^* = conj(P~_tau), impossible by Lemma 10. So tau' = tau,
E commutes with P_tau, and since every off-diagonal entry of P_tau is nonzero (Lemma 8), e_t = e_t' for all t, t'. QED
**Corollary 12a.** The 100 planes D_w P_tau D_w^* are pairwise distinct.
Proof. D_w^* D_w' is a unimodular multiple of X^a Z^c ((a, c) = w' - w); equality of two planes gives
Z^c P_tau' Z^(-c) = X^(-a) P_tau X^a after rearranging the diagonal factor (X^(-a) Z^(-c) X^a is diagonal), i.e.
E P_tau' E^* = X^(-a) P_tau X^a with E diagonal; Lemma 11 gives a = 0, tau = tau', Z^c scalar, c = 0. QED

## 7. The exact compatibility sets (Theorem A)
**Lemma 12 (the key relation).** Q conj(P_tau) Q^* = P_(-tau); equivalently conj(P_tau) = Q^* P_(-tau) Q.
Proof. (Q conj(x))_t = zeta^(2t^2) conj(zeta^(t^2) X_t) = zeta^(t^2) conj(X_t) and conj(X) is X with sigma -> -sigma;
same for y. QED
**Theorem 12 (Z).** C_Z(D_w P_tau D_w^*, D_w' P_tau' D_w'^*) is empty unless tau' = -tau and w' - w = (0, c') for
some c' in Z_5; in that case it equals { lambda D_w Z^(c') Q K D_w^(-1) : |lambda| = 1 }.
Proof. By Lemma 4(c),(d) with W = D_w^(-1) it suffices to take w = 0 (D_w^* D_w' is a unimodular multiple of
D_(w'-w)). Let v = w' - w = (a, c') and A = D K in Anti_Z: A P_tau A = D conj(P_tau) D^* = (D Q^*) P_(-tau) (D Q^*)^*
(Lemma 12). With D_v a unimodular multiple of X^a Z^(c'), this equals D_v P_tau' D_v^* = X^a Z^(c') P_tau' Z^(-c') X^(-a)
iff E' P_(-tau) E'^* = X^a P_tau' X^(-a) for the diagonal unitary E' := X^a Z^(-c') X^(-a) D Q^* (conjugate both sides by
X^a Z^(-c') X^(-a), a unimodular multiple of Z^(-c')). By Lemma 11 (applied to -tau) this forces a = 0, tau' = -tau and
E' = lambda I, i.e. D = lambda Z^(c') Q. Conversely these D work. QED
**Theorem 12 (T, X).** C_T(D_w P_tau D_w^*, D_w' P_tau' D_w'^*) is nonempty iff tau' = -tau and w' - w lies in L_T, and then
equals U C_Z(D_(M^-1 w) P_tau D^*, D_(M^-1 w') P_tau' D^*) U^(-1) (a circle); C_X likewise with L_X and U^2.
Proof. Lemma 4(b),(d) with W = U^(-1): A in Anti_T is U B U^(-1) with B in Anti_Z, and A P A = P' iff
B (U^(-1) P U) B = U^(-1) P' U. U^(-1) D_w P_tau D_w^* U = D_(M^-1 w) P_tau D_(M^-1 w)^* (Lemma 4(a), U P_tau U^* = P_tau). By
the Z case: tau' = -tau and M^(-1)(w' - w) in L_Z, i.e. w' - w in M L_Z = L_T. For X use U^2 and M^2 L_Z = L_X. QED
Frames: by Proposition 2(iv), for each A in these sets and each frame V of the first plane, A V J is a frame of the
second with orthogonal (and, as both planes are flat - not used here - equal-norm) beta_b-rows; the circle parameter
lambda multiplies the second frame by lambda. Counting: for fixed (w, tau) the partners in basis b are exactly the five
planes D_w' P_(-tau) D_w'^* with w' in w + L_b. This proves Theorem A.

## 8. Theorem B (K4 exclusion of F)
Proof. Suppose (H) holds with S_r = D_(w_r) P_(tau_r) D_(w_r)^* for all four r (labels unique by Corollary 12a). By
Proposition 2(iii), S_s = A S_r with A in Anti_(b(r,s)) for each couple, so C_(b(r,s))(S_r, S_s) is nonempty and Theorem A
gives tau_s = -tau_r. The triangle 00 -(Z)- 01 -(T)- 10 -(X)- 00 consists of three couples, so
tau_00 = -tau_01 = tau_10 = -tau_00, impossible as tau_00 != -tau_00. QED
Frames and phases play no role: the obstruction is the sign flip tau -> -tau forced on every couple inside F
(no frame/holonomy condition and no inequation was needed). In particular F contains no K4 pattern at any cardinality.

## 9. Scope, gaps, dependencies
Proved here: Theorems A and B for the explicitly defined family F (flatness of F is not used anywhere).
Remaining (not claimed): (i) whether the W8 representative planes can be flat planes outside F (MUB-pair planes are
excluded by the W8 slice's unreviewed Corollary 14, not re-derived here; other flat planes are not classified);
(ii) mixed configurations with some but not all planes in F: a Z-partner of P_tau is a diagonal conjugate E P_(-tau) E^*,
and the set of diagonal E making it flat for X and T (eight real equations in four phases) is not determined here;
(iii) everything about 1-RQLS(10), which remains OPEN / UNKNOWN.
Imports: character orthogonality on Z_5; trigonometric sum/product formulas and monotonicity of cos on [0, pi];
elementary linear algebra (antiunitary operators, real forms, Bloch vectors and their rotation under U(2) frame changes).
No Haagerup/Chebotarev, no computation, no float data as premise.
