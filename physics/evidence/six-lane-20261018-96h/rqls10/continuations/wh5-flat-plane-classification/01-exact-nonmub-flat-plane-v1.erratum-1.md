# Erratum 1 to 01-exact-nonmub-flat-plane-v1.md (f41c5326ad103fb1afeed3369fdd0b22632d6b6cd407eb9064575c9dd438cdbe)

Recorded after actual `/bin/date`: 2026-10-19T17:32:18-0700. Author ContinueRQLS10b. Found by the author's re-read of the
frozen file before delivery; the frozen file is not edited. No result changes.

E1 (scope of Lemma 4(b), used in Proposition 9(c)). Lemma 4(b) is stated for k in {1, 2, 3}, but Proposition 9(c) also
needs it for the bases beta_X, beta_T and beta_Z. Statement and proof hold verbatim for every k in Z_5: the formula
(X Z^k) psi^k_m = zeta^(2k - m) psi^k_m and the commutation D_u (X Z^k) = zeta^(c - ka) (X Z^k) D_u do not use k != 0, 4;
psi^0 = beta_X and psi^4 = beta_T. For beta_Z directly: D_(a,c) e_t = zeta^(ct) e_(t+a). Since every eigenspace of
X Z^k is one-dimensional, D_u maps each vector of each of these six bases to a unimodular multiple of a vector of the
same basis (diagonal if u lies on the basis' line). This is exactly what Proposition 9(c) uses.

E2 (wording, Lemma 1(c)). "Completing the square" means: for a != 0, a r^2 + b r = a (r + h)^2 - b^2 (4a)^(-1) with
h = b (2a)^(-1), and r -> r + h is a bijection of Z_5, so sum_r zeta^(a r^2 + b r) = zeta^(-b^2 (4a)^(-1)) G(a).
