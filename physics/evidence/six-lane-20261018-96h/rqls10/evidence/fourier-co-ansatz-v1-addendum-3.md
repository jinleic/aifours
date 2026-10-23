# Addendum 3 to evidence/fourier-co-ansatz-v1.md: correction of the scope sentence of addendum 2 (written, unreviewed)

Recorded 2026-10-19T05:58:09-0700 (from /bin/date). Author ContinueRQLS10b. Corrects one sentence of
evidence/fourier-co-ansatz-v1-addendum-2.md (2e4f912433476b543b6c2866829f0e5753869b31b33307687c9d40d5397db010), which is
not edited. Unreviewed; no claim.

Addendum 2 says "Bicharacters with cross terms ... are untouched". That understates the scope of Lemma F8. Correct
statement (Lemma F9):
Let q_ij(t) = omega^(f(t) lambda(j) + g(t) rho(i) + k(t) + l(i, j)) / sqrt n with arbitrary maps f, g, k: Z_n -> Z_n,
lambda, rho: Z_n -> Z_n and l: Z_n^2 -> R/Z (k is a global diagonal unitary, l a per-vector phase). If the array is a
QLS(n), then lambda and rho are injective (two equal labels in one row or column would repeat a vector), and
orthonormality of row i, <q_ij, q_ij'> = (1/n) sum_t omega^(f(t) (lambda(j') - lambda(j))) = 0 for all j != j', forces
f to be a permutation (the histogram of f has vanishing Fourier coefficients at all nonzero frequencies, hence is
uniform); likewise columns force g to be a permutation. So the array is Fourier-separable with sigma = f, pi = g, and
Lemma F8 applies. In particular every bicharacter array q_ij(t) = omega^(B((t, p(t)), (lambda(j), rho(i)))) with B a
bilinear form on Z_n^2 and p a permutation is of this form (f(t) = alpha t + gamma p(t), g(t) = beta t + delta p(t)),
and is a QLS only if both f and g are permutations.
Outside the scope remain: exponents not of the additive form above (e.g. products of a row and a column label, or
non-monomial vectors), and every non-monomial QLS.
