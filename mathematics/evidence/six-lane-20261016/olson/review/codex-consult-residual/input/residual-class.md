# Exact residual class after T0 (ordered EGZ, D_{2p})

Lane MathOlson, written 2026-10-16 (host clock ~21:50 PDT).  Every statement
below is either a definition or a one-line consequence of the cited proved
results (proof-theoremP.md, proof-dihedral-partial.md, proof-T0.md).  Nothing
here is a coverage claim.

## Notation

p odd prime, w a cyclic word of length N = 4p-1 over D_{2p}, F reflections and
R = N - F rotations.  If F, R >= 1, w is a cyclic alternation
R_1 F_1 R_2 F_2 ... R_k F_k of maximal rotation runs R_i (length a_i >= 1) and
maximal reflection runs F_i (length l_i >= 1).
o_F := #{i : l_i odd},  k_O := #{i : a_i odd},  k_E := k - k_O.
Gaps (between cyclically consecutive reflections): F - k empty gaps (inside
reflection runs) and the k rotation runs.

## Res := words satisfying NONE of the proved sufficient conditions

(E)  EGZ:            R >= 3p-1.
(P)  Theorem P:      F + sum_i floor(a_i/2) >= 3p-1.
(D)  Doubling:       some packed stretch (Sec. 3) exists; in particular (j = 0)
                     some R_i contains p rotations with zero sum.
(V)  Davenport-alpha (F >= 2): R + sum_i floor(l_i/2) >= 3p-1
                     (the empty gaps of distinct runs are non-adjacent, and a
                     run of length l has a non-adjacent set of floor(l/2) of them).
(A)  Lemma A:        some even reflection set Phi with
                     sum_g min(k, mu_Phi(g)) - k + 1 >= p, k = 2p - |Phi|.
(Rg) Theorem R:      all letters in {rho_x, rho_-x, sigma_y}.
(R') Corollary R'.
(T0) Theorem T0:     o_F <= 1.

## Elementary consequences for w in Res (all proved, one line each)

(c1) F >= p+1 and R <= 3p-2                                   [not E]
(c2) F <= 2p-3 + k_O       [not P: sum floor(a_i/2) = (R - k_O)/2]
(c3) R <= 2p-3 + o_F       [not V: sum floor(l_i/2) = (F - o_F)/2]
(c4) o_F + k_O >= 5, and o_F + k_O is odd   [(c2)+(c3), F+R = 4p-1 odd,
                                             F = o_F, R = k_O mod 2]
(c5) o_F >= 2                                                  [not T0]
(c6) every R_i has <= 2p-2 letters and <= p-1 copies of any value [not D, EGZ]
(c7) k >= max(o_F, k_O) >= 3 (from c4, c5: if o_F = 2 then k_O >= 3).

So every word in Res has at least 2 odd reflection runs, at least 5 odd runs in
total, and both letter types between p+1 and 3p-2.

## What a covering argument must do

Prove: every w in Res has an identity 2p-subword.  Planned route (group-algebra
tiling of proof-T0.md): cut w at one "odd unit"; pair the defects (one leftover
letter of each odd run) by units of full depth; rotation defects pair by nests
r[U]r (always full, proved); reflection defects need units with reflections from
two different runs ("brackets" f[S]f' or crossing units).  Combinatorially a
non-crossing same-type pairing of all defects but one always exists (reduction
in the infinite dihedral group Z_2*Z_2: an odd cyclic word reduces to one
letter).  The open part is fullness of the reflection units: finite-exact
degeneracy data (code/bracket_full.py, /tmp-free reruns below) show degenerate
brackets exist (e.g. f rr f with x1+x2 = y_f - y_f' != 0; constant f r^4 f;
sigma_0 rho_1^4 sigma_1^3 at p = 7).  No covering proof yet.
