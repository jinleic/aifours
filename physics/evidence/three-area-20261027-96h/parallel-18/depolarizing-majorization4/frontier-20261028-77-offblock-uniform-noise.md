# Off-block refinement of the uniform high-noise k3 candidate

**HIGH-CONSEQUENCE CONDITIONAL AUTHOR CANDIDATE; FULL DISJOINT REVIEW REQUIRED.** Assuming the exact product-gauge and Hessian proof in `frontier-20261028-59-uniform-high-noise-k3.md` SHA256 `6f13422e52e6761a3d0d325df821ca78a721ea9c3ad1c8d321043bf93eeb2752`, the refined two-conjugation estimates below propose the original k3 inequality for **every** four-qubit density and actual complex rank-three projector throughout
\[
 |1-p|\le9\cdot10^{-6}\quad\text{within }0\le p\le4/3.\tag{1}
\]
This improves the unreviewed `frontier-20261028-65-parseval-uniform-noise.md` threshold \(10^{-7}\), not the full original all-p problem. All predecessor files remain unchanged; no parent adoption, novelty, formal/human or independent-family acceptance is asserted.

## Exact off-block bounds

Use the predecessor's scaled operator \(H_t\), closest-product gauge \(\psi=(|0\rangle+\epsilon v)/\sqrt{1+\epsilon^2}\), and the 0/1/rest computational-weight blocks. The unit v has no weight0 or weight1 component. Restrict temporarily to \(0\le t\le1/1000\). The scaled reference gaps satisfy
\[
 d_0-d_1=2(1+t)^3\ge2,\qquad
 d_1-d_2=2(1+t)^2(1-t)\ge2,
\]
because \(1+t-t^2-t^3\ge1\) on this interval. Also \(\|D\|\le5\).

Let \(X_1=|v\rangle\langle0|+|0\rangle\langle v|\), \(X_2=|v\rangle\langle v|-|0\rangle\langle0|\), \(V=\mathcal H_t(X_1)\), and \(W=\mathcal H_t(X_2)\). Pauli Parseval and absence of weight0/1 coefficients for \(X_1\) give
\[
 \|V\|_F\le16\sqrt2\,t<23/1000.
\]
At \(t=0\), \(W_0=\sum_i(\vec r_i(v)-\hat z)\cdot\vec\sigma_i\). Since each local Bloch vector has length at most1,
\[
 \|W_0\|_F\le16,\qquad \|\operatorname{off}_{0,1,\mathrm{rest}}W_0\|_F\le8.
\]
The second estimate uses that each Z term is diagonal in the three weight blocks; the X/Y terms have squared Frobenius norm \(16\sum_i(r_{ix}^2+r_{iy}^2)\le64\). Orthogonality of Pauli strings also gives
\[
 \|W-W_0\|_F\le16\sqrt2\,t<23/1000,\qquad \|W\|_F<17.
\]
For the first divided-gap generator, \(\|S_1\|_F\le\|V\|_F/2<3/250\). The normalized cubic remainder obeys \(\|R\|<1/5\) whenever \(|\epsilon|\le1/100\), because its exact numerator consists of V plus \(\epsilon W\).

Set \(Q=W+[V,S_1]+\tfrac12[[D,S_1],S_1]\). Frobenius commutator bounds imply
\[
\begin{aligned}
 \|Q\|_F&<16+\tfrac{23}{1000}+2\tfrac{23}{1000}\tfrac3{250}
 +2(5)(\tfrac3{250})^2<17,\\
 \|\operatorname{off}Q\|_F&<8+\tfrac{23}{1000}+2\tfrac{23}{1000}\tfrac3{250}
 +2(5)(\tfrac3{250})^2<81/10.
\end{aligned}
\]
Only off-block entries are used in the second divided-gap generator, so \(\|S_2\|_F< (81/10)/2<41/10\). All these estimates apply to every complex normal v, not just the examples in §4.

## Uniform remainder and far-input bridge

For \(|\epsilon|\le1/100\), the exponential commutator factors in the predecessor are below2. Substitution of the bounds above gives a first conjugation cubic matrix-remainder coefficient below
\[
5(3/125)^3/3+(23/1000)(3/125)^2+2(17)(3/125)+1/5<11/10.
\]
The second conjugation's **total** cubic coefficient is below
\[
5(41/5)^2/100+2(23/1000)(41/5)
+2(17)(41/5)/100+11/10=4767/625<8.\tag{2}
\]
The first-order block-diagonal pinching has norm below23/1000. Both actual and approximating scaled matrices differ from the reference by less than0.002 on this temporary epsilon range, so the 1+4 leading reference blocks remain separated by much more than half their gap2. Weyl bounds the top3 sum error by three times the matrix remainder.

The predecessor's corrected Hessian gives rescaled second coefficient \(\le-15/16\); \(3(8)(1/100)=6/25<15/32\). Therefore for \(\epsilon\le1/100\), \(0<t\le1/1000\), the original top3 gap is at least \(15t\epsilon^2/512\). The case \(\epsilon=0\) is a product input with exactly the reference spectrum.

If the closest-product gauge has \(\epsilon>1/100\), its maximal product overlap satisfies \(m<10000/10001\). The predecessor's actual-marginal union bound gives \(8-L\ge2(1-m)>2/10001\). Its common-P first-order bound has \(\sqrt{39(15-S)}-5<20\), and for \(t\le9/10^6\)
\[
 20t\le9/50000<2/10001<8-L,
\]
so the far case has a strictly positive original k3 gap. Together with product covariance, the exact spin-flip mirror, and the same-P affine mixed-state argument, this gives the conditional claim (1). The constants are conservative; no claim is made about the largest such interval.

## Executed checks and review boundary

`frontier-20261028-75-offblock-constants-check.py`, SHA256 `985ee8bb41dbc3bcfd7a75645200b8e697f2038dc85b64fc0c244ab2fd86e8d9`, ran `python3 -B ...`, exit0. Exact Fraction/Gaussian-rational calculations verified the displayed \(V,W_0,\operatorname{off}W_0,W-W_0,S_1,Q,\operatorname{off}Q,S_2\) Frobenius inequalities on eight actual complex normal directions at \(t=1/1000\) and \(9/10^6\), plus the exact scalar budgets in (2) and the far comparison.

`frontier-20261028-76-offblock-numeric-audit.py`, SHA256 `e86c18787768a2da54d18ceb4e67db139077f747b65f61da8038dbc860020832`, ran with single-threaded BLAS and `python3 -B`, exit0: 90 actual unitary-block numerical cases, `t=0,9e-6,0.001`, \(\epsilon=0.01\); observed maximum \(\|\text{remainder}\|/\epsilon^3\) `0.07230513408977104`, maximum off-Q Frobenius norm `3.1511302592543204`, minimum rescaled k3-gap/\(\epsilon^2\) `7.000484308097299`. These floating examples are **not** a universal proof or extreme-precision certificate. Native checker-pin clock **Wed Oct 28 18:53:25 PDT 2026**.

Full review must cover the entire frozen 59 Hessian/overlap proof AND this source's Pauli/off-block decomposition, norms, exponential error accounting, actual rank-three Ky-Fan ordering and same-P mixed/negative-shrink bridge. No all-p original result or independent novelty assessment follows.
