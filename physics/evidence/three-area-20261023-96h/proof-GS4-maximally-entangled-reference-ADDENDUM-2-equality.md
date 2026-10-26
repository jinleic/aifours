# Addendum 2 — strict positivity and all zero cases in the maximally-entangled-reference family

Last before-creation clock observed: **2026-10-23T13:13:28-07:00**. Status: **CANDIDATE written proof**, dependent on the explicitly stated GSd candidate, not independently reviewed or kernel-verified. No scientific program has been run for this addendum.

## 1. Exact result

Let d>=3, let H1 be any finite-dimensional complex Hilbert space, and let eta be a normalized maximally entangled vector on `C^d⊗C^d`. Suppose C is a complex rank-at-most-two operator on `H1⊗C^d⊗C^d` and its **range** contains a ray `a⊗eta` with a nonzero.

**Theorem EQ (candidate):**

1. `q_3(C)>=0`, as in the reference-ray theorem.
2. If the range of C is **not** contained in `H1⊗span{eta}`, then `q_3(C)>0`.
3. For a nonzero C in this family, `q_3(C)=0` holds if and only if

   `C=P_E⊗|eta><w|`,

   where P_E is an orthogonal projection onto a two-dimensional subspace of H1 and w is a nonzero vector on the other two copy slots. Arbitrary nonzero scalar multiples are included by absorbing the scalar into w.

There is an adjoint version when the **co-range** contains the reference ray: its zero operators are the adjoints of the displayed family. If H1 has dimension below two, no nonzero zero case exists.

This is a classification within the structured reference-ray family, not a classification of every zero or negative rank-two operator in W4. Its explicit zero family is an already-known tensor padding family; the candidate additional content is the exclusion of every other zero case under the reference-ray hypothesis.

## 2. Exact kernel information supplied by GSd

The dependency is `proof-GS4-maximally-entangled-reference-ADDENDUM-1-GSd.md`, SHA-256 `c51a4c9d0665d37d91bd325b6e9771c4591207ffb44eac92beeeadbe7664ff4b`. Its proof gives more than two PSD signs:

`C_d+S_d>0`,

`ker(C_d-S_d)=span{Omega_d}_input⊗(C^d⊗C^d)_output`.

Here C_d is the two-site co-Choi matrix, not the coefficient operator C of the theorem.

To reconstruct the kernel rather than infer it from the finite assay:

- On the Bell-range complement all scalar minus eigenvalues are strictly positive.
- On the identity block, the exact minus form has only the p direction in its kernel.
- On each traceless block, its three positive-square coefficients force `z_minus=0`, `z0=sqrt((d+2)/(d-2))z1`, and `z_plus=-sqrt(2d/(d-2))z1`. In the original Ji coordinates, this is precisely the one-dimensional J2(X) direction.
- The p direction together with all J2(X), Tr X=0, is exactly `ran P_12=span{Omega_d}_input⊗B_output`, of dimension d^2. No additional kernel direction remains.

The plus form is strictly positive on every component, by the positive scalar table, the positive identity-block determinant and the positive traceless principal determinants.

For the first-site reference `|0>`, its one-site matrices satisfy `C0+S0>0` and `C0-S0>=0`, directly from their three reducing-space matrices in the frozen proof. The exact first-site minus kernel is not needed below; only that it is a genuine kernel and that the plus sign has no kernel.

## 3. Kernel of the tensorized co-Choi defect

Let

`T0=C0^(-1/2)S0 C0^(-1/2)`,

`Td=C_d^(-1/2)S_d C_d^(-1/2)`.

They are Hermitian contractions. Their eigenvalues lie in `(-1,1]`, because the plus signs are strictly positive. An eigenvalue of `T0⊗Td` can equal one only when both factors have eigenvalue one; two negative eigenvalues in (-1,0) cannot have product one.

The co-Choi matrix of

`Delta=Lambda_1⊗Lambda_B-M0⊗M_d`

is

`Jhat(Delta)=C0⊗C_d-S0⊗S_d>=0`.

Undoing the congruence gives exactly

`ker Jhat(Delta)=ker(C0-S0)⊗ker(C_d-S_d)`.

Thus, after regrouping input/output slots, every vector in this kernel has its **two-site input factor** in span{eta}. The use of eta instead of the unnormalized Omega only changes a nonzero scalar and not this kernel.

For any positive map E with the co-Choi convention used here, a direct matrix-unit contraction gives

`<z,E(|x><x|)z>=<x⊗z,Jhat(E)(x⊗z)>`.

There is no missing conjugation in this formula: `<x,|b><a|x>=bar(x_b)x_a` is exactly the coefficient of |a><b| in |x><x|.

If `x notin H1⊗span{eta}` and z is nonzero, then x⊗z cannot belong to the displayed kernel: projecting its two-site input factor onto eta-perp leaves the nonzero vector `(I⊗P_eta_perp)x⊗z`. For a PSD Hermitian matrix, a vector outside the kernel has strictly positive quadratic value. Hence

**`Delta(|x><x|)>0` whenever `x notin H1⊗span{eta}`.**

This is positive definiteness of a finite matrix for each such x, not a claim of a uniform gap over every x approaching the common-reference subspace.

## 4. Strictness away from a common two-site range

By local-unitary covariance set the first-site reference to |0>. Extend the reference ray u to an orthonormal basis u,x of the two-dimensional range and write

`C=|u><v|+|x><y|`.

If the range is not contained in `H1⊗span{eta}`, its second basis vector x has a nonzero component outside that subspace. Rank two implies y is nonzero. The switched complement equals `Delta(|x><x|)` and is strictly positive by Section 3.

The exact square completion is

`q_3(C)=||A_u^(1/2)(v+A_u^(-1)L†y)||^2`

`         +<y,(D-L A_u^(-1)L†)y>`.

The second term is strictly positive. Thus q3(C)>0. Rank-one nonzero operators already have a strictly positive rank-one swap bound, at least `||C||_HS^2/8`; they cannot be zero exceptions.

## 5. Direct classification on the remaining common-reference range

It remains to classify rank-two C with `ran C subset H1⊗span{eta}`. Choose an orthonormal basis a0,a1 of its two-dimensional first-site range E and extend it to a full basis of H1. Write

`C=Σ_(alpha=0)^1 |a_alpha⊗eta><v_alpha|`,

`v_alpha=Σ_i |a_i>⊗v_(alpha,i)`.

Set `A_eta=Lambda_B(|eta><eta|)>0` and `||v||_A^2=<v,A_eta v>`. For every v the two-copy rank-one form satisfies

`q_2(|eta><v|)=||v||_A^2`,

by the same swap contraction. Separating the first-site partial trace in q3 gives exactly

`q_3(C)=Σ_(alpha,i)||v_(alpha,i)||_A^2`

`             -(1/2)||v_(0,0)+v_(1,1)||_A^2`

`       =(1/2)||v_(0,0)-v_(1,1)||_A^2`

`             +Σ_((alpha,i) notin {(0,0),(1,1)})||v_(alpha,i)||_A^2`.

Every coefficient and the factor one half are explicit. A_eta is positive definite, so equality holds if and only if all off-diagonal vectors vanish and `v_(0,0)=v_(1,1)=w`. Substituting back gives exactly

`C=(|a0><a0|+|a1><a1|)⊗|eta><w|=P_E⊗|eta><w|`.

Conversely every displayed operator has rank two when w is nonzero and has q3=0: the form factorizes, and the one-copy value on an orthogonal rank-two projection is `2-(1/2)·4=0`. This verifies both directions and excludes a mere necessary-condition classification. The adjoint identity q3(C†)=q3(C) gives the co-range version.

## 6. Why this matters and what it does not do

Within the new maximally-entangled-reference class, any nontrivial zero is already a simple two-state first-slot projection with common two-site range. Every operator in that class outside this padding geometry is strictly positive. In particular the full-local-support, product-ray-free separating example from checkpoint 001 is strict, consistently with its direct value 59/36.

This does not extend positivity to arbitrary two-planes, arbitrary biseparable references or generic three-copy operators. It gives no uniform neighborhood size and no conclusion that a generic rank-two plane contains a maximally entangled biseparable ray. The primary unrestricted W4 target remains NOT PROVED. The proof depends on the unpromoted GSd algebra and requires independent reconstruction of both it and this kernel/strictness argument. Novelty is separate; the known padding equality family is attributed rather than presented as a discovery.
