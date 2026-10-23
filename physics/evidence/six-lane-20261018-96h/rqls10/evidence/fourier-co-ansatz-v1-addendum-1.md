# Addendum 1 to evidence/fourier-co-ansatz-v1.md (b3a79dd2a87f8d4477188f91e2777c2afc2efa41e431316b028a6c7e49f844bf)

Recorded 2026-10-19T05:51:19-0700 (from /bin/date). Author ContinueRQLS10b. Written, unreviewed, not parent-accepted. No
code or request change; this fixes how a COMPLETE result of code/fourier_co_enum_v1.py (2b72ec87...83a6) is to be read.

## F7. The full Fourier-type family reduces to FCO(n)
Call a QLS(n) Fourier-type if, after one global unitary and per-vector phases, every entry is
q_ij(t) = omega^(sigma(t) lambda(j) + pi(t) rho(i)) / sqrt n for permutations sigma, lambda, pi, rho of Z_n (the vectors
are characters of Z_n x Z_n restricted to the graph of a permutation). Rows and columns are then automatically
orthonormal (as in F1). A global basis permutation gives sigma = id.
Claim: if a Fourier-type 1-RQLS(n) exists whose resolution B is isotopic to Cay(Z_n) via row and column permutations
(symbol permutations do not change the classes), then FCO(n) has a solution.
Proof. Row permutations of B are absorbed into rho (rho' = rho o tau^-1) and column permutations into lambda, so take
B = Cay(Z_n) with classes {(i, j): j - i = s}. The class-s condition is S_pi(lambda(i'+s) - lambda(i+s), rho(i') - rho(i))
= 0 for all i != i'. For s = 0 the differences (lambda(i') - lambda(i), rho(i') - rho(i)) are exactly the differences of
the graph of psi = rho o lambda^-1 (points (m, psi(m)), m = lambda(i)). Hence S_pi(m' - m, psi(m') - psi(m)) = 0 for all
m != m', which is the FCO(n) condition for the pair (pi, psi). QED.
(Equivalently: with alpha = lambda o tau_1 o lambda^-1, an n-cycle, the family needs psi o alpha^s in C_pi for all s,
where C_pi is the set of permutations whose graph has all differences in the zero set of S_pi; FCO(n) is alpha = tau_1,
and s = 0 alone already gives psi in C_pi.)

## Consequences for reading the enumeration
- A COMPLETE FCO(10) enumeration with no solution would exclude every Fourier-type 1-RQLS(10) with a resolution
  isotopic to Cay(Z_10), at any cardinality. This covers the Huang-Li character construction for every labelling and
  the Zhang-Cao construction over G = Z_2 x Z_5 (isomorphic to Z_10 by CRT; their T_c = {(i, i + c)} is Cay(G)) for every
  map mu, not only complete mappings. It says nothing about non-Fourier-type squares or other resolutions (e.g.
  Cay(D_5)). Scope remains: restricted, one implementation, unreviewed.
- If FCO(10) has solutions, F7 does not by itself produce new ones; the found (pi, rho) are the Fourier-type squares with
  lambda = id, and maximality is decided exactly by R1/R2 in the probe.
