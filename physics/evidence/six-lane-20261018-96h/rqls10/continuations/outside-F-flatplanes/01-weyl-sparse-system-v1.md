# Flat planes as Weyl-sparse idempotents: exact polynomial system, support lemma, MUB-pair planes (v1)

Recorded after actual `/bin/date`: 2026-10-19T21:36:26-0700 (written in the following minutes). ContinueRQLS10b.
Single author, UNREVIEWED, written only, not Lean-checked. Scope: 00-scope-freeze-v1.md (3e161b96...31e5).
No computation; decimals never used. Nothing here assumes anything about F. 1-RQLS(10) stays OPEN / UNKNOWN.

## 1. Symmetric Weyl operators
zeta = e^(2 pi i/5), phi = (1 + sqrt5)/2, 2^(-1) = 3 in Z_5. X e_t = e_(t+1), Z e_t = zeta^t e_t, so ZX = zeta XZ and
Z^c X^a' = zeta^(c a') X^a' Z^c. For z = (a, c) in Z_5^2 put W_z := zeta^(3ac) X^a Z^c and [u, v] := u_1 v_2 - u_2 v_1.
**Lemma 1.** (a) W_u W_v = zeta^(2[u,v]) W_(u+v); W_z^* = W_(-z); W_(ju) W_(iu) = W_((i+j)u); W_u^5 = I.
(b) tr(W_u^* W_v) = 5 delta_(u,v), so every operator P equals (1/5) sum_z y_z W_z with y_z := tr(W_z^* P).
(c) P Hermitian iff y_(-z) = conj(y_z) for all z.
Proof. (a) X^a Z^c X^a' Z^c' = zeta^(c a') X^(a+a') Z^(c+c'); collecting powers, the phase of W_u W_v W_(u+v)^(-1) is
zeta^(3ac + 3a'c' + ca' - 3(a+a')(c+c')) = zeta^(-2ca' - 3ac') = zeta^(3ca' - 3ac') = zeta^(-3[u,v]) = zeta^(2[u,v]).
W_z^* = zeta^(-3ac) Z^(-c) X^(-a) = zeta^(-3ac + ac) X^(-a) Z^(-c) = zeta^(3ac) X^(-a) Z^(-c) = W_(-z). [ju, iu] = 0 gives the
collinear rule, hence W_u^5 = W_0 = I. (b) W_u^* W_v is a multiple of W_(v-u), traceless unless v = u (X^a Z^c has zero
diagonal for a != 0 and trace sum_t zeta^(ct) = 0 for a = 0, c != 0). (c) conj(y_z) = tr(P^* W_z) = tr(W_z P^*) and
y_(-z) = tr(W_z P). QED

## 2. Lines and flatness
Lines through 0: L_Z = {(0,c)}, L_X = {(a,0)}, L_T = {(a,-a)} ("forbidden"), and l_k = {j v_k : j in Z_5}, v_k := (1, k),
k = 1, 2, 3 ("allowed"). W_(0,c) is a multiple of Z^c, W_(a,0) = X^a, W_(a,-a) is a multiple of (X Z^(-1))^a, and
X Z^(-1) g_m = zeta^(3 - m) g_m (direct check: the exponent difference -(t-1) + 2(t-1)^2 + m(t-1) - 2t^2 - mt = 3 - m - 5t).
So for b in {Z, X, T} the W_z, z in L_b, are diagonal in beta_b with eigenvalues characters of L_b.
**Lemma 2 (flatness).** A Hermitian P with tr P = 2 is flat (scope (Fl)) iff y_z = 0 for every z != 0 on L_Z, L_X, L_T.
Proof. Fix b, write p_m := b_m^* P b_m and W_z b_m = lambda_m(z) b_m (z in L_b). Then y_z = sum_m conj(lambda_m(z)) p_m; as
z runs over L_b (a group isomorphic to Z_5) the maps m -> lambda_m(z) are the five distinct characters (W_z for a generator
z has five distinct eigenvalues, the fifth roots of unity, by W_z^5 = I and tr W_z^j = 0). Character inversion: (p_m) is
constant iff y_z = 0 for all z in L_b \ 0. QED
**Lemma 3 (idempotency).** P = (1/5) sum y_z W_z with y_0 = 2 is a rank-2 orthogonal projector iff P is Hermitian and
  (I_z)  sum_u y_u y_(z-u) zeta^(2[u,z]) = 5 y_z   for every z in Z_5^2.
Proof. P^2 = (1/25) sum_(u,v) y_u y_v zeta^(2[u,v]) W_(u+v) by Lemma 1(a); substitute v = z - u, [u, z - u] = [u, z], compare
coefficients (Lemma 1(b)). A Hermitian idempotent with trace 2 is a rank-2 orthogonal projector. QED
(I_0) reads sum_(u != 0) |y_u|^2 = 6. For z != 0 the terms u = 0, z contribute 4 y_z, so (I_z) is
  sum_(u not in {0, z}) y_u y_(z-u) zeta^(2[u,z]) = y_z.

## 3. The explicit system
Write Y_k(j) := y_(j v_k) (j in Z_5^*), alpha_k := Y_k(1), beta_k := Y_k(2); by Lemma 1(c) Y_k(4) = conj(alpha_k),
Y_k(3) = conj(beta_k). For a flat P (Lemma 2) y is supported on {0} and the twelve points of l_1, l_2, l_3 minus 0.
For u = j v_k, v = j' v_k' (k != k'): [u, v] = j j' (k' - k), and u + v = (j + j', jk + j'k') lies on a line other than
l_k, l_k'. Solving u + v = z for z on each forbidden line (inverses in Z_5: 2^(-1) = 3, 3^(-1) = 2, 4^(-1) = 4):
  pair (1,2): (a,0) = 2a v_1 + 4a v_2, [u,v] = 3a^2; (0,c) = 4c v_1 + c v_2, [u,v] = 4c^2; (a,-a) = 3a v_1 + 3a v_2, 4a^2;
  pair (1,3): (a,0) = 4a v_1 + 2a v_3, a^2;  (0,c) = 2c v_1 + 3c v_3, 2c^2;  (a,-a) = 2a v_1 + 4a v_3, a^2;
  pair (2,3): (a,0) = 3a v_2 + 3a v_3, 4a^2; (0,c) = 4c v_2 + c v_3, 4c^2; (a,-a) = 4a v_2 + 2a v_3, 3a^2;
and the fourth ratio of each pair lands on the third allowed line: j v_1 + 3j v_2 = 4j v_3, j v_1 + j v_3 = 2j v_2,
j v_2 + 2j v_3 = 3j v_1. (Each line is checked by substituting into (j + j', jk + j'k').)
In (I_z) the ordered terms (u, z - u) and (z - u, u) combine to y_u y_(z-u) (zeta^(2s) + zeta^(-2s)) with s = [u, z] = [u, v],
and zeta^(2s) + zeta^(-2s) = 2cos(4 pi s/5) equals -phi for s = +-1 and 1/phi for s = +-2. Since a^2, c^2 in {1, 4}, the
coefficient depends only on (pair, line):
              L_X     L_Z     L_T            (allowed third line: always 1/phi, as s = 3j^2 there)
  pair (1,2): 1/phi   -phi    -phi
  pair (1,3): -phi    1/phi   -phi
  pair (2,3): -phi    -phi    1/phi
For z forbidden, u, z - u must lie on two different allowed lines (y vanishes elsewhere and y_z = 0), one term per pair.
For z = j v_k allowed, the terms are u in l_k \ {0, z} (coefficient 1) and one cross pair. Taking a, c, j in {1, 2}
(the values 3, 4 give the complex conjugate equations by Lemma 1(c)) and multiplying the forbidden ones by phi:
**Theorem 4 (exact system).** A Hermitian P with tr P = 2 is a flat rank-2 projector iff y_z = 0 on the forbidden lines
and (alpha_k, beta_k) (k = 1, 2, 3) satisfy (overline = complex conjugate):
  (X1) beta_1 conj(alpha_2) = phi^2 [conj(alpha_1) beta_3 + conj(beta_2) conj(beta_3)]
  (X2) conj(alpha_1) conj(beta_2) = phi^2 [conj(beta_1) conj(alpha_3) + alpha_2 alpha_3]
  (Z1) beta_1 conj(beta_3) = phi^2 [conj(alpha_1) alpha_2 + conj(alpha_2) alpha_3]
  (Z2) conj(alpha_1) alpha_3 = phi^2 [conj(beta_1) beta_2 + conj(beta_2) beta_3]
  (T1) conj(alpha_2) beta_3 = phi^2 [conj(beta_1) conj(beta_2) + beta_1 conj(alpha_3)]
  (T2) conj(beta_2) conj(alpha_3) = phi^2 [alpha_1 alpha_2 + conj(alpha_1) conj(beta_3)]
  (A1_1) 2 conj(alpha_1) beta_1 + conj(beta_1)^2 + (1/phi) beta_2 conj(alpha_3) = alpha_1
  (A1_2) alpha_1^2 + 2 conj(alpha_1) conj(beta_1) + (1/phi) conj(alpha_2) conj(beta_3) = beta_1
  (A2_1) 2 conj(alpha_2) beta_2 + conj(beta_2)^2 + (1/phi) conj(beta_1) conj(beta_3) = alpha_2
  (A2_2) alpha_2^2 + 2 conj(alpha_2) conj(beta_2) + (1/phi) alpha_1 alpha_3 = beta_2
  (A3_1) 2 conj(alpha_3) beta_3 + conj(beta_3)^2 + (1/phi) conj(alpha_1) beta_2 = alpha_3
  (A3_2) alpha_3^2 + 2 conj(alpha_3) conj(beta_3) + (1/phi) conj(beta_1) conj(alpha_2) = beta_3
  (Tr)  sum_k (|alpha_k|^2 + |beta_k|^2) = 3.
Proof. Lemmas 2, 3 and the table. E.g. (X1) is (I_(1,0)): pair (1,2) gives (1/phi) Y_1(2) Y_2(4), pair (1,3) gives
-phi Y_1(4) Y_3(2), pair (2,3) gives -phi Y_2(3) Y_3(3); (A1_1) is (I_(v_1)): u in {2v_1, 3v_1, 4v_1} gives
Y_1(2)Y_1(4) + Y_1(3)^2 + Y_1(4)Y_1(2), and the cross pair (2,3) gives (1/phi) Y_2(2) Y_3(4). The others are read off the
same way from the table; (Tr) is (I_0). QED
So flat planes <-> points of a real-algebraic set in C^6 (12 real unknowns): an exact parametrization with no reference
to F. Conjugate equations (a, c, j in {3, 4}) are implied.

## 4. Support lemma and the MUB-pair planes
For k in {1,2,3} let N_k := (1/5) sum_(j != 0) Y_k(j) W_(j v_k); it is diagonal in the eigenbasis B_k of W_(v_k), and
P = (2/5) I + N_1 + N_2 + N_3 for flat P.
**Theorem 5.** Let P be flat. (a) If exactly one N_k is nonzero, P = w w^* + w' w'^* for two distinct vectors w, w' of B_k
(a MUB-PAIR plane). (b) Exactly two nonzero N_k is impossible. (c) N_1 = N_2 = N_3 = 0 is impossible.
Conversely every MUB-pair plane (k in {1,2,3}, any two of the five vectors of B_k) is flat: 30 distinct flat planes.
Proof. (c) contradicts (Tr). (a) P = (2/5)I + N_k is diagonal in B_k and idempotent of trace 2, so its diagonal there is a
0/1 vector with two ones. (b) Say N_k, N_k' != 0 = N_k''. Each forbidden equation keeps only its (k, k') term, whose
coefficient is nonzero, so Y_k(j) Y_k'(j') = 0 for the twelve (j, j') with j' != r j (r the ratio landing on l_k'', from the
list in section 3). Pick j with Y_k(j) != 0; then also Y_k(-j) != 0, so Y_k'(j') = 0 unless j' = rj and j' = -rj, which
never happen together; thus N_k' = 0, a contradiction. Converse: B_k is unbiased to beta_Z, beta_X, beta_T (B_k is the
eigenbasis of X Z^k, whose eigenvectors are zeta^(c t^2 + m t)/sqrt5 with 2c = k, and Gauss sums of nonzero quadratic
coefficient have modulus sqrt5), so each diagonal entry is 1/5 + 1/5. Distinct pairs give distinct projectors; vectors of
different B_k are not orthogonal, so the 30 planes are distinct. QED
**Corollary 6.** Every flat plane that is not one of the 30 MUB-pair planes has N_1, N_2, N_3 all nonzero, i.e. its
diagonals in all three remaining mutually unbiased bases are non-constant.
Status: exact reformulation only; no classification is claimed here. Membership of MUB-pair planes in F, the symmetry
group and symmetric solutions are treated in later notes of this package.
