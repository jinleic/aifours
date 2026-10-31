# An analytic GME family violating original-channel pointwise \(\lambda_2\) comparison

**Exact author-written obstruction to a stronger proof strategy, not an original k3 counterexample.** For the original local depolarizing channel at physical \(p=1/5\), there are genuinely four-partite-entangled inputs arbitrarily close to a product input whose **second individual output eigenvalue** exceeds the product reference's second eigenvalue. Majorization compares sums, not each eigenvalue; this statement does not prove any original k3 violation. No novelty, independent-family or formal acceptance is claimed.

## Family and exact physical compression

For real
\[
0<|z|<\frac{27}{\sqrt{253}},\qquad
|\psi_z\rangle=
\frac{|0000\rangle+z(|0011\rangle+|0101\rangle+|1111\rangle)}{\sqrt{1+3z^2}},
\quad \rho_z=|\psi_z\rangle\langle\psi_z|,
\]
let \(\sigma_z=\Phi_{1/5}^{\otimes4}(\rho_z)\), with the original channel \(\Phi_p(X)=(1-p)X+(p/2)\operatorname{Tr}(X)I\). Define the actual orthogonal vectors
\[
 u=|0000\rangle,\qquad
 w_z=|0010\rangle+|0100\rangle+\tfrac32z|0111\rangle,
 \qquad \|w_z\|^2=2+\tfrac94z^2.
\]
The product reference has \(a=9/10,b=1/10\) and second eigenvalue \(\lambda_*=a^3b=729/10000\). Direct exact channel algebra gives, for every real z,
\[
\begin{aligned}
\langle u|\sigma_z|u\rangle-\lambda_*
 &=\frac{729-253z^2}{1250(1+3z^2)},\\
\frac{\langle w_z|\sigma_z|w_z\rangle}{\|w_z\|^2}-\lambda_*
 &=\frac{27z^2}{2500(1+3z^2)(2+9z^2/4)},\\
\langle u|\sigma_z|w_z\rangle&=0.
\end{aligned}\tag{1}
\]
Both differences are strictly positive on the displayed range. The span of \(u,w_z\) is therefore an actual 2D subspace on which \(\sigma_z-\lambda_*I\) is positive definite, so min–max implies
\[
 \lambda_2(\sigma_z)>\lambda_2(\sigma_*)=729/10000.
\]
For an explicit actual rank-three projector containing that subspace, take the orthogonal sum of \(|u\rangle\langle u|\), \(|w_z\rangle\langle w_z|/\|w_z\|^2\), and \(|1000\rangle\langle1000|\). No separate optimizers or nonphysical blocks are introduced.

## Why every input here is genuinely four-partite entangled

For \(z\ne0\), on each 1|3 cut the two coefficient rows are linearly independent: one has coefficient1 at the all-zero complementary label while the other has coefficient z at the all-one label. For the 12|34 and 13|24 cuts, the coefficient matrix, up to the corresponding tensor index order and the common normalization, is
\[
\begin{pmatrix}1&0&0&z\\0&z&0&0\\0&0&0&0\\0&0&0&z\end{pmatrix};
\]
for the 14|23 cut it is
\[
\begin{pmatrix}1&0&0&0\\0&z&z&0\\0&0&0&0\\0&0&0&z\end{pmatrix}.
\]
Each has rank3. All seven bipartition Schmidt ranks are therefore greater than1. The family is actual, not merely a formal coefficient assignment, and tends to the pure product input as \(z\to0\).

## Source-level channel identity and exact check

The \(p=1/5\) channel maps diagonal single-qubit matrix units to probabilities \(a=9/10,b=1/10\), and off-diagonal units to \((4/5)\) times themselves. In the ordered basis indices \(2,4,7\), multiplication of the original four local channels gives
\[
10000(1+3z^2)\,\sigma_z\big|_{2,4,7}=
\begin{pmatrix}
729+747z^2&576z^2&576z\\
576z^2&729+747z^2&576z\\
576z&576z&9+2187z^2
\end{pmatrix},
\quad 10000(1+3z^2)(\sigma_z)_{00}=6561+163z^2.
\]
The original input has even computational parity and the channel preserves parity covariance, giving the zero cross terms in (1). Substitution of \(w_z=(1,1,3z/2)\) into the displayed block yields the second equality in (1); the first follows from the displayed \((0,0)\) entry.

`frontier-20261028-53-pointwise-family-check.py`, SHA256 `939bf89a70beed5c162c693cff7aaf7a0a59976bc956f97125465cb583345029`, ran under `python3 -B` from repo root, exit0, exact Fraction/Gaussian-rational arithmetic. It constructs the three coefficient matrices in
\((1+3z^2)\rho_z=R_0+zR_1+z^2R_2\), independently applies BOTH the complete original Pauli Kraus mixture and sequential local channel to each, verifies every matrix entry agrees, and checks the ten displayed coefficient-entry polynomials plus six zero parity-cross polynomials. Its exact coefficient list for the w-Rayleigh difference after clearing positive denominators is `(0,0,27/2500,0,0)`; for the u-Rayleigh difference it is `(729/1250,0,-253/1250)`. Because the unnormalized channel is exactly quadratic in z and w is linear, this is a polynomial identity, not extrapolation from numerical samples.

At \(z=1/10\), the input is the separately checked concrete witness in `frontier-20261028-52-original-pointwise-obstruction.md`: that exact original output also satisfies k3 strictly, via its actual Kraus matrix and rational LDL/inertia certificate. **No assertion about original k3 for other z follows here.** The actual full global k3 problem remains open, including arbitrarily near-product inputs. Native checker-pin clock **Wed Oct 28 18:16:50 PDT 2026**.
