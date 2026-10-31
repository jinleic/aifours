# Global original k5 and k6 from the balanced-rank spin-flip certificate

**HIGH-CONSEQUENCE WRITTEN AUTHOR CANDIDATE — NOT ADOPTED.** This successor proposes the ORIGINAL four-qubit k5 and k6 product-reference comparisons for **every** physical density, every actual complex projector of the required rank, and all `0<=p<=4/3`. It generalizes the rank-six proof in `frontier-20261028-98-rank6-global-k10.md`, SHA256 `05c04b8b093835c2a0fe63e849e2552c012ef1d33a7b35e78a9738ebce0799f2`, without assuming a scientific theorem from a held or unverified historical packet. The new rank-ten and rank-eleven cases are independent written arguments below; all need full disjoint review. This does **not** prove global k3, full output majorization, novelty, formal/kernel/human/stronger-family acceptance, or cure any prior process finding.

## 1. One dual lemma simultaneously at four ranks

For `X` on four qubits let

\[
H_1(X)=\sum_i I_{\bar i}\otimes\operatorname{Tr}_{\bar i}X,
\qquad\widetilde X=Y^{\otimes4}X^T Y^{\otimes4}.
\]

**Lemma.** If `Q` is an actual complex rank-r orthogonal projector and

\[
r\in\{5,6,10,11\},
\qquad H_1(Q)+\widetilde Q\ge(2r-5)I_{16}.\tag{2}
\]

*Proof.* Diagonalize each actual one-qubit marginal of Q by local unitaries, writing it as `(r/2)I+(m_i/2)Z_i` with `m_i>=0`, and put `S=sum_i m_i`. Both sides of (2) are covariant under these local changes. In this basis

\[
H_1(Q)-(2r-5)I=5I+\tfrac12\sum_i m_iZ_i.\tag{3}
\]

For every listed rank, the r-largest eigenvalue sum of `sum_i Z_i` is 12, since the spectrum is `4^1,2^4,0^6,(-2)^4,(-4)^1` and `5<=r<=11`. Hence `S<=12`. For **each** omitted site i, the r-largest eigenvalue sum of the sum of the other three Zs, including the twofold fourth-site multiplicity, is respectively `9,10,10,9` at ranks `5,6,10,11`. Thus

\[
\sum_{j\ne i}m_j\le10,\quad\text{so}\quad m_i\ge S-10\quad\text{for all }i.\tag{4}
\]

If `S<=10`, (3) is already positive semidefinite and so is `tilde Q`. Otherwise set `c=(S-10)/2`, so `0<c<=1`, and `E=|1111><1111|` in the rotated basis. The eigenvalue of (3) at `E` is `-c` and every other computational eigenvalue is at least `-c+min_i m_i>=c`; hence

\[
H_1(Q)-(2r-5)I\ge c(I-2E).\tag{5}
\]

Set `q=<1111|tilde Q|1111>=<0000|Q|0000>`. If `N=sum_i(I-Z_i)/2` and `Pi_1` is the rank-four weight-one projector, then `N>=2I-2|0000><0000|-Pi_1`. Using `Tr Q=r` and `Tr Q Pi_1<=4`,

\[
\operatorname{Tr}(QN)\ge2r-2q-4,
\quad S=4r-2\operatorname{Tr}(QN)\le8+4q,
\quad q\ge(S-8)/4=(1+c)/2.\tag{6}
\]

For any orthogonal projection R, unit `e` and `0<=c<=1`, `R+c(I-2|e><e|)>=0` whenever `<e|R|e> >=(1+c)/2`: in the two-dimensional span of `Re` and `(I-R)e`, its diagonal entries are `1+c-2cq` and `c(2q-1)` and its determinant is `c(2q-1-c)`; the orthogonal complement has `R+cI>=0`. The endpoint `q=1` is immediate. Apply this with `R=tilde Q` and e=`|1111>`, and combine with (5). ∎

The rank-6 lemma is exactly the previous `98` case; the rank-5 and rank-11 three-site spectral bounds are actually 9, but the common bound 10 is sufficient. We make **no** assertion of this proof for ranks 7,8,9 or 12–16, where the relevant spectral cut is different.

## 2. Common-projector erasure coefficients

For a four-qubit density put

\[
H_2(\rho)=\sum_{i<j}I_{\overline{ij}}\otimes\rho_{ij},\quad
F(\rho)=\sum_{i,a}\sigma_i^a\rho\sigma_i^a.
\]

As reconstructed in `98` from the one-qubit spin flip and Pauli twirl,

\[
H_2(\rho)-H_1(\rho)+I
=\rho+\widetilde\rho+\tfrac12F(\rho)\ge\widetilde\rho.\tag{7}
\]

The full identity is also checked exactly in the cited `97` finite example. `H1` and full spin flip are self-adjoint in the trace pairing, so for the SAME actual `Q` from the lemma,

\[
\operatorname{Tr}(QH_2(\rho))
\ge\operatorname{Tr}\rho[H_1(Q)+\widetilde Q]-r
\ge r-5.\tag{8}
\]

Independently, the actual H1 is a convex average of local-unitary conjugates of `sum_i |0><0|_i`. Its spectrum starts `0^1,1^4,2^6`, so for each of the above four ranks

\[
\operatorname{Tr}(QH_1(\rho))\ge2r-6.\tag{9}
\]

Both (8) and (9) apply to the same arbitrary Q and same physical rho.

## 3. Global original k5 and k6

For `0<=p<=1`, set `t=1-p`, `b=p/2`, `a=t+b`. The original four-qubit channel has the exact positive-erasure lower bound

\[
\Phi_p^{\otimes4}(\rho)\ge b^4I+tb^3H_1(\rho)+t^2b^2H_2(\rho).
\]

Equations (8)–(9) imply, for each listed r,

\[
\operatorname{Tr}[Q\Phi_p^{\otimes4}(\rho)]
\ge rb^4+(2r-6)tb^3+(r-5)t^2b^2.\tag{10}
\]

The right side is **exactly** the sum of the product reference's r smallest eigenvalues: one `b^4`, four `ab^3`, and `r-5` copies of `a^2b^2`. Minimize over rank-r Q and subtract from the unit trace. Rank `r=10` yields global original `k=6`; rank `r=11` yields global original `k=5`; rank 6 reproduces k10 and rank 5 k11. Ties and zero p coefficients are covered. At `p=1` all outputs are uniform. For `1<=p<=4/3`, the full-transpose global spin-flip identity bijects actual projectors and preserves the spectrum and product reference, so the same comparison holds. No coefficient inequality is inferred from a different actual Q or from a floating optimization.

The combined author-candidate coverage from this packet and the new global tail packet 94 is `k=1,5,6,10,11,12,13,14,15,16` (some earlier k2/k4 results have their **separate** old parent-supported scopes). These are ordinary written claims pending their own gate; genuinely entangled global k3 and indices 7–9 are **not** closed here.

## 4. Exact finite checks and review limits

`frontier-20261028-99-balanced-rank-tail-check.py`, SHA256 `bc67b4f3e1e2cf7c43e4d62e10e98a0cccc6fd90dc0053bf0c2f828c9b1f0637`, ran with `python3 -B` and single-threaded BLAS, exit0. It constructs two explicit non-diagonal actual projectors, ranks ten and eleven, by including `(24|0000>+7|1111>)/25`, the four weight-one basis vectors, respectively five and six weight-two basis vectors. Exact Gaussian-rational checks establish their rank/idempotence/Hermiticity, both nontrivial `S=7108/625>10`, `c=429/625`, `q=576/625`, and all 16 positive LDL pivots of `H1(Q)+tilde Q-(2r-5)I`. On the actual pure state `(2|0000>+|0101>+|0110>+|1001>+|1010>+|1111>)/3`, the same projectors have exact `(Tr QH1,Tr QH2)=(41054/1875,99743/5625)` at rank ten and `(44804/1875,105368/5625)` at rank eleven, each satisfying (8)–(9).

At both `p=2/3` and `p=4/3`, original Pauli and sequential channel matrices were checked equal exactly. The actual respective Q/reflected-Q output traces were `106364/151875` and `113864/151875`, above the product r-bottom sums `29/81` and `11/27`. Numeric bottom-sum printouts are approximate. These are checks of two projectors and one physical input at two p values, not a universal program proof. Native checker-pin clock `Wed Oct 28 20:12:54 PDT 2026`.

A complete disjoint written review must examine every rank case, local-basis covariance, the one-negative-direction lift with full complex projectors, (7)'s exact four-qubit spin flip, common-Q coefficientwise lower bounds, actual reference multiplicities and all-noise reflection. No reviewer or parent verdict is transferred from 98 or any older index gate.
