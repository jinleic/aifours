# WH_10 single-orbit ansatz: the C^5 flat-plane problem for the line triple {L_inf, L_0, L_2} (v1)

Recorded 2026-10-19T04:29:10-0700 (from /bin/date; written in the following minutes). Author ContinueRQLS10b. Lane-internal,
single author, unreviewed, NOT parent-accepted. Restricted ansatz only; the target stays OPEN / UNKNOWN. No novelty claim.
Builds on evidence/wh10-reduction-v1.md (7e77051c33431921c6d50ddcd8bd2f1c1ba961a0956cb2678f529d0290c0cac8), Theorem W4.
Exact computations: code/wh10_flat_system_v1.py (receipt evidence/wh10_flat_system_v1.receipt.md, to follow).

## 0. Setting
zeta = e^(2 pi i/5), X e_t = e_(t+1), Z e_t = zeta^t e_t on C^5, tau = zeta^3 (tau^2 = zeta), D_(a,c) = tau^(ac) X^a Z^c,
<(a,c),(a',c')> = a c' - c a', so D_u D_v = tau^(-<u,v>) D_(u+v) and D_u^* = D_(-u) (checked exactly). L_s = <(1,s)>,
L_inf = <(0,1)>. B_Z, B_X, B_2 = eigenbases of Z, X, X Z^2 (lines L_inf, L_0, L_2). Theorem W4: (H_10) <=> there is a 2-plane
S (projector P) flat in B_Z, B_X, B_2 (v^* P v = 2/5) containing unit vectors q_Z, q_X, q_2, pairwise unbiased, with q_a
flat in B_a. Unused (complementary) lines: L_1, L_3, L_4; e_k := (1, k); c(n) := tau^n + tau^-n, so c(+-1) = -phi and
c(+-2) = 1/phi (phi the golden ratio, phi = 1 + zeta + zeta^4), Phi := phi^2.

## 1. Lemma F1 (normal form; proof as Lemma 2 of evidence/w8-decision-v1.md)
P is a flat plane for the triple iff P = (2/5) I + S, S = sum_(k in {1,3,4}) sum_(x in Z_5^*) alpha_k(x) D_(x e_k) with
alpha_k(-x) = conj(alpha_k(x)), and S^2 = S/5 + (6/25) I. Unknowns: a_x = alpha_1(x), b_x = alpha_3(x), g_x = alpha_4(x),
i.e. (a_1, a_2, b_1, b_2, g_1, g_2) in C^6 (12 real numbers).

## 2. Proposition F2 (explicit system; exact derivation, checked exactly)
The 25 WH components of S^2 - S/5 - (6/25) I are (sums over x, y in Z_5^* with x + y = z):
 w = 0:       sum_x (|a_x|^2 + |b_x|^2 + |g_x|^2) - 6/25
 w = (0, c):  a_2c b_3c c(2c^2) + a_3c g_2c c(3c^2) + b_4c g_c c(4c^2)
 w = (s, 0):  a_4s b_2s c(s^2) + a_3s g_3s c(2s^2) + b_4s g_2s c(3s^2)
 w = (s, 2s): a_3s b_3s c(3s^2) + a_4s g_2s c(4s^2) + b_2s g_4s c(3s^2)
 w = z e_1:   sum a_x a_y + b_3z g_3z c(4z^2) - a_z/5
 w = z e_3:   sum b_x b_y + a_2z g_4z c(4z^2) - b_z/5
 w = z e_4:   sum g_x g_y + a_2z b_4z c(z^2) - g_z/5
Derivation: D_(x e_k) D_(y e_l) = tau^(-xy(l-k)) D_(x e_k + y e_l); a vector w outside L_k u L_l has exactly one decomposition
w = x e_k + y e_l, and the two orders contribute alpha_k(x) alpha_l(y) c(xy(l - k)); the decompositions were solved by hand
for each target line. Flat planes = common zeros. The used-line part, multiplied by phi (c = 1, 2; s = 1, 2):
 U1 a_2 b_3 + a_3 g_2 - Phi b_4 g_1 = 0     U2 a_4 b_1 + a_1 g_4 - Phi b_3 g_2 = 0
 U3 -Phi a_4 b_2 + a_3 g_3 + b_4 g_2 = 0    U4 -Phi a_3 b_4 + a_1 g_1 + b_3 g_4 = 0
 U5 a_3 b_3 - Phi a_4 g_2 + b_2 g_4 = 0     U6 a_1 b_1 - Phi a_3 g_4 + b_4 g_3 = 0
(c = 3, 4 and s = 3, 4 are the complex conjugates). Complementary-line part (z = 1, 2), all cross coefficients -phi:
 2 a_2 a_4 + a_3^2 - phi b_3 g_3 = a_1/5;  a_1^2 + 2 a_3 a_4 - phi b_1 g_1 = a_2/5;
 2 b_2 b_4 + b_3^2 - phi a_2 g_4 = b_1/5;  b_1^2 + 2 b_3 b_4 - phi a_4 g_3 = b_2/5;
 2 g_2 g_4 + g_3^2 - phi a_2 b_4 = g_1/5;  g_1^2 + 2 g_3 g_4 - phi a_4 b_3 = g_2/5;
 2 (|a_1|^2 + |a_2|^2 + |b_1|^2 + |b_2|^2 + |g_1|^2 + |g_2|^2) = 6/25.

## 3. Lemma F3 (one vanishing block forces a MUB-pair plane; written, complete)
If a flat plane for the triple has A_k = 0 for one k in {1, 3, 4}, it is a MUB-pair plane (spanned by two vectors of one
complementary basis). Proof: with A_k = 0 only the pair (i, j) of the other two lines contributes to the used-line
components, one product alpha_i(x) alpha_j(y) per used vector w = x e_i + y e_j, which must vanish. The ratios y/x hit
by the three used lines are R = {4, 3, 1} for (i,j) = (1,3), {4, 1, 3} for (1,4), {4, 3, 2} for (3,4) (solving the
decompositions; checked exactly). If alpha_i(x) != 0 then alpha_i(-x) = conj(alpha_i(x)) != 0, which kills alpha_j(y) for
y/x in R u (-R) = Z_5^* in all three cases; so A_j = 0 and P = (2/5) I + A_i is diagonal in the basis of L_i, i.e. a
MUB-pair plane. With Corollary W6 (MUB-pair planes violate condition (c)): in every WH_10 solution, all three blocks
A_1, A_3, A_4 are nonzero.

## 4. Proposition F4 (equivalent forms of condition (c); written, complete)
Let S be flat in B_a, Phi_S: C^2 -> S an isometry, and n_a(v) the Bloch vector of Phi_S^* v (|Phi_S^* v|^2 = 2/5) for v in B_a.
(i) Per basis: TFAE (1) S contains a B_a-flat unit vector; (2) the five n_a(v) lie on one great circle (their sum is 0
    by flatness, so they are never collinear: 5 is odd); (3) S is invariant under an antiunitary involution J_a = E_a K_a,
    K_a the complex conjugation in B_a and E_a diagonal unitary in B_a. Then the B_a-flat unit vectors of S are exactly
    the two states with Bloch vectors +-m_a (m_a the normal of the circle), so q_a is determined up to phase and
    orthogonal complement. Proof: |<v, q>|^2 = (1/5)(1 + n_a(v) . m) for the Bloch vector m of q, so (1) <=> (2);
    (2) <=> rows of Phi_S in B_a are real up to one phase per row in a suitable frame <=> (3) with E_a the squared
    phases (and conversely a J_a-real orthonormal basis of S gives such a frame).
(ii) Cross condition: q_Z, q_X, q_2 pairwise unbiased <=> m_Z, m_X, m_2 pairwise orthogonal <=> the antiunitary
    Theta := J_Z J_X J_2 satisfies Theta^2 = -1 on S (on the Bloch sphere of S the J_a are reflections in the planes
    m_a-perp; three reflections compose to -id iff the planes are mutually orthogonal). Theta^2 is a unitary of C^5 and
    its (-1)-eigenspace is Theta-invariant with a quaternionic structure, so it has dimension 2 or 4 and contains S.
(iii) Perfect-sequence form: write b_0(s) = u_s / sqrt10, b_1(s) = u_s w_s / sqrt10 with |u_s| = |w_s| = 1 (rows of (H_10) give
    |b_0(s)| = |b_1(s)|). Then (H_10) <=> the four length-5 sequences c_+-(s) = u_s (1 +- w_s) and d_+-(s) =
    zeta^(-s^2) u_s (1 +- i w_s) have flat DFT moduli (|sum_s c(s) zeta^(-ks)|^2 = 10 for all k). Proof: the column and class
    conditions of W4 read |A_k|^2 + |B_k|^2 = 10, Re(conj(A_k) B_k) = 0 and the same with Im for the chirped sums,
    i.e. |A_k +- B_k|^2 = 10 and |A'_k +- i B'_k|^2 = 10. Parseval then gives sum_s w_s = 0 (five unit vectors closing up).

## 5. Proposition F5 (C-symmetric planes: reduction to a finite computation; written, complete as a reduction)
M = [[4,3],[3,0]] in SL(2,5) has M^3 = I, M^2 + M + I = 0, and maps L_inf -> L_0 -> L_2 -> L_inf and L_1 -> L_4 -> L_3 -> L_1
(direct computation). Its Weil-representation unitary C satisfies C^3 = I (the Weil representation of SL(2,p), p odd, is
linear) and has eigenspaces of dimensions 1, 2, 2 (all order-3 elements of SL(2,5) are conjugate; |tr C| = 1 for an
elliptic element leaves only the multiset {1, 2, 2}). C permutes the three bases (up to phases) cyclically. Let S be
C-invariant. (a) If S is a 2-dimensional eigenspace, C acts on S as a scalar, the normals satisfy m_X = m_Z, and (ii)
fails. (b) Otherwise S = l (+) l' with l, l' in distinct eigenspaces; C acts on the Bloch sphere of S as a rotation R by
+-120 degrees about an axis a; flatness in B_Z implies flatness in B_X and B_2 (transport by C), and the conditions
v^* P v = 2/5 are AFFINE in the Bloch vectors (n_l, n_l') of l and l' inside their eigenspaces, so the C-invariant flat
planes of this type are the points of an affine 2-plane of R^6 (if l, l' both vary) intersected with S^2 x S^2: at most
four (Bezout) unless degenerate; of type (1-dim eigenspace) (+) l: an affine condition set on one sphere, generically
empty. (c) For such S, condition (i) for B_Z implies it for B_X, B_2 with m_X = R m_Z, m_2 = R^2 m_Z, and (ii) holds iff
m_Z . a = +-1/sqrt3 (cos of the angle between m and R m is (3 (m.a)^2 - 1)/2). Hence the C_w-symmetric WH_10 solutions
(C_w = D_w C D_w^*, w in Z_5^2, all of which stabilise the triple) are decided by a finite exact computation:
eigenspaces of C in Q(zeta_15), an affine solve, the intersection with two spheres (a quartic), and two checks.
This computation has NOT been carried out.

## 6. Status (scoped)
Proved (single author): F1, F2 (with exact check), F3, F4, F5 (as a reduction). Not established: that every
non-MUB-pair flat plane for this triple is C_w-invariant (for W8's triple this held for all 100 planes found numerically;
those planes are NOT transported here - the triples are not Clifford-equivalent); the finite C-symmetric computation; any
completeness statement. Observation (parent run, float): every LM target run stalled at the same residual
0.13757415725848..., suggesting a structured global minimiser of the residual; identifying it exactly could give a
lower-bound certificate, but nothing is claimed. Any numerical plane enumeration needs a new GO with a frozen plan and
positive controls (proposal: the enumerator must reproduce the 30 MUB-pair planes and, as an external positive control,
the 130-plane list of the W8 triple; then classify the planes of this triple and test F4 (i)-(ii) on each).
