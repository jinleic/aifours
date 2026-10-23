# Addendum 7: rank reformulation of the Hadamard-product family (structural lead, not a no-go)

Written about 15:10 PDT, 2026-10-18. Lane-internal, **unreviewed**.

## Set-up

- q_ij = (alpha_i o beta_j)/sqrt10, where alpha_i and beta_j are the rows of complex Hadamard matrices A and B of
  order 10 (unimodular entries).
- The classes of a Latin square L(i,s) = sigma_s(i) give the transversals {(i, sigma_s(i))}.
- Rows and columns of the square are automatically ONBs.

## Equivalent class condition

The 10 vectors of class s form an ONB iff the square matrix K_s with rows alpha_i o beta_{sigma_s(i)} is unitary up
to scale. That holds iff its columns are orthogonal: for all t != t',

sum_i a_i(t,t') b_{sigma_s(i)}(t,t') = 0,

where a_i(t,t') = conj(alpha_i(t)) alpha_i(t') and b_j(t,t') = conj(beta_j(t)) beta_j(t').

Collect these over s: for every pair t != t',

a(t,t')^T M_{b(t,t')} = 0, where M_b is the 10x10 matrix with (M_b)_{i,s} = b_{L(i,s)}.

## Consequences

- Column orthogonality of A and B gives sum_i a_i = 0 and sum_j b_j = 0. Hence M_b 1 = 0 and 1^T M_b = 0.
- a(t,t') has unimodular entries summing to 0, so it is not proportional to 1.
- Therefore a resolution needs **rank M_{b(t,t')} <= 8 for all 45 pairs {t,t'}**, with a(t,t') in the left kernel
  beyond span{1}.
- The symmetric statement holds with the roles of alpha and beta swapped (transpose the square).

## Calibration against the source construction

- Take L to be the Cayley table of Z_2 x Z_m and b = a character value.
- Then M_b is a group matrix of rank 1. That is why Zhang-Cao Construction 3.3 works when mu is a complete mapping.

## Lead

- For a non-group Latin square L and generic b, one expects rank M_b = 9, which would force failure.
- A Hadamard-product 1-RQLS(10) therefore needs 45 simultaneous rank drops in Latin-square matrices.
- R3, R9 and R10 are instances where these rank drops fail.
- A general theorem excluding all Hadamard-product 1-RQLS(10) is **not** claimed. It is a natural target for later
  written work or a parent-authorised search.
