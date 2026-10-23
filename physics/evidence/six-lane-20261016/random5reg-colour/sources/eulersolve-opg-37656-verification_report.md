# Verification report: OPG-37656

Complete written result: a random n-lift of K5 has chromatic number three
with probability tending to one through all integers n. The exact frozen
K5 concentration proposition is resolved. The broader all-Km extension
in its background is not resolved.

The originating-researcher self-audit checks the sharp scalar inequality,
its equality case, the spectral edge bound, all zero-marginal cases,
the exact factorial sums, full integer-lattice parametrizations, Hessian
positivity and constants, all-n affine shifts, every small-subgraph
conditioning hypothesis, and the odd-cycle lower bound.

The accompanying standard-library checks pass 389 tests identically in
normal Python 3.13 and optimized Python 3.12. No test uses assert. Exact
checks include polynomial certificates, matrix-tree and cycle-lattice
determinants, independent least-norm flow calculations, the nonbacktracking
determinant, all 36 bounded reference arrays, and an exhaustive 46,656-model
three-lift enumeration checked independently against overlap counting.

The exploratory numerical optimizer results are not used to certify the
proof. Finite tests are supplementary; this is not formal verification or
independent peer review. A bounded current literature search did not locate
the exact conclusion; no absolute priority claim is made. The 2021
Nir--Perez-Gimenez moment framework and classical small subgraph
conditioning are explicitly credited. AI assistance is disclosed in prose
in the manuscript, with the author responsible for its contents.
