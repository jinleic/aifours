# Global low-tail comparison and conditional full biseparable majorization

**WRITTEN AUTHOR RESULT, UNREVIEWED.** For **every** `n>=1`, every actual n-qubit density, every physical qubit depolarizing parameter `0<=p<=4/3`, and every `1<=ell<=n+1`, the sum of the `ell` smallest original output eigenvalues is at least the corresponding product-reference sum. Equivalently, all original upper prefixes `k=2^n-ell` for these ell are product-bounded (with `k=0` the trivial empty prefix). In particular, for arbitrary four-qubit physical inputs this gives original indices **11,12,13,14,15**, and trace equality gives 16. This theorem says nothing by itself about the open global index3.

**Separate conditional consequence:** if the named previously parent-supported three-qubit ORIGINAL prefix-2 and prefix-3 result is imported at its stated ordinary-written boundary, then the whole three-qubit output is product-majorized at every index, and every four-qubit **BISEPARABLE** density has the full original output majorization at all 16 indices. This extends the earlier all-BISEP index3 application, but neither the inherited proof nor this new consequence has been freshly reconstructed by an independent reviewer here. No global GME majorization, novelty, human/formal/kernel/stronger-family acceptance, or process-history cure is claimed.

## 1. Exact Loewner lower bound

Write `Phi_p(X)=(1-p)X+(p/2)Tr(X)I_2` and `Lambda_p^(n)=Phi_p^tensor n`. For `0<=p<=1`, set

\[
 t=1-p,\qquad b=p/2,\qquad a=t+b=(1+t)/2.
\]

Let `E_i(X)=I_i tensor Tr_i(X)/2`, restoring tensor order, and `E_S=prod_{i in S}E_i`. These maps commute and send positive operators to positive operators. For every actual density `rho`, expanding all n local channels and keeping only the terms with exactly n and n-1 erased sites gives

\[
\Lambda_p^{(n)}(\rho)\ge
 b^n I_{2^n}+tb^{n-1}\sum_{i=1}^n
 I_{\bar i}\otimes\rho_i,\qquad \rho_i=\operatorname{Tr}_{\bar i}\rho.\tag{2}
\]

Every omitted term is positive; the factor `tb^(n-1)` follows because the `(2b)^(n-1)` expansion coefficient cancels `2^(n-1)` in the erased-state normalization. At `b=0`, `n=1`, and `t=0`, the same identity is interpreted in the obvious integer-power sense; no inverse is used.

Put `H=sum_i I_bar_i tensor rho_i`. Diagonalize each `rho_i` and express it as a convex combination of its two orthogonal pure eigenstates. Taking product weights across the independent local decompositions expresses H as a convex combination of operators locally unitarily conjugate to

\[
H_*=\sum_i I_{\bar i}\otimes |0\rangle\langle0|_i.
\]

The spectrum of `H_*` begins with one zero and n ones. For **any one actual rank-ell projector Q**, the minimum-trace variational principle therefore gives

\[
\operatorname{Tr}(QH)\ge\ell-1,\qquad 1\le\ell\le n+1.\tag{3}
\]

This argument does not assume independent or compatible chosen marginals: the marginals are those of the given `rho`, and their convex eigen-decompositions only bound the displayed sum.

Trace (2) against the same `Q`, and then minimize over `Q`. We obtain

\[
\sum_{j=2^n-\ell+1}^{2^n}\lambda_j^{\downarrow}(\Lambda_p^{(n)}\rho)
\ge \ell b^n+(\ell-1)tb^{n-1}.
\tag{4}
\]

For a pure product reference, the bottom `ell` eigenvalues are `b^n` once and `ab^(n-1)` `ell-1` times (ties allowed), giving equality in (4). Unit trace converts this into the claimed upper-prefix comparison.

For completeness, the same nonnegative erasure expansion also proves the global index-one comparison: `E_S(rho)=2^{-|S|} I_S tensor rho_barS <= 2^{-|S|}I`, so

\[
\Lambda_p^{(n)}(\rho)\le(t+b)^n I=a^n I.
\tag{5}
\]

At `p=1` every output is uniform. For `1<=p<=4/3`, `p'=2-p` lies in `[2/3,1]`. On **every** n-qubit operator,

\[
\Lambda_p^{(n)}(X)=Y^{\otimes n}\Lambda_{p'}^{(n)}(X)^T Y^{\otimes n},\tag{6}
\]

because `Y X^T Y=Tr(X)I-X` at one qubit. The full transpose and unitary conjugation preserve spectrum also when n is odd; the product-reference spectra agree. Hence (4), (5) cover the whole physical interval.

## 2. Full 3-qubit and BISEP comparison at a named import

**Explicit import, NOT freshly reconstructed:** the parent ordinary-written disposition `institute/runs/three-area-2026-10-23-96h/depol-v27-v29-biseparable-Slater-active-exterior-entire-parent-v1.md`, SHA256 `f9dbeadccd036db0e6f7131aef06c4c84985a6bad84e0b32784081b00653faf7`, supports the complete three-physical-qubit original prefix `k=1,2,3` theorem of `physics/evidence/three-area-20261023-96h/parallel-18/depolarizing-majorization4/depolarizing-k3-whole-biseparable-original-channel-v27.md`, SHA256 `fd14ff4e6065a9ed6f4e39d27cd45f4e1e31df0630ef345a7c86795957ed1dc1`, specifically its §§3–7. The proof uses its named ordinary Slater/Schur-Weyl/S3/S4/PSD facts and exact physical/projector application. Only its three-qubit **k=2,3** statements are needed here; no old withdrawn, held, zero-credit, TC, PAR, scalar optional or extra gate is imported. The parent disposition is ordinary written support, not formal or cross-family certification.

For `n=3`, (4) supplies `k=4,5,6,7`, (5) supplies `k=1`, and `k=8` is trace equality. The imported `k=2,3` therefore complete the three-qubit output majorization for every three-qubit density and every physical p. For `n=2`, (4) alone covers `k=1,2,3` and trace covers 4; for one qubit, (5) and trace suffice.

For any **pure** four-qubit state product across a `1|3` split, the actual output spectrum is the tensor product of the one- and three-qubit output spectra. Each factor is majorized by its corresponding pure product spectrum; the tensor product of their doubly stochastic matrices is doubly stochastic, so the actual four-qubit output is product-majorized at every index. The `2|2` case uses the corresponding unconditional two-qubit conclusion twice. Every biseparable density is a convex combination of such pure product states over the possible physical partitions. Fix one actual rank-k projector while averaging original channel traces; the common product bound is preserved and Ky Fan maximization gives all-index output majorization on the complete BISEP class. This reasoning imports the named **three-qubit prefix theorem**, not the older four-qubit BISEP conclusion, and does not extend it to genuinely four-partite-entangled inputs.

## 3. Actual exact physical example

`frontier-20261028-93-global-tail-check.py`, SHA256 `b55f55dbe358c4242cf900fc11926a187072dfb7eed9ca6342a73c8cf0515e47`, ran under `python3 -B` and single-threaded BLAS, exit0. For the actual pure state

\[
(2|0000\rangle+|0101\rangle+|0110\rangle+|1001\rangle+|1010\rangle+|1111\rangle)/3,
\]

whose genuine four-partite entanglement was separately exact-cut-rank checked in `frontier-20261028-33-simple-frame-witness.py`, the program checked `rho=rho^2=rho^dagger`, trace one, and the actual marginal sum H. Exact Gaussian-rational arithmetic found `spec(H)=(4/3)^1,(5/3)^4,2^6,(7/3)^4,(8/3)^1`, so its smallest-five sum is `8`. At `p=2/3`, it independently assembled both original Pauli and sequential channels and obtained the same exact matrix; exact 16-pivot positive LDL certified both the output and the remainder

\[
\Lambda_{2/3}^{(4)}(\rho)-I/81-H/81>0.
\]

Thus every rank-five complement has actual output trace greater than `13/81`, versus product bottom-five `1/9`; equivalently `K11(actual)<68/81<8/9=K11(reference)`. The single named rank-five complement has trace `11/27`. The exact full-spin-flip identity was also checked against the actual `p=4/3` output; the reflected bound and remainder have 16 positive LDL pivots and the same universal rank-five lower bound, while the same displayed computational rank-five projector has trace `20/81`. Numerical eigenvalue printouts are approximate. These are finite checks for one state at two p values, not a computation of the universal theorem. Native checker-pin clock `Wed Oct 28 20:00:58 PDT 2026`.

The new general Loewner/tail argument and the conditional tensor/convex application require disjoint full written review. The named old import retains its own status and all prior process/cadence/quarantine findings; no earlier gate is retroactively expanded.
