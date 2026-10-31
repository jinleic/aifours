# Fourier-transversal transpose duality: both Diţă orientations in orders 8 and 10

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Wed Oct 28 23:20:08 PDT 2026**. This is a deterministic consequence of the separately computer-assisted 2×4 and 2×5 theorems; it is not an arbitrary-Hadamard or unrestricted QLS no-go.

## Transpose duality

Let F_n be the symmetric unnormalized cyclic Fourier matrix. A Fourier-product QLS based on a complex Hadamard K has an orthogonal transversal if and only if there exists a column permutation P such that BOTH `H=K P` and the entrywise product `F_n ∘ H` are complex Hadamard. Indeed P chooses the transversal's column for each physical row; the second matrix has exactly those transversal rays as columns.

Taking transposes, `(F_n ∘ H)^T=F_n ∘ H^T`. Therefore the following property is transpose-invariant:

> For every source-row permutation R of K, the Fourier-product QLS based on R K has no orthogonal transversal.

Proof: if some R K^T had a transversal with column permutation P, then `H=R K^T P` and `F_n∘H` would both be Hadamard. Their transposes yield a transversal with identity column assignment for `H^T=P^T K R^T`, which is a source-row permutation of K followed by a column permutation. Column permutation cannot affect existence of a transversal. The reverse implication is identical. This is an all-source-orders statement: no corresponding fixed-source-order equivalence is asserted.

## Application to both Diţă orientations

Consider an order `2m` Diţă construction with an arbitrary m×m complex Hadamard A as the base and arbitrary 2×2 complex Hadamards B_h as the m blocks. Every 2×2 complex Hadamard is equivalent to F2. After column phases and a shared source-coordinate phase, each block has entries `delta_h^t (-1)^(tb)` for t,b∈{0,1}, with arbitrary unit delta_h. Reordering block indices gives the matrix

`[[A, A], [A Delta, -A Delta]] = [[A^T, Delta A^T], [A^T, -Delta A^T]]^T`.

The matrix inside the transpose is a 2×m Diţă matrix (indeed the two m×m blocks coincide). Hence **any theorem covering ALL 2×m Diţă matrices under all source-row permutations also covers ALL m×2 Diţă matrices**, including arbitrary block phases and monomial equivalences.

For m=4 invoke `frontier-20261028-n8-dita-two-arbitrary-blocks-no-transversal-v1.md` SHA **d0c6dac193ab6bde47b2c27b11e1508948ca3d948434a1417591c1898a0d2eee**. For m=5 invoke `frontier-20261028-n10-dita-two-arbitrary-blocks-no-transversal-v1.md` SHA **86539e2b5f2fce4a1924c41105687f289367f1b7f53f38b8cc2e4b5e353cbb50**, including its Haagerup CH5 classification import. Thus both 2×4/4×2 and 2×5/5×2 Diţă orientations yield NO Fourier-product transversal for ANY source-row order, as a conditional written corollary of those unreviewed finite certificates. In particular this closes the 5×2 omission explicitly stated in the order10 predecessor, without modifying it.

## Boundary

Not all complex Hadamards are known to be Diţă; no claim is made for arbitrary K, arbitrary even orders, or unrestricted QLS10. The all-orders premises and classification import require the independent reviews requested in their respective packets; this algebraic transpose caller likewise needs review.
