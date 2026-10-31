# An open noise/input region violating pointwise \(\lambda_2\) domination

**Exact author-written strengthening of the original-channel auxiliary obstruction.** It refutes the stronger idea that each sorted output eigenvalue is individually bounded by its product-reference counterpart. It is **not** a counterexample to k3 or to majorization, makes no claim about the original k3 comparison for every input below, and is not novelty/formal/independent-family acceptance.

## Statement

For every
\[
 \frac{\sqrt{17}-1}{4}<q<1,\qquad p=1-q,\qquad
 a=\frac{1+q}{2},\ b=\frac{1-q}{2},
\]
and every real z satisfying
\[
 0<|z|<\sqrt{\frac{a^3}{b(3a^2+ab+b^2)}},\tag{1}
\]
take the actual pure input
\[
|\psi_z\rangle=\frac{|0000\rangle+z(|0011\rangle+|0101\rangle+|1111\rangle)}{\sqrt{1+3z^2}}.
\]
Then \(0<p<(5-\sqrt{17})/4\) is physical, every \(\psi_z\) is genuinely four-partite entangled, and
\[
 \lambda_2(\Phi_p^{\otimes4}(|\psi_z\rangle\langle\psi_z|))>a^3b
 =\lambda_2(\Phi_p^{\otimes4}(|0000\rangle\langle0000|)).\tag{2}
\]
The region is open and contains points arbitrarily close to both the pure product input \(z=0\) and noiseless \(p=0\), without including either boundary. The state, parameter and projector are actual; no pointwise violation of a partial-sum inequality is asserted.

## Direct proof with one physical subspace

Put \(N=1+3z^2\), \(\lambda_*=a^3b\), \(u=|0000\rangle\), and
\[
 w=|0010\rangle+|0100\rangle+2qz|0111\rangle,
 \qquad \|w\|^2=2+4q^2z^2.
\]
The original output \(\sigma=\Phi_p^{\otimes4}(\rho_z)\) has zero \(u\)-to-w cross term, since the input has even computational parity and the channel preserves parity covariance. Exact channel multiplication yields
\[
\begin{aligned}
 \langle u|\sigma|u\rangle-\lambda_*
 &=\frac{q\,[a^3-b(3a^2+ab+b^2)z^2]}{N},\\
 \frac{\langle w|\sigma|w\rangle}{\|w\|^2}-\lambda_*
 &=\frac{2abq(2q^2+q-2)z^2}{N(2+4q^2z^2)}.
\end{aligned}\tag{3}
\]
The first expression is positive exactly under (1); the second is positive for the displayed q because \(a,b,q>0\) and \(2q^2+q-2>0\). Thus the compression of \(\sigma-\lambda_*I\) to the actual span of \(u,w\) is positive definite; the min–max principle proves (2). An explicit rank-three orthogonal projector extending this span is the sum of the projectors onto \(u\), \(w/\|w\|\), and \(|1000\rangle\), which are mutually orthogonal.

All one-versus-three Schmidt ranks are2, and the three representative two-versus-two coefficient matrices have rank3 for every \(z\ne0\), as displayed in `frontier-20261028-54-original-pointwise-family.md`. Hence this is a genuine four-party entangled family, not a nonphysical block or a biseparable input.

## Channel algebra and exact finite verification

With indices \(2,4,7\) and unnormalized denominator N, the exact original output block is
\[
N\,\sigma\big|_{2,4,7}=
\begin{pmatrix}
\lambda_*+(\lambda_*+2ab^3)z^2&q^2abz^2&q^2abz\\
q^2abz^2&\lambda_*+(\lambda_*+2ab^3)z^2&q^2abz\\
q^2abz&q^2abz&ab^3+3\lambda_*z^2
\end{pmatrix},
\quad N\sigma_{00}=a^4+(2a^2b^2+b^4)z^2.
\]
Substituting w and subtracting \(\lambda_*\|w\|^2\) gives the second numerator in (3); the first uses
\(2a^2b^2+b^4-3a^3b=-b(a-b)(3a^2+ab+b^2)\).

`frontier-20261028-70-pointwise-parameter-check.py`, SHA256 `d88862a794dc4174205a14f0ae27b312051c943e835ba1b07cbf50f50b24b589`, ran `python3 -B ...` from the repo root, exit0. The checker independently evaluates the original full Pauli Kraus mixture and the sequential local channel for **all three** z-coefficient matrices at the five exact q values `0,1/4,1/2,3/4,1`: 15 full matrix comparisons. It verifies all ten displayed channel-entry coefficient identities and six zero cross entries at each q. Every such unnormalized entry is a polynomial in q of degree at most4, so equality at five distinct exact q values verifies that listed polynomial identity, not just a numerical sample. It also exactly checks the w numerator `2ab q(2q²+q−2)` and u numerator in (3). Native checker-pin clock **Wed Oct 28 18:44:48 PDT 2026**.

At the concrete previously certified point \(q=4/5,z=1/10\), the original k3 comparison is strictly satisfied by exact rational LDL/inertia bounds in `frontier-20261028-52-original-pointwise-obstruction.md`. No statement about original k3 at other points of this open region follows here. Full mathematical review, novelty and the actual unrestricted k3 target remain open.
