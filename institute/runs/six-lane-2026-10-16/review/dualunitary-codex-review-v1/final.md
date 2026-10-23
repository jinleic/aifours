VERDICT: ACCEPT

No required fixes. Both pinned SHA-256 hashes match.

1. **FATAL findings: none.** The conventions and linear algebra are correct. In [PROOF.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/dualunitary-parent-inputs-r3/PROOF.md:26), lines 26–46 correctly identify
   \[
   M_{12}=U^T,\quad M_{13}=S_9U^RS_9,\quad M_{14}=(U^\Gamma)^TS_9.
   \]
   Both LU covariance formulas hold. Lines 67–98 correctly give a perfect tetracode, a free \(S_3\) action on the 72 off-code points, twelve six-point orbits, and real kernel dimension \(9+24=33\). Lines 105–115 correctly give LU tangent rank \(24+9=33\), including global phase. **Fix: none.**

2. **MAJOR findings: none.** The nonlinear arguments are valid.
   
   In r3, lines 119–134, the implicit-function argument uses a regular subsystem of 129 equations. Its 33-dimensional zero manifold contains the embedded 33-dimensional orbit, making the orbit locally open. This does not assume constant rank of the full constraint map nearby.
   
   In the [addendum](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/dualunitary-radius-addendum-v2.md:22), lines 22–40 correctly use Frobenius weights and obtain
   \[
   \operatorname{spec}(J^*J)=\{0^{33},2^{48},6^{48},8^{33}\}.
   \]
   Lines 50–54 correctly obtain a normal displacement from any nearest orbit point; uniqueness of that point is unnecessary. Lines 58–68 give the exact quadratic expansion and valid inequality
   \[
   \|XX^\dagger\|_F^2=\sum_i\sigma_i^4
   \leq\left(\sum_i\sigma_i^2\right)^2.
   \]
   Consequently, for an exterior gate,
   \[
   \sqrt2\,\delta\leq\|JH\|
   \leq\sqrt2\,\delta^2
   \quad\Longrightarrow\quad\delta\geq1.
   \]
   No smallness assumption is hidden here. The separation is uniform over the orbit. **Fix: none.**

3. **MINOR findings: none.** The scope and imported result are stated correctly. R3 lines 19–22 distinguish the trivial literal reading of [T7](https://arxiv.org/html/2508.04777v3) from approximation by non-2-unitary gates. Lines 138–149 correctly use [44, Theorem 1](https://arxiv.org/html/2212.06737v2): uniqueness covers **all** order-9 2-unitaries, not merely minimal-support examples. Compactness of the exterior set and the characterization \(e_p=1\iff\) 2-unitary then give the qualitative gap. Neither isolation proof requires [44]. **Fix: none.**

**Checks actually run.** All calculations ran in memory with Python `-B`; the checkers’ file-writing entry points were not invoked.

```text
Cut dictionary, LU covariance, swap identities: EXACT PASS
Both cut pairs: group order 6; 12 free six-point orbits
Both Jacobians: rank 129; real kernel dimension 33
LU tangent: exact real rank 33; J*T = 0
Both weighted Gram spectra: {0:33, 2:48, 6:48, 8:33}
G(G-2I)(G-6I)(G-8I) = 0: EXACT PASS
Receipt Jacobian minors: determinant -512, both cases
Receipt tangent minor: determinant 27
Independently built Jacobian and Gram hashes: MATCH
All six parent receipt cases: every saved field MATCH
Integer quadratic-expansion checks: EXACT PASS
Unweighted smallest positive eigenvalue: approximately 1
100 random norm-inequality ratios: maximum 0.529599475347
Rank-one equality control: ratio 1
```

The negative controls also replayed: unitarity alone has kernel 81; the \(d=4\) systems have kernel 136 and tangent rank 61.

**Independent distance tests.** With seed `20261017`, I tested four random controlled-SWAP dual gates, each dressed by random local unitaries, and their four T-dual partners. Unitarity residuals were below \(2.6\times10^{-15}\). The missing-cut singular values give lower bounds independently of the claimed radius theorem:

| Example | Missing-cut lower bound | Fitted orbit distance |
|---|---:|---:|
| SWAP / identity | 3.464102 | 3.464102 |
| Random dual 0 | 2.843130 | 2.879352 |
| Random dual 1 | 2.879151 | 2.904776 |
| Random dual 2 | 2.790603 | 2.828204 |
| Random dual 3 | 2.977695 | 3.007190 |

The T-dual partners gave identical lower bounds and compatible fitted distances. An on-orbit control fitted to \(2.042\times10^{-15}\).

For SWAP and identity, the global distance is **exactly \(\sqrt{12}\)**: the missing-cut singular values \((3,0^8)\) give the lower bound, and an explicit LU image attains it. Further alternating-projection diagnostics produced three approximate dual gates with residuals below \(3\times10^{-13}\), all consistent with the separation.

**Trust limits.** Exact computations use ordinary integer linear algebra, not a proof-assistant kernel. [44] remains an imported theorem. Numerical orbit fits generally provide upper bounds, not certified global minima; the separate missing-cut bounds supply the lower bounds above. This review establishes neither optimality of radius 1, the conjectured \(15/16\) entangling-power optimum, nor novelty. No files were modified, no delegation occurred, and no other review notes or disposition files were read.