# Addendum 4: R9 (quaternary parity; the Paley Hadamard-product family has no orthonormal transversal)

Written about 14:55 PDT, 2026-10-18, after the exact probe quaternary_paley_probe_v1 (2000 sampled pi, zero
transversal cliques). Lane-internal derivation, **unreviewed**, restricted family only. Per the GO, the probe's own
status remains a sampled UNKNOWN. This addendum is a separate written argument.

Notation:
- For x in {+-1, +-i}^10 write x(t) = i^{a(t)}, with a(t) in Z_4.
- The type vector tau_x in Z_2^10 marks the imaginary entries: tau_x = a mod 2.
- S(x) = sum_t a(t) mod 4.
- <tau, tau'> is the integer count of common 1s.

## Lemma Q (quaternary parity in length 10)

If x is orthogonal to y, then S(y) - S(x) = 2 + wt(tau_x XOR tau_y) (mod 4).

*Proof.*
1. Let h = b - a mod 4, and let n_k be the number of t with h(t) = k.
2. <x,y> = (n_0 - n_2) + i(n_1 - n_3) = 0 gives n_0 = n_2 = A and n_1 = n_3 = C, with A + C = 5.
3. sum_t h(t) = 2A + 4C = 2A (mod 4).
4. wt(h mod 2) = 2C, and 2A = 10 - 2C = 2 + 2C (mod 4).
5. Finally, sum_t h(t) = S(y) - S(x) (mod 4) and h mod 2 = tau_x XOR tau_y. QED

## Corollary Q3

If x_1, x_2, x_3 in {+-1, +-i}^10 are pairwise orthogonal, then

sum_{a<b} <tau_a, tau_b> = 1 + sum_a wt(tau_a) (mod 2).

*Proof.*
1. Sum Lemma Q around the cycle 1 -> 2 -> 3 -> 1. This gives
   0 = 6 + 2 sum wt(tau_a) - 2 sum_{a<b} <tau_a, tau_b> (mod 4), using wt(u XOR v) = wt u + wt v - 2<u,v>.
2. Halve the congruence. QED

The constant 1 comes from n = 10 = 2 (mod 4). For n = 0 (mod 4) the same computation gives sum <tau_a, tau_b> =
sum wt (mod 2).

## R9. Paley product family

**Set-up.**
- H = I + iC, where C is the symmetric conference matrix of order 10 on PG(1,9) (Paley). Its rows h_r satisfy
  h_r(t) = 1 for t = r and h_r(t) in {+-i} otherwise.
- For any permutation pi of the coordinates, set q_ij(t) = h_i(t) h_j(pi(t)) / sqrt10.
- Rows and columns are orthonormal.

**Claim.** For every pi and every permutation sigma, the transversal {(r, sigma(r))} is not orthonormal. So no
Latin square B makes this a 1-RQLS(10), of any cardinality.

*Proof.*
1. Put rho = pi^{-1} o sigma. The entry q_{r,sigma(r)}(t) is imaginary iff exactly one factor is real, i.e. iff
   t lies in {r} symmetric-difference {rho(r)}. So tau_r = {r, rho(r)}, or tau_r is empty when rho(r) = r. Every
   weight is even.
2. For k != l: <tau_k, tau_l> = [rho(l) = k] + [rho(k) = l]. This is the adjacency of the graph G_rho, which has
   maximum degree 2.
3. Ten vertices with maximum degree 2 always contain an independent triple; greedy selection even gives 4.
4. On an independent triple the left side of Q3 is 0, while Q3 requires 1. Contradiction. QED

This matches the probe: 2000 of 2000 sampled pi gave zero transversal cliques.

## Necessary condition for the general quaternary Hadamard-product family (open)

**Set-up.**
- q_ij = alpha_i o beta_j, where alpha_i and beta_j are the rows of quaternary complex Hadamard matrices.
- A_i = tau(alpha_i), B_j = tau(beta_j), and M_ij = <A_i, B_j> mod 2.

**Condition.** Apply Q3 to a class triple, a row triple of H_alpha and a column triple of H_beta, and use
bilinearity mod 2. If {(r, sigma(r))} is an orthonormal transversal, then for every triple {a,b,c}:

sum over ordered pairs x != y in {a,b,c} of M_{x, sigma(y)} = 1 (mod 2).

**Equivalent form.** Put S_xy = M_{x,sigma(y)} + M_{y,sigma(x)}. Then S_xy = 1 + g(x) + g(y) for some
g: [10] -> Z_2.

**Uses.**
- This gives a fast exact filter for any future authorised search.
- For the Paley family, M_ij = [i = pi^{-1}(j)]. There the condition fails, as shown in R9.
- Whether some pair (H_alpha, H_beta) of BH(10,4) matrices passes it, and then yields a 1-RQLS(10), is **open**.
