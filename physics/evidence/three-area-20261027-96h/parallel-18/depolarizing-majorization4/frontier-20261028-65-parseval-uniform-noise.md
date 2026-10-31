# Parseval-sharpened explicit uniform k3 noise interval

**HIGH-CONSEQUENCE CONDITIONAL AUTHOR CANDIDATE — REVIEW THE FULL PREDECESSOR.** Assuming the product-gauge, exact Hessian identities and \(15t/256\) second-order bound in `frontier-20261028-59-uniform-high-noise-k3.md`, SHA256 `6f13422e52e6761a3d0d325df821ca78a721ea9c3ad1c8d321043bf93eeb2752`, the sharpened estimates below propose the explicit uniform interval
\[
 |1-p|\le10^{-7}\tag{1}
\]
for the **original k3 inequality for every actual four-qubit density and complex rank-three projector**. This would improve the predecessor's conservative \(10^{-33}\) to \(10^{-7}\); neither result is admitted here. No all-p, all-k, optimal-constant, independent-model/human/formal or novelty claim is made. Earlier process records remain unchanged.

## Parseval bounds in the product gauge

Use the predecessor's nonnegative shrinkage \(t=1-p\), scaled Hermitian map
\[
\mathcal H_t(X)=\sum_{k=1}^4t^{k-1}\!\sum_{\operatorname{wt}(w)=k}\operatorname{Tr}(X\sigma_w)\sigma_w,
\]
and its product gauge \(\psi=(|0\rangle+\epsilon v)/\sqrt{1+\epsilon^2}\), \(\|v\|=1\), \(v\) supported on weights2–4. Restrict temporarily to \(0\le t\le1/100\), so the predecessor's reference block gaps are still at least \(3/2\).

Let \(X_1=|v\rangle\langle0|+|0\rangle\langle v|\) and \(X_2=|v\rangle\langle v|-|0\rangle\langle0|\). Both are Hermitian with \(\|X_i\|_F^2=2\). Pauli Parseval gives \(\sum_w|\operatorname{Tr}(X\sigma_w)|^2=16\|X\|_F^2\), hence \(\|\mathcal H_t(X_2)\|_F\le16\sqrt2<23\). The weight0 and weight1 coefficients of \(X_1\) vanish, so
\[
 \|V\|_F=\|\mathcal H_t(X_1)\|_F
 \le16\sqrt2\,t\le\frac{16\sqrt2}{100}<\frac14.\tag{2}
\]
Set \(W=\mathcal H_t(X_2)\). The exact normalization remainder has norm at most \(\|V\|+|\epsilon|\|W\|<29\) for \(|\epsilon|\le1\), and the reference \(D\) obeys \(\|D\|\le6\).

For the first anti-Hermitian divided-gap block generator, entrywise division only occurs across distinct reference blocks, so
\[
 \|S_1\|\le\|S_1\|_F\le\|V\|_F/(3/2)<1/6.
\]
Using \(\|[A,B]\|_F\le2\|A\|\|B\|_F\), its second-order coefficient satisfies
\[
\begin{aligned}
\|Q\|_F&\le\|W\|_F+2\|V\|\|S_1\|_F
 +2\|D\|\|S_1\|\|S_1\|_F\\
&<23+2(1/4)(1/6)+2(6)(1/6)^2=281/12<24.
\end{aligned}\tag{3}
\]
The second divided-gap generator consequently has \(\|S_2\|\le\|S_2\|_F<24/(3/2)=16\).

## Explicit block-remainder budget

For \(|\epsilon|\le1/500\), both \(e^{2|\epsilon|\|S_1\|}\) and \(e^{2\epsilon^2\|S_2\|}\) are below2. As in the predecessor, the first unitary conjugation removes first-order off-blocks. Its cubic matrix-remainder coefficient is less than
\[
6(1/3)^3\frac{2}{6}+(1/4)(1/3)^2\frac{2}{2}
+23(1/3)2+29=\frac{4799}{108}<45.
\]
The first-order block-diagonal pinching has norm \(<1/4\). The second conjugation removes the second-order off-blocks; using \(|\epsilon|\le1/500\), its **total** cubic matrix-remainder coefficient is less than
\[
6(32)^2/500+2(1/4)(32)+2(24)(32)/500+45
=\frac{1909}{25}<77.\tag{4}
\]
Both the actual scaled matrix and its block-diagonal approximation remain separated into weight0, weight1 and lower blocks: their perturbations of D have norms respectively below
\[
 \tfrac1{4\cdot500}+\tfrac{23}{500^2}+\tfrac{29}{500^3}<0.001,
 \qquad \tfrac1{4\cdot500}+\tfrac{24}{500^2}<0.001,
\]
well below half the reference gap \(3/2\).

The predecessor's all-complex-direction Hessian calculation gives the rescaled second-order coefficient at most \(-15/16\). Weyl's top-three bound contributes at most three times the matrix remainder. Taking the **actual** product-gauge radius \(\epsilon_0=1/500\),
\[
3(77)\epsilon_0=231/500<15/32.
\]
The same leading-block comparison therefore gives the predecessor's local gap
\[
R_3(p)-K_3(\Lambda_p\rho)\ge\frac{15t\epsilon^2}{512}
\quad(0<t\le1/100,\ 0\le\epsilon\le1/500).\tag{5}
\]
No uniform Taylor remainder is inferred from a finite numerical fit: it is the explicit commutator-norm budget (4).

## Far inputs and mixed states

With \(m\) the maximal squared product overlap, the predecessor proves \(8-L\ge2(1-m)\). If the actual maximizer's gauge has \(\epsilon>1/500\), then
\[
8-L>\frac{2}{250001}>\frac1{250000}=4\cdot10^{-6}.
\]
The same-projector first-order bound has coefficient \(\sqrt{39(15-S)}-5<20\). For \(t\le10^{-7}\), this coefficient times t is below \(2\cdot10^{-6}\), so that far-case original k3 gap is strictly positive. The local case uses (5), product inputs have exactly the reference spectrum, and \(t=0\) is uniform output. Averaging over any finite pure decomposition with one fixed actual P gives the mixed-state result. The exact transpose/spin-flip mirror carries the positive-shrink proof to the physical negative-shrink side.

## Checks and limitations

`frontier-20261028-64-tighter-parseval-check.py`, SHA256 `4f3d72adb52a4249e52913ad8ceeda0a4ffb7a04e6b81f1b9a095cc05e0c3431`, ran under `python3 -B` from repo root, exit0. Exact Fraction arithmetic checked all scalar constants in (2)–(4), the strict \(231/500<15/32\), the far-case comparison, the predecessor's three Hessian identities at exact \(t=10^{-7}\), and one mixed-weight identity. It reports `Q_Frobenius_upper=281/12`, first remainder coefficient `4799/108`, second `1909/25`. The already pinned numerical block audit in `frontier-20261028-61-perturbation-block-audit.py` tests only finitely many ordinary-scale cases, not this universal claim.

The predecessor and this successor require a complete disjoint written audit, particularly of the complex Hessian formulas, exact Pauli norm accounting, both unitary conjugations and their uniform block ordering, and same-P quantifiers. Their finite checks are neither a formal proof nor permission to self-adopt the theorem. Native checker-pin clock **Wed Oct 28 18:37:07 PDT 2026**.
