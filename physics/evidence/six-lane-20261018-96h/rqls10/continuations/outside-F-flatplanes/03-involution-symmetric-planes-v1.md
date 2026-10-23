# Flat planes with an involutive symmetry Pi, QK (and their translates): only MUB-pair planes (v1)

Recorded after actual `/bin/date`: 2026-10-19T21:50:14-0700 (written in the following minutes). ContinueRQLS10b.
Single author, UNREVIEWED, written only, not Lean-checked. Uses notes 01 (6be70323...b09a) and 02 (d84b74c5...8af0).
No computation. The antiunitary QPiK (the other involution class) is treated in a later note.

## 1. Actions on Weyl coefficients
Pi e_t := e_(-t), K := complex conjugation in beta_Z, Q = diag(zeta^(2t^2)); Pi Q = Q Pi.
**Lemma 1.** Pi W_z Pi = W_(-z); conj(W_(a,c)) = W_(a,-c); Q W_(a,c) Q^* = W_(a, c-a). With N(a, c) := (a, -a - c):
(a) Pi P Pi has coefficients y'_z = y_(-z); (b) (QK) P (QK)^(-1) = Q conj(P) Q^* has y'_(Nz) = conj(y_z);
(c) (QPiK) P (QPiK)^(-1) has y'_(-Nz) = conj(y_z). QK and QPiK are antiunitary involutions; Pi, QK, QPiK map flat
planes to flat planes; N fixes l_2 pointwise, swaps j v_1 <-> j v_3, fixes L_Z and swaps L_X <-> L_T.
Proof. Pi X Pi = X^(-1), Pi Z Pi = Z^(-1) and zeta^(3ac) is even. conj(zeta^(3ac) X^a Z^c) = zeta^(-3ac) X^a Z^(-c).
Q X Q^* = W_(1,-1) (note 02 Lemma 1), Q Z Q^* = W_(0,1), so Q W_(a,c) Q^* = zeta^(3ac) W_(a,-a) W_(0,c) =
zeta^(3ac + 2ac) W_(a, c-a). Hence Q conj(P) Q^* = (1/5) sum conj(y_z) W_(N z), N = (a,c) -> (a,-c) -> (a, -c-a); (c) adds
Pi. (QK)^2 = Q conj(Q) = I and (QPiK)^2 = Q Pi conj(Q) Pi = I. N(j, jk) = (j, -j - jk): k = 1 -> (j, 3j) = j v_3,
k = 3 -> (j, j) = j v_1, k = 2 -> (j, 2j) = j v_2; N(0,c) = (0,-c), N(a,0) = (a,-a), N(a,-a) = (a,0). Since y'
is y transported by +-N (with conjugation) and +-N permutes the forbidden lines, note 01 Lemma 2 shows flatness is
preserved (Pi: z -> -z fixes every line). QED
So: P = Pi P Pi iff every y_z is real; P is QK-invariant iff y_(Nz) = y_(-z), i.e. alpha_3 = conj(alpha_1),
beta_3 = conj(beta_1), alpha_2, beta_2 real; P is QPiK-invariant iff y_(Nz) = y_z, i.e. alpha_3 = alpha_1, beta_3 = beta_1.

## 2. Pi-invariant flat planes
**Theorem 2.** The flat planes with Pi P Pi = P are exactly six MUB-pair planes: for k = 1, 2, 3 the span of the
eigenvectors of W_(v_k) for the eigenvalues zeta^(+-1), and the span of those for zeta^(+-2). Consequently every flat
plane invariant under some D_w Pi D_w^* (= a phase times D_(2w) Pi) is a MUB-pair plane.
Proof. For real data put x := (beta_1, alpha_2, beta_3), m := (alpha_1, beta_2, alpha_3). Note 01 Theorem 4 becomes,
for {i, j, k} = {1, 2, 3} (X1, Z1, T1 = (F_x) for {1,2}, {1,3}, {2,3}; X2, Z2, T2 = (F_m); A1_1, A2_2, A3_1 = (A_m);
A1_2, A2_1, A3_2 = (A_x)):
  (F_x) x_i x_j = phi^2 x_k (m_i + m_j),   (F_m) m_i m_j = phi^2 m_k (x_i + x_j),
  (A_m) m_i = 2 m_i x_i + x_i^2 + m_j m_k/phi,   (A_x) x_i = m_i^2 + 2 m_i x_i + x_j x_k/phi,   (Tr) sum (m_i^2 + x_i^2) = 3.
Put X := x_1 + x_2 + x_3, M := m_1 + m_2 + m_3. (F_m) for {j,k} gives m_j m_k = phi^2 m_i (X - x_i); inserted in (A_m):
  (1) x_i^2 = m_i (1 - phi X - x_i/phi^2)   (2 - phi = 1/phi^2), and symmetrically (2) m_i^2 = x_i (1 - phi M - m_i/phi^2).
Suppose all three lines are nonzero. By (1), (2), m_i = 0 iff x_i = 0, so all six numbers are nonzero. Multiplying
(F_x) for {i,j} and {i,k} and dividing by x_j x_k: x_i^2 = phi^4 (m_i + m_j)(m_i + m_k) = phi^4 (m_i M + m_j m_k) =
phi^4 m_i (M + phi^2 X - phi^2 x_i). Comparing with (1) and dividing by m_i:
  x_i (phi^6 - phi^(-2)) = phi^4 M + phi^6 X - 1 + phi X,
independent of i; so x_1 = x_2 = x_3 =: x and, by the symmetric argument, m_1 = m_2 = m_3 =: m. Then (F_x) reads
x^2 = 2 phi^2 x m and (F_m) m^2 = 2 phi^2 m x, so x = 2phi^2 m = 4 phi^4 x, x = 0: contradiction. By note 01 Theorem 5
exactly one line is nonzero; for it (A_m), (A_x), (Tr) read m = 2mx + x^2, x = m^2 + 2mx, m^2 + x^2 = 3. Subtracting,
(m - x)(1 + m + x) = 0; m = x gives 3m^2 = m, incompatible with (Tr); so x = -1 - m and m^2 + m - 1 = 0:
(m, x) = (1/phi, -phi) or (-phi, 1/phi). On line k the MUB-pair plane on the eigenvalues zeta^mu, zeta^mu' of W_(v_k) has
Y_k(j) = zeta^(-mu j) + zeta^(-mu' j) (note 01 Lemma 2), real iff mu' = -mu, giving (2cos(2pi mu/5), 2cos(4pi mu/5)) =
(1/phi, -phi) for mu = +-1 and (-phi, 1/phi) for mu = +-2. Consequence: D_v Pi D_v^(-1) is a phase times D_(2v) Pi, and P
is invariant under it iff D_v^* P D_v is Pi-invariant; translates of MUB-pair planes are MUB-pair. QED

## 3. QK-invariant flat planes
**Theorem 3.** The flat planes with (QK) P (QK)^(-1) = P are exactly the two Pi-invariant MUB-pair planes of l_2
(Theorem 2, k = 2). Consequently every flat plane invariant under a translate D_v QK D_v^(-1) is MUB-pair.
Proof. Put a := alpha_1, b := beta_1 (so alpha_3 = conj(a), beta_3 = conj(b)) and c := alpha_2, d := beta_2 (real).
X1, X2, Z1, Z2 of note 01 Theorem 4 become
  (X1) b (c - phi^2 d) = phi^2 conj(a) conj(b),  (X2) conj(a) (d - phi^2 c) = phi^2 a conj(b),
  (Z1) b^2 = 2 phi^2 c conj(a),  (Z2) conj(a)^2 = 2 phi^2 d conj(b).
If a = b = 0, only l_2 is nonzero and its data are real: Theorem 2 (k = 2). Otherwise Z1, Z2 show a != 0 != b
(a = 0 forces b^2 = 0 and conversely), hence c != 0 != d. Write a = A e^(i theta), b = B e^(i psi), A, B > 0. Z1 gives
e^(i(2psi + theta)) = sign(c) and B^2 = 2phi^2 |c| A; X1 gives (c - phi^2 d) e^(i(2psi + theta)) = phi^2 A > 0, so
sign(c - phi^2 d) = sign(c) and |c - phi^2 d| = phi^2 A. Z2 gives e^(i(psi - 2theta)) = sign(d) and A^2 = 2phi^2 |d| B;
X2 gives (d - phi^2 c) = phi^2 B e^(i(2theta - psi)), so sign(d - phi^2 c) = sign(d) and |d - phi^2 c| = phi^2 B.
If c > 0 then d < c/phi^2, and d > 0 would give d > phi^2 c > c/phi^2; so d < 0. If c < 0 then d > c/phi^2, and d < 0 would
give d < phi^2 c < c/phi^2; so d > 0. Hence c, d have opposite signs and, with g := |c|, h := |d| > 0:
  A = g/phi^2 + h, B = g + h/phi^2, B^2 = 2phi^2 g A, A^2 = 2phi^2 h B.
Expanding with phi^2 - phi^(-2) = sqrt5: g^2 + 2sqrt5 g h - h^2/phi^4 = 0 and h^2 + 2sqrt5 g h - g^2/phi^4 = 0. So both g/h and
h/g are the unique positive root of t^2 + 2sqrt5 t - phi^(-4) (the product of its roots is negative); hence g = h and
1 + 2sqrt5 = phi^(-4) < 1, a contradiction. Translates: as in Theorem 2. QED
(Only the forbidden equations were needed in Theorem 3.)

## 4. Status
Proved: Pi-type and QK-type symmetric flat planes are MUB-pair. With note 02: translation- and D_w U D_w^*-symmetric
flat planes are MUB-pair or in F. Remaining involution class (QPiK, which fixes the P_tau) and conjugates under the full
symmetry group: later notes. No statement here about planes without symmetry; 1-RQLS(10) OPEN / UNKNOWN.
