# Residue working notes v7 (Sun7K62Successor) - navigation only, NOT a candidate

- **Written:** `/bin/date` immediately before this exclusive write: 2026-10-19T07:32:14-0700. Unchecked scratch; no computation.

## New lever: equality structures give index-3 subgroups (sketch)
At an apex a in W of C, if the VFC count is FG-tight with D_j = D_k and both equal their Y-sets (mu(D_j) + mu(X_j) = 1),
then X_j = X_k, i.e. U_aU_j = U_aU_k =: X. X is right-invariant under H := <U_j, U_k>, contains 1, so H subset X; if
mu(U_jU_k) = mu(X) then H = X = U_jU_k is a subgroup of index 6/x_jk (here 3) containing U_a, U_j, U_k, and the three
cosets g_aU_a, g_jU_j, g_kU_k lie in three distinct left H-cosets (disjointness <=> g^-1 g' not in UU' = H).

**LFC inside an H-coset.** If H (index 3) contains U_a, the fibres at a inside g_aH number n_a/3; a coset g_jU_j meets
m_j := [U_j : U_j cap H] left H-cosets and, by homogeneity, t_j/m_j fibres in each. Hence for feasible y over the j
meeting g_aH: sum_j y_j x_aj / (2 m_j) <= 1 - 3/n_a < 1. In particular a single j meeting g_aH with x_aj / (2 m_j) >= 1
(e.g. x_aj = 4, m_j = 2) is impossible.

## Case B (Q_B'-family), C^alpha*
- Apex a1 (masses = a1's alpha-row: a2, a3 4; v1, v2, t 2; z 3; note t is a two and {z, t, s} is allowed since
  gcd(z,t) = 6): the count still forces union = 5/6, D*_a2 = D*_a3 = cosets meeting a2 or a3 (4/6).
- Both D*'s equal their Y-sets, so U*_a1U*_a2 = U*_a1U*_a3; with mu(U*_a2U*_a3) = alpha*_a2a3/6 = 1/3 this gives an
  index-3 subgroup H = U*_aU*_a' (all pairs) containing U*_a1, U*_a2, U*_a3; the three a-cosets occupy the three H-cosets.
- m_v, m_t >= 2 (mu(U*_aU*_v) = mu(U*_aU*_t) = 4/6); the inside-H LFC kills m = 2 (4/(2*2) = 1), so m_v1 = m_v2 = m_t = 3.
- If alpha*_tv1 = alpha*_tv2 = 2, apex v1 (2F3S with fours v2, t) gives a second index-3 subgroup K' = U*_v2U*_t
  containing U*_v1, U*_v2, U*_t, K' != H, and m'_a = 3 for all a. No contradiction yet.

## K_{2,3} family (Case A), C^alpha
Apex v1 (masses v2 4, t 4, twos x, y, w): D_v2 = D_t; if alpha_tv1 = alpha_tv2 = 2 this gives an index-3 subgroup
K = U_v2U_t containing U_v1, U_v2, U_t (cosets in distinct K-cosets). To explore with the inside-K count.
