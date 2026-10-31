# Equality in the 1/142 all-density k3 candidate: exactly pure products away from complete depolarization

Owner PhysicsDepol4-2, physics-2. Actual native clock preceding composition: **Thu Oct 29 09:52:24 PDT 2026**.

**AUTHOR-WRITTEN CONDITIONAL ADDENDUM.** This conclusion requires the complete new uniform-window proof in packet 180, SHA256 `03618f679ca4570c752e693f69464b55faa898a6d3345beee6d11d3fc05bb8e9`. That proof remains unreviewed. No equality theorem is independently admitted by this note; it enlarges no parameter interval. This is not a characterization at p=0 or at arbitrary physical p. No formal/kernel/independent-family/novelty claim is made; Zhang attribution and every earlier scope qualification remain.

## Statement

Assuming packet 180's all-direction tube and far bounds, for every physical p with

`0<|1-p|<=1/142`,

`K3(Lambda_p(rho)) = a^4+2a^3b` holds **if and only if rho is a pure product density**.

For a fixed rank-three Q equality additionally requires Q to be a top-three maximizing projector for that product output. Equality is not automatic for every Q.

At p=1 every density gives I/16 and every rank-three Q gives 3/16, so that endpoint is explicitly excluded from the characterization.

## 1. Nonproduct pure inputs have a strictly positive gap

Let m be the largest squared product overlap and eta^2=1-m. Compactness makes m=1 exactly for product vectors. For nonproduct pure inputs eta>0. Packet 180 yields:

- if `0<eta<=19/80`, gap at least `t eta^2/2000>0`;
- if `eta>=19/80`, gap strictly greater than `31t/3635200>0`.

Thus, conditional on that full proof, no nonproduct pure input has equality for 0<t<=1/142. This conclusion uses the written inequalities, not numerical observations of near-product states.

## 2. Product maximizers lie in affine tangent spaces

First take positive shrinkage p=1-t with 0<t<=1/142. For a product unit vector u=u_1 tensor ... tensor u_4, the one-qubit output has eigenvalues a>b>0. Its tensor output has:

- unique largest eigenvalue a^4 on u;
- second eigenvalue a^3b of multiplicity four, one orthogonal local flip;
- all remaining eigenvalues strictly below a^3b.

Consequently any maximizing rank-three projector Q must contain u and satisfy

`range(Q) subset E_u := sum_(i=1)^4 u_1 tensor ... tensor C^2_i tensor ... tensor u_4`.

This five-dimensional space is the affine tangent space of the product-vector cone; its definition uses all local factor directions, not merely a chosen orthonormal frame.

## 3. Two distinct product tangent spaces intersect in dimension at most two

Let u and v be distinct product rays, and let d be the number of sites where u_i and v_i are linearly independent. Then d>=1. At each differing site choose an invertible complex 2-by-2 map sending u_i to |0> and v_i to |1>; at each remaining site send their common ray to |0>. Their tensor product L is invertible, and

`L E_u = E_(0000)`, `L E_v = E_x`, where x has Hamming weight d.

These are the coordinate spans of the Hamming balls of radius one about 0000 and x. Because both spans use subsets of one common computational basis, their intersection is the span of the basis strings lying in both balls.

- d=1: the two centres are the only common strings, so the intersection has dimension two.
- d=2: the two midpoint strings are the only common strings, again dimension two.
- d>=3: the two balls are disjoint by the triangle inequality, so the intersection is zero.

Invertibility preserves intersections and their dimensions. Hence `dim(E_u intersect E_v)<=2` for any two distinct product rays, including nonorthogonal and arbitrary complex local factors.

In particular, no rank-three projector can maximize the product outputs for two distinct product inputs: its range would have to lie in an intersection of dimension at most two.

## 4. Mixed densities

Suppose the mixed density rho has equality and choose an actual rank-three Ky Fan maximizer Q for its output. In any finite pure-state spectral decomposition `rho=sum_j q_j psi_j psi_j^dag`, fixed-Q linearity and packet 180's universal bound give

`R3 = sum_j q_j Tr(Q Lambda_p(psi_j psi_j^dag))`, with every summand at most R3.

Thus every positive-weight component must itself attain equality. Section 1 forces every such component to be a product ray. Sections 2–3 show that all these product rays must be the same, since the same rank-three Q maximizes each output. Hence rho is a pure product density. The converse follows from the exact product-reference spectrum.

For negative shrinkage the full-transpose spin-flip reflection keeps the input fixed and maps the maximizing Q bijectively. It therefore transfers this equality classification to `1<p<=143/142`, without making an unjustified statement about p=4/3.

## Status boundary

The tangent-space intersection lemma and the fixed-Q mixing implication are exact written linear algebra. The channel equality conclusion is conditional on the entire unreviewed packet 180, including its uniform all-state inequalities, and is not promoted by this addendum alone. Within the older f172-adopted 1/200 interval the same argument applies to the already supported strict pure-state bounds, but any new parent equality disposition still requires its own complete read/reconstruction.
