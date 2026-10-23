# U-invariant flat planes are exactly four; F is exactly the set of flat planes with a D_w U D_w^* symmetry (v1)

Recorded after actual `/bin/date`: 2026-10-19T21:43:23-0700 (written in the following minutes). ContinueRQLS10b.
Single author, UNREVIEWED, written only, not Lean-checked. Uses note 01 (6be70323...b09a) and, where stated, the
PARENT-ACCEPTED E1 interface (RUN/review/rqls10-E1-nonMUB-parent-verdict-v1.md, ad790caa850c16e14706a95bad12b7c2297ff4221cedc5a9c6b85389eec9e872:
E1 section 4 closed form and Proposition 9 at literal scope). No unreviewed candidate is a premise. No computation.

## 1. Covariance (no phases)
F e_m := f_m, Q := diag(zeta^(2t^2)), U := Q F^*. Notation W_z, [u,v], v_k, l_k as in note 01.
**Lemma 1.** (a) U W_z U^* = W_(Mz) with M(a, c) := (c, -a - c). (b) W_w W_z W_w^* = zeta^(4[w,z]) W_z, so for
D_w = X^a Z^c (w = (a,c)) the translate D_w P D_w^* has coefficients y'_z = zeta^(4[w,z]) y_z.
Proof. X f_m = zeta^(-m) f_m and Z f_m = f_(m+1) give F^* X F = Z^(-1), F^* Z F = X. Q X Q^* e_t = zeta^(2(t+1)^2 - 2t^2)
e_(t+1) = zeta^(4t+2) e_(t+1) = zeta^2 X Z^(-1) e_t, and zeta^2 X Z^(-1) = W_(1,-1); Q Z Q^* = Z. So U X U^* = Z^(-1) = W_(0,-1)
and U Z U^* = W_(1,-1). By Lemma 1 of note 01, U W_(a,c) U^* = zeta^(3ac) W_(0,-a) W_(c,-c) (collinear powers) and
W_(0,-a) W_(c,-c) = zeta^(2[(0,-a),(c,-c)]) W_(c,-a-c) = zeta^(2ac) W_(c,-a-c); total phase zeta^(5ac) = 1.
(b) note 01 Lemma 1(a) twice: zeta^(2[w,z] + 2[w+z,-w]) = zeta^(4[w,z]); D_w differs from W_w by a phase. QED
On the allowed lines: M(j v_1) = (j, -2j) = j v_3, M(j v_3) = (3j, -4j) = 3j v_2, M(j v_2) = (2j, -3j) = 2j v_1.
M - I = [[-1, 1], [-1, -2]] has determinant 3, so M - I is invertible on Z_5^2.

## 2. Reduction
**Theorem 2.** A flat P satisfies U P U^* = P iff its data (note 01, section 3) are
  alpha_1 = alpha_3 =: a, beta_1 = beta_3 =: b, alpha_2 = b, beta_2 = conj(a),
and then the system of note 01 Theorem 4 is equivalent to
  (A1) a = 2 conj(a) b + conj(b)^2 + conj(a)^2/phi,     (A2) b = a^2 + 2 conj(a) conj(b) + conj(b)^2/phi,
  (F1) |b|^2 = 2 phi^2 Re(conj(a) b),   (F2) |a|^2 = 2 phi^2 Re(a b),   (Tr) |a|^2 + |b|^2 = 1.
Proof. U P U^* = (1/5) sum y_z W_(Mz), so invariance is y_(Mz) = y_z; by the action of M on the allowed lines this is
Y_3(j) = Y_1(j) and Y_2(j) = Y_1(2j), i.e. the displayed data (Y_1(4) = conj(a)). Substituting: X1, Z1, T1 become (F1);
X2, Z2, T2 become (F2); A1_1, A3_1 and the conjugate of A2_2 become (A1); A1_2, A3_2, A2_1 become (A2); (Tr) becomes
3(|a|^2 + |b|^2) = 3. (E.g. Z2: conj(alpha_1) alpha_3 = |a|^2 and phi^2 [conj(beta_1) beta_2 + conj(beta_2) beta_3] =
phi^2 [conj(b) conj(a) + a b].) QED

## 3. The exact solution
**Theorem 3.** The solutions of (A1), (A2), (F1), (F2), (Tr) are exactly the four points
  a = -1/(2 phi) + i x, b = -1/(2 phi) + i y, with x^2 + y^2 = phi/2 and y^2 - x^2 = 4 phi^2 x y
(the circle meets the two distinct lines y^2 - x^2 - 4phi^2 xy = 0 through 0 in four points). All a, b are nonzero.
Proof. Write a = a1 + i a2, b = b1 + i b2, S := a1 + b1, D := a1 - b1. (F1) + (F2) is |a|^2 + |b|^2 = 2phi^2 Re((a +
conj(a)) b) = 4 phi^2 a1 b1, so with (Tr): a1 b1 = 1/(4 phi^2), hence S^2 - D^2 = 1/phi^2. (F1) - (F2) is
|b|^2 - |a|^2 = 2phi^2 Re(-2i a2 b) = 4 phi^2 a2 b2. Real and imaginary parts of (A1), (A2):
  (A1r) a1 = 2(a1 b1 + a2 b2) + b1^2 - b2^2 + (a1^2 - a2^2)/phi,   (A1i) a2 (1 + 2b1 + 2a1/phi) = 2 b2 D,
  (A2r) b1 = a1^2 - a2^2 + 2(a1 b1 - a2 b2) + (b1^2 - b2^2)/phi,   (A2i) b2 (1 + 2a1 + 2b1/phi) = 2 a2 D.
(A1r) + (A2r): S = 4a1b1 + phi(a1^2 + b1^2 - a2^2 - b2^2) (1 + 1/phi = phi). With (Tr) and a1^2 + b1^2 = S^2 - 1/(2phi^2):
S = 1/phi^2 + phi(2S^2 - 1/phi^2 - 1), i.e. 2phi S^2 - S + (3 - 3phi) = 0 (1/phi^2 = 2 - phi, 1/phi = phi - 1), whose
discriminant is 1 - 24phi + 24phi^2 = 25 (phi^2 = phi + 1): S = -1/phi or S = 3/(2phi).
Case S = 3/(2phi): D^2 = S^2 - 1/phi^2 = 5/(4phi^2) != 0. If a2 = 0, (A1i) gives b2 = 0; then (F1) - (F2) gives
b1^2 = a1^2, so b1 = -a1 (D != 0) and a1 b1 <= 0, contradiction. If b2 = 0 != a2, (A2i) gives D a2 = 0, contradiction.
So a2 b2 != 0 and multiplying (A1i), (A2i): c_a c_b = 4D^2 with c_a = 1 + phi S - D/phi^2, c_b = 1 + phi S + D/phi^2
(substitute 2a1 = S + D, 2b1 = S - D). Thus (1 + phi S)^2 - D^2/phi^4 = 4D^2, i.e. 25/4 - 5/(4phi^6) = 5/phi^2, i.e.
5phi^6 - 4phi^4 - 1 = 0; but phi^4 = 3phi + 2, phi^6 = 8phi + 5 give 5phi^6 - 4phi^4 - 1 = 28 phi + 16 > 0. Impossible.
Case S = -1/phi: D^2 = 0, so a1 = b1 = -1/(2phi); then 1 + 2b1 + 2a1/phi = 1 - (1 + 1/phi)/phi = 0, so (A1i), (A2i) hold.
(A1r) - (A2r) reads D = 4a2b2 + (1 - 1/phi)[(b1^2 - b2^2) - (a1^2 - a2^2)], i.e. (1 - 1/phi = 1/phi^2) 0 = 4xy + (x^2 - y^2)/phi^2,
the same as (F1) - (F2); (Tr) reads x^2 + y^2 = 1 - 1/(2phi^2) = phi^3/(2phi^2) = phi/2; given these, (F1) + (F2) and
(A1r) + (A2r) hold by the computation above (a1 b1 = 1/(4phi^2), S = -1/phi is a root). QED
**Corollary 4.** Exactly four flat planes commute with U (note 01 Theorem 4 is an equivalence), for every eigen-type.

## 4. Identification with the four P_tau (accepted interface)
By the accepted E1 Proposition 9(b) there are exactly four flat planes of type (line of E(-omega)) + (line of
E(-omega^2)); they commute with U. By the accepted E1 section 4 closed form (sigma = sigma' = +1) and Proposition 9(b)
(x = sqrt(p) a^ + i sigma zeta sqrt(1-p) b^, y likewise with sigma'), whose sigma-dependence multiplies only the terms
i s sqrtB, i s sqrtA, they are exactly the frozen P_tau, tau in {+-1}^2 (00-scope-freeze-v1.md, definition of F).
**Corollary 5.** The planes of Theorem 3 are exactly P_tau (four commuting flat planes, Corollary 4, contain the four
accepted ones). In particular every U-invariant flat plane is of that eigen-type.

## 5. The translates: exactly 100, and an intrinsic description of F
**Theorem 6.** (a) For P in S := {P_tau} and w != 0, D_w P D_w^* is not U-invariant. (b) The 100 planes D_w P_tau D_w^*
are pairwise distinct; so |F| = 100. (c) A flat plane lies in F iff it commutes with D_w U D_w^* for some w in Z_5^2;
the flat planes commuting with D_w U D_w^* are exactly the four D_w P_tau D_w^*. (d) No plane of F is MUB-pair, and
none is invariant under a nontrivial translation D_w.
Proof. (a) If y' (Lemma 1(b)) were U-invariant: zeta^(4[w,Mz]) y_(Mz) = zeta^(4[w,z]) y_z with y_(Mz) = y_z != 0
(Theorems 2, 3) for the twelve allowed z, which span Z_5^2, so [w, (M - I)u] = 0 for all u; M - I is invertible, so w = 0.
(b) Equality of D_w P D_w^* and D_w' P' D_w'^* makes P' a U-invariant translate of P by w - w', so w = w' and P = P'.
(c) P commutes with D_w U D_w^* iff D_w^* P D_w commutes with U; apply Corollary 5. (d) Translation multiplies each
y_z by a phase, so all three allowed lines carry nonzero data (note 01 Theorem 5); a D_w-invariant plane (w != 0) is spanned
by two eigenvectors of D_w (five distinct eigenvalues), i.e. it is MUB-pair (allowed line) or has diagonal (1,1,0,0,0) in a
forbidden basis (not flat). QED
This settles the translate count left open by E1 (exactly 100). Not claimed: that every flat plane has a symmetry.
**Corollary 7.** A flat plane outside F that is not MUB-pair has no symmetry D_w U^(+-1) D_w^* and no translation symmetry.
Remaining symmetric cases (unitary involutions, antiunitary involutions) and the general case are treated later.
