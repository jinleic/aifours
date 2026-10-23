# E1 decided in the negative: an exact flat plane for Z, X, T that is not a MUB-pair plane (v1)

Recorded after actual `/bin/date`: 2026-10-19T17:29:22-0700 (written in the following minutes). Author ContinueRQLS10b.
Lane-internal, single author, UNREVIEWED, not parent-accepted, not Lean-checked. Scope frozen before derivation:
00-scope-freeze-v1.md (e925c1a4ddd1d6a591cab3b721c140121f326d7a0cd00c9a3d7908a75f1f0f85). This decides closure item E1 as
posed (the flat-plane question) and nothing about solutions of the W8 ansatz or about 1-RQLS(10) (OPEN / UNKNOWN).
No novelty claim. No computation of any kind; every identity below is proved by hand.

## 0. Outcome: NO
**Theorem.** There is a rank-2 orthogonal projector P on C^5 with v^* P v = 2/5 for every v in beta_Z u beta_X u beta_T
that is not a MUB-pair plane. An explicit one is P = x x^* + y y^* with x, y given in closed form in section 4
(coordinates: zeta, i, the numbers 2cos(2pi k/15), and square roots of explicit positive elements of Q(cos(2pi/15))).
Moreover (Proposition 9) the flat planes spanned by one line of each of the two 2-dimensional eigenspaces of the
order-3 Clifford unitary U of section 2 are exactly four, and no rank-2 projector commuting with U is a MUB-pair plane.

## 1. Notation and elementary identities
zeta = e^(2 pi i/5), omega = e^(2 pi i/3), eps = e^(i pi/15); so eps^30 = 1, eps^15 = -1, zeta = eps^6, omega = eps^10.
e_t (t in Z_5) standard basis; X e_t = e_(t+1), Z e_t = zeta^t e_t, ZX = zeta XZ. f_m = 5^(-1/2) sum_t zeta^(mt) e_t
(beta_X; X f_m = zeta^(-m) f_m); g_m = 5^(-1/2) sum_t zeta^(2t^2+mt) e_t (beta_T); psi^k_m = 5^(-1/2) sum_t
zeta^(3k t^2+mt) e_t, so psi^0 = f, psi^4 = g. Q := diag(zeta^(2t^2)), so g_m = Q f_m. F := sum_m f_m e_m^* (unitary,
F e_m = f_m). Pi e_t = e_(-t). A flat plane / MUB-pair plane are as in the scope freeze (k in {1,2,3} for MUB-pair).
phi = (1 + sqrt5)/2. Four real numbers: alpha = 2cos(2pi/15), gamma = 2cos(4pi/15), beta = 2cos(8pi/15),
delta = 2cos(14pi/15) (approximately 1.827, 1.338, -0.209, -1.956; signs only are used: alpha > beta, gamma > delta,
since cos decreases on [0, pi]).

**Lemma 1.** (a) zeta + zeta^4 = 1/phi = phi - 1, zeta^2 + zeta^3 = -phi, phi^2 = phi + 1, sqrt5 = phi + 1/phi = 2phi - 1.
(b) G(a) := sum_t zeta^(a t^2): G(1) = sqrt5, G(2) = -sqrt5. (c) For a in Z_5^*, b in Z_5:
sum_r zeta^(a r^2 + b r) = zeta^(-b^2 (4a)^(-1)) G(a). (d) alpha + beta = phi, gamma + delta = -1/phi,
alpha beta = 1/phi - 1, gamma delta = -phi^2, alpha gamma = alpha + 1/phi, beta delta = beta + 1/phi,
gamma^2 = 2 + beta, delta^2 = 2 + alpha, (alpha - beta)^2 = 9 - 3phi.
Proof. (a) s = zeta + zeta^4, s' = zeta^2 + zeta^3: s + s' = -1, s s' = zeta^3 + zeta^4 + zeta + zeta^2 = -1, so they are
the roots of x^2 + x - 1; s = 2cos(2pi/5) > 0. (b) t^2 takes 0, 1, 4, 4, 1 and 2t^2 takes 0, 2, 3, 3, 2:
G(1) = 1 + 2s = sqrt5, G(2) = 1 + 2s' = -sqrt5. (c) Completing the square in Z_5 (2 and 4a invertible).
(d) 2cos x + 2cos y = 4cos((x+y)/2)cos((x-y)/2) and 2cos x * 2cos y = 2cos(x+y) + 2cos(x-y), with 2cos(pi/5) = phi,
2cos(2pi/5) = 1/phi, 2cos(3pi/5) = -1/phi, 2cos(2pi/3) = -1, 2cos(6pi/5) = -phi:
alpha + beta = 4cos(pi/3)cos(pi/5) = phi; gamma + delta = 4cos(3pi/5)cos(pi/3) = -1/phi;
alpha beta = 2cos(2pi/3) + 2cos(2pi/5); gamma delta = 2cos(6pi/5) + 2cos(2pi/3) = -phi - 1;
alpha gamma = 2cos(2pi/5) + 2cos(2pi/15); beta delta = 2cos(22pi/15) + 2cos(2pi/5) and 2cos(22pi/15) = beta;
gamma^2 = 2 + 2cos(8pi/15), delta^2 = 2 + 2cos(28pi/15) = 2 + alpha; (alpha - beta)^2 = phi^2 - 4(1/phi - 1)
= phi + 1 + 4 - 4(phi - 1) = 9 - 3phi. QED
Put A := sqrt5 + alpha - delta, B := sqrt5 + beta - gamma, N := 15 + 3 sqrt5.
**Corollary 2.** A + B = 3 sqrt5 and A B = 9 - 3phi = (alpha - beta)^2.
Proof. A + B = 2sqrt5 + (alpha + beta) - (gamma + delta) = 2sqrt5 + phi + 1/phi. With u = alpha - delta,
v = beta - gamma: u + v = sqrt5 and uv = alpha beta - alpha gamma - beta delta + gamma delta =
(1/phi - 1) - (alpha + 1/phi) - (beta + 1/phi) - phi^2 = -1 - phi - 1/phi - phi^2 = -1 - 3phi; so
AB = 5 + sqrt5(u + v) + uv = 9 - 3phi. QED

## 2. The order-3 Clifford unitary U := Q F^*
**Lemma 3.** U e_s = g_(-s), U g_(-s) = -zeta^(3s^2) f_s, U f_s = zeta^(2s^2) e_s for all s; hence U^3 = -I, and U maps
beta_Z onto beta_T, beta_T onto beta_X and beta_X onto beta_Z, each vector to a unimodular multiple of a basis vector.
Proof. (F^* v)_t = <f_t, v> = 5^(-1/2) sum_r zeta^(-tr) v_r. So F^* e_s = f_(-s), U e_s = Q f_(-s) = g_(-s); F^* f_s = e_s,
U f_s = zeta^(2s^2) e_s. For g_m: (F^* g_m)_t = (1/5) sum_r zeta^(2r^2 + (m - t) r) = (G(2)/5) zeta^(3(m-t)^2) by Lemma 1(c)
((4 * 2)^(-1) = 2, -2 = 3); times zeta^(2t^2): (U g_m)_t = (G(2)/5) zeta^(3m^2 - mt) (5t^2 = 0, -6mt = -mt), i.e.
U g_m = (G(2)/sqrt5) zeta^(3m^2) f_(-m) = -zeta^(3m^2) f_(-m); put m = -s. Then U^3 e_s = -zeta^(3s^2) U f_s =
-zeta^(5s^2) e_s = -e_s. QED

**Lemma 4.** Let D_(a,c) := X^a Z^c and L_k := {(a, ka)} (k in Z_5), L_Z := {(0, c)}. (a) U D_(a,c) U^* = (unimodular)
D_(c, -a-c); the map M(a, c) = (c, -a - c) sends L_1 -> L_3 -> L_2 -> L_1, and no complementary line L_k (k = 1, 2, 3)
is mapped to itself. (b) For k in {1, 2, 3}: (X Z^k) psi^k_m = zeta^(2k - m) psi^k_m (five distinct eigenvalues), and for
u = (a, c) not in L_k, every diagonal entry <psi^k_m, D_u psi^k_m> vanishes.
Proof. (a) F^* X F e_m = F^* X f_m = zeta^(-m) e_m and F^* Z F e_m = F^* f_(m+1) = e_(m+1), so F^* X F = Z^(-1),
F^* Z F = X; Q Z^(-1) Q^* = Z^(-1) and Q X Q^* e_t = zeta^(2(t+1)^2 - 2t^2) e_(t+1) = zeta^2 (X Z^(-1)) e_t. So
U X U^* = Z^(-1), U Z U^* = zeta^2 X Z^(-1), and U X^a Z^c U^* = Z^(-a) (zeta^2 X Z^(-1))^c = (unimodular) X^c Z^(-a-c)
(reordering only uses ZX = zeta XZ). M(1, k) = (k, -1 - k) lies in L_k iff k^2 + k + 1 = 0 in Z_5, which fails for
k = 1, 2, 3 (values 3, 2, 3); M(1,1) = (1, 3), M(1,3) = (3, 1) = 3(1, 2), M(1,2) = (2, 2) = 2(1, 1).
(b) (X Z^k psi)(t) = zeta^(k(t-1)) psi(t-1) and psi^k_m(t - 1) = psi^k_m(t) zeta^(-6kt + 3k - m), giving the eigenvalue
zeta^(2k - m) (zeta^(-5kt) = 1). D_u (X Z^k) = zeta^(c - ka) (X Z^k) D_u, and c - ka != 0 for u not in L_k, so D_u maps
the eigenvector psi^k_m to an eigenvector of X Z^k with a different eigenvalue, which is orthogonal to psi^k_m. QED

## 3. Eigenvectors of U
**Lemma 5.** tr U = 1; the eigenvalues of U are -1 (multiplicity 1), -omega and -omega^2 (multiplicity 2 each). For
mu in {omega, omega^2} and every s, v_(mu,s) := e_s - mu^2 g_(-s) - mu zeta^(3s^2) f_s satisfies U v = -mu v.
Proof. U_(t,t) = <e_t, Q F^* e_t> = zeta^(2t^2) zeta^(-t^2)/sqrt5, so tr U = G(1)/sqrt5 = 1. By Lemma 3 the eigenvalues
lie in {-1, -omega, -omega^2}; with multiplicities n_1, n_2, n_3, the trace -n_1 - n_2 omega - n_3 omega^2 is real only
if n_2 = n_3, and then equals -n_1 + n_2 = 1 with n_1 + 2n_2 = 5: n_1 = 1, n_2 = 2. With lambda = -mu (lambda^(-1) = -mu^2,
lambda^(-2) = mu, lambda^3 = -1), Lemma 3 gives U v = g_(-s) - mu^2(-zeta^(3s^2) f_s) - mu zeta^(3s^2) zeta^(2s^2) e_s
= -mu e_s + g_(-s) + mu^2 zeta^(3s^2) f_s = -mu v. QED

Define for mu in {omega, omega^2}: a^mu := v_(mu,0) and b^mu := v_(mu,1) - v_(mu,4). Since Pi e_t = e_(-t),
Pi g_m = g_(-m), Pi f_m = f_(-m), a^mu is even and b^mu odd in t, so <a^mu, b^mu> = 0. Coordinates (times sqrt5):
  sqrt5 a_t = sqrt5 delta_(t,0) - mu^2 zeta^(2t^2) - mu,
  sqrt5 b_t = sqrt5 (delta_(t,1) - delta_(t,4)) + (zeta^t - zeta^(-t)) (mu^2 zeta^(2t^2) - mu zeta^3)
(zeta^(3*16) = zeta^3). Writing all roots of unity as powers of eps and using eps^30 = 1:

**Lemma 6 (explicit coordinates).** For mu = omega (eigenvalue -omega):
  sqrt5 a_0 = 1 + sqrt5, sqrt5 a_(+-1) = -gamma zeta, sqrt5 a_(+-2) = -delta zeta^4, sqrt5 b_0 = 0,
  sqrt5 b_(+-1) = +-B, sqrt5 b_(+-2) = +-(alpha - beta) zeta^3.
For mu = omega^2 (eigenvalue -omega^2), writing a', b':
  sqrt5 a'_0 = 1 + sqrt5, sqrt5 a'_(+-1) = -delta zeta, sqrt5 a'_(+-2) = -gamma zeta^4, sqrt5 b'_0 = 0,
  sqrt5 b'_(+-1) = +-A, sqrt5 b'_(+-2) = -+(alpha - beta) zeta^3.
Here "+-1" means t = 1 and t = 4, "+-2" means t = 2 and t = 3, upper signs for t = 1, 2.
Proof. mu + mu^2 = -1 gives a_0. mu = omega: omega^2 zeta^2 + omega = eps^32 + eps^10 = eps^6(eps^(-4) + eps^4) =
gamma zeta; omega^2 zeta^3 + omega = eps^38 + eps^10 = eps^9 (eps^(-1) + eps) = -delta eps^9 and eps^9 = -eps^(-6) = -zeta^4
(eps^15 = -1), so -(...) = -delta zeta^4. (zeta - zeta^4)(omega^2 zeta^2 - omega zeta^3) = (eps^6 - eps^24)(eps^2 - eps^28)
= eps^8 - eps^4 - eps^26 + eps^22 = beta - gamma. (zeta^2 - zeta^3) zeta^3 (omega^2 - omega) = eps^18 (eps^12 - eps^18)
(eps^20 - eps^10) = eps^18 (eps^2 + eps^28 - eps^22 - eps^8) = (alpha - beta) zeta^3. mu = omega^2: omega zeta^2 + omega^2
= eps^22 + eps^20 = eps^21 (eps + eps^(-1)) = -delta eps^21 and eps^21 = -zeta, so -(...) = -delta zeta;
omega zeta^3 + omega^2 = eps^28 + eps^20 = gamma eps^24 = gamma zeta^4; (zeta - zeta^4)(omega zeta^2 - omega^2 zeta^3) =
(eps^6 - eps^24)(eps^22 - eps^8) = eps^28 - eps^14 - eps^16 + eps^2 = alpha - delta; the last product changes sign
with omega^2 - omega. Values at -t follow from parity. QED

**Corollary 7 (norms and phases).** ||sqrt5 a||^2 = ||sqrt5 a'||^2 = N, ||sqrt5 b||^2 = 6sqrt5 B, ||sqrt5 b'||^2 = 6sqrt5 A;
in particular A, B > 0. For every t: zeta conj(a_t) b_t and zeta conj(a'_t) b'_t are real.
Proof. (1 + sqrt5)^2 + 2gamma^2 + 2delta^2 = 6 + 2sqrt5 + 2(4 + alpha + beta) = 14 + 2sqrt5 + 2phi = N (Lemma 1).
2B^2 + 2(alpha - beta)^2 = 2B^2 + 2AB = 2B(A + B) = 6sqrt5 B by Corollary 2; this is a positive squared norm (b has
nonzero entry (alpha - beta) zeta^3 / sqrt5 at t = 2), so B > 0; likewise A. Phases: conj(a_t) b_t at t = 1, 2 is a real
multiple of conj(zeta) * 1 or conj(zeta^4) zeta^3 = conj(zeta); for a', of conj(zeta) or conj(zeta^4) zeta^3; parity
and b_0 = 0 cover the other t. QED

## 4. The counterexample
Put p := 3(5 - sqrt5)/20 (about 0.4146; 0 < p < 1), c := sqrt(p/N) = sqrt((3 - sqrt5)/40),
s := sqrt((1 - p)/(6 sqrt5)) = sqrt((3 + sqrt5)/120), and
  x := sqrt(p) a/||a|| + i zeta sqrt(1 - p) b/||b||,   y := sqrt(p) a'/||a'|| + i zeta sqrt(1 - p) b'/||b'||.
By Lemma 6 and Corollary 7, explicitly (t = 0, 1, 2, 3, 4):
  x = ( 1/sqrt5,  zeta(-c gamma + i s sqrtB),  zeta^4(-c delta + i s sqrtA),  zeta^4(-c delta - i s sqrtA),  zeta(-c gamma - i s sqrtB) ),
  y = ( 1/sqrt5,  zeta(-c delta + i s sqrtA),  zeta^4(-c gamma - i s sqrtB),  zeta^4(-c gamma + i s sqrtB),  zeta(-c delta - i s sqrtA) ).
(Entry t = 0: sqrt(p)(1 + sqrt5)/sqrtN with p(6 + 2sqrt5)/N = 1/5, checked below; entries t = +-2 use
(alpha - beta)/sqrtB = sqrt(AB/B) = sqrtA, alpha > beta.) Useful values: c^2 (4 + phi) = (3 - sqrt5)(9 + sqrt5)/80 =
(11 - 3sqrt5)/40, s^2 * 3sqrt5 = (5 + 3sqrt5)/40, 4 c^2 phi^2 = phi^2 (3 - sqrt5)/10 = 1/5 (phi^2 (3 - sqrt5) = (3 + sqrt5)(3 - sqrt5)/2 = 2).
p(6 + 2sqrt5)/N = (3(5 - sqrt5)/20)(2(3 + sqrt5))/(3(5 + sqrt5)) = (5 - sqrt5)(3 + sqrt5)/(10(5 + sqrt5)), and
(5 - sqrt5)(3 + sqrt5) = 10 + 2sqrt5 = 2(5 + sqrt5), giving 1/5.

**Theorem 8 (verification).** (i) ||x|| = ||y|| = 1 and <x, y> = 0, so P := x x^* + y y^* is a rank-2 orthogonal
projector. (ii) e_t^* P e_t = 2/5 for all t. (iii) U x = -omega x, U y = -omega^2 y, U P U^* = P, and v^* P v = 2/5 for
every v in beta_X u beta_T. (iv) P is not a MUB-pair plane. Hence P is a flat plane that is not a MUB-pair plane.
Proof. (i) ||x||^2 = 1/5 + 2(c^2 gamma^2 + s^2 B) + 2(c^2 delta^2 + s^2 A) = 1/5 + 2c^2(4 + alpha + beta) + 2s^2 (A + B)
= 1/5 + (11 - 3sqrt5)/20 + (5 + 3sqrt5)/20 = 1; the same terms occur in ||y||^2. In <x, y> = sum_t conj(x_t) y_t the
phases zeta, zeta^4 cancel; the t = 1, 4 terms give 2c^2 gamma delta + 2 s^2 sqrt(AB) and the t = 2, 3 terms give
2 c^2 gamma delta - 2 s^2 sqrt(AB) (imaginary parts cancel in pairs), so <x, y> = 1/5 + 4c^2 gamma delta =
1/5 - 4c^2 phi^2 = 0. (ii) e_0^* P e_0 = 1/5 + 1/5; for t = +-1: c^2 gamma^2 + s^2 B + c^2 delta^2 + s^2 A =
c^2 (4 + phi) + s^2 * 3sqrt5 = (11 - 3sqrt5 + 5 + 3sqrt5)/40 = 2/5; for t = +-2 the same four terms occur.
(iii) x lies in span(a, b), an eigenspace of U for -omega (Lemma 5), and y in the one for -omega^2; so
U x x^* U^* = x x^*, U y y^* U^* = y y^*. By Lemma 3, every v in beta_T is a unimodular multiple of U e for some
e in beta_Z, and every v in beta_X of U^2 e; so v^* P v = e^* U^* P U e = e^* P e = 2/5 (and likewise with U^2).
(iv) Proposition 9(a) below, since U P U^* = P. QED
(Consistency: the coordinate form agrees with the definition because zeta conj(a_t) b_t is real (Corollary 7), so the
cross term 2 sqrt(p(1-p)) Re(i zeta conj(a^_t) b^_t) in |x_t|^2 vanishes, i.e. |x_t|^2 = p|a^_t|^2 + (1-p)|b^_t|^2.)

## 5. Non-MUB-pair-ness of U-invariant planes; all U-invariant planes of type (-omega line) + (-omega^2 line)
**Proposition 9.** (a) No rank-2 projector P with U P U^* = P is a MUB-pair plane. (b) The rank-2 projectors
P = x x^* + y y^* with x in E_(-omega)(U), y in E_(-omega^2)(U) unit vectors that are flat for Z, X, T are exactly the
four with x = sqrt(p) a^ + i sigma zeta sqrt(1-p) b^, y = sqrt(p) a'^ + i sigma' zeta sqrt(1-p) b'^, sigma, sigma' in {+1, -1}
(a^ = a/||a|| etc.); they are pairwise distinct. (c) For every w in Z_5^2, D_w P D_w^* is again a flat non-MUB-pair plane.
Proof. (a) Suppose P = psi psi^* + psi' psi'^* with psi, psi' two vectors of the basis psi^k (k in {1,2,3}). Then P is
diagonal in psi^k with diagonal (1, 1, 0, 0, 0) up to order. With W := X Z^k (eigenvalues lambda_m = zeta^(2k - m),
distinct), sum_(n=0)^(4) |tr(P W^n)|^2 = sum_(m,m') P_mm P_m'm' sum_n (lambda_m conj(lambda_m'))^n = 5 sum_m P_mm^2 = 10,
and the n = 0 term is (tr P)^2 = 4; so tr(P W^n) != 0 for some n in {1,...,4}. W^n is a unimodular multiple of D_u with
u = n(1, k) in L_k. By Lemma 4(a), D_(Mu) = (unimodular) U D_u U^*, so |tr(P D_(Mu))| = |tr(U^* P U D_u)| = |tr(P D_u)|
!= 0. But Mu lies in L_(M(k)), a line different from L_k, and is nonzero, so Mu is not in L_k; by Lemma 4(b), D_(Mu) has
zero diagonal in psi^k while P is diagonal there, so tr(P D_(Mu)) = 0. Contradiction.
(b) By Lemma 5, E_(-omega) = span(a, b) and E_(-omega^2) = span(a', b') (dimension 2, orthogonal nonzero vectors). Up to
phases x = sqrt(p) a^ + tau sqrt(1-p) b^ and y = sqrt(q) a'^ + tau' sqrt(1-q) b'^ with p, q in [0,1], |tau| = |tau'| = 1.
Flatness for Z suffices (Lemma 3, as in Theorem 8(iii)). Since a^ is even and b^ odd, |x_t|^2 + |x_(-t)|^2 =
2(p|a^_t|^2 + (1-p)|b^_t|^2) and |x_t|^2 - |x_(-t)|^2 = 4 sqrt(p(1-p)) Re(tau conj(a^_t) b^_t). Even part (t = 0 and t = 2,
using |b^_2|^2 = AB/(6sqrt5 B) = A/(6sqrt5), |b'^_2|^2 = B/(6sqrt5), |a^_2|^2 = (2 + alpha)/N, |a'^_2|^2 = (2 + beta)/N):
  (E0) (p + q)(6 + 2sqrt5)/N = 2/5,  (E2) p((2+alpha)/N - A/(6sqrt5)) + q((2+beta)/N - B/(6sqrt5)) = 2/5 - 1/2
(t = +-1 then holds automatically because the five diagonal values sum to 2). The determinant of (E0), (E2) is
((6 + 2sqrt5)/N)((A - B)/(6sqrt5) - (alpha - beta)/N); here A - B = (alpha - beta) + (gamma - delta) > 0 and
(A - B)^2 = (A + B)^2 - 4AB = 9 + 12phi > 9 - 3phi = (alpha - beta)^2, while 6sqrt5 < N; so (A - B)/(6sqrt5) >
(alpha - beta)/N and the determinant is nonzero. Hence p = q is the unique solution, and p = q = 3(5 - sqrt5)/20 does solve
(E0), (E2) (this is Theorem 8(ii)). Odd part (t = 1, 2): by Corollary 7 write conj(a^_t) b^_t = r_t conj(zeta) and
conj(a'^_t) b'^_t = r'_t conj(zeta) with real
r_1 = -gamma B/K, r_2 = -delta (alpha - beta)/K, r'_1 = -delta A/K', r'_2 = gamma (alpha - beta)/K' (K = sqrt(N 6sqrt5 B),
K' = sqrt(N 6sqrt5 A) > 0; from Lemma 6: conj(-gamma zeta) B, conj(-delta zeta^4)(alpha - beta) zeta^3, conj(-delta zeta) A,
conj(-gamma zeta^4)(-(alpha - beta)) zeta^3). The equations are r_t X + r'_t Y = 0 (t = 1, 2) with X := Re(tau conj(zeta)),
Y := Re(tau' conj(zeta)) (the common factor sqrt(p(1-p)) > 0); the determinant r_1 r'_2 - r_2 r'_1 =
-(alpha - beta)(gamma^2 B + delta^2 A)/(K K') is nonzero, so X = Y = 0, i.e. tau, tau' in {i zeta, -i zeta}. Distinctness:
P meets E_(-omega) exactly in the line of x (P = span(x, y), y orthogonal to E_(-omega)), and the two choices of sigma
give non-parallel x because 0 < p < 1.
(c) D_w permutes each of beta_Z, beta_X, beta_T and each basis psi^k up to unimodular factors (Lemma 4(b) for the
off-line case; diagonal on its own line), so it preserves flatness and maps MUB-pair planes to MUB-pair planes (and
back, using D_w^*). QED

## 6. What this does and does not settle
Settled: E1 as posed has answer NO - the flat planes for Z, X, T are not all MUB-pair planes; four explicit U-invariant
ones are exact (Proposition 9(b)), and their WH-translates are flat and non-MUB-pair (their number is not determined here).
Consistency remark (not a premise): the lane's float evidence reported 100 non-MUB-pair flat planes, 4 per conjugate
U_w, each a line of the omega- plus a line of the omega^2-eigenspace; Proposition 9(b) is the exact version of "4 per
conjugate" for U itself (U = -U_0 has the same eigenspaces as an order-3 Clifford with eigenvalues 1, omega, omega^2).
Not settled (exact remaining gap for a FULL classification): whether every flat non-MUB-pair plane commutes with some
conjugate D_w U D_w^* (and whether flat planes of other types exist, e.g. not U_w-invariant, or U_w-invariant but
containing the -1 eigenvector or a whole 2-dimensional eigenspace). Nothing here decides the W8 ansatz (couple and frame
conditions, lane items E2-E3) or 1-RQLS(10); the maximal target remains OPEN / UNKNOWN.

## 7. Imports and dependencies
Imports: character orthogonality on Z_5 (used in Proposition 9(a) as sum_n lambda^n = 5 delta), elementary trigonometric
sum/product formulas, elementary linear algebra (eigenspaces of unitaries are orthogonal; trace of a unitary). No Haagerup
classification, no Chebotarev theorem, no lane result as premise, no computation, no float data as premise.
