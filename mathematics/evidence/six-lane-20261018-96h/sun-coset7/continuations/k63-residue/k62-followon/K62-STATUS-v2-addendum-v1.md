# K62-STATUS-v2-addendum-v1: the 6-point model at an unmarked O-vertex, and P_ob at c1 (VFC side)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T04:35:37-0700.
- **Supplements** `K62-STATUS-v2.md` (sha256 696a627f14453655578d9444bdbf0bb20ce59ec1da09bff08d11fb0f695da7fd), frozen.
  Author Sun63Successor; no computation; CANDIDATE/navigation.

## 1. Lemma P6 (6-point model) [NEW, candidate]
Let v in O with n_v = 6 w_v, and suppose gcd(n_v, [G : W_Q]) divides 6 for every Q contained in V minus {v}
(W_Q = intersection of U_j, j in Q). This holds in the e_d >= 4 residue when no 3-marker lies in O, by the chain of
Lemma FG-62 (`K62-FG-v1.md` section 3: order d, i*, p, rest; every k <= 3). Normalise g_v = 1, X_j = U_vU_j.
Then **every Boolean atom of the family (X_j) has measure in (1/6)Z.**
*Proof.* The intersection of the X_j (j in Q) is left U_v-invariant and right W_Q-invariant, hence a union of
(U_v, W_Q)-double cosets, each of measure [G : U_v cap x W_Q x^-1] / (n_v [G : W_Q]), a multiple of
1/gcd(n_v, [G : W_Q]) by L0.1 and Lagrange. Atoms are integer combinations of such intersections (inclusion-
exclusion). QED
So, at such v, G behaves like six points of mass 1/6; X_j is a set of 6 mu(X_j) points (alpha_vj for C-vertices,
3 for d), all X_j share the point p0 containing U_v, and every tight edge vj has D_j = Y_j as point sets. The same
holds for the conjugate family when its chain hypothesis holds.

## 2. P_ob at c1, VFC side: a consistent 6-point model
At c1 every edge of P_ob is tight. Forced containments (F7, apex c1, alpha-family): X_c3 in X_c5, X_c4 in X_c2,
X_c3 in X_(i*), X_c5 = X_(i*). K2 forbids X_d in X_c (c in O), X_c3 in X_c2 and X_c4 in X_c5. With points
p0, a, b, c, e, f:
  Y_c5 = Y_(i*) = {a, b}, Y_c2 = {c, e}, Y_c3 = {a, b, c, f}, Y_c4 = {b, c, e, f}, Y_d = {a, c, f}.
The alpha*-label types at c1 are c2: 2, c3: 4, c4: 4, c5: 2, i*: 4, d: >= 8, and the point sets
S(a) = {c3, c5, i*, d}, S(b) = {c3, c4, c5, i*}, S(c) = {c2, c3, c4, d}, S(e) = {c2, c4}, S(f) = {c3, c4, d},
S(p0) = empty are all allowed; the union of the Y's has measure 5/6 (the bound of Corollary 5/6-62); every forced
containment holds; no K2-forbidden containment holds; every pair intersection of X's satisfies the L4 lower bound
tau_min / (gamma alpha) and the inclusion-exclusion bound (checked pair by pair: the equalities are
X_c2 cap X_c5 = X_c2 cap X_(i*) = 2/6 against lower bound 2/6, and the 1/6 intersections against lower bound 1/6).
**Scope:** this shows that the VFC-side single-vertex system at c1 (tightness, F7, K2, L4 pair bounds, (V3), the 5/6
bound and the 1/6 grid) does not exclude P_ob. The LFC side at c1, the other O-vertices, i* and d were not checked in
this form; no claim is made about them.

## 3. Consequence for the frontier (navigation)
The e_d >= 4 residue is not closed by any single-vertex test examined here. Old exploratory K62 probes evaluated
e_d = 3 items only (now covered by K62-E3); no exploratory evidence exists for e_d >= 4. A closure needs
multi-vertex coupling (for example through the common values tau of triangles, which enter the 6-point models of
all three apexes) or genuinely group-theoretic input.
