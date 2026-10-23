# Structural note S2 — twisted reductions for ext1 and a fixed-column restriction lemma (2026-10-19T03:20:50-0700, ContinueCFR21)

Status: written proofs by the worker; UNREVIEWED. Standard arguments; no novelty claimed.
Notation: a (Z_n,k;1)-DM is a set C of n columns in Z_n^k such that for all rows x != y the map
d_xy : C -> Z_n, c |-> c_x - c_y, is a bijection. A twisted element s = (mu, pi, tau) with mu a unit, pi in Sym(k),
tau in Z_n^k acts by (s.c)_x = mu c_(pi^-1 x) + tau_x; it is an automorphism if s.C = C (untwisted: tau = 0).

## 1. ext1 T1 also excludes twisted G6-equivariant seventh rows
Let D be the exact anchor (Sage DM_39_6_1, raw 3c8dbe62...), G6 = <s, z>, s = (16,(012)(345)), z = (-1,id), acting
on the exact column set C (probe a1). Suppose [D; f] is a DM and f(g.c) = mu_g f(c) + tau_g for all g in G6, c in C.
(a) tau is a 1-cocycle: f(gh.c) gives tau_gh = tau_g + mu_g tau_h.
(b) Replacing f by f + a keeps [D; f + a] a DM (every difference D_i - f shifts by -a) and changes tau_g by (1 - mu_g) a.
(c) Take a = tau_z / 2 (2 is a unit mod 39), so tau_z = 0 afterwards. Since sz = zs:
    tau_sz = tau_s + 16 tau_z = tau_s and tau_zs = tau_z - tau_s = -tau_s, hence 2 tau_s = 0, tau_s = 0.
So every twisted G6-equivariant extension is a translate of an untwisted one; T1 (COMPLETE, 0 solutions) therefore
also excludes the twisted case. Same reduction for the subgroups: C2 = <z> by (c); C3 = <s>: the zero column c0 of D
is fixed by s, so f(c0) = 16 f(c0) + tau_s, i.e. tau_s = -15 f(c0), and a = -f(c0) gives tau_s = 0.

## 2. Fixed-column restriction lemma
Let s = (mu, pi, tau) be an automorphism of a (Z_n,k;1)-DM, R = Fix(pi), |R| >= 2, F = {c in C : s.c = c},
d = gcd(mu - 1, n), K = ker(mu - 1) (cyclic of order d).
(i) For x != y in R: d_xy(s.c) = mu d_xy(c) + (tau_x - tau_y). So d_xy conjugates s on C to the affine map
    A_xy : w |-> mu w + (tau_x - tau_y) on Z_n, and |F| = |Fix(A_xy)|, which is 0 or d (Fix(A_xy) is empty or a coset of K).
(ii) If |F| = d > 0: for c in F and x in R, c_x lies in the coset {w : (mu - 1) w = -tau_x} =: t_x + K, and for x != y in
    R the map c |-> (c_x - t_x) - (c_y - t_y) is a bijection F -> K. Hence the |R| x d array (c_x - t_x) is a
    (Z_d, |R|; 1)-DM.
(iii) If two rows x, y in R have tau_x - tau_y in (mu - 1)Z_n, then A_xy has a fixed point and |F| = d; then every pair
    in R has a fixed point, i.e. all tau_x (x in R) lie in one class of Z_n / (mu - 1)Z_n (a group of order d).
Corollary (n = 39). If mu = 1 mod 3 and mu != 1 mod 13, then d = 3 and |Fix(pi)| <= 3 for every k >= 4 DM:
if |R| >= 4, two rows share a class mod 3 (pigeonhole over d = 3 classes), so by (iii) all of R share it and |F| = 3,
and (ii) gives a (Z_3,|R|;1)-DM with |R| >= 4, impossible (N(3) = 2).
Corollary (multiplier-only models, pi = id, twisted or not, k = 7, n = 39). Every unit u mod 39 has u^2 = 1 mod 3, so a
multiplier group M must satisfy: mu = 1 mod 3 implies mu = 1 mod 13. Then mu^2 = 1 for all mu in M, and M is one of
{1}, {1,14}, {1,38} ({1,25} and the Klein group contain 25 = 1 mod 3, -1 mod 13). Large cyclotomic multiplier groups
with all rows fixed are therefore impossible for a seven-row DM over Z39; this is why the planned models move rows.
Corollary (mu = 1). If (1, pi, 0) is an automorphism with |Fix(pi)| >= 2 then d = n, F = C (by (i) with tau = 0), so
c_(pi x) = c_x for all columns: rows x and pi(x) coincide, impossible unless pi = id. (Consistent with model z39_m1,
whose involution fixes exactly one row.)
Scope: restrictions on symmetric models only; nothing here bears on the existence of a seven-row DM over Z39.
