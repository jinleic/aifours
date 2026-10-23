# W8 addendum 1: written analysis of the WH_5 (x) C^2 orbit ansatz (no computation run)

Recorded 2026-10-19T01:19:58-0700. Extends evidence/w8-wh5-c2-orbit-ansatz-setup-v1.md (sha256 bedfe9a7b35771f4c4e119c8431535d839c87180170bc67523fee6c6c5ce6471).
Lane-internal, unreviewed, restricted. Notation: X_r (r in {00,01,10,11}) the 5 x 2 representative matrices; for a basis
vector e of the bases Z (computational), X (Fourier), T (eigenbasis of X Z^-1), e^dag X_r in C^2 is its row.
Couples: Z: 00-01, 10-11; X: 00-10, 01-11; T: 00-11, 01-10 (the three perfect matchings of K4).

**Lemma 1 (Gram matrices).** X_r^dag X_r = I_2 / 2 for every r. Proof: for a couple (r, r') in basis b and e in b the two
rows sqrt5 e^dag X_r, sqrt5 e^dag X_r' are an orthonormal basis of C^2 (row form), so (e^dag X_r)^dag (e^dag X_r) +
(e^dag X_r')^dag (e^dag X_r') = I_2 / 5; summing over e gives G_r + G_r' = I_2 with G_r = X_r^dag X_r. Applied to the six
K4 edges: G_01 = G_10 = G_11 = I - G_00 and G_10 + G_11 = I, hence G_00 = I/2 and all G_r = I/2. So X_r = V_r / sqrt2 with
V_r an isometry and P_r = V_r V_r^dag a rank-2 projector with diagonal 2/5 in each of Z, X, T.

**Lemma 2 (antilinear couple maps).** For a couple (r, r') in basis b, e^dag X_r' = e^(i theta_e) * (row-orthogonal of
e^dag X_r), i.e. X_r' = D_b K_b X_r J with K_b complex conjugation in basis b, D_b a unitary diagonal in b and
J = [[0,1],[-1,0]]. Composing two couple maps of different bases gives LINEAR relations, e.g.
X_11 = -D'_Z (K_Z D_X K_Z) (K_Z K_X) X_00 with K_Z K_X = Pi the parity operator t -> -t; going round a K4 triangle gives
X_00 = A X_00 J for an antiunitary A, hence A^2 X_00 = -X_00: the column space of X_00 lies in the (-1)-eigenspace of
the unitary A^2 (a Kramers-type pairing). This is the general structure a later exact or numerical treatment must use.

**Proposition 3 (sub-case excluded).** There is no solution in which, for every r, the columns of X_r are (phase
multiples of) two eigenvectors of one complementary Weyl-Heisenberg operator X Z^k (k in {1,2,3}), with a common
column frame (X_r = [e^(i alpha_r) psi^k_m, e^(i beta_r) psi^k_m'] / sqrt2 up to one common right unitary).
Proof: in each basis b in {Z, X, T}, <e|psi^k_m> = g_(k,b) zeta^(Q(e,m)) / sqrt5 with Q quadratic over Z_5 and g a
unimodular constant independent of m, so rho_r(e) = u_r(e) / w_r(e) = e^(i gamma_r) zeta^(L_r(e)) with L_r affine in e.
Orthogonality of the rows of a couple with all four moduli 1/sqrt5 is rho_r(e) = -rho_r'(e) for all e in b, which forces
e^(i(gamma_r - gamma_r')) = -zeta^(c) for some c in Z_5. Multiplying around the triangle 00-01 (Z), 01-10 (T), 10-00 (X)
gives 1 = (-1)^3 zeta^(c'), i.e. zeta^(c') = -1, impossible for a fifth root of unity. (The same K4-triangle parity
as in R11.)

**Status.** The general W8 case (individual column frames W_r, non-MUB-span projectors) is not decided; Lemma 2 gives
its structure. A native LM test still needs a separate parent GO.
