# No finite-Butson circulant Hadamard pair in the diagonal Fourier-product branch

**CONDITIONAL WRITTEN COROLLARY, UNREVIEWED.** This is a direct physical-matrix consequence of the exact ratio obstruction `frontier-20261028-mub-all-root-ratio-obstruction-v1.md` SHA **3fac11c5e6f334f543de33bf934b89292df03aba18643efd63659e96fbcd8419** and inherits its explicitly named Lam–Leung small-root-sum import and all pending review. The original unrestricted QLS10 remains open.

Let q be ANY positive integer, let `f=(f_0,...,f_9)` have entries in a single arbitrary-phase coset of the q-th roots, and let

`H_(t,c)=f_(t-c mod10)/sqrt(10)`, `F_(t,c)=exp(2*pi*i*t*c/10)`.

**Claim:** H and H∘F cannot both be unitary. This does not assume maximal cardinality. Arbitrary row and column PHASE gauges of H are also allowed, since they factor out from BOTH H and H∘F. It does NOT allow arbitrary independent row/column permutations while keeping the Fourier coordinates fixed, and does NOT cover noncirculant H.

Proof: if both H and H∘F were unitary, the first column `phi=f/sqrt(10)` would be unbiased to the three fixed Weyl bases I,F/√10,D F/√10, by the exact autocorrelation/chirp equivalence in `frontier-20261028-weyl-mub-qls-equivalence-v1.md` SHA **f063984a0ac5ff0a51e064b8e32eb901ba2e7edaff6e2667e0f6c7f47ad43a5d**. In CRT coordinates, every relative Schmidt ratio `b_t/a_t` is itself a q-th root, contrary to the all-root ratio obstruction. This covers ALL q, not only q=10 or a prime power. A single common overall phase in f cancels from those ratios.

The conclusion is conditional on the cited author proofs and on the published root-sum import, not a new computational exclusion based on the q10 Z3 run (which returned UNKNOWN). It gives no lower bound for arbitrary-phase circulant pairs and does not eliminate general noncirculant H, other transversals or nonproduct quantum Latin squares.
