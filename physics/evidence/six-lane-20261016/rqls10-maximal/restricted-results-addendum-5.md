# Addendum 5: which root-of-unity alphabets carry the n = 2 (mod 4) parity (lead for future searches)

Written about 15:00 PDT, 2026-10-18. Lane-internal, **unreviewed**. This is an arithmetic observation, not a
result about the target.

Consider flat vectors in C^10 with entries in mu_{2^k}, i.e. zeta^{a(t)} with zeta = e^{2 pi i/2^k}.

**Orthogonality.**
- Write h = b - a mod 2^k.
- {1, zeta, ..., zeta^{2^{k-1}-1}} is a Q-basis and zeta^{j + 2^{k-1}} = -zeta^j. Hence sum_t zeta^{h(t)} = 0 iff
  the multiset of h-values is invariant under +2^{k-1}, i.e. it splits into 5 antipodal pairs.

**Sum of exponents.** Let h_1, ..., h_5 be the pair representatives. Then

sum_t h(t) = 2 sum_m h_m + 5 * 2^{k-1} (mod 2^k).

- **k = 2 (quaternary).** sum h = 2 + wt(h mod 2) (mod 4), which is Lemma Q. Its cyclic sum carries the constant 1
  that drives R9 (Corollary Q3).
- **k >= 3 (8th roots and finer).** 5 * 2^{k-1} = 0 (mod 4), so sum h = wt(h mod 2) (mod 4). The cyclic-sum
  constraint becomes sum <tau_a, tau_b> = sum wt(tau_a) (mod 2). That is the same as for n = 0 (mod 4), so it gives
  **no obstruction of R9 type**.
- **k = 1 (real +-1).** There is no real Hadamard matrix of order 10 at all.

**Lead.**
- The R9-type parity obstruction is specific to quaternary alphabets in dimension 10.
- For flat or Hadamard-product families, alphabets containing mu_8, i.e. Q(zeta_8), avoid it. This includes
  BH(10,8) matrices that are not equivalent to quaternary ones. Q(zeta_8) is also the field of source Example 2.4.
- This is not evidence that any such 1-RQLS(10) exists.
