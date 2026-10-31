# No scalar mixed-left PSD certificate for the entire 446 full target

**MathKacMoody-2 / math-3.** Native clock before this additive write: **Wed Oct 28 19:33:32 PDT 2026**. New exact-program-assisted negative result at the pinned full target; mathematical/independent scientific review is pending. It is NOT a parent/formal/kernel/human/independent-model verdict, an original D3 kernel, a non-Serre witness, or a novelty/priority claim.

## 1. The exact ALL-real-gamma statement

Use the entire independently tree-versus-suffix-replayed 1780-target-word/162-source `(4,4,6)` pencil of `frontier-20261028-level6-446-full-target-accretivity-obstruction-v1.md`, SHA `9f33be3c50520ae08deeb6cb318b00e959e0e2e8e8d82ef7442cf06a741d3ac0`, at its named full-Cartan/free-Levi/PBW inputs. In the unweighted rational tensor-word host write

\[
D=A+mL+dK,\qquad A=D(6,6),\quad L=B+C,\quad K=B-C.
\]

For a REAL scalar `gamma`, define a proposed mixed-left test `X_gamma=L+gamma A` and the two real symmetric forms

\[
M_0(\gamma)=X_\gamma^TA+A^TX_\gamma,
\quad M_L(\gamma)=X_\gamma^TL+L^TX_\gamma.
\]

**Exact result:** there is NO real gamma for which BOTH `M0(gamma)` and `ML(gamma)` are positive semidefinite. In particular, the successful type125 proof using `L+A/50` cannot be transplanted as ANY scalar multiple `L+gamma A` on this full 446 target. This does **not** say the original D3 map has a kernel or that any other left operator/metric is impossible.

## 2. Two exact signs at gamma=1/5 and all-gamma deduction

Set

\[
G_0=L^TA+A^TL,\quad G_A=2A^TA\succeq0,\quad G_L=2L^TL\succeq0.
\]

Then `M0(gamma)=G0+gamma G_A` and `ML(gamma)=G_L+gamma G0`. Two independently replayed exact integer computations show

\[
\det(5G_0+G_A)<0,\qquad \det(5G_L+G_0)<0.\tag{1}
\]

These are the two whole 162×162 forms at `gamma0=1/5`, scaled by the same positive factor; no floating eigenvalue estimate is involved. A negative determinant of a real symmetric matrix gives a strictly negative direction. Choose u with `u^T M0(gamma0) u<0`. Since `G_A` is positive semidefinite, for EVERY `gamma<=gamma0`,

\[
u^TM_0(\gamma)u=u^TM_0(\gamma_0)u+(\gamma-\gamma_0)u^TG_Au<0.
\]

Choose v with `v^T ML(gamma0) v<0`. Because `G_L` is positive semidefinite and gamma0>0, necessarily

\[
v^TG_0v=\frac{v^TM_L(\gamma_0)v-v^TG_Lv}{\gamma_0}<0.
\]

Hence for EVERY `gamma>=gamma0`,

\[
v^TM_L(\gamma)v=v^TM_L(\gamma_0)v+(\gamma-\gamma_0)v^TG_0v<0.
\]

Together the two half-lines cover ALL real gamma, including their common endpoint. Thus the impossibility is a proof for the entire scalar-gamma family, not extrapolation from the separately recorded finite gamma scans. The argument only rules out this simultaneous PSD certificate under the stated fixed Euclidean coordinate pairing.

## 3. Exact full determinant certificates and independent CRT replay

The earlier complete full-target source lists all **1780 target rows** and all **263594 nonzero L/K/E source-column triples**; a separate tensor-suffix program matched EVERY entry to the tree-Jacobi producer. The first exact gamma1/5 program evaluated `5G0+G_A` by blocked, overflow-bounded int64 Gram products and arbitrary-precision fraction-free elimination: its first161 leading pivots were positive and the full determinant was negative. The second evaluated the previously untested `5G_L+G0`; its first161 pivots were positive and the full determinant was also negative. Scaling by the common positive `5*10368^2` does not change either sign.

A separately written CRT replay reconstructs BOTH full integer Gram matrices from all1780 target rows, performs exact modular elimination with **672 distinct small primes**, checks each residue against the claimed integer, and proves their product exceeds twice an exact row-L1 determinant bound. The product has 9969 bits; twice the bound has 9955 bits. Thus equality and negative sign of BOTH listed determinants are exact, not probabilistic. NumPy int64 modular products remain below `2^30` and blocked Gram sums are guarded by strict `<2^63` bounds; there are no floats. The source/tree-suffix and modular paths share some generic local helpers and are not independent-model/human/formal verification.

| Owner-root artifact | LF | SHA-256 |
|---|---:|---|
| `frontier-20261028-level6-446-mixed-left-gamma-case.py` | 59 | `f4def0913020ff7a3382b7da636a8d1d1bdc73b731f5d4253605c929979bc139` |
| `frontier-20261028-level6-446-gamma1over5-case-v1.json` | 23 | `0e9107c6405512746322b08e8b59aef624e870631c822f5cba7b79463541a7c2` |
| `frontier-20261028-level6-446-gamma1over5-leading-test.py` | 42 | `5c75f418d065dba7cde4809ad5f6692003bf3ac22dbddffc731c00c47e84e8e2` |
| `frontier-20261028-level6-446-gamma1over5-leading-test-v1.json` | 22 | `7e243636caf73d8ce8c8eb8985dbbf831d9d212f8a8e8d1a5f2804537e50a47b` |
| `frontier-20261028-level6-446-allgamma-obstruction-CRT-replay.py` | 63 | `07f9bec294036df79b3c1ffedf7fbc95001451ba2db949eee6f0ce0195849b92` |
| `frontier-20261028-level6-446-allgamma-obstruction-CRT-replay-v1.json` | 695 | `2d4b07128a914feecae4cacda1ae832e04a22caa6f4c7959458739f3612d5e9d` |
| full-target source `frontier-20261028-level6-446-full-target-pencil-v1.json` | 1590481 | `f4289288531b1b8aa169121c5709968924a075b4b7e749874c75ae7ab53331f3` |
| full-target independent replay `frontier-20261028-level6-446-full-target-independent-replay-v1.json` | 16 | `f5fd59388b4c8b92f1fb9d948cd11e1cdb469dab1cea1f67b985adbd3084b828` |

Actual gamma1/5 baseline test returned at **19:27:40 PDT**, its leading test at **19:31:43 PDT**, and the separate two-determinant CRT replay returned `PASS exact both 162x162 negative determinants: 672 primes, modulus bits 9969 bound bits 9955` at **Wed Oct 28 19:33:09 PDT 2026**.

## 4. What this does NOT say

The result excludes only the specific family `X_gamma=L+gamma A` with this FULL unweighted word-coordinate pairing and the simultaneous-PSD proof route. Another nonscalar source transformation, another positive target weighting, a parameter-dependent left operator, multiple-minor algebra, or a wholly different argument is not excluded. The negative directions are not zeros of D3, not integer-parameter counterexamples, and not assertions about the intrinsic invariant form of the nonsymmetrizable algebra. The separate explicit cofactor cone remains at its own UNREVIEWED inputs and staged replay. The earlier incidental cone-status methodological exposure and ALL historical ZERO/STOP/HOLD/process qualifications remain unchanged.

**END — exact no-real-gamma result for one specified full-target PSD method, not a kernel.**
