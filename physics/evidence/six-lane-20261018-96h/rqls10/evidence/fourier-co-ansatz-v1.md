# Fourier-type clock-orbit ansatz for B = Cay(Z_n): reduction to spectral pairs of permutation graphs (written, unreviewed)

Recorded 2026-10-19T05:27:55-0700 (from /bin/date; written after the v4 request). Author ContinueRQLS10b. Status:
written restricted analysis, unreviewed, not parent-accepted. Target remains OPEN / UNKNOWN. Nothing here is a claim
about general 1-RQLS(10).

## 1. Ansatz FCO(n)
omega = e^(2 pi i/n), Z = diag(omega^t). For permutations pi, rho of Z_n put g_i(t) = omega^(pi(t) rho(i)) / sqrt n and
q_ij = Z^j g_i, i.e. q_ij(t) = omega^(t j + pi(t) rho(i)) / sqrt n. Resolution: classes C_s = {(i, j): j - i = s}
(B(i,j) = j - i, isotopic to Cay(Z_n)). Huang-Li (arXiv:2606.27758, Theorem "Construction--complete mapping") is the
case rho = id, pi = mu a complete mapping (their transversals T_s = {i - j = s} are our classes).

## 2. Lemmas
F1 (QLS for all pi, rho). Rows: <Z^j g_i, Z^j' g_i> = (1/n) sum_t omega^(t (j'-j)) = delta. Columns: <g_i, g_i'> = (1/n)
   sum_t omega^(pi(t) (rho(i') - rho(i))) = delta because pi is a permutation and rho is injective.
F2 (classes). <Z^(i+s) g_i, Z^(i'+s) g_i'> = S_pi(i'-i, rho(i')-rho(i)) / n with S_pi(a, b) = sum_t omega^(a t + b pi(t)),
   independent of s. Hence FCO(n) is a 1-RQLS(n) iff S_pi(a, b) = 0 for every difference (a, b) of two distinct points of
   the permutation graph Gamma_rho = {(i, rho(i))}, i.e. iff the matrix K_(t,i) = omega^(<(t, pi(t)), (i, rho(i))>) / sqrt n
   (pairing <(t,s),(i,r)> = t i + s r) is unitary: (Gamma_pi, Gamma_rho) is a spectral pair in Z_n x Z_n. The condition
   is symmetric in (pi, rho).
F3 (normalisation). S_(pi + d)(a, b) = omega^(b d) S_pi(a, b), so pi(0) = rho(0) = 0 may be assumed. (u^-1 pi, u rho)
   is a solution with (pi, rho) for every unit u; (pi^-1, rho^-1) likewise (S_(pi^-1)(a, b) = S_pi(b, a)).
F4 (rays). q_ij and q_i'j' (cells distinct) span the same ray iff i != i' and t -> c pi(t) + k t is constant mod n with
   c = rho(i) - rho(i') and k = j - j'. Hence a solution is maximal (n^2 rays) iff there is no c != 0 and k with
   c pi + k id constant ("pi is affine in no direction"; for prime n: pi not affine, Huang-Li's condition (*)).
F5 (n = 10, exact necessary conditions). For 10th roots of unity, omega^m = (-1)^u eta^(3w) with u = m mod 2,
   w = m mod 5, eta = e^(2 pi i/5); as 1, eta, ..., eta^3 are linearly independent over Q, sum_m c_m omega^m = 0 iff
   c[m] - c[m+5] is the same for all even m. With A = pi(evens), S_pi(5, b) = 2 sum_(x in A) omega^(b x) for b != 0, and
   this vanishes iff (b odd, b != 5, and A in {evens, odds}) or (b even, b != 0, and A meets every residue mod 5 once);
   it never vanishes for b = 5. Dually S_pi(a, 5) = -2 sum_(t in pi^-1(odds)) omega^(a t). Since Gamma_rho always has
   differences with a = 5 (pairs (i, i+5)) and with b = 5 (rho is onto), a solution needs: pi(evens) and pi^-1(evens)
   both meet every residue mod 5 exactly once, rho(i+5) - rho(i) != 5 and rho^-1(x+5) - rho^-1(x) != 5 for all i, x.
   (Proof: write the multiset {b x : x in A} in the criterion; for b a unit a 5-element vanishing set must be a coset of
   2Z_10, for b even the 5 values lie in 2Z_10 and must be all of it, for b = 5 the sum is #even - #odd, an odd number.)
F6 (rho = id at n = 10). rho = id requires S_pi(a, a) = 0 for all a != 0, i.e. t + pi(t) a permutation: a complete
   mapping of Z_10, which does not exist. So any FCO(10) solution has rho != id (and pi != id by symmetry).

## 3. Status and plan
FCO(10) is a finite problem: 9! normalised pi times a backtracking search for rho over the exact zero table of S_pi.
A planned small stdlib probe (code/fourier_co_enum_v1.py, exact integer arithmetic; NOT run) enumerates it for n = 2..8
and 10 (n = 9 if time remains), with the F5 prefilter at n = 10 (its equivalence with the direct tests is re-checked on
a random sample), the imports as controls (no solution for n = 2, 4, 6; only 5-ray solutions for n = 5, 3-ray for n = 3;
Huang-Li solutions incl. 14 non-affine normalised complete mappings at n = 7), and an explicit exact Gram check of every
reported square over all 3n lines. A solution at n = 10 would be an exact 1-RQLS(10) (entries 10th roots of unity /
sqrt 10); it is maximal iff F4 holds. Any such output is a CANDIDATE until independently verified; a complete negative
enumeration would be a restricted result for FCO(10) only.
