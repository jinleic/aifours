# QPiK-symmetric planes, the symmetry group G (order 600) and the stabiliser theorem (v1)

Recorded after actual `/bin/date`: 2026-10-19T21:57:18-0700 (written in the following minutes). ContinueRQLS10b.
Single author, UNREVIEWED, written only, not Lean-checked. Uses notes 01 (6be70323...b09a), 02 (d84b74c5...8af0),
03 (b0828677...be2c); through note 02 the parent-accepted E1 interface (ad790caa...e872). No computation.

## 1. QPiK-invariant flat planes
**Theorem 1.** The flat planes P with (QPiK) P (QPiK)^(-1) = P are exactly the 10 MUB-pair planes of l_2 and the 20
planes D_(0,s) P_tau D_(0,s)^* (s in Z_5, tau in {+-1}^2) of F.
Proof. By note 03 Lemma 1 the data are a := alpha_1 = alpha_3, b := beta_1 = beta_3, c := alpha_2, d := beta_2 (all
complex). X1/T1 and X2/T2 of note 01 Theorem 4 coincide in pairs, leaving
  (X1) b conj(c) = phi^2 (conj(a) b + conj(d) conj(b)),   (X2) conj(a) conj(d) = phi^2 (conj(a) conj(b) + c a),
  (Z1) |b|^2 = 2 phi^2 Re(conj(a) c),                      (Z2) |a|^2 = 2 phi^2 Re(conj(b) d).
If a = b = 0 only l_2 is nonzero: note 01 Theorem 5 (all ten MUB-pair planes of l_2 have alpha_1..beta_3 = 0, hence
qualify). Otherwise a = 0 forces |b|^2 = 0 by Z1 and b = 0 forces |a|^2 = 0 by Z2, so a != 0 != b.
Moduli. X1 gives conj(c) = phi^2 (conj(a) + conj(d) conj(b)/b), so |c|^2 = phi^4 (|a|^2 + |d|^2 + 2 Re(conj(a) d b/conj(b)));
Z1 with c = phi^2 (a + d b/conj(b)) gives |b|^2 = 2phi^4 (|a|^2 + Re(conj(a) d b/conj(b))); eliminating the real part,
  (M1) |c|^2 - |b|^2 = phi^4 (|d|^2 - |a|^2).
X2 gives conj(d) = phi^2 (conj(b) + c a/conj(a)), so |d|^2 = phi^4 (|b|^2 + |c|^2 + 2 Re(conj(b) conj(c) conj(a)/a)); Z2 with
d = phi^2 (b + conj(c) conj(a)/a) gives |a|^2 = 2phi^4 (|b|^2 + Re(conj(b) conj(c) conj(a)/a)); hence
  (M2) |d|^2 - |a|^2 = phi^4 (|c|^2 - |b|^2).
Together (1 - phi^8)(|c|^2 - |b|^2) = 0: |c| = |b| and |d| = |a|.
Phases. X1 times conj(beta_3) and Z1 times conj(alpha_2) have the same left side beta_1 conj(alpha_2) conj(beta_3), so
conj(alpha_1)(|beta_3|^2 - |alpha_2|^2) = conj(alpha_2)^2 alpha_3 - conj(beta_2) conj(beta_3)^2 (in general); likewise X2 times
alpha_3 and Z2 times conj(beta_2) give conj(beta_1)(|alpha_3|^2 - |beta_2|^2) = conj(beta_2)^2 beta_3 - alpha_2 alpha_3^2.
Here these read a conj(c)^2 = conj(b)^2 conj(d) and b conj(d)^2 = a^2 c. Put omega := c/b, nu := d/conj(a) (both unimodular):
the first gives conj(omega)^2 = conj(nu), i.e. nu = omega^2; the second gives conj(nu)^2 = omega, i.e. conj(omega)^4 = omega,
so omega^5 = 1, omega = zeta^s. The translate by w = (0, s) (note 02 Lemma 1(b): y_(j v_k) -> zeta^(sj) y_(j v_k)) has data
(zeta^s a, zeta^(2s) b, zeta^(2s) b, zeta^(4s) conj(a)) on (alpha_1, beta_1, alpha_2, beta_2) and equal lines 1, 3, i.e. it
satisfies note 02 Theorem 2's U-invariance pattern; so it is some P_tau (note 02 Corollary 5) and P = D_(0,-s) P_tau D_(0,-s)^*.
Conversely, Z^s commutes with... more precisely: translation by (0, s) multiplies alpha_k by zeta^s and beta_k by zeta^(2s)
on all three lines alike, so it preserves alpha_3 = alpha_1, beta_3 = beta_1; the 20 planes qualify. QED
(Only the forbidden equations were used beyond note 02.)

## 2. The symmetry group
G := all unitaries and antiunitaries of C^5, modulo scalars, mapping every vector of beta_Z, beta_X, beta_T to a
unimodular multiple of a vector of one of them and permuting the three bases. G maps flat planes to flat planes.
**Lemma 2.** (a) D_w, Pi, S_2 K, U, QK lie in G (S_a e_t := e_(at)). (b) The kernel G_0 of the action on the three bases
is {D_w, D_w Pi, D_w S_2 K, D_w S_3 K : w in Z_5^2}, of order 100; <U, QK> realises all six permutations; |G| = 600.
(c) Every g in G satisfies g W_z g^(-1) = (phase) W_(L_g z) with L_g in GL(2,5), det L_g = 1 for unitary and -1 for
antiunitary g; g -> L_g is a homomorphism with kernel {D_w}; its image H = {I, 2I, 4I, 3I} x <M, N> (M from note 02,
N from note 03; NMN = M^(-1), so <M, N> is S_3) has order 24.
Proof. (a) D_w permutes each basis up to phases (they are the eigenbases of Z, X, X Z^(-1), and D_w commutes with each
up to a fifth root of unity); Pi: e_t -> e_(-t), f_m -> f_(-m), g_m -> g_(-m); S_2 K e_t = e_(2t), S_2 K f_m = f_(2m),
S_2 K g_m = g_(2m) (S_2 h(t) = h(3t) and -18 = 2, -3 = 2 mod 5); U: by note 02 Lemma 1, U Z U^* and U X U^* and
U (X Z^(-1)) U^* are multiples of X Z^(-1), Z^(-1) and X^(-1), so U maps beta_Z -> beta_T -> beta_X -> beta_Z (eigenbases of
operators with five distinct eigenvalues); QK e_t = e_t, QK f_m = g_(-m), QK g_m = f_(-m).
(b) Let g fix each basis, g unitary: g e_t = lambda_t e_(sigma(t)) and g f_m = c_m f_(pi(m)). Comparing coefficients,
lambda_(sigma^(-1)(s)) zeta^(m sigma^(-1)(s)) = c_m zeta^(pi(m) s); m = 0 makes lambda a character in s, and m = 1 then forces
sigma^(-1)(s) = kappa s + s_0, kappa != 0; so g = (phase) Z^c X^b S_a. S_a g_m(t) = zeta^(2a^(-2) t^2 + m a^(-1) t)/sqrt5 lies in
beta_T iff a^2 = 1; so g in {D_w, D_w Pi}. If g is antiunitary, g (S_2 K)^(-1) is unitary and fixes each basis. The four
cosets are distinct (L-images I, -I, 2I, 3I below), giving 100. U (order 3 on bases) and QK (fixing beta_Z, swapping the
others) generate S_3, so |G| = 6 * 100. (c) For unitaries this is the covariance of the generators (note 02 Lemma 1,
note 03 Lemma 1: L = I, -I, M, and S_2 conj(W_(a,c)) S_2^(-1) = S_2 W_(a,-c) S_2^(-1) = W_(2a,2c) for S_2 K, N for QK); an
antiunitary conjugation reverses the commutation phase zeta^(2[u,v]), so [Lu, Lv] = -[u, v], det L = -1. Elements with
L = I act on all W_z by phases, hence (Schur) are D_w, and no antiunitary has L = I. NMN(a,c) = (-a-c, a) = M^(-1)(a,c). QED
**Lemma 3 (prime-order elements).** Every g in G of prime order (modulo scalars) is: (5) a translation D_w, w != 0;
(3) D_w U^(+-1) D_w^(-1); (2, unitary) D_w Pi D_w^(-1); (2, antiunitary) D_w U^r A U^(-r) D_w^(-1) with r in {0,1,2},
A in {QK, QPiK}.
Proof. If g^5 is scalar, L_g^5 = I in H of order 24, so L_g = I and g is a translation. Order 3: the elements of order 3
of H = Z_4 x S_3 are M^(+-1), so g = (phase) D_v U^(+-1); since M - I and M^(-1) - I are invertible, D_w U D_w^(-1) =
(phase) D_(w - Mw) U reaches every D_v U (same for U^(-1)). Order 2: L_g^2 = I gives L_g in {I, -I, +-M^r N M^(-r)}
(elements s*tau of Z_4 x S_3 with s^2 tau^2 = I). L = I is a translation (order 5), excluded. L = -I (unitary): g =
D_v Pi = D_(v/2) Pi D_(v/2)^(-1) (phase). L = +-M^r N M^(-r) (det -1, antiunitary): g = D_v B with B = U^r A U^(-r), an
involution with L_B = L; g^2 = (phase) D_(v + Lv) is scalar iff v lies in the (-1)-eigenline of L, which is the image of
I - L; then D_w B D_w^(-1) = (phase) D_(w - Lw) B with (I - L)w = v. QED

## 3. The stabiliser theorem
**Theorem 4.** For a flat plane P the following are equivalent: (i) some g != 1 in G fixes P; (ii) P is one of the
30 MUB-pair planes or one of the 100 planes of F. Hence the flat planes outside MUB-pair and F (if any) have trivial
stabiliser and fall into free G-orbits of exactly 600 planes each; if the set of flat planes is finite, its size is
130 + 600 n for some integer n >= 0.
Proof. (ii) => (i): a MUB-pair plane of B_k is fixed by W_(v_k); D_w P_tau D_w^* is fixed by D_w U D_w^*. (i) => (ii):
the stabiliser contains an element of prime order (Cauchy), conjugate by some h in <D_w, U> to D_w (w != 0), U^(+-1),
Pi, QK or QPiK (Lemma 3). h^(-1) P h is flat and fixed by it, so it is MUB-pair (translation: note 02 Theorem 6(d);
Pi: note 03 Theorem 2; QK: note 03 Theorem 3; QPiK: Theorem 1) or in F (U: note 02 Theorem 6; QPiK: Theorem 1).
Translations and U map MUB-pair planes to MUB-pair planes (they permute the allowed lines; support in note 01) and F to
F (U D_w P_tau D_w^* U^* = (phase) D_(Mw) P_tau D_(Mw)^* since U P_tau U^* = P_tau). So P is MUB-pair or in F. QED
Status: this is the complete classification of SYMMETRIC flat planes (w.r.t. the full 600-element symmetry group of the
three bases). It does not exclude asymmetric flat planes; float evidence (not a premise) found none. Maximal 1-RQLS(10)
remains OPEN / UNKNOWN; no W8 statement is made here.
