# W8 decision note v1: the WH_5 (x) C^2 orbit ansatz - MUB-pair sub-case closed in writing, exact surviving sub-case

Recorded 2026-10-19T02:37:15-0700 (from /bin/date). Author ContinueRQLS10b. Lane-internal, single author, unreviewed.
Restricted ansatz only; nothing here concerns arbitrary 1-RQLS(10); the target stays OPEN / UNKNOWN. No novelty claim.

## 0. Hypotheses (H) and notation (frozen in checkpoints/008-checkpoint-v1.md)
Exactly the ansatz of evidence/w8-wh5-c2-orbit-ansatz-setup-v1.md (bedfe9a7...6471) and addendum 1 (213f2fa7...2fc9):
B = Cay(Z_5 x Z_2); the cell ((i1,i2),(j1,j2)) carries (X^i1 Z^j1 (x) I_2) x_(i2 j2); x_r in C^5 (x) C^2 is the 5 x 2
matrix X_r (r in {00, 01, 10, 11}); any cardinality. zeta = e^(2 pi i/5); X e_t = e_(t+1), Z e_t = zeta^t e_t.
Lines of Z_5^2: L_Z = <(0,1)>, L_X = <(1,0)>, L_k = <(1,k)> (eigenbasis of X Z^k); T = L_4 ("used": Z, X, T);
complementary k = 1, 2, 3 with orthonormal eigenbases psi^k_m(t) = zeta^(3 k t^2 + m t)/sqrt5 (m in Z_5; also
k = 0 gives the Fourier basis and k = 4 gives T). Couples: Z: 00-01, 10-11; X: 00-10, 01-11; T: 00-11, 01-10.
[I-H] (import, used ONLY in Proposition B): every bi-unimodular sequence h of length 5 (|h(t)| = 1, |sum_t h(t)
zeta^(-nt)| = sqrt5 for all n) equals c zeta^(alpha t^2 + beta t) (Haagerup's order-5 classification, as cited by the
old lane, W1 Addendum 3, VALID-WITH-IMPORT).

## 1. Reduction (re-derived; addendum 1 Lemma 1)
(R) For b in {Z, X, T}, e in b and every r: |e^* X_r|^2 = 1/5; for a couple (r, s) of b: e^* X_r is orthogonal to
e^* X_s (rows in C^2). Summing the couple identities over e gives X_r^* X_r + X_s^* X_s = I for all six K4 edges,
hence X_r^* X_r = I/2. So X_r = Phi_r U_r / sqrt2 with Phi_r an orthonormal frame of the plane S_r = range X_r and
U_r in U(2); P_r = Phi_r Phi_r^* is a rank-2 projector with e^* P_r e = 2/5 for every e in Z, X, T ("flat plane").
Couple (r, s) in b  <=>  (e^* Phi_r) V_rs (e^* Phi_s)^* = 0 for all e in b, V_rs := U_r U_s^*  (linear in V_rs).

## 2. Flat planes: exact normal form
Lemma 2. Let A_L^0 be the traceless operators diagonal in the eigenbasis of the line L. An operator M has constant
diagonal in that basis iff its A_L^0-component (in M_5 = C I (+) the six A_L^0, Hilbert-Schmidt orthogonal) vanishes.
Hence P is a flat plane iff P = (2/5) I + A_1 + A_2 + A_3 with A_k Hermitian in A_(L_k)^0 (k = 1, 2, 3) and P^2 = P.
Proof. W_w e = lambda_w(e) e for w in L and e in the basis of L; for w not in L, W_v W_w = zeta^(<v,w>) W_w W_v with
<v,w> != 0 for some v in L, so W_w e is an eigenvector of W_v with another eigenvalue and e^* W_w e = 0. Thus
e^* M e = (1/5)[tr M + sum_(w in L, w != 0) tr(W_w^* M) lambda_w(e)], constant in e iff all these traces vanish
(the lambda_w are the nontrivial characters). For P: components on A_Z^0, A_X^0, A_T^0 vanish, the I-component is 2/5.

Lemma 3 (one vanishing block forces a MUB-pair plane). If P is a flat plane and A_k = 0 for one k, then P is the
projector onto two vectors of one complementary basis {psi^k'_m} ("MUB-pair plane").
Proof. Write A_j = sum_(u in L_j, u != 0) alpha_j(u) D_u with Weyl operators D_(a,c) = tau^(ac) X^a Z^c (tau = zeta^3,
tau^2 = zeta), so D_u D_v = tau^(-<u,v>) D_(u+v), D_u^* = D_(-u), alpha_j(-u) = conj(alpha_j(u)). P^2 = P is
S^2 = (6/25) I + S/5 for S = A_1 + A_2 + A_3; the right side has no component on L_Z, L_X, L_T. A_j^2 is diagonal in
the basis of L_j, and for i != j, A_i A_j + A_j A_i = sum alpha_i(u) alpha_j(v) (tau^m + tau^(-m)) D_(u+v),
m = <u,v> != 0, with tau^m + tau^(-m) = 2 cos(6 pi m/5) != 0. Since L_i (+) L_j = Z_5^2, every w outside L_i u L_j is
u + v for exactly one pair. With u = x(1,1), v = y(1,2): u + v = (x+y, x+2y) lies on L_Z iff y = -x, on L_X iff
y = 2x, on T iff y = x, on L_3 iff y = 3x. If A_3 = 0, the L_Z, L_X, T components of S^2 are
c alpha_1(x) alpha_2(y) for y/x in {4, 2, 1} and must vanish; if alpha_1(x) != 0 then alpha_1(-x) != 0 too, which kills
alpha_2(y) for y/x in {4,2,1} u {1,3,4} = Z_5^*, i.e. A_2 = 0. (Pairs (1,3): z/x in {4,3,2} on used lines, union with
the -x set = Z_5^*; pair (2,3): z/y in {4,1,3}, likewise.) So at most one A_k != 0, P = (2/5) I + A_k is diagonal in
the basis psi^k, and a rank-2 projector diagonal in an orthonormal basis is the span of two of its vectors.

Lemma 4 (first order at a MUB-pair plane; uses Chebotarev's theorem [I-C]: every minor of the DFT matrix of prime
order is nonzero). At P_0 = span(psi^k_m1, psi^k_m2) the tangent space of the flat-plane variety has real dimension 2.
Proof. A tangent vector is a Hermitian dP with entries (in the psi^k basis) only between {m1, m2} and the other three
indices; flatness at first order says tr(W_w^* dP) = 0 for the 12 w on the used lines. Such W_w shift the psi^k basis by
s(w) != 0 with diagonal phase factors; the three w of a given shift s differ by three distinct characters of L_k, so the
conditions are three distinct Fourier coefficients of the shift-s diagonal y_s(j) = dP_(j+s, j) (times fixed phases).
With d = m2 - m1, y_s is supported on 2 positions for s = +-d and on 4 positions for s = +-2d; Chebotarev gives rank 2
resp. 3, so y_(+-d) = 0 and y_(2d) ranges over a complex line (y_(-2d) is its Hermitian partner): real dimension 2.

## 3. Theorem A (no import): no three representatives with MUB-pair planes
Statement. In any solution of (H) (any cardinality), at most two of X_00, X_01, X_10, X_11 have MUB-pair planes.
Proof. Any three representatives form a triangle of K4 whose edges are couples (in Z, X, T). For a MUB-pair plane
S_r = span(psi^k_m, psi^k_m') take Phi_r = [psi^k_m, psi^k_m'] (U_r stays arbitrary). Index the vectors of b by
n in Z_5 (Z: e_n; X: zeta^(nt)/sqrt5; T: psi^4_n). Gauss sums give, for k in {1,2,3}:
e_n^* psi^k_m = zeta^(3kn^2+mn)/sqrt5 (b = Z), G(3k) zeta^(-(m-n)^2/(12k))/5 (b = X), G(3(k-4)) zeta^(-(m-n)^2/(12(k-4)))/5
(b = T), all of modulus 1/sqrt5 (G(a) = sum_t zeta^(a t^2), |G(a)| = sqrt5 for a != 0). Hence
e_n^* Phi_r = (e_n^* psi^k_m)(1, zeta^(L_r(n))), L_r(n) = a_r n + beta_r with slope a_r = (m'-m), (m'-m) k^-1 or
(m'-m)(k+1)^-1 (b = Z, X, T): a_r != 0. For a couple (r, s) in b the prefactors are nonzero, so with V = V_rs
  f(n) = v11 + v12 zeta^(-beta_s) zeta^(-a_s n) + v21 zeta^(beta_r) zeta^(a_r n) + v22 zeta^(beta_r - beta_s) zeta^((a_r - a_s) n) = 0
for all n. The characters n -> zeta^(cn) are linearly independent. If a_r != +-a_s the four frequencies 0, -a_s, a_r,
a_r - a_s are distinct and V = 0, impossible. If a_r = a_s, then v12 = v21 = 0 and v22/v11 = -zeta^(beta_s - beta_r).
If a_r = -a_s (the frequencies 0, a_r, 2 a_r are distinct since p is odd), then v11 = v22 = 0 and
v21/v12 = -zeta^(-beta_s - beta_r). So every V_rs is monomial with "ratio" rho (v22/v11 if diagonal, v21/v12 if
anti-diagonal) in -zeta^(Z_5). For the triangle r1 r2 r3: V_12 V_23 V_31 = U_1 U_2^* U_2 U_3^* U_3 U_1^* = I. A product
of monomial 2 x 2 matrices is diagonal iff an even number of factors is anti-diagonal, and then its ratio is
rho_1^(+-1) rho_2^(+-1) rho_3^(+-1) in (-1)^3 zeta^(Z_5) (checked case by case: DD' -> rho rho', AA' -> rho_A / rho_A',
DA, AD -> antidiagonal). I has ratio 1, and -1 is not a fifth root of unity. Contradiction.
Remarks. (i) This contains addendum 1 Proposition 3 (one k, common column frame) and needs no frame or k restriction:
the planes of the three representatives may lie in different complementary bases with arbitrary U_r.
(ii) Equivalent consequence: if two representatives have MUB-pair planes, the other two do not.

## 4. Proposition B (conditional on [I-H]): no representative at all has a MUB-pair plane
Claim. If S_r is a MUB-pair plane and (r, s) is a couple, S_s is a MUB-pair plane. With Theorem A (K4 is connected,
every three vertices form a triangle) no representative has a MUB-pair plane.
Proof (modulo [I-H]). Addendum 1 Lemma 2: X_s = D_b K_b X_r J, so S_s = D_b K_b S_r with K_b the conjugation in b
(K_Z = K, K_X = Pi K, K_T = diag(zeta^(-t^2)) Pi K, all anti-Clifford) and D_b diagonal in b. K_b S_r is a MUB-pair
plane of a WH basis B' != b. A Clifford unitary C maps b to Z; then C S_s = diag(gamma) span(phi_a, phi_a') with
phi_m = psi^kappa_m (line <(1,kappa)>), and S_s flat in b', b'' iff C S_s is flat in two bases psi^lambda (lambda_1 !=
lambda_2). Since phi_a' = Z^d phi_a (d = a' - a != 0) and Z commutes with diag(gamma), the plane is span(u, Z^d u),
u = diag(gamma) phi_a, u orthogonal to Z^d u; its psi^lambda_n-diagonal is H(n) + H(n - d) with
H(n) = |(psi^lambda_n)^* u|^2 = |hat h_lambda(n - a)|^2 / 25, h_lambda(t) = gamma_t zeta^(3(kappa - lambda) t^2). Flatness
2/5 for all n forces H(n) = H(n - 2d) = constant = 1/5, i.e. h_lambda is bi-unimodular. By [I-H],
gamma_t = c zeta^(alpha' t^2 + beta t), a Clifford diagonal, which maps WH bases to WH bases; so S_s is a MUB-pair plane
of some WH basis, and flatness in Z, X, T makes it complementary.

## 5. Surviving sub-case (exact statement)
Unconditionally: every W8 solution has at least two representatives whose planes are flat but NOT MUB-pair planes, and
for such a plane all three blocks A_1, A_2, A_3 are nonzero (Lemma 3). Under [I-H]: all four representatives are of
this kind. Within the surviving sub-case the remaining conditions are the six linear couple conditions of section 1
(each needs a nonzero unitary in the kernel of a 5 x 4 matrix) and the K4 frame consistency V_12 V_23 V_31 = I.
The flat-plane system is the polynomial system P = (2/5) I + A_1 + A_2 + A_3, S^2 = (6/25) I + S/5 in 12 real
unknowns (two complex coefficients per complementary line), whose used-line part is, with a_x = alpha_1(x(1,1)),
b_y = alpha_2(y(1,2)), g_z = alpha_3(z(1,3)), Phi = phi^2 (phi = golden ratio) and s in Z_5^*:
  E_Z(s): -Phi a_(-s) b_s + a_(2s) g_(3s) - Phi b_(-s) g_s = 0
  E_X(s): a_(2s) b_(4s) - Phi a_(4s) g_(2s) - Phi b_(3s) g_(3s) = 0
  E_T(s): -Phi a_(3s) b_(3s) - Phi a_(2s) g_(4s) + b_(4s) g_(2s) = 0
(after multiplying by phi; coefficients 2cos(6 pi m/5) in {-phi, 1/phi}; the complementary-line and trace parts complete
the system). This exact system is the input for a future exact classification.

## 6. Float evidence (stdlib, one implementation; NOT a proof, not a premise of section 3-5)
Receipts: evidence/z5_flat_rank2_projectors_v1.receipt.md (3fa2eead...fa39), evidence/w8_flat_planes_couples_v3.receipt.md
(6f43db55...e5a), evidence/w8_flat_planes_couples_v4_v5.receipt.md (eedbadb9...443a).
- Four LM searches (seeds 20261019, 20261020, 20261021 and a replay of 20261021; 21,481 / 9,628 / 9,153 / 9,017 starts,
  all converged); the last three each found exactly the same 130 flat planes (v1's stored examples agree): the 30
  MUB-pair planes and 100 "exotic" ones (4 orbits of 25 under X^a Z^c; Frobenius distance >= 1.0128 from every
  MUB-pair plane; ||P^2 - P|| < 1e-12 after polishing), each block A_k of every exotic plane a permutation of
  {1.912648879, 1.522874379, -0.904840390, 1 - sqrt5 (to 1e-9), -1.294614890} (coefficients a_(k,m) of
  P = (2/5) I + sum (a_(k,m)/5) psi psi^*). Float evidence (not an exact verification) that exotic flat planes exist,
  i.e. that the surviving sub-case is probably not empty at the plane level. At every MUB-pair plane the numerical
  first-order kernel has real dimension 2 (Lemma 4) and kernel-direction starts return to the MUB-pair point.
- Couple tests (gap-justified rule, v5: lambda_1 either <= 1e-16.2 or >= 1e-0.96): MUB-exotic couples are never
  compatible (consistent with Proposition B); each exotic plane has 5 compatible exotic partners per basis; there is
  NO assignment of four exotic planes with all six couples pairwise compatible; all-MUB assignments fail the frame test
  (residuals (2/5)|cos(k pi/5)|, k = 0, 1, 2), as Theorem A says. No W8 solution of any cardinality in the list.
- The earlier numpy LM (evidence/rqls_w8_lm_v2.sv2.receipt.md, parent audit) found 0/512 at the full conditions, consistent.

## 7. Status and what would close W8 exactly
W8 is NOT decided in writing. Proven: Lemmas 2-3, Theorem A; conditional: Proposition B. Numerically (float, complete
only as far as the random searches are): no solution. Exact closure needs (i) an exact classification of the flat
planes (the system of section 5; exact recognition of the 100 exotic planes, apparently over Q(zeta_5, sqrt(...))),
(ii) an exact check that the exotic couple graph has no K4 pattern (or an exact frame obstruction), (iii) either [I-H]
or a direct proof that MUB-pair and exotic planes never couple.
