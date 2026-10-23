# W8 written slice v1: exact ONB and ray-distinctness equations of the WH_5 (x) C^2 orbit ansatz; unconditional exclusion of MUB-pair representatives; exact remaining system

Recorded after actual `/bin/date`: 2026-10-19T16:47:26-0700 (written in the following minutes). Author ContinueRQLS10b.
Lane-internal, single author, UNREVIEWED, not parent-accepted, not Lean-checked. Restricted ansatz (H) only: nothing here
concerns arbitrary 1-RQLS(10), whose maximal case stays OPEN / UNKNOWN. No novelty or priority claim (Lemma 10 may be
known in the MUB literature). Scope frozen before derivation: 00-scope-freeze-v1.md
(79394cc6f23c81058a1b51d650b9dfd01729449ff023db380180424e20bd7c12).

## 0. Outcome
Outcome class: **UNRESOLVED** (no witness, no ansatz-wide no-go). Proved below with complete written proofs (imports in
section 10): the exact reduction of all 30 ONB conditions (Theorem 1), the Gram lemma (Lemma 2), the complete
ray-distinctness structure with 120 inequations (Theorem 3), an equivalent system in one flat plane and three
antiunitary couple maps (Theorems 4-5), a triangle Kramers condition excluding Weyl-Heisenberg-type couple maps
(Theorem 6, Lemma 7, Corollary 8), and a new import-free lemma: the vectors unbiased to Z, X and T are exactly the 15
vectors of the three complementary WH bases (Lemma 10). Consequence (Corollary 14): **in every solution of (H), of any
cardinality, no representative plane is a MUB-pair plane** - unconditional; the lane's earlier Proposition B needed
Haagerup's order-5 classification, which is no longer used. Section 9 states the exact remaining system.

## 1. Notation and hypotheses
zeta = e^(2 pi i/5); e_t (t in Z_5) the standard basis of C^5; X e_t = e_(t+1), Z e_t = zeta^t e_t, so ZX = zeta XZ and
Z^c X^a = zeta^(ac) X^a Z^c. For w = (a, c) in Z_5^2 put W_w := X^a Z^c. conj(.) is complex conjugation (entrywise in the
standard basis), M^* the adjoint, <x, y> is antilinear in x. For v in C^5 and Y in C^(5x2), v^* Y in C^(1x2) is the
"v-row" of Y.
Bases: beta_Z = (e_t); beta_X = (f_m), f_m := 5^(-1/2) sum_t zeta^(mt) e_t; beta_T = (g_m), g_m := 5^(-1/2) sum_t
zeta^(2t^2 + mt) e_t. More generally psi^k_m := 5^(-1/2) sum_t zeta^(3k t^2 + m t) e_t (k, m in Z_5), so psi^0 = f and
psi^4 = g (3 * 4 = 12 = 2 mod 5). One checks: X f_m = zeta^(-m) f_m; (X Z^k) psi^k_m = zeta^(2k - m) psi^k_m (so psi^k is
the eigenbasis of X Z^k, with distinct eigenvalues; k = 4 gives X Z^(-1) g_m = zeta^(3 - m) g_m); Z^d psi^k_m = psi^k_(m+d).
Lines: L_Z = {(0, c)}, L_X = {(a, 0)}, L_T = {(a, -a)}; for w in L_b, W_w is diagonal in beta_b. The complementary bases
are psi^1, psi^2, psi^3; a **MUB-pair plane** is span(psi^k_m, psi^k_m') with k in {1, 2, 3}, m != m'.
Couples: M_Z = {{00, 01}, {10, 11}}, M_X = {{00, 10}, {01, 11}}, M_T = {{00, 11}, {01, 10}} (the three perfect
matchings of K4 on {00, 01, 10, 11}); every pair {r, s} (r != s) lies in exactly one M_b, written b(r, s).

**(H)** Rows i = (i1, i2), columns j = (j1, j2) and symbols in Z_5 x Z_2, B(i, j) = i + j. The cell (i, j) carries
q_ij := (X^(i1) Z^(j1) (x) I_2) x_(i2 j2), where x_r in C^5 (x) C^2 is identified with the 5 x 2 matrix X_r via
x = sum X_(tc) e_t (x) eps_c; then (W (x) I) x <-> W X and <x, y> = tr(X^* Y). (H) demands that every row
{q_ij : j}, every column {q_ij : i} and every B-class {q_ij : i + j = s} ("transversal") is an orthonormal basis of
C^10. Maximal cardinality = the 100 cell rays are pairwise distinct.

## 2. Theorem 1 (exact reduction of the 30 ONB conditions)
(H) holds iff for every b in {Z, X, T} and every v in beta_b:
  (R1) |v^* X_r|^2 = 1/5 for all four r;   (R2) (v^* X_r)(v^* X_s)^* = 0 for every couple {r, s} in M_b.
(120 real equations: 15 basis vectors x (4 norms + 2 complex orthogonalities).)

Proof. Rows. Row (i1, i2) consists of (X^(i1) Z^(j1) (x) I) x_(i2 c), j1 in Z_5, c in Z_2. Applying the unitary
X^(-i1) (x) I, it is orthonormal iff tr(X_r^* Z^k X_s) = delta_(k,0) delta_(r,s) for all k in Z_5 and r, s in
{(i2,0), (i2,1)}. With Z^k = sum_t zeta^(kt) e_t e_t^* this trace is sum_t zeta^(kt) h(t), h(t) := (e_t^* X_s)(e_t^* X_r)^*.
By character orthogonality on Z_5 (h(t) = (1/5) sum_k zeta^(-kt) sum_t' zeta^(kt') h(t')) the condition holds iff
h(t) = delta_(r,s)/5 for all t, i.e. (R1) and (R2) in beta_Z for that couple. This does not depend on i1, so the ten
rows are equivalent to (R1), (R2) over beta_Z with couples M_Z.
Columns. X^i Z^j = zeta^(-ij) Z^j X^i, so column (j1, j2) consists of unimodular multiples of
(Z^(j1) X^(i1) (x) I) x_(i2 j2); after removing Z^(j1) it is orthonormal iff tr(X_r^* X^k X_s) = delta delta for
r, s in {(0, j2), (1, j2)}; with X^k = sum_m zeta^(-mk) f_m f_m^* the same inversion gives (R1), (R2) over beta_X with M_X.
Transversals. The class (s1, s2) consists of the cells i1 + j1 = s1, i2 + j2 = s2, i.e. of
(X^(i1) Z^(-i1) Z^(s1) (x) I) x_(i2, s2 - i2); X^i Z^(-i) = kappa_i (X Z^(-1))^i with |kappa_i| = 1 (reordering only uses
ZX = zeta XZ). Put G = X Z^(-1) and Y_r := Z^(s1) X_r: orthonormality iff tr(Y_r^* G^k Y_r') = delta delta for r, r' in
{(0, s2), (1, s2 - 1)}. With G^k = sum_m zeta^((3-m)k) g_m g_m^* and m -> 3 - m a bijection, inversion gives
(g_m^* Y_r')(g_m^* Y_r)^* = delta_(r,r')/5 for all m. Finally g_m^* Z^(s1) = (Z^(-s1) g_m)^* = g_(m - s1)^*, and m - s1
runs over Z_5: so for every s1 the condition is (R1), (R2) over beta_T for the couple {00, 11} (s2 = 0) or {01, 10}
(s2 = 1). Unit norms of cells follow from (R1) summed over beta_Z. Conversely (R1), (R2) give all 30 bases. QED

## 3. Lemma 2 (Gram lemma; re-proof of setup addendum 1, Lemma 1)
(R1), (R2) imply X_r^* X_r = I_2/2 for every r. Hence V_r := sqrt2 X_r is an isometry, P_r := V_r V_r^* is the orthogonal
projector onto the 2-dimensional S_r := range X_r, (R1) <=> v^* P_r v = 2/5 for all v in beta_Z u beta_X u beta_T
("S_r is a flat plane"), and (R2) <=> (v^* V_r)(v^* V_s)^* = 0.
Proof. For {r, s} in M_b and v in beta_b the 2 x 2 matrix sqrt5 [v^* X_r ; v^* X_s] has orthonormal rows, so it is
unitary and (v^* X_r)^*(v^* X_r) + (v^* X_s)^*(v^* X_s) = I/5. Summing over v in beta_b: G_r + G_s = I, G_r := X_r^* X_r.
This holds for all six pairs; for distinct r, s, t, G_r = I - G_s = G_t and G_r + G_t = I, so G_r = I/2. QED

## 4. Theorem 3 (ray distinctness and cardinality)
Assume (H). For r, s and w in Z_5^2 put tau_rs(w) := tr(X_r^* W_w X_s).
(a) For cells c = ((i1,i2),(j1,j2)) in orbit r = (i2, j2) and c' = ((i1',i2'),(j1',j2')) in orbit s = (i2', j2'),
    |<q_c, q_c'>| = |tau_rs(w)| with w = (i1' - i1, j1' - j1).
(b) The 25 rays of one orbit are pairwise distinct.
(c) For r != s: |tau_rs(w)| = 1 iff W_w X_s = mu X_r with |mu| = 1, and then the orbits r and s have the same 25 rays;
    otherwise they share no ray. Hence the number of distinct rays is 25 x (number of classes of the equivalence "same
    ray set" on the four representatives), i.e. one of 25, 50, 75, 100.
(d) Forced orthogonality: tau_rs(w) = 0 for every w in L_(b(r,s)) (5 values per pair, 30 in all).
(e) Maximal cardinality <=> |tau_rs(w)| < 1 for each of the 6 unordered pairs {r, s} and each of the 20 w outside
    L_(b(r,s)): **120 inequations** (|tau_sr(-w)| = |tau_rs(w)|, so ordered pairs add nothing).
Proof. (a) (X^(i1) Z^(j1))^* X^(i1') Z^(j1') = Z^(-j1) X^(i1'-i1) Z^(j1') = (unimodular) W_w, and <q_c, q_c'> =
tr(X_r^* (...) X_s). (b) By Lemma 2, ||X_r||_F = 1, so |tau_rr(w)| <= 1 with equality iff W_w X_r = mu X_r, i.e. both
columns of X_r (orthogonal, nonzero) are eigenvectors of W_w for one eigenvalue; for w != 0 every eigenspace of W_w is
one-dimensional (Lemma 9(ii)) - impossible. (c) Cauchy-Schwarz gives the equality case. If X_s = mu W_w^(-1) X_r then for
every w', W_(w') X_s = (unimodular) W_(w'-w) X_r, a bijection between the cell vectors of the two orbits up to phases. If
one ray is shared, (a) gives |tau| = 1 for some w and the whole ray sets agree; so "same ray set" is an equivalence whose
classes have disjoint ray sets. (d) For {r, s} in M_Z (same i2) the cells ((i1,i2),(j1,j2)), ((i1,i2),(j1',j2')) lie in
one row, w = (0, j1' - j1); for M_X (same j2) one column, w = (i1' - i1, 0); for M_T (i2 + j2 = i2' + j2') one class,
i1 + j1 = i1' + j1', w = (a, -a). Distinct members of an orthonormal basis are orthogonal. (e) follows from (c), (d). QED
In terms of the isometries: |tau_rs(w)| = 1 iff V_r = mu W_w V_s (frames included), which in particular needs
S_r = W_w S_s.

## 5. Antiunitary couple maps and an equivalent system
For b in {Z, X, T} let K_b be the antiunitary with K_b(sum_v c_v v) = sum_v conj(c_v) v (sum over v in beta_b), and
Anti_b := {D K_b : D unitary and diagonal in beta_b}. Let J := [[0, 1], [-1, 0]] (real, J^2 = -I). For an antiunitary R
and Y in C^(5x2), RY is taken columnwise; since J is real, R(YJ) = (RY)J.
Facts. (i) Every A = D K_b in Anti_b is an antiunitary involution: K_b D K_b = sum_v conj(lambda_v) v v^* if
D = sum_v lambda_v v v^*, so A^2 = I. (ii) v^*(AY) = lambda_v conj(v^* Y) for v in beta_b: <v, D K_b y> =
lambda_v <v, K_b y> = lambda_v conj(<v, y>). (iii) Row complement: for a nonzero row rho in C^(1x2), the rows sigma with
|sigma| = |rho| and rho sigma^* = 0 are exactly sigma = lambda conj(rho) J, |lambda| = 1 (conj(rho) J = (-conj(rho_2),
conj(rho_1)); the orthogonal complement of rho is one-dimensional). (iv) For antiunitary involutions R, R' and an
isometry V with P = V V^*: (RV)(R'V)^* = R P R' (a linear operator). Indeed (RV)(R'V)^* y = sum_k R v_k <R' v_k, y> and
<R' v_k, y> = conj(<v_k, R' y>), so the sum is R(sum_k v_k <v_k, R' y>) = R P R' y.
Coordinates. K_Z = K (K y = conj(y)); K_X y = Pi conj(y) with Pi e_t = e_(-t) (because sum_m f_m f_m^T = Pi); K_T y =
Q^2 Pi conj(y) with Q := diag(zeta^(2t^2)) (because (sum_m g_m g_m^T)_(t,t') = zeta^(4t^2) delta_(t',-t)). The unitaries
diagonal in beta_X are the circulant unitaries; those diagonal in beta_T are Q C Q^* with C circulant (g_m = Q f_m).
Hence A in Anti_Z: A y = D conj(y) (D diagonal unitary); B in Anti_X: B y = C_X Pi conj(y); C in Anti_T:
C y = Q C_T Q Pi conj(y) (C_X, C_T circulant unitaries).

**Theorem 4 (couple maps; re-proof and sharpening of setup addendum 1, Lemma 2).** Assume (R1), (R2) and put
V_r = sqrt2 X_r. For every couple {r, s} in M_b there is a unique A_(r->s) in Anti_b with V_s = A_(r->s) V_r J; and
A_(s->r) = -A_(r->s). Conversely, if V_r is an isometry whose range is flat in beta_b and A is in Anti_b, then
V_s := A V_r J is an isometry and the beta_b-rows of V_r and V_s are orthogonal of equal norm.
Proof. For v in beta_b the rows v^* V_r, v^* V_s have norm^2 2/5 and are orthogonal, so by (iii) v^* V_s =
lambda_v conj(v^* V_r) J with a unique unimodular lambda_v; with D := sum lambda_v v v^* and (ii), v^*(D K_b V_r J) =
v^* V_s for all v, so V_s = D K_b V_r J. Applying the involution A := D K_b gives A V_s = V_r J, so
V_r = -A V_s J. Converse: (A V_r)^*(A V_r) has entries <A v_i, A v_j> = conj(delta_ij), so V_s^* V_s = J^* J = I; the rows
follow from (ii) and (iii). QED

**Theorem 5 (equivalent system).** (H) has a solution iff there exist a flat plane with projector P and
A in Anti_Z, B in Anti_X, C in Anti_T such that
  (F) APA is flat in beta_X and beta_T; BPB is flat in beta_Z and beta_T; CPC is flat in beta_Z and beta_X;
  (O) e^* B P C e = 0 (e in beta_Z),  f^* A P C f = 0 (f in beta_X),  g^* A P B g = 0 (g in beta_T).
Every solution is X_00 = V/sqrt2, X_01 = A V J/sqrt2, X_10 = B V J/sqrt2, X_11 = C V J/sqrt2 with V V^* = P, and every
such quadruple (any isometry V with V V^* = P) is a solution. In coordinates (conj(P) entrywise):
  APA = D conj(P) D^*,  BPB = C_X Pi conj(P) Pi C_X^*,  CPC = Q C_T Q (Pi conj(P) Pi) Q^* C_T^* Q^*,
  APB = D conj(P) conj(C_X) Pi,  APC = D conj(P) Q^* conj(C_T) Q^* Pi,  BPC = C_X Pi conj(P) Q^* conj(C_T) Q^* Pi.
Proof. (=>) Put V := V_00 and A := A_(00->01), B := A_(00->10), C := A_(00->11) (Theorem 4). By (iv) the projector of
range(V_01) = range(AVJ) is (AV)(AV)^* = APA, so (R1) for X_01 is flatness of APA (beta_Z is automatic, see below); the
same for X_10, X_11. The three remaining couples are {10,11} in M_Z, {01,11} in M_X, {01,10} in M_T, and (by (iv), J
unitary) their row products are e^*(BV)(CV)^* e = e^* BPC e, f^* APC f, g^* APB g. (<=) The X_r are isometries over
sqrt2 (Theorem 4, converse); P is flat; APA is flat in beta_Z automatically, because for e in beta_Z with A e = lambda_e e
one has e^* APA e = conj(<A e, P A e>) = <e, P e> (A an antiunitary involution: <x, A y> = conj(<A x, y>)); likewise BPB in
beta_X and CPC in beta_T; together with (F) all four planes are flat. Couples containing 00 hold by Theorem 4, the other
three by (O); Theorem 1 gives (H). The coordinate forms follow from the explicit A, B, C, conj(Q) = Q^*, Pi Q Pi = Q and
conj(C) = Pi C^* Pi for circulant C. QED
Remarks. (1) The whole problem, including the 120 inequations of Theorem 3 (which are invariant under V -> V U,
U in U(2)), depends only on (P; A, B, C). (2) Unknowns given P: the 15 phases of D, C_X, C_T, of which one per map is
inessential; equations: (F) 24 real, (O) 30 real. (3) Each of AS, BS, CS is again a flat plane, so the four planes lie in
the (finite or not) set of flat planes and are related by maps of Anti_Z, Anti_X, Anti_T.

## 6. Triangles: a Kramers condition
**Theorem 6.** Assume (H). For every triangle r -> s -> t -> r of K4 (its three edges lie in three different M_b), the
antiunitary Theta := A_(t->r) A_(s->t) A_(r->s) satisfies Theta V_r = V_r J; hence Theta^2 = -I on S_r.
Proof. V_t = A_(s->t) A_(r->s) V_r J^2 and V_r = A_(t->r) V_t J = -Theta V_r J (J^3 = -J). Multiplying by J^(-1) = -J on
the right gives Theta V_r = V_r J, and Theta^2 V_r = Theta(V_r J) = (Theta V_r) J = V_r J^2 = -V_r. QED

**Lemma 7 (Kramers parity).** Let Theta be antiunitary on C^n. Then Theta^2 is unitary and commutes with Theta;
Theta maps the lambda-eigenspace of Theta^2 onto the conj(lambda)-eigenspace; the (-1)-eigenspace E_(-1) is
Theta-invariant and has even dimension; and if n is odd, +1 is an eigenvalue of Theta^2.
Proof. Theta^2 (Theta y) = Theta(Theta^2 y) = Theta(lambda y) = conj(lambda) Theta y. On E_(-1), Theta is antiunitary
with Theta^2 = -1; for y != 0, <y, Theta y> = <Theta(Theta y), Theta y> = <-y, Theta y> forces <y, Theta y> = 0, so
span{y, Theta y} is a Theta-invariant plane whose orthogonal complement in E_(-1) is again Theta-invariant: induction.
The non-real eigenvalues pair off with equal multiplicities, so dim E_(+1) = n mod 2. QED
Consequence. In C^5, for every triangle through r: S_r lies in E_(-1)(Theta^2), whose dimension is 2 or 4.

**Corollary 8 (Weyl-Heisenberg-type couple maps excluded).** Call A = D K_b in Anti_b of WH type if D = mu W_w with
|mu| = 1 and w in L_b. In a solution of (H), no triangle of K4 has all three couple maps of WH type (scalar maps D = mu I
included).
Proof. Write the three maps as R_i = mu_i W_i N_i K with W_i Weyl-Heisenberg (up to phase) and
N_i in {I, Pi, Q^2 Pi} (types Z, X, T; one of each). Then Theta = R_3 R_2 R_1 = M K with
M = (unimodular) W_3 N_3 conj(W_2) conj(N_2) W_1 N_1. Complex conjugation, Pi and Q^(+-2) normalise the WH group
(conj(X) = X, conj(Z) = Z^(-1); Pi X Pi = X^(-1), Pi Z Pi = Z^(-1); Q X Q^* = zeta^2 X Z^(-1), Q Z Q^* = Z), so
M = W Q^(2 eps) with W Weyl-Heisenberg up to phase and eps = +-1 (the N's contribute one factor Q^2 or conj(Q^2) =
Q^(-2) and two commuting factors Pi). Then Theta^2 = M conj(M) = W Q^(2 eps) conj(W) Q^(-2 eps), a product of WH
operators, i.e. Theta^2 = gamma W_(w0). If w0 != 0 all eigenspaces of Theta^2 are one-dimensional (Lemma 9(ii)); if
w0 = 0, Lemma 7 (n = 5 odd) forces gamma = 1 and E_(-1) = 0. Either way S_r cannot lie in E_(-1)(Theta^2),
contradicting Theorem 6. QED

## 7. Weyl-Heisenberg facts and the three-basis unbiased vectors
**Lemma 9.** (i) For a != 0 in Z_5 and any b: |sum_t zeta^(a t^2 + b t)| = sqrt5 and sum_t zeta^(a t^2 + b t) =
zeta^(-b^2/(4a)) sum_t zeta^(a t^2). (ii) For w != 0, W_w has five distinct eigenvalues. (iii) Any two of the six bases
psi^0 = beta_X, psi^1, psi^2, psi^3, psi^4 = beta_T, beta_Z are mutually unbiased; in particular MUB-pair planes are flat.
(iv) X^c psi^k_m = zeta^(3k c^2 - m c) psi^k_(m - kc); (X Z^(-1)) psi^k_m is a unimodular multiple of psi^k_(m - 1 - k);
Z^d psi^k_m = psi^k_(m+d). (v) For w not in L_b, W_w maps beta_b to itself up to phases by a fixed-point-free cyclic
permutation; for w in L_b it is diagonal in beta_b.
Proof. (i) |S|^2 = sum_(s,h) zeta^(a(2sh + h^2) + bh) (t = s + h) = sum_h zeta^(a h^2 + b h) sum_s zeta^(2ahs) = 5; and
a t^2 + b t = a(t + b/(2a))^2 - b^2/(4a) with t -> t + b/(2a) bijective. (ii) Choose w' with symplectic product
s = a c' - c a' != 0; W_w W_(w') = zeta^(s') W_(w') W_w with s' != 0, so W_(w') shifts eigenvalues by zeta^(s') and all five
values occur. (iii) <psi^k_m, psi^k'_m'> = (1/5) sum_t zeta^(3(k'-k)t^2 + (m'-m)t) has modulus 1/sqrt5 for k != k' by (i);
|<e_t, psi^k_m>| = 1/sqrt5. (iv) Direct substitution (6 = 1 mod 5). (v) beta_b is the eigenbasis of W_(w_b) (w_b
spanning L_b) with distinct eigenvalues; if w is not in L_b, W_(w_b) W_w = zeta^s W_w W_(w_b) with s != 0, so W_w sends
the lambda-eigenvector to the zeta^s lambda-eigenvector. QED

**Lemma 10 (vectors unbiased to Z, X, T; no import).** Let u be a unit vector with |<e_t, u>|^2 = 1/5 for all t, and
eps_t := sqrt5 <e_t, u>. If the lag-one autocorrelations sum_t eps_(t+1) conj(eps_t) and
sum_t zeta^t eps_(t+1) conj(eps_t) both vanish, then u = theta psi^k_m with |theta| = 1, k in {1, 2, 3}, m in Z_5.
In particular, the unit vectors unbiased to beta_Z, beta_X and beta_T are exactly the unimodular multiples of the 15
vectors psi^k_m, k in {1, 2, 3}.
Proof. Unbiasedness to beta_X: <f_m, u> = (1/5) sum_t zeta^(-mt) eps_t, and |sum_t zeta^(-mt) eps_t|^2 =
sum_k zeta^(-mk) R(k), R(k) := sum_s eps_(s+k) conj(eps_s); this is 5 for all m iff R(k) = 0 for k != 0, so R(1) = 0.
Unbiasedness to beta_T: <g_m, u> = (1/5) sum_t zeta^(-mt) eta_t with eta_t := zeta^(-2t^2) eps_t, so likewise
0 = R_eta(1) = sum_s zeta^(-2(s+1)^2 + 2s^2) eps_(s+1) conj(eps_s) = zeta^(-2) sum_s zeta^(s) eps_(s+1) conj(eps_s)
(zeta^(-4s) = zeta^s). So the hypotheses hold for every vector unbiased to the three bases.
Main step. u_t := eps_(t+1) conj(eps_t) is unimodular. Write u_t = sum_f c_f zeta^(ft). The hypotheses say c_0 = 0 and
c_4 = (1/5) sum_t zeta^t u_t = 0, so u_t = c_1 zeta^t + c_2 zeta^(2t) + c_3 zeta^(3t). Expanding |u_t|^2 = 1 and using the
linear independence of the five characters: the coefficient of zeta^(-2t) gives c_1 conj(c_3) = 0 and that of zeta^(-t)
gives c_1 conj(c_2) + c_2 conj(c_3) = 0. If c_1 = 0 then c_2 conj(c_3) = 0; if c_3 = 0 then c_1 conj(c_2) = 0. Hence
exactly one c_f is nonzero: u_t = gamma zeta^(ft), |gamma| = 1, f in {1, 2, 3}. Iterating eps_(t+1) = u_t eps_t:
eps_t = eps_0 gamma^t zeta^(f t(t-1)/2) for t = 0, ..., 5, and eps_5 = eps_0 gives gamma^5 = 1, gamma = zeta^g. For
integers t, t(t-1)/2 = 3t(t-1) mod 5, so eps_t = eps_0 zeta^(3f t^2 + (g - 3f) t), i.e. u = eps_0 psi^f_(g - 3f).
The converse is Lemma 9(iii). QED

**Corollary 11.** (a) A flat plane containing a unit vector unbiased to beta_Z, beta_X and beta_T is a MUB-pair plane.
(b) If S = span(u, W_w u) is a flat plane with w != 0 and u a unit vector orthogonal to W_w u, then S is a MUB-pair plane.
Proof. (a) By Lemma 10, S = span(psi^k_m, y) with y a unit vector orthogonal to psi^k_m; flatness gives
|<v, y>|^2 = 2/5 - 1/5 for all v in the three bases, so y = theta' psi^k'_m' (Lemma 10), and orthogonality forces k' = k
(Lemma 9(iii)), m' != m. (b) For b in {Z, X, T} put H(v) := |<v, u>|^2 (v in beta_b), so v^* P v = H(v) + |<W_w^* v, u>|^2.
If w is in L_b, the second term equals H(v) and flatness gives H = 1/5. Otherwise (Lemma 9(v)) W_w^* permutes beta_b up to
phases by a fixed-point-free cyclic permutation sigma, so H(v) + H(sigma v) = 2/5, H(sigma^2 v) = H(v), and sigma^2 is
transitive on the 5 vectors (5 prime): H = 1/5. So u is unbiased to all three bases, u = theta psi^k_m, and W_w u is a
unimodular multiple of psi^k_m' (WH operators permute each basis psi^k up to phases), m' != m. QED

## 8. MUB-pair planes cannot occur
**Proposition 12 (no import).** Assume (H). If S_r is a MUB-pair plane and {r, s} is a couple, then S_s is a MUB-pair plane.
Proof. Let b = b(r, s) and A_(r->s) = D K_b (Theorem 4), so S_s = D K_b S_r. By direct substitution, K_Z psi^k_m =
psi^(-k)_(-m); K_X psi^k_m = Pi conj(psi^k_m) = psi^(-k)_m; K_T psi^k_m = Q^2 Pi conj(psi^k_m) = psi^(3-k)_m
(3(3 - k) = 4 - 3k mod 5). Thus K_b S_r = span(psi^kappa_n, psi^kappa_n') with n != n' and kappa = -k (b = Z, X) or
3 - k (b = T); note kappa != 0 if b = X and kappa != 4 if b = T. Let Y_b := Z^c (b = Z), X^c (b = X), (X Z^(-1))^c
(b = T); Y_b commutes with D (both diagonal in beta_b), and by Lemma 9(iv) Y_b sends psi^kappa_n to a unimodular
multiple of psi^kappa_(n + delta) with delta = c, -kappa c, -(1 + kappa) c respectively; the coefficient is nonzero mod 5,
so c (!= 0) can be chosen with n + delta = n'. Then S_s = span(u, Y_b u) with u := D psi^kappa_n a unit vector orthogonal
to Y_b u. S_s is flat (Lemma 2), so by Corollary 11(b) it is a MUB-pair plane. QED

**Theorem 13 (lane Theorem A, re-proved here).** Assume (H). No three representative planes are MUB-pair planes.
Proof. Let S_r = span(psi^k_m, psi^k_m') (k = k_r in {1,2,3}, m != m') and Phi_r := [psi^k_m, psi^k_m']; then
U_r := Phi_r^* V_r is unitary and V_r = Phi_r U_r. Step 1: for b in {Z, X, T} index beta_b as v_n (e_n, f_n, g_n). Then
v_n^* Phi_r = p_r(n) (1, rho_r(n)) with p_r(n) = <v_n, psi^k_m> != 0 and rho_r(n) = zeta^(a_r n + h_r), a_r != 0 and
h_r in Z_5. For b = Z, rho = zeta^((m'-m)n). For b = X, <f_n, psi^k_j> = (1/5) sum_t zeta^(3k t^2 + (j - n)t) =
(1/5) zeta^(-(j-n)^2/(12k)) G(3k) (Lemma 9(i)), so rho = zeta^(((m-n)^2 - (m'-n)^2)/(12k)) with n-coefficient
(m'-m)/(6k) != 0. For b = T, the same with 3k - 2 (!= 0 for k in {1,2,3}) in place of 3k: n-coefficient
(m'-m)/(2(3k-2)) != 0. Step 2: for a couple {r, s} in M_b with both planes MUB-pair, (R2) reads
f(n) := w11 + w12 conj(rho_s(n)) + w21 rho_r(n) + w22 rho_r(n) conj(rho_s(n)) = 0 for all n, with
[[w11, w12], [w21, w22]] := U_r U_s^*. The frequencies (in n) are 0, -a_s, a_r, a_r - a_s. If a_r is not +-a_s they are
distinct and U_r U_s^* = 0, impossible. If a_r = a_s, then w12 = w21 = 0 and w22/w11 = -zeta^(h_s - h_r); if a_r = -a_s
(then 0, a_r, 2a_r are distinct), w11 = w22 = 0 and w21/w12 = -zeta^(-h_r - h_s). So U_r U_s^* is monomial with ratio
(lower/upper nonzero entry) in -mu_5. Step 3: for a triangle r1 r2 r3, (U_1 U_2^*)(U_2 U_3^*)(U_3 U_1^*) = I. For monomial
2 x 2 matrices, diag(x,y) diag(x',y') has ratio rho rho', antidiag(x,y) antidiag(x',y') is diagonal with ratio rho/rho',
and mixed products are antidiagonal; so the product is diagonal only with zero or two antidiagonal factors, and its ratio
is then in (-1)^3 mu_5 (each step multiplies or divides by an element of -mu_5). I has ratio 1, and -1 is not a fifth
root of unity. QED

**Corollary 14 (unconditional).** In every solution of (H), of any cardinality: no representative plane is a MUB-pair
plane; no representative plane contains a vector unbiased to beta_Z, beta_X and beta_T; and no representative plane has
the form span(u, W_w u) with w != 0.
Proof. If S_r were MUB-pair, the three other representatives are couple partners of r (K4), hence MUB-pair by
Proposition 12, contradicting Theorem 13. The other two statements follow by Corollary 11. QED
This removes the import [I-H] from the lane's Proposition B (evidence/w8-decision-v1.md, section 4) and settles closure
item (E4) of evidence/w8-decision-v1-addendum-1.md; it is a statement inside (H) only.

## 9. Attempts and the exact remaining system
Witness attempt. Every exactly describable candidate available in writing was examined: planes spanned by WH or
complementary-basis vectors (excluded by Corollary 14), and couple maps of Weyl-Heisenberg or scalar type (excluded in
every triangle by Corollary 8). Any solution therefore needs four flat planes that contain no complementary stabiliser
vector, together with couple maps not all of WH type in any triangle. No exact description of such planes is available
in writing, and the cited float evidence (not a premise: 100 non-MUB-pair flat planes found, no compatible K4 pattern;
parent-audited LM 0/512, RUN/review/rqls10-w8-lm-parent-audit-v1.json 444fe891...40fc) gives no candidate. No witness is
claimed.
No-go attempt. Closed in writing: MUB-pair planes (all of them, Corollary 14); WH-generated planes; WH-type couple-map
triangles. Not closed: the non-MUB-pair flat planes.
**Exact remaining system (equivalent to (H) by Theorem 5 and Corollary 14).** Unknowns: a Hermitian 5 x 5 matrix P, a
diagonal unitary D and circulant unitaries C_X, C_T. Equations:
  (P1) P^2 = P, tr P = 2, v^* P v = 2/5 for all v in beta_Z u beta_X u beta_T; P is not one of the 30 MUB-pair projectors
       (equivalently, P dominates no projector psi psi^* with psi in a complementary basis);
  (P2) the six image-flatness conditions (F) with APA = D conj(P) D^*, BPB = C_X Pi conj(P) Pi C_X^*,
       CPC = Q C_T Q (Pi conj(P) Pi) Q^* C_T^* Q^*;
  (P3) the three cross conditions (O): diag_Z(C_X Pi conj(P) Q^* conj(C_T) Q^* Pi) = 0,
       diag_X(D conj(P) Q^* conj(C_T) Q^* Pi) = 0, diag_T(D conj(P) conj(C_X) Pi) = 0;
  maximal cardinality additionally: (P4) the 120 inequations of Theorem 3(e) for X_00 = V/sqrt2, X_01 = A V J/sqrt2,
       X_10 = B V J/sqrt2, X_11 = C V J/sqrt2 (any V with V V^* = P), e.g. |tr(V^* W_w A V J)| < 2 for w not in L_Z.
Necessary conditions usable inside this system: Theorem 6 / Lemma 7 for each of the four triangles (S_r in an even-
dimensional E_(-1)(Theta^2)), Corollary 8, and Corollary 14 for all four planes AS, BS, CS, S.
What would close W8 exactly: (C1) an exact classification of the flat planes satisfying (P1) (float evidence suggests
100 planes in 4 WH-translation orbits, each invariant under a conjugate of an order-3 Clifford unitary - unproved);
(C2) for each, the exact solution sets of the compatibility equations in (P2); (C3) the K4 conditions (P3). (C1)-(C3) are
the lane's items (E1)-(E3); (E4) is now closed.

## 10. Imports, dependencies, non-claims
Imports: (I1) character orthogonality / DFT inversion on Z_5; (I2) elementary linear algebra (Cauchy-Schwarz for the
Frobenius inner product, spectral theorem for unitaries, algebra of antiunitary operators: <R a, R b> = conj(<a, b>)).
Gauss sums are proved inline (Lemma 9(i)); no Haagerup classification, no Chebotarev theorem, no computation of any kind.
Lane dependencies: none as premises. Re-proved here: setup reduction (Theorem 1), addendum-1 Lemma 1 (Lemma 2),
addendum-1 Lemma 2 (Theorem 4), decision-note Theorem A (Theorem 13). Superseded: decision-note Proposition B's import.
Context only: decision-note Lemmas 2-4 and the explicit flat-plane coefficient system; addendum Lemma 5; all float probes.
Non-claims: no witness; no ansatz-wide no-go; no statement about any other ansatz or about unrestricted 1-RQLS(10); the
maximal 1-RQLS(10) target remains OPEN / UNKNOWN.
