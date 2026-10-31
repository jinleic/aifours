# Exact original-channel obstruction to coordinatewise spectral domination

The following genuinely four-partite-entangled **physical original-channel output** satisfies
\[
 \lambda_2(\Lambda_p(\rho))>\lambda_2(\Lambda_p(|0000\rangle\langle0000|)),
\]
while its original **top-three sum is strictly below** the product reference. Thus an attempted proof of k3 majorization cannot demand term-by-term domination of the sorted eigenvalues. This is **not** a violation of majorization or of the original k3 inequality, and it does not resolve the unrestricted target. No novelty or independent-family/formal review is claimed.

## Actual input and exact second-eigenvalue certificate

Let
\[
 |\psi\rangle=\frac{10|0000\rangle+|0011\rangle+|0101\rangle+|1111\rangle}{\sqrt{103}},
 \quad \rho=|\psi\rangle\langle\psi|,\quad p=\frac15.
\]
This is an actual normalized rank-one density. Exact Schmidt coefficient-matrix ranks are `(2,2,2,2)` for the four one-versus-three cuts and `(3,3,3)` for the three representative two-versus-two cuts, so the input is genuinely four-partite entangled.

The pure product reference has single-qubit output eigenvalues \(a=9/10,b=1/10\). Its second output eigenvalue is
\[
 \lambda_2(\sigma_*)=a^3b=\frac{729}{10000},
\]
and its top-three sum is \(a^4+2a^3b=8019/10000\).

Define the two orthogonal actual vectors
\[
 u=|0000\rangle,\qquad w=20|0010\rangle+20|0100\rangle+3|0111\rangle,
 \quad\langle w,w\rangle=809.
\]
For the actual original output \(\sigma=\Lambda_{1/5}(\rho)\), exact rational channel evaluation gives
\[
\begin{aligned}
 \langle u|\sigma|u\rangle&=\frac{656263}{1030000},\\
 \frac{\langle w|\sigma|w\rangle}{809}&=
 \frac{60788583}{833270000}
 =\frac{729}{10000}+\frac{108}{2083175},\\
 \langle u|\sigma|w\rangle&=0.
\end{aligned}
\]
The compression of \(\sigma-(729/10000)I\) to the span of \(u,w\) is strictly positive definite. By the finite-dimensional min–max principle, \(\lambda_2(\sigma)\ge60788583/833270000>729/10000\). This exact strict lower bound uses one actual state and a two-dimensional subspace; no floating threshold or nonphysical block is involved.

A corresponding actual rank-three orthogonal projector is
\[
 P=|u\rangle\langle u|+\frac{|w\rangle\langle w|}{809}
 +|1000\rangle\langle1000|.
\]
It has exact Hermiticity, idempotence and trace3; the checker obtains \(\operatorname{Tr}(P\sigma)=650703293/833270000\). The rank-two subspace above is contained in this one actual rank-three projector.

## The original k3 comparison is strictly safe for this witness

The checker independently constructs the **complete original channel** both by the physical Pauli Kraus mixture at \(p=1/5\) and by sequential local partial traces, and verifies their rational matrices are entrywise equal. Exact Hermitian-LDL positivity gives 16 positive pivots for \(\sigma\) and for
\[
 \frac{81}{125}I-\sigma,
\]
so \(\lambda_1(\sigma)<81/125\). Exact congruence-inertia for \((73/1000)I-\sigma\) is `(15 positive,1 negative,0 zero)`; consequently \(\lambda_2(\sigma),\lambda_3(\sigma)<73/1000\). Hence
\[
 \lambda_1(\sigma)+\lambda_2(\sigma)+\lambda_3(\sigma)
 <\frac{81}{125}+2\frac{73}{1000}
 =\frac{397}{500}
 <\frac{8019}{10000},
\]
with exact product-reference gap strictly greater than \(79/10000\). The same state therefore refutes the **stronger pointwise premise** while respecting the target k3 comparison.

For numerical observation only, the original output's top three eigenvalues were approximately `(0.647779137658874, 0.07296386982203326, 0.07222559083117797)`, with sum `0.7929685983120852`; the exact min–max and LDL/inertia statements above, not the decimals, establish the claimed conclusions.

## Evidence and boundary

`frontier-20261028-51-original-pointwise-witness.py` SHA256 `70ee771aff41f5e3ee228eb3daf846b69b8394543c0053b2946cd821dcb7bfb6` ran with single-threaded BLAS and `python3 -B` from repo root, exit0. It checks the exact input/projector, all seven representative cut ranks, the full original Kraus/sequential matrix equality, the displayed positive two-vector compression, the 16 rational LDL pivots and exact 15+/1− inertia. NumPy supplies only the explicitly labelled decimal eigenvalues. It imports the previously pinned exact rational and inertia helper chain.

The separate numerical `frontier-20261028-50-product-hessian-scout.py` SHA256 `f9674390030cbafc00b61c999138c8c5b32e876745462a562daf04a19c239918` tested 500 weight-at-least-two complex directions at each shrinkage `(0.03,0.1,0.25,0.5,0.8)`; its observed positive individual excited-block curvature motivated this example. That finite search is not used as proof.

Native clock after code pins: **Wed Oct 28 18:14:01 PDT 2026**. The example does not prove that every input satisfies k3, that any input violates it, a uniform noise interval, or any novelty claim.
