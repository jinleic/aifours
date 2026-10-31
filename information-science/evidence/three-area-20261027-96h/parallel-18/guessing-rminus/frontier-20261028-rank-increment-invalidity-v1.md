# The conditional projection-rank increment is a binary fiber bound

**Status: WRITTEN linear-fiber argument; scientific review pending.** The exploratory LPs `frontier-20261028-two-syndrome-increment-lp.py` SHA-256 `47c3ef24ba20bf9415442af9026d1232bf1f3b1cd4dcaa81f81a9f0a38c3a261` and `frontier-20261028-two-syndrome-increment-topFD-lp.py` SHA-256 `a3949e03473344218967e27e19572ad3ee6cf7f1867e1c4a2abb6c09aa5d6be6` imposed rows

\[
H(X_i\mid X_A,S)\le r_J(A\cup\{i\})-r_J(A).
\]

These rows are valid in the **fixed-syndrome binary triangle-factor model**, even with arbitrary correlations, by the following linear-fiber argument. Fix `S` and write the ambient factor support as an affine binary linear code. Projection to `A` is a linear map, as is projection to `A union {i}`. Every nonempty fiber over a fixed `X_A` has image on `X_i` equal to an affine coset of the image of the kernel of the first map, of dimension exactly the difference of the two projection ranks. Hence at most `2^(r_J(A union {i})-r_J(A))` distinct values of `X_i` occur in the fiber. Restricting to the support of an arbitrary correlated law cannot enlarge this fiber, giving the claimed conditional-entropy bound.

The implemented rank `r_J(A)=sum_{T in J} min(|A intersect T|,2)` is the projection rank: each fixed-XOR triangle is a two-dimensional affine plane, its projection onto one/two/three of its components has binary rank one/two/two, and distinct factor coordinates form a Cartesian product in the ambient code. These rows may not be transferred automatically to arbitrary nonlinear product supports. The floating LP optima are only proposals: no no-go conclusion follows until an exact dual certificate is reconstructed and checked.

The coarser valid inequalities `H(X_A|S)<=r_J(A)` depend only on the conditional projection support size and remain correct. The earlier rational positive-gap polymatroid in `frontier-20261028-two-syndrome-polymatroid-obstruction-v1.md` SHA-256 `dc4ca13fe4039d867f67934de1767bb206a4270a00dec51fabd4d13e474c156b` uses only those coarse caps; the original-neighbour common-syndrome obstruction also does not rely on rank increments. Scientific status and all previous source errata remain unchanged.
