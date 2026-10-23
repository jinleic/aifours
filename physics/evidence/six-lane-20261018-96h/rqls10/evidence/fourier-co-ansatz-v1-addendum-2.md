# Addendum 2 to evidence/fourier-co-ansatz-v1.md: any orthonormal transversal of a Fourier-separable array gives an FCO(n) solution (written, unreviewed)

Recorded 2026-10-19T05:56:02-0700 (from /bin/date). Author ContinueRQLS10b. Status: written lemma, unreviewed, NOT
parent-accepted, not part of any GO; it generalises addendum 1 (F7, 9833aedf...56d1, also unreviewed) along the line the
parent suggested at 05:5x. No claim until both reviews (of this lemma and of the FCO(10) enumeration) are complete.

## Setting
Fourier-separable array of order n: q_ij(t) = omega^(sigma(t) lambda(j) + pi(t) rho(i)) / sqrt n, omega = e^(2 pi i/n),
with sigma, lambda, pi, rho permutations of Z_n (t = component, i = row, j = column), up to one global unitary and
per-vector phases (neither affects any inner-product modulus). It is a QLS(n) for all four permutations:
rows <q_ij, q_ij'> = (1/n) sum_u omega^(u (lambda(j') - lambda(j))) = delta (u = sigma(t)); columns
<q_ij, q_i'j> = (1/n) sum_t omega^(pi(t) (rho(i') - rho(i))) = delta.

## Lemma F8 (exact formula, with the sigma relabelling)
Let T = {(i, tau(i)) : i in Z_n} be a transversal (tau a permutation). Put pi' = pi o sigma^-1 and
psi = rho o tau^-1 o lambda^-1. Then the n vectors of T are orthonormal if and only if (pi', psi) is an FCO(n) solution,
i.e. S_pi'(a' - a, psi(a') - psi(a)) = 0 for all a != a', where S_p(x, y) = sum_u omega^(x u + y p(u)).
Proof. For i != i', with u = sigma(t):
<q_(i,tau(i)), q_(i',tau(i'))> = (1/n) sum_u omega^(u (lambda(tau(i')) - lambda(tau(i))) + pi(sigma^-1(u)) (rho(i') - rho(i))).
Relabel the rows by a = lambda(tau(i)) (a bijection Z_n -> Z_n); then rho(i) = psi(a), and the inner product equals
S_pi'(a' - a, psi(a') - psi(a)) / n. The pairs i != i' correspond exactly to the pairs a != a'. QED.

## Consequences (conditional; no claim yet)
- Every resolution class of a 1-RQLS and the diagonal of an idempotent QLS is an orthonormal transversal. Hence, IF
  FCO(n) has no solution, then no Fourier-separable QLS(n) has any orthonormal transversal: no Fourier-separable
  1-RQLS(n) for ANY resolution B (at any cardinality) and no Fourier-separable idempotent or diagonal QLS(n).
- The parent's run RUN/review/rqls10-FCO-parent-run-v1/ (audit parent-audit-v1.json
  f8b5a8e2ec7cf0fae09305b401c7027358099177a6faa7e902f38e09154b5807) reports FCO(n) COMPLETE with no solution for
  n = 2, 4, 6, 8, 10 from ONE producer (code/fourier_co_enum_v1.py 2b72ec87...83a6); the parent is preparing an
  independent exhaustive verification. Until that and a review of F8 exist, the statement "no Fourier-separable
  1-RQLS(10) for any resolution" is a one-producer restricted negative CANDIDATE, not a result.
- Scope: only arrays of the separable form above (all vectors characters of Z_n x Z_n restricted to one permutation
  graph, rows and columns labelled through single permutations). Bicharacters with cross terms, non-monomial vectors,
  and everything outside this family are untouched; the general 1-RQLS(10) question is unaffected.
- Addendum 1 (F7) is the special case of F8 with B isotopic to Cay(Z_n) and the s = 0 class.
