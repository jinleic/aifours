# Residue working notes v8 (Sun7K62Successor) - navigation only, NOT a candidate

- **Written:** `/bin/date` immediately before this exclusive write: 2026-10-19T07:35:16-0700. Unchecked scratch; no computation.

## Cell argument (sketch)
Two index-3 subgroups K != L with HK-type covering: if K contains U_j for three vertices j whose cosets occupy the three
K-cosets, L likewise for three other vertices, m^K_i = 3 for the L-vertices and m^L_j = 3 for the K-vertices (inside-K /
inside-L LFC counts with entry 4 kill m = 2), then KL = G, [G : K cap L] = 9, and each of the 9 cells (K-coset cap
L-coset, a coset of K cap L) holds one K-vertex piece (index n_j/3 = 2 r_j in K cap L) and one L-vertex piece
(2 w_i). A third piece of a vertex z has index N_z with prime factors in {2,3} cup primes(w_z)
([U_z : U_z cap K cap L] = m^K_z * (<= 3)), so a triple whose pairwise gcds are all <= 2 violates Sun(3).

## K_{2,3} family: sub-case alpha_tv1 = alpha_tv2 = 2 is DEAD (sketch)
K := U_v2U_t (index 3; from apex v1 in C^alpha: D_v2 = D_t, both equal their Y-sets); L := U_yU_w (index 3; from apex x
in C^alpha with alpha*_tx = 2, which holds for at least two 3-side x by LFC at t in C^alpha*: at most one 3-side
alpha*_t = 1). Cells: z cannot meet a cell of g_v1K or g_v2K (triple v, x, z all gcd <= 2), so g_zU_z lies in g_tK,
U_z subset K and mu(U_zU_v1) <= 1/3, contradicting alpha_zv1 = 3.

## Case B (Q_B'-family): sub-case alpha*_tv1 = alpha*_tv2 = 2 is DEAD (sketch)
In C^alpha*: H = U*_aU*_a' (notes v7) and K' := U*_v2U*_t (apex v1: 2F3S with fours v2, t). m^H_v = m^H_t = 3,
m^K'_a = 3, so [G : H cap K'] = 9. z avoids the cells of g*_v1K', g*_v2K' (triple a, v, z), so U*_z subset K'; then
N_z = n_z m^H_z / 9 forces m^H_z = 3 and N_z = 2^(E+1) w_z (no factor 3), so the triple a, t, z also has all gcds 2:
z meets no cell. Contradiction.

## Remaining sub-cases
K_{2,3}: exactly one of alpha_tv1, alpha_tv2 equals 1. Case B: exactly one of alpha*_tv1, alpha*_tv2 equals 1 (LFC at t
forbids both = 1). There the apex-v count gives K' = <U_v, U_t> of index 3 or 6.
