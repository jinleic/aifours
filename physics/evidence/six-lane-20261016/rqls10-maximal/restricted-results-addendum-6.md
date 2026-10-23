# Addendum 6: R10 (Paley rows times any i-free Hadamard family: no orthonormal transversal)

Written about 15:05 PDT, 2026-10-18. Lane-internal, **unreviewed**, restricted family only. This is a written
argument; no computation was run for it.

## Set-up

- alpha_i = h_i is a row of H = I + iC, the Paley quaternary Hadamard matrix of order 10.
  - C is the symmetric conference matrix over GF(9).
  - Any row or column permutation, and any row or column phase, of H is also allowed. A column phase is a global
    diagonal unitary on all q_ij, so it is irrelevant.
- beta_j is a row of any complex Hadamard matrix of order 10 whose entries, together with their conjugates, lie in a
  subfield F of C with i not in F. Examples:
  - every BH(10,10) matrix, including the Fourier matrix (F = Q(zeta_10));
  - parametric Fourier-type families with phases algebraically independent over Q(zeta_10).
- q_ij = (alpha_i o beta_j)/sqrt10. Rows and columns are ONBs automatically.
- For alpha = Paley and beta = Fourier, all 100 rays are automatically pairwise non-parallel. This is the case that
  motivated the check.

## Claim R10

No transversal {(r, sigma(r))} is orthonormal. Hence no Latin square B makes (B,q) a 1-RQLS(10).

## Proof

**Step 1: the quotients u.**
- u_{ii'} = conj(h_i) o h_{i'} is real (+-1) off {i, i'}.
- At t = i it equals i C_{ii'}, and at t = i' it equals -i C_{ii'}. Here C_{ii'} = +-1 because i != i'.
- With a coordinate permutation, these two positions are moved accordingly.

**Step 2: splitting into real and imaginary parts.**
- Put w = conj(beta_{sigma(i)}) o beta_{sigma(i')}, which has entries in F.
- The class inner product is R + i X, with R = sum_{t not in {i,i'}} u(t) w(t) and X = C_{ii'} (w(i) - w(i')).
  Both R and X lie in F.
- Since i is not in F, {1, i} is F-linearly independent. So orthogonality forces X = 0, i.e. w(i) = w(i').

**Step 3: vanishing principal minors.**
- Let G(a, t) = beta_{sigma(a)}(t), with columns permuted if needed. G is complex Hadamard: G G^* = 10 I and all
  entries are unimodular.
- Step 2 for every pair a != a' says G(a,a) G(a',a') = G(a,a') G(a',a). So every principal 2x2 minor of G vanishes.

**Step 4: a Hermitian Hadamard matrix with unit diagonal.**
- Let D = diag(G(a,a)) and G' = D^{-1/2} G D^{-1/2}.
- G' is complex Hadamard, because D is unimodular diagonal.
- G' has unit diagonal.
- G'(a,a') G'(a',a) = 1 with unimodular entries. Hence G'(a',a) = conj(G'(a,a')), so G' is Hermitian.

**Step 5: trace contradiction.**
- Then G'^2 = G' G'^* = 10 I, so the eigenvalues are +-sqrt10.
- The trace is 10 = (n_+ - n_-) sqrt10. That is impossible in integers. QED

## Scope and remarks

- **What is covered.** R10 covers every beta-family free of i, for alpha in the Paley equivalence class only.
- **R9 vs R10.** R9 handles beta from the Paley class itself, where F contains i, by a different argument (mod-4
  parity). Together, R9 and R10 exclude:
  - Paley x Paley products with any coordinate permutation;
  - Paley x (any i-free Hadamard).
- **Still open.**
  - alpha from the other BH(10,4) equivalence classes, if any;
  - beta containing i but not Paley-equivalent;
  - non-Hadamard-product vector families.
- **Mechanism.** Paley quotients u_{ii'} have exactly two non-real entries, and they are opposite. This forces the
  rigid minor condition.
